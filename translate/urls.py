from django.urls import path
from . import views

app_name = 'translate'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/<int:author_id>/', views.create, name='create')

]