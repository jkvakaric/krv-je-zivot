from django.apps import AppConfig


class AdministrationConfig(AppConfig):
    name = "krvjezivot.administration"
    verbose_name = "Administration"

    def ready(self):
        """Override this to put in:
            Administration system checks
            Administration signal registration
        """
        try:
            import administration.signals  # noqa F401
        except ImportError:
            pass
