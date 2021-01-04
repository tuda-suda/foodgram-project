from django.urls import include, path
from rest_framework.routers import DefaultRouter


from .views import (IngredientViewSet, SubscriptionViewSet, FavoriteViewSet,
                    PurchaseViewSet)

router = DefaultRouter()
router.register(r'ingredients', IngredientViewSet, basename='ingredients')
router.register(
    r'subscriptions',
    SubscriptionViewSet,
    basename='subscriptions',
)
router.register(r'favorites', FavoriteViewSet, basename='favorites')
router.register(r'purchases', PurchaseViewSet, basename='purchases')


urlpatterns = [
    path('v1/', include(router.urls)),
]
