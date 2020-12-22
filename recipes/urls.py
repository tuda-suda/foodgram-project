from django.urls import path, include

from . import views


recipes_urls = [
    path('new/', views.recipe_new, name='recipe_new'),
    path('<int:id>/', views.recipe_view, name='recipe_view'),
    path('<int:id>/edit/', views.recipe_edit, name='recipe_edit')
]

urlpatterns = [
    path('', views.index, name='index'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('favorites/', views.favorites, name='favorites'),
    path('shop-list/', views.shop_list, name='shop_list'),
    path('recipe/', include(recipes_urls)),
    path('<str:username>/', views.profile_view, name='profile_view'),
]
