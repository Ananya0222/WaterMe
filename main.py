import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="**Please water the plants now**",
            message="Water the Plants, It's time to water the Plants!",
            app_name="WaterMe",
            timeout=15
        )
        time.sleep(60*60)


    
