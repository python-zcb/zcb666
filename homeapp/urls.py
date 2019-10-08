from django.urls import path
from homeapp import views

app_name = 'homeapp'

urlpatterns = [
    path('home/',views.home,name='home'),
    path('bookdetail/',views.bookdetail,name='bookdetail'),
    path('booklist/',views.booklist,name='booklist'),

]