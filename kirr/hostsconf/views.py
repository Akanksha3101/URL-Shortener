from django.conf import settings
from django.http import HttpResponseRedirect

from kirr.settings import DEFAULT_REDIRECT_URL

DEFAULT_PATH = getattr(settings, "DEFAULT_REDIRECT_URL", "http://www.short.com:8000")


def wildcard_redirect(request, path=None):
    new_url = DEFAULT_REDIRECT_URL
    if path is not None:
        new_url = DEFAULT_REDIRECT_URL + "/" + path
    return HttpResponseRedirect(new_url)
