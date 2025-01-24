{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "5087ac42-17ab-400f-ac19-406aa9df8279",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['support@example.com', 'sales@example.org']\n"
     ]
    }
   ],
   "source": [
    "import re\n",
    "\n",
    "def extract_emails(text):\n",
    "    # Regular expression pattern for matching email addresses\n",
    "    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}'\n",
    "    \n",
    "    # Find all email addresses in the text\n",
    "    emails = re.findall(email_pattern, text)\n",
    "    \n",
    "    return emails\n",
    "\n",
    "# Example usage\n",
    "text = 'Contact us at support@example.com and sales@example.org.'\n",
    "emails = extract_emails(text)\n",
    "print(emails)  # Output: ['support@example.com', 'sales@example.org']\n"
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
