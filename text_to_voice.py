from gtts import gTTS
import os
import pygame

# Define the text you want to convert to speech
text = "Hello, kia kr rhi o"

# Create a gTTS object
tts = gTTS(text=text, lang='en', slow=False)

# Save the converted audio to a file
tts.save("output.mp3")

# Play the converted file (this works on most systems)
print()

# Initialize pygame mixer
pygame.mixer.init()

# Load and play the converted file
pygame.mixer.music.load("output.mp3")
pygame.mixer.music.play()

# Keep the script running until the audio finishes playing
while pygame.mixer.music.get_busy():
    pass