from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .forms import Userinfo
from django.views import View
from django.contrib import messages
from .models import Users
from django.utils.decorators import method_decorator
from .middleware import userAuthentication
from django.db.models import Q 
from django.contrib.auth import authenticate
# global middleware
from MiniMarket.middleware import checkUserStatus
# Create your views here.

# for the new User Create account
@userAuthentication
@checkUserStatus
def index(request):
    userForm = Userinfo()
    userdata = request.userdata
    passInTemplates ={'userForm':userForm,'userdata':userdata}

    return render(request,'users/create.html',passInTemplates)
   


class verifyUserForm(View):
    @method_decorator(checkUserStatus)
    @method_decorator(userAuthentication)
    def post(self, request):
        existingData = Users.objects.all()
        is_exist = existingData.exists()
        
        Userdata = Userinfo(request.POST)
        if Userdata.is_valid():
            uname = Userdata.cleaned_data['name']
            upassword = Userdata.cleaned_data['password']
            ucpassword = Userdata.cleaned_data['cpassword']
            uemail = Userdata.cleaned_data['email']
            umobile = Userdata.cleaned_data['mobile']
            uaddress = Userdata.cleaned_data['address']

            # code for the validation 
            if uname == "":
                messages.info(request,'Username Cannot Be Blank')
                return render(request,'users/create.html',{'userForm':Userdata,'userdata':request.userdata})
            elif upassword != ucpassword:
                messages.info(request,'Password And Confirm Password Does not Matched')
                return render(request,'users/create.html',{'userForm':Userdata,'userdata':request.userdata})
            elif '@gmail.com' not in uemail:
                messages.info(request,'Inccorect Email')
                return render(request,'users/create.html',{'userForm':Userdata,'userdata':request.userdata})
            elif len(umobile) !=10:
                messages.info(request,'Incorrect Mobile')
                return render(request,'users/create.html',{'userForm':Userdata,'userdata':request.userdata})
            elif len(uaddress) < 3:
                messages.info(request,'Invalid Address')
                return render(request,'users/create.html',{'userForm':Userdata,'userdata':request.userdata})
        
                
            else:
                checkEmailInDBS = Users.objects.filter(email=uemail)
                
                if is_exist == False:
                    Users.objects.create(name =uname,email =uemail ,password =upassword,mobile =umobile,address =uaddress).save()
                    request.session['email'] = uemail
                    request.session['name'] = upassword
                    
                elif len(checkEmailInDBS) == 0:
                    Users.objects.create(name =uname,email =uemail ,password =upassword,mobile =umobile,address =uaddress).save()
                    request.session['email'] = uemail
                    request.session['name'] = uname
                else:
                    messages.info(request,'Eamil Already Exist')
                    return render(request,'users/create.html',{'userForm':Userdata,'userdata':request.userdata})


                
                return HttpResponseRedirect('/')
            


class loginForm(View):
    @method_decorator(checkUserStatus)
    @method_decorator(userAuthentication)
    def get(self,request):
        return  render(request,'users/login.html',{'userdata':request.userdata})
     
    def post(self,request):
        
        uemail = request.POST.get('email')
        upass = request.POST.get('password')

        allUserinfo = Users.objects.filter(Q(email=uemail) & Q(password=upass))
      
        if allUserinfo.exists() :
            for i in allUserinfo:
                
                request.session['email'] = i.email
                request.session['name'] = i.name
            return HttpResponseRedirect('/')
        else:
            messages.info(request,'Incorrect Email Or Password')
            return  render(request,'users/login.html',{'userdata':request.userdata})



class userLogout(View):
    def get(self, request):
        if 'name' in request.session and 'email' in request.session:
            request.session.flush()
            request.session.clear_expired()
        else:
            request.session.flush()
            request.session.clear_expired()
        
        return HttpResponseRedirect('/')

        
        