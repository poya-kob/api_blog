from django.contrib import admin
from .models import Comments, Blog, BlogCategory

admin.site.register(Comments)
admin.site.register(Blog)
admin.site.register(BlogCategory)
