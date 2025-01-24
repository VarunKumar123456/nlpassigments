{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5087ac42-17ab-400f-ac19-406aa9df8279",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Title of the webpage: Example Domain\n"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "\n",
    "# URL to be fetched\n",
    "url = 'https://example.com'\n",
    "\n",
    "# Send a GET request to the URL\n",
    "response = requests.get(url)\n",
    "\n",
    "# Parse the HTML content of the page\n",
    "soup = BeautifulSoup(response.content, 'html.parser')\n",
    "\n",
    "# Find and print the title of the page\n",
    "title = soup.title.string\n",
    "print(f\"Title of the webpage: {title}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d7561e7-b755-49b2-8776-75f5babba36a",
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
