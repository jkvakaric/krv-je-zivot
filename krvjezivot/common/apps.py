from django.apps import AppConfig


class CommonConfig(AppConfig):
    name = 'krvjezivot.common'
    verbose_name = "Common"

    def ready(self):
        """Override this to put in:
            Common system checks
            Common signal registration
        """
        try:
            import common.signals  # noqa F401
        except ImportError:
            pass
