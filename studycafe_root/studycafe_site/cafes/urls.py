from django.urls import path
from . import views
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from .views import UserProfileView
from .views import MapView

urlpatterns = [
    path('', views.CafeListView.as_view(), name='home'),
    path('cafes/', views.CafeListView.as_view(), name='cafe-list'),
    path('cafe/<int:pk>/', views.CafeDetailView.as_view(), name='cafe-detail'),
    path('cafe/new/', views.CafeCreateView.as_view(), name='cafe-create'),
    path('cafe/<int:pk>/edit/', views.CafeUpdateView.as_view(), name='cafe-update'),
    path('cafe/<int:pk>/delete/', views.CafeDeleteView.as_view(), name='cafe-delete'),
    path('cafe/<int:cafe_id>/rate/', views.add_rating, name='add-rating'),
    path('rating/<int:rating_id>/delete/', views.delete_rating, name='delete-rating'),
    path('register/', views.register, name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('change-password/', views.custom_password_change, name='custom_password_change'),
    path('cafe/<int:cafe_id>/bookmark/', views.add_bookmark, name='add-bookmark'),
    path('cafe/<int:cafe_id>/unbookmark/', views.remove_bookmark, name='remove-bookmark'),
    path('map/', MapView.as_view(), name='map'),
    # Photo gallery
    path('cafe/<int:cafe_id>/photo/add/', views.add_photo, name='add-photo'),
    path('photo/<int:photo_id>/delete/', views.delete_photo, name='delete-photo'),
    # Follow/Unfollow
    path('user/<int:user_id>/follow/', views.follow_user, name='follow-user'),
    path('user/<int:user_id>/unfollow/', views.unfollow_user, name='unfollow-user'),
    # User followers and following pages
    path('user/<int:user_id>/followers/', views.user_followers, name='user-followers'),
    path('user/<int:user_id>/following/', views.user_following, name='user-following'),
]