from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TuitionViewSet,ReviewViewset,GetAllSubjectsViewSet

router = DefaultRouter()
router.register('list', TuitionViewSet)
router.register('reviews', ReviewViewset)
router.register('subjects', GetAllSubjectsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]


