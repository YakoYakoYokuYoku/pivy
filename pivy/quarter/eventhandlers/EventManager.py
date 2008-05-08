

class EventManager:
    """ The EventManager class is responsible for holding a list of
      devices which can translate events such as a MouseHandler and
      KeyboardHandler for translation of mouse and keyboard events,
      respectively.

      Custom device handlers can be registered with this class for more
      functionality
    """
    def __init__(self, quarterwidget):
        assert(quarterwidget)
        self.quarterwidget = quarterwidget
        self.eventhandlers = []

    def handleEvent(self, qevent):
        """Runs trough the list of registered devices to translate events"""
        for handler in self.eventhandlers:
            if handler.handleEvent(qevent):
                return True
        return False

    def getWidget(self):
        """Returns the QuarterWidget this devicemanager belongs to"""
        return self.quarterwidget

    def registerEventHandler(self, handler):
        """Register a device for event translation"""
        if (not handler in self.eventhandlers):
            handler.setManager(self)
            self.eventhandlers.append(handler)

    def unregisterEventHandler(self, handler):
        """unregister a device"""
        if handler in self.eventhandlers:
            self.eventhandlers.removeAt(self.eventhandlers.indexOf(handler))
