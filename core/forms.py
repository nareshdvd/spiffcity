from django import forms
from django.forms import extras
from core.models import Country, State, City

class UserForm(forms.Form):
    username = forms.CharField(max_length = 100,required = True)
    email = forms.EmailField(max_length = 200,required = True)
    password = forms.CharField(max_length = 16, min_length = 3,widget = forms.PasswordInput(),required = True)
    
class SettingsForm(forms.Form):
    username = forms.CharField(max_length = 100,required = True)
    email = forms.EmailField(max_length = 200, required = True)
    first_name = forms.CharField(max_length = 100, required = True)
    last_name = forms.CharField(max_length = 100)
    dob = forms.DateField(widget = extras.SelectDateWidget()),
    profile_pic = forms.ImageField(),
    gender = forms.ChoiceField(
        choices = (
            ('m','Male'),
            ('f','Female')
        ),
        required = True
    ), #not in user table
    zipcode = forms.IntegerField(max_length = 20), #not in user table
    street_address1 = forms.CharField(max_length = 500, widget = forms.Textarea()) #not in user table
    street_address2 = forms.CharField(max_length = 500, widget = forms.Textarea()) #not in user table
    country = forms.ChoiceField(choices = [
        (obj.id,obj.name) for obj in Country.objects.filter()
    ]) #not in user table
    state = forms.ChoiceField(choices =[
        (obj.id,obj.name) for obj in State.objects.filter()
    ]), #not in user table
    city = forms.ChoiceField(choices = [
        (obj.id,obj.name) for obj in City.objects.filter()
    ]) #not in user table