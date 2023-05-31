from django import forms


class FormCalculate(forms.Form):

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


class FormSettings(forms.Form):

    sms_cost = forms.DecimalField(decimal_places=3,
                                   widget=forms.NumberInput,
                                   label="SMS total",
                                   initial=f"R {0.00}", )

    call_cost = forms.DecimalField(decimal_places=3,
                               widget=forms.NumberInput,
                               label="Total",
                               initial=f"R {0.00}", )


