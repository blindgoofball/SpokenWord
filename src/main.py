import wx
from app import SpokenWord

if __name__ == '__main__':
    app=wx.App()
    window=SpokenWord()
    app.MainLoop()