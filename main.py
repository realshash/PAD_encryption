import random as rnd

text = input("Enter the string you want to Encrypt: ")
intensity = int(input("Enter the intensity of encryption: "))


def encrypt(text, intensity=1):
    result = ""
    for i in text:
        choice = rnd.randint(1, 3)
        with open(f"noise{choice}.txt", "r") as f:
            noise = f.read() * intensity
            result += str(choice) + noise[ord(i)]

    return result

print(encrypt(text, intensity))
