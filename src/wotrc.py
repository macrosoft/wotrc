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
    return (random.choice(camouflages), int(time.time()), 7)

VehicleAppearance._VehicleAppearance__getCamouflageParams = new_va_prerequisites
