import pyautogui, pyperclip, time
from PIL import Image
import pytesseract

prev = ""
while True:
    # pyautogui.moveTo(170, 30)
    pyautogui.screenshot('screen.png', region=(60, 450, 180, 100))
    # pyautogui.click('screen.png')
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open("screen.png"), lang="kor")
    text = text.replace(" ", "").replace("\n", "")
    if text != prev:
        print(text)
        pyautogui.click(x=20, y=550)
        if "?" in text : pyperclip.copy("무엇이 궁금하신가요?")
        else : pyperclip.copy("")
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press('enter')

    with open("scan.txt", "w", encoding="utf8") as f:
        f.write(text)

    prev = text
    time.sleep(3)