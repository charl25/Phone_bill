from django.shortcuts import render
from . import forms


def index(request):
    return render(request, 'index.html')


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        action = request.POST['text']

        my_bill = CalculateBill()
        my_bill.calc(action)

        form.fields['total'].initial = f"R {my_bill.total()}"

    return render(request, 'calculate_bill.html', {'form': form})


class CalculateBill:

    def __init__(self):
        self.callPrice = 2.75
        self.smsCost = 0.75
        self.theTotal = 0

    def calc(self, x):

        bill_list = x.split(",")

        for word in bill_list:
            word = word.strip()
            if word == "call":
                self.theTotal += self.callPrice
            elif word == "sms":
                self.theTotal += self.smsCost
            else:
                continue

    def total(self):
        return self.theTotal
