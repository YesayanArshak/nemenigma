from django import forms
from django.conf import settings
from django.contrib.auth import password_validation


from user.models import User, Key
from key.models import KeyType, KeyToolType
from key.tools import validate


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    def clean_password(self) -> str:
        password = self.cleaned_data.get('password')

        if not password:
            raise forms.ValidationError(
                'Password cannot be empty.',
                code='password_empty'
            )

        try:
            password_validation.validate_password(password)
        except forms.ValidationError as e:
            raise forms.ValidationError(e.messages)

        return settings.PASSWORD_HASHER.hash(password)

    class Meta:
        model = User
        fields = '__all__'


class KeyForm(forms.ModelForm):
    def clean_key(self) -> str:
        key_type = KeyType(self.cleaned_data.get('key_type'))
        tool_type = KeyToolType(self.cleaned_data.get('tool_type'))
        key = self.cleaned_data.get('key')

        try:
            validate(key, key_type, tool_type)
        except forms.ValidationError as e:
            raise forms.ValidationError(e.messages)
        
        return key

    class Meta:
        model = Key
        fields = '__all__'
