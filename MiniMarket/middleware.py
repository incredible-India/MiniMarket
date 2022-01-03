from django.utils.functional import partition
from users import models
from django.template.response import TemplateResponse
class checkUserStatus:
 
    def __init__(self,get_response):
        self.get_response  =get_response
    
    def __call__(self,request):
        if 'name' in request.session:
            if 'email' in request.session:
                try:
                    
              
                    checkingData = models.Users.objects.get(email = request.session['email'])

                    request.islogin = True
                    request.userdata = {
                            'uname' : checkingData.name,
                            'o1' : 'My Cart',
                            'o1link' : '/user/show/mycart/',
                        
                            'o3':'Log Out',
                            'o3link':'/user/logout',
                   

                    }
                    # no ndeed to write this code
                except Exception as e:
                    request.islogin = False
                    request.userdata = {
                        'uname' : 'User',
                        'o1' : 'Sign in',
                        'o1link' : '/user/login/',
                        'o2' : 'New User',
                        'o2link' : '/user/createaccount/',
                                        }
        else:
            request.islogin = False
            request.userdata = {
                        'uname' : 'User',
                        'o1' : 'Sign in',
                        'o1link' : '/user/login/',
                        'o2' : 'New User',
                        'o2link' : '/user/createaccount/',
                                        }

        response = self.get_response(request)
        return response
   
        
    

        
                
        


                
                

