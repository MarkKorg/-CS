import requests
import math

link = "https://drand.cloudflare.com/public/latest"
hex_text = ""
for i in range(1, 21):
    print(f"Please wait {i}/20")
    a = requests.get(link)
    data = a.json()
    # print("round: ",data["round"])
    round = data["round"] - 1
    # print(hex)
    hex = data["randomness"]
    # print(hex_text)
    hex_text += hex
    # print(link)
    link = "https://drand.cloudflare.com/public/" + str(round)
"""
print(hex)
print(hex_text)
"""


def getProbability(hex_text, length, char):
    sum = 0
    for i in hex_text:
        if i == char:
            sum += 1
    prob = sum / length
    # print(prob)
    return prob


def getEntropy(hex_chars, hex_text):
    entropy = 0
    length = len(hex_text)
    for char in hex_chars:
        prob = getProbability(hex_text, length, char)
        entropy -= (prob * math.log(prob, 2))
    return entropy


hex_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
entropy = getEntropy(hex_chars, hex_text)
print(f"For this:\n {hex_text}")
print(f"Entropy is:\n {entropy}")
