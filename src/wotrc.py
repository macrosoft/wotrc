#!/usr/bin/python
# -*- coding: utf-8 -*-
import BigWorld
import items.vehicles
import random
import time
from VehicleAppearance import VehicleAppearance
from debug_utils import *

old_va_prerequisites = VehicleAppearance._VehicleAppearance__getCamouflageParams

def new_va_prerequisites(self, vehicle):
    vDesc = vehicle.typeDescriptor
    customization = items.vehicles.g_cache.customization(vDesc.type.customizationNationID)
    camouflages = customization['camouflages'].keys()
    camouflages.append(None)
    camouflageId = (BigWorld.player().arena.arenaUniqueID + vehicle.id) % len(camouflages)\
        if hasattr(BigWorld.player(), 'arena') \
        else random.randint(0, len(camouflages) - 1)
    return (camouflages[camouflageId], int(time.time()), 7)

VehicleAppearance._VehicleAppearance__getCamouflageParams = new_va_prerequisites

