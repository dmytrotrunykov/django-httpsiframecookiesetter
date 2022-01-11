import logging
from urllib.parse import unquote

from django.conf import settings as django_settings
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.clickjacking import xframe_options_exempt

from .settings import HTTPS_IFRAME_COOKIESETTER_LOADING_GRAPHIC

logger = logging.getLogger(__name__)


@xframe_options_exempt
def cookiesetter(request):
    quoted_absurl = request.GET.get('absurl', '/')
    absurl = unquote(request.GET.get('absurl', '/'))
    fixed = request.GET.get('cookiefix', 'false')
    cookiesetter_view_path = reverse('cookiesetter',
                                     urlconf=django_settings.ROOT_URLCONF)

    return render(request, 'cookiesetter.html', {
        "redirect": (absurl!=cookiesetter_view_path),
        "current_url": request.build_absolute_uri().encode("utf8"),
        "cookiesetter_url": cookiesetter_view_path,
        "cookie_fixed": fixed == 'true',
        "cookies": request.COOKIES,
        "absurl": absurl,
        "quoted_absurl": quoted_absurl,
        "loading_graphic": HTTPS_IFRAME_COOKIESETTER_LOADING_GRAPHIC
    })
