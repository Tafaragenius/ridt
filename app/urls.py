from django.urls import path
from . import views

urlpatterns = [
    path('dashboard', views.dashboard, name = 'dashboard'),
    path('dashboard', views.create_blog, name = 'create_blog'),
    path('read-blog', views.read_blog, name = 'read_blog'),
    path('admin-blog', views.admin_blog, name = 'admin_blog'),
    path('admin-blog', views.delete_blog, name = 'delete_blog'),
    path('read-blog', views.create_comment, name = 'create_comment'),
    path('admin-comment', views.admin_comment, name = 'admin_comment'),
    path('admin-comment', views.delete_comment, name = 'delete_comment'),
    path('admin-user', views.admin_user, name = 'admin_user')
]
