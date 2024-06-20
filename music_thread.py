import pygame as p
import threading

def play_music():
    p.mixer.init()
    p.mixer.music.load("./theme.mp3")
    p.mixer.music.play(-1)
    
def stop_music():
    p.mixer.music.stop()
    
def start_music_thread():
    music_thread = threading.Thread(target=play_music)
    music_thread.start()
    
def stop_music_thread():
    stop_music()
    p.mixer.quit()