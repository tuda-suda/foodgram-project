from django.urls import include, path
from rest_framework.routers import DefaultRouter


from .views import IngredientViewSet, SubscriptionViewSet

router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet, basename='ingredients')
router.register(r'subscriptions', SubscriptionViewSet, basename='subscriptions')


urlpatterns = [
    path('', include(router.urls)),
]