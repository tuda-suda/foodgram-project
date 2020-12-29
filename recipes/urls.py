from django.urls import path, include

from . import views


recipes_urls = [
    path('new/', views.recipe_new, name='recipe_new'),
    path('<int:recipe_id>/', views.recipe_view, name='recipe_view'),
    path('<int:recipe_id>/edit/', views.recipe_edit, name='recipe_edit'),
    path('<int:recipe_id>/delete/', views.recipe_delete, name='recipe_delete'),
]

purchases_urls = [
    path('', views.purchases, name='purchases'),
    path('download/', views.purchases_download, name='purchases_download'),
]

urlpatterns = [
    path('', views.index, name='index'),
    path('subscriptions/', views.subscriptions, name='subscriptions'),
    path('favorites/', views.favorites, name='favorites'),
    path('purchases/', include(purchases_urls)),
    path('recipe/', include(recipes_urls)),
    path('<str:username>/', views.profile_view, name='profile_view'),
]
