from game import Game
from music_thread import start_music_thread, stop_music_thread

if __name__ == "__main__":
    game = Game()
    
    start_music_thread()
    game.gameLoop()
    stop_music_thread()

