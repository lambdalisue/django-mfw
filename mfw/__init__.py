from django.conf import settings

def setconf(name, default_value):
    value = getattr(settings, name, default_value)
    setattr(settings, name, value)

# A dictionary of dotted python path of CIDR scrapper classes.
# The key of the dictionary is carrier name used to determine
# which scrapper should be used to scrape CIDR
setconf('MFW_CIDR_SCRAPER_CLASSES', {
        'docomo': 'mfw.cidr.scrapers.DoCoMoCIDRScraper',
        'kddi': 'mfw.cidr.scrapers.KDDICIDRScraper',
        'softbank': 'mfw.cidr.scrapers.SoftbankCIDRScraper',
    })

# Expiration days of each CIDR. Each CIDR will be updated if
# the CIDR is expired.
setconf('MFW_CIDR_EXPIRATION_DAYS', 30)

# A list of dotted python path of Device classes.
# Add your own Device class when builtin devices are not enough
# to use (but I suggest you to contribute :-) Contribution is always welcome.)
setconf('MFW_DEVICE_CLASSES', (
        'mfw.device.smartphone.Smartphone',
        'mfw.device.browser.Browser',
        'mfw.device.mobilephone.DoCoMo',
        'mfw.device.mobilephone.KDDI',
        'mfw.device.mobilephone.Softbank',
    ))

# Checking reliable makes the response slow sometime. You can turned off
# the feature with the setting below.
setconf('MFW_CHECK_DEVICE_RELIABLE', True)

# mfw SessionMiddleware does not trust non reliable device and does not use
# UID based SessionMiddleware in that case because of security.
# However if you desire to turned off this feature and accept all non cookie
# supported device, use the setting below but STRONGLY NOT RECOMMENDED.
setconf('MFW_SESSION_TRUST_NON_RELIABLE_DEVICE', False)

# Used to create flavour from device. The function receive ``device`` instance
# and must return list/tuple
setconf('MFW_DEVICE_FLAVOUR_COLUMNS', lambda device: (device.kind.lower(), device.name.lower(), device.model.lower(), device.version.lower()))

# Used to create flavour from device. Each list item has ``condition`` and
# ``columns`` function and when ``condition`` function return ``True`` then
# ``columns`` function is used to overlap existing columns. Both function
# receive ``device`` and ``previous`` and must return list/tuple.
setconf('MFW_DEVICE_FLAVOUR_OVERLAP_RULES', ())
