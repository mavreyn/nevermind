import json

with open("data.json") as f:
    data = json.load(f)

print(data["games"][0]["moves"][0]["possibility"])

>INPUTFOODCODE:
MENU <BACON>;V;'CRISPY';
(CIN>>EGGS)OVEREASY // N++(TOAST);
/>>LIQ,(O_J)N:(NOPULP<)

