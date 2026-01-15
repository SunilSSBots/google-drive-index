<!-- =====================================================
     Google Drive Index & Token Generator
     Professional README (Markdown + Styled HTML)
====================================================== -->

<div align="center">

<h1>🚀 Google Drive Index & Token Generator</h1>

<p>
A <b>single professional repository</b> to generate <code>token.pickle</code>  
and deploy a <b>Google Drive Index</b> using <b>Cloudflare Workers</b>.
</p>

<p>
<img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge">
<img src="https://img.shields.io/badge/Google%20Drive-API-success?style=for-the-badge">
<img src="https://img.shields.io/badge/Cloudflare-Workers-orange?style=for-the-badge">
<img src="https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge">
</p>

<hr/>

</div>

## ✨ Overview

This project provides a **clean, reliable, and repeatable workflow** to:

- 🔐 Authenticate Google Drive using OAuth
- 📦 Generate `token.pickle`
- 🔓 Reuse the same token for indexing
- 🌐 Deploy a Google Drive Index with Cloudflare Workers

No panels.  
No paid services.  
Full control in your hands.

---

## 📁 Repository Structure

```
google-drive-index/
│
├── generate.py          → Creates token.pickle (OAuth login)
├── unlock_token.py      → Reads token & prints auth details
├── worker.example.js    → Cloudflare Worker Drive Index
├── credentials.json    → Google OAuth file (user provided)
└── README.md
```

---

## 🧰 Requirements

### 🖥 System
- Python **3.8 or higher**
- pip installed
- Internet connection

### ☁ Google Cloud
- Google Cloud account
- Drive API enabled
- OAuth Client ID (Desktop App)

### 🌩 Cloudflare
- Cloudflare account
- Workers enabled

---

## 🟢 STEP 1 — Google Cloud Setup (Very Important)

🔹 This step creates the base credentials required for everything.

### 1️⃣ Create Project
- Go to **Google Cloud Console**
- Create a **new project**

### 2️⃣ Enable Drive API
- Open **APIs & Services**
- Enable **Google Drive API**

### 3️⃣ OAuth Consent Screen
- User type: **External**
- Fill required fields
- Save & continue

### 4️⃣ Create OAuth Credentials
- Credentials → Create Credentials
- Type: **OAuth Client ID**
- Application type: **Desktop App**

⬇ Download the file and rename it to:

```
credentials.json
```

📂 Place it inside the project folder.

---

## 🟢 STEP 2 - How To Generate Token Pickle With Android Easily After Google Auth2.0 New policy update and How to create client id, client secret, refresh token for cloudflare . Without any kind of error.

1. Install Termux F-Droid
2. Open Termux and just copy paste all the commands that described below, Make sure you have internet connection. if you see Y/n then Type y.

```bash
apt update && apt upgrade -y && pkg install git -y && pkg install python -y && apt update && pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib && pip install --upgrade pip
```

2.1 ERROR: Installing pip is forbidden, this will break the python-pip package (termux)
If you get this error, you need to run the following command:

```bash
curl -sS https://bootstrap.pypa.io/get-pip.py | python
```

Now run command number 2 again. Hopefully no error will appear.


 # Clone the Repository

```bash
git clone https://github.com/SunilSSBots/google-drive-index
cd google-drive-index
```

Make sure `credentials.json` is present in this directory.

---

## 🟢 STEP 3 — Install Python Dependencies

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2
```

This installs all required Google authentication libraries.

---

## 🟢 STEP 4 — Generate token.pickle

```bash
python3 generate.py
```

### 🔐 What Happens Now?
1. A Google login URL appears in terminal
2. Open it in your browser
3. Login to your Google account
4. Allow Drive permissions
5. Authorization completes

✅ A new file will be created:

```
token.pickle
```

This file contains:
- Access token
- Refresh token
- OAuth session data

---

## 🟢 STEP 5 — Verify / Unlock Token (Optional but Recommended)

```bash
python3 unlock_token.py
```

This step helps to:
- Confirm token is valid
- Ensure refresh token exists
- Debug authentication issues

---

## 🟢 STEP 6 — Cloudflare Worker Setup

### 1️⃣ Create Worker
- Open **Cloudflare Dashboard**
- Go to **Workers & Pages**
- Create a new Worker

### 2️⃣ Add Code
- Open `worker.example.js`
- Copy all content
- Paste into Worker editor
- Save

---

## 🟢 STEP 7 — Configure Worker Secrets

Go to:
**Worker → Settings → Variables → Secrets**

Add the following:

| Name | Description |
|----|-----------|
| CLIENT_ID | Google OAuth Client ID |
| CLIENT_SECRET | Google OAuth Client Secret |
| REFRESH_TOKEN | Refresh token from OAuth |
| ROOT_ID | Drive root / folder / shared drive ID |

### 📌 ROOT_ID Examples

| Use Case | Value |
|-------|------|
| My Drive | `root` |
| Shared Drive | Shared Drive ID |
| Folder Only | Folder ID |

---

## 🟢 STEP 8 — Deploy & Test

- Click **Deploy**
- Open the Worker URL
- Your Google Drive Index should appear 🎉

---

## 🔒 Security Best Practices

⚠ Never upload these files publicly:
- `credentials.json`
- `token.pickle`

✔ Always use **Cloudflare Secrets**
✔ Revoke tokens immediately if exposed

---

## 🛠 Troubleshooting

### ❌ token.pickle not created
- credentials.json missing
- Drive API not enabled
- OAuth not completed fully

### ❌ Worker shows error / blank page
- Wrong refresh token
- Incorrect CLIENT_ID / SECRET
- Wrong ROOT_ID
- Variable names mismatch

---

## 📜 License

MIT License

---

## ⚠ Disclaimer

This project is for educational and personal use.  
You are responsible for complying with Google and Cloudflare terms.

---

<div align="center">

✨ **Built for developers who want control, clarity, and simplicity.** ✨

</div>
