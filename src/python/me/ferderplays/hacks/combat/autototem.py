class autototem:
    if module.enabled(module = autototem):
        def update():
            mc.placeItemInOffhand(item = totem_of_undying, tick = 0.07)
        if mc.playerDamages(player = mc.player):
            def update():
                mc.placeItemInOffhand(item = totem_of_undying, tick = 0.07)