from django import forms
from bloodcamps.models import bloodcamp
class newcamp(forms.ModelForm):
    class Meta:
        model=bloodcamp
        fields='__all__'
