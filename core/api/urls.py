from django.urls import path
from .views import ActivitiesView, ActivityUpdateView, UserActivityViewSet

urlpatterns = [
    path("activities/", ActivitiesView.as_view(), name="activity"),
    path("activities/<int:id>/done", ActivityUpdateView.as_view(), name="activity_update"),
    path("user-activities/", UserActivityViewSet.as_view({'get':'list'}), name="user_activities")
]