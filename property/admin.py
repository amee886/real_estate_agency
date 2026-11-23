from django.contrib import admin
from django.contrib.auth.models import User
from .models import Flat,Complaint,Owner

class OwnerInline(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ['owner']
    extra = 3

class AuthorAdmin(admin.ModelAdmin):
    search_fields = ("town","address")
    readonly_fields = ["created_at"]
    list_display = ["address","price","new_building","construction_year","town"]
    list_editable = ["new_building"]
    list_filter = ["new_building","rooms_number","has_balcony"]
    raw_id_fields = ["liked_by"]
    inlines = [OwnerInline]

class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ["complainant","flat"]
    

class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ["flats"]
admin.site.register(Owner,OwnerAdmin)
admin.site.register(Flat,AuthorAdmin)
admin.site.register(Complaint,ComplaintAdmin)
