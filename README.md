# 💅🏻 ParlorPal – Your AI Marketing Buddy for Small Businesses

ParlorPal is an **AI-powered web app** designed to help **beauty parlour owners** and **local service businesses** create attractive, personalized marketing content — instantly and effortlessly.

✨ Built with love for the **Epsilon Hackathon 2025** by **Team HustlePioneers**, ParlorPal empowers small business owners who may not have the time, design experience, or marketing expertise to grow their business online.

---

## 🌟 Features

### 🚀 Core User Flows
- **Sign Up & Profile Creation:** Register and set up your business profile (name, logo, description, contact info, etc.).
- **Personalized Dashboard:** Get AI-driven suggestions and quick access to all tools.
- **AI Content Generation:**
  - **Captions:** Generate catchy, emoji-rich marketing captions in English or Kannada (Cohere API).
  - **Posters:** Instantly create visually appealing, brand-themed posters (VertexAI + PIL + Cloudinary).
  - **Videos:** Generate short marketing videos for campaigns (Google Vertex AI Veo).
  - **Email Subject Lines:** Get AI-generated subject lines for your campaigns (Google Gemini API).
- **AI Chatbot:** Get instant help, marketing tips, and navigation guidance from a context-aware AI assistant (Gemini).
- **Analytics & History:** Track your content generation, view insights, and revisit past creations.
- **Feedback & Support:** Submit feedback and get support directly from the app.
- **Email Verification & Festival Notifications:** Secure your account and get timely marketing reminders for festivals.

### 🛠️ Advanced/Admin Features
- **Admin Feedback Panel:** View and manage user feedback.
- **Festival Management:** Manage festival notifications and email templates.

---

## 🧠 Tech Stack & Integrations

| Layer         | Technology Used           |
|---------------|--------------------------|
| Backend       | Django (Python)           |
| Frontend      | Django Templates, Bootstrap 5, Custom CSS/JS |
| AI Text Gen   | Cohere API                |
| AI Chatbot    | Google Gemini API         |
| Image Gen     | VertexAI (Image), PIL, htmlcsstoimage |
| Video Gen     | Google Vertex AI (Veo)    |
| Cloud Storage | Cloudinary                |
| Database      | SQLite (dev), Firebase (optional prod) |
| Hosting       | Railway                   |
| Env Mgmt      | python-dotenv             |

**Key Integrations:**
- **Cohere:** For social media caption generation.
- **Google Gemini:** For chatbot and email subject line generation.
- **VertexAI:** For poster and video generation.
- **Cloudinary:** For image/logo/poster storage and optimization.

---

## 🖥️ Project Structure

```
parlorpal/
├── core/
│   ├── templates/           # HTML templates (UI, emails, etc.)
│   ├── static/              # CSS, JS, images
│   ├── views.py             # Main business logic & user flows
│   ├── models.py            # Database models (User, Profile, History, Feedback, etc.)
│   ├── forms.py             # Django forms
│   ├── cloudinary_utils.py  # Cloudinary integration
│   ├── email_utils.py       # Email sending & templates
│   └── ...
├── parlorpal/               # Django settings & config
├── media/                   # Uploaded files (dev)
├── static/                  # Static assets (prod)
├── manage.py                # Django entrypoint
├── requirements.txt         # Python dependencies
└── ...
```

---

## ⚡ Quick Start (Local Development)

1. **Clone the repo:**
   ```bash
   git clone <your-repo-url>
   cd parlorpal
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   - Create a `.env` file in the root directory with the following keys:
     - `COHERE_API_KEY` (Cohere text gen)
     - `CLOUDINARY_CLOUD_NAME`, `CLOUDINARY_API_KEY`, `CLOUDINARY_API_SECRET` (Cloudinary)
     - `DJANGO_SECRET_KEY` (Django secret)
     - `GEMINI_API_KEY` (Google Gemini)
     - `GCP_PROJECT_ID` (Google Cloud project for VertexAI)
     - `GOOGLE_VERTEX_API_KEY` (VertexAI video gen)
4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Start the server:**
   ```bash
   python manage.py runserver
   ```
6. **Access the app:**
   - Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 🔑 Environment Variables

| Variable                  | Purpose                        |
|---------------------------|--------------------------------|
| COHERE_API_KEY            | Cohere text generation         |
| CLOUDINARY_CLOUD_NAME     | Cloudinary image storage       |
| CLOUDINARY_API_KEY        | Cloudinary image storage       |
| CLOUDINARY_API_SECRET     | Cloudinary image storage       |
| DJANGO_SECRET_KEY         | Django security                |
| GEMINI_API_KEY            | Google Gemini API (chatbot, email) |
| GCP_PROJECT_ID            | Google Cloud project (VertexAI) |
| GOOGLE_VERTEX_API_KEY     | VertexAI video generation      |

> **Note:** These are **private** and not included in the repository.

---

## 📸 Screenshots & Demo

- **Live Demo:** [https://web-production-209f.up.railway.app/](https://web-production-209f.up.railway.app/)  
  *Best viewed on mobile devices*
- **Demo Video:** [Watch Live Demo Video](https://drive.google.com/drive/folders/1oNkoA-bDattusrEVzLRwbasv8VjUAB0u?usp=sharing)
- *(Add screenshots here if available)*

---

## 🤖 AI/ML Model Usage
- **Cohere:** Used for generating creative, emoji-rich captions in multiple languages.
- **Google Gemini:** Powers the chatbot and email subject line generator, providing context-aware, conversational responses.
- **VertexAI (Image & Video):** Generates posters and marketing videos using business info and campaign details.
- **PIL:** For image processing and poster composition.

**Limitations:**
- AI outputs may vary in quality; always review before publishing.
- Some features (e.g., video generation) may require valid Google Cloud credentials and may incur costs.

---

## 📝 Contributing

This project was built for the Epsilon Hackathon 2025 and is **not open for public contributions** at this time.

If you have suggestions or want to collaborate, please contact **Team HustlePioneers**.

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
