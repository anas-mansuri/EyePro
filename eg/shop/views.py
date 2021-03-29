from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from .models import contacts


# Create your views here.

def index(request):
    return render(request, 'shop/index.html')


def contact(request):
    if request.method=="POST":
        nm=request.POST.get('name')
        em=request.POST.get('email')
        phn=request.POST.get('phone')
        msg=request.POST.get('desc')
        c1=contacts(name=nm,email=em,phone=phn,message=msg)
        c1.save()
        return render(request, 'shop/contact.html')
    else:
        return render(request, 'shop/contact.html')






def account(request):
    return render(request, 'shop/account.html')


def eyeglass(request):
    return render(request, 'shop/eyeglass.html')


def goggle(request):
    return render(request, 'shop/goggle.html')


def cart(request):
    return render(request, 'shop/cart.html')


def checkout(request):
    return render(request, 'shop/checkout.html')


def productframe(request):
    return render(request, 'shop/productframe.html')


def productframe1(request):
    return render(request, 'shop/productframe1.html')


def productframe2(request):
    return render(request, 'shop/productframe2.html')


def productframe3(request):
    return render(request, 'shop/productframe3.html')


def productframe4(request):
    return render(request, 'shop/productframe4.html')

def productframe5(request):
    return render(request, 'shop/productframe5.html')

def shoplogin(request):
    if request.method == "POST":
        # Get the post Parameters
        uname = request.POST['uname']
        passw = request.POST['password']

        user = auth.authenticate(username=uname, password=passw)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/home/")
        else:
            msg = "Username Or Password Incorrect"
            return render(request, 'shop/shoplogin.html', {"msg": msg})
    else:
        return render(request, 'shop/shoplogin.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/shoplogin/')


def contactlense(request):
    return render(request, 'shop/contactlense.html')


def lens(request):
    return render(request, 'shop/lens.html')


def prescription(request):
    return render(request, 'shop/prescription.html')


def wishlist(request):
    return render(request, 'shop/wishlist.html')


def signup(request):
    if request.method == "POST":
        # Get the post Parameters
        uname = request.POST['uname']
        email = request.POST['email']
        pas = request.POST['password']
        passw = make_password(pas)

        if User.objects.filter(username=uname).exists():
            msg1 = "User Name Taken"
            # return HttpResponseRedirect("/signup/",{"msg":msg})
            return render(request, 'shop/signup.html', {"msg1": msg1})
        elif User.objects.filter(email=email).exists():
            msg2 = "Email Taken"
            return render(request, 'shop/signup.html', {"msg2": msg2})
        else:
            user = User.objects.create(username=uname, email=email, password=passw)
            user.save()
        return HttpResponseRedirect("/shoplogin/")
    else:
        return render(request, 'shop/signup.html')
