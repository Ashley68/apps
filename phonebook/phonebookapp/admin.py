from django.contrib import admin
from myphonebook.models import Record

class RecordAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['last_name']}),
        (None,               {'fields': ['first_name']}),
        (None,               {'fields': ['work_phone']}),
        (None,               {'fields': ['home_phone']}),
        (None,               {'fields': ['notes']}),
        (None, {'fields': ['dob']}),
    ]

admin.site.register(Record, RecordAdmin)
