from django.urls import path
from . import views
urlpatterns = [
    path('auth',views.auth,name="auth"),
    path('signup',views.signup),
    path('login',views.loginuser),
    path('authlogin',views.authlogin,name="authlogin"),
    
]
