from django import forms
#noinspection PyUnresolvedReferences
from django.forms import ModelForm
#noinspection PyUnresolvedReferences
from .models import Todo

class TodoForm(forms.ModelForm):
	title= forms.CharField(widget= forms.TextInput(attrs={'placeholder': 'Add a new task in list'}))

	class Meta:
		model = Todo
		fields = '__all__'