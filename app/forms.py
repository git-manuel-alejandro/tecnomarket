from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeValidator
from django.forms import ValidationError




class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        # fields = ['nombre','correo','tipo_consulta','mensaje','avisos']
        fields = '__all__'


class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3 , max_length= 50)
    imagen = forms.ImageField(required= False , validators=[MaxSizeValidator(max_file_size=1)])

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        existe = Producto.objects.filter(nombre = nombre).exists()

        if existe:
            raise ValidationError('Producto ya existe')
        else:
            return nombre


    class Meta:
        model = Producto
        # fields = ['nombre','correo','tipo_consulta','mensaje','avisos']
        fields = '__all__'

        widgets = {
            "fecha_fabricacion" : forms.SelectDateWidget()
        }


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username' , 'first_name' , 'last_name', 'email', 'password1' , 'password2']
