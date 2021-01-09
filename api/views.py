from rest_framework import filters, mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


from recipes.models import Ingredient
from .models import Subscription, Favorite
from .serializers import (IngredientSerializer, SubscriptionSerializer,
                          FavoriteSerializer, PurchaseSerializer)


class CreateDestroyViewSet(mixins.CreateModelMixin,
                           mixins.DestroyModelMixin,
                           viewsets.GenericViewSet):
    """
    A viewset that provides `create` and `destroy` actions.

    `destroy` action is overriden to return a json with a `success` flag.
    """
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        success = instance.delete()
        return Response({'success': bool(success)}, status=status.HTTP_200_OK)


class IngredientViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Provide a search for ingredients in database.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('^title',)


class SubscriptionViewSet(CreateDestroyViewSet):
    """
    A viewset that provides creation and deletion of
    `api.Subscription` entries.
    """
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated, )
    lookup_field = 'author'


class FavoriteViewSet(CreateDestroyViewSet):
    """
    A viewset that provides creation and deletion of
    `api.Favorite` entries.
    """
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (IsAuthenticated, )
    lookup_field = 'recipe'


class PurchaseViewSet(mixins.ListModelMixin, CreateDestroyViewSet):
    """
    A viewset that provides creation, deletion and listing of
    `api.Purchase` entries for a given `auth.User`.
    """
    serializer_class = PurchaseSerializer
    permission_classes = (IsAuthenticated, )
    lookup_field = 'recipe'

    def get_queryset(self):
        return self.request.user.purchases.all()
