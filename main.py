import requests
import dotenv, os, json


LANGS = {"Python": 0,"Nix": 0,"HTML": 0, "Go": 0, "Lua": 0, "JavaScript": 0, "Shell": 0, "Dockerfile": 0}

def get_credentials():
    dotenv.load_dotenv()
    username = os.getenv("USERNAME")
    token = os.getenv("TOKEN")
    return username, token

def total():
    total = 0
    for lang in LANGS:
        total += LANGS[lang] 
    return total

def get_langs():

    username, token = get_credentials()
    repositories = requests.get('https://api.github.com/users/grosheth/repos', auth=(username,token))

    for repo in json.loads(repositories.text):
        language = requests.get(f"https://api.github.com/repos/grosheth/{repo['name']}/languages", auth=(username,token))
        values = json.loads(language.text)
        for lang in LANGS:
            if lang in json.loads(language.text):
                LANGS[lang] += values[lang]

    total = total()
    print(total)


get_langs()



    
    # build a dictionnary with values and sum values
    # Then build graph





# Make a graph of percentage per repo
