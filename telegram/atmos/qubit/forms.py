from django.forms import ModelForm
from .models import users


class userform(ModelForm):
    class Meta:
        model=users
        fields=['email','phno']