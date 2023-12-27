from django.shortcuts import render,redirect
from .form import usersignupForm,creditcardapplyForm,contactsForm
from .models import usersignup,creditcardapply,contacts
from django.contrib import messages
from django.core.mail import send_mail
import requests

import random

# Create your views here.
def index(request):
    user = request.session.get('user')
    if request.method == 'POST':  # root
        if request.POST.get('SignUp') == 'SignUp':
            username = ""
            newuser = usersignupForm(request.POST)
            if newuser.is_valid():
                username = newuser.cleaned_data.get('email')
                try:
                    un = usersignup.objects.get(email=username)
                    print("Username is already exists!")
                   
                except usersignup.DoesNotExist:
                    newuser.save()
                    print("User created successfully!")
                    messages.success(request,"Signup Successfully!")

               
            else:
                print(newuser.errors)
                messages.error(request,newuser.errors)
                
        elif request.POST.get('login') == 'login':
            unm = request.POST['email']
            pas = request.POST['password']

            user = usersignup.objects.filter(email=unm, password=pas)
            uid = usersignup.objects.get(email=unm)
            print("UserID:", uid.id)
            if user:  # true
                print("Login Successfull!")
                messages.success(request,"Login Success!")
                request.session['user'] = unm
                request.session['userid'] = uid.id
                return redirect('home')
        else:
                messages.error(request,"Oops... Login faild....Try again!")
    return render(request,'index.html')

def home(request):	
    if request.method=='POST':
        mynote=contactsForm(request.POST)
        if mynote.is_valid():
            mynote.save()
            print("Your notes has been submitted!")
        else:
            print(mynote.errors)       
    return render(request,'home.html')

def about(request):	     
    return render(request,'about.html')

def creditcard(request):	
    user=request.session.get('user')
    uid=request.session.get('userid')
    cuser=creditcardapply.objects.get(id=uid)
    if request.method=='POST':
        updateuser=creditcardapplyForm(request.POST)
        if updateuser.is_valid():
            updateuser=creditcardapplyForm(request.POST,instance=cuser)
            updateuser.save()
            print('Your profile has been updated!')
            return redirect('creditcard')
        else:
            print(updateuser.errors)
    return render(request,'creditcard.html',{'user':user,'cuser':creditcardapply.objects.get(id=uid)})     
    

def creditcardform(request):
    if request.method=='POST':
        creditcard=creditcardapplyForm(request.POST,request.FILES)
        if creditcard.is_valid():
            creditcard.save()
            print("Your Account Has been Created!")
        else:
            print(creditcard.errors)	  
            return redirect('creditcard')   
    return render(request,'creditcardform.html')

def services(request):	     
    return render(request,'services.html')

def client(request):	     
    return render(request,'client.html')

def contact(request):	
    if request.method=='POST':
        mynote=contactsForm(request.POST)
        if mynote.is_valid():
            mynote.save()
            #Email Send
            send_mail(subject="Thank You!",message=f"Dear User\n\nThank you for connecting us!\nWe will contact you soon!\n\nThanks & Regards\n+918347270447 | vekariyadipensi@gmail.com",from_email="djangocreditcard123@gmail.com",recipient_list=[request.POST['email']])
            print("Your notes has been submitted!")
            
            #SMS Send
            otp=random.randint(1111,9999)
            url = "https://www.fast2sms.com/dev/bulkV2"
            querystring = {"authorization":"jy1lum4IfY6henACTQa3wBZROiXtkDLocVU57GdrKM0HbSsxpv7Hp0ZtaeNj23drDVfoPu1KGQgsMB64","variables_values":f"{otp}","route":"otp","numbers":f"{request.POST['phonenumber']}"}
            headers = {
                'cache-control': "no-cache"
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            print(response.text)
        else:
            print(mynote.errors)     
    return render(request,'contact.html')