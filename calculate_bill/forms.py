from django import forms


def check_text(value):

    action = value.lower

    if action != "sms" or action != "call":
        raise forms.ValidationError("MAKE A CALL OR AN SMS")


class FormName(forms.Form):
    text = forms.CharField(widget=forms.Textarea,
                           label="Enter bill string",
                           validators=[check_text])
    total = forms.DecimalField(decimal_places=3,
                               widget=forms.TimeInput(attrs={"readonly": "readonly"}),
                               initial =f"R {0.00}",)