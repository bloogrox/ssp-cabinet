from django.contrib import admin
import campaigns.models


class CampaignFilterInline(admin.TabularInline):
    model = campaigns.models.CampaignFilter
    extra = 2


def activate_campaigns(modeladmin, request, queryset):
    queryset.update(active=True)


activate_campaigns.short_description = "Activate selected campaigns"


def deactivate_campaigns(modeladmin, request, queryset):
    queryset.update(active=False)


deactivate_campaigns.short_description = "Deactivate selected campaigns"


@admin.register(campaigns.models.Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active',)
    inlines = (CampaignFilterInline,)
    list_filter = ('active',)
    actions = [activate_campaigns, deactivate_campaigns]


@admin.register(campaigns.models.Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(campaigns.models.Dsp)
class DspAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active',)
    list_filter = ('active',)
