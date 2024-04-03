
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('filmproject/<int:filmproject_id>/',views.detail,name='detail'),
    path('add/', views.add_filmproject, name='add_filmproject'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('addedmoviesbyuser',views.addedmoviesbyuser,name='addedmoviesbyuser'),
    path('registerorlogin',views.registerorlogin,name='registerorlogin')



    
]
