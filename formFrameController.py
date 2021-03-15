import wx
from tugas1_PBO2_C import formFrame

class formFrameController(formFrame):
    def __init(self, parent):
        formFrame.__init__(self, parent)

app = wx.App()
frame = formFrame(parent=None)
frame.Show()
app.MainLoop()