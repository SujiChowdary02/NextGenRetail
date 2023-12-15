from django.contrib import admin
from dataset.models import Dataset

@admin.register(Dataset)
class DatasetModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'uploaded_by', 'uploaded_at')
    list_filter = ('uploaded_by', 'uploaded_at')
    search_fields = ('name', 'uploaded_by__email')
    date_hierarchy = 'uploaded_at'
    actions = ['delete_selected']

    def save_model(self, request, obj, form, change):
        if not obj.uploaded_by_id:
            obj.uploaded_by = request.user
        super().save_model(request, obj, form, change)
    
    def delete_selected(self, request, queryset):
        for obj in queryset:
            obj.delete()
        self.message_user(request, f"{len(queryset)} datasets were deleted.")
    delete_selected.short_description = "Delete selected datasets"
