import os
import ctypes
import sys
import json

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

class SelectableOption:
    def __init__(self, title, callback):
        self.title = title
        self.callback = callback

    def call(): callback()

class OptionSelector:
    def __init__(self, title, options: list):
        self.title = title
        self.options = options

    def addOption(self, option: SelectableOption):
        self.options.append(option)

    def requestInput(self, message):
        while True:
            try:
                result = int(input(message))
            except ValueError:
                print("Please, enter a valid number.")
                continue
            else:
                break

        return result

    def displayOptions(self):
        for k, v in enumerate(self.options):
            print(f"[{k}] {v.title}")

    def displayTitle(self):
        print("="*5 + f" {self.title} " + "="*5)

    def displayMenu(self):
        self.displayTitle()
        self.displayOptions()

    def askForAnOption(self, message):
        self.displayMenu()
        userInput = self.requestInput(message)
        self.options[userInput].callback()


class SLMGR:
    def __init__(self, key):
        self.KEY = key

    def activateKey(self):
        print(f"[STEP 1/3] slmgr /ipk {self.KEY}")
        os.system(f"slmgr /ipk {self.KEY}")

        print(f"[STEP 2/3] slmgr /skms kms.digiby.ir")
        os.system(f"slmgr /skms kms.digiby.ir")

        print("[STEP 3/3] slmgr /ato")
        os.system(f"slmgr /ato")

        print("DONE!")

def load():
    jsonfile = json.load(open("versions.json"))
    options = OptionSelector("Choose something idk", [SelectableOption(i, lambda: SLMGR(jsonfile[i]).activateKey()) for i in jsonfile.keys()])
    options.askForAnOption("Choose your windows version: ")


if __name__ == "__main__":
    if is_admin():
        print("Administrator rights verified...")
        load()
    else:
        print("/!\\ You need administrator permissions to run this file!")


    # REM Activación
    # slmgr /ipk %w10pro%

    # REM Alternativa: slmgr /skms kms.msguides.com
    # slmgr /skms kms.digiboy.ir

    # REM Remover marca de agua
    # slmgr /ato