import imports.speacker_interfice as tts
import shelve 
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext
from tkinter import messagebox

bg_color = 'gray22'
main_color = 'deepskyblue2'
main_font = ('helvetica', '11')

class WindowProperties:
   
    def __init__(self, window):
    #var
        config = self._login()
        self.engine = tts.Speaker(self.speech_return)
        self.list_voices = self.engine.all_voice()
        self.reading_companion = {'text':'', 'readed': ''}
        self.pause_control = False

    #windows_top
        self.Frame_top = Frame(window, bg=bg_color, width=590, height=60, highlightbackground=main_color, highlightthickness=3)
        self.frame_top_voices = Frame(self.Frame_top, bg=bg_color)
        self.frame_top_volRate = Frame(self.Frame_top, bg=bg_color)
        self.frame_vol = Frame(self.frame_top_volRate, bg = bg_color)
        self.frame_rate = Frame(self.frame_top_volRate, bg = bg_color)
    
    #windos top Widget
        self.label_voice = Label(self.frame_top_voices, text='Selecione as vozes', font=main_font, bg=bg_color, fg = main_color)
        self.VoicesCombox = Combobox(self.frame_top_voices, font = main_font, background=bg_color, foreground=main_color, width = 45)
        self.VoicesCombox['values'] = [i for i in self.list_voices.keys()]
        self.VoicesCombox.current(config['voice'])
        
        self.label_volume_text = Label(self.frame_vol, text='Volume', font = main_font, bg= bg_color, fg = main_color)
        self.label_rate_text = Label(self.frame_rate, text= 'Velocidade', font = main_font, bg = bg_color, fg = main_color)
        
        self.label_indice1 = Label(self.frame_vol, font = main_font, bg = 'white', fg = main_color, text = config['vol'], width =6)
        self.label_indice2 = Label(self.frame_rate, font = main_font, bg = 'white', fg = main_color, text = config['rate'], width = 6)

        self.vol_button_plus = Button(self.frame_vol, text = '+', font= main_font, bg = bg_color, fg = main_color, width= 6, command = self.volume_plus )
        self.vol_button_minus = Button(self.frame_vol, text = '-', font= main_font, bg = bg_color, fg= main_color, width= 6, command = self.volume_minus)
        self.rate_button_plus = Button(self.frame_rate, text = '+', font= main_font, bg= bg_color, fg=main_color, width= 6, command = self.rate_plus)
        self.rate_button_minus = Button(self.frame_rate, text = '-', font= main_font, bg= bg_color, fg= main_color, width= 6, command = self.rate_minus)

    #pack top widget
        self.Frame_top.pack(pady= 5)
        self.frame_top_voices.pack(side = LEFT, padx = 4)
        self.frame_top_volRate.pack(side = RIGHT, padx = 10)
        self.frame_vol.pack(side= LEFT, pady = 4, padx = 2)
        self.frame_rate.pack(side= RIGHT, pady = 4, padx = 2)

        self.label_voice.pack()
        self.VoicesCombox.pack()

        self.label_volume_text.pack()
        self.vol_button_plus.pack()
        self.label_indice1.pack()
        self.vol_button_minus.pack()

        self.label_rate_text.pack()
        self.rate_button_plus.pack()
        self.label_indice2.pack()
        self.rate_button_minus.pack()
    
    #windows down
        self.frame_down = Frame(window, bg=bg_color, width=590, height=71, highlightbackground=main_color, highlightthickness=3
        )
        self.frame_down_text = Frame(self.frame_down, bg = bg_color)
        self.frame_down_button = Frame(self.frame_down, bg = bg_color)
        
        self.textbox = scrolledtext.ScrolledText(self.frame_down_text, width=60, height=14, font ='helvetica', bg=bg_color, fg = main_color)
        
        self.buton_Read = Button(self.frame_down_button, text = 'Ler', font= main_font, bg= bg_color, fg= main_color, width= 10, command = self.ReadText)
        self.button_paste = Button(self.frame_down_button, text = 'Colar', font= main_font, bg= bg_color, fg= main_color, width= 10, command = self.past_clipboard)
        self.button_pausePlay = Button(self.frame_down_button, text = 'Pause', font= main_font, bg= bg_color, fg= main_color, width= 10, command = self.cont_pause)
    #pack down

        self.frame_down.pack()
        self.frame_down_text.pack()
        self.frame_down_button.pack(pady=5)
        self.textbox.pack()
        self.buton_Read.pack(side= LEFT)
        self.button_paste.pack(side=LEFT, padx = 123)
        self.button_pausePlay.pack()
    

    def cont_pause(self):
        
        if self.pause_control:
            self.button_pausePlay['text'] = 'Pause'
            self.pause_control = False
            self.engine.speak(self.reading_companion['text'])
        
        else:
            self.engine.stop()
            self.button_pausePlay['text'] = 'Continue'
            self.pause_control = True
        
    
    def ReadText(self):
       self._save()
       #define voice
       self.engine.set_voice(self.list_voices[self.VoicesCombox.get()])
       #read
       self.reading_companion['text'] = self.textbox.get(1.0,END)
       self.engine.speak(self.reading_companion['text'])
       self.reading_companion['readed'] = ''     
    #vol define
    def volume_plus(self):
        self.volume_value('+')
    def volume_minus(self):
        self.volume_value('-')

    def volume_value(self, control='-'):
        volume_indice = int(self.label_indice1['text'])
        if control == '-' and volume_indice != 0 :
            self.label_indice1['text'] = str(volume_indice - 1)
            self.engine.set_volume(int(self.label_indice1['text']))
        
        elif control == '+' and volume_indice != 100:
            self.label_indice1['text'] = str(volume_indice + 1)
            self.engine.set_volume(int(self.label_indice1['text']))

    # rate define 
    def rate_plus(self):
        self.rate_value('+')
    def rate_minus(self):
        self.rate_value('-')

    def rate_value(self, control = '-'):
        volume_indice = int(self.label_indice2['text'])
        if control == '-' and volume_indice != 0 :
            self.label_indice2['text'] = str(volume_indice - 25)
            self.engine.set_rate(int(self.label_indice2['text']))
        
        elif control == '+' and volume_indice != 300:
            self.label_indice2['text'] = str(volume_indice + 25)
            self.engine.set_rate(int(self.label_indice2['text']))

    def retur_number_by_value(self, voice):
        numero = 0
        for i in self.list_voices.keys():
            if i == self.VoicesCombox.get():
                return numero
            numero += 1

    def past_clipboard(self):
        #print(root.clipboard_get())
         self.textbox.delete(1.0, END)
         self.textbox.insert(END, root.clipboard_get())

    def _save(self):
        with shelve.open('config') as db:
            db['voice'] = self.retur_number_by_value(self.VoicesCombox.get())
            db['vol'] = self.label_indice1['text']
            db['rate'] = self.label_indice2['text']

    def _login(self):
        dic = {}
        try:
            with shelve.open('config') as db:
                dic['voice'] = db['voice']
                dic['vol'] = db['vol']
                dic['rate'] = db['rate']
        except:
            dic['voice'] = 0
            dic['vol'] = '100'
            dic['rate'] = '150'
        return dic

    def speech_return(self, name, location, length):
        wordsText = self.reading_companion['text']
        wordsRead = self.reading_companion['readed']
        
        wordsText = wordsText.split()
        wordsRead = wordsRead.split()

        wordsRead.append(wordsText[0])
        del(wordsText[0])

        wordsText= ' '.join(wordsText)
        wordsRead= ' '.join(wordsRead)

        self.textbox.delete(1.0, END)
        self.textbox.insert(END, wordsRead+' ', 'lido')  # <-- tagging `name`
        self.textbox.insert(END, wordsText, 'lera')  # <-- tagging `time`
        self.textbox.tag_config('lido', foreground = 'black', background = 'white')  # <-- Change colors of texts tagged `name`
        self.textbox.tag_config('lera', foreground = main_color) 

        self.reading_companion['text'] = wordsText
        self.reading_companion['readed'] = wordsRead

root = Tk()
root.geometry('600x440+400+150')
root.title('Reader')
root.resizable(width=False, height=False)
root['bg'] = bg_color
WindowProperties(root)

root.mainloop()