from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_guides, name='guides'),
    path('<guide_id>', views.guide_detail, name='guide_detail'),
]
