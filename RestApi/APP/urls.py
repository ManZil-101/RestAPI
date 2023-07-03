
from django.urls import path,include

from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
  # path('', views.home),
  # path('student/', views.add_student),
  #  path('student_patch/<id>/', views.patch_student ),
  # path('student_update/<id>/', views.update_student ),
  # path('student_delete/<id>/', views.delete_student),
  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  path('get-book/', views.get_book),
  path('student/', views.StudentGeneric.as_view()),
  path('student/<id>', views.StudentGeneric1.as_view()),
  # path('student/', views.StudentAPI.as_view()),
  path('register/', views.RegisterUser.as_view()),

]
