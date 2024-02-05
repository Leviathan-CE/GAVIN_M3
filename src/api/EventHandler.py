from src.data import WindowHints
from src.api.Events import (
    Event,
    OnPushMessageToDisplay,
    OnTextChanged,
    OnWindowResized
 )
class EventObserver():
    '''
     non singleton class for obeservers to extend
     so each child can have a singelton of its own
     with the same base functionality
    '''
    _instance = None
    _listeners: list[Event] = []
    
    def invoke(self,event):
        for i in range(0, len(EventObserver._listeners)):
            if isinstance(EventObserver._listeners[i], Event):
                EventObserver._listeners[i].invoke(event)
    
    def sub_event(self,listeners: Event):
        if not EventObserver._listeners.__contains__(listeners):
            EventObserver._listeners.append(listeners)   

    def unsub_event(self,listeners: Event):
        if EventObserver._listeners.__contains__(listeners):
            EventObserver._listeners.append(listeners)



class EventHandlerWindowSize(EventObserver):

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
   
        
    def invoke_on_window_size_changed(self, hint: WindowHints, event):
        '''
           event: is the class evoking the event
           text: the message text 
           '''
        for i in range(0, len(EventObserver._listeners)):
            if isinstance(EventObserver._listeners[i], OnWindowResized):
               events: OnWindowResized = EventObserver._listeners[i]
               events.on_window_resize(hint, event)

class EvenHandlerInputText(EventObserver):
  
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    
    def invoke_On_text_changed(self, text: str, event):
        '''
           event: is the class evoking the event
           text: the message text 
           '''
        for i in range(0, len(EventObserver._listeners)):
            if isinstance(EventObserver._listeners[i], OnTextChanged):
                events: OnTextChanged = EventObserver._listeners[i]
                events.On_text_input_changed(text, event)

class EventHandlerPushMessages(EventObserver):
  
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def invoke_on_push_message(self, text: str, event):
        '''
           event: is the class evoking the event
           text: the message text 
           '''
        for i in range(0, len(EventObserver._listeners)):
            if isinstance(EventObserver._listeners[i], OnPushMessageToDisplay):
               events: OnPushMessageToDisplay = EventObserver._listeners[i]
               events.on_push_message(text, event)
