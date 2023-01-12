from django import forms
from django.core.exceptions import ValidationError


class NoteForm(forms.Form):
    title = forms.CharField(validators=[])
    text = forms.CharField()

    def clean_text(self):
        raise ValidationError("текст неверный в принципе!")
        return self.data['text'].strip()

    def clean(self):
        if 'title' in self.cleaned_data:
            self.cleaned_data['title'] = self.cleaned_data['title'].upper()
            return self.cleaned_data

    #TODO clean
    #TODO errors