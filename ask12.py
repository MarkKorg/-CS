import requests


def convertToBinary(hex):
    scale = 16
    # print("Hex:", hex)
    binary = str(bin(int(hex, scale)).zfill(8)[2:])
    return binary


link = "https://drand.cloudflare.com/public/latest"
bin_text = ""
for i in range(0, 100):
    print(f"Please wait {i}/99")
    a = requests.get(link)
    data = a.json()
    #print(round)
    round = data["round"] - 1
    #print(hex)
    hex = data["randomness"]
    #print(convertToBinary(hex))
    #print(bin_text)
    bin_text += convertToBinary(hex)
    #print(link)
    link = "https://drand.cloudflare.com/public/" + str(round)
#print(bin_text)


def max_0_sequence(sequence):
    sum = 0
    max = 0
    flag = False
    for i in sequence:
        if i == "0":
            flag = True
            sum += 1
        if flag and i == "1":
            flag = False
            if sum > max:
                max = sum
            sum = 0
    return max


def max_1_sequence(sequence):
    sum = 0
    max = -69
    flag = False
    for i in sequence:
        if i == "1":
            flag = True
            sum += 1
        if flag and i == "0":
            flag = False
            if sum > max:
                max = sum
            sum = 0
    return max


x = max_0_sequence(bin_text)
y = max_1_sequence(bin_text)
print(f"In this huuugee binary sequence:\n{bin_text}")
print(f"The longest sequence of consecutive 0s is: {x}")
print(f"The longest sequence of consecutive 1s is: {y}")
