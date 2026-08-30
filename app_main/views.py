from django.shortcuts import render

from .models import CourseModel
from .serializer import CourseSerializer
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response


class CourseCreateView(GenericAPIView):
    serializer_class = CourseSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data={
                "message":"Course created successfully",
                "course":serializer.data
            },
            status=status.HTTP_201_CREATED
        )


class CourseListView(GenericAPIView):
    serializer_class =  CourseSerializer
    queryset = CourseModel.objects.all()

    def get(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)

        return Response(
            data={
                "message":"Product list fetched successfully",
                "count":self.get_queryset().count(),
                "products":serializer.data
            },
            status=status.HTTP_200_OK
        )


class CourseDetailView(GenericAPIView):
    serializer_class = CourseSerializer
    queryset = CourseModel.objects.all()

    def get(self, request, pk):
        course = self.get_object()
        serializer = self.get_serializer(course)

        return Response(
            data={
                "message":"Course detail fetched successfully",
                "course":serializer.data
            },
            status=status.HTTP_200_OK
        )


class CoursePartialUpdateView(GenericAPIView):
    serializer_class = CourseSerializer
    queryset = CourseModel.objects.all()

    def patch(self, request, pk):
        course = self.get_object()
        serializer = self.get_serializer(data=request.data, instance=course, partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data={
                "message":"Course partial update completed successfully",
                "course":serializer.data
            },
            status=status.HTTP_200_OK
        )


class CourseUpdateView(GenericAPIView):
    serializer_class = CourseSerializer
    queryset = CourseModel.objects.all()

    def put(self, request, pk):
        course = self.get_object()
        serializer = self.get_serializer(data=request.data, instance=course)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            data={
                "message":"Course update completed successfully",
                "course":serializer.data
            },
            status=status.HTTP_200_OK
        )


class CourseDeleteView(GenericAPIView):
    queryset = CourseModel.objects.all()

    def delete(self, request, pk):
        course = self.get_object()

        course.delete()

        return Response(
            data={
                "message":"Course deleted successfully"
            },
            status=status.HTTP_200_OK
        )