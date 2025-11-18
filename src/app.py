import wx
from sentencemanager import SentenceManager
import speech

class SpokenWord(wx.Frame):
    def __init__(self):
        super().__init__(None, title='Spoken Word')
        self.sentenceManager=SentenceManager()
        self.panel=wx.Panel(self)
        self.sizer=wx.BoxSizer(wx.VERTICAL)
        self.textField=wx.TextCtrl(self.panel)
        self.sizer.Add(self.textField, 1, wx.ALL|wx.EXPAND)
        self.panel.SetSizer(self.sizer)
        self.textField.Bind(wx.EVT_TEXT, self.onText)
        self.textField.Bind(wx.EVT_CHAR_HOOK, self.onKey)
        self.Show()
        speech.speak(self.sentenceManager.sentences[self.sentenceManager.currentSentence])
    def onText(self, evt):
        typed=self.textField.GetValue()
        if self.sentenceManager.sentenceFinished(typed):
            self.textField.Clear()
            nextSentence=self.sentenceManager.finishSentence(typed)
            if nextSentence:
                speech.speak(nextSentence)
            else:
                self.finish()
    def onKey(self, evt):
        if evt.GetKeyCode() == wx.WXK_TAB:
            speech.speak(self.sentenceManager.sentences[self.sentenceManager.currentSentence])
        else:
            evt.Skip()
    def finish(self):
        accuracy=100-(self.sentenceManager.mistakes/self.sentenceManager.totalWords*100)
        stats=f"Complete! You had an accuracy of {accuracy:.1f}%."
        dlg=wx.MessageDialog(self, stats, 'Complete!')
        dlg.ShowModal()
        self.Close()