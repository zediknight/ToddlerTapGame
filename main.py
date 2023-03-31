import pygame
import random
import os

pygame.init()

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tap Game For Toddlers")

def load_resources():
    image_files = os.listdir("images")
    sound_files = os.listdir("sounds")
    images = []
    sounds = []

    for file in image_files:
        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            images.append(pygame.image.load(os.path.join("images", file)))

    for file in sound_files:
        if file.lower().endswith(('.wav', '.mp3')):
            sounds.append(os.path.join("sounds", file))

    if not images or not sounds:
        raise Exception("Error: Make sure there is at least one image and one sound in the respective folders.")

    return images, sounds

images, sounds = load_resources()

def game_loop():
    running = True
    current_image = random.choice(images)
    current_sound = random.choice(sounds)

    while running:
        window.fill((255, 255, 255))
        window.blit(current_image, (WINDOW_WIDTH // 2 - current_image.get_width() // 2,
                                     WINDOW_HEIGHT // 2 - current_image.get_height() // 2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                current_image = random.choice(images)
                current_sound = random.choice(sounds)
                pygame.mixer.music.stop()
                pygame.mixer.music.load(current_sound)
                pygame.mixer.music.play()

    pygame.quit()

game_loop()