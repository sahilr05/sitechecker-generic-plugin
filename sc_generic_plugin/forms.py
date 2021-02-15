from django import forms

from .models import GenericAlertPlugin


class GenericAlertForm(forms.ModelForm):
    class Meta:
        model = GenericAlertPlugin
        widgets = {
            "user_id": forms.NumberInput(
                attrs={"class": "form-control", "type": "number", "min": 1}
            )
        }
        fields = ("user_id", "active_status")
