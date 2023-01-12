from django import forms


class NoteForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()
