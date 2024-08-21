import requests
import dotenv, os, json

dotenv.load_dotenv()
username = os.getenv("USERNAME")
token = os.getenv("TOKEN")

login = requests.get('https://api.github.com/search/repositories?q=github+api', auth=(username,token))

repositories = requests.get('https://api.github.com/users/grosheth/repos', auth=(username,token))

for repo in json.loads(repositories.text):
    language = requests.get(f"https://api.github.com/repos/grosheth/{repo['name']}/languages", auth=(username,token))
    print(json.loads(language.text))

    # build a dictionnary with values and sum values
    # Then build graph
