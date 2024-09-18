from django.shortcuts import render, get_object_or_404
from .models import Item

def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'item_detail.html', {'item': item})

def item_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        Item.objects.create(name=name, description=description)
    return render(request, 'item_create.html')

def item_update(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.name = request.POST.get('name')
        item.description = request.POST.get('description')
        item.save()
    return render(request, 'item_update.html', {'item': item})

def item_delete(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.delete()
    return render(request, 'item_delete.html', {'item': item})
