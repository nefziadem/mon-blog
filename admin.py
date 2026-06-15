from django.contrib import admin
from .models import Article, Message

admin.site.register(Article)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['nom', 'email', 'date_envoi', 'lu']
    list_filter = ['lu']
    readonly_fields = ['nom', 'email', 'message', 'date_envoi']