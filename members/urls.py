from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('Nav/', views.Nav, name='NAv'),
    path("About/",views.About,name="abo"),
    path("contact/",views.Contact, name="cont" ),
    path("Pot/",views.pot,name='pot')
]