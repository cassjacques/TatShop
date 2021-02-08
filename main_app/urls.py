from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('artists/', views.artists_index, name='artists_index'),
    path('artists/<int:artist_id>/', views.artists_detail, name='artists_detail'),
    path('artists/<int:artist_id>/remove_flash/<int:flash_id>/', views.remove_flash, name='remove_flash'),
    path('artists/<int:artist_id>/add_flash/<int:flash_id>/', views.add_flash, name='add_flash'),
    path('artists/<int:artist_id>/edit_flash/<int:flash_id>', views.edit_flash, name='edit_flash'),
    path('artist/<int:artist_id>/add_tats/', views.add_tats, name='add_tats'),
    path('artists/<int:artist_id>/assoc_flash/<int:flash_id>/', views.assoc_flash, name='assoc_flash'),
]
