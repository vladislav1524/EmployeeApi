from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, DepartmentViewSet


router = DefaultRouter()

router.register('employees', EmployeeViewSet)
router.register('departments', DepartmentViewSet)

urlpatterns = []

urlpatterns.extend(router.urls)
