from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import ExtendedUser


class NewUserForm(UserCreationForm):

    class Meta:
        model = ExtendedUser

        fields = ("email","full_name","password1","password2")


    def save(self,commit = True):
        user = super(NewUserForm,self).save(commit = False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user



class MyUserChangeForm(UserChangeForm):
    # form = NewUserForm
    # add_form = NewUserForm
    class Meta(UserChangeForm.Meta):
        Model = ExtendedUser
        fields = '__all__'
