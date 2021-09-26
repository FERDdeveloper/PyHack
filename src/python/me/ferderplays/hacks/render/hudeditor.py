class hudeditor:
    if hud.dragged(arrays):
        def update(self):
            arrays.position += drag(position)
    if hud.dragged(keystrokes):
        def update(self):
            keystrokes.position += drag(position)
    if hud.dragged(watermark):
        def update(self):
            watermark.position += drag(position)
    if hud.dragged(inventoryInterface):
        def update(self):
            inventoryInterface.position += drag(position)
    if hud.dragged(time):
        def update(self):
            time.position += drag(position)