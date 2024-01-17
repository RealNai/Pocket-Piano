import pygame
import pygame.freetype
import pickle
import piano_lists as pl
import others as o
from pygame import mixer
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import tkinter.messagebox
import os.path
import requests
import urllib.request 
from requests_html import HTMLSession
import re

try:
    import pygame_gui
except:
    print("\n------------------------------------------------------\n     Please install module \"pygame_gui\' \n------------------------------------------------------")

pygame.init()

pygame.mixer.set_num_channels(50)

class Song:
    def __init__(self, name, author, key, chords):
        self.name = name
        self.author = author
        self.key = key
        self.chords = chords

    def setName(self, name):
        self.name = name

    def setAuthor(self, author):
        self.author = author

    def setKey(self, key):
        self.key = key

    def setChords(self, chords):
        self.chords = chords
        
    def getName(self):
        return self.name

    def getAuthor(self):
        return self.author

    def getKey(self):
        return self.key

    def getChords(self):
        return self.chords

    def getInfo(self):
        return f"{self.name: <25}{self.author: <25}{self.key: <15}{self.chords: <80}"

class SearchHistory():
    def __init__(self, results=[]) -> None:
        self.results = results

    def add_result(self, result):
        self.results.append(result)

    def clear_history(self):
        self.results = []

    def get_history(self):
        return self.results

class WebSearchHistory(SearchHistory):
    def __init__(self, search_engine, url=[], results=[]):
        super().__init__(results)
        self.search_engine = search_engine
        self.url = url

    def add_url(self, url):
        return self.url.append(url)

    def get_history(self):
        result = super().get_history().copy()
        for i in range(len(result)):
            result[i] = result[i] + f"{self.search_engine: <20}{self.url[i]: <30}"
        return result

fontsize = 16
try:
    path = os.path.dirname(__file__).replace("\\","/")
    font = pygame.font.Font(f'{path}' + '/assets/Oswald-Regular.ttf', 48)
    medium_font = pygame.font.Font(f'{path}' + '/assets/Oswald-Regular.ttf', 28)
    small_font = pygame.font.Font(f'{path}' + '/assets/Oswald-Regular.ttf', 16)
    real_small_font = pygame.font.Font(f'{path}' + '/assets/Oswald-Regular.ttf', 10)
    font_2 = pygame.freetype.SysFont(f'{path}' + '/assets/Oswald-Regular.ttf', fontsize)
except:
    print("____________________________\nPlease change your directory to this project file\n____________________________")
fps = 60
timer = pygame.time.Clock()
#WIDTH = 52 * 35
WIDTH = 52 * 35
HEIGHT = 600

MANAGER = pygame_gui.UIManager((WIDTH, HEIGHT))
TEXT_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((5+80+30,5+50),(30+80,30)), manager=MANAGER, object_id="#main_text_entry")
screen = pygame.display.set_mode([WIDTH, HEIGHT])
white_sounds = []
black_sounds = []
active_whites = []
active_blacks = []
left_oct = 4
right_oct = 5
time_when_click = []
playback = []
play_on = False
record_color_light = '#ff4242'
record_color_dark = '#ab0000'
play_color_light = '#4cff42'
play_color_dark = '#08a100'
record_button_clicked = False
play_button_clicked = False
play_clicked = False
hover_record_button = False
hover_play_button = False
hover_history_bn = False
hover_setting_bn = False
setting_bn_clicked = False
history_bn_clicked = False
hover_text_input = False
text_entry = False
printed_text = False
searched_text = False
newfiles = []
song_name = ""
entered_text = ""
found_chords = []
rendered_fonts =[]
spacing_y = 4  # pixels between lines
inc = 1
chord_as_text = ""
song_list = []
song_key = ''
author_name = ""
url2 = ""
play_check = 0

left_hand = pl.left_hand
right_hand = pl.right_hand
piano_notes = pl.piano_notes
white_notes = pl.white_notes
black_notes = pl.black_notes
black_labels = pl.black_labels
keys = pl.keys
keybinds = pl.keybinds
keybinds_default = pl.keybinds_default
key_dict = pl.key_dict
key_all = pl.key_all
piano_lists_all = o.piano_lists_all
piano_lists_back = o.piano_lists_back
piano_lists_front = o.piano_lists_front


