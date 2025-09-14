import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import ContactMessage


def export_as_csv(modeladmin, request, queryset):
    """
    Export selected messages to CSV
    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=contact_messages.csv'
    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Phone', 'Subject', 'Message', 'Created At'])

    for obj in queryset:
        writer.writerow([
            obj.name,
            obj.email,
            obj.phone,
            obj.subject,
            obj.message,
            obj.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        ])
    return response

export_as_csv.short_description = "Export Selected to CSV"


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

    # Add CSV export action
    actions = [export_as_csv]
