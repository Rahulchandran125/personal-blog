"""
URL configuration for blogging_project project.

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
from django.urls import path,include

from home import views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.indexfun),
    # path('blog/', views.blogfun),
    path('Dashboard/', views.Dashboardfun),
    path('manage-post/', views.managepostfun),
    path('add-category/', views.addcategoryfun),
    path('register/', views.registerfun),
    path('login/', views.loginfun),
    path('logout/',views.logoutfun),
    path('addpost/', views.addpostfun),
    path('category/<int:c_id>', views.categoryfun),
    path('addcategory/', views.addcategoryfun),
    path('editcategory/<int:c_id>',views.editcategoryfun),
    path('deletecategory/<int:c_id>',views.deletecategoryfun),
    path('about/', views.aboutfun),
    path('gellary/', views.gellaryfun),
    path('post/', views.postfun),
    path('editpost/<int:e_id>',views.editpostfun),
    path('deletepost/<int:e_id>',views.deletepostfun),
    path('profile/', views.profilefun),
    path('addprofile/', views.addprofilefun),
    path('editprofile/', views.editprofilefun),
    path('search/', views.searchfun),
    path('privacy/', views.privacyfun),
    path('userprofile/<int:u_id>', views.userprofilefun),


    # path('like/<int:post_id>/', views.like_post, name='like_post'),


    path('blog/', include('home.urls', namespace='home')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 