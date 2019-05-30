from django.urls import path

from . import views

urlpatterns = [
    path('', views.creations, name='creations'),
    path('<int:creation_id>', views.creation, name='creation'),
    path('search', views.search, name='search')

]
