from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from LittleLemonAPI.views import MenuItemsView, SingleMenuItemView

urlpatterns = [

    path('menu-items/', MenuItemsView.as_view(),name= 'menu-list'),
    path('menu-items/<int:pk>', SingleMenuItemView.as_view()),
    path('api-token-auth/', obtain_auth_token),
]