from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
from cases.urls import router as case_router
SCHEMA_VIEW = get_schema_view(title='ashray ngo APIs')
class CommonRouter(DefaultRouter):
    """
    Router for Common Api-root for multiple apps and their urls
    full description of issue:
    https://github.com/tomchristie/django-rest-framework/pull/2001
    """
    def extend(self, router):
        """
        read the src:
        http://bit.ly/2jAzkbW
        """
        self.registry.extend(router.registry)

#https://www.python.org/dev/peps/pep-0008/#constants
ROUTER = CommonRouter()
ROUTER.extend(case_router)
#ROUTER.extend(compaints_router)
#ROUTER.extend(anganwadi_router)
urlpatterns = [
                  url(r'^$', TemplateView.as_view(template_name="app/index.html"), name='index'),
                  url(r'^api/',include(ROUTER.urls)),
                  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                  url(r'^schema/$', SCHEMA_VIEW)

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        url(r'^400/$', default_views.bad_request, kwargs={'exception': Exception('Bad Request!')}),
        url(r'^403/$', default_views.permission_denied, kwargs={'exception': Exception('Permission Denied')}),
        url(r'^404/$', default_views.page_not_found, kwargs={'exception': Exception('Page not Found')}),
        url(r'^500/$', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [
                          url(r'^__debug__/', include(debug_toolbar.urls)),
                      ] + urlpatterns
