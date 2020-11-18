from django import forms


class MarkForm(forms.ModelForm):

    tecname = forms.CharField(label='Digite seu nome')
    CHOICES = [('entrada','Entrada'), ('saida','Saída')]
    inorout = forms.ChoiceField(label='Entrada ou saída?', choices=CHOICES, widget=forms.RadioSelect)
    locname = forms.CharField(label='Digite o local') 
    opsticket = forms.CharField(label='Ticket')