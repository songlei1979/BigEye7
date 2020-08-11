from rest_framework import routers
from .api import ClientViewSet, CaseViewSet, PaymentViewSet, InvestigatorViewSet, EquipmentViewSet, AssignmentViewSet, \
    AllocationViewSet

router = routers.DefaultRouter()
router.register('api/clients', ClientViewSet,'Clients')
router.register('api/cases', CaseViewSet,'Cases')
router.register('api/payments', PaymentViewSet,'Payments')
router.register('api/investigators', InvestigatorViewSet,'Investigators')
router.register('api/equipments', EquipmentViewSet,'Equipments')
router.register('api/assignments', AssignmentViewSet,'Assignments')
router.register('api/allocations', AllocationViewSet,'Allocations')


urlpatterns = router.urls