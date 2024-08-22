import requests
import dotenv, os, json


LANGS = {"Python": 0,"Nix": 0,"HTML": 0, "Go": 0, "Lua": 0, "JavaScript": 0, "Shell": 0, "Dockerfile": 0}

def get_credentials():
    dotenv.load_dotenv()
    username = os.getenv("USERNAME")
    token = os.getenv("TOKEN")
    return username, token

def login():
    username, token = get_credentials()
    login = requests.get('https://api.github.com/search/repositories?q=github+api', auth=(username,token))
    return login


def get_langs():

    username, token = get_credentials()
    repositories = requests.get('https://api.github.com/users/grosheth/repos', auth=(username,token))

    for repo in json.loads(repositories.text):
        language = requests.get(f"https://api.github.com/repos/grosheth/{repo['name']}/languages", auth=(username,token))
        print(json.loads(language.text))


get_langs()



    
    # build a dictionnary with values and sum values
    # Then build graph





# Make a graph of percentage per repo
