import wx

class SpokenWord(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Spoken Word')
        self.panel=wx.Panel(self)
        self.sizer=wx.BoxSizer(wx.VERTICAL)
        self.textField=wx.TextCtrl(self.panel)
        self.sizer.Add(self.textField, 1, wx.ALL|wx.EXPAND)
        self.panel.SetSizer(self.sizer)
        self.Show()