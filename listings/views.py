from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm, InquiryForm
from .models import Property


def home(request):
    form = InquiryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/?sent=1#contact')

    sent = request.GET.get('sent') == '1'
    properties = Property.objects.all()
    return render(request, 'home.html', {'properties': properties, 'sent': sent, 'form': form})


def booking(request, id):
    p = get_object_or_404(Property, id=id)
    message = ''
    form = BookingForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        booking = form.save(commit=False)
        booking.property = p
        booking.save()
        message = 'Thank you ' + booking.name + ', your booking request is received!'
    return render(request, 'Booking.html', {'p': p, 'message': message, 'form': form})
