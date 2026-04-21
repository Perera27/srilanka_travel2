"""
Management command to seed the database with real Sri Lankan destinations.
Run: python manage.py seed_data
"""

from django.core.management.base import BaseCommand
from destinations.models import Destination, Category, Province


PROVINCES = [
    "Western", "Central", "Southern", "Northern", "Eastern",
    "North Western", "North Central", "Uva", "Sabaragamuwa"
]

CATEGORIES = [
    ("Beach & Coastal", "beach", "🏖️"),
    ("Wildlife & Nature", "wildlife", "🐘"),
    ("Cultural & Heritage", "cultural", "🏛️"),
    ("Religious & Spiritual", "religious", "🕌"),
    ("Adventure & Trekking", "adventure", "🥾"),
    ("Historical Sites", "historical", "🏰"),
    ("Scenic & Viewpoints", "scenic", "🌄"),
    ("Waterfalls", "waterfalls", "💧"),
    ("Food & Cuisine", "food", "🍛"),
]

DESTINATIONS = [
    # BEACHES
    {
        "name": "Mirissa Beach",
        "category": "beach", "province": "Southern",
        "short_description": "Crescent-shaped paradise beach famous for whale watching and surf.",
        "description": "Mirissa is a small beach town on the south coast of Sri Lanka, renowned for its beautiful crescent-shaped beach, vibrant nightlife, and incredible whale watching tours. Between November and April, blue and sperm whales migrate through these waters, making it one of the best whale-watching spots in the world. The beach itself is perfect for swimming and snorkelling, with calm waters during the dry season.",
        "city": "Mirissa", "latitude": 5.9478, "longitude": 80.4716,
        "budget_level": "moderate", "difficulty": "easy",
        "best_time_to_visit": "November to April",
        "opening_hours": "Open 24 hours",
        "entry_fee": "Free",
        "is_featured": True, "is_hidden_gem": False,
        "tags": "beach,whale watching,surf,sunset,swimming",
        "safety_notes": "Strong currents can occur during monsoon season (May–October). Always swim near lifeguard stations.",
    },
    {
        "name": "Unawatuna Beach",
        "category": "beach", "province": "Southern",
        "short_description": "Stunning bay with calm turquoise water, ideal for snorkelling.",
        "description": "Unawatuna is one of Sri Lanka's most beloved beaches, sitting in a sheltered bay near Galle. The crescent of golden sand is lined with coconut palms and backed by a colorful strip of guesthouses, restaurants and dive shops. The calm, clear waters make it excellent for snorkelling and diving, and the nearby Galle Fort adds a cultural dimension to any visit.",
        "city": "Unawatuna", "latitude": 6.0174, "longitude": 80.2489,
        "budget_level": "moderate", "difficulty": "easy",
        "best_time_to_visit": "December to March",
        "entry_fee": "Free", "is_featured": True,
        "tags": "beach,snorkelling,diving,galle,swimming",
    },
    {
        "name": "Arugam Bay",
        "category": "beach", "province": "Eastern",
        "short_description": "Sri Lanka's surf capital — world-class waves and a laid-back vibe.",
        "description": "Arugam Bay is internationally recognised as one of Asia's top surf destinations, boasting a world-class right-hand point break. Located on the east coast, the town has a bohemian, relaxed atmosphere popular with backpackers and surfers. Beyond surfing, the area offers stunning natural beauty, friendly elephants at nearby Lahugala National Park, and authentic local food.",
        "city": "Arugam Bay", "latitude": 6.8418, "longitude": 81.8356,
        "budget_level": "budget", "difficulty": "moderate",
        "best_time_to_visit": "April to October",
        "entry_fee": "Free", "is_featured": True,
        "tags": "surfing,beach,backpacker,wildlife,east coast",
    },
    # WILDLIFE
    {
        "name": "Yala National Park",
        "category": "wildlife", "province": "Southern",
        "short_description": "The world's highest density of leopards. See elephants, crocs and birds.",
        "description": "Yala National Park is Sri Lanka's most visited and second largest national park, spanning 979 km². It is world-famous for having the highest density of leopards of any region on Earth. Safaris also offer sightings of elephants, sloth bears, water buffalo, crocodiles, and hundreds of bird species. The park's diverse ecosystems range from dry monsoon forest to wetlands and sandy beaches.",
        "city": "Tissamaharama", "latitude": 6.3728, "longitude": 81.5210,
        "budget_level": "premium", "difficulty": "easy",
        "best_time_to_visit": "February to July",
        "opening_hours": "6:00 AM – 6:00 PM",
        "entry_fee": "USD 15 + vehicle charge",
        "is_featured": True, "is_hidden_gem": False,
        "tags": "leopards,elephants,safari,wildlife,birds,photography",
        "safety_notes": "Always stay inside your safari vehicle. Do not feed or approach wild animals.",
    },
    {
        "name": "Udawalawe National Park",
        "category": "wildlife", "province": "Uva",
        "short_description": "Guaranteed elephant sightings in herds of 100+. A true elephant paradise.",
        "description": "Udawalawe National Park is famous for its large population of Sri Lankan elephants and is arguably the best place in Asia to see elephants in the wild. Herds of 50–100 elephants roam the grasslands and reservoir shores. The park also houses buffalo, crocodiles, sambar deer, and over 180 bird species. The Elephant Transit Home within the park rehabilitates orphaned elephants.",
        "city": "Udawalawe", "latitude": 6.4726, "longitude": 80.8966,
        "budget_level": "moderate", "difficulty": "easy",
        "best_time_to_visit": "Year-round (dry season: May–September)",
        "entry_fee": "USD 15 + vehicle charge",
        "is_featured": True,
        "tags": "elephants,safari,wildlife,birds,reservoir",
    },
    # CULTURAL / RELIGIOUS
    {
        "name": "Temple of the Tooth (Sri Dalada Maligawa)",
        "category": "religious", "province": "Central",
        "short_description": "Sri Lanka's most sacred Buddhist temple, housing a tooth relic of the Buddha.",
        "description": "The Temple of the Sacred Tooth Relic is Sri Lanka's most revered Buddhist shrine and a UNESCO World Heritage Site. Located in Kandy, it houses the relic of the left canine tooth of the Buddha, brought to Sri Lanka during the 4th century. The complex includes several museums, a moat, and beautiful architecture. The annual Esala Perahera festival in July/August transforms the entire city into a spectacular procession of elephants, dancers and drummers.",
        "city": "Kandy", "latitude": 7.2936, "longitude": 80.6413,
        "budget_level": "budget", "difficulty": "easy",
        "best_time_to_visit": "Year-round; Esala Perahera in July/August",
        "opening_hours": "5:30 AM – 8:00 PM",
        "entry_fee": "LKR 1,500 (foreigners)",
        "is_featured": True, "requires_dress_code": True,
        "dress_code_description": "Shoulders and knees must be covered. Remove shoes before entering. Sarongs and shawls are available at the entrance. No shorts or sleeveless tops allowed.",
        "tags": "buddhism,kandy,temple,heritage,UNESCO,tooth relic",
        "safety_notes": "Photography is restricted inside the inner shrine. Respect worshippers during prayer times.",
    },
    {
        "name": "Sigiriya Rock Fortress",
        "category": "historical", "province": "North Central",
        "short_description": "Ancient 5th-century citadel atop a 200m volcanic rock. A UNESCO Wonder.",
        "description": "Sigiriya, or Lion Rock, is a UNESCO World Heritage Site and Sri Lanka's most iconic landmark. Built by King Kashyapa in the 5th century AD, this ancient citadel sits 200 metres atop a massive granite column. The climb takes visitors past ancient frescoes, the famous Mirror Wall with 1,200-year-old graffiti, and the iconic Lion Paws gateway. The summit reveals remarkable ruins of a royal palace with panoramic views across the Sri Lankan jungle.",
        "city": "Sigiriya", "latitude": 7.9570, "longitude": 80.7603,
        "budget_level": "premium", "difficulty": "moderate",
        "best_time_to_visit": "January to April, September to November",
        "opening_hours": "7:00 AM – 5:30 PM",
        "entry_fee": "USD 30",
        "is_featured": True,
        "tags": "UNESCO,history,climbing,frescoes,rock fortress,ancient",
        "safety_notes": "The climb involves steep metal stairs. Not suitable for people with severe vertigo or heart conditions. Carry water — no vendors on top.",
    },
    {
        "name": "Polonnaruwa Ancient City",
        "category": "historical", "province": "North Central",
        "short_description": "Remarkably preserved medieval capital with stunning stone sculptures.",
        "description": "Polonnaruwa served as the second ancient capital of Sri Lanka (10th–12th century) and is a UNESCO World Heritage Site. Unlike Anuradhapura, Polonnaruwa's ruins are extraordinarily well preserved. The site includes the magnificent Gal Vihara — four giant Buddha statues carved from a single granite face — the royal palace complex, and beautiful lotus ponds. Cycling between the ruins through jungle pathways is a popular and memorable way to explore.",
        "city": "Polonnaruwa", "latitude": 7.9395, "longitude": 81.0003,
        "budget_level": "moderate", "difficulty": "easy",
        "best_time_to_visit": "May to September",
        "opening_hours": "7:30 AM – 6:00 PM",
        "entry_fee": "USD 25",
        "is_featured": True, "requires_dress_code": True,
        "dress_code_description": "Cover shoulders and knees when visiting active temples and shrines within the complex.",
        "tags": "UNESCO,ancient,history,cycling,Buddha,medieval",
    },
    {
        "name": "Galle Fort",
        "category": "historical", "province": "Southern",
        "short_description": "Dutch colonial fort with cobblestoned streets, boutiques and ocean views.",
        "description": "Galle Fort is a UNESCO World Heritage Site located on Sri Lanka's southwest coast. Built originally by the Portuguese in 1588 and later fortified by the Dutch in the 17th century, the fort is a unique blend of European and South Asian architecture. Inside the fort walls are 400-year-old streets, a lighthouse, colonial mansions converted into boutique hotels and cafés, craft shops, and churches. The ramparts offer spectacular sunset views over the Indian Ocean.",
        "city": "Galle", "latitude": 6.0269, "longitude": 80.2169,
        "budget_level": "free", "difficulty": "easy",
        "best_time_to_visit": "December to April",
        "entry_fee": "Free to walk; museum has entry fee",
        "is_featured": True,
        "tags": "UNESCO,dutch colonial,history,architecture,shopping,sunset",
    },
    # SCENIC / NATURE
    {
        "name": "Nine Arch Bridge (Demodara)",
        "category": "scenic", "province": "Uva",
        "short_description": "Sri Lanka's most photographed railway bridge, set in emerald tea hills.",
        "description": "The Nine Arch Bridge, also known as the Bridge in the Sky, is Sri Lanka's most iconic architectural landmark in the hill country. Built entirely of stone, brick and cement — no steel was used — during the British colonial era (1921), it spans across a deep valley covered in lush tea plantations near Ella. Watching the blue train cross the bridge while framed by green hills is one of the most memorable sights in Sri Lanka.",
        "city": "Ella", "latitude": 6.8750, "longitude": 81.0593,
        "budget_level": "free", "difficulty": "moderate",
        "best_time_to_visit": "Year-round; avoid heavy monsoon",
        "opening_hours": "Viewable any time; train schedule varies",
        "entry_fee": "Free",
        "is_featured": True, "is_hidden_gem": False,
        "tags": "railway,bridge,ella,tea,photography,colonial",
        "safety_notes": "Do not stand on the bridge tracks when trains are approaching. Check train schedules before visiting.",
    },
    {
        "name": "Adam's Peak (Sri Pada)",
        "category": "adventure", "province": "Sabaragamuwa",
        "short_description": "Sacred mountain pilgrimage with a spectacular sunrise from the summit.",
        "description": "Adam's Peak, known as Sri Pada in Sinhalese, is a 2,243-metre conical mountain in central Sri Lanka famous for the sacred footprint shrine at its summit. The mountain is revered by Buddhists, Hindus, Muslims and Christians alike. Pilgrims and trekkers climb the illuminated 5,500-step staircase through the night to witness one of the most breathtaking sunrises in Asia. The pilgrimage season runs from December to May.",
        "city": "Hatton", "latitude": 6.8096, "longitude": 80.4994,
        "budget_level": "free", "difficulty": "challenging",
        "best_time_to_visit": "December to May (pilgrimage season)",
        "opening_hours": "Night climb recommended (depart midnight–2AM)",
        "entry_fee": "Free",
        "is_featured": True, "requires_dress_code": True,
        "dress_code_description": "Modest clothing required as this is a sacred pilgrimage site. Cover shoulders and wear comfortable footwear for the steep climb.",
        "tags": "hiking,pilgrimage,sunrise,mountain,sacred,adventure",
        "safety_notes": "The climb is strenuous — 4–5 hours up, 3 hours down. Carry warm layers (summit is cold), water, and a torch. Not recommended for those with serious health conditions.",
    },
    # WATERFALLS
    {
        "name": "Ravana Falls",
        "category": "waterfalls", "province": "Uva",
        "short_description": "One of the widest falls in Asia, steeped in Ramayana mythology.",
        "description": "Ravana Falls is one of the widest waterfalls in Asia and is steeped in the legendary Hindu epic, the Ramayana. According to legend, King Ravana hid Princess Sita in the cave behind these falls. Located just outside Ella, the falls cascade 25 metres down a rocky cliff into a pool popular for swimming. The surrounding landscape is lush with jungle and the views are spectacular.",
        "city": "Ella", "latitude": 6.8648, "longitude": 81.0524,
        "budget_level": "free", "difficulty": "easy",
        "best_time_to_visit": "Year-round; most impressive after rains",
        "entry_fee": "Free",
        "is_hidden_gem": False, "is_featured": True,
        "tags": "waterfall,ella,swimming,ramayana,mythology,nature",
        "safety_notes": "Currents can be strong after heavy rainfall. Do not swim immediately after rains.",
    },
    {
        "name": "Bambarakanda Falls",
        "category": "waterfalls", "province": "Uva",
        "short_description": "Sri Lanka's tallest waterfall at 263m, a hidden gem in the highlands.",
        "description": "Bambarakanda Falls is the tallest waterfall in Sri Lanka at an impressive 263 metres, cascading through mist and forest in the Uva Highlands. Despite being the tallest, it remains far less visited than other falls, making it a true hidden gem. The journey to reach it involves a scenic hike through pine forests and paddy fields, rewarding visitors with solitude and breathtaking natural beauty.",
        "city": "Kalupahana", "latitude": 6.7559, "longitude": 80.8007,
        "budget_level": "free", "difficulty": "moderate",
        "best_time_to_visit": "Year-round; best during/after rains",
        "entry_fee": "Free",
        "is_hidden_gem": True,
        "tags": "waterfall,tallest,hidden gem,hiking,nature,highlands",
    },
    # HIDDEN GEMS
    {
        "name": "Pasikuda Beach",
        "category": "beach", "province": "Eastern",
        "short_description": "Calm, shallow turquoise lagoon on the east coast — still off the tourist trail.",
        "description": "Pasikuda is a gem on Sri Lanka's east coast, famous for its shallow, crystal-clear turquoise waters that extend far from the shore — perfect for families and non-swimmers. Unlike the south coast beaches, Pasikuda sees far fewer tourists and retains an authentic, peaceful quality. The beach stretches nearly 3km with pristine white sand and the town offers a taste of authentic east coast Sri Lankan life.",
        "city": "Pasikuda", "latitude": 7.9295, "longitude": 81.5598,
        "budget_level": "budget", "difficulty": "easy",
        "best_time_to_visit": "April to September",
        "entry_fee": "Free",
        "is_hidden_gem": True,
        "tags": "beach,east coast,shallow water,family,hidden gem,peaceful",
    },
    {
        "name": "Knuckles Mountain Range",
        "category": "adventure", "province": "Central",
        "short_description": "Misty UNESCO-listed range with cloud forests, waterfalls and tribal villages.",
        "description": "The Knuckles Conservation Forest is a UNESCO World Heritage Site largely overlooked by mainstream tourism. Named for the peaks resembling a clenched fist, this mountain range features cloud forests, diverse biodiversity, cascading waterfalls, and traditional Kandyan villages. Multi-day trekking routes pass through tea plantations, paddy terraces, and forests home to endemic species. The cool misty climate makes it a refreshing escape from the heat.",
        "city": "Kandy", "latitude": 7.4167, "longitude": 80.7833,
        "budget_level": "moderate", "difficulty": "challenging",
        "best_time_to_visit": "January to April",
        "entry_fee": "USD 10 (conservation fee)",
        "is_hidden_gem": True,
        "tags": "trekking,UNESCO,cloud forest,wildlife,hidden gem,camping",
        "safety_notes": "Hire a local guide for multi-day treks. Paths can be slippery. Inform someone of your route.",
    },
    {
        "name": "Jaffna Fort",
        "category": "historical", "province": "Northern",
        "short_description": "A sprawling Portuguese-Dutch fortress in the recovering, vibrant north.",
        "description": "Jaffna Fort is a massive star-shaped fortification built by the Portuguese in 1618 and later significantly expanded by the Dutch. Located in the northernmost province of Sri Lanka, visiting Jaffna means experiencing a completely different culture — Tamil heritage, unique cuisine, and the extraordinary determination of a city rebuilding after decades of conflict. The fort overlooks a serene lagoon and the surrounding town is rich with Hindu temples, colonial churches, and excellent seafood.",
        "city": "Jaffna", "latitude": 9.6615, "longitude": 80.0034,
        "budget_level": "free", "difficulty": "easy",
        "best_time_to_visit": "January to September",
        "entry_fee": "Free",
        "is_hidden_gem": True,
        "tags": "history,fort,jaffna,north,tamil culture,colonial,hidden gem",
    },
    {
        "name": "Ritigala Forest Monastery",
        "category": "historical", "province": "North Central",
        "short_description": "Eerie, jungle-consumed ruins of an ancient forest monastery. Almost no tourists.",
        "description": "Ritigala is one of Sri Lanka's most atmospheric and least-visited ancient sites. Scattered across a forested mountain plateau, these ruins of a 1st-century forest monastery are slowly being reclaimed by jungle. Monolithic stone causeways, meditation platforms, and stone walkways appear through the mist and ancient trees. The site appears in the Ramayana and the entire atmosphere is unlike anywhere else in Sri Lanka — silent, mysterious, and hauntingly beautiful.",
        "city": "Kekirawa", "latitude": 8.1186, "longitude": 80.6892,
        "budget_level": "budget", "difficulty": "moderate",
        "best_time_to_visit": "January to April",
        "entry_fee": "LKR 500",
        "is_hidden_gem": True,
        "tags": "ruins,hidden gem,forest,ancient,jungle,archaeology,mysterious",
        "safety_notes": "Bring insect repellent. The site is remote — hire a tuk-tuk driver who knows the route.",
    },
]


