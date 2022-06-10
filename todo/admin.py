import datetime

import pytz
from django.contrib import admin

from todo.models import Todo


class TodoAdmin(admin.ModelAdmin):
    date_hierarchy = 'deadline'
    empty_value_display = '???'
    list_display = [
        'title', 'description', 'is_done', 'deadline',
        'created_at', 'updated_at', 'is_relevant',
    ]
    fields = [
        'title', 'description', 'is_done', 'deadline',
        'created_at', 'updated_at',
    ]
    readonly_fields = ['created_at', 'updated_at']

    list_filter = ('created_at', 'is_done',)

    list_editable = ('is_done',)

    @admin.display(boolean=True)
    def is_relevant(self, obj):
        return datetime.datetime.now(tz=pytz.UTC) < obj.deadline


admin.site.register(Todo, TodoAdmin)
