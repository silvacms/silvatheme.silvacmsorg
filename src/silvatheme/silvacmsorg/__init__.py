# package

from silva.core.contentlayout.blocks.slot import BlockSlot


import sys
import copy_reg
import DateTime

# Due to a name override in __init__ you can't import this module
DateTime = sys.modules['DateTime.DateTime']

orig_patch_reconstructor = DateTime._dt_reconstructor

def patch_of_patch_reconstructor(cls, base, state):
    if cls is BlockSlot:
        obj = BlockSlot.__new__(cls, state)
        if base.__init__ != object.__init__:
            base.__init__(obj, state)
        return obj
    return orig_patch_reconstructor(cls, base, state)

DateTime._dt_reconstructor = patch_of_patch_reconstructor
copy_reg._reconstructor = patch_of_patch_reconstructor
