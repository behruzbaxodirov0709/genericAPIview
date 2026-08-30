from rest_framework.urls import path
from .views import *


urlpatterns = [
    path("create/", CourseCreateView.as_view()),
    path("list/", CourseListView.as_view()),
    path("detail/<int:pk>", CourseDetailView.as_view()),
    path("partial-update/<int:pk>", CoursePartialUpdateView.as_view()),
    path("update/<int:pk>", CourseUpdateView.as_view()),
    path("delete/<int:pk>", CourseDeleteView.as_view())
]