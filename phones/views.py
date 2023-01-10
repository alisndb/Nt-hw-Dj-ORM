from django.shortcuts import render
from phones.models import Phone


def catalog_view(request):
    sort = request.GET.get('sort')

    if sort == 'name':
        phone_objects = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phone_objects = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phone_objects = Phone.objects.all().order_by('-price')
    else:
        phone_objects = Phone.objects.all()

    context = {
        'phones': phone_objects
    }

    return render(request, 'catalog.html', context)


def product_view(request, product):
    phone_object = Phone.objects.filter(slug=f'{product}')
    phone_object = [i for i in phone_object][0]

    context = {
        'phone': phone_object
    }

    return render(request, 'product.html', context)
