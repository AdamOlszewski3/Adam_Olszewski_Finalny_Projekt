from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import CategoryViewSet, EquipmentViewSet, RentalViewSet, MaintenanceViewSet, RegisterView

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'equipment', EquipmentViewSet)
router.register(r'rentals', RentalViewSet)
router.register(r'maintenance', MaintenanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
]
