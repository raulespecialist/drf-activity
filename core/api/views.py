from django.shortcuts import render
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response
import requests
from .models import Activity
from rest_framework import viewsets
from .serializers import ActivitySerializer

class ActivitiesView(APIView):
    def get(self, request):
        try:
            response = requests.get("https://www.boredapi.com/api/activity")
            data = response.json()
            # For validate activity not exist for this user
            if Activity.objects.filter(user=request.user,activity=data["activity"]).exists():
                return Response({"error":"Activity already exists for this user."}, status=400)
            serializer = ActivitySerializer(data=data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=200)
            else:
                return Response(serializer.errors, status=400)
        except requests.exceptions.RequestException as e:
            return Response(str(e), status=500)
        except Exception as e:
            return Response(str(e), status=500)

class ActivityUpdateView(APIView):
    def patch(self, request, id):
        try:
            activity = Activity.objects.get(pk=id)
            serializer = ActivitySerializer(activity, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(status=204)
            else:
                return Response(serializer.errors, status=400)
        except Activity.DoesNotExist:
            return Response({"error":"Activity not found."}, status=404)

class UserActivityViewSet(viewsets.ViewSet):
    def list(self, request):
        user = request.user
        activities = Activity.objects.filter(user=user)
        if not activities:
            return Response({"error":"Activities not found for this user."}, status=404)
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)