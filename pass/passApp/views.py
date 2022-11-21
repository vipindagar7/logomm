from django.shortcuts import render,redirect
from django.http import HttpResponse
from passApp.models import Customer 
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request , 'home.html')
@login_required(login_url='/')
def entry(request):
    return render(request, "entry.html")
@login_required(login_url='/')

def show(request):
    data = Customer.objects.all()
    return render(request,"show.html",{'data':data})
@login_required(login_url='/')

def send(request):
    if request.method =='POST':
        uid =request.POST['uid']
        name =request.POST['name']
        phnNo=request.POST['phnNo']
        gender = request.POST['gender']
        paymentMode =request.POST['paymentMode']
        regDate =request.POST['regDate']
        story =request.POST['story']
        # checkIn = request.POST['checkIn']
        Customer(uid= uid ,name = name, phnNo=phnNo,gender=gender,paymentMode=paymentMode,regDate=regDate,story=story).save()
        return render(request,"entered.html")
    else:
        return HttpResponse('method is not post')
@login_required(login_url='/')

def delete(request):
    uid = request.GET['uid']
    Customer.objects.filter(uid = uid).delete()
    return render(request ,"deleted.html")

@login_required(login_url='/')

def edit(request):
    id = request.GET['uid']
    name = phnNo = paymentMode =gender= checkIn = "not_available"
    for x in Customer.objects.filter(uid = id):
        name = x.name
        phnNo = x.phnNo
        gender=x.gender
        paymentMode= x.paymentMode
        regDate=x.regDate
        story=x.story
        checkIn= x.checkIn
    return render(request,"edit.html", {'uid':id,'name':name,'phnNo':phnNo ,'gender':gender, 'paymentMode':paymentMode,'regDate':regDate,'story':story,'checkIn':checkIn})
@login_required(login_url='/')

def editRecord(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        name = request.POST['name']
        phnNo = request.POST['phnNo']
        gender = request.POST['gender']
        paymentMode = request.POST['paymentMode']
        checkIn = request.POST['checkIn']
        Customer.objects.filter(uid=uid).update(uid=uid,name=name,phnNo=phnNo,gender=gender,paymentMode=paymentMode,checkIn=checkIn)
        return redirect('/show')
    else :
        return HttpResponse('method is not post')

    
# login system
# signup save success
def signup_views(request):
    return render(request,"login.html")

def handelSignup_views(request):
    username = request.POST['username']
    email = request.POST['useremail']
    pass1 = request.POST['pass1']
    pass2 = request.POST['pass2']
    user = User.objects.create_user(username,email,pass1)
    user.save()
    return render(request,"login.html")


def handelLogin_views(request):
    if request.method=="POST":
        username = request.POST['loginUsername']
        password = request.POST['loginPassword']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"login successfully")
            return redirect("/entry")
        else:
            messages.error(request,"wrong id password")
            return redirect("/")
    else:
       return HttpResponse("404 - error")



@login_required(login_url='/')

def logout_view(request):
    
    logout(request)
    return redirect("/")
    

