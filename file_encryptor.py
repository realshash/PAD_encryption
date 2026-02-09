import main



if __name__ == "__main__":
    while True:
        print("-"*69)
        print("What Operation To Execute:")
        print("(1)--> Encrypt Text File")
        print("(2)--> Decrypt Text File")
        print("(3)--> Quit")
        print("-"*69)
        try:
            choice = input(">>")
            if choice == '1':
                sentence = input("Enter Text File Name to be Encrypted(.txt not included):>> ")
                print("-" * 69)
                try:
                    with open(f"{sentence}.txt",'r') as f:
                        contents = f.read()
                        f.seek(0)
                        contents = main.encrypt(contents)
                    
                    #writing in new file
                    with open(f"{sentence}_encrypted.txt",'w') as r:
                        r.write(contents)
                        r.seek(0)
                        print("File Encrypted!")

                except:
                    print("File Not Found!")

                print("-" * 69)

            elif choice == '2':
                sentence = input("Enter Text File Name to be Decrypted(.txt not included):>> ")
                print("-" * 69)
                try:
                    with open(f"{sentence}.txt",'r') as f:
                        contents = f.read()
                        f.seek(0)
                        contents = main.decrypt(contents)
                    
                    #writing in new file
                    with open(f"{sentence}_decrypted.txt",'w') as r:
                        r.write(contents)
                        r.seek(0)
                        print("File Decrypted!")

                except:
                    print("File Not Found! or Issue with decrypting File!")

                print("-" * 69)

            elif choice == '3':
                break

            else:
                print("Not a Suitable Option!")
                print("-" * 69)


        except IndexError as e:
            print("Error Occured!")
            print("-" * 69)