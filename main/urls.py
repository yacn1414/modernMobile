from . import views
from django.urls import path

urlpatterns = [
    path('',views.main),
    path('search',views.search),
    path('likes/<id>',views.likes),
    path('sabad/<id>',views.sabad),
    path('sabad/',views.sabad),

    
]
