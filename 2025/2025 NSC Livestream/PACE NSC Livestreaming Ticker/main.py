import config
import ticker
import gui
import obs

config.init()

config.time.sleep(1)

gui_ticker = config.threading.Thread(target=gui.init_gui, daemon=True)
gui_ticker.start()
'''
thread_ticker = config.threading.Thread(target=ticker.loop_ticker, daemon=True)
thread_ticker.start()
'''
try:
    while True:
        config.time.sleep(1)

except Exception as e:
    config.stop()
    print(f"Failed to connect or perform actions: {e}")

config.stop()