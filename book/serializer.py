from rest_framework import serializers
from .models import Book,Category
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name','id']

class BooksSerializers(serializers.ModelSerializer):
    # name = serializers.CharField()
    # price = serializers.DecimalField(max_digits=5,decimal_places=2)
    # inventory = serializers.IntegerField()
    # stock = serializers.IntegerField(source='inventory')
    # new_price = serializers.SerializerMethodField(method_name='newPrice')
    category = CategorySerializers(read_only=True)
    class Meta:
        model = Book
        fields = ['name','category','price','author']
        
    def newPrice(self,book:Book):
        return book.inventory * 10