

from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#offer 
class Offer(models.Model):
    time = models.DateTimeField(_("زمان تخفیف"))
    darsad = models.IntegerField(_("درصد تخفیف"))
    def __str__(self):
        return str(self.darsad)
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'تخفیف ها '
        verbose_name_plural = 'تخفیف ها'

class Product(models.Model):
    NUMBERS = [
        ("1", 1),
        ("22", 2),
        ("333", 3),
        ("4444", 4),
        ("55555", 5),
    ]

    
    name = models.CharField(_("اسم محصول"),max_length=255)
    price = models.IntegerField(_("قیمت به تومان"))
    picture = models.ImageField(_("عکس نمایشی"),upload_to='ProductImage/picture')
    picture2 = models.ImageField(_("عکس پیش نمایش"),upload_to='ProductImage/picture2')
    picture3 = models.ImageField(_("عکس جزيیات"),upload_to='ProductImage/picture3')
    picture4 = models.ImageField(_("عکس جزییات"),upload_to='ProductImage/picture4')
    vip = models.CharField(_("محصول ویژه"),max_length=20,default="no",choices=[("no","خیر"),("yes","بله")])
    price_offer = models.ForeignKey(Offer,on_delete = models.CASCADE,blank=True,null=True,default=0)
    category = models.ForeignKey("category",on_delete=models.CASCADE)
    star = models.CharField(_("امتیاز به ستاره"),max_length=25,choices=NUMBERS)
    caption = models.TextField(_("معرفی جزیَی"),)
    detail = models.TextField(_("معرفی دقیق"),)
    buyers = models.IntegerField(_("تعداد فروش"),default=0)
    view = models.IntegerField(_("تعداد بازدید"),default=0)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'محصولات'
        verbose_name_plural = 'محصولات'

class Userphone(models.Model):
    phone = models.CharField(max_length=11)
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'شماره کاربر‍‍‍'
        verbose_name_plural = '‍شماره کاربر'
class Email(models.Model):
    Email = models.EmailField(blank=False,unique=True)
    def __str__(self):
        return str(self.Email)
# category
class category(models.Model):
    name = models.CharField(_("اسم "),max_length=255)
    image = models.ImageField(_("عکس "),upload_to="category")
    Tpost = models.IntegerField(_("تعداد پست"),default=0)
    def __str__(self):
        return self.name
    class Meta:
        db_table = ''
        managed = True
        verbose_name = ' دسته بندی ها'
        verbose_name_plural = 'دسته بندی ها'
# image trend 2
class Image_trend_2(models.Model):
    image1 = models.ImageField(_("عکس اولی"),upload_to="main/pic/1")
    cat1 = models.ForeignKey(category,on_delete=models.CASCADE,related_name="cat1")
    image2 = models.ImageField(_("عکس دومی"),upload_to="main/pic/2")
    cat2 = models.ForeignKey(category,on_delete=models.CASCADE,related_name="cat2")

    class Meta:
        db_table = ''
        managed = True
        verbose_name = ' دو عکس ترند'
        verbose_name_plural = 'دو عکس ترند'

# image_under

class image_u(models.Model):
    image = models.ImageField(_("عکس"),upload_to="main/u")
    category = models.ForeignKey(category,on_delete=models.CASCADE)
    def __str__(self):
        return "image"

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'عکس پایینی'
        verbose_name_plural = 'عکس پایینی'

# Product


class interest(models.Model):
    id_pro = models.IntegerField()
    id_user = models.IntegerField(blank=True,null=True)
    class Meta:
        verbose_name_plural = _("علاقمندی ها")
        verbose_name = _("علاقمندی ها")
class sabad(models.Model):
    id_pro = models.IntegerField()
    T = models.IntegerField(_("تعداد"),default=1)
    id_user = models.IntegerField(blank=True,null=True)
    p = models.CharField(max_length=255)
    p2 = models.CharField(max_length=255)
class jamsabad(models.Model):
    jam = models.IntegerField(blank=True,null=True)

    id_user = models.IntegerField()

    class Meta:
        verbose_name = _("jam")
        verbose_name_plural = _("jam sabad")

class Brand(models.Model):
    name = models.CharField(_("نام"),max_length=200)
    image = models.ImageField(_("عکس برند"),upload_to="brands")
    

    class Meta:
        verbose_name = _("brand")
        verbose_name_plural = _("brands")

    def __str__(self):
        return self.name
class contact(models.Model):
    username = models.CharField(max_length=30)
    textmessage = models.TextField()
    response = models.TextField(null=True,blank=True)
    class Meta:
        verbose_name = _("contact")
        verbose_name_plural = _("contact")

    def __str__(self):
        return self.username
from django.dispatch import receiver
from django.db.models.signals import post_save,post_delete
@receiver(post_save,sender=Product)
def add_to_category(sender,instance,created,**kwargs):
    if created:
        b = category.objects.get(id=instance.category.id)
        b.Tpost += 1
        b.save()


@receiver(post_delete,sender=Product)
def delete_category(sender,instance,**kwargs):
    b = category.objects.get(id=instance.category.id)
    b.Tpost -= 1
    b.save()


