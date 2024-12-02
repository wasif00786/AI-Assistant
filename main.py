import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
import openai
# pip install SpeechRecognition
# pip install PyAudio
# pip install pyttsx3
# pip install requests
# pip install openai        i am using pip install openai==0.28.0...because i'm using old api method
# pip install pocketsphinx



# pip install pocketsphinx
recogniser = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "947d21879f7e45a4896ede4f54d75cfd"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def aiProcess(command):
    # Set your OpenAI API key.....change the api key if not woriking...need to buy a paln of open ai in order to get api
    openai.api_key = "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"  #replace your api key with this sample key

    # Create a chat completion
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use a valid model
            messages=[
                {"role": "system", "content": "You are a helpful virtual assistant named Jarvis."},
                {"role": "user", "content": command}
            ]
        )

        # Print the response
        return(response['choices'][0]['message']['content'])
    except Exception as e:
        print(f"An error occurred: {e}")
        
    
    
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open snapchat" in c.lower():
        webbrowser.open("https://snapchat.com")
    elif "open chat gpt" in c.lower():
        webbrowser.open("https://chatgpt.com")
    elif "open spotify" in c.lower():
        webbrowser.open("https://spotify.com")
         
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)
        
    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=947d21879f7e45a4896ede4f54d75cfd")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            
            # Printing the headlines
            for article in articles:
                speak(article['title'])
                
                
    else:
        #let open ai handles the request
        output = aiProcess(c)
        speak(output)
        
        
    
if __name__ == "__main__":
    speak("Initializing jarvis....")
    while True:
        #listing for the wake word "jarvis"
        #obtain audio from the microphone
        r = sr.Recognizer()
        

        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listning...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes captain....")
                # listen for command
                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
                
        except Exception as e:
            print("error; {0}".format(e))            
            
            
