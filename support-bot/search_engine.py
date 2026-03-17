from endee import Endee

db = Endee("support_db")

def search_answer(query):
    with open("data.txt", "r") as f:
        faqs = f.readlines()

    results = []

    for faq in faqs:
        if query.lower() in faq.lower():
            results.append(faq.strip())

    if not results:
        return ["No exact match found, try another query"]

    return results[:2]