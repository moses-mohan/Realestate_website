from django.shortcuts import render, redirect, get_object_or_404
from .models import Property, Booking, Inquiry


def home(request):
    if request.method == 'POST':
        Inquiry.objects.create(
            name=request.POST.get('name', ''),
            email=request.POST.get('email', ''),
            mobile=request.POST.get('mobile', ''),
            address=request.POST.get('address', ''),
            city=request.POST.get('city', ''),
            district=request.POST.get('district', ''),
            message=request.POST.get('message', ''),
        )
        return redirect('/?sent=1#contact')

    sent = request.GET.get('sent') == '1'
    properties = Property.objects.all()
    return render(request, 'home.html', {'properties': properties, 'sent': sent})


def booking(request, id):
    p = get_object_or_404(Property, id=id)
    message = ''
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        Booking.objects.create(property=p, name=name, phone=phone)
        message = 'Thank you ' + name + ', your booking request is received!'
    return render(request, 'booking.html', {'p': p, 'message': message})