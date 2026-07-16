import json, re, collections

d = json.load(open('/c/one/paperclip-company/_issues_fetch.json'))
hermes = "9eed5712-96c2-4f3c-9fea-1cef0e6b7f2f"

by_id = {i['id']: i for i in d}
children = collections.defaultdict(list)
for i in d:
    p = i.get('parentId')
    if p:
        children[p].append(i['identifier'])

def refs(ident):
    pat = re.compile(r'\b' + re.escape(ident) + r'\b')
    return [i['identifier'] for i in d if i['identifier'] != ident and pat.search(i.get('title','') or '')]

print("=== DONE issues: follow-up children / referenced follow-ups ===")
done_no_followup = []
for i in d:
    if i.get('status') == 'done':
        ident = i['identifier']
        kids = children.get(i['id'], [])
        refd = refs(ident)
        flag = "" if (kids or refd) else "  <-- NO FOLLOW-UP"
        if not (kids or refd):
            done_no_followup.append(ident)
        print(f"{ident:9} kids={kids} refs={refd}{flag}")

print("\n=== DONE with NO follow-up:", done_no_followup)

print("\n=== Rule 3: status in (todo,backlog) and no assignee ===")
rule3 = [i['identifier'] for i in d if i.get('status') in ('todo','backlog') and not i.get('assigneeAgentId') and not i.get('assigneeUserId')]
print("matches:", rule3)
print("distinct statuses:", sorted(set(i.get('status') for i in d)))

print("\n=== Unassigned OPEN issues (blocked/in_progress/in_review, no agent/user) ===")
un = [i['identifier'] for i in d if i.get('status') in ('blocked','in_progress','in_review') and not i.get('assigneeAgentId') and not i.get('assigneeUserId')]
print("count:", len(un), un)

print("\n=== Hermes-owned by status ===")
he = collections.Counter(i.get('status') for i in d if i.get('assigneeAgentId')==hermes)
print(dict(he))
print("Hermes issues:", [i['identifier'] for i in d if i.get('assigneeAgentId')==hermes])

print("\n=== Issues referencing PRE-5/6/7/8 (the 4 named) ===")
for t in ['PRE-5','PRE-6','PRE-7','PRE-8']:
    print(t, "->", refs(t))
