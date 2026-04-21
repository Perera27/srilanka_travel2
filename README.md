# 🇱🇰 Lanka Explorer — Web-Based Travel Information System for Sri Lanka

**Student:** Bulathsinghalage Dinuk Nemitha Perera (w1998413)  
**Supervisor:** David Huang  
**Course:** BSc (Hons) Computer Science — 6COSC023W Final Year Project  
**University:** University of Westminster  
**Deadline:** 23 April 2026  

---

## 🗂️ Project Structure

```
srilanka_travel/
├── manage.py
├── requirements.txt
├── db.sqlite3                  ← auto-created on setup
├── srilanka_travel/            ← Django project config
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/                       ← Homepage, about, safety pages
├── accounts/                   ← Registration, login, user profiles
├── destinations/               ← All destination data, favourites
│   └── management/commands/
│       └── seed_data.py        ← Pre-loads real Sri Lankan destinations
├── recommendations/            ← Personalised recommendation engine
├── reviews/                    ← Star ratings and written reviews
├── templates/
│   ├── base/base.html          ← Master layout
│   ├── core/                   ← home, about, safety
│   ├── accounts/               ← register, login, profile, setup
│   ├── destinations/           ← list, detail, favourites, hidden gems
│   ├── recommendations/        ← personalised, popular
│   └── reviews/                ← submit review
└── static/
    ├── css/main.css            ← Full design system
    └── js/main.js              ← Interactive features
```

---

## ⚡ Quick Setup (5 minutes)

### 1. Clone / unzip and navigate into the project
```bash
cd srilanka_travel
```

### 2. Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run database migrations
```bash
python manage.py migrate
```

### 5. Seed the database with real Sri Lankan destinations
```bash
python manage.py seed_data
```
This creates:
- 9 provinces of Sri Lanka
- 9 destination categories (Beach, Wildlife, Cultural, Religious, etc.)
- 16 real destinations (Mirissa, Yala, Sigiriya, Temple of Tooth, Galle Fort, etc.)
- Superuser: **admin** / **admin1234**

### 6. Collect static files (optional for development)
```bash
python manage.py collectstatic
```

### 7. Start the server
```bash
python manage.py runserver
```

Visit: **http://127.0.0.1:8000**  
Admin panel: **http://127.0.0.1:8000/admin** → admin / Nemitha123

Manager panel **http://127.0.0.1:8000/manager/)** → manager1 / Dinuk123

---

## 🌐 Pages & URLs

| URL | Description |
|-----|-------------|
| `/` | Homepage with featured destinations and hero |
| `/destinations/` | Browse & filter all destinations |
| `/destinations/<slug>/` | Destination detail with map & reviews |
| `/destinations/hidden-gems/` | Hidden gem destinations |
| `/destinations/favourites/` | User's saved destinations |
| `/recommendations/` | Personalised recommendations (login required) |
| `/recommendations/popular/` | Trending destinations |
| `/accounts/register/` | Create account |
| `/accounts/login/` | Login |
| `/accounts/profile/` | Edit profile & preferences |
| `/accounts/setup/` | Initial profile setup after registration |
| `/reviews/<slug>/submit/` | Write a review |
| `/admin/` | Django admin panel |

---

## ✨ Features Implemented

### For Users
- ✅ **Register & Login** — Full auth with profile setup wizard
- ✅ **Browse Destinations** — Filter by category, province, budget, difficulty, search
- ✅ **Personalised Recommendations** — Engine scores destinations by interests, budget, location
- ✅ **Destination Detail Pages** — Photos, map (Leaflet), info, reviews, related destinations
- ✅ **Dress Code Guidance** — Shown on religious/cultural sites
- ✅ **Safety Information** — Per-destination safety notes + dedicated safety page
- ✅ **Hidden Gems** — Dedicated section for off-the-beaten-path destinations
- ✅ **Save Favourites** — AJAX toggle, stored per user
- ✅ **Write Reviews** — Star rating + written review, one per destination
- ✅ **Travel History** — View & manage your profile and reviews

### For Admins
- ✅ **Django Admin Panel** — Full CRUD on all models
- ✅ **Destination Management** — Add/edit destinations, image galleries, categories
- ✅ **Review Moderation** — Approve or reject user reviews
- ✅ **User Management** — View all registered users and profiles

---

## 🛠️ Technology Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 5.0 (Python) |
| Database | SQLite (via Django ORM) |
| Frontend | HTML5, CSS3, JavaScript (ES6+) |
| CSS Framework | Bootstrap 5.3 |
| Maps | Leaflet.js + OpenStreetMap (free, no API key) |
| Icons | Bootstrap Icons |
| Fonts | Google Fonts (Playfair Display + DM Sans) |
| Project Mgmt | Trello |
| Version Control | GitHub |

---

## 📋 Adding Real Images

Destination images can be added via the Django admin:
1. Go to `/admin/destinations/destination/`
2. Click any destination → upload a Featured Image
3. Add gallery images via the inline "Destination Images" section

---

## 🔮 Future Enhancements (Post-Deadline)

- AI chatbot for travel Q&A
- Real-time hotel/flight booking integration
- Google Maps API (swap Leaflet)
- Email notifications for new reviews
- Social login (Google/Facebook)
- Multi-language support (Sinhala, Tamil)

---

## 📄 References

- SLTDA (2023). Tourist Arrivals to Sri Lanka — Year in Review 2023.
- TripAdvisor. (2025). https://www.tripadvisor.com
- Google Travel. (2025). https://www.google.com/travel
- Yamu.lk. (2025). https://yamu.lk
- Django Documentation. https://docs.djangoproject.com
- Bootstrap Documentation. https://getbootstrap.com
- Leaflet.js Documentation. https://leafletjs.com


## Submission rescue notes

- Initial migration files are now included in the project so a fresh clone/unzip can usually start with `python manage.py migrate`.
- If you change models again before submission, run `python manage.py makemigrations` and then `python manage.py migrate`.
- The `toggle_favourite` endpoint now expects POST requests only.
