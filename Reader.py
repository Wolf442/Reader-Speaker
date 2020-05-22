import imports.speacker_interfice as tts
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import scrolledtext

bg_color = 'gray22'
main_color = 'deepskyblue2'
main_font = ('helvetica', '11')

class WindowProperties:
   
    def __init__(self, window):
    #windows_top
        self.Frame_top = Frame(window, bg=bg_color, width=590, height=60,highlightbackground=main_color, highlightthickness=1)
        self.frame_top_voices = Frame(self.Frame_top, bg=bg_color)
        self.frame_top_volRate = Frame(self.Frame_top, bg=bg_color)
        self.frame_vol = Frame(self.frame_top_volRate, bg = bg_color)
        self.frame_rate = Frame(self.frame_top_volRate, bg = bg_color)
    #windos top Widget
        self.label_voice = Label(self.frame_top_voices, text='Selecione as vozes', font=main_font, bg=bg_color, fg = main_color)
        self.VoicesCombox = Combobox(self.frame_top_voices, font = main_font, background=bg_color, foreground=main_color, width = 45)
        self.VoicesCombox['values'] = (1,3,4,5)
        
        self.label_volume_text = Label(self.frame_vol, text='Volume', font = main_font, bg= bg_color, fg = main_color)
        self.label_rate_text = Label(self.frame_rate, text= 'Velocidade', font = main_font, bg = bg_color, fg = main_color)
        
        self.label_indice1 = Label(self.frame_vol, font = main_font, bg = 'white', fg = main_color, text = 0, width =6)
        self.label_indice2 = Label(self.frame_rate, font = main_font, bg = 'white', fg = main_color, text = 0, width = 6)

        self.vol_button_plus = Button(self.frame_vol, text = '+', font= main_font, bg = bg_color, fg = main_color, width= 6)
        self.vol_button_minus = Button(self.frame_vol, text = '-', font= main_font, bg = bg_color, fg= main_color, width= 6)
        self.rate_button_plus = Button(self.frame_rate, text = '+', font= main_font, bg= bg_color, fg=main_color, width= 6)
        self.rate_button_minus = Button(self.frame_rate, text = '-', font= main_font, bg= bg_color, fg= main_color, width= 6)

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
        self.frame_down = Frame(window, bg=bg_color, width=590, height=71, highlightbackground=main_color, highlightthickness=1)
        self.frame_down_text = Frame(self.frame_down, bg = bg_color)
        self.frame_down_button = Frame(self.frame_down, bg = bg_color)
        
        self.textbox = scrolledtext.ScrolledText(self.frame_down_text, width=60, height=14, font ='helvetica', bg=bg_color, fg = main_color)
        
        self.buton_Read = Button(self.frame_down_button, text = 'Ler', font= main_font, bg= bg_color, fg= main_color, width= 10)
        self.button_paste = Button(self.frame_down_button, text = 'Colar', font= main_font, bg= bg_color, fg= main_color, width= 10)
        self.button_pausePlay = Button(self.frame_down_button, text = 'Pause', font= main_font, bg= bg_color, fg= main_color, width= 10)
    #pack down

        self.frame_down.pack()
        self.frame_down_text.pack()
        self.frame_down_button.pack(pady=5)
        self.textbox.pack()
        self.buton_Read.pack(side= LEFT)
        self.button_paste.pack(side=LEFT, padx = 123)
        self.button_pausePlay.pack()

root = Tk()
root.geometry('600x440+400+150')
root.title('Reader')
root.resizable(width=False, height=False)
root['bg'] = bg_color
WindowProperties(root)

root.mainloop()