#!/usr/bin/python
# ================================
# (C)2019-2021 Dmytro Holub
# heap3d@gmail.com
# --------------------------------
# modo python
# EMAG
# switch to OCIO - ACES
# ================================

import lx
import modo

try:
    # change preferences settings
    lx.eval("pref.value colormanagement.default_ocio_config nuke-default")
    lx.eval('pref.value colormanagement.8bit_default_colorspace "nuke-default:sRGB"')
    lx.eval('pref.value colormanagement.16bit_default_colorspace "nuke-default:sRGB"')
    lx.eval('pref.value colormanagement.float_default_colorspace "nuke-default:linear"')
    lx.eval('pref.value colormanagement.numeric_default_colorspace "nuke-default:sRGB"')
    lx.eval('pref.value colormanagement.view_default_colorspace "nuke-default:sRGB"')

    lx.eval("pref.value colormanagement.colorMappingApplyToColorSwatches true")

    # change scene settings
    scene = modo.scene.current()
    scene.sceneItem.select(replace=True)
    lx.eval("item.channel scene$ocioConfig nuke-default")
    lx.eval('item.channel scene$def8bitColorspace "nuke-default:sRGB"')
    lx.eval('item.channel scene$def16bitColorspace "nuke-default:sRGB"')
    lx.eval('item.channel scene$defFloatColorspace "nuke-default:linear"')

except Exception:
    modo.dialogs.alert(
        "Nuke-default",
        "Error while switching to Nuke-default. Change your profiles manually",
        "error",
    )
