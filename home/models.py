from django.db import models
    
class Home(models.Model):
    home_id = models.IntegerField(primary_key=True)
    home_name = models.CharField(max_length=30)
    rooms_number = models.IntegerField()
    hotel_name = models.CharField(max_length=50,default="mans")
    
    def __str__ (self):
        return f"{self.home_name} yea mans ${self.rooms_number}"
    