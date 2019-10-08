from  homeapp.models import Goods



class Car_item():
    # book就是QuerySet对象
    def __init__(self, book, number):
        self.book = book
        self.number = number


class Cart():
    def __init__(self):
        self.save_price = 0
        self.total_price = 0
        self.cart_items = []

    def sums(self):
        self.save_price = 0
        self.total_price = 0
        for i in self.cart_items:
            self.total_price += float(i.book.book_dprice * int(i.number))
            self.save_price += float((i.book.book_price - i.book.book_dprice )* int(i.number))

    def add_cart(self, bookid,number):
        for i in self.cart_items:
            # 判断是否已有当前商品
            if i.book.book_id == bookid:
                # 有的话数量加number
                i.number = int(i.number) + int(number)
                self.sums()
                return
        # 没有，添加一个Car_item对象
        self.cart_items.append(Car_item(Goods.objects.get(book_id=bookid), int(number)))
        self.sums()

    def change_item(self,bookid,number):
        print(number)
        for i in self.cart_items:
            if i.book.book_id == bookid:
                i.number = number
        self.sums()

    def del_book(self, bookid):
        for i in self.cart_items:
            if int(i.book.book_id) == int(bookid):
                self.cart_items.remove(i)
                self.sums()