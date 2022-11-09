from django.urls import path
from . import views
app_name = "details"
urlpatterns = [
    path('factors',views.factor,name="factor"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    # path('my-account',views.account,name="account"),
    # path('security',views.security,name="security"),
    path('c/<parametr>',views.categoryview,name="security"),
    path('pro/<id>',views.pro),
    path('next/<id>',views.next),
    path('com/<id>',views.comment),
    path('delete/<id>',views.delete)
]
