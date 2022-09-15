#!/usr/bin/python
# ================================
# (C)2019-2021 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# EMAG
# switch to OCIO - ACES
# works with Kelvin color picker
# ================================

import lx
import modo
try:
    # change preferences settings
    lx.eval('pref.value colormanagement.default_ocio_config aces_1.2')
    lx.eval('pref.value colormanagement.8bit_default_colorspace "aces_1.2:Input - Generic - sRGB - Texture"')
    lx.eval('pref.value colormanagement.16bit_default_colorspace "aces_1.2:Input - Generic - sRGB - Texture"')
    lx.eval('pref.value colormanagement.float_default_colorspace "aces_1.2:Utility - Linear - sRGB"')
    lx.eval('pref.value colormanagement.numeric_default_colorspace "aces_1.2:Input - Generic - sRGB - Texture"')
    lx.eval('pref.value colormanagement.view_default_colorspace "aces_1.2:Input - Generic - sRGB - Texture"')

    # change scene settings
    scene = modo.scene.current()
    scene.sceneItem.select(replace=True)
    lx.eval('item.channel scene$ocioConfig aces_1.2')
    lx.eval('item.channel scene$def8bitColorspace "aces_1.2:Input - Generic - sRGB - Texture"')
    lx.eval('item.channel scene$def16bitColorspace "aces_1.2:Input - Generic - sRGB - Texture"')
    lx.eval('item.channel scene$defFloatColorspace "aces_1.2:Utility - Linear - sRGB"')

except Exception:
    modo.dialogs.alert('ACES 1.2', 'Error switching to ACES 1.2. Change your profiles manually', 'error')
