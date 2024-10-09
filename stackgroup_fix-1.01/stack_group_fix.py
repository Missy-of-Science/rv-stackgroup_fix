from rv import rvtypes, commands


class StackGroupFix(rvtypes.MinorMode):
    "Work around for the Stack Group Differences in Layers."

    def exec(self, event):
        event.reject()
        viewNode = commands.viewNode()
        if commands.nodeType(viewNode) != "RVStackGroup":
            return

        sourceGroups = commands.nodeConnections(viewNode)[0]
        for node in sourceGroups:
            prop = f"{viewNode}_t_{node}.stencil.visibleBox"
            if commands.getFloatProperty(prop) == [0.0, 1.0, 0.0, 1.0]:
                commands.setFloatProperty(prop, [0.0, 1.0, 0.0001, 1.0])

    def __init__(self):
        rvtypes.MinorMode.__init__(self)
        self.init(
            "StackGroupFix", [("render", self.exec, "Keep Visible Box away from Edges."),], None
        )


def createMode():
    return StackGroupFix()
