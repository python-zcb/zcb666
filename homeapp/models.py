# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# 书籍分类
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20, blank=True, null=True)
    book_counts = models.IntegerField(blank=True, null=True)
    category_pid = models.IntegerField(blank=True, null=True)
    column_5 = models.CharField(db_column='Column_5', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'category'

# 书籍
class Goods(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=128)
    book_author = models.CharField(max_length=64)
    book_publish = models.CharField(max_length=128)
    publish_time2 = models.DateField(blank=True, null=True)
    revision2 = models.IntegerField(blank=True, null=True)
    book_isbn = models.CharField(max_length=64, blank=True, null=True)
    word_count2 = models.CharField(max_length=64, blank=True, null=True)
    page_count2 = models.IntegerField(blank=True, null=True)
    open_type2 = models.CharField(max_length=20, blank=True, null=True)
    book_paper = models.CharField(max_length=64, blank=True, null=True)
    book_wrapper = models.CharField(max_length=64, blank=True, null=True)
    book_category = models.ForeignKey(Category, models.DO_NOTHING, db_column='book_category', blank=True, null=True)
    book_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    book_dprice = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    editor_recommendation = models.CharField(max_length=2000, blank=True, null=True)
    content_introduction = models.CharField(max_length=2000, blank=True, null=True)
    author_introduction = models.CharField(max_length=2000, blank=True, null=True)
    menu2 = models.CharField(max_length=2000, blank=True, null=True)
    media_review2 = models.CharField(max_length=2000, blank=True, null=True)
    digest_image_path2 = models.CharField(max_length=2000, blank=True, null=True)
    product_image_path = models.CharField(max_length=2000, blank=True, null=True)
    series_name = models.CharField(max_length=128, blank=True, null=True)
    printing_time = models.DateField(blank=True, null=True)
    impression = models.CharField(max_length=64, blank=True, null=True)
    stock2 = models.IntegerField(blank=True, null=True)
    shelves_date = models.DateField(blank=True, null=True)
    customer_socre = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    book_status = models.IntegerField(blank=True, null=True)
    sales = models.IntegerField(blank=True, null=True)
    column_27 = models.CharField(db_column='Column_27', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goods'

#车儿
class GoodsCar(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    book = models.ForeignKey(Goods, models.DO_NOTHING, blank=True, null=True)
    products_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    discount_price = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
    products_count = models.IntegerField(blank=True, null=True)
    column_7 = models.CharField(db_column='Column_7', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goods_car'

# 商品订单
class GoodsOrder(models.Model):
    address = models.ForeignKey('UserAddress', models.DO_NOTHING, blank=True, null=True)
    order_uid = models.ForeignKey('User', models.DO_NOTHING, db_column='order_uid')
    create_date = models.DateTimeField()
    num = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    column_8 = models.CharField(db_column='Column_8', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'goods_order'

# 订单项
class Orderitem(models.Model):
    shop_id = models.AutoField(primary_key=True)
    shop_bookid = models.ForeignKey(Goods, models.DO_NOTHING, db_column='shop_bookid')
    order = models.ForeignKey(GoodsOrder, models.DO_NOTHING, blank=True, null=True)
    shop_num = models.IntegerField()
    total_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    column_6 = models.CharField(db_column='Column_6', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderitem'

# 用户
class User(models.Model):
    e_mail = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    user_status = models.IntegerField()
    column_8 = models.CharField(db_column='Column_8', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'

# 用户地址
class UserAddress(models.Model):
    id2 = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    detail_address = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    telphone = models.CharField(max_length=20, blank=True, null=True)
    addr_mobile = models.CharField(max_length=20, blank=True, null=True)
    user_id2 = models.ForeignKey(User, models.DO_NOTHING, db_column='user_id2', blank=True, null=True)
    column_6 = models.CharField(db_column='Column_6', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_address'
