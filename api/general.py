from rest_framework.decorators import api_view
from rest_framework.response import Response
from dynamic_preferences.registries import global_preferences_registry


@api_view(['GET'])
def general(request):
    global_preferences = global_preferences_registry.manager()
    settings = {
        "bids_volume": global_preferences["bid_request_volume"],
        "push_limit_per_token": global_preferences["push_per_token"],
        "start_hour": global_preferences["start_hour"],
        "end_hour": global_preferences["end_hour"]
    }
    return Response(settings)
