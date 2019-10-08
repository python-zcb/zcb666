from django.urls import path
from login_registapp import views

app_name = 'login_registapp'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('loginlogic/',views.loginlogic,name='loginlogic'),
    path('regist/',views.regist,name='regist'),
    path('registlogic/',views.registlogic,name='registlogic'),
    path('getcaptcha/',views.getcaptcha,name='getcaptcha'),
    path('chackcaptcha1/',views.chackcaptcha1,name='chackcaptcha1'),
    path('chackcaptcha/',views.chackcaptcha,name='chackcaptcha'),
    path('chackname/',views.chackname,name='chackname'),
    path('registok/',views.registok,name='registok'),
    path('quit/',views.quit,name='quit'),
    path('username/',views.username,name='username'),
]