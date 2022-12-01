from django import forms

class cursoForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    comision=forms.IntegerField()

class profesoresForm(forms.Form):
    nombre=forms.CharField( max_length=50)
    apellido=forms.CharField(max_length=50)
    email=forms.EmailField(max_length=254)
    profesiones=forms.CharField(max_length=50)