from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from bookmyshow.serilizer import CreateBookingRequestDto


# Create your views here.

def create_booking(request):
    req = CreateBookingRequestDto(request.data)
    req.is_valid(raise_exception=True)
    try:
        
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class BooingViewSet(viewsets.ModelViewSet):

    def delete_booking(self,request):
        pass

    def edit_booking(self,request):
        pass