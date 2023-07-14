from rest_framework import serializers
from .models import Post,Person

class Postserializer(serializers.ModelSerializer):
    person_id = serializers.IntegerField()
    
    class Meta:
        model = Post
        fields = ['id','title','created_at','content','person_id']
        
        
class PersonSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Person
        fields = ['name','age','email']
        
class PersonSerializerbgd(serializers.ModelSerializer):
    class Meta : 
        model = Person
        fields = '__all__'