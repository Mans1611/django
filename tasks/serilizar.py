from rest_framework import serializers

from .models import Tasks

class TasksSerializerName(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['name']
class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields ='__all__' 
        
    def create(self,data):
        
        name = data.pop('name')
        instance = self.Meta.model(**data)
        if name is not None:
            print("name is not none")
            instance.set_password(name)
        instance.save()
        return instance