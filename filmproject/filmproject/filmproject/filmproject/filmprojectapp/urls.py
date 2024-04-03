
from django.urls import path
from . import views

urlpatterns = [

    path('',views.index,name='index'),
    path('filmproject/<int:getmovie_id>/',views.detail,name='detail'),
    path('add/', views.addmovie, name='addmovie'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('addedmoviesbyuser',views.addedmoviesbyuser,name='addedmoviesbyuser'),
    path('detailbycategory/<str:category>/', views.detailbycategory, name='detailbycategory'),
    path('search/', views.search_results, name='search_results'),
    path('review/<int:id>/', views.post_review, name='post_review'),




    
]
