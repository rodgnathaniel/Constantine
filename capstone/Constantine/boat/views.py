from django.http import HttpResponse
from django.shortcuts import render
# from .models import Product


def boat_view(request):

    return render(request, "boat/boat.html", {})
# # Create your views here.
# def home_view(request):
#
#     my_context = {
#         'title': "has good deals",
#         'my_number': 123,
#         'my_list': ['Plush Toys', 'Posters', 'Clothes', 'MP3\'s', 'Foreign Candy'],
#         'my_html': "<h3>sells lots of things</h3>"
#     }
#     return render(request, "products/home.html", my_context)



