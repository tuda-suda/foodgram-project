from django.urls import path, include

from . import views


recipes_urls = [
    path('new/', views.recipe_new, name='recipe_new'),
    path('<int:recipe_id>/', views.recipe_view, name='recipe_view'),
    path('<int:recipe_id>/edit/', views.recipe_edit, name='recipe_edit'),
    path('<int:recipe_id>/delete/', views.recipe_delete, name='recipe_delete'),
]

urlpatterns = [
    path('', views.index, name='index'),
    path('subscriptions/', lambda x: x, name='subscriptions'),
    path('favorites/', lambda x: x, name='favorites'),
    path('shop-list/', lambda x: x, name='shop_list'),
    path('recipe/', include(recipes_urls)),
    path('<str:username>/', views.profile_view, name='profile_view'),
]
