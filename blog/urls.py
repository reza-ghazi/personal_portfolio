from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),

    # Showing the content of specific blog by its id.
    path('<int:blog_id>/', views.detail, name='detail'),
]
