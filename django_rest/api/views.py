from django.shortcuts import render
# from django.contrib.auth.models import User,Group
from rest_framework import viewsets
# from api.serializers import UserSeriaLizer, GroupSerializer
from api.serializers import EventSerialLizer, GuestSerializer
from api.models import Event, Guest
# Create your views here.
# ViewSets定义视图的展现形式
# class UserViewSet(viewsets.ModelViewSet):
#     '''API endpoint that allows users to be viewed or edited'''
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSeriaLizer
#
# class GroupViewSet(viewsets.ModelViewSet):
#     '''API endpoint that allows groups to be viewed or edited'''
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer

class EventViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allows events to be viewed or edited.
    '''
    queryset = Event.objects.all()
    serializer_class = EventSerialLizer

class GuestViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that guests to be viewed or edited.
    '''
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer


