``django-mfw`` はDjango用モバイルWebサイト開発フレームワークです。以下のような特徴があります

+	ユニコード絵文字と各キャリア絵文字(DoCoMo, KDDI, SoftBank)の変換
+	HTTPのメタ情報(主に ``HTTP_USER_AGENT`` )からのアクセスデバイスの判別
+	各キャリアのIPアドレス範囲からの なりすまし チェック
+	各デバイスに最適なエンコーディングにレスポンスを自動変換
+	デバイス情報による使用テンプレートの自動切り替え(iPhoneでアクセスした場合は ``template/smartphone/iphone/index.html``
	を使用し他は ``template/index.html`` を使用するなど)
+	クッキー不可デバイス用のクッキーベースでは無いセッション管理およびCSRFプロテクション。
	このメカニズムはキャリアのUIDおよびキャリアのIPアドレス範囲を使用します。セキュリティ
	リスク軽減の関係からIPアドレス範囲はキャリアの なりすまし チェックに利用されます。詳しい
	話は **spoofってなんだ** をご覧ください。
+	テンプレート内で絵文字を記述するためのemojiタグ
+	Web経由による各キャリアのIPアドレス範囲の自動更新 (DoCoMo, KDDI, SoftBank)


インストール
=================================================
::

	sudo pip install django-mfw
	
or::

	sudo pip install git+git://github.com/lambdalisue/django-mfw.git#egg=django-mfw


必要なライブラリ(自動でインストールされます)
=================================================
+	`uamd <https://github.com/lambdalisue/uamd>`_ (User Agent Mobile Detector)
+	`e4u <https://github.com/lambdalisue/e4u>`_ (emoji4unicode bundle framework)


使用方法
=================================================

1.	``mfw`` をsettings.pyのINSTALL_APPSに追加
2.	``mfw.middleware.session.SessionMiddleware`` と ``mfw.middleware.csrf.CsrfViewMiddleware`` を ``MIDDLEWARE_CLASSES``
	に追加。その後 ``django.contrib.sessions.middleware.SessionMiddleware`` と ``django.middleware.csrf.CsrfViewMiddleware``
	を *コメントアウト*
3.	``mfw.middleware.device.DeviceDetectionMiddleware``, ``mfw.middleware.emoji.DeviceEmojiTranslationMiddleware`` と
	``mfw.middleware.flavour.DeviceFlavourDetectionMiddleware`` を ``MIDDLEWARE_CLASSES`` に追加。アクセス速度を向上させるために
	``mfw.middleware.device.DeviceDetectionMiddleware`` が他の二つのミドルウェアよりも先に来ていることを確認してください。
4.	``mfw.template.loaders.flavour.Loade`` を **一番最初の項目** として ``TEMPLATE_LOADERS`` に追加
5.	``mfw.core.context_processors.device`` と ``mfw.core.context_processors.flavour`` を ``TEMPLATE_CONTEXT_PROCESSORS`` に追加

下記コードは設定例です。詳しくは `settings.py <https://github.com/lambdalisue/django-mfw/blob/master/mfw-test/src/mfw_test/settings.py>`_ をご覧ください::

	# List of callables that know how to import templates from various sources.
	TEMPLATE_LOADERS = (
	    'mfw.template.loaders.flavour.Loader',
	    'django.template.loaders.filesystem.Loader',
	    'django.template.loaders.app_directories.Loader',
	#     'django.template.loaders.eggs.Loader',
	)
	
	MIDDLEWARE_CLASSES = (
	    'django.middleware.common.CommonMiddleware',
	    #'django.contrib.sessions.middleware.SessionMiddleware',
	    #'django.middleware.csrf.CsrfViewMiddleware',
	    'mfw.middleware.session.SessionMiddleware',
	    'mfw.middleware.csrf.CsrfViewMiddleware',
	    'django.contrib.auth.middleware.AuthenticationMiddleware',
	    'mfw.middleware.device.DeviceDetectionMiddleware',
	    'mfw.middleware.emoji.DeviceEmojiTranslationMiddleware',
	    'mfw.middleware.flavour.DeviceFlavourDetectionMiddleware',
	)
	
	TEMPLATE_CONTEXT_PROCESSORS = (
	    "django.core.context_processors.auth",
	    "django.core.context_processors.debug",
	    "django.core.context_processors.i18n",
	    "django.core.context_processors.media",
	    "django.core.context_processors.request",
	    "mfw.core.context_processors.device",
	    "mfw.core.context_processors.flavour",
	)

使い方
===============================================

デバイス判定
----------------------------------------------------
アクセスしてきたデバイスは ``mfw.middleware.device.DeviceDetectionMiddleware`` によって判定され ``request.device`` にuamd's deviceとして
保存されます。uamd's deviceのインスタンスはデバイスに対する情報を下記のように持っています

+	``device.support_cookie`` デバイスでクッキーがサポートされているかどうか
+	``device.carrier`` デバイスのキャリア名
+	``device.version`` デバイスのバージョン
+	``device.model`` デバイスのモデル名
+	``device.encoding`` デバイスで最適なエンコーディング

.. WARNING::
    使いやすくするためにuamd's deviceは ``AttributeError`` を送信する代わりに ``None`` を返します。したがって以下のコードは予想通りには動きません。::

        if hasattr(device, 'carrier'):
            # code using device.carrier

    ``hasattr(device, 'carrier')`` を使う代わりに **``device.carrier is not None``** を使ってください。


