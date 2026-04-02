from django.urls import path
from . import views

app_name = 'builder'

urlpatterns = [
    path('', views.builder_home, name='home'),
    path('bow/create/', views.create_bow, name='create_bow'),
    path('build/create/<int:bow_id>/', views.create_build, name='create_build'),
    path('my-builds/', views.my_builds, name='my_builds'),
]