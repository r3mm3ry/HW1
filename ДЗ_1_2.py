import zipfile, json, sqlite3

with zipfile.ZipFile('egrul.json.zip', 'r') as zipobj:
    names = zipobj.namelist()
    con = sqlite3.connect("hw1.db")
    cur = con.cursor()
    for jname in names:
        with zipobj.open(jname, mode='r') as jfile:
            jlist = json.loads(jfile.read())
            for i in jlist:        
                if i['data'].get('СвОКВЭД', False) and i['data']['СвОКВЭД'].get('СвОКВЭДОсн', False) and i['data']['СвОКВЭД']['СвОКВЭДОсн']['КодОКВЭД'][:2] == '61':  
                    cur.execute("INSERT INTO telecom_companies VALUES(?, ?, ?, ?, ?)", \
                                [i['full_name'], i['inn'], i['ogrn'], i['data']['СвОКВЭД']['СвОКВЭДОсн']['КодОКВЭД'], i['data']['СвОКВЭД']['СвОКВЭДОсн']['НаимОКВЭД']])
    con.commit()
