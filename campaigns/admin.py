import redis
from django.contrib import admin
import campaigns.models
from cabinet.redis import REDIS_POOL


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
    list_display = (
        'id',
        'name',
        'dsp',
        'subscriber_selection_size',
        'pushes_sent',
        'active',
    )
    inlines = (CampaignFilterInline,)
    list_filter = ('active',)
    actions = [activate_campaigns, deactivate_campaigns]

    def pushes_sent(self, obj):
        try:
            client = redis.Redis(connection_pool=REDIS_POOL)
            value = client.get(f"stats:campaign:{obj.id}:total-count")
            try:
                return int(value)
            except TypeError:
                return 0
        except Exception:
            return 'error'

    pushes_sent.short_description = 'Pushes Sent'


@admin.register(campaigns.models.Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


@admin.register(campaigns.models.Dsp)
class DspAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'active',)
    list_filter = ('active',)
