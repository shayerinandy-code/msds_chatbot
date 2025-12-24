import requests

FASTAPI_URL = "http://localhost:8000/api/v1/query"
PRODUCT = "ESPL-30-Seconds-Nzl-En-090625-1"  # Example product

print("SDS Query System Ready. Type exit to quit.\n")

while True:
    question = input("Enter your SDS question: ")

    if question.lower().strip() in ["exit", "quit"]:
        break

    payload = {
        "query": question,
        "product": PRODUCT
    }

    try:
        response = requests.post(FASTAPI_URL, json=payload)
        if response.status_code != 200:
            print("❌ Error:", response.text)
            continue

        data = response.json()
        print("\nAnswer:\n")
        print(f"Query: {data.get('query')}")
        print(f"Answer: {data.get('answer')}")
        print(f"Confidence: {data.get('confidence')}")
        print(f"Recommended Action: {data.get('recommended_action')}")
        print("\n---\n")

    except Exception as e:
        print("❌ Exception:", e)
