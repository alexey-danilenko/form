from .models import MyForm
from django.forms import ModelForm, TextInput, EmailInput

class MyFormForm (ModelForm):
    class Meta:
        model = MyForm
        fields = ['first_name', 'last_name', 'phone', 'email']

        widgets = {
            'first_name' : TextInput(attrs={
                'class' : 'form-control',
                'id' : 'floatingInput',
                'placeholder' : ' ',
            }),
            'last_name' : TextInput(attrs={
                'class' : 'form-control',
                'id' : 'floatingInput',
                'placeholder' : ' ',
            }),
            'phone' : TextInput(attrs={
                'class' : 'form-control',
                'id' : 'floatingInput',
                'placeholder' : ' ',
            }),
            'email' : EmailInput(attrs={
                'class' : 'form-control',
                'id' : 'floatingInput',
                'placeholder' : ' ',
            }),
        }