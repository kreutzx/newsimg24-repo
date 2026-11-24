# Story data for the 24 November 2026 front page.
# Every item was reported on Tuesday 24 November 2026 (any time zone)
# or happened that day. Certainty: CONFIRMED / REPORTED / CLAIM / FORECAST.

HEROES = [
    {
        "kicker": "MONEY & TECH",
        "headline": "HUANG IS BACK \u2014 AND WALL STREET ROARS",
        "deck": "Nvidia reinstates Jensen Huang as CEO after Trump intervenes; shares jump 31.5%, the biggest one-day gain in 23 years, restoring about $1 trillion of value.",
        "source": "REUTERS",
        "cert": "CONFIRMED",
        "icon": "chip",
    },
    {
        "kicker": "WORLD",
        "headline": "24 KILLED IN INDONESIA FACTORY FIRE",
        "deck": "A blaze at a candy factory kills at least 24 people; rescuers keep searching for around 30 missing workers.",
        "source": "AP",
        "cert": "CONFIRMED",
        "icon": "flame",
    },
]

SECTIONS = [
    # (section, headline, deck, source, cert, icon or None)
    ("WORLD", "NATO SENDS AWACS TO POLAND AFTER MISSILES LAND",
     "NATO sends early-warning jets to its eastern flank.",
     "REUTERS", "CONFIRMED", "radar"),
    ("WORLD", "UKRAINE SAYS IT SANK A RUSSIAN WARSHIP OFF LIBYA",
     "Kyiv claims drones sank a corvette in a Libyan port.",
     "REUTERS", "CLAIM", "ship"),
    ("WORLD", "EU PROPOSES 22ND SANCTIONS PACKAGE ON RUSSIA",
     "Brussels targets banks, crypto and Russian flag teams.",
     "REUTERS", "CONFIRMED", "stars"),
    ("WORLD", "ISRAELI STRIKES KILL THREE IN GAZA, INCLUDING UN WORKER",
     "Airstrikes kill three, including a UN agency worker.",
     "REUTERS", "CONFIRMED", "building"),
    ("WORLD", "SEOUL WARNS ISLAND AFTER RUSSIAN JET ENTERS AIRSPACE",
     "Warning for Ulleung island after a Russian jet intrudes.",
     "REUTERS", "CONFIRMED", "jet"),
    ("MONEY & TECH", "ASIA SURGES AS NVIDIA RELIEF SPREADS",
     "KOSPI +7.5%, Taiwan +9.1%, Nikkei +4.5% in relief rally.",
     "REUTERS", "CONFIRMED", "chart"),
    ("MONEY & TECH", "SENSEX SLIDES 1,484 POINTS AS NIFTY DROPS 1.75%",
     "Sensex 82,436; Nifty 25,350 as bank stocks lead losses.",
     "REUTERS", "CONFIRMED", "cart"),
    ("MONEY & TECH", "DEEPMIND FINDS LEAN-VERIFIED QUANTUM ALGORITHMS",
     "Autonomously discovered algorithms, formally verified.",
     "GOOGLE DEEPMIND", "REPORTED", "atom"),
    ("MONEY & TECH", "CROWDSTRIKE SINKS 8.9% ON ZSCALER DEAL",
     "Shares slide as Wall Street rallies; S&P 500 up 4.7%.",
     "REUTERS", "CONFIRMED", "shield"),
    ("MONEY & TECH", "FED DECEMBER HIKE NOW PRICED AS A CERTAINTY",
     "Futures price a December hike at 100%; 50bp odds at 5%.",
     "CME FEDWATCH", "REPORTED", "bank"),
    ("SCIENCE & PLANET", "COP31 FALLOUT: BLAME, BACKLASH AND DESPAIR",
     "Australia blames its minister; Pacific nations despair.",
     "REUTERS", "CONFIRMED", "globe"),
    ("SCIENCE & PLANET", "CHINA UNVEILS EARTH-SYSTEM AI PLATFORM ZHU-GE",
     "Meteorology agency launches a planet-scale AI forecast.",
     "CMA", "REPORTED", "satellite"),
    ("SCIENCE & PLANET", "LAHORE TOPS WORLD POLLUTION RANKING AGAIN",
     "AQI crosses 500; eight Pakistani cities among worst.",
     "TIMES OF INDIA", "CONFIRMED", "smog"),
    ("SCIENCE & PLANET", "4.0 QUAKE STRIKES PAKISTAN NEAR AFGHAN BORDER",
     "Tremor near the Afghan border; no casualties reported.",
     "TIMES OF INDIA", "REPORTED", "quake"),
    ("SOCIETY & CULTURE", "MODI OPENS AI CENTRE AT IIT PATNA",
     "PM opens an AI centre and a Rs 400-crore research park.",
     "TIMES OF INDIA", "CONFIRMED", "cap"),
    ("SOCIETY & CULTURE", "SWIFT'S VIENNA SHOWS 'SAVED BY MOSSAD TIP-OFF'",
     "Ex-Mossad chief: Israel tipped off Vienna over a plot.",
     "TIMES OF INDIA", "REPORTED", "stage"),
    ("SOCIETY & CULTURE", "TRUMP HITS NEWSOM OVER 548 DEATH-ROW COMMUTATIONS",
     "President attacks governor in a Justice Dept speech.",
     "TIMES OF INDIA", "CONFIRMED", "podium"),
    ("SOCIETY & CULTURE", "DUTCH ACTIVIST, 28, DIES BY EUTHANASIA",
     "Jason Bhugwandass, 28, dies after years of suffering.",
     "TIMES OF INDIA", "REPORTED", "candle"),
]

