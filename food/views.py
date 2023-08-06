from django.http import HttpResponse

from food.models import Item


# Create your views here.
def index(request):
    item_list = Item.objects.all()
    return HttpResponse(item_list)


def item(request):
    return HttpResponse('<h1>This is an item view</h1>')
