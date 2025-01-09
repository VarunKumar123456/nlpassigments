{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6b71a148-55ac-467d-bd78-2b937e1ab749",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "You:  hello\n",
      "You:  goodbye\n"
     ]
    }
   ],
   "source": [
    "import pyttsx3\n",
    "\n",
    "# Initialize the engine\n",
    "engine = pyttsx3.init()\n",
    "\n",
    "def speak(text):\n",
    "    \"\"\"Make the assistant speak.\"\"\"\n",
    "    engine.say(text)\n",
    "    engine.runAndWait()\n",
    "\n",
    "def main():\n",
    "    speak(\"Hello, I am your simple bot from Mallareddy University College.\")\n",
    "    speak(\"You can say hello, ask my name, or say goodbye.\")\n",
    "\n",
    "    while True:\n",
    "        command = input(\"You: \").lower()\n",
    "\n",
    "        # Respond to commands\n",
    "        if \"hello\" in command:\n",
    "            speak(\"Hi there! Welcome to Mallareddy University.\")\n",
    "        elif \"what's your name\" in command or \"what is your name\" in command:\n",
    "            speak(\"My name is Simple Bot from Mallareddy University.\")\n",
    "        elif \"goodbye\" in command:\n",
    "            speak(\"Goodbye! Have a great day at Mallareddy University.\")\n",
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
   "id": "18817949-c2c1-4e64-9fb7-f5dda700e70b",
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
