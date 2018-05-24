from django.apps import AppConfig


class DonationsConfig(AppConfig):
    name = "krvjezivot.donations"
    verbose_name = "Donations"

    def ready(self):
        """Override this to put in:
            Donations system checks
            Donations signal registration
        """
        try:
            import donations.signals  # noqa F401
        except ImportError:
            pass
