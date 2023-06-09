from django import forms
from clubs_app.models import *
from ckeditor.widgets import CKEditorWidget


class ChangeClubData(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['title_club'].label = 'Изменить название клуба'
        self.fields['cat_club'].label = 'Изменить категорию'
        self.fields['info_club'].label = 'Изменить информацию'
        self.fields['days_event'].label = 'Изменить дни'
        self.fields['time_event'].label = 'Изменить время'
        self.fields['price_club'].label = 'Изменить цену'

    class Meta:
        model = ClubModel
        fields = ['title_club', 'cat_club', 'info_club', 'days_event', 'time_event', 'price_club', ]

        widgets = {
            'title_club': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'cat_club': forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'info_club': forms.Textarea(attrs={'class': 'form-control form-control-lg', 'rows': 4}),
            'days_event': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'time_event': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'price_club': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
        }


class ArticleClubForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = ArticleClubModel
        fields = ('title_article', 'text_body', 'image')

        widgets = {
            'title_article': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'})
        }


class MessageAddForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title_msg'].label = 'Заголовок сообщения'

    class Meta:
        model = MessageClub
        fields = ('title_msg', 'body_msg')

        widgets = {
            'title_msg': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'body_msg': forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
        }
