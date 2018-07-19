from django import forms

class TodoForm(forms.Form):
    task = forms.CharField(max_length=50,
            widget=forms.TextInput(attrs={"type":"text","name":"task","placeholder":"Add new Task"})               
            )