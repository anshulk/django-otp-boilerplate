from random import randint

from django.shortcuts import render
from django.core.exceptions import ValidationError

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .models import Otp
from user.models import User


@api_view(['GET'])
@permission_classes([])
def send_otp(request):
    phone = request.query_params.get('phone', None)
    if phone is None:
        return Response({'error': 'Missing phone param.'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(phone=phone)
    except:
        try:
            user = User(phone=phone)
            user.full_clean(exclude=['password'])
            user.save()
        except ValidationError as e:
            return Response({'error': e}, status.HTTP_400_BAD_REQUEST)

    # Write OTP sending logic here. Using any third party api_view
    
    Otp.objects.create(user=user, otp=randint(111111, 999999))
    return Response({'message': 'We\'ve sent an OTP to your phone'}, status=status.HTTP_201_CREATED)
