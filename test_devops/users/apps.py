import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "test_devops.users"
    verbose_name = _("Users")

    def ready(self):
        with contextlib.suppress(ImportError):
            import test_devops.users.signals  # noqa: F401
