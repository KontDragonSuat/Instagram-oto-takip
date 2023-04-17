# -*- coding: utf-8 -*-

import colorama
import pyautogui
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from colorama import Fore
from os import system

colorama.init(autoreset=True)

system('cls||clear')
print("\n")
print(Fore.YELLOW + "BILGILENDIRME! Instagram, bot olarak algılamasın diye işlemler yavaş yapılmaktadır!")
sleep(5)
basla = input("(Başlamak için Enter tuşuna basın)")
account = input(Fore.CYAN + "Instagram kullanıcı adınız\n: @")
password = input(Fore.CYAN + "Şifrenizi gitriniz\n: $")
kimin = input(Fore.GREEN + "Kimin takipçilerini takip etmek istiyorsunuz\n: @")
basladi = print(Fore.GREEN + "İşlem başlatılıyor...")
sleep(3)

def instagiris():

    def wait():
        driver.implicitly_wait(20)

    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://instagram.com")
    driver.implicitly_wait(60)
    driver.delete_all_cookies()
    driver.find_element(By.CSS_SELECTOR, "button[class='_a9-- _a9_1']").click()
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='loginForm']/div[1]/div[1]/div/label/input").send_keys(account)
    sleep(1)
    driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(password)
    sleep(1)
    driver.find_element(By.CSS_SELECTOR, "button[class='_acan _acap _acas _aj1-']").click()
    driver.implicitly_wait(10)
    try:
        hata = driver.find_element(By.ID, "slfErrorAlert")
        if hata.is_enabled():
            print(Fore.RED + "Giriş Yapılamadı!")
            exit()
    except:
        driver.get(f"https://instagram.com/{kimin}/following")
        wait()
        pyautogui.moveTo(866, 630, duration=3)
        pyautogui.mouseDown(button="left", duration=30)
        sleep(31)
        kisiler = driver.find_elements(By.CSS_SELECTOR, "div[class='x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1']")
        new_kisiler = []

        for i in kisiler:
            new_kisiler.append(i.text.replace("\nDoğrulanmış",""))


        for i in new_kisiler:
            driver.get(f"https://instagram.com/{i}")
            wait()
            try:
                driver.find_element(By.CSS_SELECTOR, "button[class='_acan _acap _acas _aj1-']").click()
                print(Fore.GREEN + f"{i} takip edildi!")
                sleep(10)
            except:
                print(Fore.CYAN + f"{i} zaten takip ediliyor!")
                sleep(10)
                continue


try:
    instagiris()
    print(Fore.GREEN + "İşlem tamamlandı!")
except:
    print(Fore.RED + "Bir hata ile karşılaşıldı! Program sonlandırılıyor...")