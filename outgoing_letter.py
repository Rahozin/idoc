from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep
import random
import json

USERNAME = 'vrsp04'
PASSWORD = 'Пу556834'

def get_source_html(url):
    driver = webdriver.Chrome(
        executable_path='chromedriver/chromedriver.exe')
    driver.maximize_window()

    try:
        driver.get(url=url)
        sleep(1)

        username_box = driver.find_element(By.XPATH, "/html/body/div/div[1]/form[1]/div[1]/input[1]")
        username_box.send_keys(USERNAME)
        sleep(1)
        password_box = driver.find_element(By.XPATH, "/html/body/div/div[1]/form[1]/div[1]/input[2]")
        password_box.send_keys(PASSWORD)
        sleep(1)
        password_box.submit()
        sleep(5)
        print("[INFO] Logged in successfully!")

        button1 = driver.find_element(By.CLASS_NAME, "create-buttons")
        button1.click()
        sleep(5)
        button2 = driver.find_element(By.ID, 'ui-select-choices-row-11-1')
        button2.click()
        sleep(1)


        button3 = driver.find_element(By.CLASS_NAME, 's4Iyt')
        button3.click()
        sleep(random.randrange(2, 5))
        driver.get(url='https://www.instagram.com/makar2108/')

        sleep(3)
        with open("source-page-inst.html", "w", encoding='UTF-8') as source_page_file:
            source_page_file.write(driver.page_source)

        # ОШИБКА нужен текст, а не файл
        soup = BeautifulSoup(source_page_file, "html.parser")
        items_divs = soup.find_all("div", class_="v1Nh3 kIKUG _bz0w")

        urls = []
        for item in items_divs:
            item_url = item.find("a").get("href")
            urls.append(item_url)

        with open("posts_urls.txt", "w", encoding='UTF-8') as posts_urls_file:
            for url in urls:
                posts_urls_file.write(f"{'https://www.instagram.com'}{url}\n")

        print("[INFO] Posts urls collected successfully!")

    except Exception as _ex:
        print(_ex)
    finally:
        input("continue?")
        print('[INFO] Done')
        # driver.close()
        driver.quit()


# def get_data(file_path):
#     with open(file_path, encoding='UTF-8') as file:
#         urls_list = [url.strip() for url in file.readlines()]

#     driver = webdriver.Chrome(
#         executable_path='chromedriver/chromedriver.exe')
#     driver.maximize_window()

#     driver.get(url='https://www.instagram.com/')
#     time.sleep(3)

#     username_box = driver.find_element(By.NAME, 'username')
#     username_box.send_keys(USERNAME)
#     time.sleep(random.randrange(2, 5))
#     password_box = driver.find_element(By.NAME, 'password')
#     password_box.send_keys(PASSWORD)
#     time.sleep(random.randrange(2, 5))
#     password_box.submit()
#     time.sleep(random.randrange(2, 5))
#     button1 = driver.find_element(By.CLASS_NAME, 's4Iyt')
#     button1.click()
#     time.sleep(random.randrange(2, 5))
#     button2 = driver.find_element(By.CLASS_NAME, 'HoLwm')
#     button2.click()
#     time.sleep(random.randrange(2, 5))
#     button3 = driver.find_element(By.CLASS_NAME, 's4Iyt')
#     button3.click()
#     time.sleep(random.randrange(2, 5))

#     try:
#         driver.get(url=urls_list[0])
#         time.sleep(3)

#         page_sourse = driver.page_source

#         soup = BeautifulSoup(page_sourse, "html.parser")

#         try:
#             likes_number = soup.find(
#                 'div', class_='_7UhW9 xLCgt qyrsm KV-D4 fDxYl T0kll')
#             likes_number = likes_number.find('span').text.strip()
#         except Exception as _ex:
#             likes_number = None

#         time.sleep(random.randrange(2, 5))
#         print(likes_number)

#     except Exception as _ex:
#         print(_ex)
#     finally:
#         driver.close()
#         driver.quit()

#     return "[INFO] Data collected successfully!"


# # def get_data(file_path):
#     with open(file_path, encoding='UTF-8') as file:
#         urls_list = [url.strip() for url in file.readlines()]

#     result_list = []
#     urls_count = len(urls_list)
#     count = 1
#     for url in urls_list:
#         response = requests.get(url=url, headers=headers)
#         soup = BeautifulSoup(response.text, "html.parser")

#         try:
#             likes_number = soup.find(
#                 text='Позначки «Подобається»: ').find('span').text.strip()
#         except Exception as _ex:
#             likes_number = None

#         # item_phones_list = []
#         # try:
#         #     item_phones = soup.find(
#         #         "div", class_="service-phones-list").find_all("a", class_="js-phone-number")

#         #     for phone in item_phones:
#         #         item_phone = phone.get("href").split(":")[-1].strip()
#         #         item_phones_list.append(item_phone)
#         # except Exception as _ex:
#         #     item_phones_list = None

#         # try:
#         #     item_address = soup.find("address", class_="iblock").text.strip()
#         # except Exception as _ex:
#         #     item_address = None

#         # try:
#         #     item_site = soup.find(text=re.compile(
#         #         "Сайт|Официальный сайт")).find_next().text.strip()
#         # except Exception as _ex:
#         #     item_site = None

#         # social_networks_list = []
#         # try:
#         #     item_social_networks = soup.find(text=re.compile(
#         #         "Страница в соцсетях")).find_next().find_all("a")
#         #     for sn in item_social_networks:
#         #         sn_url = sn.get("href")
#         #         sn_url = unquote(sn_url.split("?to=")[1].split("&")[0])
#         #         social_networks_list.append(sn_url)
#         # except Exception as _ex:
#         #     social_networks_list = None

#         result_list.append(
#             {
#                 "post_url": url,
#                 "likes_number": likes_number
#                 # "item_phones_list": item_phones_list,
#                 # "item_address": item_address,
#                 # "item_site": item_site,
#                 # "social_networks_list": social_networks_list
#             }
#         )

#         time.sleep(random.randrange(2, 5))

#         if count % 10 == 0:
#             time.sleep(random.randrange(5, 9))

#         print(f"[+] Processed: {count}/{urls_count}")

#         count += 1

#     with open("lesson12/result.json", "w") as file:
#         json.dump(result_list, file, indent=4, ensure_ascii=False)

#     return "[INFO] Data collected successfully!"


def main():
    get_source_html(url="https://idoc.poe.pl.ua/login")
    # print(get_items_urls(file_path="source-page-inst.html"))
    # print(get_data(file_path="posts_urls.txt"))


if __name__ == "__main__":
    main()