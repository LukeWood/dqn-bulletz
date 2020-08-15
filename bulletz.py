import atexit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

import time

class Bulletz():
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.actions = ActionChains(self.driver)
        atexit.register(lambda: self.driver.quit())

    def start(self):
        self.driver.get("https://bulletz.io/play?server=memes.bulletz.io")
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, "play")))
        self.driver.find_element_by_id("play").click()

    def dispatch_key_event(self, key, activation):
        keySet = f"var key = \"{key}\";"
        activationSet = f"var activation = \"{activation}\";"
        self.driver.execute_script(
        keySet + "\n" + activationSet + "\n" + """
            if(document.createEventObject) {
                var eventObj = document.createEventObject();
                eventObj.key = key
                document.body.fireEvent("on" + activation, eventObj);   
            } else if(document.createEvent) {
                var eventObj = document.createEvent("Events");
                eventObj.initEvent(activation, true, true);
                eventObj.key = key
                document.body.dispatchEvent(eventObj);
            }
        """)

    def reset_input(self):
        for i in ["ArrowRight", "ArrowLeft", "ArrowUp", "ArrowDown"]:
            self.dispatch_key_event("ArrowRight", "keyup")

    def alive(self):
        self.driver.find_element_by_id("player-stats")

    def score(self):

    
    def right(self):
        self.dispatch_key_event("ArrowRight", "keydown")

    def left(self):
        self.dispatch_key_event("ArrowLeft", "keydown")

    def up(self):
        self.dispatch_key_event("ArrowUp", "keydown")

    def down(self):
        self.dispatch_key_event("ArrowDown", "keydown")

b = Bulletz()
b.start()
b.right()
time.sleep(5)
b.reset_input()
time.sleep(1)
b.left()
time.sleep(5)
