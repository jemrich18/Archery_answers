# Archery Answers

**Bowhunting Ballistics & Arrow Building Platform**

Archery Answers is a web application built for bowhunters who are tired of bouncing between spine charts, forum posts, and YouTube videos trying to piece together basic answers about their setup. It provides real-world arrow speed estimates, kinetic energy and momentum calculations, animal harvest thresholds, and a community-driven arrow builder — all in one place.

---

## Features

### Arrow Speed Calculator
Estimates real-world arrow speed based on your bow's IBO rating, draw length, draw weight, and total arrow weight. Uses industry-standard deduction formulas:
- 10 FPS lost per inch of draw length under 30"
- ~17.5 FPS lost per 10 lbs of draw weight under 70 lbs
- 1.5 FPS lost per 5 grains of arrow weight over 350 grains

Speed estimates do not account for string accessories (peep sight, D-loop, dampeners, nock sets), which typically reduce speed by an additional 3-10 FPS.

### Kinetic Energy & Momentum Calculator
For archers who already know their arrow speed (e.g. from a chronograph), enter speed and arrow weight to get KE and momentum instantly.

- **KE** = (arrow weight × velocity²) / 450,240
- **Momentum** = (arrow weight × velocity) / 225,120

### Animal Reference Chart
Minimum recommended kinetic energy and momentum values for ethical hunting:

| Animal | Min KE (ft-lbs) | Min Momentum (slug-ft/s) |
|--------|----------------|--------------------------|
| Small Game | 25 | 0.25 |
| Medium Game (Deer, Antelope) | 25-41 | 0.40 |
| Large Game (Elk, Black Bear, Boar) | 42 | 0.50 |
| Big Game (Cape Buffalo, Grizzly) | 65 | 0.65 |

Every calculator result includes pass/fail/marginal ratings against these thresholds.

### Community-Driven Component Database
Users submit arrow components (shafts, vanes, nocks, inserts, broadheads) with real specs from their own gear. Submissions are available immediately in the user's builds and reviewed by an admin for public listing. No scraping, no proprietary data — just public specs entered by the community.

Supported component types:
- **Arrow Shafts** — manufacturer, model, spine, GPI, inner/outer diameter, straightness
- **Vanes** — manufacturer, model, length, height, weight per vane
- **Nocks** — manufacturer, model, type (press-fit/pin), weight, compatible diameter
- **Inserts/Outserts** — manufacturer, model, type, weight, material, compatible diameter
- **Broadheads** — manufacturer, model, type (fixed/mechanical/hybrid), weight, cutting diameter, blade count

### Arrow Builder
Users create bow setups and build complete arrows by selecting components from the database. The system automatically calculates:
- Total arrow weight (from shaft GPI × cut length + all component weights)
- Estimated arrow speed (from bow IBO with deductions)
- Kinetic energy
- Momentum
- Pass/fail ratings for each game animal

Multiple bows and multiple builds per bow are supported.

### User Accounts
Registration, login, and logout. Users can save bow setups, create arrow builds, and submit components. All builds and submissions are tied to the user's account.

### Admin Panel
Full Django admin interface for managing users, components, builds, and animal thresholds. Component submissions can be approved or rejected directly from the list view.

---

## Tech Stack

- **Backend:** Django 6.0
- **Database:** SQLite (development), PostgreSQL (production)
- **Frontend:** Django templates, vanilla JavaScript, HTMX (for future arrow builder enhancements)
- **Styling:** Custom CSS with CSS variables, dark theme
- **Deployment:** Railway (planned)

---

## Project Structure

```
archery_answers/
├── manage.py
├── core/                   # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── calculator/             # Arrow speed, KE/momentum calculators
│   ├── models.py           # AnimalThreshold
│   ├── views.py            # Home page view
│   ├── urls.py
│   └── management/
│       └── commands/
│           └── seed_thresholds.py
├── components/             # Community component database
│   ├── models.py           # ArrowShaft, Vane, Nock, Insert, Broadhead, Manufacturer
│   ├── views.py            # Component submission views
│   ├── forms.py            # Submission forms with ManufacturerMixin
│   ├── admin.py
│   └── urls.py
├── builder/                # Arrow build tool
│   ├── models.py           # BowSetup, ArrowBuild (with calculate() method)
│   ├── views.py            # Builder views
│   ├── forms.py            # Bow and build forms
│   ├── admin.py
│   └── urls.py
├── accounts/               # User registration and auth
│   ├── models.py           # ArcherProfile
│   ├── views.py            # Register, login, logout
│   ├── forms.py            # RegisterForm
│   ├── admin.py
│   └── urls.py
├── templates/
│   ├── base.html           # Base template with tab navigation
│   ├── home.html           # Main page with all calculator tabs
│   ├── accounts/
│   │   ├── register.html
│   │   └── login.html
│   ├── builder/
│   │   ├── home.html
│   │   ├── create_bow.html
│   │   └── create_build.html
│   └── components/
│       └── submit.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── main.js
```

---

## Getting Started

### Prerequisites
- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd archery_answers

# Create virtual environment and install dependencies (using uv)
uv sync

# Or with pip
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install django psycopg2-binary django-htmx whitenoise
```

### Setup

```bash
# Run migrations
python manage.py migrate

# Seed animal threshold data
python manage.py seed_thresholds

# Create admin superuser
python manage.py createsuperuser

# Start the development server
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to use the app.

Visit `http://127.0.0.1:8000/admin/` to manage data.

---

## Roadmap

- [ ] Edit and delete existing builds and bows
- [ ] FOC (Front of Center) calculation
- [ ] Side-by-side build comparison
- [ ] String accessory weight input for more accurate speed estimates
- [ ] Deploy to Railway with PostgreSQL
- [ ] Mobile responsiveness polish
- [ ] Component search with autocomplete in the arrow builder
- [ ] User-to-user build sharing
- [ ] Spine recommendation engine based on bow setup

---

## Contributing

This project uses a community-driven component database. The best way to contribute is to create an account, submit your gear specs, and help build out the component library.

For code contributions, fork the repo and submit a pull request.

---

## License

This project is currently private. License TBD.