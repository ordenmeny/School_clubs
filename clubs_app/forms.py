from django import forms
from .models import ClubModel


class FormClubModel(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title_club'].label = 'Название клуба'
        self.fields['cat_club'].empty_label = 'Тип клуба не выбран:'
        self.fields['cat_club'].label = 'Тип клуба'
        self.fields['info_club'].label = 'Информация о клубе'
        self.fields['days_event'].label = 'Дни проведения'
        self.fields['time_start_event'].label = 'Время проведения'
        self.fields['price_club'].label = 'Цена'

        self.fields['duration_event'].label = 'Длительность'

    class Meta:
        model = ClubModel
        fields = ["title_club", "cat_club", "info_club", "days_event", "time_start_event", "duration_event",
                  "price_club"]

        widgets = {
            'title_club': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'cat_club': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'info_club': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows': 4}),
            'days_event': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'time_start_event': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'duration_event': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'price_club': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }
