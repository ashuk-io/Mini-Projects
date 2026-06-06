import time
from plyer import notification

while True:
    notification.notify(title='Reminder', 
                        
                        message='You should drink some water now')
    time.sleep(5)





