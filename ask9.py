with open('two_cities_ascii.txt') as f:
    text = f.read()


# text = "Testing word stuff 69"

def convertToAscii(text):
    ascii = []
    for i in text:
        ascii.append(ord(i))
    return ascii


def convertToBinary(ascii):
    bin_list = []
    for i in ascii:
        bin_list.append(bin(i)[2:])
    return bin_list


def max_0_sequence(bin_cont):
    sum = 0
    max = 0
    flag = False
    for i in bin_cont:
        if i == "0":
            flag = True
            sum += 1
        if flag and i == "1":
            flag = False
            if sum > max:
                max = sum
            sum = 0
    return max


def ma_1_sequence(bin_cont):
    sum = 0
    max = -69
    flag = False
    for i in bin_cont:
        if i == "1":
            flag = True
            sum += 1
        if flag and i == "0":
            flag = False
            if sum > max:
                max = sum
            sum = 0
    return max


ascii = convertToAscii(text)
# ex: "Papei" -> [80, 97, 112, 101, 105]
bin_list = convertToBinary(ascii)
# ex: [80, 97, 112, 101, 105] -> ['1010000', '1100001', '1110000', '1100101', '1101001']

bin_cont = ""  # bin_continuous
for i in bin_list:
    bin_cont += i
# ex: ['1010000', '1100001', '1110000', '1100101', '1101001'] -> 10100001100001111000011001011101001

max0 = max_0_sequence(bin_cont)
max1 = ma_1_sequence(bin_cont)

print("\n")
# print(f"Original text: {text}\n")
# print(f"each character in ASCII number: {ascii}\n")
print(f"each character in binary: {bin_list}\n")
# print(f"merged binary list: {bin_cont}\n")
print(f"Longest sequence of continuous 0s: {max0}\n")
print(f"Longest sequence of continuous 1s: {max1}\n")
