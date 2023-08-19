import time
import requests
site = input("The link of the site you want to refresh\n :")
print ("Press ctrl + c to exit")
def refresh_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        print("Page actualisée avec succès.")
    except requests.exceptions.RequestException as e:
        print("Erreur lors de l'actualisation de la page:", e)

if __name__ == "__main__":
    url_to_refresh = site
    while True:
        refresh_page(url_to_refresh)
        time.sleep(120) 
