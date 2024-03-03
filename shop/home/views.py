from django.shortcuts import render
from django.views import View
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# from django.contrib.auth.mixins import LoginRequiredMixin
# from accounts.models import Person
# import json

class HomeView(View):
    def get(self, request):
        return render(request, 'home/homePage.html')