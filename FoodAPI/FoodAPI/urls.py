"""FoodAPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.urls import path, include
from FoodAPI.AppAPI import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Rest/', views.restList),
    path('Rest/ID/<int:pk>/', views.restID),
    path('Rest/Zip/<int:zipcode>/', views.restZip),
    path('Item/', views.itemList),
    path('Item/ID/<int:pk>/', views.itemID),
    path('Item/Rest/<int:restId>/', views.itemRest),
    path('User/', views.userList),
    path('User/ID/<str:pk>/', views.userID),
    path('Rating/', views.ratingList),
    path('Rating/Rest/<int:restId>/', views.ratingRest),
    path('Rating/User/<str:userEmail>/', views.ratingUser),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
