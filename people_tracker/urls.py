"""people_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('', TemplateView.as_view(template_name="index.html"), name="index")
        path('',views.index, name="index"),
        path('about', views.about, name="about"),
        path('contact', views.contact, name="contact"),
        path("accounts/profile/", views.ProfileView.as_view(), name="profile"),
        
        # Django auth stuff
        # couldn't register a custom view called 'accounts' so using the default 'registration' for now  
        path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
       #path('login/', auth_views.LoginView.as_view(), name='login')
        path("logout/", auth_views.LogoutView.as_view(), name="logout")
]
    # Django default views
    # path('accounts/', include('django.contrib.auth.urls'))

    # accounts/login/   [na e='login']
    # accounts/login/ [nme= 'login' 
    # accounts/logout/ [name='logout']
    # accounts/password_change/ [name='password_change']
    # accounts/password_change_done/ [name='password_change_done']
    # accounts/password_reset/ [name='password_reset']
    # accounts/password_reset_done/ [name='password_reset_done']
    # accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
    # accounts/reset/done/ [name='password_reset_complete']