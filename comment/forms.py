from dataclasses import fields
from pyexpat import model
from django import forms
from comment.models import comment

class commentform(forms.ModelForm):
    class Meta():
        model=comment
        fields={"firstname","lastname","description","contact","email"}