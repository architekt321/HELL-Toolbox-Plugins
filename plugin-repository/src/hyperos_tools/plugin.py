"""HyperOS Tools integration plugin."""

from miro.plugins import Plugin


class HyperOsToolsPlugin(Plugin):
    """Loadable extension point for HyperOS Tools."""

    plugin_id = "hyperos_tools"
    name = "HyperOS Tools"

    def workflow_steps(self):
        # The repository package is deliberately non-destructive. Concrete
        # device/firmware operations can be added as reviewed workflow steps.
        return ()
