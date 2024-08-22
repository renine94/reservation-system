from django.urls import path

from ..views import v1

app_name = 'accounts-v1'

urlpatterns = [
    # User
    path('users/', v1.UserCRUDView.as_view({'get': 'list', 'post': 'create'}), name="user-list"),
    path('users/<int:pk>/', v1.UserCRUDView.as_view({'get': 'retrieve', 'delete': 'destroy', 'put': 'update'}), name="user-retrieve"),
    path('users/me/', v1.UserCRUDView.as_view({'get': 'me'}), name="user-info-me"),
    path('users/login/', v1.UserCRUDView.as_view({'post': 'login'}), name="user-login"),
    path('users/login/refresh/', v1.UserCRUDView.as_view({'post': 'login_refresh'}), name="user-login-refresh"),
    path('users/logout/', v1.UserCRUDView.as_view({'post': 'logout'}), name="user-logout"),
    
    # TBD
]
