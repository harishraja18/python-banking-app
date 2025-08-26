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
        return redirect('signin')
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
            messages.success(request,"Login Successfully")
            return redirect('profile')
    return render(request,'signin.html')

############# USER LOGOUT PAGE ##################. 3

def logout_user(request):
    logout(request)
    messages.success(request, "Logout successfully")
    return redirect('home') ##### YOU HAVE TO WORK WITH IT #####



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


###################### REST PASSWORD ON LOGIN PAGE###########################
# def reset_password_withour_login(request):
#     if request.method == 'POST':
#         email = email.POST.get('email')
#         new_password = request.POST['new_password']

#         try:
#             user = User.objects.get(email = email)
#             new_password = user.set_password(new_password)
#             user.save()
#             messages.success(request,"Meassage successfully changed")
#             return redirect('login')
#         except User.DoesNotExist:
#             messages.error(request,"user with this mail does not exist")
#             return redirect('login_forget')

def reset_password_without_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')

        try:
            user = User.objects.get(email=email)   # find user
            user.set_password(new_password)        # update password
            user.save()
            messages.success(request, "Password successfully changed")
            return redirect('signin')  # go to login page
        except User.DoesNotExist:
            messages.error(request, "User with this email does not exist")
            return redirect('forger_password_login_page')

    # 👇 This handles GET request → just show form
    return render(request, 'forger_password_login_page.html')


###################### FORGET PASSWORD ###########################

# def changepassword(request):
#     if request.method == 'POSt':
#         user = request.user
#         old_password = request.POST['old_password']
#         new_password = request.POST['new_password']
#         confirm_password = request.POST['confirm_password']
#         if not user.check_password(old_password):
#             messages.error(request,"Old Password is not correct")
#         elif new_password != confirm_password:
#             messages.error(request,"New Password and Current password does not match")
#         else:
#             if request.method == 'POST':
#                 user.set_password(new_password)
#                 user.save()
#                 update_session_auth_hash(request,user)
#                 messages.success(request,"Password is Changed")
#                 return redirect('signin')
#     return render(request,'update_password.html')