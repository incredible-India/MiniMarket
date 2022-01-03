from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .forms import Userinfo
from django.views import View
from django.contrib import messages
from .models import Users,cart
from django.utils.decorators import method_decorator
from .middleware import userAuthentication
from django.db.models import Q 


# global middleware
from MiniMarket.middleware import checkUserStatus
from marketAdmin.models import vegitables,grocrey
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

        


# add to cart option for the user

class AddtoCart(View):

    def get(self, request,id,price,name):

        if 'name' not in request.session and  'email' not in request.session:
            return HttpResponseRedirect('/user/login')
           
 
            
        else:
        
 
            myitemv = vegitables.objects.filter(Q(vname=name) & Q(vprice=price) & Q(id=id))
   
            myitemg = grocrey.objects.filter(Q(gname=name) & Q(gprice=price) & Q(id=id))

      
        
        
        # print(getattr(myitemg, myitemg.other_field))
      
            if myitemg.count() != 0:
                for i in myitemg:
                    name = i.gname
                    price = i.gprice
                    # gamm = i.gamm
       
   
                cart.objects.create(uid = Users.objects.get(email=request.session['email']), item_name =name,item_price =price).save()
                messages.info(request,'Item sdded successfully to cart')
                return HttpResponseRedirect('/market/groc')
            if myitemv.count() != 0:
                for i in myitemv:
                    name = i.vname
                    price = i.vprice
                    # vamm = i.vamm
        
          
                cart.objects.create(uid = Users.objects.get(email=request.session['email']),item_name =name,item_price =price).save()
                messages.info(request,'Item sdded successfully to cart')
                return HttpResponseRedirect('/market/vegs')
                
            return HttpResponseRedirect('/')


@checkUserStatus
def mycart(request):
    if request.islogin :
        # first getting the id of the user
        mycart =[]
        userEmail = request.session['email']
        ownerID = cart.objects.filter()
        for i in ownerID:
            if i.uid.email == userEmail:
      
                mycart.append({'name':i.item_name,'price':i.item_price,'id':i.id})
       
                


        
        
        pprice =0
        if len(mycart) !=0:
            
            for i in mycart:
                for j in i:
                 
                    if j == 'price':
                        pprice = pprice + i[j]
                        
        return render(request, 'users/mycart.html',{'userdata':request.userdata,'mycart':mycart,'Cartlen':len(mycart),'tammount':pprice})



        
    else:
        return HttpResponseRedirect('/user/login/')
        



def deleteFromCart(request,id):
    userEmail= request.session['email']
    if cart.objects.get(pk=id).uid.email == userEmail: 
        cart.objects.filter(id=id).delete()
        return HttpResponseRedirect('/user/show/mycart')
    else:
        return HttpResponseRedirect('/user/login/')

@checkUserStatus
def deleteAllFRMCART(request):
    if request.islogin :
        cart.objects.all().delete()
        return HttpResponseRedirect('/user/show/mycart')
    else:
        return HttpResponseRedirect('/user/login/')
    




def BuyFRMCart(request,totalIt,totalAm):
    if 'name' in request.session and 'email' in request.session:
        em=Users.objects.filter(email=request.session['email'])
        address = ''
        name =''
        for i in em:
            address=i.address
            name = i.name
        userdata = {'uname' : name,
                            'o1' : 'My Cart',
                            'o1link' : '/user/show/mycart/',
                       
                            'o3':'Log Out',
                            'o3link':'/user/logout',}
        request.session['cnf'] ='cnfDATA'
        return render(request,'users/buyCart.html',{'address':address,'totalAm':totalAm,'totalIt':totalIt,'userdata':userdata,'cnf':False})

    else:
        return HttpResponseRedirect('/user/login/')



def CnfBuyFRMCart(request):
    if 'name' in request.session and 'email' in request.session:
        em=Users.objects.filter(email=request.session['email'])
   
        name =''
        for i in em:
          
            name = i.name
        userdata = {'uname' : name,
                            'o1' : 'My Cart',
                            'o1link' : '/user/show/mycart/',
                        
                            'o3':'Log Out',
                            'o3link':'/user/logout',}
        if request.session['cnf'] == 'cnfDATA':
            request.session['cnf']  =False
            return render(request,'users/buyCart.html',{'userdata':userdata,'cnf':True})
        else:
            return HttpResponseRedirect('/user/show/mycart/')
    else:
        return HttpResponseRedirect('/user/login/')


def DRCTBuyFrmcrd(request,id):
    if 'name' in request.session and 'email' in request.session:
        em=Users.objects.filter(email=request.session['email'])
        name =''
        for i in em:
          
            name = i.name
        userdata = {'uname' : name,
                            'o1' : 'My Cart',
                            'o1link' : '/user/show/mycart/',
                         
                            'o3':'Log Out',
                            'o3link':'/user/logout',}
      
        myItems = vegitables.objects.get(pk=id)
        

           
     
        
        return render(request,'users/singlebuy.html',{'userdata':userdata,'myItems':myItems,'veg':False})

    
    else:
        return HttpResponseRedirect('/user/login/')



def DRCTBuyFrmcrdGroce(request,id):
    if 'name' in request.session and 'email' in request.session:
        em=Users.objects.filter(email=request.session['email'])
        name =''
        for i in em:
          
            name = i.name
        userdata = {'uname' : name,
                            'o1' : 'My Cart',
                            'o1link' : '/user/show/mycart/',
                        
                            'o3':'Log Out',
                            'o3link':'/user/logout',}
      
        myItems = grocrey.objects.get(pk=id)
        

           
       
        
        return render(request,'users/singlebuy.html',{'userdata':userdata,'myItems':myItems,'veg':True})

    
    else:
        return HttpResponseRedirect('/user/login/')

@checkUserStatus
def confirmBuy(request):
    if request.islogin :
        return render(request,'users/orderCNF.html')
    else:
        return HttpResponseRedirect('/user/login/')




