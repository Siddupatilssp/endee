def search_answer(query):
    with open("data.txt", "r") as f:
        faqs = f.readlines()

    results = []

    for faq in faqs:
        if query.lower() in faq.lower():
            results.append(faq.strip())

    if not results:
        return ["Sorry, I couldn't find an exact answer. Please contact support."]

    return results[:2]