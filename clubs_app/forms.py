from django import forms
from .models import ClubModel


class CreateClubForm(forms.ModelForm):
    class Meta:
        model = ClubModel
        fields = ('name_club', 'author')

        widgets = {
            'name_club': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'})
        }