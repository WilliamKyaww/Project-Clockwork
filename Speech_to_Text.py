import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()

def speech_input():
    while(1):
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                print("\033[93m Active \033[0m")
                
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower() 
                
                return MyText
        
        except sr.RequestError as e:
            print("\033[91m Could not request results; {0} \033[0m".format(e))
            print()
            
        except sr.UnknownValueError:
            print("\033[91m Unknown error occurred \033[0m")
            print()
            
