from rest_framework import serializers
from.models import StudentModel
class StudentSerializer(serializers.Serializer):
    sname=serializers.CharField()
    rollno=serializers.CharField()
    course=serializers.CharField()

    def create(self, validated_data):
        return StudentModel.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.sname=validated_data.get('sname',instance.sname)
        instance.rollno=validated_data.get('rollno',instance.rollno)        
        instance.course=validated_data.get('course',instance.course)
        instance.save()
        return instance