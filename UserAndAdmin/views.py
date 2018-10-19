'''

视图文件


'''
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
from UserAndAdmin import forms, models
from django.contrib import messages
from django.core.mail import send_mail
from COMP9900 import settings


def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        print(register_form.errors)
        if register_form.is_valid():
            first_name = register_form.cleaned_data['first_name']
            last_name = register_form.cleaned_data['last_name']
            email = register_form.cleaned_data['email']
            password = register_form.cleaned_data["password"]

            same_email_user = models.User.object.filter(email=email)
            if same_email_user:  # 邮箱地址唯一
                message = "Email already exists!"
                print(message)
                return HttpResponse(1)
                # 当一切都OK的情况下，创建新用户


            new_user = models.User()
            new_user.first_name = first_name
            new_user.set_active()
            new_user.last_name = last_name
            new_user.set_password(password)
            new_user.email = email
            new_user.save()

            up = models.UserProfile()
            up.user = new_user
            up.save()

            # 发送邮件

            # subject = "Thank you for your registration "
            # message = "welcome to NSWLodge! we are very much appreciate your bussiness./n we will be in touch soon."
            # from_email = settings.EMAIL_HOST_USER
            # to_list = [new_user.email]
            # send = send_mail(subject,message,from_email,to_list,fail_silently=True)
            # print(send)

        return HttpResponse(2)
    else:
        return render(request,"index.html")



def login(request):
    if request.method == 'POST':
        #  前端 保证 email  password 有值
        email = request.POST.get('email',None)
        password = request.POST.get('password',None)
        # 检查该用户 邮箱是否存在 并 确认
        _email = models.User.object.filter(email=email)
        if not _email.exists():
            message = "email account doesn't exist!"
            return HttpResponse(0)

        _is_active =_email[0].active
        if not _is_active:
            message = "please confirm your email account!"
            return HttpResponse(1)

        user = auth.authenticate(email=email, password=password)

        if user:
            auth.login(request,user)
            return HttpResponse(3)
        else:
            message = "Your email or password is incorrect. "
            return HttpResponse(2)
    return render(request,"index.html")


def logout(request):
    auth.logout(request)
    return redirect("userandadmin:index")

def editprofile(request,page_id):
    print(page_id)
    print("editprofile user {}".format(request.user.first_name))
    if page_id == '1':
        if request.method == "POST":
            profileForm = forms.editprofileForm(request.POST)
            print(profileForm.errors)
            if profileForm.is_valid():

                first_name = profileForm.cleaned_data['first_name']
                last_name = profileForm.cleaned_data['last_name']
                gender =  profileForm.cleaned_data['gender']
                date_of_birth = profileForm.cleaned_data['date_of_birth']
                language = profileForm.cleaned_data['language']
                location = profileForm.cleaned_data['location']
                user_description = profileForm.cleaned_data['user_description']

                user = request.user
                if date_of_birth:
                    user.date_of_birth = '-'.join(date_of_birth.split(","))
                user.first_name = first_name
                user.last_name = last_name

                # if not user.userprofile:
                #     userProfile = models.UserProfile()
                #     userProfile.user = request.user

                user.userprofile.GENDER_CHOICES = gender
                user.userprofile.language = language
                user.userprofile.user_description = user_description
                user.userprofile.location = location
                user.userprofile.save()
                user.save()

                return HttpResponse(1)
        year = 1888
        month = ""
        day = ""
        if request.user.date_of_birth:
            year,month,day = str(request.user.date_of_birth).split("-")
        return render(request,'editprofile_editprofile.html',{"year":year, "month":month,"day":day})
    elif page_id == '2':
        return render(request,'editprofile_photos.html')
    else:
        return render(request,'editprofile.html')

def accountsetting(request):
    if request.method =="POST":
        passwordChangeForm = forms.passwordChangeForm(request.POST)
        print(passwordChangeForm.errors)
        if passwordChangeForm.is_valid():
            oldpassword = passwordChangeForm.cleaned_data['old_password']
            newpassword = passwordChangeForm.cleaned_data['new_password']

            user = auth.authenticate(email=request.user.email, password=oldpassword)

            if not user:
                return HttpResponse(2)
            else:
                request.user.set_password(newpassword)
                request.user.save()
                return HttpResponse(1)
    return render(request,'accountsetting.html')