current_key = key_dict[keys[0]] # key C default
currnet_key_name = key_all[0]


search_history = WebSearchHistory(search_engine="Google")
song = Song(name="",author="",key="",chords="")


key_lable = small_font.render(f'Select key to play on:', True, 'black')

key_text_list =[]
for i in range(len(keys)):
    key_text = small_font.render(f'{keys[i]}', True, 'black')
    key_text_list.append(key_text)

try:
    for i in range(len(white_notes)):
        white_sounds.append(mixer.Sound(f'{path}' + f'\\assets\\notes\\{white_notes[i]}.wav'))

    for i in range(len(black_notes)):
        black_sounds.append(mixer.Sound(f'{path}' + f'\\assets\\notes\\{black_notes[i]}.wav'))
except:
    print("____________________________\nPlease change your directory to this project file\n____________________________")

pygame.display.set_caption("Pocket Piano")


def draw_piano(whites, blacks):
    white_rects = []
    for i in range(52):
        rect = pygame.draw.rect(screen, 'white' , [i * 35, HEIGHT - 300, 35, 300], 0, 2)
        white_rects.append(rect)
        pygame.draw.rect(screen, 'black', [i * 35, HEIGHT - 300, 35, 300], 2, 2)
    skip_count = 0
    last_skip = 2
    skip_track = 2
    black_rects = []
    for i in range(36):
        rect = pygame.draw.rect(screen, '#3d3d3d', [23 + (i * 35) + (skip_count * 35), HEIGHT - 300, 24, 200], 0, 2)
        for q in range(len(blacks)):
            if blacks[q][0] == i:
                if blacks[q][1] > 0:
                    pygame.draw.rect(screen, '#ffb300', [23 + (i * 35) + (skip_count * 35), HEIGHT - 300, 24, 200], 0, 2)
                    blacks[q][1] -= 1
        black_rects.append(rect)
        skip_track += 1
        if last_skip == 2 and skip_track == 3:
            last_skip = 3
            skip_track = 0
            skip_count += 1
        elif last_skip == 3 and skip_track == 2:
            last_skip = 2
            skip_track = 0
            skip_count += 1
    for i in range(len(whites)):
        HEIGHT_GREEN = 100 #default 100
        if whites[i][1] > 0:
            j = whites[i][0]
            pygame.draw.rect(screen, '#ebebeb', [j * 35 + 2, HEIGHT - HEIGHT_GREEN, 31, HEIGHT_GREEN-2], 0, 0)
            pygame.draw.rect(screen, '#f7f7f7', [j * 35 + 2, HEIGHT - HEIGHT_GREEN + 0, 31, HEIGHT_GREEN-90], 0, 0)
            pygame.draw.rect(screen, '#f0f0f0', [j * 35 + 2, HEIGHT - HEIGHT_GREEN + 10, 31, HEIGHT_GREEN-90], 0, 0)
            pygame.draw.rect(screen, '#ffb300', [j * 35 + 2, HEIGHT - HEIGHT_GREEN, 31, HEIGHT_GREEN-2], 0, 0)
            whites[i][1] -= 1

    return white_rects, black_rects, whites, blacks

