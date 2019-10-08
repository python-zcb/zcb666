from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render,redirect

# 这个py文件中向模板传输的uname其实都是username    原因是登录和注册后再路径传输的就是用户的username
# Create your views here.
from homeapp.models import Category,Goods,User

# 主界面
def home(request):
    e_mail = request.session.get('e_mail')
    uname = 0
    # 注册后过来的有e_mail  有username
    if e_mail and request.session.get("uname"):
        u = User.objects.filter(e_mail=e_mail)[0]
        u.username = request.session.get("uname")
        u.save()
        uname = User.objects.filter(e_mail=e_mail)[0].username
    # 自动登陆
    elif e_mail and request.GET.get("uname") is None:
        uname = User.objects.filter(e_mail=e_mail)[0].username
    # 直接登录
    elif request.GET.get("uname"):
        uname = request.GET.get('uname')
    # 从哪里登录登录后依旧跳哪
    elif request.session.get('uname'):
        uname= request.session.get('uname')
    request.session["uname"]=uname
    print(uname,"username,进入",type(uname))
    # 新书上架
    nbss = Goods.objects.all().order_by("printing_time")[:8]
    # 新书热卖
    nbs  = Goods.objects.all().order_by("publish_time2","sales")[0:6]
    # 主编推荐
    er = Goods.objects.filter(editor_recommendation__isnull = False)
    # 左侧分类
    # 父分类不是空 证明是二级标题
    sort1 = Category.objects.filter(category_pid__isnull=True)
    # 父分类是零  证明是一级标题
    sort2 = Category.objects.filter(~Q(category_pid=0))
    return render(request,"index.html",{"nbss":nbss,"nbs":nbs,"er":er,"sort1":sort1,"sort2":sort2,
                                        "uname":uname     ##  是昵称
                                        })

# 书籍详情页
def bookdetail(request):
    uname = request.session.get('uname')
    # 判断是否有书籍id   没有跳到home
    if request.GET.get("id"):
        bookid = request.GET.get("id")
    elif request.session.get('shujiid'):
        bookid = request.session.get('shujiid')
    else :
        return redirect('homeapp:home')
    request.session['shujiid'] = bookid
    # 根据id查询书籍
    book = Goods.objects.filter(book_id=bookid)[0]
    print(55,book)
    # 外键查询  查询分类
    bookC = Category.objects.filter(category_id=book.book_category.category_id)[0]
    f=0
    # 判断有没有父分类
    if bookC.category_pid is not None:
        fid = bookC.category_pid
        f = Category.objects.filter(category_id=fid)[0]
    return render(request,'Book details.html',{"book":book,    ##书籍对象
                                               "bookC":bookC,     ##书籍对象的分类
                                               "f":f,             ##书籍对象的  父  分类
                                               "uname":uname     ##  是昵称
                                               })


# 书籍分类列表页面
def booklist(request):
    uname = request.session.get('uname')

    # 左侧分类
    # 父分类不是空 证明是二级标题
    sort1 = Category.objects.filter(category_pid__isnull=True)
    # 父分类是零  证明是一级标题
    sort2 = Category.objects.filter(~Q(category_pid=0))
    # 书籍分类id
    if request.GET.get('id'):
        bookCid = request.GET.get('id')
        request.session['bookCid'] = bookCid
    elif request.session.get('bookCid'):
        bookCid = request.session.get('bookCid')
    else:
        return redirect('homeapp:home')
    # 筛选书籍分类表对象
    cate=0
    print(88,bookCid)
    if bookCid:
        cate = Category.objects.filter(category_id=bookCid)[0]
    books = []
    # 排序选择                     给他一个默认排序
    if request.GET.get('sort'):
        sort = request.GET.get('sort')
    elif request.session.get('sort'):
        sort = request.session.get('sort')
    else:
        sort = request.GET.get('sort','111')
    print(99,sort)
    request.session['sort'] = sort
    # 如果有父分类
    f=0
    if cate.category_pid is not None:
        # 父id
        fid = cate.category_pid
        # 父分类对象
        f = Category.objects.filter(category_id=fid)[0]
        if sort == 'sales':
            books = Goods.objects.filter(book_category=bookCid).order_by("-sales")     ##销量排序
        elif sort == 'price':
            books = Goods.objects.filter(book_category=bookCid).order_by("book_dprice")    ##价格排序
        elif sort == 'pubtime':
            books = Goods.objects.filter(book_category=bookCid).order_by("-printing_time")    ##出版时间排序
        elif sort == '111':
            books = Goods.objects.filter(book_category=bookCid)     ##默认排序
    # 没有父分类
    elif cate.category_pid == None:
        a = Category.objects.filter(category_pid=bookCid)
        l=[]
        for i in a:
            l.append(i.category_id)
        if sort == 'sales':
            books = Goods.objects.filter(book_category__in=tuple(l)).order_by("-sales")
        elif sort == 'price':
            books = Goods.objects.filter(book_category__in=tuple(l)).order_by("book_dprice")
        elif sort == 'pubtime':
            books = Goods.objects.filter(book_category__in=tuple(l)).order_by("-printing_time")
        elif sort == '111':
            books = Goods.objects.filter(book_category__in=tuple(l))
    # 分页                        默认第一页
    print(131,books)
    n = request.GET.get("number", '1')
    pagtor = Paginator(books, per_page=3)
    if int(n) not in pagtor.page_range:
        n = 1
    page = pagtor.page(n)
    return render(request, 'booklist.html',{"page":page,
                                            "sort1":sort1,        ##左侧分类栏   一级分类
                                            "sort2":sort2,        ##左侧分类栏    二级分类
                                            'books':books,        ##图书对象列表
                                            "id":int(bookCid),    ##图书分类id
                                            "f":f,                ##父分类
                                            "sort":sort,          ##排序选择
                                            "cate":cate,          ## 书籍分类表对象  查看所在位置   导航栏
                                            "uname":uname})       ##  是昵称


