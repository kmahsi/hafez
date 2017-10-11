from __future__ import unicode_literals
from random import randint

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics
from hafez_telegram_bot.models import Hafez_Fall, UserInformation
from .serializer import HafezFallSerializer
from rest_framework.permissions import AllowAny
import json


class HafezFallViewSet(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = HafezFallSerializer

    def get_queryset(self):
        count = Hafez_Fall.objects.count()
        r = randint(0, count - 1)

        queryset = Hafez_Fall.objects.filter()[r:r+1]
#	print(queryset)
        return queryset


@csrf_exempt
def set_user_id(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        user_id_get = data.get("user_id", "")
        username_get = data.get("username", "")
        first_name_get = data.get("first_name", "")
        last_name_get = data.get("last_name", "")
        user_get = UserInformation.objects.filter(user_id=user_id_get).first()
        if user_get is None:
            user = UserInformation.objects.create(user_id=user_id_get, username=username_get, first_name=first_name_get,
                                                  last_name=last_name_get)
            user.save()
            return JsonResponse({"user": "جدید", "status": "فعال"})
        else:
            return JsonResponse({"user": "وجوددارد", "status": user_get.status})
