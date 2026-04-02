from django.urls import path
from . import views

app_name = 'components'

urlpatterns = [
    path('submit/shaft/', views.submit_shaft, name='submit_shaft'),
    path('submit/vane/', views.submit_vane, name='submit_vane'),
    path('submit/nock/', views.submit_nock, name='submit_nock'),
    path('submit/insert/', views.submit_insert, name='submit_insert'),
    path('submit/broadhead/', views.submit_broadhead, name='submit_broadhead'),
]