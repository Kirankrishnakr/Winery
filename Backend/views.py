from django.shortcuts import render,redirect
from Backend.models import Catdb
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from Frontend.models import Contactdb,Signupdb,Cartdb,Checkout
from django.contrib import messages

# Create your views here.

def mainfun(req):
    return render(req,"main.html")

def Addcat(req):
    return render(req,"Add-Category.html")
def savcat(req):
    if req.method=="POST":
        cn =req.POST.get("Cname")
        im =req.FILES['cimage']
        de =req.POST.get("description")
        pr =req.POST.get("price")
        qn =req.POST.get("quantity")
        vi =req.POST.get("vintage")
        va =req.POST.get("varieties")
        obj =Catdb(Cna=cn,Im=im,Des=de,Price=pr,Quantity=qn,Vin=vi,Varieties=va)
        obj.save()
        messages.success(req,"Products Saved Successfully")
        return redirect(Addcat)
def discat(req):
    data =Catdb.objects.all()
    return render(req,"Display-Category.html",{'data':data})

def editcat(req,dataid):
    data =Catdb.objects.get(id=dataid)
    return render(req,"Edit-Category.html",{'data':data})

def updatecat(request,dataid):
    if request.method =="POST":
        cn = request.POST.get("Cname")
        de = request.POST.get("description")
        pr = request.POST.get("price")
        qn = request.POST.get("quantity")
        vi = request.POST.get("vintage")
        va = request.POST.get("varieties")
        try:
            img = request.FILES['cimage']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file =Catdb.objects.get(id=dataid).Im
        Catdb.objects.filter(id=dataid).update(Cna=cn,Des=de,Price=pr,Quantity=qn,Vin=vi,Varieties=va,Im=file)
        messages.success(request,"Products Updated Successfully")
        return redirect(discat)

def deletecat(req,dataid):
    data =Catdb.objects.filter(id=dataid)
    data.delete()
    messages.error(req,"Deleted")
    return redirect(discat)

def Adminpage(req):
    return render(req,"Adminpage.html")

def Admin_Login(request):
    if request.method=="POST":
        username_r =request.POST.get('username')
        password_r =request.POST.get('password')
        if User.objects.filter(username__contains=username_r).exists():
            user =authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request,user)
                request.session['username']=username_r
                request.session['password']=password_r
                return redirect(mainfun)
            else:
                return redirect(Adminpage)
        else:
            return redirect(Adminpage)

def AdminLogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(Adminpage)

def displaycontact(request):
    data =Contactdb.objects.all()
    return render(request,"Displaycontact.html",{'data':data})
def deletecontact(req,dataid):
    data =Contactdb.objects.filter(id=dataid)
    data.delete()
    messages.error(req,"Deleted")
    return redirect(displaycontact)

def displayuser(request):
    use =Signupdb.objects.all()
    return render(request,"Display-UserDetails.html",{'use':use})
def deleteuser(req,dataid):
    data =Signupdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayuser)

def displaycheck(request):
    check =Checkout.objects.all()
    return render(request,"Display-checkout.html",{'check':check})
def deletecheck(req,dataid):
    item =Checkout.objects.filter(id=dataid)
    item.delete()
    return redirect(displaycheck)


