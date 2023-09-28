# student_info/views.py
from django.shortcuts import render
from fetcher.models import Student
import requests  # for making API requests

def index(request):
  return render(request , 'index.html')
  
def get_student_data(request):
    if request.method == 'POST':
        roll_no = request.POST.get('roll_no')
        api_url = f'https://pu_results_20-1-w0009924.deta.app/{roll_no}'  # Replace with your API endpoint
        try:
            response = requests.get(api_url)
            data = response.json()
            student_data = data.get('results')[0]
            student = Student(
                name=student_data['name'],
                father_name=student_data['father_name'],
                institute=student_data['institute'],
                degree=student_data['degree'],
                roll_no=student_data['roll_no'],
                reg_no=student_data['reg_no'],
            )
            student.save()
            return render(request, 'result.html', {'student': student})
        except Exception as e:
            return render(request, 'student_info/error.html', {'error_message': str(e)})
    else:
        return render(request, 'result.html')
