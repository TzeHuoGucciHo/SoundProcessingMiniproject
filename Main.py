import numpy as np
import sounddevice as sd
import librosa
import tkinter as tk
from tkinter import Scale, HORIZONTAL

# Function to create a comb filter
# This function applies a comb filter to the input signal. The comb filter simulates the effect of sound reflections in a room.
def comb_filter(input_signal, delay_time, feedback_gain):
    # Initialize the output signal with extra space for the delay
    output = np.zeros(len(input_signal) + delay_time)
    # Copy the input signal to the start of the output signal
    output[:len(input_signal)] = input_signal

    # Apply the comb filter equation to each sample
    for i in range(delay_time, len(output)):
        output[i] += feedback_gain * output[i - delay_time]

    # Return the filtered signal of the original length
    return output[:len(input_signal)]

# Function to create an allpass filter
# This function applies an allpass filter to the input signal. The allpass filter preserves the amplitude of the signal but changes its phase, contributing to the reverberation effect.
def allpass_filter(input_signal, delay_time, feedback_gain):
    # Initialize the output signal with extra space for the delay
    output = np.zeros(len(input_signal) + delay_time)
    # Copy the input signal to the start of the output signal
    output[:len(input_signal)] = input_signal

    # Apply the allpass filter equation to each sample
    for i in range(delay_time, len(output)):
        output[i] = -feedback_gain * output[i - delay_time] + input_signal[i - delay_time] + feedback_gain * output[i]

    # Return the filtered signal of the original length
    return output[:len(input_signal)]

# Function to play audio data
def play_audio(audio_data, rate):
    # Reshape the audio data for playback (mono to stereo if necessary)
    audio_data_2d = np.reshape(audio_data, (-1, 1))
    # Play the audio data using sounddevice
    sd.play(audio_data_2d, rate)

# Function to stop audio playback
def stop_audio():
    # Stop any currently playing audio
    sd.stop()

# Function to update the reverb effect based on user inputs from the sliders
def update_reverb():
    # Retrieve the current values of the sliders for comb filters
    comb_delay_times = [comb_delay_slider1.get(), comb_delay_slider2.get(), comb_delay_slider3.get(), comb_delay_slider4.get()]
    comb_feedback_gains = [comb_feedback_slider1.get(), comb_feedback_slider2.get(), comb_feedback_slider3.get(), comb_feedback_slider4.get()]
    # Retrieve the current values of the sliders for allpass filters
    allpass_delay_times = [allpass_delay_slider1.get(), allpass_delay_slider2.get()]
    allpass_feedback_gains = [allpass_feedback_slider1.get(), allpass_feedback_slider2.get()]

    # Apply the input signal to each comb filter in parallel
    reverb_signal = np.zeros(len(input_data))
    for i in range(len(comb_delay_times)):
        comb_output = comb_filter(input_data, comb_delay_times[i], comb_feedback_gains[i])
        reverb_signal += comb_output

    # Apply the reverb signal to each allpass filter in series
    for i in range(len(allpass_delay_times)):
        allpass_output = allpass_filter(reverb_signal, allpass_delay_times[i], allpass_feedback_gains[i])
        reverb_signal = allpass_output

    # Normalize the reverb signal to prevent clipping
    reverb_signal /= np.max(np.abs(reverb_signal))

    # Output the final reverb signal
    output_signal = reverb_signal

    # Play the final reverb signal
    play_audio(output_signal, input_rate)

# Load the input audio file
input_file = "Guitar_Input_Audio.wav"
input_data, input_rate = librosa.load(input_file, sr=None, mono=True)

# Create a Tkinter window for the user interface
window = tk.Tk()

# Create sliders for adjusting the comb filter parameters
comb_delay_slider1 = Scale(window, from_=0, to=5000, orient=HORIZONTAL, length=400, label='Comb Filter 1 Delay Time')
comb_delay_slider1.set(1557)
comb_delay_slider1.pack()
comb_feedback_slider1 = Scale(window, from_=0, to=1, resolution=0.01, orient=HORIZONTAL, length=400, label='Comb Filter 1 Feedback Gain')
comb_feedback_slider1.set(0.6)
comb_feedback_slider1.pack()

comb_delay_slider2 = Scale(window, from_=0, to=5000, orient=HORIZONTAL, length=400, label='Comb Filter 2 Delay Time')
comb_delay_slider2.set(1617)
comb_delay_slider2.pack()
comb_feedback_slider2 = Scale(window, from_=0, to=1, resolution=0.01, orient=HORIZONTAL, length=400, label='Comb Filter 2 Feedback Gain')
comb_feedback_slider2.set(0.6)
comb_feedback_slider2.pack()

comb_delay_slider3 = Scale(window, from_=0, to=5000, orient=HORIZONTAL, length=400, label='Comb Filter 3 Delay Time')
comb_delay_slider3.set(1491)
comb_delay_slider3.pack()
comb_feedback_slider3 = Scale(window, from_=0, to=1, resolution=0.01, orient=HORIZONTAL, length=400, label='Comb Filter 3 Feedback Gain')
comb_feedback_slider3.set(0.6)
comb_feedback_slider3.pack()

comb_delay_slider4 = Scale(window, from_=0, to=5000, orient=HORIZONTAL, length=400, label='Comb Filter 4 Delay Time')
comb_delay_slider4.set(1422)
comb_delay_slider4.pack()
comb_feedback_slider4 = Scale(window, from_=0, to=1, resolution=0.01, orient=HORIZONTAL, length=400, label='Comb Filter 4 Feedback Gain')
comb_feedback_slider4.set(0.6)
comb_feedback_slider4.pack()

# Create sliders for adjusting the allpass filter parameters
allpass_delay_slider1 = Scale(window, from_=0, to=2500, orient=HORIZONTAL, length=400, label='Allpass Filter 1 Delay Time')
allpass_delay_slider1.set(225)
allpass_delay_slider1.pack()
allpass_feedback_slider1 = Scale(window, from_=0, to=1, resolution=0.01, orient=HORIZONTAL, length=400, label='Allpass Filter 1 Feedback Gain')
allpass_feedback_slider1.set(0.5)
allpass_feedback_slider1.pack()

allpass_delay_slider2 = Scale(window, from_=0, to=2500, orient=HORIZONTAL, length=400, label='Allpass Filter 2 Delay Time')
allpass_delay_slider2.set(556)
allpass_delay_slider2.pack()
allpass_feedback_slider2 = Scale(window, from_=0, to=1, resolution=0.01, orient=HORIZONTAL, length=400, label='Allpass Filter 2 Feedback Gain')
allpass_feedback_slider2.set(0.5)
allpass_feedback_slider2.pack()

# Create buttons for playing the input and output audio
play_input_button = tk.Button(window, text='Play Input', command=lambda: play_audio(input_data, input_rate))
play_input_button.pack()
play_output_button = tk.Button(window, text='Play Output', command=update_reverb)
play_output_button.pack()
stop_button = tk.Button(window, text='Stop', command=stop_audio)
stop_button.pack()

# Start the Tkinter event loop
window.mainloop()
