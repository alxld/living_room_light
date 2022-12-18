"""Platform for light integration"""
from __future__ import annotations
import sys
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType

from . import DOMAIN

sys.path.append("custom_components/new_light")
from new_light import NewLight


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
        self.motion_disable_entities.append("remote.sony_xbr_65a1e")

        self.has_brightness_threshold = True
        self.brightness_threshold = 191
        self.motion_sensor_brightness = 150
