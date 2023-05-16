from django.shortcuts import render
from . import forms


def index(request):
    return render(request, 'index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        action = request.POST['radio_button']
        call_total = request.POST['call_total']
        sms_total = request.POST['sms_total']
        total = request.POST['total']

        my_bill = CalculateBill()
        my_bill.calc(action, call_total, sms_total, total)

        call_total = my_bill.get_call_total()
        sms_total = my_bill.get_sms_total()
        total = my_bill.get_total()

        form.fields['call_total'].initial = f"R {call_total}"
        form.fields['sms_total'].initial = f"R {sms_total}"
        form.fields['total'].initial = f"R {total}"

    return render(request, 'radio_button_bill.html', {'form': form})


def cutter(word):
    new_word = ""
    for char in word:
        if char != "R" and char != " ":
            new_word += char
    return new_word


class CalculateBill:

    def __init__(self):
        self.callPrice = 2.75
        self.smsCost = 0.75
        self.callTotal = 0
        self.smsTotal = 0
        self.theTotal = 0

    def calc(self, x, call_total, sms_total, total):

        x = x.strip()
        call_total = cutter(call_total)
        sms_total = cutter(sms_total)
        total = cutter(total)

        if float(call_total) >= self.callTotal:
            self.callTotal = float(call_total)
        if float(sms_total) >= self.smsTotal:
            self.smsTotal = float(sms_total)
        if float(total) >= self.theTotal:
            self.theTotal = float(total)

        if x == "call":
            self.callTotal += self.callPrice
            self.theTotal += self.callPrice

        elif x == "sms":
            self.smsTotal += self.smsCost
            self.theTotal += self.smsCost

    def get_call_total(self):
        return self.callTotal

    def get_sms_total(self):
        return self.smsTotal

    def get_total(self):
        return self.theTotal

