
from django.contrib import messages
from django.shortcuts import render,redirect,HttpResponse
from . import models
from .forms import Emailc,contactForm
# Create your views here.

def main(request):
    Offrs = []
    if request.user.is_authenticated:
        id_use = request.user.id
        name = request.user.username
    else:
        id_use = 0
        name = None
    banner2 = models.Image_trend_2.objects.all()
    banner = models.image_u.objects.first()
    category = models.category.objects.all()
    product_all = models.Product.objects.all()
    if request.user.is_authenticated:
        
        sabad = len(models.sabad.objects.filter(id_user=request.user.id))
        ino = len(models.interest.objects.filter(id_user=request.user.id))
    else:
        sabad = 0
        ino = 0
    saba = models.sabad.objects.all()
    brands = models.Brand.objects.all()
    
    for e in models.Product.objects.all():
        if e.price_offer != None:
            
            
            Offrs += models.Product.objects.filter(name= e)
    if request.method == "POST":
        if request.user.is_authenticated:
            models.contact.objects.create(textmessage=request.POST['message'],username=request.user.username)
            messages.success(request,"پیام شما در سیستم ثبت شد پس از پاسخ داده شدن به پیام شما در پروفایل کاربری نمایش داده میشود")
        else:
            messages.warning(request,".شما لاگین نکردید برای تماس با ما از منو لاگین کنید")
            redirect('/')

    else:
        
        redirect('/')


    


    return render(request,
    "index.html",
    {"name":name,"data_banner":banner2,"id_use":id_use,"ofpr":Offrs,
    "category":category,"allp":product_all,
    "banner":banner,"brand":brands,
    "ino":ino,"sabad":sabad,
    "saba":saba})



def search(request):
    if request.method == "POST":
        search = request.POST['search_cahr']
        context = models.Product.objects.filter(name__contains=search)
        T = len(context)
    else:
        context = None
        search = ''
        T = 0
    if request.user.is_authenticated:
        sabadcount = models.sabad.objects.count()
        ino = models.interest.objects.count()
        saba = models.sabad.objects.all()
        id_use = request.user.id
        name = request.user.username
        allp = models.Product.objects.all()
    else:
        sabadcount = 0
        ino = 0
        saba = None
        id_use = 0
        name = None
        allp = None
    return render(request, 'opiran.html',{"context":context,"search":search,'T':T,
    "ino":ino,"sabad":sabadcount,"saba":saba,"id_use":id_use,"name":name,"allp":allp,
    })

def sabadolikes(request):
    models.sabad.objects.all()
    models.interest.objects.all()
    
def likes(request,id):
    if request.user.is_authenticated:
        pro = models.Product.objects.get(id=id)
        a = request.user.id
        models.interest.objects.create(id_user=a,id_pro=pro.id)
        return redirect("/likes")
    else:
        messages.info(request,"شما عضو سایت نشدید")
        return redirect('/')
def sabad(request,id=0):
    if request.user.is_authenticated:

        if request.user.username:
            name = request.user.username
        else:
            name = None

        if request.method == "POST":
            
            if request.user.is_authenticated:
                if models.sabad.objects.filter(id_user=request.user.id,id_pro=id).exists():
                    return redirect("../")
                else:
                    t = request.POST['T']
                    sp = request.POST['hidden']
                    sp2 = request.POST['hidden2']
                    p = sp.replace(",", "")
                    p2 = sp2.replace(",", "")
                    models.sabad.objects.create(id_user=request.user.id,id_pro=id,T=t,p=p,p2=p2)
                    return redirect("../")
            else:
                return redirect('/')        
        id_use = 0
        
        if request.user.is_authenticated:
            id_use = request.user.id
            name = request.user.username
        
    #################################################################################
        sabad = models.sabad.objects.count()
        ino = models.interest.objects.count()
        saba = models.sabad.objects.all()
        category = models.category.objects.all()
        product_all = models.Product.objects.all()
        return render(request,
        "sabad.html",{
    "ino":ino,"sabad":sabad,"saba":saba,"category":category,"allp":product_all,"id_use":id_use,"name":name
        })
    else:
        return redirect('/')