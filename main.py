import requests
import dotenv, os, json
from jinja2 import Template
import codecs
import matplotlib.pyplot as plt

# Cherry picking languages instead of getting 0.001% for Dockerfile...
LANGS = {"Python": [0, 0],"Nix": [0, 0],"HTML": [0, 0], "Go": [0, 0], "Lua": [0, 0], "JavaScript": [0, 0], "Shell": [0, 0]}

def get_credentials():
    dotenv.load_dotenv()
    username = os.getenv("USERNAME")
    token = os.getenv("TOKEN")
    return username, token

def get_langs():
    username, token = get_credentials()
    repositories = requests.get('https://api.github.com/users/grosheth/repos', auth=(username,token))

    for repo in json.loads(repositories.text):
        language = requests.get(f"https://api.github.com/repos/grosheth/{repo['name']}/languages", auth=(username,token))
        values = json.loads(language.text)
        for lang in LANGS:
            if lang in json.loads(language.text):
                LANGS[lang][0] += values[lang]

    # Obtaining percentages
    total = 0
    for lang in LANGS:
        total += LANGS[lang][0] 
    for lang in LANGS:
        LANGS[lang][1] = 100 * float(LANGS[lang][0]) / float(total)

def generate_graph():
    labels = []
    percentages = []
    for lang in LANGS:
        labels.append(lang)
        percentages.append(LANGS[lang][1])

    fig, ax = plt.subplots()
    ax.pie(percentages, labels=labels, autopct='%1.1f%%')
    plt.savefig('pie.png')

def generate_readme():

    with open('README.j2', 'r') as file:
      template = Template(file.read(),trim_blocks=True)
    rendered_file = template.render(langs=LANGS)

    print(rendered_file)
    output_file = codecs.open("README.md", "w", "utf-8")
    output_file.write(rendered_file)
    output_file.close()


get_langs()
generate_graph()
generate_readme()
