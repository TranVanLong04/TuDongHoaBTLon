import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

value_bien_so_xe = '14A60778'
captcha_path = r"D:\TDHQT\BaiTap\BaiTapLon\captcha.png"

def tra_cuu_vi_pham():
    driver = webdriver.Chrome()
    driver.get("https://www.csgt.vn/tra-cuu-phuong-tien-vi-pham.html")
    xpath_loai_xe = '//*[@id="formBSX"]/div[2]/div[2]/select/option[1]'
    xpath_bien_so = '//*[@id="formBSX"]/div[2]/div[1]/input'
    xpath_captcha_input = '//*[@id="formBSX"]/div[2]/div[3]/div/input'
    xpath_btn = '//*[@id="formBSX"]/div[2]/input[1]'
    xpath_captcha_resuilt = '//*[@id="formBSX"]/div[2]/div[4]'
    xpath_ket_qua = '//*[@id="bodyPrint123"]'

    driver.find_element(By.XPATH, xpath_loai_xe).click()
    element_input = driver.find_element(By.XPATH, xpath_bien_so)
    element_input.clear()
    element_input.send_keys(value_bien_so_xe)

    n = 0
    while n < 10:
        n += 1
        print(f"Thử captcha lần ", n)
        captcha_element = driver.find_element(By.ID, "imgCaptcha")
        captcha_element.screenshot(captcha_path)
        img = cv2.imread(captcha_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        boxes = pytesseract.image_to_string(img).strip().replace(" ", "").replace("\n", "")
        print("Mã captcha:", boxes)
        element_captcha = driver.find_element(By.XPATH, xpath_captcha_input)
        element_captcha.clear()
        element_captcha.send_keys(boxes)
        driver.find_element(By.XPATH, xpath_btn).click()
        time.sleep(3)
        list_captcha_resuilt = driver.find_elements(By.XPATH, xpath_captcha_resuilt)
        if list_captcha_resuilt and "Mã captcha sai!" in list_captcha_resuilt[0].text:
            print("Captcha sai. Thử lại...")
            driver.refresh()
            time.sleep(2)
            driver.find_element(By.XPATH, xpath_loai_xe).click()
            element_input = driver.find_element(By.XPATH, xpath_bien_so)
            element_input.clear()
            element_input.send_keys(value_bien_so_xe)
            continue

        ket_qua_elements = driver.find_elements(By.XPATH, xpath_ket_qua)
        if ket_qua_elements:
            text_ket_qua = ket_qua_elements[0].text.strip()
            if "Không tìm thấy kết quả !" in text_ket_qua:
                print("Không có vi phạm.")
            else:
                print("Có vi phạm.")
            break
        else:
            print("Không tìm thấy phần tử kết quả. Kết thúc.")
            break

    else:
        print("Đã thử 10 lần nhưng captcha vẫn sai. Kết thúc.")

    driver.quit()

def main_loop():
    while True:
        now = datetime.now()
        print(f"Thời gian hiện tại: {now.strftime('%H:%M:%S')}")
        if now.hour == 6 or now.hour == 20 and now.minute == 55 and now.second == 00:
            print("Đến giờ tra cứu")
            tra_cuu_vi_pham()
            print("Tra cứu hoàn tất.\n")
        time.sleep(1)

if __name__ == "__main__":
    main_loop()
