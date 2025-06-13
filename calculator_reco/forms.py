from django import forms

class MathForm(forms.Form):
    input1 = forms.FloatField(label="Input 1")
    input2 = forms.FloatField(label="Input 2")
    OPERATION_CHOICES = [
        ('power', 'Power'),
        ('modulus', 'Modulus'),
        ('average', 'Average'),
        ('max', 'Max'),
    ]
    operation = forms.ChoiceField(choices=OPERATION_CHOICES, label="Operation")
