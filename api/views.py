from django.shortcuts import render
from rest_framework import filters, mixins, viewsets
from rest_framework.permissions import IsAuthenticated


from recipes.models import Ingredient
from .models import Subscription
from .serializers import IngredientSerializer, SubscriptionSerializer


class IngredientViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    filter_backends = (filters.SearchFilter, )
    search_fields = ('^title',)


class SubscriptionViewSet(mixins.CreateModelMixin,
                       mixins.DestroyModelMixin,
                       viewsets.GenericViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = (IsAuthenticated, )
