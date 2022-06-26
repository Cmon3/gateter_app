from django import forms
from .models import Maullido
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MaullidoForm(forms.ModelForm):
    body = forms.CharField(required=True,
                           widget=forms.widgets.Textarea(
                               attrs={
                                   "placeholder": "Escribe tu maullido:",
                                   "class": "textarea is-info is-medium",
                               }
                           ),
                           label="",
                           )

    class Meta:
        model = Maullido
        exclude = ("user", )


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        if commit:
            user.save()
        return user
