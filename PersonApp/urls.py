from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonList, PersonViewSet

router = DefaultRouter()
router.register(r'person', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('emrekalem_api/', PersonList.as_view(), name='person_check_list'),
]