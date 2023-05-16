from django import forms


def check_text(value):
    action = value.lower

    if action != "sms" or action != "call":
        raise forms.ValidationError("MAKE A CALL OR AN SMS")


class FormName(forms.Form):
    text = forms.CharField(widget=forms.Textarea,
                           label="Action",
                           validators=[check_text],
                           initial="enter call or sms")

    call_total = forms.DecimalField(decimal_places=3,
                                    widget=forms.TextInput(attrs={"readonly": "readonly"}),
                                    label="Call total",
                                    initial=f"R {0.00}", )

    sms_total = forms.DecimalField(decimal_places=3,
                                   widget=forms.TextInput(attrs={"readonly": "readonly"}),
                                   label="SMS total",
                                   initial=f"R {0.00}", )

    total = forms.DecimalField(decimal_places=3,
                               widget=forms.TextInput(attrs={"readonly": "readonly"}),
                               label="Total",
                               initial=f"R {0.00}", )
