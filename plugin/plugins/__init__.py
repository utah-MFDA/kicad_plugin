import pcbnew
import os
import wx

class SimplePlugin(pcbnew.ActionPlugin):
    def defaults(self):
        self.name = "MFDA"
        self.category = "A descriptive category name"
        self.description = "A description of the plugin and what it does"
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), 'icon.png')

    def Run(self):
        frm = wx.Frame(None, title="Hello World")
        frm.Show()

SimplePlugin().register() # Instantiate and register to Pcbnew
