from rest_framework import serializers

from .models import Teacher

class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ['first_name', 'middle_name', 'last_name', 'st_subject']
