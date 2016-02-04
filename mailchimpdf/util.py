import os

BASE = 'https://{dc}.api.mailchimp.com/3.0'
apikey = None


def get_mailchimp_apikey():
    """Returns MailChimp api key from environment"""
    global apikey
    if apikey:
        return apikey
    else:
        with open(os.path.expanduser("~/.mailchimprc")) as config_file:
            apikey = config_file.read().strip()
        return apikey


def get_mailchimp_dc(apikey):
    """The datacenter is after the '-' in MailChimp API key"""
    return apikey.split('-')[1]


def get_mailchimp_endpoint(apikey):
    """Returns MailChimp API endpoint from apikey"""
    dc = get_mailchimp_dc(apikey)
    endpoint = BASE.format(dc=dc)
    return endpoint


def mc_build_url(path=""):
    """Given a path, returns url for method"""
    endpoint = get_mailchimp_endpoint(get_mailchimp_apikey())
    endpoint = endpoint.rstrip('/')
    return endpoint + "/{path}".format(path=path)
