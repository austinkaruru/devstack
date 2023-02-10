from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


app_name="devs"
urlpatterns = [
    path('main/', views.main, name='main'),
    path('verify/', views.verify, name="verify"),
    path('password/', views.password, name="password"),
    path('account/', views.account, name="account"),
    path('billing/', views.billing, name="billing"),
    path('findaccount/', views.findaccount, name="findaccount"),
    path('newverify/', views.newverify, name="newverify"),
    path('newpassword/', views.newpassword, name="newpassword"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('provision/', views.provision, name="provision")
]
urlpatterns += staticfiles_urlpatterns()