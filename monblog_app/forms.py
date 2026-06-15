from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Votre nom'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'votre@email.com'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Votre message...',
            'rows': 6
        })
    )