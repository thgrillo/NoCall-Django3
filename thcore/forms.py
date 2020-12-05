from django import forms
from .models import Mark


class MarkForm(forms.ModelForm):

    tecname = forms.CharField(label='Digite seu nome')
    INOROUT_CHOICES = [('entrada','Entrada'), ('saida','Saída')]
    inorout = forms.ChoiceField(label='Entrada ou saída?', choices=INOROUT_CHOICES, widget=forms.RadioSelect)
    locname = forms.CharField(label='Digite o local') 
    opsticket = forms.CharField(label='Ticket')

    class Meta:
        model = Mark
        fields = ['tecname', 'locname', 'opsticket', 'inorout', 'latitude', 'longitude',]
        widgets = {'latitude': forms.HiddenInput(), 
            'longitude': forms.HiddenInput(),
        }
