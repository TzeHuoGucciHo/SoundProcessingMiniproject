MED4	Soundprocessing Miniproject
---
## Interface Overview

The application interface consists of sliders and buttons that allow you to adjust the parameters of the reverb effect.

### Sliders

#### Comb Filter Parameters

1. **Comb Filter 1 Delay Time**
   - Adjusts the delay time for the first comb filter.
   - Range: 0 to 5000
   - Default: 1557

2. **Comb Filter 1 Feedback Gain**
   - Adjusts the feedback gain for the first comb filter.
   - Range: 0 to 1 (with a resolution of 0.01)
   - Default: 0.6

3. **Comb Filter 2 Delay Time**
   - Adjusts the delay time for the second comb filter.
   - Range: 0 to 5000
   - Default: 1617

4. **Comb Filter 2 Feedback Gain**
   - Adjusts the feedback gain for the second comb filter.
   - Range: 0 to 1 (with a resolution of 0.01)
   - Default: 0.6

5. **Comb Filter 3 Delay Time**
   - Adjusts the delay time for the third comb filter.
   - Range: 0 to 5000
   - Default: 1491

6. **Comb Filter 3 Feedback Gain**
   - Adjusts the feedback gain for the third comb filter.
   - Range: 0 to 1 (with a resolution of 0.01)
   - Default: 0.6

7. **Comb Filter 4 Delay Time**
   - Adjusts the delay time for the fourth comb filter.
   - Range: 0 to 5000
   - Default: 1422

8. **Comb Filter 4 Feedback Gain**
   - Adjusts the feedback gain for the fourth comb filter.
   - Range: 0 to 1 (with a resolution of 0.01)
   - Default: 0.6

#### Allpass Filter Parameters

1. **Allpass Filter 1 Delay Time**
   - Adjusts the delay time for the first allpass filter.
   - Range: 0 to 2500
   - Default: 225

2. **Allpass Filter 1 Feedback Gain**
   - Adjusts the feedback gain for the first allpass filter.
   - Range: 0 to 1 (with a resolution of 0.01)
   - Default: 0.5

3. **Allpass Filter 2 Delay Time**
   - Adjusts the delay time for the second allpass filter.
   - Range: 0 to 2500
   - Default: 556

4. **Allpass Filter 2 Feedback Gain**
   - Adjusts the feedback gain for the second allpass filter.
   - Range: 0 to 1 (with a resolution of 0.01)
   - Default: 0.5

### Buttons

1. **Play Input**
   - Plays the original input audio file.

2. **Play Output**
   - Applies the reverb effect with the current slider settings and plays the resulting audio.

3. **Stop**
   - Stops any currently playing audio.

## Instructions for Use

1. **Load the Input Audio File**
   - Ensure the input audio file is named `Guitar_Input_Audio.wav` and is in the same directory as the script.

2. **Adjust Comb Filter Parameters**
   - Use the sliders labeled "Comb Filter X Delay Time" and "Comb Filter X Feedback Gain" to adjust the delay time and feedback gain for each of the four comb filters.

3. **Adjust Allpass Filter Parameters**
   - Use the sliders labeled "Allpass Filter X Delay Time" and "Allpass Filter X Feedback Gain" to adjust the delay time and feedback gain for each of the two allpass filters.

4. **Play Input Audio**
   - Click the "Play Input" button to listen to the original input audio file.

5. **Apply Reverb Effect**
   - Adjust the sliders to set your desired reverb parameters.
   - Click the "Play Output" button to apply the reverb effect with the current settings and listen to the processed audio.

6. **Stop Audio Playback**
   - Click the "Stop" button to stop any audio that is currently playing.

## Notes

- The reverb effect parameters can be adjusted before pressing "Play Output" to hear the changes.
- The output reverb signal is normalized to prevent clipping.
- Experiment with different settings to achieve a variety of reverb effects. 

---