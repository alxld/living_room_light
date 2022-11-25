"""Platform for light integration"""
from __future__ import annotations
import sys
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import DOMAIN

sys.path.append("custom_components/new_light")
from new_light import NewLight


light_entity_all = "light.living_room_group_new"
light_entity_lamps = "light.living_room_lamps_group"
light_entity_ceiling = "light.living_room_ceiling_group"
harmony_entity = "media_player.sony_bravia_tv"
switch_action = "zigbee2mqtt/Living Room Switch/action"
motion_sensor_action = "zigbee2mqtt/Living Room Motion Sensor"
brightness_step = 43
motion_sensor_brightness = 191
has_harmony = True
has_motion_sensor = True
has_switch = True


async def async_setup_platform(
    hass: HomeAssistant,
    config: ConfigType,
    add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the light platform."""
    # We only want this platform to be set up via discovery.
    if discovery_info is None:
        return
    ent = LivingRoomLight()
    add_entities([ent])


class LivingRoomLight(NewLight):
    """Living Room Light."""

    def __init__(self) -> None:
        """Initialize Living Room Light."""
        super(LivingRoomLight, self).__init__(
            "Living Room", domain=DOMAIN, debug=False, debug_rl=False
        )
        self.entities["light.living_room_lamps_group"] = None
        self.entities["light.living_room_ceiling_group"] = None
        self.entities["light.living_room_group_new"] = None
        self.switch = "Living Room Switch"
        self.motion_sensors.append("Living Room Motion Sensor")
        self.harmony_entity = "media_player.sony_bravia_tv"
