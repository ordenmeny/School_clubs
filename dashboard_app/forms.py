from django import forms
from clubs_app.models import ClubModel, ArticleClubModel
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
    class Meta:
        model = ArticleClubModel
        fields = ('title_article', 'text_body', 'image')

        # widgets =