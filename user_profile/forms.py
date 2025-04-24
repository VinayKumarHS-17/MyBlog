from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic']
        widgets={
            'bio':forms.Textarea(attrs={
                'class':'form-control',
                'placeholder':'Tell us about yourself.....',
                'rows':'2',
            }),

            'profile_pic':forms.ClearableFileInput(attrs={
                'class':'form-control',
            })
        }