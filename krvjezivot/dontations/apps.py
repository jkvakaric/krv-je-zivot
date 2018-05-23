from django.apps import AppConfig


class DontationsConfig(AppConfig):
    name = "krvjezivot.dontations"
    verbose_name = "Dontations"

    def ready(self):
        """Override this to put in:
            Dontations system checks
            Dontations signal registration
        """
        try:
            import donations.signals  # noqa F401
        except ImportError:
            pass
