from django import forms


class NoteForm(forms.Form):
    title = forms.CharField(label='Название')
    text = forms.CharField(widget=forms.Textarea(), label='Текст')
