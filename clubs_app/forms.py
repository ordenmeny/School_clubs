from django import forms
from .models import ClubModel


class CreateClubForm(forms.ModelForm):
    class Meta:
        model = ClubModel
        fields = ('name_club', 'type_club', 'paid_free', 'info_club')

        widgets = {
            'name_club': forms.TextInput(attrs={'class': 'form-control style-placeholder',
                                                'style': 'height:70px; border-radius:20px; font-size:30px; font-weight:400',
                                                'placeholder': 'Название клуба:'}),
            'type_club': forms.Select(attrs={'class': 'form-control form-select',
                                             'style': 'height:70px; border-radius:20px;font-size:30px; font-weight:400'}),
            'paid_free': forms.Select(attrs={'class': 'form-control form-select',
                                             'style': 'height:70px; border-radius:20px;font-size:30px; font-weight:400'}),

            'info_club': forms.Textarea(
                attrs={'class': 'form-control', 'style': 'border-radius: 20px !important; font-size:30px; font-weight:400;',
                       'rows': 3, 'placeholder': 'Добавь информацию о клубе:'})
        }
