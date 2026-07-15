import json
d=json.load(open("C:/one/paperclip-company/issues.json"))
print("total",len(d))
from collections import Counter
c=Counter(i["status"] for i in d)
print(c)
# focus PRE-5,6,7,8
by_id={i["identifier"]:i for i in d}
for k in ["PRE-5","PRE-6","PRE-7","PRE-8"]:
    i=by_id.get(k)
    if i: print(k,i["status"],"assignee=",i["assigneeAgentId"],"|",i["title"][:60])
print("---- todo/backlog with no assignee ----")
for i in d:
    if i["status"] in ("todo","backlog") and not i["assigneeAgentId"]:
        print(i["identifier"],i["status"],"|",i["title"][:70])
print("---- in_progress ----")
for i in d:
    if i["status"]=="in_progress":
        print(i["identifier"],"assignee=",i["assigneeAgentId"],"|",i["title"][:60])
print("---- in_review ----")
for i in d:
    if i["status"]=="in_review":
        print(i["identifier"],"|",i["title"][:70])
