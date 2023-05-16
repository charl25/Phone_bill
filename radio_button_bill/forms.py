from django import forms


class FormName(forms.Form):

    OPTIONS = [
        ('call', 'Call'),
        ('sms', 'SMS'),
    ]

    radio_button = forms.ChoiceField(widget=forms.RadioSelect,
                                     choices=OPTIONS)

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
