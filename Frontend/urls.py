from django.urls import path
from Frontend import views

urlpatterns =[
    path('home/',views.home,name="home"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('savecontact/',views.savecontact,name="savecontact"),
    path('signup/',views.signup,name="signup"),
    path('savesign/',views.savesign,name="savesign"),
    path('userlogin/',views.userlogin,name="userlogin"),
    path('logout/',views.logout,name="logout"),
    path('products/',views.products,name="products"),
    path('single/<int:dataid>/',views.single,name="single"),
    path('cart/',views.cart,name="cart"),
    path('savecart/',views.savecart,name="savecart"),
    path('checkout/',views.checkout,name="checkout"),
    path('savecheck/',views.savecheck,name="savecheck"),
    path('blog/',views.blog,name="blog"),
    path('deletecart/ <int:dataid>/',views.deletecart,name="deletecart"),
]