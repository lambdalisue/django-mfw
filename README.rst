``django-mfw`` is a framework for developping mobile site with Django. The
following feature is available

-   Detect accessing device via HTTP_USER_AGENT and determine the device can
    handle cookie or not.

-   Non cookie based Session and Csrf protection for the devices which cannot
    handle cookies.

-   Dynamically change loading template via the device information. That's
    mean you can prepare the HTML template for each device (flavour template
    system)

-   Encode request and response via detected device encoding. It is required
    because some Japanese mobile phone cannot handle UTF-8

-   Translate Japanese Emoji in request and response to proper character code
    or image for PC.


.. Note::
    This is under development. The codes below may not work.

Install
=================================================
::

	sudo pip install django-mfw
	
or::

	sudo pip install git+git://github.com/lambdalisue/django-mfw.git#egg=django-mfw


Required (Automatically installed)
=================================================

+	`e4u <https://github.com/lambdalisue/e4u>`_ (emoji4unicode bundle framework)


Quick tutorial
=================================================

1.	Add ``mfw`` and ``mfw.contrib.emoji`` to your ``INSTALL_APPS`` settings in ``settings.py``

2.  Add ``mfw.middleware.device.DeviceDetectionMiddleware`` to **the first
    item** of ``MIDDLEWARE_CLASSES`` in ``settings.py``

    .. Note::
        The following django-mfw middlewares are assumed that this middleware
        has called before they are called.

3.	Add ``mfw.middleware.session.SessionMiddleware`` and ``mfw.middleware.csrf.CsrfViewMiddleware``
	to your ``MIDDLEWARE_CLASSES`` setting and *comment out* existing middlewares.

4.	Add ``mfw.contrib.emoji.middleware.DeviceEmojiTranslationMiddleware`` and
	``mfw.middleware.flavour.DeviceFlavourDetectionMiddleware`` to your ``MIDDLEWARE_CLASSES`` setting.

5.	Add ``mfw.template.loaders.flavour.Loader`` to **the first item** of ``TEMPLATE_LOADERS`` setting.

6.	Add ``mfw.context_processors.device`` and ``mfw.context_processors.flavour`` to your ``TEMPLATE_CONTEXT_PROCESSORS`` setting.

The code below describe sample settings. See `settings.py <https://github.com/lambdalisue/django-mfw/blob/master/tests/src/miniblog/settings.py>`_ for more detail.::

	# List of callables that know how to import templates from various sources.
	TEMPLATE_LOADERS = (
	    'mfw.template.loaders.flavour.Loader',
	    'django.template.loaders.filesystem.Loader',
	    'django.template.loaders.app_directories.Loader',
	#     'django.template.loaders.eggs.Loader',
	)
	
	MIDDLEWARE_CLASSES = (
	    'mfw.middleware.device.DeviceDetectionMiddleware',

	    'django.middleware.common.CommonMiddleware',
	    #'django.contrib.sessions.middleware.SessionMiddleware',
	    'mfw.middleware.session.SessionMiddleware',
	    #'django.middleware.csrf.CsrfViewMiddleware',
	    'mfw.middleware.csrf.CsrfViewMiddleware',
	    'django.contrib.auth.middleware.AuthenticationMiddleware',
	    'mfw.contrib.emoji.middleware.DeviceEmojiTranslationMiddleware',
	    'mfw.middleware.flavour.DeviceFlavourDetectionMiddleware',
	)
	
	TEMPLATE_CONTEXT_PROCESSORS = (
	    "django.core.context_processors.auth",
	    "django.core.context_processors.debug",
	    "django.core.context_processors.i18n",
	    "django.core.context_processors.media",
	    "django.core.context_processors.request",
	    "mfw.context_processors.device",
	    "mfw.context_processors.flavour",
	)

Usage
===============================================

Device detection
----------------------------------------------------
request device is detected with ``mfw.middleware.device.DeviceDetectionMiddleware`` and stored in ``request.device``
the ``device`` instance has following attributes


``device.support_cookie``
    is the device support cookie or not.

``device.kind``
    A kind of this device. It is used for flavour template system.

``device.name``
    A name of this device. It is used for flavour template system.

``device.model``
    A model name of this device. It is used for flavour template system.

``device.version``
    A version name of this device. It is used for flavour template system.

``device.encoding``
    A recommended encoding for the device. It is used to encode the request/response

``device.carrier (additional)``
    An attribute which Mobilephone device has. the carrier name of the device.

``device.uid (additional)``
    An attribute which Mobilephone device has. User id which is passed from
    carrier server.

``device.reliable (additional)``
    An attribute which Mobilephone device has. If ``False`` then the
    HTTP_USER_AGENT might be modified thus passed user id is not reliable
    enough.



Non cookie based Session and CSRF protection
----------------------------------------------------
Django default session is saved on cookie because of security reason. However some device doesn't support cookie
so ``mfw.middleware.session.SessionMiddleware`` use carrier's UID and django cache system for saving session.

the middleware never try to use carrier's UID for device which support cookie. it is only for the device which doesn't support cookie
and commonly such device has carrier's UID. Because of security, device accessed from out of carrier's CIDR
is not trusted so it cannot save session if cookie is not supported.

.. Note::
    To accept non cookie based session for the device accessed from out of carrier's CIDR, set ``MFW_IGNORE_NON_RELIABLE_MOBILE`` to ``False``
    but **IT IS STRONGLY NOT RECOMMENDED**


Unicode emoji and Japanese carrier emoji conversion
----------------------------------------------------
``mfw.contrib.emoji.middleware.DeviceEmojiTranslationMiddleware`` care it. it detect device and automatically translate unicode emoji to
carrier's encoded emoji in response. That's why you do not need to care the code of emoji. Just write emoji as unicode emoji then
middleware translate everything correctly and encode response to carrier's encoding

Incoming translation is also handled the middleware. if ``request.GET`` or ``request.POST`` has carrier emoji, the middleware automatically
translate the carrier emojis to unicode emojis and decode value to unicode. 

Unicode emoji is found on http://www.unicode.org/~scherer/emoji4unicode/snapshot/full.html . this is a part of `emoji4unicode <http://code.google.com/p/emoji4unicode/>`_ project
and translation method is using conversion table of it. see `e4u <https://github.com/lambdalisue/e4u>`_ for more detail.


Flavour template system
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
