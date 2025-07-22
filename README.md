# 💅🏻 ParlorPal – Your AI Marketing Buddy for Small Businesses

ParlorPal is an **AI-powered web app** designed to help **beauty parlour owners** and **local service businesses** create attractive, personalized marketing content — instantly and effortlessly.

✨ Built with love for the **Epsilon Hackathon 2025** by **Team HustlePioneers**, ParlorPal aims to empower small business owners who may not have the time, design experience, or marketing expertise to grow their business online.

---

## 🌟 Features

✔️ Generate catchy marketing text in **English or Kannada**  
✔️ Auto-create posters using your **business name, offer details, brand color, and logo**  
✔️ No design skills or templates needed — it's all automatic  
✔️ Ready-to-share content for **Instagram, WhatsApp, Facebook**, and more  
✔️ Clean, mobile-first UI designed for business owners on the go  

---

## 🧠 Tech Stack

| Layer         | Technology Used           |
|---------------|----------------------------|
| Backend       | Django                     |
| AI Text Gen   | Cohere API                 |
| Image Gen     | Python (PIL), htmlcsstoimage |
| Cloud Storage | Cloudinary                 |
| Database      | SQLite (dev), Firebase (optional prod) |
| Hosting       | Railway                     |

---

## 🚀 Live Demo

🔗 Try it here: [https://web-production-209f.up.railway.app/](https://web-production-209f.up.railway.app/)  
📱 *Best viewed on mobile devices*

🎥 [Watch Live Demo Video](https://drive.google.com/drive/folders/1oNkoA-bDattusrEVzLRwbasv8VjUAB0u?usp=sharing)

---

## 🛠️ How It Works

1. Enter your **business details** (name, logo, description)
2. Choose what you want to promote (e.g., Bridal Packages, Monsoon Discounts)
3. Select your **language, text length, and theme color**
4. ParlorPal generates:
   - A **marketing caption**
   - A **custom poster** using your brand identity
5. Copy or download instantly — share anywhere 🎯

---

## 📁 Project Structure

parlorpal/

├── core/

│ ├── templates/

│ ├── static/

│ └── views.py, models.py, etc.

├── media/uploads/

├── parlorpal/ # Django settings

├── db.sqlite3

├── manage.py

├── Procfile

└── requirements.txt


---

## 🔐 Environment Setup (Private Keys Not Included)

This project uses the following environment variables:

- `COHERE_API_KEY`
- `CLOUDINARY_CLOUD_NAME`
- `CLOUDINARY_API_KEY`
- `CLOUDINARY_API_SECRET`
- `DJANGO_SECRET_KEY`

> These are **kept private** and not included in the repository for security reasons.

---

## ⚠️ License & Code Usage

This project is submitted for evaluation during the **Epsilon Hackathon 2025**.  
All rights reserved by **Team HustlePioneers**.

🚫 **Please do not reuse, publish, or modify** the source code for personal or commercial purposes without permission.

---

## 🙌 Team HustlePioneers

- 👨‍💻 **Girish Yandigeri** – Team Lead & Full-Stack Developer  
- 🎯 Mission: *To support small businesses and empower women entrepreneurs with accessible AI tools.*

---

> Thank you for exploring ParlorPal!  
> 💖 Let's bring beautiful businesses online, one poster at a time.
