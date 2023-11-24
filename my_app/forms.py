from django.forms import ModelForm

from my_app.models import Criminal, Crime, Casuality, Witness, Offence

class CriminalForm(ModelForm):
    class Meta:
        model = Criminal
        fields = '__all__'


class CrimeForm(ModelForm):
    class Meta:
        model = Crime
        fields = '__all__'

class CasualityForm(ModelForm):
    class Meta:
        model = Casuality
        fields = '__all__'

class WitnessForm(ModelForm):
    class Meta:
        model = Witness
        fields = '__all__'

class OffenceForm(ModelForm):
    class Meta:
        model = Offence
        fields = '__all__'
    