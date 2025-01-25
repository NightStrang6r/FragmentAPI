<h1 align="center">
    ⚡️ Fragment API ⚡️
</h1>

<h4 align="center">
    🧩 API for Fragment (<a href="https://fragment.com">fragment.com</a>): purchase of Telegram Stars and Premium 🧩
</h4>

<p align="center">
	<img src="https://i.ibb.co/YNxYtn7/2025-01-25-213756244.png" alt="Fragment API"/>
</p>

<p align="center">
    <img src="https://i.ibb.co/9bG0D5Q/2025-01-25-214508436-1.png" alt="Fragment API"/>
</p>

<p align="center">
    <img src="https://i.ibb.co/hWwfFy0/2025-01-25-214704759.png" alt="Fragment API"/>
</p>


## 💫 **Documentation & Endpoints**

- **Online documentation is available here: https://fragmentapi.nightstranger.space**

## ☑️ **Examples**

### Purchase Telegram Stars

```python
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
```

## ▶️ **Quickstart & Fees**

- **Fees depend on your daily turnover and needs. To get started, contact the developer: https://t.me/NightStrang6r**

## 🎉 **Like it? Star it!**

Please rate this repository by giving it a star rating in the top right corner of the GitHub page (you must be logged in to your account). Thank you ❤️

![](https://i.ibb.co/x3hFFvf/2022-08-18-132617815.png)