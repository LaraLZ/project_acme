from cadastros.models import Empresas_afiliacao, Empresas 
from django.forms.models import ModelForm
from django import forms

class EmpresasForm(ModelForm):
    class Meta: 
        model = Empresas
        fields = (
            "empresa",
            "status",
        ) 
    def __init__(self, args, **kwargs):
        super(EmpresasForm, self).__init__(args, **kwargs)
        self.fields['empresa'].label = 'Empresa'
        self.fields['status'].label = 'Status'

