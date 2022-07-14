from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("websearching", views.WebSearchingViewSet, basename="websearching")
router.register(
    "cosinesimilarity", views.CosineSimilarityViewSet, basename="cosinesimilarity"
)
router.register("signup", views.UserSignupViewSet, basename="signup")
router.register("login", views.UserLoginViewSet, basename="login")


urlpatterns = router.urls
