from django.contrib import admin
import campaigns.models


class CampaignFilterInline(admin.TabularInline):
    model = campaigns.models.CampaignFilter
    extra = 2


@admin.register(campaigns.models.Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active',)
    inlines = (CampaignFilterInline,)
    list_filter = ('active',)


@admin.register(campaigns.models.Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
