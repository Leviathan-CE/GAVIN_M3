
try:
    
    from src.gui.widgets.Form import Form, ApiKeyForm
    from PyQt6.QtWidgets import (
        QApplication,
        QWidget

    )   
    from src.data.Paths import GUI_STYLES
    import sys

    from src.models.Gavin import  GavinMarkI
    from src.api.EventHandler import (
            EventObserver,
            EvenHandlerInputText,
            EventHandlerPushMessages,
            EventHandlerWindowSize
        )
    from src.gui.widgets.MarkdownLatexViewer import MarkdownLatexViewer
    from src.gui.widgets.ChatHistory import ViewPort      
    from src.gui.widgets.TextInputBar import TextInputBar
    from PyQt6.QtCore import Qt
    from PyQt6.QtWidgets import QVBoxLayout
    from src.api.Exceptions import ApiKeyNotFoundException
except Exception as e:
            import traceback
             # Log the exception details to a file or print them
            with open("error_log.txt", "w") as f:
                traceback.print_exc(file=f)
            # Print the exception details to the console
            traceback.print_exc()
            input("Press Enter to exit...")
            sys.exit(1)

if __name__ == "__main__":
    
    
    eventhandlers: list = [EventObserver(),
                            EventHandlerWindowSize(),
                            EvenHandlerInputText(),
                            EventHandlerPushMessages()]

    app = QApplication(sys.argv)


    
    def main(): 

        
        
        llm_model = GavinMarkI()
        llm_model.active_model = GavinMarkI.MODEL
        
        
        form_main = Form()
        form_main.move((form_main.pos().x()/2).__round__(),
                    (form_main.pos().y()/2).__round__())

        form_main.setFixedSize(600, 800)
        chat_scrol_view = ViewPort(550, 350)
        chat_scrol_view.load_from_db(5)
        margins = QWidget()    
        input_text_bar = TextInputBar(500)


            # for what ever reason if vewier is not populated
            # then wierd minimize glitch occurs.
        empty_message = MarkdownLatexViewer(
                "", chat_scrol_view)
        empty_message.setMaximumHeight(0)
        chat_scrol_view.add_widget(empty_message)
        margins.setContentsMargins(10,0,10,10)
            
        form_main.setCenterWidget(margins)
        margins.setLayout(QVBoxLayout())
        margins.layout().addWidget(chat_scrol_view)
        margins.layout().addWidget(input_text_bar)
            
        margins.layout().setAlignment(input_text_bar, Qt.AlignmentFlag.AlignHCenter)
        margins.layout().setAlignment(chat_scrol_view, Qt.AlignmentFlag.AlignHCenter)
       
        file = open(GUI_STYLES+"\\dark_mode.css", "r")
        app.setStyleSheet(file.read())
        file.close()
        app.exec()

       

       
        
    try:    
        try:   
            main()
        except ApiKeyNotFoundException:
                api_form = ApiKeyForm(main)
                file = open(GUI_STYLES+"\\dark_mode.css", "r")
                app.setStyleSheet(file.read())
                file.close()
                app.exec()
    except Exception as e:
            import traceback
             # Log the exception details to a file or print them
            with open("{ROOT}/error_log.txt", "w") as f:
                traceback.print_exc(file=f)
            # Print the exception details to the console
            traceback.print_exc()
            input("Press Enter to exit...")
            sys.exit(1)
    

        

