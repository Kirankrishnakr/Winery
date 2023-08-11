from django.shortcuts import render,redirect
from Backend.models import Catdb
from Frontend.models import Contactdb,Signupdb,Cartdb,Checkout
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib import messages


# Create your views here.
def home(request):
    data =Catdb.objects.all()
    paginator = Paginator(data, 8)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(request,"Homepage.html",{'data':data,'page':page})
def about(req):
    return render(req,"Aboutpage.html")

def contact(request):
    return render(request,"Contact.html")



def savecontact(request):
    if request.method =="POST":
        na =request.POST.get('name')
        em =request.POST.get('email')
        sub =request.POST.get('subject')
        me =request.POST.get('message')
        obj =Contactdb(Nam=na,Ema=em,Sub=sub,Mes=me)
        obj.save()
        messages.success(request,"Feedback Send Successfully")
        return redirect(contact)
def signup(request):
    return render(request,"Signup.html")
def savesign(request):
    if request.method =="POST":
        uname =request.POST.get('username')
        ema =request.POST.get('emaill')
        pas =request.POST.get('password')
        cpas =request.POST.get('cpassword')
        obj =Signupdb(Name=uname,Email=ema,Password=pas,Cpass=cpas)
        obj.save()
        return redirect(signup)
def userlogin(request):
    if request.method =="POST":
        username_r =request.POST.get('username')
        password_r =request.POST.get('password')
        if Signupdb.objects.filter(Name=username_r,Password=password_r).exists():

            request.session['usernamel'] =username_r
            request.session['passwordl'] =password_r
            messages.success(request,"Login Successfully")
            return redirect(home)
        else:
            return redirect(signup)

    return redirect(signup)
def logout(request):
    del request.session['usernamel']
    del request.session['passwordl']
    messages.error(request,"Logout Successfully")
    return redirect(signup)

def products(request):
    data =Catdb.objects.all()
    paginator = Paginator(data, 8)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return render(request,"Products.html",{'data':data, 'page':page})
def single(request,dataid):
    data =Catdb.objects.get(id =dataid)
    return render(request,"Singleproduct.html",{'data':data})

def savecart(request):
    if request.method =="POST":
        us =request.POST.get("user")
        pro =request.POST.get("product")
        ppr =request.POST.get("pprice")
        qua =request.POST.get("quantity")
        to =request.POST.get("totalprice")
        obj =Cartdb(User=us,Product=pro,Pprice=ppr,Quan=qua,Tot=to)
        obj.save()
        return redirect(cart)

def cart(request):
    car =Cartdb.objects.filter(User=request.session['usernamel'])
    return render(request,"cart.html",{'car':car})
def deletecart(request,dataid):
    data =Cartdb.objects.filter(id=dataid)
    data.delete()
    return redirect(cart)


def checkout(request):
    item =Cartdb.objects.filter(User=request.session['usernamel'])
    total_price =0
    for i in item:
        total_price =total_price + i.Tot
    return render(request,"Checkout.html",{"item":item,"total_price":total_price})
def savecheck(request):
    if request.method =="POST":
        fi =request.POST.get("first")
        la =request.POST.get("last")
        st =request.POST.get("state")
        str =request.POST.get("street")
        po =request.POST.get("post")
        to =request.POST.get("town")
        ph =request.POST.get("mob")
        gt =request.POST.get("Total")
        obj =Checkout(First=fi,Last=la,State=st,Street=str,Postal=po,Town=to,Phone=ph,Grat=gt)
        obj.save()
        messages.success(request,"Order Placed Successfully")
        return redirect(home)

def blog(req):
    return render(req,"Blog.html")


