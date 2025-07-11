"""
URL configuration for Helping project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from hands import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home1,name='home'),
    path('register/',views.register1,name='register'),
    path('login/',views.login1,name='login'),
    path('search/',views.search,name='search'),
    path('editing/',views.editing,name='editing'),
    path('update/<int:uid>',views.Update,name='update'),
    path('details/',views.details1,name='details'),
    path('logout/',views.logout,name='logout'),
    path('edit/<int:uid>/',views.u_editing,name='editing1'),
    path('user/',views.User1,name='user')
]
