
class Event():

    def invoke(self, event):
       pass
        

class OnTextChanged(Event):
 '''
 listener extendable any class wishing to rercive
 text from possible observers must override the method
 '''   
 def On_text_input_changed(self,text: str, event):
    raise NotImplementedError("missing Override of this function")


class OnTextLoaded(Event):

 def On_text_input_loaded(self, text: str, event):
    raise NotImplementedError("missing Override of this function")


class EventObserver():
    '''
    singelton class for obeservers to extend 
    all observers chare the same class so a event 
    param is taken with the call to pass a refrence to the
    class invoking the call for listners to know who's calling
    '''
    
    _instance = None
    _listeners: list[Event] = []
  
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def invoke(self,event):
        for i in range(0, len(EventObserver._listeners)):
            if isinstance(EventObserver._listeners[i], Event):
                EventObserver._listeners[i].invoke(event)
                
                
    def invoke_On_text_changed(self,text: str, event):
        '''
        event: is the class evoking the event
        text: the message text 
        '''
        for i in range(0,len(EventObserver._listeners)):
            if isinstance(EventObserver._listeners[i], OnTextChanged):
               event:OnTextChanged = EventObserver._listeners[i]
               event.On_text_input_changed(text, event)

    def invoke_On_text_loaded(self,text: str, event):
        for i in range(0,len(EventObserver._listeners)):
            if isinstance(EventObserver._listeners[i], OnTextLoaded):
               event:OnTextLoaded = EventObserver._listeners[i]
               event.On_text_input_loaded(text, event)
    
    def sub_event(listeners: Event):
        if not EventObserver._listeners.__contains__(listeners):
            EventObserver._listeners.append(listeners)

    

    def unsub_event(listeners: Event):
        if EventObserver._listeners.__contains__(listeners):
            EventObserver._listeners.append(listeners)

