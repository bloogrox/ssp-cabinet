from dynamic_preferences.types import IntegerPreference
from dynamic_preferences.registries import global_preferences_registry


@global_preferences_registry.register
class PushPerToken(IntegerPreference):
    name = 'push_per_token'
    default = 3
    verbose_name = "Limit pushes per token"


@global_preferences_registry.register
class BidRequestVolume(IntegerPreference):
    name = 'bid_request_volume'
    default = 3
    verbose_name = "Bid requests volume"


@global_preferences_registry.register
class StartHour(IntegerPreference):
    name = 'start_hour'
    default = 10
    verbose_name = "Start Hour"


@global_preferences_registry.register
class EndHour(IntegerPreference):
    name = 'end_hour'
    default = 20
    verbose_name = "End Hour"
