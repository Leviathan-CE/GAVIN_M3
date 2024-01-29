

from src.api.EventHandler import OnTextChanged, EventObserver


class GAVIN_MODEL_M3(OnTextChanged, EventObserver):
    
    def __init__(self):
        EventObserver.sub_event(self)
    
    def On_text_input_changed(self,text:str, event):
        print(f"{text} + it worked")
        


   