from django.contrib import admin
from app.models import user, author, Blog, Comment
# Register your models here.



admin.site.register(user)
admin.site.register(author)
admin.site.register(Blog)
admin.site.register(Comment)