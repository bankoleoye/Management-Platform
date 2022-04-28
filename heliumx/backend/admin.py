from django.contrib import admin
from .models import User, Sessions, Ticket, Subscription, NewsLetter


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'mobile_number', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('username', 'email', 'mobile_number', 'duties')
admin.site.register(User,UserAdmin)

class SessionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'date')
    list_filter = ('date',)
    search_fields = ('title', 'description')
admin.site.register(Sessions, SessionAdmin)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_filter = ('title',)
    search_fields = ('title',)
admin.site.register(Ticket, TicketAdmin)

class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'topic')
    list_filter = ('title', 'topic')
    search_fields = ('title', 'topic')
admin.site.register(NewsLetter, NewsLetterAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('title', 'package', 'price', 'plans')
    list_filter = ('title', 'package', 'price')
    search_fields = ('title', 'package', 'price')
admin.site.register(Subscription, SubscriptionAdmin)
