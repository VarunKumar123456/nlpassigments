{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "52e9bd00-ac14-41c9-9349-d35bca6cea03",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Integer: 10 Type: <class 'int'>\n",
      "Float: 3.14 Type: <class 'float'>\n",
      "String: Hello, World! Type: <class 'str'>\n",
      "Boolean: True Type: <class 'bool'>\n"
     ]
    }
   ],
   "source": [
    "# Declare variables of different data types\n",
    "integer_var = 10\n",
    "float_var = 3.14\n",
    "string_var = \"Hello, World!\"\n",
    "boolean_var = True\n",
    "\n",
    "# Print each variable and its type\n",
    "print(\"Integer:\", integer_var, \"Type:\", type(integer_var))\n",
    "print(\"Float:\", float_var, \"Type:\", type(float_var))\n",
    "print(\"String:\", string_var, \"Type:\", type(string_var))\n",
    "print(\"Boolean:\", boolean_var, \"Type:\", type(boolean_var))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "ec77bafa-6fac-43c2-8d4c-fc43d734c1af",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "def is_palindrome(s):\n",
    "    return s == s[::-1]\n",
    "\n",
    "# Test the function\n",
    "print(is_palindrome(\"radar\")) \n",
    "print(is_palindrome(\"hello\"))  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b7b3f463-e72f-4c57-96c1-f668c5210e0e",
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
