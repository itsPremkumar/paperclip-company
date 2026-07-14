import json
d=json.load(open("C:/one/paperclip-company/issues.json"))
print("total", len(d))
from collections import Counter
print(Counter(i["status"] for i in d))
for i in d:
    print(i.get("identifier"), i["status"], "| parent:", i.get("parentId"), "| assigneeId:", i.get("assigneeId"), "|", i["title"][:70])
