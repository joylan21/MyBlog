from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('createpost/',views.Create_Post,name='createpost'),
    path('myposts/',views.MyPosts,name='myposts'),
    path('update/<int:id>',views.update,name='update'),
    
]
