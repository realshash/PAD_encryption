import random as rnd


def encrypt(text):
    result = ""
    for i in text:
        choice = rnd.randint(1, 3)
        with open(f"noise{choice}.txt", "r") as f:
            noise = f.read() * 5
            f.seek(0)
            result += str(choice) + str(len(noise) - ord(i)) + noise[ord(i)]

    return result


def decrypt(encrypted_text):
    result = ""
    text_copy = str(encrypted_text)
    i = 0
    while i < len(text_copy):

        if text_copy[i].isnumeric() != True:
            smallstring = text_copy[:i+1]
            text_copy = text_copy[i + 1:]
            #choosing partition
            partition = smallstring[0]
            smallstring = smallstring[1:]
            #choosing alphabet
            reverse = smallstring[::-1]
            alphabet = reverse[0]
            smallstring = smallstring[:-1]
            #choosing difference
            difference = int(smallstring)
            #resetting loop variable
            i = 0
            #to acquire letter
            with open(f"noise{partition}.txt",'r') as f:
                indices = []
                contents = f.read()
                f.seek(0)
                while contents.find(alphabet) != -1:
                    index = contents.find(alphabet)
                    indices.append(index)
                    contents = contents[:index] + " " +contents[index+1:]
                #to filter correct index using difference
                for l in indices:
                    contant = f.read()
                    f.seek(0)
                    if l == len(contant) * 5 - difference:
                        final_index = l
                        
                noise = f.read()
                f.seek(0)
                final_letter = chr(final_index)
                result += final_letter
                



        else:
            i += 1

    return result

#To Run when this code is running            
if __name__ == "__main__":
    while True:
        print("-"*69)
        print("What Operation To Execute:")
        print("(1)--> Encrypt")
        print("(2)--> Decrypt")
        print("(3)--> Quit")
        print("-"*69)
        try:
            choice = input(">>")
            if choice == '1':
                sentence = input("Enter Text to be Encrypted:>> ")
                print("-" * 69)
                print("Encrypted Text:>>",encrypt(sentence))
                print("-" * 69)

            elif choice == '2':
                sentence = input("Enter Encrypted Text:>> ")
                print("-" * 69)
                print("Decrypted Text:>>",decrypt(sentence))
                print("-" * 69)

            elif choice == '3':
                break

            else:
                print("Not a Suitable Option!")
                print("-" * 69)


        except IndexError as e:
            print("Unproper Encrypted Text!")
            print("-" * 69)





