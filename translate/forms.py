from django import forms
from translate.models import Data, Author


class AuthorForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Author
        fields = ['email']
        labels = {
            'email': '유저 이메일',
        }


