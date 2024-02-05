from django import forms


class Get_textForm(forms.Form):
    phone = forms.IntegerField(label="Если знаешь только телефон")
    name_user = forms.CharField(label="Если знаешь только Name User")
    text_otpravki = forms.Textarea()

