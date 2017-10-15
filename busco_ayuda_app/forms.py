# coding=utf-8
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from busco_ayuda_app.models import Trabajador, TiposDeServicio


class TrabajadorForm(ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese sus nombres'})
    )
    apellidos = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese sus apellidos'})
    )
    aniosExperiencia = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad de años de experiencia'}),
        label='Años De Experiencia'
    )
    tiposDeServicio = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=TiposDeServicio.objects.all(),
        empty_label='Seleccione el tipo de servicio que ofrecerá',
        label='Tipo De Servicio'
    )
    telefono = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número telefónico'}),
        label='Teléfono'
    )
    correo = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
        label='Correo'
    )

    class Meta:
        model = Trabajador
        fields = ['nombre', 'apellidos', 'aniosExperiencia', 'tiposDeServicio', 'telefono', 'correo', 'imagen']


class UserForm(ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='Usuario'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Contraseña'
    )

    class Meta:
        model = User
        fields = ['username', 'password']
