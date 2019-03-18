from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name='home'),
    path('searchResults/', views.search, name='searchResults'),
    path('entryDetails/<int:id>/',views.entryDetails,name='entryDetails'),
    path('createEntry/', views.createEntry, name='createEntry'),
    path('createRelated/<int:id>/', views.createRelated, name='createRelated'),
    path('editPost/<int:id>/', views.editPost, name='editPost'),
    path('editRelated/<int:id>', views.editRealted, name='editRelated'),
    path('deletePost/<int:id>', views.deletePost, name='deletePost'),
    path('deleteRelated/<int:id>/', views.deleteRelated, name='deleteRelated'),
    path('profile/', views.get_logged_in_user_posts, name='profile'),
    path('accounts/profile/', views.get_logged_in_user_posts, name='profile')
]