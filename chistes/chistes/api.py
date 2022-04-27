from rest_framework import routers

from joke_api import views as joke_views

router = routers.DefaultRouter()
router.register(r'jokes', joke_views.JokeViewSet, basename="jokes")

urlpatterns = router.urls
