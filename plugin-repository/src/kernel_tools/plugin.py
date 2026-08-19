"""Kernel Tools integration plugin."""

from miro.plugins import Plugin


class KernelToolsPlugin(Plugin):
    """Loadable extension point for Kernel Tools."""

    plugin_id = "kernel_tools"
    name = "Kernel Tools"

    def workflow_steps(self):
        # The repository package is deliberately non-destructive. Concrete
        # device/firmware operations can be added as reviewed workflow steps.
        return ()
