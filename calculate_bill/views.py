from django.shortcuts import render
from . import forms


def index(request):
    return render(request, 'index.html')


def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        action = request.POST['text']
        total = request.POST['total']

        my_bill = CalculateBill()
        my_bill.calc(action, total)

        total = my_bill.total()

        form.fields['total'].initial = f"R {total}"

    return render(request, 'calculate_bill.html', {'form': form})


def cutter(word):
    new_word = ""
    for char in word:
        if char != "R" and char !=" ":
            new_word += char
    return new_word


class CalculateBill:

    def __init__(self):
        self.callPrice = 2.75
        self.smsCost = 0.75
        self.theTotal = 0

    def calc(self, x, old_total):

        old_total = cutter(old_total)

        if float(old_total)> self.theTotal:
            self.theTotal = float(old_total)
        x = x.strip()
        if x == "call":
            self.theTotal += self.callPrice
        elif x == "sms":
            self.theTotal += self.smsCost

    def total(self):
        return self.theTotal