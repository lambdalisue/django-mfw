from django.conf import settings

def setconf(name, default_value):
    value = getattr(settings, name, default_value)
    setattr(settings, name, value)

setconf('MFW_CIDR_SCRAPER_CLASSES', {
        'docomo': 'mfw.cidr.scrapers.DoCoMoCIDRScraper',
        'kddi': 'mfw.cidr.scrapers.KDDICIDRScraper',
        'softbank': 'mfw.cidr.scrapers.SoftbankCIDRScraper',
    })
setconf('MFW_CIDR_EXPIRATION_DAYS', 30)

setconf('MFW_DEVICE_CLASSES', (
        'mfw.device.smartphone.Smartphone',
        'mfw.device.browser.Browser',
        'mfw.device.mobilephone.DoCoMo',
        'mfw.device.mobilephone.KDDI',
        'mfw.device.mobilephone.Softbank',
    ))
setconf('MFW_IGNORE_NON_RELIBLE_MOBILE', True)

#setconf('MFW_FLAVOUR_PATTERN', r"%(cookie)s/%(kind)s/%(name)s/%(model)s/%(version)s")
setconf('MFW_FLAVOUR_PATTERN', r"%(kind)s/%(name)s/%(model)s/%(version)s")
setconf('MFW_CHECK_DEVICE_RELIABLE', True)
