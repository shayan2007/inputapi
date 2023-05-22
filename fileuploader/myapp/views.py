from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

class FileUploadView(APIView):
    def get(self, request):
        return render(request, 'upload.html')

    def post(self, request, format=None):
        file_obj = request.FILES.get('file')
        # Process the file here
        return Response({'message': 'File uploaded successfully'})
