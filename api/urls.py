from django.urls import include, path
from rest_framework.routers import DefaultRouter


from .views import IngredientViewSet, SubscriptionViewSet, FavoriteViewSet

router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet, basename='ingredients')
router.register(r'subscriptions', SubscriptionViewSet, basename='subscriptions')
router.register(r'favorites', FavoriteViewSet, basename='favorites')


urlpatterns = [
    path('', include(router.urls)),
]