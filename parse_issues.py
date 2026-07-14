import json
d=json.load(open("C:/one/paperclip-company/issues.json"))
print("total issues:", len(d))
from collections import Counter
print(Counter(i["status"] for i in d))
print("="*60)
# focus PRE-5..8 and any children
byid={i["id"]:i for i in d}
def ident(i): return i.get("identifier")
targets=[i for i in d if ident(i) in ("PRE-5","PRE-6","PRE-7","PRE-8")]
for i in sorted(d,key=lambda x:(ident(x) or "")):
    idn=ident(i)
    print(idn, "|", i["status"], "|assignee:",i.get("assigneeId"),"|parent:",i.get("parentId"),"|",i.get("title","")[:60])
