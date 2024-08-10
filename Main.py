import json
import time
import random
import ctypes
import threading
import httpx
import datetime
from colored import fg
from pystyle import Write, System, Colors, Colorate

reset = fg(7)
red = fg(1)
green = fg(2)
purple = fg(5)
pink = fg(216)
views_sent = 0

def get_time_rn():
    return datetime.datetime.now().strftime("%H:%M:%S")

def view_booster():
    thread_name = threading.currentThread().getName()
    with open("config.json") as f:
        github_link = json.load(f).get('github_link')
    
    global views_sent
    while True:
        ctypes.windll.kernel32.SetConsoleTitleW(f'Github Profile View Booster By Ghost Sellz | Views Sent : {views_sent}')
        try:
            response = httpx.get(github_link, timeout=20)
            if response.status_code == 200:
                views_sent += 1
                print(f"{reset}{get_time_rn()} {pink}| {reset}[ {pink}{thread_name}{reset} ] Success {purple}>{green} Sent View {reset}[{pink} Total : {views_sent} {reset}]")
            else:
                print(f"{reset}{get_time_rn()} {pink}| {reset}[ {pink}{thread_name}{reset} ] Error {purple}>{red} Bad Gateway 502")
        except (httpx.RequestError, httpx.TimeoutException):
            print(f"{reset}{get_time_rn()} {pink}| {reset}[ {pink}{thread_name}{reset} ] Error {purple}>{red} Request failed")

def run():
    while True:
        view_booster()

if __name__ == "__main__":
    with open("config.json") as f:
        num_threads = json.load(f).get('threads', 250)
    
    threads = [threading.Thread(target=run, name=f"VIEW_BOOSTER-{i+1}") for i in range(int(num_threads))]
    
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
