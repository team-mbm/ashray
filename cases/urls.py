from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from cases.views import CaseViewset, TypeOfCaseViewSet, LocationViewSet, ContactViewSet

router = DefaultRouter()
router.register(r'case', CaseViewset)
router.register(r'typeofcase', TypeOfCaseViewSet)
router.register(r'location', LocationViewSet)
router.register(r'contact', ContactViewSet)
urlpatterns = [
    url(r'^', include(router.urls))
]
