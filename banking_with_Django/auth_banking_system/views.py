from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout,update_session_auth_hash
from .forms import ContactForm
from django.contrib import messages

# Create your views here.

############# USER ID CREATION PAGE #############. 1
def signup(request):
    if request.method == 'POST':
        User.objects.create_user(
            first_name = request.POST['first_name'],
            last_name = request.POST['last_name'],
            email = request.POST['email'],
            username=request.POST['username'],
            password=request.POST['password'],
        )
    return render(request,'Signup.html')

############# USER LOGIN PAGE ##################. 2
def signin(request):
    if request.method == 'POST':
        user = authenticate(request,
                                username = request.POST['username'],
                                password = request.POST['password'],
        )
        if user:
            login(request,user)
            return redirect('signup')
    return render(request,'signin.html')

############# USER LOGOUT PAGE ##################. 3

def logout_user(request):
    logout(request)
    return redirect('signin') ##### YOU HAVE TO WORK WITH IT #####




############# USER home PAGE ##################. 4
def home(request):
    return render(request,'home.html')



############# USER about PAGE ##################. 5
def about(request):
    return render(request,'about_us.html')



############# USER contact PAGE ##################. 6
def contact(request):
    if request.method =='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # here you can save to DB or send email
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            return redirect('home')
    else:
        form = ContactForm()
    return render(request,'contact_us.html',{'form':form})