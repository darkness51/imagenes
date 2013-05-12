from django import forms
from subir.models import Foto

class FormFoto(forms.ModelForm):
	class Meta:
		model = Foto