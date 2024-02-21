
import threading
from gesture_recognition import get_current_gesture
from mail_system import activeCurrentDaySchedule

mail_system_thread = threading.Thread(target=activeCurrentDaySchedule)
gesture_recognition_thread = threading.Thread(target=get_current_gesture)

gesture_recognition_thread.start()
mail_system_thread.start()
