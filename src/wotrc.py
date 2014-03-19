#!/usr/bin/python
# -*- coding: utf-8 -*-
import BigWorld
import items.vehicles
import random
import time
from gui import g_tankActiveCamouflage
from gui.ClientHangarSpace import ClientHangarSpace
from VehicleAppearance import VehicleAppearance
from debug_utils import *

old_va_getCamouflageParams = VehicleAppearance._VehicleAppearance__getCamouflageParams

def new_va_getCamouflageParams(self, vehicle):
    result = old_va_getCamouflageParams(self, vehicle)
    if result[0] is not None:
        return result
    arenaType = BigWorld.player().arena.arenaType
    camouflageKind = arenaType.vehicleCamouflageKind
    vDesc = vehicle.typeDescriptor
    customization = items.vehicles.g_cache.customization(vDesc.type.customizationNationID)
    camouflages = []
    for key in customization['camouflages']:
        if customization['camouflages'][key]['kind'] == camouflageKind:
            camouflages.append(key)
    camouflages.append(None)
    camouflageId = vehicle.id % len(camouflages)
    return (camouflages[camouflageId], int(time.time()), 7)

VehicleAppearance._VehicleAppearance__getCamouflageParams = new_va_getCamouflageParams

old_cs_recreateVehicle = ClientHangarSpace.recreateVehicle

def new_cs_recreateVehicle(self, vDesc, vState, onVehicleLoadedCallback = None):
    customization = items.vehicles.g_cache.customization(vDesc.type.customizationNationID)
    camouflages = customization['camouflages'].keys()
    camouflages.append(None)
    vDesc.camouflages = ((random.choice(camouflages), int(time.time()), 7), \
        (random.choice(camouflages), int(time.time()), 7), \
        (random.choice(camouflages), int(time.time()), 7))
    old_cs_recreateVehicle(self, vDesc, vState, onVehicleLoadedCallback)

ClientHangarSpace.recreateVehicle = new_cs_recreateVehicle
