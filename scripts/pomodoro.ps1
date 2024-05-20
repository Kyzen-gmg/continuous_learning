# Paths to your audio files
$workAudioFile = "ms-warning2.wav"
$breakAudioFile = "ms-warning2.wav"

# Number of Pomodoro cycles
$pomodoroCycles = 5

for ($cycle = 0; $cycle -lt $pomodoroCycles; $cycle++) {
    # 45-minute work timer
    Start-Sleep -Seconds (45 * 60)
    Write-Output "Pomo is down, pomo is down!"
    [System.Media.SoundPlayer]::new($workAudioFile).PlaySync()

    # 15-minute break timer
    Start-Sleep -Seconds (15 * 60)
    Write-Output "Pomo has started, pomo has started!"
    [System.Media.SoundPlayer]::new($breakAudioFile).PlaySync()
}

Write-Output "All Pomodoro cycles are complete!"
