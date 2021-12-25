from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .forms import Userinfo
from django.views import View
from django.contrib import messages
# Create your views here.

# for the new User Create account
def index(request):
    userForm = Userinfo()
    return render(request,'users/create.html',{'userForm':userForm})


class verifyUserForm(View):
    def post(self, request):
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
                return HttpResponseRedirect('/')
            
