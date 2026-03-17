from endee import Endee

db = Endee("support_db")

faqs = [
    "Refund is available within 7 days",
    "You can reset password using forgot password option",
    "We provide AI and software services",
    "Contact us at support@company.com"
]

# save data locally
with open("data.txt", "w") as f:
    for faq in faqs:
        f.write(faq + "\n")

print("Data saved successfully!")