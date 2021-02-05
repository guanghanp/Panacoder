

from django.conf import settings


def settings_info(request):
    return {

        'my_github': settings.MY_GITHUB,
        'my_linkedin': settings.MY_LINKEDIN

    }