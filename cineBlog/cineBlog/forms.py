from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    telefono = forms.CharField(max_length=20, required=False)
    email = forms.EmailField(required=True)
    asunto = forms.CharField(max_length=200, required=True)
    mensaje = forms.Textarea()

    class Meta:
        fields = ['nombre', 'telefono', 'email', 'asunto', 'mensaje']