def draw_title_bar():
    global chord_as_text
    global inc
    global song_key
    global author_name
    global url2
    global song
    global search_history
    if inc == 0:
        found_chords = []
        song_key = ""
        author_name = ""
        url_list = scrape_google(entered_text+ "chords")
        url2 = f"https://www.google.com/search?q={entered_text}+chords+\"key\"+ultimate+guitar".replace(" ","+")
        s2 = requests.get(url2).text
        try:
            url = get_link(url_list)
            s = requests.get(url).text
        except:
            s = ""
        for chord in pl.chord_names:
            if '[ch]'+chord+'[/ch]' in s:
                found_chords.append(chord)
        try:
            chord_as_text = str(found_chords)[1:-1].replace("\'","")
        except:
            None
        for i in key_all:
            if f"Key: {i}." in s2:
                song_key = i
        try:
            result = re.search('Chords - (.*) - Ultimate Guitar', s2)
            author_name = result.group(1)
            try:
                index = author_name.find('-')
                author_name = author_name[:index]
            except:
                None
        except:
            None
        if len(author_name) > 30:
            author_name = ""
        inc = 1
        song = Song(name= entered_text,author = author_name, key= song_key, chords=chord_as_text)
        song_list.append(song)
        search_history.add_url(url2)
        search_history.add_result(song.getInfo())
    try:
        instruction_text = small_font.render(f'Search:', True, 'black')
        instruction_text2 = small_font.render('(Search any song on the internet)', True, 'black')
        instruction_text3 = small_font.render(f'Song: {song_list[-1].getName()}', True, 'black')
        instruction_text4 = small_font.render(f'Author: {author_name}', True, 'black')
        instruction_text5 = small_font.render(f'Key: {song_key}', True, 'black')
        instruction_text6 = small_font.render(f'Chords: {song_list[-1].getChords()}', True, 'black')
    except:
        instruction_text = small_font.render(f'Search:', True, 'black')
        instruction_text2 = small_font.render('(Search any song on the internet)', True, 'black')
        instruction_text3 = small_font.render(f'Song:', True, 'black')
        instruction_text4 = small_font.render(f'Author: {author_name}', True, 'black')
        instruction_text5 = small_font.render(f'Key: {song_key}', True, 'black')
        instruction_text6 = small_font.render(f'Chords: ', True, 'black')
    screen.blit(instruction_text, (70, 60))
    screen.blit(instruction_text2, (70, 60+25))
    screen.blit(instruction_text3, (70, 60+50))
    screen.blit(instruction_text4, (70, 60+75))
    screen.blit(instruction_text5, (70, 60+100))
    screen.blit(instruction_text6, (70, 60+125))

def draw_buttons():
    if record_button_clicked == False:
        pygame.draw.rect(screen,record_color_dark,[5,5,30,30])
    else:
        pygame.draw.rect(screen,record_color_light,[5,5,30,30])

    if hover_record_button == True:
        pygame.draw.rect(screen,record_color_light,[5,5,30,30])

    if hover_play_button == True:
        pygame.draw.polygon(screen,play_color_light,[(45, 5),(70,20),(45,35)])
    else:
        pygame.draw.polygon(screen,play_color_dark,[(45, 5),(70,20),(45,35)])
        

    if hover_history_bn == True:
        pygame.draw.rect(screen,'#d9d9d9', history_bn)
        history_text = small_font.render('Search History', True, '#a6a6a6')
    else:
        pygame.draw.rect(screen,'#808080', history_bn)
        history_text = small_font.render('Search History', True, 'white')

    if hover_setting_bn == True:
        pygame.draw.rect(screen,'#d9d9d9', setting_bn)
        setting_text = medium_font.render('Option', True, '#a6a6a6')
    else:
        pygame.draw.rect(screen,'#808080', setting_bn)
        setting_text = medium_font.render('Option', True, 'white')

    screen.blit(setting_text, (5+90, 1))
    screen.blit(history_text, (5+62,215))
    
    key_lable2 = small_font.render(f'(Currnet Key: {currnet_key_name})          Use 1-7 on keyboard to play the chords', True, 'black')
    screen.blit(key_lable, (WIDTH-840, 49))
    screen.blit(key_lable2, (WIDTH-825, 75))

    
    for i in range(len(key_text_list)):
        if currnet_key_name == keys[i]:
            key_text_list[i] = small_font.render(f'{keys[i]}', True, 'white')
        else:
            key_text_list[i] = small_font.render(f'{keys[i]}', True, 'black')

        screen.blit(key_text_list[i], (WIDTH-700+ (30*i), 50))

def display_song(song_name=""):
    if play_check == 1:
        currnet_song = medium_font.render(f"Playing: {song_name}", True, 'black')
        screen.blit(currnet_song, (WIDTH - 1620, 2))


