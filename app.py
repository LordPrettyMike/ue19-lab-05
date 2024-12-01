import requests

kanyurl = "https://api.kanye.rest"
geekurl = "https://programming-quotesapi.vercel.app/api/random"

try:
    # Fetch data from APIs
    get_url = requests.get(kanyurl)
    get_geeked = requests.get(geekurl)

    # Parse JSON responses
    reponse_api = get_url.json()
    geek_res = get_geeked.json()

    # Print the quotes
    print(f"La citation du jour est : \n{reponse_api.get('quote')}\n - Kanye West")
    print(f"La citation geek du jour est :\n{geek_res.get('quote')}\n - {geek_res.get('author')}")

# Handle errors
except requests.exceptions.RequestException as e:
    print("Une erreur est survenue lors de la connexion :")
    print(e)
