from django.contrib import admin
from .models import Video, Comment


class VideoInline(admin.StackedInline):
    model = Comment
    extra = 1


class VideoAdmin(admin.ModelAdmin):
    inlines = [VideoInline]
    list_filter = ["VideoTable"]


admin.site.register(Video)
admin.site.register(Comment)
