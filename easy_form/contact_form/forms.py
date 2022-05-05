from .models import MyForm
from django.forms import ModelForm, TextInput, EmailInput
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class MyFormForm (ModelForm):
    captcha = ReCaptchaField(score_threshold=0.5)

    class Meta:
        model = MyForm
        

        fields = ['first_name', 'last_name', 'phone', 'email', 'captcha']

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