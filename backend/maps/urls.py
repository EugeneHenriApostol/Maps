from django.urls import path, include
from rest_framework.routers import DefaultRouter
from maps.views import StudentViewSet, ClusterViewSet
from maps import views

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'clusters', ClusterViewSet)

urlpatterns = [
    path('', include(router.urls)),  
]