def play_load(playback):
    global active_blacks
    global active_whites
    if play_button_clicked == True:
        for i in range(len(playback)):
            if i == 0:
                pygame.time.delay(playback[i][2] - playback[0][2]) # - playback[0][2]
            else:
                pygame.time.delay(playback[i][2] - playback[i-1][2])

            if playback[i][0] == 'b':
                black_sounds[playback[i][1]].play(0, 1000)
                #active_blacks.append([playback[i][1], 30])
            if playback[i][0] == 'w':
                white_sounds[playback[i][1]].play(0, 3000)
                #active_whites.append([playback[i][1], 30])

def play(playback):
    global active_blacks
    global active_whites
    if play_clicked == True:
        for i in range(len(playback)):
            if i == 0:
                pygame.time.delay(playback[i][2] - playback[0][2]) # - playback[0][2]
            else:
                pygame.time.delay(playback[i][2] - playback[i-1][2])

            if playback[i][0] == 'b':
                black_sounds[playback[i][1]].play(0, 1000)
                active_blacks.append([playback[i][1], 30])
            if playback[i][0] == 'w':
                white_sounds[playback[i][1]].play(0, 3000)
                active_whites.append([playback[i][1], 30])

def get_source(url):
    try:
        session = HTMLSession()
        response = session.get(url)
        return response

    except requests.exceptions.RequestException as e:
        print(e)

def scrape_google(query):

    query = urllib.parse.quote_plus(query)
    response = get_source("https://www.google.co.uk/search?q=" + query)

    links = list(response.html.absolute_links)
    google_domains = ('https://www.google.', 
                      'https://google.', 
                      'https://webcache.googleusercontent.', 
                      'http://webcache.googleusercontent.', 
                      'https://policies.google.',
                      'https://support.google.',
                      'https://maps.google.')

    for url in links[:]:
        if url.startswith(google_domains):
            links.remove(url)

    return links

def get_link(list):
    for i in range(len(list)):
        if "tabs.ultimate-guitar.com" in list[i] and "translate.google" not in list[i]:
            return list[i]

def show_history():
    W = 1200
    H = 480
    history_text_list = []
    hover_clear_bn = False
    history_list = search_history.get_history()
    window_size = (W, H)
    # Create the window
    screen2 = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Pocket Piano Search History")

    history_lable = small_font.render(f'{"Song Name": <25}{"Author": <25}{"Key": <15}{"Chords": <80}{"Search Engine": <20}{"Url": <30}', True, 'white')
    for i in range(len(history_list)):
        history_text = small_font.render(f'{history_list[i]}', True, 'white')
        history_text_list.append(history_text)
    
    clear_bn = pygame.Rect(990,420,150,30)
    run = True
    while run:
        timer.tick(fps)
        screen2.fill('Black')
        mouse3 = pygame.mouse.get_pos()
        for i in range(len(history_text_list)):
            screen2.blit(history_text_list[i], (5, 5+(50*(i+1))))

        screen2.blit(history_lable, (5, 5))
        
        #hover clear bn condition
        if hover_clear_bn == True:
            pygame.draw.rect(screen2,'#d9d9d9', clear_bn)
            clear_text = medium_font.render('Clear History', True, '#a6a6a6')
        else:
            pygame.draw.rect(screen2,'#808080', clear_bn)
            clear_text = medium_font.render('Clear History', True, 'white')
        screen2.blit(clear_text, (1000, 415))

        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                #clear bn
                if clear_bn.collidepoint(event.pos):
                    if history_text_list != []:
                        ask = tkinter.messagebox.askyesno("Clear", "Do you want to clear your search history?")
                        if ask:
                            history_text_list = []
                            search_history.clear_history()
                    else:
                        tkinter.messagebox.showerror(None, "No history to clear")

        
        #hover clear bn (990,420,150,30)
        if mouse3[0] in range(990, 990+(150)) and mouse3[1] in range(420, 420+(30)):
            hover_clear_bn = True
        else:
            hover_clear_bn = False
        pygame.display.flip()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Pocket Piano")

