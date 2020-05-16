import pyttsx3 as tts 

class Speaker(object):
    def __init__(self, return_function):
        self.engine = tts.init()
        if return_function != None:
            self.engine.connect('started-word', return_function)

#speacker
    def speak(self, text_to_read):
        self.engine.say(' ')
        self.engine.say(text_to_read)
        self.engine.startLoop(False)
        self.engine.iterate()
        self.engine.endLoop()

#define voice properties
    def set_voice(self, voice_id):
        self.engine.setProperty('voice',voice_id)
    
    def set_volume(self, volume = 50):
        self.engine.setProperty('volume',volume/100)
    
    def set_rate(self, rate):
        self.engine.setProperty('rate',rate)

#returns state or properties of voices
    def all_voice(self):
        voices_dic = {}
        voices = self.engine.getProperty('voices')
        for i in voices:
            voices_dic[i.name] = i.id 
        return voices_dic
    
    def volume(self):
        return  int(self.engine.getProperty('volume') * 100)

    def rate(self):
        return self.engine.getProperty('rate')