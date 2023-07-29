import speech_recognition as sr
import os


# Para listar os microfones do seu computador
# print(sr.Microphone().list_microphone_names())


# Cria um reconhecedor de voz
r = sr.Recognizer()


# Inicia o microfone
with sr.Microphone(1) as source:
    print("Say something:")
    audio = r.listen(source)


response = {
    "success": True,
    "error": None,
    "transcription": None
}


try:
    response["transcription"] = r.recognize_google(audio, language="pt-BR")
except sr.RequestError:
    response["success"] = False
    response["error"] = "API unavailable"
except sr.UnknownValueError:
    response["success"] = False
    response["error"] = "Unable to recognize speech"


text = None


if response["success"]:
    text = "{}".format(response["transcription"])
else:
    print("Erro: {}".format(response["error"]))


if text.lower() == "computador desligar":
    os.system("shutdown -s -t 0")