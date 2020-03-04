
from django.contrib import admin

from .models import DemoModel


@admin.register(DemoModel)
class DemoModelAdmin(admin.ModelAdmin):
    autocomplete_fields = ('locality',)
