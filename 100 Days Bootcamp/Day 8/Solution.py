class CaesarCipher:
    def __init__(self):
        self.alphabetList = [
            "a",
            "b",
            "c",
            "d",
            "e",
            "f",
            "g",
            "h",
            "i",
            "j",
            "k",
            "l",
            "m",
            "n",
            "o",
            "p",
            "q",
            "r",
            "s",
            "t",
            "u",
            "v",
            "w",
            "x",
            "y",
            "z",
        ]
        self.logo = r'''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88
'''
        print(self.logo)
        while True:
            match self.getUserChoice():
                case "encode":
                    self.encode()
                case "decode":
                    self.decode()
                case _:
                    print("Invalid choice. Please choose 'encode' or 'decode'.")
            conti = input(
                "Type 'yes' if you want to go again. Otherwise type 'no': "
            ).lower()
            if conti == "no":
                print("Goodbye")
                break
            else:
                continue

    def getUserChoice(self):
        return (
            input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
            .lower()
            .strip()
        )

    def encode(self):
        inputText = input("Type your message:\n").lower()
        try:
            shift = int(input("Type the shift number:\n"))
        except ValueError:
            print("Shift number must be an integer.")
            return
        if shift > len(self.alphabetList):
            shift -= 26

        encodedText = ""
        for char in inputText:
            if char in self.alphabetList:
                newIndex = (self.alphabetList.index(char) + shift) % len(
                    self.alphabetList
                )
                encodedText += self.alphabetList[newIndex]
            else:
                encodedText += char

        print(f"Encoded text: {encodedText}")

    def decode(self):
        inputText = input("Type your message:\n").lower()
        try:
            shift = int(input("Type the shift number:\n"))
        except ValueError:
            print("Shift number must be an integer.")
            return

        if shift > len(self.alphabetList):
            shift -= 26

        decodedText = ""
        for char in inputText:
            if char in self.alphabetList:
                newIndex = (self.alphabetList.index(char) - shift) % len(
                    self.alphabetList
                )
                decodedText += self.alphabetList[newIndex]
            else:
                decodedText += char

        print(f"Decoded text: {decodedText}")


if __name__ == "__main__":
    CaesarCipher()
