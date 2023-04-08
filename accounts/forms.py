from django.contrib.auth.forms import UserCreationForm
from .models import SignUpModel


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = SignUpModel
        fields = UserCreationForm.Meta.fields + ('email',)
