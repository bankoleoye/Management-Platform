from django.contrib import admin
from .models import User, Session, Ticket


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email', 'mobile_number', 'role', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('username', 'email', 'mobile_number', 'duties')
admin.site.register(User,UserAdmin)

class SessionAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'description', 'session_date')
    list_filter = ('session_date')
    search_fields = ('title', 'description')
admin.site.register(Session, SessionAdmin)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id','ticket_title', 'ticket_description')
    list_filter = ('ticket_title')
    search_fields = ('ticket_title')
admin.site.register(Ticket, TicketAdmin)
