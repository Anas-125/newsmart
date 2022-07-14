from django.contrib import admin
from .models import CosineSimilarity, WebSearching, User

# Register your models here.
admin.site.register(WebSearching)
admin.site.register(CosineSimilarity)
admin.site.register(User)
