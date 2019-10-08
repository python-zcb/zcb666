import random
import string
from django.http import HttpResponse
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse
from login_registapp.captcha.image import ImageCaptcha
from homeapp.models import User
import hashlib

def getcaptcha(request):
    # 图片验证的对象
    image = ImageCaptcha()
    # 验证码随机组成   可控制长短   是一个列表
    codes = random.sample(string.ascii_letters+string.digits,4)
    # 把列表变成字符串
    codes = "".join(codes)
    # session记录验证码  注册时验证
    request.session["codes"] = codes
    print(request.session["codes"])
    # 图片上生成验证码
    date = image.generate(codes)
    return HttpResponse(date,"image/png")

# 登录
def login(request):
    uname = request.COOKIES.get("uname")
    upwd = request.COOKIES.get("upwd")
    a = User.objects.filter(e_mail=uname, password=upwd)
    if a:
        request.session["login"] = "ok"
        return redirect(reverse('homeapp:home')+'?e_mail='+uname)
    # 页面号码   存储
    page = request.GET.get('page')
    print(page,37,type(page))
    request.session['page'] = page
    return render(request,"login.html")

# 登录逻辑
def loginlogic(request):
    uname = request.POST.get('uname')
    upwd = request.POST.get('upwd')
    rem = request.POST.get('rem')
    # 加密
    upwd2 = upwd.encode(encoding="utf-8")
    h1 = hashlib.sha256()
    yan = b'666'
    h1.update(upwd2 + yan)
    # 最终结果
    upwd = h1.hexdigest()

    a = User.objects.filter(e_mail=uname,password=upwd)
    if a:
        page = request.session.get('page')
        request.session['uname'] = a[0].username
        ren = HttpResponse('ok1')
        if page == '2':
            ren = HttpResponse('ok2')
        elif page == '3':
            ren = HttpResponse('ok3')
        # 购物车时
        elif page == '4':
            ren = HttpResponse('ok4')
        if rem == 'true':
            ren.set_cookie("uname", uname, max_age=3600 * 24 * 2)
            ren.set_cookie("upwd", upwd, max_age=3600 * 24)
        user = User.objects.get(e_mail=uname)
        user.user_status="1"
        user.save()
        request.session['login'] = 'ok'
        return ren
    return HttpResponse("用户名或密码错误")

# 登陆判断验证码
def chackcaptcha1(request):
    number = request.POST.get("uyzm")
    code = request.session.get("codes")
    if number.lower() == code.lower():
        return HttpResponse("ok")
    return HttpResponse("error")

# 注册界面
def regist(request):
    # 保存page之后判断回到那个界面
    page = request.GET.get('page')
    request.session['page'] = page
    return render(request,"register.html")

# 注册逻辑
def registlogic(request):
    uname = request.POST.get('uname')
    upwd = request.POST.get('upwd')
    # 加密
    upwd2 = upwd.encode(encoding="utf-8")
    h1 = hashlib.sha256()
    yan = b'666'
    h1.update(upwd2 + yan)
    # 最终结果
    upwd=h1.hexdigest()
    # 添加对象
    user = User.objects.create(e_mail=uname,password=upwd,user_status=1)
    request.session['login'] = 'ok'
    a = User.objects.filter(e_mail=uname)[0]
    return HttpResponse(a.e_mail)


#  注册判断验证码
def chackcaptcha(request):
    number = request.POST.get("number")
    code = request.session.get("codes")
    if number.lower() == code.lower():
        return HttpResponse("1")
    return HttpResponse("0")

# 判断用户名是否存在
def chackname(request):
    name = request.POST.get("name")
    a = User.objects.filter(e_mail=name)
    print(a,120)
    if a:
        return HttpResponse("0")
    return HttpResponse("1")

# registok界面  将用户名传过去
def registok(request):
    e_mail = request.GET.get("e_mail")
    request.session['e_mail'] =e_mail
    return render(request,'register ok.html',{'e_mail':e_mail})

# 退出
def quit(request):
    username = request.session.get('uname')
    # 修改状态
    u= User.objects.filter(username=username)[0]
    u.user_status="0"
    u.save()
    # 万无一失的删除session
    request.session['login'] = 'no'
    del request.session['uname']
    request.session.clear()
    return HttpResponse("no")

# 判断昵称
def username(request):
    # 获取用户输入的昵称
    username = request.POST.get("uname")
    request.session['uname'] = username
    # 判断是否存在
    a = User.objects.filter(username=username)
    if a:
        # 若存在  重新输入 修改
        return HttpResponse('no')
    else:
        # 不存在进行则入库
        e_mail = request.session.get('e_mail')
        u = User.objects.filter(e_mail=e_mail)[0]
        u.username = request.session.get("uname")
        u.save()
    # 判断在那个界面注册的   还回到那个界面
    page = request.session.get('page')
    ren = HttpResponse('ok1')
    if page == '2':
        ren = HttpResponse('ok2')
    elif page == '3':
        ren = HttpResponse('ok3')
    return ren
