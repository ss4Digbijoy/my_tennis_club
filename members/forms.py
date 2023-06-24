from django import forms
def check(b):
    if len(b)>10:
        raise forms.ValidationError("10 exceeding")
def check2(v):
    if not(v.endswith("gmail.com")):
        raise forms.ValidationError("EMAIL NOT VALID")
    
class contfr(forms.Form):
    Name=forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}),error_messages={'required': "req"}, validators=[check])
    msg=forms.CharField(label="Message",required=True,widget=forms.Textarea(attrs={'placeholder': 'ENTER YOUR MSG HERE'}))
    email=forms.EmailField(required=True, label='EMAIL',validators=[check2])