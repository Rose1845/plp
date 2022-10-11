
from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import get_user_model
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address please',required=True)
    class Meta:
        model= get_user_model()
        fields = ['first_name','last_name','username','email','password','password2']
    
    def save(self,commit=True):
        user= super(UserRegistrationForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
def UserLoginForm():
    def __init__(self,*args,**kwargs):
        super(UserLoginForm,self).__init__(*args,**kwargs)
    
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control','placeholder':'username or Email'}),
        label = "Username or Email")


    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class':'form-control','placeholder':'password'}))


    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name','email','image','description']
        
