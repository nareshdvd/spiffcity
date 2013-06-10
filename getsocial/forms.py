from django import forms
from getsocial.models import Album, Category
from core.models import City


class AlbumForm(forms.Form):
    title = forms.CharField(max_length = 200, required = True)
    category = forms.ChoiceField(
        choices = [
            (obj.id, obj.name) for obj in Category.objects.filter()
        ]
    )
    
    
class PhotoForm(forms.Form):
    def __init__(self, user, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.fields['album'] = forms.ChoiceField(
            choices = [
                (obj.id, obj.title) for obj in Album.objects.filter(user = user)
            ]
        )
        
        self.fields['city'] = forms.ChoiceField(
            choices = [
                (obj.id, obj.name) for obj in City.objects.filter()
            ]
        )
    title = forms.CharField(max_length = 200, required = True)
    image = forms.ImageField()
    cover_image = forms.BooleanField(required=False)
    featured = forms.BooleanField(required = False)