from django.urls import path
from carapp import views

app_name = 'carapp'

urlpatterns = [
    path('car/',views.car,name='car'),
    path('add_cart/',views.add_cart,name='add_cart'),
    path('update_cart/',views.update_cart,name='update_cart'),
    path('delete_book/',views.delete_book,name='delete_book'),
    path('indent/',views.indent,name='indent'),
    path('indent_add/',views.indent_add,name='indent_add'),
    path('indentok/',views.indentok,name='indentok'),
]