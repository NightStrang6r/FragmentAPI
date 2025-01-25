import requests
import base64

url = "https://fragmentapi.nightstranger.space/buyStars"
headers = {
    "Content-Type": "application/json"
}

username = "@example_user"  # Replace with the Telegram username
amount = 100  # Replace with the number of stars to purchase
fragment_cookies = base64.b64encode(b"your_fragment_cookies").decode("utf-8")  # Replace with Fragment cookies (Copy from Cookie Editor extension as "Header String")
seed = base64.b64encode(b"your_seed").decode("utf-8")  # Replace with TON seed

# Request payload
data = {
    "username": username,
    "amount": amount,
    "fragment_cookies": fragment_cookies,
    "seed": seed
}

try:
    # Sending POST request
    response = requests.post(url, headers=headers, json=data)

    # Handling success responses
    if response.status_code == 200:
        result = response.json()
        if result.get("success"):
            print("\n🎉 Purchase completed successfully!")
            print(f"👤 Username: {username}")
            print(f"✨ Stars purchased: {amount}")
        else:
            print("\n⚠️ Purchase failed.")
            print(f"❌ Reason: {result.get('message', 'Unknown error')}")

    # Handling other responses
    elif response.status_code == 400:
        print("\n⚠️ Bad Request.")
        print(f"Message: {response.json().get('message', 'Invalid request data')}")
    elif response.status_code == 422:
        print("\n⚠️ Validation Error.")
        print(f"Message: {response.json().get('message', 'Validation failed')}")
    elif response.status_code == 500:
        print("\n💥 Server Error.")
        print(f"Message: {response.json().get('message', 'Internal server error')}")
    else:
        print("\n❓ Unexpected status code:", response.status_code)
        print("Response:", response.json())

# Handling request exceptions
except requests.RequestException as e:
    print("\n🚨 Request failed:", str(e))