class Command(BaseCommand):
    help = 'Seed the database with Sri Lankan provinces, categories and destinations'

    def handle(self, *args, **kwargs):
        self.stdout.write('🌴 Seeding Lanka Explorer database...\n')

        # Provinces
        province_objs = {}
        for name in PROVINCES:
            p, _ = Province.objects.get_or_create(name=name)
            province_objs[name] = p
        self.stdout.write(f'  ✅ Created {len(PROVINCES)} provinces')

        # Categories
        cat_objs = {}
        for name, cat_type, icon in CATEGORIES:
            c, _ = Category.objects.get_or_create(
                name=name,
                defaults={'category_type': cat_type, 'icon': icon}
            )
            cat_objs[cat_type] = c
        self.stdout.write(f'  ✅ Created {len(CATEGORIES)} categories')

        # Destinations
        count = 0
        for data in DESTINATIONS:
            cat_key = data.pop('category')
            prov_name = data.pop('province')
            dest, created = Destination.objects.get_or_create(
                name=data['name'],
                defaults={
                    **data,
                    'category': cat_objs.get(cat_key),
                    'province': province_objs.get(prov_name),
                }
            )
            if created:
                count += 1

        self.stdout.write(f'  ✅ Created {count} destinations')

        # Create a superuser for demo
        from django.contrib.auth.models import User
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@lankaexplorer.lk', 'admin1234')
            self.stdout.write('  ✅ Created superuser: admin / admin1234')

        self.stdout.write(self.style.SUCCESS('\n🎉 Database seeded successfully!\n'))
        self.stdout.write('  → Run: python manage.py runserver')
        self.stdout.write('  → Admin: http://127.0.0.1:8000/admin (admin / admin1234)\n')
