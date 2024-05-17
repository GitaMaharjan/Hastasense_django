from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Category
from .models import Content
from .models import Word
from .models import Feedback

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email','username', 'password','first_name','last_name','is_staff')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_dat):
        user = User.objects.create_user(**validated_dat)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
class CategorySerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, use_url=True)

    class Meta:
        model = Category
        fields = ['category_id', 'category_title', 'image', 'slug']

        
        
class ContentSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    class Meta:
        model = Content
        fields = ['content_id', 'content_title', 'content_image', 'content_sign_video', 'slug', 'category']
        
class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ['word_id', 'word_title', 'word_image', 'word_video_file', 'content']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        # fields = ['review_id','title', 'description', 'user', 'created_at']
        fields = '__all__'
        




# # detection
# class DetectionResultSerializer(serializers.Serializer):
#     detected_sign = serializers.CharField()
#     detected_emotion = serializers.CharField()