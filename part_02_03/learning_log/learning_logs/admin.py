from django.contrib import admin

from .models import Topic, Entry

# Register your models here.
@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    pass