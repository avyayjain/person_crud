from django.urls import path
from . import views


urlpatterns = [
    path('post/', views.add_user),
    path('get/', views.return_all_users),
    path('get/<int:pk>', views.return_user_by_id),
    path('delete/<int:pk>/', views.delete_user_by_id),
    # path('logout/', views.logout),
]
