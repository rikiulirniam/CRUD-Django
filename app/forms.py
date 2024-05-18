from django import forms
from .models import UserData

class UserForms(forms.ModelForm):
    class Meta:
        model = UserData
        fields = ['username', 'password', 'address']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")

        # Validasi kredensial pengguna
        if username and password:
            user = UserData.objects.filter(username=username, password=password).first()
            if not user:
                raise forms.ValidationError("Invalid username or password")
        return cleaned_data