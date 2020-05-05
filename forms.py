from django import forms

class ResponseForm(forms.Form):
    content = forms.CharField()



class CommentForm(forms.Form):
    content = forms.CharField()
    