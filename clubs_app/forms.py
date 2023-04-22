from django import forms
from .models import ClubModel


class FormClubModel(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat_club'].empty_label = 'Тип клуба не выбран:'
        self.fields['cat_club'].label = 'Тип клуба'
    
    class Meta:
        model = ClubModel
        fields = ["title_club", "cat_club", "info_club", "days_event", "time_start_event", "duration_event"]

        widgets = {
            'title_club': forms.TextInput(attrs={'class': 'form-control'}),
            'cat_club': forms.Select(attrs={'class': 'form-control'}),

        }
