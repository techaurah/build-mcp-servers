"""Lesson 27: merging two catalogues, collision included."""
LEADDESK = ["capture_lead", "score_lead", "list_leads"]
NOTES = ["capture_note", "search", "list_notes"]
OTHER_SEARCH = ["search", "fetch"]

def collisions(*catalogues):
    seen, clash = set(), set()
    for cat in catalogues:
        for name in cat:
            if name in seen:
                clash.add(name)
            seen.add(name)
    return sorted(clash)

def namespace(server, names):
    return [f"{server}__{n}" for n in names]

if __name__ == "__main__":
    print("collision across notes + other:", collisions(NOTES, OTHER_SEARCH))
    print("leaddesk stays clean:", collisions(LEADDESK, NOTES, OTHER_SEARCH))
    print("namespaced merge sample:", namespace("notes", NOTES)[:2], "+ leaddesk tools unprefixed in their own server")
    print("Rule: names are unique per server; hosts namespace; distinctive names travel best.")
