from django.shortcuts import render
from django.http import HttpResponse
from.models import StudentModel
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser
# Create your views here.
@csrf_exempt
def students(request):
        if request.method == 'GET':
                model_instance =  StudentModel.objects.all()
                ser_data=StudentSerializer(model_instance,many=True)
                py_data=ser_data.data
                json_data=JSONRenderer().render(py_data)
                return HttpResponse(json_data)

        if request.method == 'POST':
                req_data=request.body
                stream_data=io.BytesIO(req_data)
                py_data=JSONParser().parse(stream_data)
                de_ser=StudentSerializer(data=py_data)
                if de_ser.is_valid():
                        de_ser.save()
                msg={'msg':'data submitted'}
                return HttpResponse(JSONRenderer().render(msg))
@csrf_exempt      
def student(request,pk):
        try:
                stu=StudentModel.objects.get(id=pk) #old data
        except:
                msg={'msg':'record or student data not found'}
                return HttpResponse(JSONRenderer().render(msg))
        
        if request.method == 'PUT':
                req_data=request.body
                stream_data=io.BytesIO(req_data)
                py_data=JSONParser().parse(stream_data)
                print(py_data) #new data
                de_ser=StudentSerializer(stu,data=py_data,partial=True) #pass instance
                if de_ser.is_valid():
                        de_ser.save()
                msg={'msg':'record updated'}
                return HttpResponse(JSONRenderer().render(msg))
        if request.method == 'DELETE':
                stu.delete()
                msg={'msg':'record deleted'}
                return HttpResponse(JSONRenderer().render(msg))