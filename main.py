import pygame
import pygame_gui
import pygame.freetype
import pickle
import piano_lists as pl
from pygame import mixer
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import os.path
import requests
import urllib.request 
from requests_html import HTMLSession
import re

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
hover_record_button = False
hover_play_button = False
hover_setting_bn = False
setting_bn_clicked = False
text_input_clicked = False
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

left_hand = pl.left_hand
right_hand = pl.right_hand
piano_notes = pl.piano_notes
white_notes = pl.white_notes
black_notes = pl.black_notes
black_labels = pl.black_labels
keys = pl.keys
keybinds = pl.keybinds
key_dict = pl.key_dict
key_all = pl.key_all

current_key = key_dict[keys[0]] # key C default
currnet_key_name = key_all[0]

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

pygame.display.set_caption("Python Piano")


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
    instruction_text = small_font.render(f'Search:', True, 'black')
    instruction_text2 = small_font.render('(Search any song on the internet)', True, 'black')
    instruction_text3 = small_font.render(f'Song: {song_list[-1].getName()}', True, 'black')
    instruction_text4 = small_font.render(f'Author: {author_name}', True, 'black')
    instruction_text5 = small_font.render(f'Key: {song_key}', True, 'black')
    instruction_text6 = small_font.render(f'Chords: {song_list[-1].getChords()}', True, 'black')
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
    
    key_lable2 = small_font.render(f'(Currnet Key: {currnet_key_name})          Use 1-7 on keyboard to play the chords', True, 'black')
    screen.blit(key_lable, (WIDTH-840, 49))
    screen.blit(key_lable2, (WIDTH-825, 75))
    for i in range(len(key_text_list)):
        screen.blit(key_text_list[i], (WIDTH-700+ (30*i), 50))

def display_song(song_name=""):
    currnet_song = medium_font.render(song_name, True, 'black')
    screen.blit(currnet_song, (WIDTH - 1720, 2))


def play(playback):
    if play_button_clicked == True:
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
    
relative_rec = pygame.Rect(5+80+30+65+10,5,30+65,30)
run = True
while run:
    left_dict = {'Z': f'C{left_oct}',
                 'S': f'C#{left_oct}',
                 'X': f'D{left_oct}',
                 'D': f'D#{left_oct}',
                 'C': f'E{left_oct}',
                 'V': f'F{left_oct}',
                 'G': f'F#{left_oct}',
                 'B': f'G{left_oct}',
                 'H': f'G#{left_oct}',
                 'N': f'A{left_oct}',
                 'J': f'A#{left_oct}',
                 'M': f'B{left_oct}'}
                  
    right_dict = {'=': f'C{right_oct}',
                  ']': f'C#{right_oct}',
                  '[': f'D{right_oct}',
                  '-': f'D#{right_oct}',
                  '/': f'E{right_oct}',
                  'U': f'F{right_oct}',
                  '8': f'F#{right_oct}',
                  'I': f'G{right_oct}',
                  '9': f'G#{right_oct}',
                  'O': f'A{right_oct}',
                  '0': f'A#{right_oct}',
                  'P': f'B{right_oct}'}

    timer.tick(fps)
    screen.fill('gray')
    white_keys, black_keys, active_whites, active_blacks = draw_piano(active_whites, active_blacks)
    draw_buttons()
    display_song(song_name)
    play(playback)
    play_button_clicked = False
    #show_text(entered_text)
    mouse = pygame.mouse.get_pos()
    draw_title_bar()

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            print(time_when_click)
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
                    record_button_clicked = True
                    #record on
                    time_when_click = []
            else:
                if 5 <= mouse[0] <= 5+30 and 5 <= mouse[1] <= 5+30:
                    record_button_clicked = False
                    #record finish
                    if time_when_click == []:
                        None
                    else:
                        try:
                            filepath = asksaveasfilename(filetypes=[('All Files', '.')], title="Save Python Piano Recording")
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

            # key c
            for i in range(len(keys)):
                if mouse[0] in range (WIDTH-700+ (30*i),WIDTH-700 + (30*i)+15) and mouse[1] in range (50, 50+15):
                    current_key = key_dict[keys[i]]
                    currnet_key_name = keys[i]

            if relative_rec.collidepoint(event.pos) and text_input_clicked == False:
                text_input_clicked = True
            else:
                text_input_clicked = False


        if event.type == pygame.TEXTINPUT:
            for i in range(len(keybinds)):
                if event.text.upper() == keybinds[i]:
                    playback = current_key[i]
                    for j in range(len(current_key[i])):
                        time_when_click.append([current_key[i][j][0], current_key[i][j][1], pygame.time.get_ticks()])
                    play_button_clicked = True

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

        if 5+80 <= mouse[0] <= 5+80+30+65 and 5 <= mouse[1] <= 5+30:
            hover_setting_bn = True
        else:
            hover_setting_bn = False

        if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#main_text_entry":
            text_entry = True
            inc = 0
            entered_text = event.text
                    
        MANAGER.process_events(event)

    MANAGER.update(fps/10000)
    MANAGER.draw_ui(screen)
    pygame.display.flip()
pygame.quit()