spoofってなんだ
~~~~~~~~~~~~~~~~~~~~
多くのWebアプリケーションが各キャリアのUID(User ID)とIPアドレス情報をセッション管理や認証に使用しています(例: 簡単ログイン)
しかしながら最近ではJailbreakしたiPhoneやAndroid他さまざまなデバイスでテザリングを行うことにより携帯会社のIPアドレスを使用して
携帯用サイトにコンピューターからアクセスすることが可能です。そしてアクセスさえできてしまえばFirefoxのプラグインなどを用いて
HTTPのXヘッダーの書き換えを行えるため、あたかも携帯電話からのアクセスかのように振舞うことができます。

uamd's deviceはキャリア情報を持つデバイスに対して ``device.spoof`` プロパティを提供しています。これはデバイスが判定されたキャリア外の
IPアドレスからアクセスされた場合に ``True`` となります。ほとんどのキャリアはUID取得用のHTTPのXヘッダーをネットワークサーバーで書き換えているため
判定されたキャリアのIPアドレス範囲内からアクセスしているデバイスが送信してくるキャリアのUID情報は信用におけます。

``django-mfw`` ではデバイスの判定に `uamd <https://github.com/alisue/uamd>`_ ライブラリを使用しています。さらに詳しい情報は
そちらをご覧ください。


クッキーベースでは無いSessionとCSRFプロテクション
----------------------------------------------------
セキュリティリスク低減の関係上Djangoのデフォルトではセッションはクッキーに保存されるようになっています。しかしながら
いくつかのデバイスではクッキーをサポートしていないため ``mfw.middleware.session.SessionMiddleware`` ではキャリアのUIDを
セッション保存に利用しています。

このミドルウェアはクッキーをサポートするデバイスに対しては従来通りのクッキーベースのセッション管理を行ないます。UIDを使用するのは
クッキーをサポートしていないデバイスで、そのようなデバイスはたいてい携帯電話なのでキャリアUIDを持っています。セキュリティリスク低減
の関係からキャリアのIPアドレス範囲外からアクセスしてきたデバイスのUIDは信用されません、したがってそのようなデバイスはセッションを保存できません。
セキュリティリスクについては **spoofってなんだ** の項目で説明しているので詳しい話はそちらをお読みください。


ユニコード絵文字とキャリア絵文字の変換
----------------------------------------------------
``mfw.middleware.emoji.DeviceEmojiTranslationMiddleware`` がすべてのことを行ないます。このミドルウェアはデバイスを
判定し(もしくは判定されたデバイス情報を使用し)自動的にレスポンス内部のユニコード絵文字をキャリア絵文字に変換します。したがって
テンプレート内部で絵文字をユニコード絵文字として記述している限りあなたが絵文字に関して気にする必要はありません。ミドルウェアが
相互変換とエンコーディングの変更を自動的に行ないます。

受信データに関してもこのミドルウェアが処理を行ないます。 ``request.GET`` もしくは ``request.POST`` 内部にキャリア絵文字がある場合ミドルウェアは
自動的にそれをユニコード絵文字に変換し、内容をユニコードへとデコードします。

ユニコード絵文字は http://www.unicode.org/~scherer/emoji4unicode/snapshot/full.html で見ることができます。これは `emoji4unicode <http://code.google.com/p/emoji4unicode/>`_ プロジェクト
の一部でありユニコード絵文字とキャリア絵文字の変換はこのプロジェクトの変換テーブルを使用しています。詳しい話は使用している `e4u <https://github.com/alisue/e4u>`_ ライブラリのページをご覧ください。


ダイナミックテンプレート(動的テンプレート)
----------------------------------------
``mfw.middleware.flavour.DeviceFlavourDetectionMiddleware`` はデバイスを判定し自動的にデバイス用の **フレバー** を作成します。
フレバーはテンプレートの名前解決時に接頭辞としてしようされます。したがってもしフレバーが ``smartphone/iphone/1.3`` であり呼ばれた
テンプレート名が ``blogs/post_detail.html`` だった場合は以下のように ``mfw.template.loaders.flavour.Loader`` は読み込みを試行します。
（読み込みには ``TEMPLATE_LOADERS`` の ``mfw.template.loaders.flavour.Loader`` 以外のローダーが順番に使用されます)

1.	``TEMPLATE_DIRECTORY/smartphone/iphone/1.3/blogs/post_detail.html``
2.	``TEMPLATE_DIRECTORY/smartphone/iphone/blogs/post_detail.html``
3.	``TEMPLATE_DIRECTORY/smartphone/blogs/post_detail.html``
4.	``TEMPLATE_DIRECTORY/blogs/post_detail.html``

``mfw.template.loaders.flavour.Loader`` はバンドルローダーなのでロード方法は ``TEMPLATE_LOADERS`` 内のローダーに依存しています。
したがって正しいテンプレートローダーがリストに含まれているか注意してください。


スペシャルサンクス
==================================================================
``django-mfw`` のコンセプトは `django-bpmobile <https://bitbucket.org/tokibito/django-bpmobile>`_
`django-mobile <https://github.com/gregmuellegger/django-mobile>`_ と `emoji4unicode <http://code.google.com/p/emoji4unicode/>`_ に強く影響を受けています。
