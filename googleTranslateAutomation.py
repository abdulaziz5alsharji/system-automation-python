import sys

try:
    import os
    import pyperclip
    from selenium import webdriver
    from time import sleep
    from platform import system
    from termcolor import colored
    from pyfiglet import figlet_format
except ModuleNotFoundError as error:
    print(colored(error, color="red"))
    input(colored("[!!]Press Any Key To Exit..", color="red"))
    sys.exit()

clear = lambda: os.system("cls") if system() == "Windows" else os.system("clear")


class GoogleTranslate:
    def __init__(self, driver) -> None:
        self.browser = driver

    def translate(self, word: str) -> str:
        self.browser.get("https://translate.google.com/?sl=en&tl=ar&op=translate")
        sleep(3)
        self.browser.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div["
                                           "2]/c-wiz[1]/span/span/div/textarea").send_keys(word)
        sleep(5)
        self.browser.find_element_by_xpath("/html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div["
                                           "2]/c-wiz[2]/div[5]/div/div[4]/div[2]/div/span/button").click()

        return pyperclip.paste()


if __name__ == '__main__':
    clear()
    print()
    print(colored(figlet_format("Google Translate"), color="blue"))
    print("\n")
    Word = input(colored("[++]Word: ", color="blue"))
    print("\n")
    browser = webdriver.Chrome()
    Bot = GoogleTranslate(browser)
    print(colored(Bot.translate(Word), color="blue"))
