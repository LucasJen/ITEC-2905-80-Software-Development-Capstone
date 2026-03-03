from django.shortcuts import render, redirect
from .models import Place
from .forms import NewPlaceForm


def place_list(request):

    if request.method == 'POST':
        # Create new place
        form = NewPlaceForm(request.POST)  # create a form the data in the request
        place = form.save() # create a model object from form
        if form.is_valid(): # validation against DB constraints
            place.save() #saves place to db
            return redirect('place_list') #reloads home page.

    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm() # used to create html
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})

def about(request):
    author='Lucas'
    about= 'A website to create a list of places to visit'
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about})
