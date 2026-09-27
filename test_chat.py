import requests

url = "http://localhost:5001/chat"

print("Linux AI Agent chat is ready! (Type 'quit' to exit)\n")

while True:
    prompt = input("Your question: ")
    if prompt.lower() == 'quit':
        break

    try:
        response = requests.post(url, json={"prompt": prompt})
        res_json = response.json()

        # Prints the exact response from Flask with the Linux AI Agent label
        print("\nLinux AI Agent:", res_json.get("agent_response", res_json), "\n")
    except Exception as e:
        print("Error:", response.text)
