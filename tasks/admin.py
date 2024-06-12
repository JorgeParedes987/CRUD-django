from django.contrib import admin
from .models import Talk
# Register your models here.
class TalkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', )
admin.site.register(Talk,TalkAdmin)