SPORT = [
    ("CHESS", "GUKESH DEFENDS CROWN AS GAME 1 OPENS IN GENEVA",
     "The youngest world-title match ever: two 20-year-olds, 14 games, $2.5m fund.", "FIDE", "FORECAST"),
    ("FOOTBALL", "ARSENAL HOST DORTMUND; CITY FACE NAPOLI",
     "Matchday 5: Galatasaray host Aston Villa; Bodo/Glimt face LASK under the lights.", "UEFA", "FORECAST"),
    ("CRICKET", "INDIA\u2013NEW ZEALAND FIRST TEST ENDS IN A DRAW",
     "Visitors fight back at the Basin Reserve in Wellington to save the opener.", "TIMES OF INDIA", "CONFIRMED"),
    ("FOOTBALL", "DOUVIKAS LEADS UCL SCORING WITH SIX GOALS",
     "Como's striker tops the chart ahead of Tresoldi and Haaland on five.", "UEFA", "CONFIRMED"),
]

NUMBERS = [
    ("+31.5%", "Nvidia's one-day jump, its biggest in 23 years"),
    ("24", "killed in the Indonesia factory fire"),
    ("92,000", "registered at COP31, the largest climate summit ever"),
    ("500+", "Lahore's air quality index, worst in the world"),
]

MARKETS = [
    ("WALL STREET", "S&P 500 +4.7% \u00b7 Nasdaq +6.5% \u00b7 Nvidia +31.5%"),
    ("COMMODITIES", "Brent $89.50 \u00b7 Gold $3,657.97 \u00b7 10-yr Treasury 4.94%"),
    ("WEATHER", "Lahore AQI over 500 \u00b7 O'Hare ground stop"),
]

WIRE = [
    ("WAYMO PULLS DRIVERLESS TAXIS OFF US FREEWAYS", "REPORTED"),
    ("ICJ: MYANMAR COMMITTED GENOCIDE AGAINST ROHINGYA", "REPORTED"),
    ("MIGRANT BOAT CAPSIZES OFF SENEGAL; DOZENS MISSING", "REPORTED"),
    ("BRAZIL CUTS 2027 GROWTH FORECAST TO 1.8%", "REPORTED"),
    ("INFURION PAYMENT BREACH LEAKS UP TO 250,000 RECORDS", "REPORTED"),
]

TIMELINE = [
    ("00:10", "Indonesia fire toll reaches 24"),
    ("01:00", "Seoul warns Ulleung island"),
    ("07:00", "Asian markets surge on Nvidia relief"),
    ("10:00", "Sensex closes down 1.77%"),
    ("14:00", "Gukesh\u2013Sindarov Game 1 opens"),
    ("16:45", "Champions League night kicks off"),
]

DATE_LINE = "TUESDAY 24 NOVEMBER 2026"
ACCOUNTING = "36 STORIES \u00b7 7 REGIONS \u00b7 6 FIELDS \u00b7 ALL FROM TUESDAY 24 NOVEMBER 2026"
FIELD_COUNTS = "WORLD 6 \u00b7 MONEY & TECH 6 \u00b7 SCIENCE & PLANET 4 \u00b7 SOCIETY & CULTURE 4 \u00b7 SPORT 4 \u00b7 BY THE NUMBERS 4 \u00b7 MARKETS & WEATHER 3 \u00b7 LATE WIRE 5"
