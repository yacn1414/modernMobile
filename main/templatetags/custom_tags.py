from django.db.models import ExpressionWrapper,F,DecimalField

from django import template

from ..models import sabad,jamsabad
register = template.Library()
@register.simple_tag
def takhfif(price, price_offer, *args, **kwargs):
    resualt = int((price/100)*int(str(price_offer)[0:2])-price)*-1
    

    return f"{resualt:,}"

@register.simple_tag
def jam(price,price_offer, t,*args, **kwargs):
    a = ""
    for i in takhfif(price,price_offer).split(","):
        a += i
    
    resualt = int(a) * t
    return f"{resualt:,}"
@register.simple_tag
def format(resualt,*args, **kwargs):
    return f"{resualt:,}"
@register.simple_tag
def jam2(id_use, *args, **kwargs):
    discount_price = ExpressionWrapper(
        F('p'),output_field=DecimalField()
    )
    all = sabad.objects.annotate(
    discount_price=discount_price
    )
    a=0
    for am in all:
        a += int(am.p)
    if id_use:
        if jamsabad.objects.filter(jam=a).exists():
            pass
        else:
            jamsabad.objects.filter(id_user=id_use).delete()
            jamsabad.objects.create(jam=a,id_user=id_use)
    return ""
@register.simple_tag
def res(id_use, *args, **kwargs):
    if id_use :
        a = jamsabad.objects.get(id_user=id_use)
        return f"{a.jam:,}"
@register.simple_tag
def nerkhasli(id_use, *args, **kwargs):
    if id_use :
        a = sabad.objects.filter(id_user=id_use)
        ab=0
        for mm in a:
            ab += int(mm.p2)
        return f"{ab:,}"