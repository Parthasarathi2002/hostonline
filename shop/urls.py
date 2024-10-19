from django.urls import path
from . import views

urlpatterns = [
    path("hom",views.home),
    path("all/",views.all),
    path('add/',views.add,name='add'),
    path('show/',views.show),
    path('delete/<int:n>',views.delet,name='delete'),
    path('update/<int:n>',views.update,name='update'),
]
