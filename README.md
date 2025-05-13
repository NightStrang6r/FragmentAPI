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


## 🚀 **Features**

- 💸 **Purchase Telegram Stars & Premium**

- ⚡️ Works **with** or **without** KYC

- 🔂 Bypass Fragment **purchase limits**

- 🔐 Full **end-to-end** encryption

- 🧩 No **API key** or registration required

- 💙 No TON API required

- 📈 **Multi-transaction** support

- 🔁 Simple integration

- 📈 Optimized **for automation**

- 🧠 Developer-friendly

## 🌐 **Documentation & Endpoints**

**Online documentation is available here: https://fragment-api.net**

## 📌 **Requirements**

- ✅ TON Wallet v4r2 🪙

- ✅ TON Wallet should be Active (send any transaction from it) 🪙

- ✅ Seed should be base64-encoded 🔐

## 📌 **Requirements if you use your own Fragment account**

- ✅ Fragment account with linked TON wallet and Telegram account 🔗

- ✅ KYC verification on Fragment 🆔

- ✅ Export cookies from Fragment 🍪 (as Header String using Cookie Editor extension)

- ✅ Fragment cookies should be base64-encoded 🔐

## ☑️ **Examples**

### ✨ Purchase Telegram Stars

```python
import requests
import base64

url = "https://api.fragment-api.net/buyStars"
headers = {
    "Content-Type": "application/json"
}

username = "@durov"  # Replace with the Telegram username
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

**Fees depend on your daily turnover and needs. To get more information, contact the developer: https://t.me/NightStrang6r**

## 🎉 **Like it? Star it!**

Please rate this repository by giving it a star rating in the top right corner of the GitHub page (you must be logged in to your account). Thank you ❤️

![](https://i.ibb.co/x3hFFvf/2022-08-18-132617815.png)

## 📄 **License**

© Leonid Tsaruk 2025

This repository is licensed under GNU GENERAL PUBLIC LICENSE.