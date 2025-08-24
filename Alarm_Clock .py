import time
from datetime import datetime
from playsound import playsound  # pip install playsound==1.2.2

def alarm_clock(alarm_time, sound_file):
    print(f"⏰ Alarm set for {alarm_time}")
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            print("🔔 Time to wake up!")
            playsound(sound_file)  # Play alarm sound (MP3/WAV)
            break
        time.sleep(10)  # check every 10 seconds

if __name__ == "__main__":
    alarm_time = input("Enter alarm time (HH:MM in 24hr format): ")
    sound_file = "alarm.mp3"  # replace with your file path
    alarm_clock(alarm_time, sound_file)
