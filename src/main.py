import wx
from app import SpokenWord
import speech

if __name__ == '__main__':
    app=wx.App()
    window=SpokenWord()
    app.MainLoop()