def show_setting():
    global keybinds
    W = 540
    H = 480
    X = 175
    MANAGER = pygame_gui.UIManager((W, H))
    keybind_lable = small_font.render(f'{"Chord number": ^25}{"Change to": ^25}{"Current keybinds": ^25}{"Default": ^25}', True, 'white')
    keybinds_text_list = []
    keybinds_current_text_list = []
    keybinds_default_text_list = []
    hover_save_bn = False
    hover_set_to_default_bn = False
    alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    char_on_keyboard_list = ['1','2','3','4','5','6','7','8','9','0','-','=','+','/','\\','[',']','\'','\"']
    char_on_keyboard_list = char_on_keyboard_list + alphabet
    chord_nummber = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    for i in range(7):
        keybinds_text = small_font.render(f'{chord_nummber[i]: ^25}', True, 'white')
        keybinds_text_list.append(keybinds_text)
    for i in range(7):
        keybinds_default_text = small_font.render(f'{keybinds_default[i]: ^25}', True, 'white')
        keybinds_default_text_list.append(keybinds_default_text)
    
    
    TEXT_INPUT1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((X,50),(50,30)), manager=MANAGER, object_id='#1_text_entry')
    TEXT_INPUT2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((X,100),(50,30)), manager=MANAGER, object_id='#2_text_entry')
    TEXT_INPUT3 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((X,150),(50,30)), manager=MANAGER, object_id='#3_text_entry')
    TEXT_INPUT4 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((X,200),(50,30)), manager=MANAGER, object_id='#4_text_entry')
    TEXT_INPUT5 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((X,250),(50,30)), manager=MANAGER, object_id='#5_text_entry')
    TEXT_INPUT6 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((X,300),(50,30)), manager=MANAGER, object_id='#6_text_entry')
    TEXT_INPUT7 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((X,350),(50,30)), manager=MANAGER, object_id='#7_text_entry')
    text_input_list = [TEXT_INPUT1,TEXT_INPUT2,TEXT_INPUT3,TEXT_INPUT4,TEXT_INPUT5,TEXT_INPUT6,TEXT_INPUT7]
    for i in text_input_list:
        i.set_text_length_limit(1)
    TEXT_INPUT2.set_text_length_limit(1)
    window_size = (W, H)
    # Create the window
    screen3 = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Option")
    
    save_bn = pygame.Rect(260,420,70,30)
    set_to_default_bn = pygame.Rect(350,420,160,30)
    run = True
    while run:
        timer.tick(fps)
        screen3.fill('black')
        mouse2 = pygame.mouse.get_pos()
        
        #hover save bn condition
        if hover_save_bn == True:
            pygame.draw.rect(screen3,'#d9d9d9', save_bn)
            save_text = medium_font.render('Save', True, '#a6a6a6')
        else:
            pygame.draw.rect(screen3,'#808080', save_bn)
            save_text = medium_font.render('Save', True, 'white')
        screen3.blit(save_text, (270, 415))

        #hover set to default bn condition
        if hover_set_to_default_bn == True:
            pygame.draw.rect(screen3,'#d9d9d9', set_to_default_bn)
            set_to_default_text = medium_font.render('Set to Default', True, '#a6a6a6')
        else:
            pygame.draw.rect(screen3,'#808080', set_to_default_bn)
            set_to_default_text = medium_font.render('Set to Default', True, 'white')
        screen3.blit(set_to_default_text, (360, 415))

        screen3.blit(keybind_lable, (5, 5))
        for i in range(7):
            keybinds_current_text = small_font.render(f'{keybinds[i]: ^25}', True, 'white')
            keybinds_current_text_list.append(keybinds_current_text)
        for i in range(7):
            screen3.blit(keybinds_text_list[i], (15, 50+(50*i)))
        for i in range(7):
            screen3.blit(keybinds_current_text_list[i], (270, 50+(50*i)))
        for i in range(7):
            screen3.blit(keybinds_default_text_list[i], (405, 50+(50*i)))

        for event in pygame.event.get():
        
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                #save bn
                if save_bn.collidepoint(event.pos):
                    change_list = []
                    change_bool = False
                    duplicates = False
                    for i in range(len(text_input_list)):
                        change_list.append(text_input_list[i].get_text().upper())
                    for i in char_on_keyboard_list:
                        if i in change_list:
                            change_bool = True
                    for i in change_list:
                        if i in keybinds[:6]:
                            duplicates = True

                    #check for no duplicate inputs
                    while "" in change_list:
                        change_list.remove("")
                    while " " in change_list:
                        change_list.remove(" ")      
                    myset = set(change_list)
                    if len(change_list) != len(myset):
                        duplicates = True
                    if duplicates == False:
                        if change_bool:
                            ask = tkinter.messagebox.askyesno("Save", "Do you want to save your settings?")
                            if ask:
                                for i in range(len(text_input_list)):
                                    change = text_input_list[i].get_text().upper()
                                    if change != "" and change != " ":
                                        keybinds[i] = change

                                #access piano_lists local file and overwrite directly
                                filepath = f'{path}'+'/piano_lists.py'
                                
                                changed_keybinds = "keybinds = "+str(keybinds)
                                changed_piano_lists = piano_lists_front+changed_keybinds+piano_lists_back
                                with open(filepath, 'w') as f:
                                    f.write(changed_piano_lists)
                                #print("Data type before reconstruction : ", type(data))
                                
                                tkinter.messagebox.showinfo(None, "New keybinds has been saved")
                                #reset the window because current keybinds won't change for some reason IDK
                                show_setting()
                                run = False
                        else:
                            tkinter.messagebox.showerror(None, "Please change some setting")
                    else:
                        tkinter.messagebox.showerror(None, "Duplicates keybinds are not allow")


                #set_to_default bn
                if set_to_default_bn.collidepoint(event.pos):
                    if keybinds != keybinds_default:
                        ask = tkinter.messagebox.askyesno("Save", "Do you want to set your keybinds to default?")
                        if ask:
                            keybinds = keybinds_default.copy()
                            filepath = f'{path}'+'/piano_lists.py'
                            changed_piano_lists = piano_lists_all
                            with open(filepath, 'w') as f:
                                f.write(changed_piano_lists)
                            show_setting()
                            run = False
                    else:
                        tkinter.messagebox.showerror(None, "The keybinds are already set to default")

                    
            #hover save bn (260,420,70,30)
            if mouse2[0] in range(260, 260+(70)) and mouse2[1] in range(420, 420+(30)):
                hover_save_bn = True
            else:
                hover_save_bn = False

            #hover set_to_default bn (350,420,160,30)
            if mouse2[0] in range(350, 350+(160)) and mouse2[1] in range(420, 420+(30)):
                hover_set_to_default_bn = True
            else:
                hover_set_to_default_bn = False
            
            MANAGER.process_events(event)
        MANAGER.update(fps/10000)
        MANAGER.draw_ui(screen3)
        pygame.display.flip()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption("Pocket Piano")

