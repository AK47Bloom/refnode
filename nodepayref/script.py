import os
import sys
import random
import string
import time
import requests

# Coba untuk mengimpor requests, jika gagal, install requests
try:
    import requests
except ImportError:
    os.system('pip install requests')

# Fungsi untuk mencetak garis pemisah
def linex():
    print('\033[0m================================================')

# Logo untuk script
logo = f"""
\x1b[38;5;46m     ▗▖  ▗▖ ▗▄▖ ▗▄▄▄  ▗▄▄▄▖▗▄▄▖  ▗▄▖▗▖  ▗▖
\x1b[38;5;47m     ▐▛▚▖▐▌▐▌ ▐▌▐▌  █ ▐▌   ▐▌ ▐▌▐▌ ▐▌▝▚▞▘
\x1b[38;5;48m     ▐▌ ▝▜▌▐▌ ▐▌▐▌  █ ▐▛▀▀▘▐▛▀▘ ▐▛▀▜▌ ▐▌
\x1b[38;5;49m     ▐▌  ▐▌▝▚▄▞▘▐▙▄▄▀ ▐▙▄▄▖▐▌   ▐▌ ▐▌ ▐▌\x1b[38;5;46m V/0.1
\033[0m================================================
 \033[1;35m        Developer : Zain Arain
         YouTube   : @ZainArain279
         tele chnl   : @AirdropScript6
         Tele grop  : @AirdropScript7
\033[0m================================================"""

# Membaca daftar proxy dari file
proxy_list = open('proxy.txt', 'r').read().splitlines()

# Fungsi untuk mendapatkan token Captcha
def get_token():
    while True:
        res = requests.get(f'http://localhost:5000/get').text
        if not 'None' in res:
            print(f'\r\r\033[0m>>\033[1;32m Captcha token get successful \033[0m')
            return res
        else:
            time.sleep(0.5)

# Fungsi untuk membersihkan layar terminal dan mencetak logo
def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')
    print(logo)

# Fungsi untuk mendapatkan header dengan token otorisasi
def get_headers(auth_token=None):
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://app.nodepay.ai',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'
    }
    if auth_token:
        headers['Authorization'] = f'Bearer {auth_token}'
        headers['origin'] = 'chrome-extension://lgmpfmgeabnnlemejacfljbmonaomfmm'
    return headers

# Fungsi untuk mendaftar akun
def reg_account(email, password, username, ref_code, proxy_url=None, captcha_token=None):
    try:
        if proxy_url:
            print(f'\r\r\033[0m>>\033[1;32m Proxy : {proxy_url} \033[0m')
            proxy_url = {'http': proxy_url, 'https': proxy_url}
        register_data = {
            'email': email,
            'password': password,
            'username': username,
            'referral_code': ref_code,
            'recaptcha_token': captcha_token
        }
        headers = get_headers()
        url = "https://api.nodepay.ai/api/auth/register"
        response = requests.post(url, headers=headers, json=register_data, proxies=proxy_url, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m')
        linex
        time.sleep(1)

# Fungsi untuk login akun dan mendapatkan token otorisasi
def login_account(email, password, captcha_token, proxy_url):
    try:
        json_data = {
            'user': email,
            'password': password,
            'remember_me': True,
            'recaptcha_token': captcha_token
        }
        proxy_url = {'http': proxy_url, 'https': proxy_url}
        headers = get_headers()
        url = "https://api.nodepay.ai/api/auth/login"
        response = requests.post(url, headers=headers, json=json_data, proxies=proxy_url, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m')
        linex()
        time.sleep(1)

# Fungsi untuk mengaktifkan akun
def activate_recent_account(auth_token, proxy_url):
    try:
        json_data = {}
        url = "https://api.nodepay.ai/api/auth/active-account"
        headers = get_headers(auth_token)
        proxy_url = {'http': proxy_url, 'https': proxy_url}
        response = requests.post(url, headers=headers, json=json_data, proxies=proxy_url, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m')
        linex()
        time.sleep(1)

# Fungsi utama untuk menjalankan semua aksi
def main():
    clear_screen()
    try:
        ref_limit = int(input('\033[0m>>\033[1;32m Put Your Reff Amount: '))
    except:
        print('\033[1;32m⚠️ Input Wrong Default Reff Amount is 1k ')
        ref_limit = 1000
        time.sleep(1)

    ref_code = input("\033[0m>>\033[1;32m Input referral code : ")
    clear_screen()
    success_count = 0
    account_data = []  # List untuk menyimpan data akun

    for atm in range(ref_limit):
        try:
            print(f'\r\r\033[0m>>\033[1;32m Processing {str(success_count)}/{str(ref_limit)} complete: {((atm + 1) / ref_limit) * 100:.2f}% ')
            domains = ["@gmail.com", "@outlook.com", "@yahoo.com", "@hotmail.com"]
            characters = string.ascii_letters + string.digits
            username = str(''.join(random.choice(characters) for _ in range(12))).lower()
            password = str(''.join(random.choice(string.ascii_letters) for _ in range(6)) + 'Rc3@' + ''.join(random.choice(string.digits) for _ in range(3)))
            email = f"{username}{str(random.choice(domains))}"
            proxy_url = random.choice(proxy_list)
            captcha_token = get_token()
            response_data = reg_account(email, password, username, ref_code, proxy_url, captcha_token)

            if response_data['msg'] == 'Success':
                print(f'\r\r\033[0m>>\033[1;32m Account Create Successful \033[0m')
                captcha_token = get_token()
                response_data = login_account(email, password, captcha_token, proxy_url)

                if response_data['msg'] == 'Success':
                    print(f'\r\r\033[0m>>\033[1;32m Account Login Successfully \033[0m')
                    auth_token = response_data['data']['token']

                    # Simpan data akun ke dalam list
                    account_data.append({
                        'email': email,
                        'username': username,
                        'password': password,
                        'np_token': auth_token  # np_token diambil dari auth_token
                    })

                    response_data = activate_recent_account(auth_token, proxy_url)

                    if response_data['msg'] == 'Success':
                        print(f'\r\r\033[0m>>\033[1;32m Successfully Referral Done \033[0m')
                        success_count += 1
                        # Simpan data ke file
                        with open('accounts.txt', 'a') as f:
                            f.write(f"{email}|{username}|{password}|{auth_token}\n")
                        time.sleep(1)
                    else:
                        print(f'\r\r\033[1;31m🌲 Referral Error, Not Success \033[0m {response_data["msg"]}')
                        time.sleep(1)
                        linex()
                else:
                    print(f'\r\r\033[1\033[1;31m🌲 Account Login Failed \033[0m {response_data["msg"]}')
                    time.sleep(1)
                    linex()
            else:
                print(f'\r\r\033[1;31m🌲 Account Create Failed \033[0m {response_data["msg"]}')
                time.sleep(1)
                linex()
            linex()
        except Exception as e:
            print(f'\r\r\033[31m⚠️ Error: {str(e)} \033[0m')
            linex()
            time.sleep(1)

    # Setelah loop selesai, simpan semua data akun ke file
    with open('accounts.txt', 'a') as f:
        for account in account_data:
            f.write(f"{account['email']}|{account['username']}|{account['password']}|{account['np_token']}\n")

    print('\r\r\033[0m>>\033[1;32m Your Referral Completed \033[0m')
    exit()

# Menjalankan fungsi utama
main()