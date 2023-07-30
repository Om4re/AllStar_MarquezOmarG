from django import forms

class ClaseForm(forms.Form):
    nombre = forms.CharField(label="Nombre de la Clase", max_length=50, required=True)
    codigo = forms.IntegerField(label="Codigo de Clase", required=True)
    email = forms.EmailField(label="Email", required=False)
    HORARIOS = (
        (1, "8:00 a.m - 10:00 a.m"),
        (2, "3:00 p.m - 5:00 p.m"),
        (3, "8:00 p.m - 10:00 p.m"),
    )
    horario = forms.ChoiceField(label="Horario elegido", choices=HORARIOS, required=True)
    
    Pago_en_Efectivo = forms.BooleanField()


    