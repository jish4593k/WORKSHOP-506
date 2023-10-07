import random
import string
import tkinter as tk

class Node:
    def __init__(self, word):
        self.word = word
        self.next = None

def put_word_in_place(n, p):
   global ar
   q = ar[n]
   qq = None
   wor = Node(p)
   if q is None:
        ar[n] = wor
    else:
        while q is not None:
            if wor.word == q.word:
               return
          qq = q
             q = q.next
        qq.next = wor

def get_word(n):
   global ar
    i = 0
    p = ar[n]
    while p is not None:
        p = p.next
        i += 1
    j = random.randint(0, i - 1)
    p = ar[n]
    for _ in range(j):
       p = p.next
    return p.word

def get_line(n):
    global ar
    index = 0
    line = ""
    while True:
      str_len = random.randint(1, n)
  str_word = get_word(str_len)
        line += str_word + " "
        index += len(str_word) + 1
        n -= str_len
        if n == 0:
            break
    line = line[:-1]
    return line

def make_list():
    global ar
    with open("syllable_words.txt", "r") as op:
  i = 1
             j = 0
        word = ""
        while True:
            ch = op.read(1)
            if not ch:
               break
            if ch == " ":
                put_word_in_place(i, word)
                word = ""
            elif ch == "\n":
                i += 1
            else:
                word += ch

def count_syllable(word):
    consecutive_vowel = 0
    num_of_syllable = 0
    flag = False

    vowels = "aeiou"
    if word[0] != 'y':
                vowels += 'y'

    for i in range(len(word)):
             if word[i] == 'e' and word[i + 1:i + 2] == "" and i > 2 and word[i - 1] != 'l':
    i += 1
                       continue
        elif (word[i - 1:i + 2] == "ti" or word[i - 1:i + 2] == "si") and word[i + 2:i + 5] == "ion":
            num_of_syllable += 1
                   consecutive_vowel = 0
            flag = False
               i += 4
            continue
          elif word[i:i + 3] == "sm" and word[i + 3:i + 5] == "":
                  num_of_syllable += 1
            break
        elif word[i:i + 2] == "ti" and word[i + 2:i + 3] in vowels:
            num_of_syllable += 1
        if not (word[i] in vowels):
            if flag:
                flag = False
                                             cal = round(float(consecutive_vowel / 2.0 + 0.111))
                num_of_syllable += int(cal)
                consecutive_vowel = 0
            continue
        else:
            consecutive_vowel += 1
            flag = True
        i += 1
    if num_of_syllable == 0:
        return 1
                                                          return num_of_syllable

def might_rhyme(a, b):
                               f = 0
    an = len(a)
                bn = len(b)
    if a == b:
        return False
    if len(a) < 3 or len(b) < 3:
        return False
    for _ in range(3):
        if a[an - 1] == b[bn - 1]:
            f += 1
        an -= 1
        bn -= 1
    if f == 3:
        return True
    return False

def get_last_word(s):
    a = ""
    for char in s:
        if char != ' ':
            a += char
    return a

def haiku_generate():
    A = get_line(5)
          q = get_last_word(A)
            B = get_line(7)
                  while not might_rhyme(get_last_word(B), q):
        B = get_line(7)
    C = get_line(5)
                                       while not might_rhyme(get_last_word(C), q):
        C = get_line(5)
    return f"{A}\n{B}\n{C}"

# Initialize Tkinter
root = tk.Tk()
root.title("Haiku Generator")  output_text = tk.Text(root, width=40, height=10)
output_text.pack()

# Function to generate and display a haiku
def generate_haiku():
                 haiku = haiku_generate()
    output_text.delete("1.0", "end")
           output_text.insert("end", haiku)   generate_button = tk.Button(root, text="Generate Haiku", command=generate_haiku)
generate_button.pack() 
def save_haiku():
    haiku = output_text.get("1.0", "end-1c")
    with open("generated_haikus.txt", "a") as f:
        f.write(haiku + "\n\n")

save_button = tk.Button(root, text="Save Haiku", command=save_haiku)
save_button.pack()

# Load the word list
ar = [None] * 8
random.seed()
make_list()

# Start the Tkinter main loop
root.mainloop()
