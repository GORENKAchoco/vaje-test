#vaje test: https://chatgpt.com/share/697f8e6a-076c-8011-b28d-a6a4ad0712f2
hisa = {
    "sobe": {
        "dnevna": {"temperatura": 22, "luči": ["strop", "kotna"]},
        "spalnica": {"temperatura": 19, "okno": {"odprto": False}}
    },
    "naprave": [
        {"tip": "termostat", "baterija": 55},
        {"tip": "kamera", "status": "online", "zadnji_gib": {"ura": "03:14", "tip": "mačka"}}
    ]
}
#a) Izpiši niz: "mačka"
#print(hisa["naprave"][1]["zadnji_gib"]["tip"])
#b) Izpiši temperaturo v spalnici
#print(hisa["sobe"]["spalnica"]["temperatura"])
#c) Izpiši odstotek baterije termostata (55)
#print(hisa["naprave"][0]["baterija"])

postaja = {
    "moduli": [
        {"ime": "habitat", "posadka": 6},
        {"ime": "laboratorij", "posadka": 2, "eksperimenti": ["alge", "kristali"]}
    ],
    "sistemi": {
        "energija": {"soncne_celice": True, "napolnjenost": 78},
        "zivljenjska_podpora": {"kisik": {"status": "OK", "rezerva_ur": 48}}
    }
}
#a) Izpiši niz: "kristali"
print(postaja["moduli"][1]["eksperimenti"][1])
#b) Izpiši število članov posadke v modulu "habitat"
print(postaja["moduli"][0]["posadka"])
#c) Izpiši število ur rezerve kisika (48)
print(postaja["sistemi"]["zivljenjska_podpora"]["kisik"]["rezerva_ur"])