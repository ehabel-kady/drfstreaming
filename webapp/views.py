import time
from adrf.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.views.generic import View  
from django.shortcuts import render
from django.http import StreamingHttpResponse
from rest_framework import status
from faker import Faker
import random
import asyncio
import aioredis




# Create your views here.

class GenerateStreamView(APIView):

    renderer_classes = [JSONRenderer]


    async def name_generator(self, data):
        
        
        while True:
            yield await data.get_message()
            await asyncio.sleep(1)

    async def get(self,request): 
        redis_cli = await aioredis.from_url(url='rediss://default:AVNS_MQwdlpMWzyPCj9-r4VS@streaming-redis-do-user-1200260-0.c.db.ondigitalocean.com:25061')
        pubsub = redis_cli.pubsub()
        await pubsub.subscribe('last_vehicle_states')
        
        name = self.name_generator(pubsub)
        #return Response({},status.HTTP_200_OK)
        response =  StreamingHttpResponse(name,status=200, content_type='text/event-stream')
        response['Cache-Control']= 'no-cache',
        return response
    

class HomeView(View):

    def get(self,request):
        return render(request,'index.html')

