from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('train', 'passenger', 'state_depart', 'state_arrive', 'date', 'time', 'carriage', 'seat', 'platform')
    # You can also add search fields and filters if needed
    search_fields = ('train', 'passenger', 'state_depart', 'state_arrive', 'seat', 'platform')
    list_filter = ('train', 'state_depart', 'state_arrive', 'date')

admin.site.register(Ticket, TicketAdmin)
