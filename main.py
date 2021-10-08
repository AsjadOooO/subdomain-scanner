"""    _         _           _ 
    / \   ___ (_) __ _  __| |
   / _ \ / __|| |/ _` |/ _` |
  / ___ \\__ \| | (_| | (_| |
 /_/   \_\___// |\__,_|\__,_|
            |__/             
            """

import requests


domain = input("""
   ____        _     ____                        _          ____ _               _             
 / ___| _   _| |__ |  _ \  ___  _ __ ___   __ _(_)_ __    / ___| |__   ___  ___| | _____ _ __ 
 \___ \| | | | '_ \| | | |/ _ \| '_ ` _ \ / _` | | '_ \  | |   | '_ \ / _ \/ __| |/ / _ \ '__|
  ___) | |_| | |_) | |_| | (_) | | | | | | (_| | | | | | | |___| | | |  __/ (__|   <  __/ |   
 |____/ \__,_|_.__/|____/ \___/|_| |_| |_|\__,_|_|_| |_|  \____|_| |_|\___|\___|_|\_\___|_|   
                                                                                              
Enter the following domain name you wanna check 'HTTP://': """)

# Give your file of wordlist
file = open('wordlist1000', 'r', )


content = file.read()

subdomains = content.splitlines()


for subdomain in subdomains:
    url = f'http://{subdomain}.{domain}'
   
    try:
        requests.get(url)
  
    except requests.ConnectionError:
        pass
   
    else:

        print("Sub Domain that has been discovered: ", url)
      
        file = open(domain + '.txt', "a", encoding="utf8")
        file.write(url + '\n')

"""    _         _           _ 
    / \   ___ (_) __ _  __| |
   / _ \ / __|| |/ _` |/ _` |
  / ___ \\__ \| | (_| | (_| |
 /_/   \_\___// |\__,_|\__,_|
            |__/             
            """