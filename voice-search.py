import speech_recognition as sr
import pyttsx3
import requests 
from bs4 import BeautifulSoup
import webbrowser



r = sr.Recognizer()  

def recognize_speech_from_mic():
        print("say something: ")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source , duration=1)
                audio = r.listen(source)
                MyText = r.recognize_google(audio)
               

        except sr.RequestError as e:
            print("Could not request results; {0}".format(e)) 

        except sr.UnknownValueError:
            print("unknown error occured") 

        return MyText


def search(text):
    print('Googling...') # display text while downloading the Google page
    res = requests.get('https://google.com/search?q=' + ' '.join(text))
    res.raise_for_status()
    return res




   


if __name__ == "__main__":

   
    t=recognize_speech_from_mic()
    s=search(t)
    print(s.text)
    soup = BeautifulSoup(s.text , "html.parser")


    linkElems = soup.select(' a ')
    print(linkElems)
    numOpen = min(5, len(linkElems))
    for i in range(numOpen):
        webbrowser.open('https://google.com' + linkElems[i].get('href'))
        
  


 

       

