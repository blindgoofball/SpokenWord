import wx
from app import SpokenWord
import speech

if __name__ == '__main__':
    app=wx.App()
    window=SpokenWord()
    wx.MessageDialog(window, 'Welcome to Spoken Word.\nYou will need to type a series of sentences as fast and as accurately as possible.\nYou can always press tab to get the current sentence spoken aloud.\nPress enter to begin.', 'Welcome').ShowModal()
    window.startTimer()
    app.MainLoop()