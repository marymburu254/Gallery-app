from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import *

def index(request):
  title = 'MyGallery'
  today = dt.datetime.today()
  all_images = Image.get_images()
  locations = Location.get_location()
  parameters = {
    "title": title,
    "today": today,
    "all_images": all_images,
    "locations": locations,
  }
  return render(request, 'index.html', parameters)

def display_location(request,id):
  locations = Location.get_location()
  images = Image.objects.filter(img_location__id=id)
  parameters = {
    "locations": locations,
    "images": images,
  }
  return render(request, 'locations.html', parameters)

def search_results(request):
  locations = Location.get_location()
  if 'category' in request.GET and request.GET["category"]:
    search_term = request.GET.get("category")
    searched_images = Image.search_by_category(search_term)
    message = f"{search_term}"
    parameters = {
      "message": message,
      "images": images,
      "locations": locations,
    }
    return render(request, 'search.html',parameters)
  else:
      message = "Search item not found",
      return render(request, "search.html", {"message": message, "locations": locations})