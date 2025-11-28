from django.urls import path
from .views import ReportViewSet

report_list = ReportViewSet.as_view({
    "get": "summary"
})
report_user = ReportViewSet.as_view({
    "get": "user"
})

urlpatterns = [
    path("summary", report_list, name="report-summary"),
    path("user/<int:pk>", report_user, name="report-user"),
]