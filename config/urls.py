from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from django.contrib.auth.decorators import login_required
from django.conf.urls import include, url
from qr_code import urls as qr_code_urls

urlpatterns = [
    url(r"^$",
        TemplateView.as_view(template_name="pages/home.html"),
        name="home"),
    url(r'^contact/$',
        TemplateView.as_view(template_name='pages/contact.html'),
        name='contact'),
    url(r'^terms/$',
        TemplateView.as_view(template_name='pages/terms.html'),
        name='terms'),
    url(r'^privacy/$',
        TemplateView.as_view(template_name='pages/privacy.html'),
        name='privacy'),

    # Django Admin, use {% url 'admin:index' %}
    url(settings.ADMIN_URL, admin.site.urls),
    # User management
    url(r"^users/", include("krvjezivot.users.urls", namespace="users")),
    url(r"^administration/", include("krvjezivot.administration.urls", namespace="administration")),
    url(r"^donations/", include("krvjezivot.donations.urls", namespace="donations")),
    url(r'^qr_code/', include(qr_code_urls, namespace="qr_code")),
    url(r"^accounts/", include("allauth.urls")),

    # Your stuff: custom urls includes go here
    url(r'^dashboard/',
        login_required(
            TemplateView.as_view(template_name='pages/dashboard.html')),
        name='dashboard')
] + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(
            r"^400/$",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        url(
            r"^403/$",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        url(
            r"^404/$",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        url(r"^500/$", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [url(r"^__debug__/", include(debug_toolbar.urls))
                       ] + urlpatterns
