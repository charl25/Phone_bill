from django import forms


class FormName(forms.Form):
    text = forms.CharField(widget=forms.Textarea,
                           label="Enter bill string",
                           )
    total = forms.DecimalField(decimal_places=3,
                               widget=forms.TimeInput(attrs={"readonly": "readonly"}),
                               initial =f"R {0.00}",)