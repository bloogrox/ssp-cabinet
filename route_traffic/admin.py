from django.contrib import admin
import route_traffic.models


@admin.register(route_traffic.models.Router)
class RouterAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'node',
        'safe_uid',
        'dsp',
        'active',
    )


@admin.register(route_traffic.models.Dsp)
class DspAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)

@admin.register(route_traffic.models.Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)