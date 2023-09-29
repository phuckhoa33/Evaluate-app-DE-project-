from django.contrib import admin
from .models import SearchQuery, SearchResult, AnalyticData

# Register your models here.
admin.register(SearchQuery, SearchResult, AnalyticData)
