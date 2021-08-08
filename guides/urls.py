from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_guides, name='guides'),
    path('<int:guide_id>/', views.guide_detail, name='guide_detail'),
    path('add/', views.add_guide, name='add_guide'),
    path('edit/<int:guide_id>', views.edit_guide, name='edit_guide'),
    path('delete/<int:guide_id>', views.delete_guide, name='delete_guide'),
]
