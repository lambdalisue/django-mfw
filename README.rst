``django-mfw`` is the frameworks for developing mobile site with Django.

this framework handle

+	Unicode emoji and Japanese emoji (DoCoMo, KDDI, SoftBank) conversion
+	Device detection via HTTP META (mainly HTTP_USER_AGENT)
+	Device spoof detection via carrier CIDR
+	Response encoding via Device
+	Dynamic template changer via Device (like iPhone use ``template/smartphone/iphone/index.html``
	and other use ``template/index.html``)
+	non cookie based session manager for device which doesn't support cookies via carrier UID.
	this mechanism is using carrier UID and carrier CIDR. carrier CIDR is used for checking
	the device spoofness for security reason. see below.
+	non cookie based csrf protection for device which doesn't support cookie. using non cookie based session for storage described above.
+	emoji tag for entering emoji on template
+	automatically update carrier's CIDR via carrier's web site (DoCoMo, KDDI, SoftBank)

Install
=================================================
::

	sudo pip install django-mfw
	
or::

	sudo pip install git+git://github.com/lambdalisue/django-mfw.git#egg=django-mfw


Required (Automatically installed)
=================================================

+	`uamd <https://github.com/lambdalisue/uamd>`_ (User Agent Mobile Detector)
+	`e4u <https://github.com/lambdalisue/e4u>`_ (emoji4unicode bundle framework)


How to use
=================================================

1.	Add ``mfw`` to your ``INSTALL_APPS`` settings in ``settings.py``

2.	Add ``mfw.middleware.session.SessionMiddleware`` and ``mfw.middleware.csrf.CsrfViewMiddleware``
	to your ``MIDDLEWARE_CLASSES`` setting and *comment out* ``django.contrib.sessions.middleware.SessionMiddleware``
	and ``django.middleware.csrf.CsrfViewMiddleware``

3.	Add ``mfw.middleware.device.DeviceDetectionMiddleware``, ``mfw.middleware.emoji.DeviceEmojiTranslationMiddleware`` and
	``mfw.middleware.flavour.DeviceFlavourDetectionMiddleware`` to your ``MIDDLEWARE_CLASSES`` setting. To accelate request
	response, make sure ``mfw.middleware.device.DeviceDetectionMiddleware`` is listed before other two middleware.

4.	Add ``mfw.template.loaders.flavour.Loade`` as **first item** to your ``TEMPLATE_LOADERS`` setting.

5.	Add ``mfw.core.context_processors.device`` and ``mfw.core.context_processors.flavour`` to your ``TEMPLATE_CONTEXT_PROCESSORS`` setting.

The code below describe sample settings. See `settings.py <https://github.com/lambdalisue/django-mfw/blob/master/mfw-test/src/mfw_test/settings.py>`_ for more detail.::

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

Usage
===============================================

Device detection
----------------------------------------------------
request device is detected with ``mfw.middleware.device.DeviceDetectionMiddleware`` and stored in ``request.device`` as uamd's device.
the uamd's device instance has information for the device like below.

+	``device.support_cookie`` is the device support cookie or not.

+	``device.carrier`` the carrier name of the device.

+	``device.version`` the version of the device

+	``device.model`` the model name of the device

+	``device.encoding`` the recommended encoding for the device

.. WARNING::
    Insted of raise ``AttributeError``, uamd's device instance will return ``None`` for convinience.
    That's why the code below woun't work as expect.::

        if hasattr(device, 'carrier'):
            # code using device.carrier
        
    Insted of using ``hasattr(device, 'carrier')``, use **``device.carrier is not None``** for checking.


What is the spoof
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A lot of application use carrier's UID and IP for session or authentification however
it is not secure because Jailbreaked iPhone or Android or whatever can tethering so accessing web site using mobile
ip address is not impossible. And once you could access the web site, you can fake the ``HTTP_USER_AGENT`` or any 
``HTTP X`` headers with Firefox plugin or whatever.

uamd's device which has carrier have ``device.spoof`` property. This will set ``True`` when the device is accessed
from out of carrier's cidr. most of carrier rewrite ``HTTP X`` headers for UID on network server. so if device is 
accessed from correct carrier CIDR, the UID for the carrier is secure.

in django-mfw, device detection is using `uamd <https://github.com/alisue/uamd>`_ library so see it
for more device detection detail.


Non cookie based Session and CSRF protection
----------------------------------------------------
Django default session is saved on cookie because of security reason. However some device doesn't support cookie
so ``mfw.middleware.session.SessionMiddleware`` use carrier's UID for saving session.

the middleware never try to use carrier's UID for device which support cookie. it is only for the device which doesn't support cookie
and commonly such device has carrier's UID. In security reason, device accessed from out of carrier's CIDR (detected from ``HTTP_USER_AGENT``)
is not trusted so it cannot save session if cookie is not supported. The security reason is described **What is the spoof** section
so check out for the detail.


Unicode emoji and Japanese carrier emoji conversion
----------------------------------------------------
``mfw.middleware.emoji.DeviceEmojiTranslationMiddleware`` care it. it detect device and automatically translate unicode emoji to
carrier's encoded emoji in response. That's why you do not need to care the code of emoji. Just write emoji as unicode emoji then
middleware translate everything correctly and encode response to carrier's encoding via ``uamd`` library.

Incoming translation is also handled the middleware. if ``request.GET`` or ``request.POST`` has carrier emoji, the middleware automatically
translate the carrier emojis to unicode emojis and decode value to unicode. 

Unicode emoji is found on http://www.unicode.org/~scherer/emoji4unicode/snapshot/full.html . this is a part of `emoji4unicode <http://code.google.com/p/emoji4unicode/>`_ project
and translation method is using conversion table of it. see `e4u <https://github.com/alisue/e4u>`_ for more detail.


Dynamic Template
----------------------------------------
``mfw.middleware.flavour.DeviceFlavourDetectionMiddleware`` detect device and automatically create **flavour** for device.
the flavour is used for prefix of template_name. so if the flavour is ``smartphone/iphone/1.3`` and called template name is ``blogs/post_detail.html``
then ``mfw.template.loaders.flavour.Loader`` will try to load the file listed below with template loaders listed in ``TEMPLATE_LOADERS`` except oneself.

1.	``TEMPLATE_DIRECTORY/smartphone/iphone/1.3/blogs/post_detail.html``

2.	``TEMPLATE_DIRECTORY/smartphone/iphone/blogs/post_detail.html``

3.	``TEMPLATE_DIRECTORY/smartphone/blogs/post_detail.html``

4.	``TEMPLATE_DIRECTORY/blogs/post_detail.html``

``mfw.template.loaders.flavour.Loader`` is bundle loader and loading method is depended with template loaders listed in ``TEMPLATE_LOADERS``
so make sure you listed correct template loader in ``TEMPLATE_LOADERS``


Special thanks
==================================================================
django-mfw's concept is inspired by `django-bpmobile <https://bitbucket.org/tokibito/django-bpmobile>`_
`django-mobile <https://github.com/gregmuellegger/django-mobile>`_ and `emoji4unicode <http://code.google.com/p/emoji4unicode/>`_
