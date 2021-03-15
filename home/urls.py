from django.urls import path, include
from rest_framework import routers
from . import views

app_name = 'home'

router=routers.DefaultRouter()
router.register("region",views.RegionViewSet,basename="region")
router.register("state",views.StateViewset,basename="state")
router.register("lga",views.LgaViewSet,basename="lga")
router.register("center",views.CenterViewset,basename="center")


urlpatterns = [
    path('api/',include(router.urls)),
    path('api/state_id/<str:id>', views.StateNameByViewSet.as_view(), name="statebyid"),
    path('api/lga_id/<str:id>', views.LgaByNameViewSet.as_view(), name="lgabyid"),
    path('api/center_id/<str:id>', views.CenterByViewSet.as_view(), name="centerbyid"),
]