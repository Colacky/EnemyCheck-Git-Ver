import requests
from bs4 import BeautifulSoup
from auth import get_token
import json
import re

access_token = get_token()

cyrillic_translit = {'\u0410': 'A', '\u0430': 'a',
'\u0411': 'B', '\u0431': 'b',
'\u0412': 'V', '\u0432': 'v',
'\u0413': 'G', '\u0433': 'g',
'\u0414': 'D', '\u0434': 'd',
'\u0415': 'E', '\u0435': 'e',
'\u0416': 'Zh', '\u0436': 'zh',
'\u0417': 'Z', '\u0437': 'z',
'\u0418': 'I', '\u0438': 'i',
'\u0419': 'I', '\u0439': 'i',
'\u041a': 'K', '\u043a': 'k',
'\u041b': 'L', '\u043b': 'l',
'\u041c': 'M', '\u043c': 'm',
'\u041d': 'N', '\u043d': 'n',
'\u041e': 'O', '\u043e': 'o',
'\u041f': 'P', '\u043f': 'p',
'\u0420': 'R', '\u0440': 'r',
'\u0421': 'S', '\u0441': 's',
'\u0422': 'T', '\u0442': 't',
'\u0423': 'U', '\u0443': 'u',
'\u0424': 'F', '\u0444': 'f',
'\u0425': 'Kh', '\u0445': 'kh',
'\u0426': 'Ts', '\u0446': 'ts',
'\u0427': 'Ch', '\u0447': 'ch',
'\u0428': 'Sh', '\u0448': 'sh',
'\u0429': 'Shch', '\u0449': 'shch',
'\u042a': '"', '\u044a': '"',
'\u042b': 'Y', '\u044b': 'y',
'\u042c': "'", '\u044c': "'",
'\u042d': 'E', '\u044d': 'e',
'\u042e': 'Iu', '\u044e': 'iu',
'\u042f': 'Ia', '\u044f': 'ia'}


name_entries = []
vers_entries = []


def get_data(name, realm):

    URL = f'https://eu.api.blizzard.com/profile/wow/character/{realm}/{name}/statistics?namespace=profile-eu&locale=en_GB&access_token={access_token}'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    char_stats = json.loads(str(soup))
    vers = round(char_stats['versatility_damage_done_bonus'])
    output = f"{name}-{realm} has {char_stats['health']} health and {vers}% versatility."
    print(output)
    return vers


def clear_vers_entries():
    for vers_entry in vers_entries:
        vers_entry.delete(0, 'end')


def translate_cyrillic(realmname, translit_table):
    converted_realm = ''
    for char in realmname:
        transchar = ''
        if char in cyrillic_translit:
            transchar = cyrillic_translit[char]
        else:
            transchar = char
        converted_realm += transchar
    print(converted_realm)
    return converted_realm


def format_realm(realmname):

    realmname = translate_cyrillic(realmname, cyrillic_translit)

    if len(re.findall(r'[A-Z]', realmname)) > 1:
        realm_split = re.sub(r"([A-Z])", r" \1", realmname).split()
        realm = str(realm_split[0].lower()+'-'+realm_split[1].lower())
        print(realm)
        return realm
    else:
        return realmname.lower()


def fill_data():
    clear_vers_entries()
    for (name_entry, vers_entry) in zip(name_entries, vers_entries):  # Iterate over input entries
        namerealm = name_entry.get().split('-', 1)  # Split the input into name and realm
        realm = namerealm[1]
        print(realm)
        versatility = get_data(namerealm[0].lower(), format_realm(realm))
        vers_entry.insert(0, versatility)









