"""MIRO Firmware Cleaner integration plugin."""

from miro.plugins import Plugin


class FirmwareCleanerPlugin(Plugin):
    """Loadable extension point for MIRO Firmware Cleaner."""

    plugin_id = "firmware_cleaner"
    name = "MIRO Firmware Cleaner"

    def workflow_steps(self):
        # The repository package is deliberately non-destructive. Concrete
        # device/firmware operations can be added as reviewed workflow steps.
        return ()
