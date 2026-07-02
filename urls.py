from django.urls import path
from .views import GenerateReportView, AnalyticsSummaryView

urlpatterns = [
    path('generate/', GenerateReportView.as_view(), name='generate-report'),
    path('analytics/', AnalyticsSummaryView.as_view(), name='analytics-summary'),
]
