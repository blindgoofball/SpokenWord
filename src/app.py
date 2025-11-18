import time
import wx
from sentencemanager import SentenceManager
import speech

class SpokenWord(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Spoken Word')
        self.sentenceManager=SentenceManager()
        self.startTime=None
        self.panel=wx.Panel(self)
        self.sizer=wx.BoxSizer(wx.VERTICAL)
        self.sentenceDisplay=wx.StaticText(self.panel, label=self.sentenceManager.getCurrentSentence())
        self.sizer.Add(self.sentenceDisplay, 0, wx.ALL|wx.EXPAND, 5)
        self.textField=wx.TextCtrl(self.panel)
        self.sizer.Add(self.textField, 1, wx.ALL|wx.EXPAND, 5)
        self.panel.SetSizer(self.sizer)
        self.textField.Bind(wx.EVT_TEXT, self.onText)
        self.textField.Bind(wx.EVT_CHAR_HOOK, self.onKey)
        self.Show()
    def onText(self, evt):
        typed=self.textField.GetValue()
        if self.sentenceManager.sentenceFinished(typed):
            self.textField.Clear()
            nextSentence=self.sentenceManager.finishSentence(typed)
            if nextSentence:
                self.sentenceDisplay.SetLabel(self.sentenceManager.getCurrentSentence())
                speech.speak(nextSentence)
            else:
                self.finish()
    def onKey(self, evt):
        if evt.GetKeyCode() == wx.WXK_TAB:
            speech.speak(self.sentenceManager.getCurrentSentence())
        else:
            evt.Skip()
    def finish(self):
        endTime=time.time()
        totalTime=int(endTime-self.startTime)
        wpm=int(self.sentenceManager.totalWords/(totalTime/60))
        accuracy=100-(self.sentenceManager.mistakes/self.sentenceManager.totalWords*100)
        stats=f"Complete!\nYour average speed was {wpm} words per minute.\nYou had an accuracy of {accuracy:.1f}%."
        dlg=wx.MessageDialog(self, stats, 'Complete!')
        dlg.ShowModal()
        self.Close()
    def startTimer(self):
        self.startTime=time.time()
        speech.speak(self.sentenceManager.getCurrentSentence())