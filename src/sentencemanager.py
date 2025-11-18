from random import choices
import difflib

class SentenceManager:
    def __init__(self):
        self.sentences=self.pickSentences()
        self.currentSentence=0
        self.totalWords=0
        self.mistakes=0
    def loadSentences(self):
        try:
            with open('sentences.txt', 'r') as f:
                sentences=f.readlines()
        except FileNotFoundError:
            return []
        sentences=[s.strip() for s in sentences if s]
        return sentences
    def pickSentences(self, amount=30):
        sentences=self.loadSentences()
        return choices(sentences, k=30)
    def finishSentence(self, value):
        words=len(value.split())
        self.totalWords+=words
        self.checkMistakes(self.sentences[self.currentSentence], value)
        self.currentSentence+=1
        if self.currentSentence >= len(self.sentences):
            return None
        return self.sentences[self.currentSentence]
    def checkMistakes(self, original, typed):
        expected=original.split()
        provided=typed.split()
        matcher=difflib.SequenceMatcher(None, expected, provided)
        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag in ['replace', 'delete', 'insert']:
                self.mistakes+=1
    def sentenceFinished(self, value):
        typedWords=value.split()
        expectedWords=self.sentences[self.currentSentence].split()
        return len(typedWords) >= len(expectedWords) and value.endswith(' ')