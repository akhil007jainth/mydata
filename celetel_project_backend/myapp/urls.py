from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.url.as_view(),name="Home"),
    path('signup/', views.signupdata.as_view(),name="signupdata"),
    path('login/', views.login.as_view(),name="login"),
    path('forgetpass/', views.forgetpass.as_view(),name="forgetpass"),
    path('reset_pass/', views.reset_pass.as_view(),name="reset_pass"),
]
