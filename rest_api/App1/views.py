from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Students
from .serializers import StudentSerializer

# Create your views here.
class StudentView(APIView):
    def get(self, request, *args, **kwargs):
        # Fetch all students
        result = Students.objects.all()
        # Serialize the data
        serializer = StudentSerializer(result, many=True)
        # Return the serialized data
        return Response({'status': 'success', "students": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request):
        # Serialize the incoming data
        serializer = StudentSerializer(data=request.data)
        # Validate and save the data
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            # Return errors if validation fails
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
