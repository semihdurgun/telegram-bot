import twint,time,os,json
while True:

    # Configure
    c = twint.Config()
    c.Search = "exosama"
    c.Limit = 60
    c.Format = 'ID {username} | Tweet {tweet}'
    c.Store_json = True
    c.Output = "exosama_tweet.json"
    # Run
    twint.run.Search(c)

    c = twint.Config()
    c.Username =  "moonsamanft"
    c.Limit = 10
    c.Format = 'ID {username} | Tweet {tweet}'
    c.Store_json = True
    c.Output = "moonsama_site_tweet.json"
    # Run
    twint.run.Search(c)

    # Configure
    """c = twint.Config()
    c.Username = "exosamanft"
    c.Limit = 10
    c.Format = 'ID {username} | Tweet {tweet}'
    c.Store_json = True
    c.Output = "exosama_site_tweet.json"
    # Run
    twint.run.Search(c)"""

    c = twint.Config()
    c.Username =  "tiggerscrypto"
    c.Limit = 10
    c.Format = 'ID {username} | Tweet {tweet}'
    c.Store_json = True
    c.Output = "tiggah_tweet.json"
    # Run
    twint.run.Search(c)

    c = twint.Config()
    c.Username =  "DonnieBigBags"
    c.Limit = 10
    c.Format = 'ID {username} | Tweet {tweet}'
    c.Store_json = True
    c.Output = "donnie_tweet.json"
    # Run
    twint.run.Search(c)

    with open("exosama_tweet.json",'r', encoding="utf8") as f:
        firstline = f.read()
    ses = "["+firstline.replace("false",'"False"').replace("\n",",")[:-1]+"]"
    d = json.loads(ses)
    replied_message=""
    output_dict = [song for song in d if "exosama" in song['tweet'].lower() ]
    for song in output_dict[:20]:
            replied_message += "<i>"+song["date"]+" "+song["time"]+"</i> <b>@"+song["username"]+"</b>: "+song["tweet"]+"\n"

    with open("exosama_tweet.txt",'w', encoding="utf8") as f:
        f.write(replied_message)
    
    # exosama site tweet
    with open("exosama_site_tweet.json",'r', encoding="utf8") as f:
        firstline = f.read()
    ses = "["+firstline.replace("false",'"False"').replace("\n",",")[:-1]+"]"
    d = json.loads(ses)

    replied_message=""
    for song in d:
            replied_message += "<i>"+song["date"]+" "+song["time"]+"</i> <b>@"+song["username"]+"</b>: "+song["tweet"]+"\n"


    with open("exosama_site_tweet.txt",'w', encoding="utf8") as f:
        f.write(replied_message)


    # moonsama site tweet
    with open("moonsama_site_tweet.json",'r', encoding="utf8") as f:
        firstline = f.read()
    ses = "["+firstline.replace("false",'"False"').replace("\n",",")[:-1]+"]"
    d = json.loads(ses)

    replied_message=""
    for song in d:
            replied_message += "<i>"+song["date"]+" "+song["time"]+"</i> <b>@"+song["username"]+"</b>: "+song["tweet"]+"\n"


    with open("moonsama_site_tweet.txt",'w', encoding="utf8") as f:
        f.write(replied_message)

    # tiggah
    with open("tiggah_tweet.json",'r', encoding="utf8") as f:
        firstline = f.read()
    ses = "["+firstline.replace("false",'"False"').replace("\n",",")[:-1]+"]"
    d = json.loads(ses)

    replied_message=""
    for song in d:
            replied_message += "<i>"+song["date"]+" "+song["time"]+"</i> <b>@"+song["username"]+"</b>: "+song["tweet"]+"\n"


    with open("tiggah_tweet.txt",'w', encoding="utf8") as f:
        f.write(replied_message)


    with open("exosama_site_tweet.txt",'w', encoding="utf8") as f:
        f.write(replied_message)

    # donnie
    with open("donnie_tweet.json",'r', encoding="utf8") as f:
        firstline = f.read()
    ses = "["+firstline.replace("false",'"False"').replace("\n",",")[:-1]+"]"
    d = json.loads(ses)

    replied_message=""
    for song in d:
            replied_message += "<i>"+song["date"]+" "+song["time"]+"</i> <b>@"+song["username"]+"</b>: "+song["tweet"]+"\n"


    with open("donnie_tweet.txt",'w', encoding="utf8") as f:
        f.write(replied_message)

    time.sleep(300)
    os.remove('exosama_tweet.json')
    #os.remove('exosama_site_tweet.json')
    os.remove('tiggah_tweet.json')
    os.remove('donnie_tweet.json')
    os.remove('moonsama_site_tweet.json')
    