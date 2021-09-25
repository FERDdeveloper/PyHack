class crystalaura:
    if module.enabled(module = crystalaura):
        def update():
           mc.placeBlock(block = end_crystall, range = 30, tick = 0.07)
        if mc.placedBlock(block = end_crystall):
           def update():
               mc.breakBlock(block = end_crystall, range = 30, tick = 0.7)