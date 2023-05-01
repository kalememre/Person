from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonCheckList, PersonViewSet

router = DefaultRouter()
router.register(r'person', PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('emrekalem_api/', PersonCheckList.as_view(), name='person_check_list'),
]