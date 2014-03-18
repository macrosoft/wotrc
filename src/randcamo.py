#!/usr/bin/python
# -*- coding: utf-8 -*-
import BigWorld
import items.vehicles
from VehicleAppearance import VehicleAppearance
from debug_utils import *

old_va_prerequisites = VehicleAppearance._VehicleAppearance__getCamouflageParams
def new_va_prerequisites(self, vehicle):
    vDesc = vehicle.typeDescriptor
    result = old_va_prerequisites(self, vehicle)
    LOG_NOTE(vDesc.camouflages[0])
    return (3, 1394280840, 7)

VehicleAppearance._VehicleAppearance__getCamouflageParams = new_va_prerequisites

