#!/usr/bin/python
# -*- coding: utf-8 -*-
import BigWorld
import items.vehicles
import time
from VehicleAppearance import VehicleAppearance
from debug_utils import *

old_va_getCamouflageParams = VehicleAppearance._VehicleAppearance__getCamouflageParams

def new_va_getCamouflageParams(self, vehicle):
    result = old_va_getCamouflageParams(self, vehicle)
    if result[0] is not None:
        return result
    vDesc = vehicle.typeDescriptor
    customization = items.vehicles.g_cache.customization(vDesc.type.customizationNationID)
    camouflages = customization['camouflages'].keys()
    camouflages.append(None)
    camouflageId = vehicle.id % len(camouflages)
    return (camouflages[camouflageId], int(time.time()), 7)

VehicleAppearance._VehicleAppearance__getCamouflageParams = new_va_getCamouflageParams

