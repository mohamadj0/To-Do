from django import forms
from .models import Todo


class TodoCreateForms(forms.Form):
    titel = forms.CharField()
    body = forms.CharField()
    created = forms.DateTimeField()

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'body', 'created')