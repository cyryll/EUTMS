from django import forms
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()

class UserCreationForm(forms.ModelForm):
    #StaffId = forms.CharField(label='staffId' ,widget = forms.TextInput(attrs={'placeholder':'Enter Staff ID'}))
    Email = forms.CharField(label='email' ,widget = forms.TextInput(attrs={'placeholder':'Enter Email'}))
    #contact = forms.CharField(label='contact' ,widget = forms.TextInput(attrs={'placeholder':'Enter Contact'}))
    password1 = forms.CharField(label = 'Password',widget=forms.PasswordInput(attrs={'placeholder':'Password Confirmation'}))
    password2= forms.CharField(label='Password Confirmation',widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}))

    class Meta:
        model = User
        fields = ('StaffId','Email', 'password1', 'password2',)

    def clean_password(self):
        password1= self.cleaned_data.get('password1')
        password2= self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password so not match')
        return password2

    def save(self,commit=True):
        user= super(UserCreationForm,self).save(commit = False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user

class UserLoginForm(forms.Form):
    StaffId = forms.CharField(label='StaffId' ,widget = forms.TextInput(attrs={'placeholder':'Enter Staff ID'}))
    password = forms.CharField(label = 'password',widget = forms.PasswordInput(attrs={'placeholder':'Enter password'}))

    def clean(self,*args, **kwargs):
        StaffId=self.cleaned_data.get('StaffId')
        password= self.cleaned_data.get('password')
        user_qs_final = User.objects.filter(
            Q(StaffId__iexact= StaffId) 
           # Q(email__iexact=query)
        ).distinct()
        if not user_qs_final.exists() and user_qs_final.count != 1:
            raise forms.ValidationError("invalid credentials-user doesnt exist")
        user_obj = user_qs_final.first()
        if not user_obj.check_password(password):
            raise forms.ValidationError('credentials are not correct')
        self.cleaned_data["user_obj"] = user_obj
        return super(UserLoginForm,self).clean(*args,**kwargs)