from django.urls import path
from . import views

urlpatterns = [
    path('',views.homep,name='home'),
    path('update/<int:id>/',views.updatedata,name='updatedata'),
    path('delete/<int:id>/',views.deletedata,name='deletedata'),
 ]