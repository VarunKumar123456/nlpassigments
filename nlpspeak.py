{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d31e16a1-4adb-4806-812b-28c95deb8f02",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pyttsx3\n",
    "import speech_recognition as sr\n",
    "\n",
    "engine = pyttsx3.init()\n",
    "\n",
    "def speak(text):\n",
    "    \"\"\"Make the assistant speak.\"\"\"\n",
    "    engine.say(text)\n",
    "    engine.runAndWait()\n",
    "\n",
    "def listen():\n",
    "    \"\"\"Listen to the user's voice command.\"\"\"\n",
    "    recognizer = sr.Recognizer()\n",
    "    with sr.Microphone() as source:\n",
    "        speak(\"I am listening, please speak.\")\n",
    "        audio = recognizer.listen(source)\n",
    "        try:\n",
    "            command = recognizer.recognize_google(audio)\n",
    "            return command.lower()\n",
    "        except sr.UnknownValueError:\n",
    "            speak(\"Sorry, I did not understand that.\")\n",
    "            return \"\"\n",
    "        except sr.RequestError:\n",
    "            speak(\"Sorry, my speech service is down.\")\n",
    "            return \"\"\n",
    "\n",
    "def main():\n",
    "    \"\"\"Main function to run the voice bot.\"\"\"\n",
    "    speak(\"Hello! I am your basic voice bot from Malla Reddy University. You can say hello.\")\n",
    "    while True:\n",
    "        command = listen()\n",
    "        if \"hello\" in command:\n",
    "            speak(\"Hi there! Welcome to Malla Reddy University.\")\n",
    "        elif \"what's your name\" in command or \"what is your name\" in command:\n",
    "            speak(\"My name is Basic Bot from Malla Reddy University.\")\n",
    "        elif \"goodbye\" in command:\n",
    "            speak(\"Goodbye! Have a great day at Malla Reddy University.\")\n",
    "            break\n",
    "        else:\n",
    "            speak(\"I didn't understand that. Please try again.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e302e965-ace9-4e7f-aa2f-8ed9eb0e7cf2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
