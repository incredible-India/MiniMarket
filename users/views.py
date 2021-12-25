from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .forms import Userinfo
from django.views import View
from django.contrib import messages
from .models import Users
# Create your views here.

# for the new User Create account
def index(request):
    userForm = Userinfo()
    return render(request,'users/create.html',{'userForm':userForm})


class verifyUserForm(View):
    def post(self, request):
        existingData = Users.objects.all()
        is_exist = existingData.exists()
        print(is_exist)
        Userdata = Userinfo(request.POST)
        if Userdata.is_valid():
            uname = Userdata.cleaned_data['name']
            upassword = Userdata.cleaned_data['password']
            ucpassword = Userdata.cleaned_data['cpassword']
            uemail = Userdata.cleaned_data['email']
            umobile = Userdata.cleaned_data['mobile']

            # code for the validation 
            if uname == "":
                messages.info(request,'Username Cannot Be Blank')
                return render(request,'users/create.html',{'userForm':Userdata})
            elif upassword != ucpassword:
                messages.info(request,'Password And Confirm Password Does not Matched')
                return render(request,'users/create.html',{'userForm':Userdata})
            elif '@gmail.com' not in uemail:
                messages.info(request,'Inccorect Email')
                return render(request,'users/create.html',{'userForm':Userdata})
            elif len(umobile) !=10:
                messages.info(request,'Incorrect Mobile')
                return render(request,'users/create.html',{'userForm':Userdata})
        
                
            else:
                checkEmailInDBS = Users.objects.filter(email=uemail)
                
                if is_exist == False:
                    Users.objects.create(name =uname,email =uemail ,password =upassword,mobile =upassword,address =upassword).save()
                elif len(checkEmailInDBS) == 0:
                    Users.objects.create(name =uname,email =uemail ,password =upassword,mobile =upassword,address =upassword).save()
                else:
                    messages.info(request,'Eamil Already Exist')
                    return render(request,'users/create.html',{'userForm':Userdata})


                
                return HttpResponseRedirect('/')
            

class loginForm(View):
    def get(self,request):
        return  render(request,'users/login.html')