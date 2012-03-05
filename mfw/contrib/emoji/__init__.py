import os
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

def setconf(name, default_value):
    value = getattr(settings, name, default_value)
    setattr(settings, name, value)

setconf('MFW_EMOJI_TRANSLATION_FILENAME', os.path.join(os.path.dirname(__file__), 'data', 'emoji4unicode.xml'))
setconf('MFW_EMOJI_DEFAULT_CARRIER', 'kddi_img')
setconf('MFW_EMOJI_DEFAULT_ENCODING', 'utf-8')

# Load e4u
import e4u
e4u.load(filename=settings.MFW_EMOJI_TRANSLATION_FILENAME)

# Validation
if 'mfw.contrib.emoji.middleware.DeviceEmojiTranslationMiddleware' in settings.MIDDLEWARE_CLASSES:
    if 'mfw.middleware.encoding.DeviceEncodingMiddleware' in settings.MIDDLEWARE_CLASSES:
        raise ImproperlyConfigured("``DeviceEmojiTranslationMiddleware`` cannot be used with ``DeviceEncodingMiddleware``")
