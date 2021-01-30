def Decode(binary_from_user: str) -> str:
    text = ""
    for index in range(0, len(binary_from_user), 8):
        text += chr(int(binary_from_user[index:index + 8], 2))
    return text


def Encode(text: str):
    binary_text = ""
    temp = 1
    for index in range(len(text)):
        length_of_binary = len(str(bin(ord(text[index])))[2:])
        if length_of_binary < 8:
            temp = 8 - length_of_binary
        binary_text += temp * "0" + str(bin(ord(text[index])))[2:]
    return binary_text


binary_string_from_user = "01011001011011110111010100100000011011010111010101110011011101000010000001110011011001010110111001100100001000000110000101101110011100110111011101100101011100100111001100100000011101000110111100100000011001010111100001100101011100100110001101101001011100110110010101110011001000000011010000100000011010000110111101110101011100100111001100100000011000100110010101100110011011110111001001100101001000000111010001101000011001010010000001101100011001010111001101110011011011110110111000101110"

print(Encode("You must send answers to exercises 4 hours before the lesson."))
print(Decode(binary_string_from_user))