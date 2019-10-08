import datetime
import random

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from homeapp.models import User,Goods,GoodsCar,UserAddress,GoodsOrder,Orderitem
from carapp.car import Cart

def car(request):
    if request.session.get('login') == 'ok':
        print(111)
        username = request.session.get('uname')
        # 那个用户
        user = User.objects.filter(username=username)[0]
        # 那个用户的购物车
        a = GoodsCar.objects.filter(user_id=user.id)
        cart = request.session.get('cart')
        if cart:
            for j in cart.cart_items:
                if GoodsCar.objects.filter(user_id=user.id, book_id=j.book.book_id):
                    c = GoodsCar.objects.get(user_id=user.id, book_id=j.book.book_id)
                    c.products_count = j.number
                    c.save()
                else:
                    print(j.number)
                    b = Goods.objects.get(book_id=j.book.book_id)
                    GoodsCar.objects.create(user_id=user.id, book_id=j.book.book_id, products_price=b.book_dprice,
                                            products_count=j.number)
        if a:
            cart = Cart()
            for i in a:
                cart.add_cart(i.book_id,i.products_count)
            request.session['cart'] =cart
        user = username
    else:
        user = '0'
    cart = request.session.get('cart')
    if cart :
        return render(request,"car.html",{"username":user,'cart':cart.cart_items,'save_price':cart.save_price,'total_price':cart.total_price})
    return  render(request,'car.html',{"username":user})


def add_cart(request):
    bookid = request.GET.get('id')
    number = request.GET.get('number')
    print(bookid,number)
    cart = request.session.get('cart')
    if cart == None:
        cart = Cart()
    cart.add_cart(int(bookid),int(number))
    request.session['cart'] =cart
    username = request.session.get('uname')
    if username:
        a = User.objects.filter(username=username)[0]
        b = Goods.objects.filter(book_id=bookid)[0]
        print(a.id,bookid)
        if GoodsCar.objects.filter(user_id=a.id,book_id=bookid):
            c = GoodsCar.objects.get(user_id=a.id, book_id=bookid)
            c.products_count += 1
            c.save()
        else:
            GoodsCar.objects.create(user_id=a.id,book_id=bookid,products_price=b.book_dprice,products_count=number)
    if request.GET.get('url'):
        print('去往购物车')
        return redirect('carapp:car')
    return redirect('homeapp:bookdetail')



# 修改商品数量
def update_cart(request):
    cart = request.session.get('cart')
    number = request.GET.get('number')
    bookid = request.GET.get('bookid')
    cart.change_item(int(bookid),int(number))
    request.session['cart'] = cart
    username = request.session.get('uname')
    if username:
        a = User.objects.filter(username=username)[0]
        b = GoodsCar.objects.filter(user_id=a.id, book_id=int(bookid))[0]
        b.products_count = int(number)
        b.save()
    moeny = cart.total_price
    print(moeny,cart.save_price)
    request.session['moeny']=moeny
    return JsonResponse({'save':cart.save_price,'moeny':moeny})

# 删除商品
def delete_book(request):
    bookid = request.GET.get('id')
    cart = request.session.get('cart')
    cart.del_book(int(bookid))
    request.session['cart'] = cart
    username = request.session.get('uname')
    if username:
        a = User.objects.filter(username=username)[0]
        print(a.id, bookid, type(a.id), type(bookid))
        GoodsCar.objects.filter(user_id=a.id, book_id=int(bookid))[0].delete()
    return redirect('carapp:car')

# 地址页面
def indent(request):
    cart = request.session.get('cart')
    print(112)
    login=request.session.get('login')
    number = 0
    moeny = cart.total_price
    print(moeny,117)
    request.session['moeny'] = moeny
    for i in cart.cart_items:
        number += i.number
    request.session['number'] = number
    print(number, '666')
    if login=='ok':
        name = request.session.get('uname')
        userid=User.objects.filter(username=name)[0]
        print(userid)
        user=UserAddress.objects.filter(user_id2=userid.id)
        print(user,128,number,type(number))
        cart = request.session.get('cart')
        if number == 0:
            return redirect('carapp:car')
        elif cart:
            return render(request,'indent.html',{'user':user,'moeny':moeny,'name':name,'cart':cart.cart_items})
    return render(request,'login.html')

# 从数据库拿地址给  前端显示
def indent_add(request):
    option=request.GET.get('option')
    if option=='0':
        return
    else:
        add=UserAddress.objects.filter(name=option)[0]
    return JsonResponse({'id':add.id2,'username':add.name,'add':add.detail_address,'zip':add.zipcode,'tel':add.telphone})

#
def indentok(request):
    moeny = request.session.get('moeny')
    if moeny == 0:
        return redirect('carapp:car')
    s1 = request.POST.get('ship_man1')
    s2 = request.POST.get('ship_man2')
    s3 = request.POST.get('ship_man3')
    s4 = request.POST.get('ship_man4')
    moeny = request.session.get('moeny')
    name = request.session.get('uname')
    u = User.objects.filter(username=name)[0]
    user_id = u.id
    # 删除购物车
    GoodsCar.objects.filter(user_id=user_id).delete()
    add=UserAddress.objects.filter(name=s1,user_id2=u.id,detail_address=s2,zipcode=s3,telphone=s4)
    date = datetime.datetime.now()
    number = request.session.get('number')
    s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    salt = ''.join(random.sample(s, 15))
    cart = request.session.get('cart')
    if add:
        print(1)
        n = UserAddress.objects.filter(name=s1).values('id2')[0]['id2']
        a=GoodsOrder.objects.create(address_id=n,order_uid_id=user_id, num=number, create_date=date, price=moeny,status='1')
        for i in cart.cart_items:
            print(i.book.book_id, user_id, i.number,148)
            Orderitem.objects.create(shop_bookid_id=i.book.book_id, order_id=user_id, shop_num=i.number,column_6=a.id)
        del request.session['cart']
        return render(request,'indent ok.html',{'moeny':moeny,'name':name,'s1':s1,'salt':salt,'number':number})
    UserAddress.objects.create(user_id2_id=user_id,name=s1,detail_address=s2,zipcode=s3,telphone=s4,addr_mobile=11)
    a=UserAddress.objects.filter(name=s1)[0]
    print(a)
    b=GoodsOrder.objects.create(address_id=a.id2,order_uid_id=user_id,num=number,create_date=date,price=moeny,status='1')
    for i in cart.cart_items:
        print(i.book.book_id,user_id,i.number,157)
        Orderitem.objects.create(shop_bookid_id=i.book.book_id, order_id=user_id, shop_num=i.number, column_6=b.id)
    #     bookC = Category.objects.filter(category_id=book.book_category.category_id)[0]
    del request.session['cart']
    return render(request,'indent ok.html',{'moeny':moeny,'name':name,'s1':s1,'salt':salt,'number':number})



