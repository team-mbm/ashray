from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from cases.views import CaseViewset, TypeOfCaseViewSet, LocationViewSet, ContactViewSet, PostalCodeViewSet

router = DefaultRouter()
router.register(r'case', CaseViewset)
router.register(r'typeofcase', TypeOfCaseViewSet)
router.register(r'location', LocationViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'postalcode', PostalCodeViewSet)
urlpatterns = [
    url(r'^', include(router.urls))
]
