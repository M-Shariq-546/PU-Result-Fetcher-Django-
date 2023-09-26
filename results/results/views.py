# views.py

from django.shortcuts import render
from django.http import JsonResponse
import requests

def index(request):
    return render(request, 'index.html')

def get_student(request):
    roll_no = request.GET.get('roll_no')
    api_url = f'https://api_last-1-j0851899.deta.app/{roll_no}'  # Update with your API URL

    try:
        response = requests.get(api_url , verify=False)
        data = response.json()
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)})

  
