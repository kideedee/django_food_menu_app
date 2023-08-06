from django.http import HttpResponse
from django.template import loader

from food.models import Item


# Create your views here.
def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {

    }
    return HttpResponse(template.render(context, request))


def item(request):
    return HttpResponse('<h1>This is an item view</h1>')
