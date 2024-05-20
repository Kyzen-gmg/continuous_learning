#!/c/Users/KLlor/AppData/Local/Microsoft/WindowsApps/python3
import time
from playsound import playsound

# Paths to your audio files
work_audio_file = 'path_to_your_work_audio_file.mp3'
break_audio_file = 'path_to_your_break_audio_file.mp3'

# Number of Pomodoro cycles
pomodoro_cycles = 5

for cycle in range(pomodoro_cycles):
        # 45-minute work timer
        time.sleep(45 * 60)
        print("Pomo is down, pomo is down!")
        playsound('D:\kyzen_trading_2024\scripts\gundam-warning-sound-sound-effect-made-with-Voicemod.mp3')
                        
        # 15-minute break timer
        time.sleep(15 * 60)
        print("Pomo has started, pomo has started!")
        playsound('D:\kyzen_trading_2024\scripts\gundam-warning-sound-sound-effect-made-with-Voicemod.mp3')

print("All Pomodoro cycles are complete!")

