from django.contrib.auth.models import User
from rest_framework import status, views
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.views import APIView
from .serializers import LoginSerializer
from django.contrib.auth import authenticate, login
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from .serializers import CategorySerializer
from .serializers import ContentSerializer
from .serializers import WordSerializer
from .serializers import FeedbackSerializer

from rest_framework.parsers import MultiPartParser
from .models import Category
from .models import Content
from .models import Word

from rest_framework.authtoken.models import Token
from django.http import JsonResponse
# from django.shortcuts import get_object_or_404


# class UserRegistrationAPIView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegistrationAPIView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # Log in the user after registration
            user = authenticate(request, username=user.username, password=request.data.get('password'))
            if user is not None:
                login(request, user)
                token = Token.objects.get_or_create(user=user)
                return Response({'user_id': user.id, 'token': token[0].key}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Failed to log in after registration'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                token = Token.objects.get_or_create(user=user)
                return Response({'message': 'Login successful' , 'user_id': user.id, 'token': token[0].key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class AllUsersView(APIView):
#     def get(self, request):
#          data = User.objects.all().values()
#          json_data = list(data) 
#          return JsonResponse(json_data, safe=False)

class AllUsersView(APIView):
    def get(self, request):
        queryset = User.objects.filter(is_staff=False, is_superuser=False)
        serializer = UserSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)

class AllAdminView(APIView):
    def get(self, request):
        queryset = User.objects.filter(is_staff=True, is_superuser=False)
        serializer = UserSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False) 
    
class LoginViewAdmin(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_superuser == 1 or user.is_staff == 1:
                login(request, user)
                token = Token.objects.get_or_create(user=user)
                return Response({'message': 'Login successful' , 'user_id': user.id,'is_staff':user.is_staff, 'token': token[0].key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddCategory(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddContent(APIView):
    def post(self, request, format=None):
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AllCategoryView(APIView):
    def get(self, request):
         data = Category.objects.all().values()
         json_data = list(data) 
        #  return JsonResponse(finalPredict())
         return JsonResponse(json_data, safe=False)    

class AddWord(APIView):
    def post(self, request, format=None):
        serializer = WordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AllContentView(APIView):
    def get(self, request):
         data = Content.objects.all().values()
         json_data = list(data) 
        #  return JsonResponse(finalPredict())
         return JsonResponse(json_data, safe=False) 
     
class AllWordView(APIView):
    def get(self, request):
         data = Word.objects.all().values()
         json_data = list(data) 
        #  return JsonResponse(finalPredict())
         return JsonResponse(json_data, safe=False) 



class AllContentByCategoryIdView(APIView):
    def post(self, request):
        category_id = request.data['category_id']
        if category_id is not None:
            content = Content.objects.filter(category=category_id).values()
            json_data = list(content)
            return JsonResponse(json_data, safe=False)
        else:
            return JsonResponse([], safe=False)


# class AllWordByContentIdView(APIView):
#     def post(self, request):
#         content_id = request.data['content_id']
#         if content_id is not None:
#             word = Word.objects.filter(content=content_id).values()  
#             data = Content.objects.filter(content_id=content_id).values()      
#             json_word_data = list(word)
#             # json_data = list(data)

#             return JsonResponse(json_word_data, safe=False)
#         else:
#             return JsonResponse([],[], safe=False)

class AllWordByContentIdView(APIView):
    def post(self, request):
        content_id = request.data.get('content_id')
        if content_id is not None:
            # Filter words and content data
            words = Word.objects.filter(content=content_id).values()
            content_data = Content.objects.filter(content_id=content_id).values()

            # Convert queryset to list of dictionaries
            json_word_data = list(words)
            json_content_data = content_data[0]

            # Return JsonResponse
            # return JsonResponse({'words': json_word_data, 'content': json_content_data,})
            if json_word_data or json_content_data:
                # Return JsonResponse with data
                return JsonResponse({'words': json_word_data, 'content': json_content_data})
            else:
                # Return JsonResponse with no data message
                return JsonResponse({'message': 'No data found for content_id {}'.format(content_id)}, status=404)
        else:
            # return JsonResponse({'words': [], 'content': []})
            return JsonResponse({'error': 'content_id is required'}, status=400)
        
class SingleWordView(APIView):
    def post(self, request):
        word_id = request.data.get('word_id')
        if word_id is not None:
            data = Word.objects.filter(word_id=word_id).values()
            word_data = data[0]
        #  return JsonResponse(finalPredict())
        return JsonResponse(word_data, safe=False) 

# delete user
class UserDeleteAPIView(APIView):
    def post(self, request):
            user_id = request.data.get('user_id')
            user = User.objects.get(id=user_id)
            
            # Delete the user object
            user.delete()
            
            return Response({'message': 'User deleted successfully'})

# delete category
class DeleteCategoryView(APIView):
    def post(self, request):
        category_id = request.data.get('category_id')
        try:
            category = Category.objects.get(pk=category_id)
            # Delete associated content
            content_ids = Content.objects.filter(category=category_id).values_list('pk', flat=True)
            Content.objects.filter(category=category_id).delete()
            # Delete associated words
            Word.objects.filter(content__in=content_ids).delete()
            # Delete category
            category.delete()
            return Response({"message": "Category and associated content and words deleted successfully"}, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"message": "Category does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteContentView(APIView):
    def post(self, request):
        content_id = request.data.get('content_id')
        try:
            content = Content.objects.get(pk=content_id)
            # Delete associated words
            Word.objects.filter(content=content_id).delete()
            # Delete content
            content.delete()
            return Response({"message": "Content and associated words deleted successfully"}, status=status.HTTP_200_OK)
        except Content.DoesNotExist:
            return Response({"message": "Content does not exist"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteWordView(APIView):
    def post(self, request):
            word_id = request.data.get('word_id')
            word = Word.objects.get(word_id=word_id)
            
            # Delete the user object
            word.delete()
            
            return Response({'message': 'Word deleted successfully'})


class UserById(APIView):
    def post(self, request):
        user_id = request.data['id']
        if user_id is not None:
            user = User.objects.filter(id=user_id).values()
            json_data = user[0]
            return JsonResponse(json_data, safe=False)
        else:
            return JsonResponse([], safe=False)
        
class AddAdmin(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    

class Validate_token(APIView):
    def post(self, request):
        token_from_request = request.data['token']
        try:
            token_obj = Token.objects.get(key=token_from_request)
            user = token_obj.user
        except Token.DoesNotExist:
            return JsonResponse({'valid_token': False, 'message': 'Token does not exist'}, status=400)

        # Compare tokens
        if token_from_request == token_obj.key:
            return JsonResponse({'valid_token': True, "username": user.username, 'message': 'Token is valid'})
        else:
            return JsonResponse({'valid_token': False, 'message': 'Token is not valid'}, status=400)

class Validate_token_Staff(APIView):
    def post(self, request):
        token_from_request = request.data['token']
        try:
            token_obj = Token.objects.get(key=token_from_request)
            user = token_obj.user
        except Token.DoesNotExist:
            return JsonResponse({'valid_token': False, 'message': 'Token does not exist'})
        if user.is_staff:
            return JsonResponse({'valid_token': True, "username": user.username, 'message': 'Token is valid for staff user'})
        else:
            return JsonResponse({'valid_token': False, 'message': 'Token is valid but user is not staff'})

class UserUpdateAPIView(APIView): 
     def put(self, request):
        try:
            user = User.objects.get(id=request.data['id'])
        except User.DoesNotExist:
            return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddFeedbackAPIView(APIView):
    def post(self, request):
        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

