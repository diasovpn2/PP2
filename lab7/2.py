import os
import pygame

pygame.init()
pygame.mixer.init()

playlist = [f for f in os.listdir() if f.endswith(".mp3")]
current_track = 0

def play_music(track):
    pygame.mixer.music.load(playlist[track])
    pygame.mixer.music.play()
    print(f"Playing: {playlist[track]}")


if playlist:
    play_music(current_track)
else:
    print("No music files found in the folder.")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    print("Paused")
                else:
                    pygame.mixer.music.unpause()
                    print("Resumed")
            elif event.key == pygame.K_s:  
                pygame.mixer.music.stop()
                print("Stopped")
            elif event.key == pygame.K_n:  
                current_track = (current_track + 1) % len(playlist)
                play_music(current_track)
            elif event.key == pygame.K_p:  
                current_track = (current_track - 1) % len(playlist)
                play_music(current_track)

pygame.quit()