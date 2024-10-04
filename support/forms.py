from django import forms
from support.models import Support


class SendMessageForm(forms.ModelForm):
    message_text = forms.CharField(widget=forms.Textarea, label="", required=True)

    class Meta:
        model = Support
        fields = ['message_text']
