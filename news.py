import requests
import json
url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=77c0b1893deb43ceb7d4d6eb40b0cc68"
news = requests.get(url).text
news_dict = json.loads(news)
arts=news_dict['articles']

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__== '__main__':
    speak("news for today...let's begin")
    i = 1
    for articles in arts:
        print(i)
        speak(i)
        print(articles['title'])
        speak(articles['title'])
        i=i+1
