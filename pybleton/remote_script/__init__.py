# Pybleton Ableton Live Remote Script (Python 3 environment)
# This directory contains the script that gets copied into Ableton's MIDI Remote Scripts folder.

from _Framework.ControlSurface import ControlSurface

class Pybleton(ControlSurface):
    def __init__(self, c_instance):
        super().__init__(c_instance)
        # Initialization logic for OSC/Sockets would go here
