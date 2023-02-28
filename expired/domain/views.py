from .models import *
from django.shortcuts import render, redirect, HttpResponseRedirect
from rest_framework import generics, authentication, viewsets
import requests
from rest_framework.response import Response
from django.http import JsonResponse
from .serializers import *
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination


class domain(viewsets.ModelViewSet):
    queryset = AllDomain.objects.all()
    serializer_class = AllDomainSerializer
    pagination_class = PageNumberPagination
    page_size = 2
