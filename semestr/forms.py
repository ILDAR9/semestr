# -*- coding: utf-8 -*-
from django import forms
import re

class Signal_info(forms.Form):
    signals = forms.CharField(help_text='Введите последовательность отсчетов:')
    step = forms.IntegerField(min_value=0, max_value=10, help_text="Введите шаг децимации")
    def clean_signals(self):
        data = self.cleaned_data['signals']
        for x in data.split():
            if not x.isdigit():
                raise forms.ValidationError("Были введены символы не соответствующие цифрам!")
#            if re.match("^\d+\.?\d+?$", x) is None:
#                raise forms.ValidationError("Были введены символы не соответствующие цифрам!")
        return data

class SignalFileInfo(forms.Form):
    signals_file = forms.FileField(help_text="Вставить текстовый файл с последовательностью отсчетов")
    step = forms.IntegerField(min_value=0, max_value=10, help_text="Введите шаг децимации")