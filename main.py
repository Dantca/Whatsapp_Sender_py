from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Isi menggunakan object seperti pada contoh initerserah kalian 
nama = input("Nama kontak: ")
pesan = input ("pesan:  ")
nomer = input ('Nomernya (gunakan kode negara):')
penerima = [
    {
        "Nama": nama,
        "Pesan": pesan,
        "Nomer": nomer 
    }
    ] 

try:
    # Initialize the Chrome driver using ChromeDriverManager
    chrome_driver_path = ChromeDriverManager().install()
    driver = webdriver.Firefox()
    driver.get('https://web.whatsapp.com')
    input("bila sudah masuk atau berada di chat bisa Enter yah dik!!")

    for penerimas in penerima:
        try:
            url = f'https://web.whatsapp.com/send?phone={penerimas["Nomer"]}&text={penerimas["Pesan"]}'
            sent = False

            # kamu bisa ganti waktu untuk pengiriman 
            for i in range(3):
                try:
                    driver.get(url)
                    break
                except:
                    if i == 2:
                        print(f"Gagal mengirim pesan coba lagi :  {penerima['Nomer']}")
                    else:
                        continue

            try:
                click_btn = WebDriverWait(driver, 35).until(
                    EC.presence_of_element_located((By.CLASS_NAME, '_3XKXx')))
                click_btn.click()
            except Exception as e:
                print(f"Maaf pesan Yang anda kirimkan kepada {penerima['Nama']} nomer ini  {penerima['Nomer']} Gagal: {e}")
            else:
                time.sleep(2)
                sent = True
                time.sleep(5)
                print(f'Pesan telah terkirim kepada :  {penerima["Nama"]} > {penerima["Nama"]} ')
        except Exception as e:
            print(f' Gagal mengiriman pesan kepada :  {penerima["Nomer"]}: {e}')

except Exception as e:
    print(f"Kesalahan dikit gak ngaruh: {e}")

finally:
    if 'driver' in locals():
        driver.quit()
        print("Script berhasil di jalankan!! ~ Dantca")
