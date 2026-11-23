from django import forms

from .models import Booking, Inquiry


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'mobile', 'address', 'city', 'district', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your email'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Mobile number'}),
            'address': forms.TextInput(attrs={'placeholder': 'Your address'}),
            'city': forms.TextInput(attrs={'placeholder': 'City'}),
            'district': forms.TextInput(attrs={'placeholder': 'District'}),
            'message': forms.Textarea(attrs={'placeholder': 'Which property are you interested in?'}),
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone number'}),
        }
