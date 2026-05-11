import django
from django.test.utils import override_settings

def pytest_configure(config):
    from django.conf import settings
    import django
    django.setup()
    settings.STORAGES = {
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
    }