setting_bn = pygame.Rect(5+80,5,30+65,30)
history_bn = pygame.Rect(5+60,215,30+65,26)
run = True
while run:
    timer.tick(fps)
    screen.fill('gray')
    white_keys, black_keys, active_whites, active_blacks = draw_piano(active_whites, active_blacks)
    draw_buttons()
    display_song(song_name)
    play(playback)
    play_load(playback)
    play_check = 0
    play_button_clicked = False
    play_clicked = False
    #show_text(entered_text) for debuging
    mouse = pygame.mouse.get_pos()
    draw_title_bar()
    

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            #print(time_when_click) for debuging
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            black_key = False
            for i in range(len(black_keys)):
                if black_keys[i].collidepoint(event.pos):
                    black_sounds[i].play(0, 1000)
                    black_key = True
                    active_blacks.append([i, 30])
                    time_when_click.append(['b',i, pygame.time.get_ticks()])
            for i in range(len(white_keys)):
                if white_keys[i].collidepoint(event.pos) and not black_key:
                    white_sounds[i].play(0, 3000)
                    active_whites.append([i, 30])
                    time_when_click.append(['w',i, pygame.time.get_ticks()])
            
            #record button
            if record_button_clicked == False:
                if 5 <= mouse[0] <= 5+30 and 5 <= mouse[1] <= 5+30:
                    tkinter.messagebox.showinfo(None, "Recording Started")
                    record_button_clicked = True
                    #record on
                    time_when_click = []
            else:
                if 5 <= mouse[0] <= 5+30 and 5 <= mouse[1] <= 5+30:
                    record_button_clicked = False
                    #record finish
                    if time_when_click == []:
                        tkinter.messagebox.showerror(None, "Nothing has been recorded")
                    else:
                        ask = tkinter.messagebox.askyesno("Save", "Do you want to save your recording?")
                        if ask:
                            try:
                                filepath = asksaveasfilename(filetypes=[('All Files', '.')], title="Save Pocket Piano Recording")
                                newfile = filepath

                                if os.path.exists(newfile):
                                    raise NameError

                                elif filepath is None:
                                    print("\nFile not saved\n")
                                else:
                                    try:
                                        newfiles.append(filepath)
                                        file = open(filepath, 'wb')
                                        pickle.dump(time_when_click, file)
                                        file.close()
                                    except:
                                        None

                            except NameError:
                                print("Name already existed")

            #play button
            if 45 <= mouse[0] <= 45+30 and 5 <= mouse[1] <= 5+30:
                filepath = askopenfilename()
                song_name = os.path.split(filepath)[1]
                try:
                    with open(filepath, 'rb') as handle:
                        data = handle.read()
                    #print("Data type before reconstruction : ", type(data))
                    d = pickle.loads(data)
                    #print("Data type after reconstruction : ", type(d))
                    playback = d
                    play_button_clicked = True
                except:
                    None
                play_check = 1
                display_song(song_name)

            # key c
            for i in range(len(keys)):
                if mouse[0] in range (WIDTH-700+ (30*i),WIDTH-700 + (30*i)+15) and mouse[1] in range (50, 50+15):
                    current_key = key_dict[keys[i]]
                    currnet_key_name = keys[i]
                    
            #history bn
            if history_bn.collidepoint(event.pos) and history_bn_clicked == False:
                show_history()


            elif history_bn.collidepoint(event.pos) and history_bn_clicked == True:
                show_history()

            #setting bn
            if setting_bn.collidepoint(event.pos) and setting_bn_clicked == False:
                show_setting()

            elif setting_bn.collidepoint(event.pos) and setting_bn_clicked == True:
                show_setting()


        if event.type == pygame.TEXTINPUT:
            for i in range(len(keybinds)):
                if event.text.upper() == keybinds[i] and hover_text_input == False:
                    playback = current_key[i]
                    for j in range(len(current_key[i])):
                        time_when_click.append([current_key[i][j][0], current_key[i][j][1], pygame.time.get_ticks()])
                    play_clicked = True

        #hover record
        if 5 <= mouse[0] <= 5+30 and 5 <= mouse[1] <= 5+30:
            hover_record_button = True
        else:
            hover_record_button = False
        
        #hover play
        if 45 <= mouse[0] <= 45+30 and 5 <= mouse[1] <= 5+30:
            hover_play_button = True
        else:
            hover_play_button = False

        #hover history (5+60,215,30+65,26) 
        if 5+60 <= mouse[0] <= 5+60+30+65 and 215 <= mouse[1] <= 215+26:
            hover_history_bn = True
        else:
            hover_history_bn = False

        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
            text_entry = True
            inc = 0
            entered_text = event.text

        #hover setting
        if 5+80 <= mouse[0] <= 5+80+30+65 and 5 <= mouse[1] <= 5+30:
            hover_setting_bn = True
        else:
            hover_setting_bn = False

        #hover text box
        if mouse[0] in range(5+80+30, 5+80+30+(30+80)) and mouse[1] in range(5+50, 5+50+(30)):
            hover_text_input = True
        else:
            hover_text_input = False
        MANAGER.process_events(event)
        

    MANAGER.update(fps/10000)
    MANAGER.draw_ui(screen)
    pygame.display.flip()
pygame.quit()
