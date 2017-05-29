from django.http import HttpResponse
from .models import Items


def index(request):
    all_items = Items.objects.all()
    html = ''
    for items in all_items:
        url = 'oferty/' + str(items.id) + '/'
        html += '<a href="' + url + '">' + items.tytul + '</a><br>'

    return HttpResponse(html)


def detail(request, items_id):
    return HttpResponse("<h2>" " Szczegóły oferty: " + str(items_id) + "</h2>")
