from rest_framework import fields, serializers
from .models import (
    Author ,
    Book ,
    Genre ,
    Publisher,
     ) 


class BookSerializer(serializers.ModelSerializer):
    publisher = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = ('title','summary','year', 'author','publisher')
        extra_kwargs = {
            # 'summery': {'write_only':True}
        }
    


class PublisherSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)

    class Meta:
        model= Publisher
        fields = ('name','phone','address','books')



class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)

    class Meta:
        model= Author
        fields = ('last_name','first_name','books')