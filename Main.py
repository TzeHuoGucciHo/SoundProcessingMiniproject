import numpy as np
import sounddevice as sd
import librosa
import tkinter as tk
from tkinter import Scale, HORIZONTAL

# Function to create a comb filter
def comb_filter(input_signal, delay_time, feedback_gain):
    output = np.zeros(len(input_signal) + delay_time)
    output[:len(input_signal)] = input_signal

    for i in range(delay_time, len(output)):
        output[i] += feedback_gain * output[i - delay_time]

    return output[:len(input_signal)]

# Function to create an allpass filter
def allpass_filter(input_signal, delay_time, feedback_gain):
    output = np.zeros(len(input_signal) + delay_time)
    output[:len(input_signal)] = input_signal

    for i in range(delay_time, len(output)):
        output[i] = -feedback_gain * output[i - delay_time] + input_signal[i - delay_time] + feedback_gain * output[i]

    return output[:len(input_signal)]

def play_audio(audio_data, rate):
    audio_data_2d = np.reshape(audio_data, (-1, 1))
    sd.play(audio_data_2d, rate)

def stop_audio():
    sd.stop()

def update_reverb():
    # Adjusted parameters for chapel-like reverb
    comb_delay_times = [comb_delay_slider.get()]
    comb_feedback_gains = [comb_feedback_slider.get()]
    allpass_delay_times = [allpass_delay_slider.get()]
    allpass_feedback_gains = [allpass_feedback_slider.get()]

    # Apply input signal to each comb filter
    reverb_signal = np.zeros(len(input_data))
    for i in range(len(comb_delay_times)):
        comb_output = comb_filter(input_data, comb_delay_times[i], comb_feedback_gains[i])
        reverb_signal += comb_output

    # Apply input signal to each allpass filter
    for i in range(len(allpass_delay_times)):
        allpass_output = allpass_filter(reverb_signal, allpass_delay_times[i], allpass_feedback_gains[i])
        reverb_signal = allpass_output

    # Normalize the reverb signal
    reverb_signal /= np.max(np.abs(reverb_signal))

    # Output the final reverb signal
    output_signal = reverb_signal

    play_audio(output_signal, input_rate)

input_file = "Guitar_Input_Audio.wav"
input_data, input_rate = librosa.load(input_file, sr=None, mono=True)

# Create a Tkinter window
window = tk.Tk()

# Create sliders for adjusting the reverb parameters
comb_delay_slider = Scale(window, from_=0, to=5000, orient=HORIZONTAL, length=400, label='Comb Filter Delay Time')
comb_delay_slider.set(1500)
comb_delay_slider.pack()
comb_feedback_slider = Scale(window, from_=0, to=1, resolution=0.01, orient=HORIZONTAL, length=400, label='Comb Filter Feedback Gain')
comb_feedback_slider.set(0.4)
comb_feedback_slider.pack()
allpass_delay_slider = Scale(window, from_=0, to=2500, orient=HORIZONTAL, length=400, label='Allpass Filter Delay Time')
allpass_delay_slider.set(750)
allpass_delay_slider.pack()
allpass_feedback_slider = Scale(window, from_=0, to=1, resolution=0.01, orient=HORIZONTAL, length=400, label='Allpass Filter Feedback Gain')
allpass_feedback_slider.set(0.4)
allpass_feedback_slider.pack()

# Create buttons for playing the input and output audio
play_input_button = tk.Button(window, text='Play Input', command=lambda: play_audio(input_data, input_rate))
play_input_button.pack()
play_output_button = tk.Button(window, text='Play Output', command=update_reverb)
play_output_button.pack()
stop_button = tk.Button(window, text='Stop', command=stop_audio)
stop_button.pack()

# Start the Tkinter event loop
window.mainloop()
