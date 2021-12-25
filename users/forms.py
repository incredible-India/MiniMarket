from django import forms

class Userinfo(forms.Form):
    name = forms.CharField(max_length=30,label_suffix='',widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=30,label_suffix='',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    cpassword = forms.CharField(label='Confirm Password',max_length=30,label_suffix='',widget=forms.PasswordInput(attrs={'class':'form-control' ,}))
    email = forms.CharField(max_length=50,label_suffix='',widget=forms.EmailInput(attrs={'class':'form-control'}))
    mobile= forms.CharField(label_suffix='',widget=forms.NumberInput(attrs={'class':'form-control'}))
    address= forms.CharField(label_suffix='',widget=forms.Textarea(attrs={'class':'form-control  mb-3 address' ,'rows':'10'}))
   