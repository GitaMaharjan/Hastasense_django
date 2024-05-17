from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from .views import MyModelViewSet
from .views import LoginView
from .views import UserRegistrationAPIView
from .views import AllUsersView
from .views import AllAdminView
from .views import LoginViewAdmin
from .views import AddCategory
from .views import AddContent
from .views import AllCategoryView
from .views import AllContentView
from .views import AllWordView
from .views import AllContentByCategoryIdView
from .views import AllWordByContentIdView
from .views import SingleWordView
from .views import UserDeleteAPIView
from .views import DeleteCategoryView
from .views import DeleteContentView
from .views import AddWord
from .views import DeleteWordView
from .views import UserById
from .views import AddAdmin
from .views import Validate_token
from .views import Validate_token_Staff
from .views import UserUpdateAPIView
from .views import AddFeedbackAPIView
from .views import GetAllFeedbackAPIView


# router = DefaultRouter()
# router.register(r'users', MyModelViewSet)

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='user_registration'),
    path('login/', LoginView.as_view(), name='login'),
    path("users/", AllUsersView.as_view(), name="allusers"),
    path("loginadmin/", LoginViewAdmin.as_view()  , name="admin_signin"),
    path("addcategory/", AddCategory.as_view()  , name="add_category"),
    path("addcontent/", AddContent.as_view()  , name="add_content"),
    path("addword/", AddWord.as_view()  , name="add_word"),

    
    # get data category
    path("getcategory/", AllCategoryView.as_view()  , name="get_category"),
    path("getcontent/", AllContentView.as_view()  , name="get_category"),
    path("getword/", AllWordView.as_view()  , name="get_word"),
    path("getcontentbycategoryid/", AllContentByCategoryIdView.as_view(), name="get_content_by_categoryid"),
    path("getwordbycontentid/", AllWordByContentIdView.as_view(), name="get_word_by_contentid"),
    path("getsingleword/", SingleWordView.as_view()  , name="get_single_word"),

    # delete user
    path("deleteuserbyid/", UserDeleteAPIView.as_view() , name="delete_user"),
    
    # delete category
    path('deletecategory/', DeleteCategoryView.as_view(), name='delete_category'),
     # delete content
    path('deletecontent/', DeleteContentView.as_view(), name='delete_content'),
    # delete word
    path('deleteword/', DeleteWordView.as_view(), name='delete_word'),
    
    
    # get loggedin user
    path("usersid/", UserById.as_view(), name="allusers"),
    
    # Add Admin
    path("addadmin/", AddAdmin.as_view(), name="add_admin"),
    
    path("validateAdmin/", Validate_token.as_view(), name="validate_admin"),
    
    # user role
    path("validatestaffview/", Validate_token_Staff.as_view(), name="validate_staff_view"),
    
    # edit profile
    path("editprofile/", UserUpdateAPIView.as_view(), name="edit_profile"),
    
    path("addfeedback/", AddFeedbackAPIView.as_view(), name="add_feedback"),
    
    # alladmin
    path("alladmin/", AllAdminView.as_view(), name="all_admin"),


    path('feedback/', GetAllFeedbackAPIView.as_view(), name='get_all_feedback'),


]