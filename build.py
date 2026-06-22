# -*- coding: utf-8 -*-
"""
build.py — Authoring tool for the Meezab Z. International static website.

Edit the DATA / TEMPLATE sections below, then regenerate the whole site with:

    py build.py

This emits 21 HTML pages + assets/ + Complete_Website.html + README.md into the
folder this script lives in. The emitted HTML is what deploys (Netlify drop / cPanel).
There is no runtime build step — this script is an authoring convenience only.

Locked brand rules baked in (see Meezab_Z_Website_Build_Prompt.md):
  - Teal family + white ONLY. No off-palette colour anywhere.
  - Meezab Z. is an IMPORTER & DISTRIBUTOR (never "manufacturer").
  - Never a product count, never "approved" / "Form-7".
  - "Distributor(s)" never "Dealer(s)". No Urdu. WhatsApp is the primary CTA.
  - Poultry-led but never poultry-bound language. Honest stats only.
"""

import os
import json
from urllib.parse import quote

OUT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------------------
# 1) BRAND CONSTANTS
# ---------------------------------------------------------------------------

PHONE        = "061-2111031"
WA_NUMBER    = "923336875033"
WA_DISPLAY   = "+92 333 6875033"
WA_URL       = "https://wa.me/923336875033"
EMAIL        = "info@meezabz.com"
WEBSITE      = "www.meezabz.com"
ADDRESS      = "Bukhari, M.A. Jinnah Road, Gulraiz Town, Multan 60000, Pakistan"
HOURS        = "Mon–Sat, 9:00 AM – 6:00 PM"

MASTER_TAG   = "Science That Works."
SLOGAN       = "Your Trusted Partner in Animal Health"

NAV = [
    ("Home", "index.html"),
    ("About", "about.html"),
    ("Solutions", "solutions.html"),
    ("Products", "products.html"),
    ("Distributors", "distributors.html"),
    ("Contact", "contact.html"),
]

STATS = [
    ("Since 2014", "Founded 18 Oct 2014"),
    ("100+", "Areas served"),
    ("2", "Certified principals"),
    ("100%", "Certified sourcing"),
]


def wa(text):
    """Return a wa.me link with a pre-filled message."""
    return WA_URL + "?text=" + quote(text)


# ---------------------------------------------------------------------------
# 2) PRODUCT DATA (the ONLY products allowed — no counts, no "approved")
#    Composition lists active ingredients + role (honest; no invented mg figures).
#    Dosage is general water-soluble guidance + a "consult your vet" qualifier.
# ---------------------------------------------------------------------------

PRODUCTS = [
    {
        "slug": "aminoreef-sol", "name": "Aminoreef Sol",
        "principal": "REEFCO", "principal_slug": "principal-reefco",
        "origin": "Jordan", "cert": "WHO-GMP", "cat": "reefco", "featured": True,
        "what": "A balanced oral source of essential vitamins and amino acids.",
        "problem": "Recovery & vitamin gaps",
        "when": ["After vaccination", "Post-disease recovery", "Heat & transport stress", "Visible weakness"],
        "composition": [
            ("L-Lysine", "Muscle growth & protein synthesis"),
            ("DL-Methionine", "Feather & tissue development"),
            ("Vitamin B-complex", "Metabolism & appetite"),
            ("Vitamin C", "Anti-stress support"),
            ("Essential amino-acid blend", "Fills dietary gaps"),
        ],
        "dosage": "1 mL per 1–2 litres of drinking water for 3–5 consecutive days, or as advised by your veterinarian.",
        "works_with": ["recal-fos", "laxi-zyme-plus"],
    },
    {
        "slug": "recal-fos", "name": "Recal Fos",
        "principal": "REEFCO", "principal_slug": "principal-reefco",
        "origin": "Jordan", "cert": "WHO-GMP", "cat": "reefco", "featured": False,
        "what": "An electrolyte and calcium supplement for heat and dehydration stress.",
        "problem": "Heat stress / dehydration",
        "when": ["Summer heat waves", "Long transport", "After dehydration", "Soft-shell eggs"],
        "composition": [
            ("Calcium", "Eggshell & bone strength"),
            ("Phosphorus", "Energy & skeletal health"),
            ("Sodium & Potassium electrolytes", "Rehydration & acid-base balance"),
            ("Magnesium", "Nerve & muscle function"),
        ],
        "dosage": "1–2 mL per litre of drinking water during heat-stress periods, or as advised by your veterinarian.",
        "works_with": ["aminoreef-sol", "reevit-ad3ek-sol"],
    },
    {
        "slug": "reeftox-sol", "name": "Reeftox Sol",
        "principal": "REEFCO", "principal_slug": "principal-reefco",
        "origin": "Jordan", "cert": "WHO-GMP", "cat": "reefco", "featured": True,
        "what": "An organic-acid acidifier and toxin binder for gut health and water hygiene.",
        "problem": "Gut & dirty water (E.coli / Salmonella)",
        "when": ["Dirty or alkaline water", "Wet litter", "E.coli / Salmonella risk", "Poor gut health"],
        "composition": [
            ("Blend of organic acids", "Lowers water & gut pH"),
            ("Toxin binder", "Captures harmful toxins"),
            ("Acidifier complex", "Suppresses E.coli & Salmonella"),
            ("Gut-conditioning agents", "Supports beneficial flora"),
        ],
        "dosage": "0.5–1 mL per litre of drinking water as a continuous or periodic program, or as advised by your veterinarian.",
        "works_with": ["laxi-zyme-plus", "fegatosim"],
    },
    {
        "slug": "reevit-ad3ek-sol", "name": "Reevit AD₃EK Sol",
        "principal": "REEFCO", "principal_slug": "principal-reefco",
        "origin": "Jordan", "cert": "WHO-GMP", "cat": "reefco", "featured": False,
        "what": "A fat-soluble vitamin solution (A, D₃, E, K) for bones, eggshell and immunity.",
        "problem": "Bones, eggshell & immunity",
        "when": ["Bone & leg weakness", "Thin eggshells", "Low immunity", "Rapid growth phases"],
        "composition": [
            ("Vitamin A", "Vision, skin & mucous membranes"),
            ("Vitamin D₃", "Calcium absorption & bones"),
            ("Vitamin E", "Immunity & antioxidant"),
            ("Vitamin K", "Blood clotting & bone health"),
        ],
        "dosage": "1 mL per 2–4 litres of drinking water for 3–5 days, or as advised by your veterinarian.",
        "works_with": ["recal-fos", "reevit-e-se-150"],
    },
    {
        "slug": "reevit-e-se-150", "name": "Reevit E-Se 150",
        "principal": "REEFCO", "principal_slug": "principal-reefco",
        "origin": "Jordan", "cert": "WHO-GMP", "cat": "reefco", "featured": False,
        "what": "A vitamin E, selenium and zinc supplement for fertility and immunity.",
        "problem": "Fertility & immunity",
        "when": ["Breeder fertility", "Hatchability issues", "Immune support", "Muscle health"],
        "composition": [
            ("Vitamin E", "Antioxidant & fertility"),
            ("Selenium", "Immunity & cell protection"),
            ("Zinc", "Skin, feather & enzyme function"),
        ],
        "dosage": "1 mL per 2 litres of drinking water for 3–5 days, or as advised by your veterinarian.",
        "works_with": ["reevit-ad3ek-sol", "mentofresh"],
    },
    {
        "slug": "diureef-plus", "name": "Diureef Plus",
        "principal": "REEFCO", "principal_slug": "principal-reefco",
        "origin": "Jordan", "cert": "WHO-GMP", "cat": "reefco", "featured": False,
        "what": "A diuretic to support kidney function and flush urates.",
        "problem": "Gumboro / IBD & kidney urates",
        "when": ["Gumboro / IBD recovery", "Kidney swelling", "Urate build-up", "Post-medication flush"],
        "composition": [
            ("Diuretic herbal-saline complex", "Promotes healthy urine flow"),
            ("Kidney-support agents", "Flush uric acid & urates"),
            ("Electrolyte balancers", "Restore fluid balance"),
        ],
        "dosage": "1 mL per litre of drinking water for 2–3 days, or as advised by your veterinarian.",
        "works_with": ["reeftox-sol", "aminoreef-sol"],
    },
    {
        "slug": "laxi-zyme-plus", "name": "Laxi-Zyme Plus",
        "principal": "Lexington", "principal_slug": "principal-lexington",
        "origin": "Singapore", "cert": "HACCP-GMP", "cat": "lexington", "featured": True,
        "what": "A probiotic and digestive-enzyme blend for better FCR and gut health.",
        "problem": "Poor FCR / gut health",
        "when": ["Poor weight gain", "Undigested feed", "After antibiotics", "Gut balance"],
        "composition": [
            ("Probiotic cultures", "Restore beneficial gut flora"),
            ("Digestive enzymes (protease, amylase, lipase)", "Improve nutrient breakdown"),
            ("Prebiotic fibre", "Feed healthy bacteria"),
        ],
        "dosage": "1 mL or 1 g per litre of drinking water through the growth cycle, or as advised by your veterinarian.",
        "works_with": ["reeftox-sol", "aminoreef-sol"],
    },
    {
        "slug": "fegatosim", "name": "Fegatosim",
        "principal": "Lexington", "principal_slug": "principal-lexington",
        "origin": "Singapore", "cert": "HACCP-GMP", "cat": "lexington", "featured": True,
        "what": "A liver tonic and detox support against mycotoxin damage.",
        "problem": "Liver damage & mycotoxins",
        "when": ["Mycotoxin exposure", "Pale / fatty liver", "Heavy medication", "Poor feed quality"],
        "composition": [
            ("Liver-protective herbs", "Repair & protect liver cells"),
            ("Choline & methionine", "Fat metabolism & detox"),
            ("Sorbitol", "Bile flow & digestion"),
            ("B-vitamins", "Liver metabolism"),
        ],
        "dosage": "1 mL per litre of drinking water for 5–7 days, or as advised by your veterinarian.",
        "works_with": ["reeftox-sol", "aminoreef-sol"],
    },
    {
        "slug": "mentofresh", "name": "Mentofresh",
        "principal": "Lexington", "principal_slug": "principal-lexington",
        "origin": "Singapore", "cert": "HACCP-GMP", "cat": "lexington", "featured": False,
        "what": "A herbal respiratory support with eucalyptus, menthol and garlic.",
        "problem": "Respiratory & vaccination stress",
        "when": ["Cold & damp weather", "Respiratory distress", "Vaccination reactions", "Ammonia-heavy sheds"],
        "composition": [
            ("Eucalyptus oil", "Opens airways"),
            ("Menthol", "Soothes the respiratory tract"),
            ("Garlic extract", "Natural antimicrobial & immunity"),
            ("Herbal expectorants", "Help clear mucus"),
        ],
        "dosage": "0.5–1 mL per litre of drinking water during respiratory challenge, or as advised by your veterinarian.",
        "works_with": ["reevit-e-se-150", "fegatosim"],
    },
]

PRODUCT_BY_SLUG = {p["slug"]: p for p in PRODUCTS}


# ---------------------------------------------------------------------------
# 3) PRINCIPALS, LEADERSHIP, PROBLEMS, SEGMENTS, NETWORK, MISC DATA
# ---------------------------------------------------------------------------

PRINCIPALS = {
    "principal-reefco": {
        "slug": "principal-reefco",
        "name": "REEFCO — Al Reef Company",
        "country": "Jordan",
        "cert": "WHO-GMP",
        "intro": "Exclusive Pakistan distributor of REEFCO — Al Reef Company, a WHO-GMP certified animal-health manufacturer based in Jordan.",
        "about": "REEFCO — Al Reef Company is a Jordan-based manufacturer of poultry and animal-health solutions, working to international WHO-GMP standards. Their water-soluble range is built around the everyday challenges of commercial poultry — heat stress, gut health, vitamins and recovery.",
        "quote": "Internationally certified science, made practical for the Pakistani shed.",
        "milestones": [
            ("Heritage", "A trusted Jordanian animal-health manufacturer with a focus on water-soluble poultry solutions."),
            ("WHO-GMP", "Manufacturing aligned to WHO Good Manufacturing Practice standards."),
            ("Pakistan", "Meezab Z. International appointed as exclusive Pakistan distributor."),
            ("Today", "REEFCO products reaching 100+ areas across Pakistan through the Meezab network."),
        ],
    },
    "principal-lexington": {
        "slug": "principal-lexington",
        "name": "Lexington Enterprises",
        "country": "Singapore",
        "cert": "HACCP-GMP",
        "intro": "Exclusive Pakistan distributor of Lexington Enterprises, a HACCP-GMP certified animal-health company based in Singapore.",
        "about": "Lexington Enterprises is a Singapore-based animal-health company producing gut-health, liver and herbal respiratory solutions to HACCP-GMP standards. Their range complements REEFCO with a strong focus on FCR, liver protection and natural respiratory support.",
        "quote": "Backed by global science, focused on results you can measure in the shed.",
        "milestones": [
            ("Heritage", "A Singapore-based animal-health company with a focus on gut, liver and herbal solutions."),
            ("HACCP-GMP", "Production aligned to HACCP and Good Manufacturing Practice standards."),
            ("Pakistan", "Meezab Z. International appointed as exclusive Pakistan distributor."),
            ("Today", "Lexington products supporting healthier flocks across the Meezab network."),
        ],
    },
}

# (name, designation, detailed description, photo filename in assets/img/)
LEADERSHIP = [
    ("Ahmed Jahanzaib Shah", "Director of Operations",
     "Ahmed leads imports, supply chain and day-to-day operations at Meezab Z. International — "
     "making sure internationally certified animal-health products move reliably from our principals "
     "to distributors and farms across Pakistan. His focus is on certified sourcing, dependable supply "
     "and the systems that keep our network running.",
     "Ahmed Jahanzaib Shah.jpg"),
    ("Dildar Hussain Shah", "Director of Sales",
     "Dildar drives sales, field and technical engagement at Meezab Z. International — building strong "
     "distributor relationships and supporting farmers on the ground with the right certified products "
     "for their flock’s problems. His hands-on, farmer-first approach is at the heart of how we grow.",
     "Dildar Hussain Shah.jpg"),
]

# 7 core farmer problems
PROBLEMS = [
    {
        "title": "Heat Stress & Dehydration",
        "signs": "Panting, spread wings, drop in feed, soft-shell eggs.",
        "cause": "High temperature and humidity overwhelm the bird's cooling system.",
        "season": "Summer (May–Aug)",
        "products": ["recal-fos", "aminoreef-sol"],
    },
    {
        "title": "Poor Growth & FCR",
        "signs": "Slow weight gain, uneven flock, more feed for less meat.",
        "cause": "Weak gut, poor digestion and nutrient absorption.",
        "season": "All year",
        "products": ["laxi-zyme-plus", "aminoreef-sol"],
    },
    {
        "title": "E.coli / Salmonella & Dirty Water",
        "signs": "Wet litter, diarrhoea, higher mortality, foul droppings.",
        "cause": "Contaminated, alkaline water and a disturbed gut environment.",
        "season": "All year (worse in heat)",
        "products": ["reeftox-sol"],
    },
    {
        "title": "Liver Damage & Mycotoxins",
        "signs": "Pale or enlarged liver, poor appetite, drop in performance.",
        "cause": "Mouldy feed and mycotoxins overload the liver.",
        "season": "Monsoon & humid storage",
        "products": ["fegatosim", "reeftox-sol"],
    },
    {
        "title": "Respiratory & Vaccination Stress",
        "signs": "Coughing, sneezing, rattling, swollen faces, post-vaccine dip.",
        "cause": "Cold, ammonia, dust and vaccine reactions stress the airways.",
        "season": "Winter & vaccination windows",
        "products": ["mentofresh", "reevit-e-se-150"],
    },
    {
        "title": "Gumboro / IBD & Kidney",
        "signs": "Swollen kidneys, urate build-up, weakness after IBD.",
        "cause": "Viral challenge and medication load strain the kidneys.",
        "season": "Brooding & grower stages",
        "products": ["diureef-plus"],
    },
    {
        "title": "Bones, Eggshell & Fertility",
        "signs": "Leg weakness, thin shells, poor hatchability.",
        "cause": "Gaps in fat-soluble vitamins, calcium and minerals.",
        "season": "Rapid growth & lay",
        "products": ["reevit-ad3ek-sol", "reevit-e-se-150"],
    },
]

SEGMENTS = [
    ("Poultry", "Now", "Our flagship focus — internationally certified solutions for broilers, layers and breeders."),
    ("Livestock", "Coming Soon", "Cattle, buffalo and small-ruminant health solutions are planned."),
    ("Pets", "Coming Soon", "Companion-animal health products are on our roadmap."),
    ("Aqua", "Coming Soon", "Fish and shrimp health solutions are planned for the future."),
]

REGIONS = [
    ("Southern & Central Punjab", "active",
     ["Multan (HQ)", "Bahawalpur", "Rahim Yar Khan", "Dera Ghazi Khan", "Muzaffargarh",
      "Lodhran", "Vehari", "Khanewal", "Sahiwal", "Pakpattan", "Okara"]),
    ("Northern Punjab & Capital", "active",
     ["Lahore", "Faisalabad", "Gujranwala", "Sialkot", "Sargodha", "Rawalpindi",
      "Islamabad", "Sheikhupura", "Kasur", "Jhang", "Toba Tek Singh"]),
    ("Sindh & Balochistan", "active",
     ["Karachi", "Hyderabad", "Sukkur", "Nawabshah", "Larkana", "Quetta", "Hub"]),
    ("Upcoming — Khyber Pakhtunkhwa", "upcoming",
     ["Peshawar", "Mardan", "Abbottabad", "Swabi", "Nowshera"]),
]

GALLERY = [
    "Farm visit — Southern Punjab", "Distributor onboarding", "Product range display",
    "Field technical session", "Warehouse & dispatch", "Poultry-shed walkthrough",
    "REEFCO product line", "Lexington product line", "Team at a trade expo",
    "Heat-stress field support", "Distributor meet-up", "Quality certifications",
]

TESTIMONIALS = [
    ("The heat-stress program kept my birds eating through the worst of summer. Steady water intake made the difference.",
     "Poultry Farmer", "Southern Punjab — placeholder"),
    ("Reliable supply and certified products. Meezab's distributor support helps me grow my own area with confidence.",
     "Distributor", "Punjab — placeholder"),
    ("A certified, problem-first range I can recommend. The gut and liver products fit real field cases well.",
     "Veterinary Consultant", "Pakistan — placeholder"),
]

FAQ = [
    ("Are these products safe to use together?",
     "Many are designed to complement each other — each product page lists a “works well with” pairing. For a specific protocol, message us on WhatsApp and we’ll guide you."),
    ("How soon will I see results?",
     "It depends on the problem and the bird’s condition. Supportive products like electrolytes and gut conditioners often help within days when used correctly alongside good management."),
    ("Do you provide technical support?",
     "Yes. Our field and technical team is a WhatsApp message away to help you match the right product to your flock’s problem."),
    ("Are the products internationally certified?",
     "Yes. We distribute only from internationally certified principals — REEFCO (Jordan, WHO-GMP) and Lexington Enterprises (Singapore, HACCP-GMP)."),
    ("Do you sell directly to farmers or through distributors?",
     "We are an importer and distributor and work through a growing distributor network across Pakistan. Message us and we’ll connect you to your nearest distributor."),
    ("How do I order or become a distributor?",
     "Tap any WhatsApp button on this site, or visit the Distributors page to apply. We’ll respond during business hours."),
]

WHY_CARDS = [
    ("Globally Certified Sourcing",
     "We distribute only from WHO-GMP and HACCP-GMP certified principals — internationally certified science, not guesswork."),
    ("Problem-First Protocols",
     "Our range is matched to the real problems you face in the shed, from heat stress to gut health and recovery."),
    ("Field & WhatsApp Support",
     "Technical guidance is a message away. We help you pick the right product for the right problem, fast."),
]

VALUES = [
    ("Integrity", "We say what’s true — honest claims, certified sourcing, no hype."),
    ("Science First", "Every product is backed by internationally certified manufacturing."),
    ("Farmer Focus", "We lead with your problem, then the solution that fits it."),
    ("Reliability", "Consistent supply and dependable support across our network."),
]

DEFINES = [
    ("Deep Expertise", "Years in the poultry industry — imports, supply chain, field and technical engagement."),
    ("Certified Sourcing", "We import only from internationally certified principals — WHO-GMP and HACCP-GMP."),
    ("Problem-First Approach", "We map every product to a real farmer problem, not a catalogue."),
    ("Reliable Distribution", "A growing distributor network delivering to 100+ areas across Pakistan."),
]

# ---------------------------------------------------------------------------
# 4) INLINE SVG: logo, WhatsApp glyph, icon set
# ---------------------------------------------------------------------------

# The brand logo is the user-supplied vector at assets/img/Logo.svg (a teal cursive
# "m" inside a teal double-line square frame). It is referenced as an <img> so the
# real artwork is used verbatim and never recoloured. NOTE: the filename casing
# ("Logo.svg") matters on case-sensitive hosts (Netlify/Linux) — keep it exact.
LOGO_FILE = "assets/img/Logo.svg"
LOGO_SVG = (f'<img class="logo" src="{LOGO_FILE}" '
            'alt="Meezab Z. International logo" width="48" height="48" loading="eager">')

WA_GLYPH = (
    '<svg class="wa-ic" viewBox="0 0 32 32" aria-hidden="true">'
    '<path fill="currentColor" d="M16 3C9 3 3.5 8.5 3.5 15.5c0 2.4.7 4.6 1.9 6.5L4 29l7.2-1.9c1.8 1 '
    '3.9 1.5 6 1.5 7 0 12.5-5.5 12.5-12.5S23 3 16 3zm0 22.8c-1.9 0-3.7-.5-5.3-1.5l-.4-.2-4.3 '
    '1.1 1.1-4.2-.2-.4C5.7 19.3 5.2 17.4 5.2 15.5 5.2 9.6 10.1 4.8 16 4.8S26.8 9.6 26.8 15.5 '
    '21.9 25.8 16 25.8zm6-7.8c-.3-.2-1.9-.9-2.2-1-.3-.1-.5-.2-.7.2-.2.3-.8 1-1 1.2-.2.2-.4.2-.7.1-1.9-.9-3.1-1.6-4.4-3.7-.3-.5.3-.5.9-1.6.1-.2 0-.4 '
    '0-.5 0-.1-.7-1.7-1-2.3-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 '
    '3.1c.2.2 2.2 3.4 5.3 4.7 2 .8 2.7.9 3.7.8.6-.1 1.9-.8 2.1-1.5.3-.7.3-1.4.2-1.5-.1-.2-.3-.2-.6-.4z"/>'
    '</svg>'
)

ICONS = {
    "shield": "M12 3l7 3v6c0 4-3 7-7 9-4-2-7-5-7-9V6l7-3z",
    "check":  "M20 6L9 17l-5-5",
    "chat":   "M4 5h16v10H8l-4 3z",
    "drop":   "M12 3s6 6 6 11a6 6 0 0 1-12 0c0-5 6-11 6-11z",
    "sun":    "M12 8a4 4 0 1 0 0 8 4 4 0 0 0 0-8z M12 2v2 M12 20v2 M3 12h2 M19 12h2 M5.2 5.2l1.4 1.4 M17.4 17.4l1.4 1.4 M18.8 5.2l-1.4 1.4 M6.6 17.4l-1.4 1.4",
    "leaf":   "M5 20c0-9 6-15 15-15 0 9-6 15-15 15z M5 20c4-5 8-7 12-8",
    "truck":  "M3 6h11v9H3z M14 9h4l3 3v3h-7z M7 19a2 2 0 1 0 0-4 2 2 0 0 0 0 4z M18 19a2 2 0 1 0 0-4 2 2 0 0 0 0 4z",
    "phone":  "M5 4h4l2 5-3 2a12 12 0 0 0 5 5l2-3 5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z",
    "mail":   "M3 6h18v12H3z M3 7l9 6 9-6",
    "pin":    "M12 22s7-6 7-12a7 7 0 1 0-14 0c0 6 7 12 7 12z M12 8a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5z",
    "clock":  "M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18z M12 7v5l3 2",
    "flask":  "M9 3h6 M10 3v6l-5 9a2 2 0 0 0 2 3h10a2 2 0 0 0 2-3l-5-9V3",
    "gut":    "M7 4c6 0 6 4 0 4s-6 4 0 4 6 4 0 4",
    "egg":    "M12 3c4 0 6 6 6 10a6 6 0 0 1-12 0c0-4 2-10 6-10z",
    "lungs":  "M12 4v8 M9 9c-3 1-4 4-4 7a2 2 0 0 0 4 0V9z M15 9c3 1 4 4 4 7a2 2 0 0 1-4 0V9z",
    "kidney": "M11 5c-5 0-8 3-8 7s3 7 7 7c3 0 3-2 3-5s2-3 2-6-2-3-4-3z",
    "hands":  "M3 12l4-4 4 3 4-3 4 4-4 5-4-3-4 3z",
    "award":  "M12 3a5 5 0 1 0 0 10 5 5 0 0 0 0-10z M9 13l-1 8 4-2 4 2-1-8",
    "arrow":  "M5 12h14 M13 6l6 6-6 6",
    "bottle": "M10 3h4 M10 6h4 M9 9h6l1 9a2 2 0 0 1-2 2H10a2 2 0 0 1-2-2l1-9z",
    "globe":  "M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18z M3 12h18 M12 3c3 3 3 15 0 18 M12 3c-3 3-3 15 0 18",
    "compass":"M12 3a9 9 0 1 0 0 18 9 9 0 0 0 0-18z M15 9l-2 4-4 2 2-4z",
}


def icon(name, cls=""):
    d = ICONS.get(name, ICONS["check"])
    return (f'<svg class="ic {cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
            f'<path d="{d}"/></svg>')


# Social media — brand glyphs + the company's public profile links
FB_GLYPH = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22 12.06C22 6.5 '
            '17.52 2 12 2S2 6.5 2 12.06c0 5 3.66 9.15 8.44 9.94v-7.03H7.9v-2.9h2.54V9.85c0-2.52 '
            '1.49-3.91 3.78-3.91 1.1 0 2.24.2 2.24.2v2.47h-1.26c-1.24 0-1.63.77-1.63 1.56v1.88h2.78l-.44 '
            '2.9h-2.34V22c4.78-.79 8.43-4.94 8.43-9.94z"/></svg>')
IG_GLYPH = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            'stroke-linecap="round" aria-hidden="true"><rect x="2.5" y="2.5" width="19" height="19" rx="5.5"/>'
            '<circle cx="12" cy="12" r="4.2"/>'
            '<circle cx="17.4" cy="6.6" r="1.1" fill="currentColor" stroke="none"/></svg>')
LI_GLYPH = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 1 '
            '0 5.001 2.5 2.5 0 0 1 0-5zM2.95 9h4.06v12H2.95zM9.34 9h3.9v1.64h.05c.54-1.03 1.87-2.12 '
            '3.85-2.12 4.12 0 4.88 2.71 4.88 6.23V21h-4.06v-5.45c0-1.3-.02-2.97-1.81-2.97-1.82 '
            '0-2.1 1.42-2.1 2.88V21H9.34z"/></svg>')

SOCIALS = [
    ("Facebook", "https://www.facebook.com/meezabZ.interenational", FB_GLYPH),
    ("Instagram", "https://www.instagram.com/meezabz.interenational", IG_GLYPH),
    ("LinkedIn", "https://www.linkedin.com/company/107295364", LI_GLYPH),
]


def social_row():
    items = "".join(
        f'<a href="{url}" target="_blank" rel="noopener" aria-label="Meezab Z. International on {name}">'
        f'{glyph}</a>' for name, url, glyph in SOCIALS)
    return f'<div class="footer-social">{items}</div>'


# ---------------------------------------------------------------------------
# 5) SHARED TEMPLATE PIECES
# ---------------------------------------------------------------------------

def header(active):
    links = "".join(
        f'<a class="nav-link{" active" if href == active else ""}" href="{href}"'
        f'{" aria-current=\"page\"" if href == active else ""}>{label}</a>'
        for label, href in NAV
    )
    return f"""<header class="site-header" id="siteHeader">
  <div class="container nav">
    <a class="brand" href="index.html" aria-label="Meezab Z. International — home">
      <span class="brand-mark">{LOGO_SVG}</span>
      <span class="brand-text"><b>MEEZAB Z</b><i>INTERNATIONAL</i></span>
    </a>
    <nav class="nav-links" aria-label="Primary">{links}</nav>
    <a class="btn btn-wa nav-cta" href="{WA_URL}" target="_blank" rel="noopener">{WA_GLYPH}<span>WhatsApp Us</span></a>
    <button class="hamburger" id="hamburger" aria-label="Open menu" aria-expanded="false" aria-controls="mobileMenu">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
<div class="scrim" id="scrim" hidden></div>
<aside class="mobile-menu" id="mobileMenu" aria-label="Mobile" hidden>
  <button class="mm-close" id="mmClose" aria-label="Close menu">&times;</button>
  <nav class="mm-links">{links}</nav>
  <a class="btn btn-wa mm-cta" href="{WA_URL}" target="_blank" rel="noopener">{WA_GLYPH}<span>WhatsApp Us</span></a>
</aside>"""


def footer():
    quick = "".join(f'<li><a href="{href}">{label}</a></li>' for label, href in [
        ("About", "about.html"), ("Distribution Network", "network.html"),
        ("Distributors", "distributors.html"), ("Gallery", "gallery.html"),
    ])
    join_wa = wa("Hi Meezab Z., I'd like to get seasonal flock alerts on WhatsApp.")
    return f"""<footer class="site-footer">
  <div class="footer-top">
    <div class="container footer-top-in">
      <p>{icon('chat')} Get seasonal flock alerts on WhatsApp.</p>
      <a class="btn btn-wa" href="{join_wa}" target="_blank" rel="noopener">{WA_GLYPH}<span>Join on WhatsApp</span></a>
    </div>
  </div>
  <div class="container footer-cols">
    <div class="footer-col footer-brand">
      <span class="brand-mark footer-mark">{LOGO_SVG}</span>
      <p class="footer-tag">{MASTER_TAG}</p>
      <p class="footer-desc">Importer &amp; distributor of internationally certified animal-health products,
        currently specialising in poultry · Multan · since 2014.</p>
      {social_row()}
    </div>
    <div class="footer-col">
      <h4>Quick Links</h4>
      <ul class="footer-links">{quick}</ul>
    </div>
    <div class="footer-col">
      <h4>Contact</h4>
      <ul class="footer-contact">
        <li>{icon('phone')}<a href="tel:{PHONE.replace('-', '')}">{PHONE}</a></li>
        <li>{icon('chat')}<a href="{WA_URL}" target="_blank" rel="noopener">{WA_DISPLAY}</a></li>
        <li>{icon('mail')}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>{icon('pin')}<span>{ADDRESS}</span></li>
        <li>{icon('clock')}<span>{HOURS}</span></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Stay Connected</h4>
      <p class="footer-desc">Questions about a product or your flock? We’re here to help during business hours.</p>
      <a class="footer-getintouch" href="contact.html">Get in Touch <span aria-hidden="true">↗</span></a>
    </div>
  </div>
  <div class="legal-bar">
    <div class="container legal-in">
      <p>© <span id="year">2026</span> Meezab Z. International. All rights reserved.
        <a href="privacy.html">Privacy</a> · <a href="terms.html">Terms</a></p>
      <p class="legal-fine">Exclusive Pakistan distributor of REEFCO (Jordan) &amp; Lexington Enterprises (Singapore).</p>
    </div>
  </div>
</footer>"""


def float_wa():
    link = wa("Hi Meezab Z., I have a question about your products.")
    return (f'<a class="float-wa" href="{link}" target="_blank" rel="noopener" '
            f'aria-label="Chat with us on WhatsApp">{WA_GLYPH}</a>')


def doc(title, desc, body, active, body_class="", extra_head=""):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Meezab Z. International">
<meta name="theme-color" content="#187986">
<link rel="icon" href="assets/img/Logo.svg">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap">
<link rel="stylesheet" href="assets/css/style.css">
<script>document.documentElement.classList.add('js-on');</script>
{extra_head}</head>
<body class="{body_class}">
<a class="skip" href="#main">Skip to content</a>
{header(active)}
<main id="main">
{body}
</main>
{footer()}
{float_wa()}
<script src="assets/js/main.js" defer></script>
</body>
</html>"""


# small markup helpers -------------------------------------------------------

def eyebrow(t):
    return f'<p class="eyebrow">{t}</p>'


def wa_btn(label, text, outline=False, big=False):
    cls = "btn btn-wa"
    if big:
        cls += " btn-lg"
    return (f'<a class="{cls}" href="{wa(text)}" target="_blank" rel="noopener">'
            f'{WA_GLYPH}<span>{label}</span></a>')


def link_btn(label, href, outline=False, big=False, arrow=False):
    cls = "btn " + ("btn-outline" if outline else "btn-solid")
    if big:
        cls += " btn-lg"
    tail = ' <span aria-hidden="true">→</span>' if arrow else ""
    return f'<a class="{cls}" href="{href}">{label}{tail}</a>'


def cta_band(title, text, primary_text="Hi Meezab Z., I'd like to know more."):
    return f"""<section class="cta-band reveal">
  <div class="container cta-in">
    <h2>{title}</h2>
    <p>{text}</p>
    <div class="btn-row">
      {wa_btn("WhatsApp Us Now", primary_text, big=True)}
      {link_btn("Become a Distributor", "distributors.html", outline=True, big=True)}
    </div>
  </div>
</section>"""


def product_card(p):
    return f"""<a class="product-card reveal" href="product-{p['slug']}.html" data-cat="{p['cat']}">
  <span class="product-thumb">{icon('bottle')}</span>
  <span class="product-body">
    <span class="badge badge-{p['cat']}">{p['principal']} · {p['origin']} · {p['cert']}</span>
    <span class="product-name">{p['name']}</span>
    <span class="product-what">{p['what']}</span>
    <span class="product-prob">{icon('check')} {p['problem']}</span>
  </span>
  <span class="product-go">View product <span aria-hidden="true">→</span></span>
</a>"""


# ---------------------------------------------------------------------------
# 6) STYLESHEET  (teal family + white ONLY — all colour via CSS custom props)
# ---------------------------------------------------------------------------

CSS = r""":root{
  /* Palette derived from the brand logo (assets/img/Logo.svg) — primary teal #187986 */
  --teal:#187986; --deep:#0E5660; --soft:#D2EBEE; --bright:#5FC8CB;
  --wash:#F1FAFB; --white:#FFFFFF; --ink:#0C2B30; --muted:#3A5D62;
  --line:#CDE6E8; --shadow:0 14px 40px -18px rgba(14,86,96,.45);
  --shadow-sm:0 6px 18px -10px rgba(14,86,96,.4);
  --radius:16px; --maxw:1140px; --grad:linear-gradient(135deg,var(--teal),var(--deep));
}
*{box-sizing:border-box}
[hidden]{display:none!important}
html{scroll-behavior:smooth}
body{margin:0;font-family:'Inter',system-ui,Arial,sans-serif;color:var(--ink);
  background:var(--white);line-height:1.6;-webkit-font-smoothing:antialiased}
img{max-width:100%;display:block}
a{color:var(--teal);text-decoration:none}
h1,h2,h3,h4{line-height:1.18;color:var(--deep);margin:0 0 .5em;font-weight:800;letter-spacing:-.01em}
p{margin:0 0 1em}
.container{width:100%;max-width:var(--maxw);margin:0 auto;padding:0 22px}
.ic{width:24px;height:24px;flex:none}
.skip{position:absolute;left:-999px;top:0;background:var(--deep);color:#fff;padding:10px 16px;border-radius:8px;z-index:1000}
.skip:focus{left:12px;top:12px}
:focus-visible{outline:3px solid var(--bright);outline-offset:2px;border-radius:6px}

/* buttons */
.btn{display:inline-flex;align-items:center;gap:.5em;font-weight:700;font-size:.98rem;white-space:nowrap;
  padding:13px 22px;border-radius:999px;border:2px solid transparent;cursor:pointer;
  transition:transform .15s ease,box-shadow .2s ease,background .2s ease,color .2s ease;line-height:1}
.btn:hover{transform:translateY(-2px)}
.btn-lg{padding:16px 28px;font-size:1.05rem}
.btn-solid{background:var(--teal);color:#fff;box-shadow:var(--shadow-sm)}
.btn-solid:hover{background:var(--deep);color:#fff}
.btn-outline{background:transparent;color:var(--deep);border-color:var(--teal)}
.btn-outline:hover{background:var(--soft)}
.btn-wa{background:var(--teal);color:#fff;box-shadow:var(--shadow-sm)}
.btn-wa:hover{background:var(--deep);color:#fff}
.wa-ic{width:20px;height:20px;flex:none}
.btn-row{display:flex;flex-wrap:wrap;gap:14px}

/* header */
.site-header{position:fixed;top:0;left:0;right:0;z-index:100;
  background:rgba(255,255,255,.92);backdrop-filter:saturate(1.4) blur(12px);
  border-bottom:1px solid var(--line);transition:background .25s ease,box-shadow .25s ease}
.site-header.scrolled{box-shadow:var(--shadow-sm)}
.nav{display:flex;align-items:center;gap:18px;height:74px}
.brand{display:flex;align-items:center;gap:11px}
.brand-mark{width:42px;height:42px;display:block;border-radius:11px;overflow:hidden;background:#fff}
.brand-mark .logo{width:100%;height:100%;object-fit:contain;display:block}
.brand-text{display:flex;flex-direction:column;line-height:1}
.brand-text b{font-size:1.02rem;color:var(--deep);letter-spacing:.06em;font-weight:800}
.brand-text i{font-size:.62rem;color:var(--teal);letter-spacing:.32em;font-style:normal;font-weight:600}
.nav-links{display:flex;align-items:center;gap:4px;margin-left:auto}
.nav-link{padding:9px 13px;border-radius:999px;color:var(--ink);font-weight:600;font-size:.95rem}
.nav-link:hover{background:var(--soft);color:var(--deep)}
.nav-link.active{background:var(--teal);color:#fff}
.nav-cta{margin-left:6px;padding:11px 18px}
.hamburger{display:none;flex-direction:column;gap:5px;width:46px;height:42px;margin-left:auto;
  border:1px solid var(--line);border-radius:11px;background:#fff;cursor:pointer;align-items:center;justify-content:center}
.hamburger span{width:22px;height:2px;background:var(--deep);border-radius:2px}

/* header transparent over hero (home, JS only) */
.js-on .home .site-header.at-top{background:transparent;border-color:transparent;box-shadow:none}
.home .site-header.at-top .brand-text b{color:#fff}
.home .site-header.at-top .brand-text i{color:var(--bright)}
.home .site-header.at-top .nav-link{color:#eafafa}
.home .site-header.at-top .nav-link:hover{background:rgba(255,255,255,.16)}
.home .site-header.at-top .nav-link.active{background:rgba(255,255,255,.22);color:#fff}
.home .site-header.at-top .hamburger{background:transparent}
.home .site-header.at-top .hamburger span{background:#fff}

/* mobile menu */
.scrim{position:fixed;inset:0;background:rgba(15,46,46,.5);z-index:110}
.mobile-menu{position:fixed;top:0;right:0;bottom:0;width:min(82vw,320px);background:#fff;z-index:120;
  padding:78px 22px 28px;box-shadow:-20px 0 50px -20px rgba(14,86,96,.5);display:flex;flex-direction:column;gap:6px}
.mobile-menu .mm-links{display:flex;flex-direction:column;gap:2px}
.mobile-menu .nav-link{font-size:1.05rem;padding:13px 14px}
.mm-cta{justify-content:center;margin-top:16px}
.mm-close{position:absolute;top:16px;right:18px;width:42px;height:42px;border:1px solid var(--line);
  border-radius:11px;background:#fff;font-size:1.7rem;line-height:1;color:var(--deep);cursor:pointer}

/* generic section */
main{padding-top:74px}
.section{padding:74px 0}
.section.wash{background:var(--wash)}
.section.soft{background:var(--soft)}
.section-head{max-width:720px;margin:0 auto 42px;text-align:center}
.section-head.left{margin-left:0;text-align:left}
.eyebrow{text-transform:uppercase;letter-spacing:.18em;font-size:.74rem;font-weight:700;color:var(--teal);margin:0 0 .7em}
h2.h2,.section-head h2{font-size:clamp(1.6rem,3.4vw,2.3rem)}
.section-head p.sub{color:var(--muted);font-size:1.06rem;margin:0}
.center{text-align:center}
.mt{margin-top:26px}

/* grids & cards */
.grid{display:grid;gap:22px}
.grid-2{grid-template-columns:repeat(2,1fr)}
.grid-3{grid-template-columns:repeat(3,1fr)}
.grid-4{grid-template-columns:repeat(4,1fr)}
.card{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:26px;
  box-shadow:var(--shadow-sm)}
.card h3{font-size:1.18rem;margin-bottom:.35em}
.card p{color:var(--muted);margin:0}
.card-icon{width:54px;height:54px;border-radius:14px;background:var(--soft);color:var(--teal);
  display:flex;align-items:center;justify-content:center;margin-bottom:16px}
.card-icon .ic{width:28px;height:28px}
.card-link{display:inline-flex;align-items:center;gap:.4em;margin-top:14px;font-weight:700;color:var(--teal)}

/* hero */
.hero{position:relative;background:var(--grad);color:#fff;overflow:hidden;
  padding:140px 0 96px;margin-top:-74px}
.hero canvas{position:absolute;inset:0;width:100%;height:100%;opacity:.55}
.hero-glow{position:absolute;inset:0;background:radial-gradient(900px 500px at 75% 10%,rgba(127,214,214,.35),transparent 60%)}
.hero-inner{position:relative;max-width:780px}
.hero-badge{display:inline-flex;align-items:center;gap:12px;background:rgba(255,255,255,.12);
  border:1px solid rgba(255,255,255,.28);padding:8px 16px 8px 8px;border-radius:999px;margin-bottom:22px}
.hero-badge .brand-mark{width:38px;height:38px;border-radius:10px}
.hero-badge span{font-weight:600;font-size:.92rem;letter-spacing:.01em}
.hero h1{color:#fff;font-size:clamp(2.3rem,6vw,4rem);margin:0 0 .25em;letter-spacing:-.02em}
.hero .slogan{color:var(--bright);font-weight:700;letter-spacing:.02em;margin:0 0 .6em;font-size:1.05rem}
.hero .lead{font-size:1.16rem;color:#e8fbfb;max-width:620px;margin:0 0 30px}
.hero-cta{display:flex;flex-wrap:wrap;gap:14px;margin-bottom:30px}
.hero .btn-outline{color:#fff;border-color:rgba(255,255,255,.6)}
.hero .btn-outline:hover{background:rgba(255,255,255,.14)}
.trust-chips{display:flex;flex-wrap:wrap;gap:10px}
.chip{display:inline-flex;align-items:center;gap:7px;background:rgba(255,255,255,.12);
  border:1px solid rgba(255,255,255,.24);padding:7px 14px;border-radius:999px;font-size:.85rem;font-weight:600}
.chip .ic{width:17px;height:17px;color:var(--bright)}

/* trust strip */
.trust-strip{background:var(--deep);color:#fff}
.trust-strip .container{display:flex;flex-wrap:wrap;justify-content:space-around;gap:18px;padding-top:22px;padding-bottom:22px}
.trust-item{display:flex;align-items:center;gap:10px;font-weight:600;font-size:.95rem}
.trust-item .ic{color:var(--bright);width:22px;height:22px}

/* stats */
.stats{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.stat{background:#fff;border:1px solid var(--line);border-radius:14px;padding:22px 16px;text-align:center}
.stat-num{font-size:1.9rem;font-weight:800;color:var(--teal);line-height:1}
.stat-label{color:var(--muted);font-size:.9rem;margin-top:6px}

/* about teaser split */
.split{display:grid;grid-template-columns:1.05fr .95fr;gap:46px;align-items:center}
.split .ph-card{aspect-ratio:4/3}
.img-card{width:100%;height:auto;border-radius:var(--radius);box-shadow:var(--shadow);border:1px solid var(--line);display:block}

/* problem grid */
.problem-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.problem-card{display:flex;flex-direction:column;gap:10px;background:#fff;border:1px solid var(--line);
  border-radius:14px;padding:22px;transition:transform .15s ease,box-shadow .2s ease;color:inherit}
.problem-card:hover{transform:translateY(-3px);box-shadow:var(--shadow)}
.problem-card .card-icon{margin:0}
.problem-card h3{font-size:1.04rem;margin:0}
.problem-card .season{margin-top:auto;font-size:.8rem;color:var(--teal);font-weight:700;text-transform:uppercase;letter-spacing:.06em}

/* product card */
.product-card{display:flex;flex-direction:column;background:#fff;border:1px solid var(--line);
  border-radius:var(--radius);overflow:hidden;transition:transform .15s ease,box-shadow .2s ease;color:inherit}
.product-card:hover{transform:translateY(-4px);box-shadow:var(--shadow)}
.product-thumb{height:120px;background:var(--grad);color:#fff;display:flex;align-items:center;justify-content:center}
.product-thumb .ic{width:46px;height:46px}
.product-body{display:flex;flex-direction:column;gap:8px;padding:20px 20px 6px}
.badge{align-self:flex-start;font-size:.7rem;font-weight:700;letter-spacing:.03em;text-transform:uppercase;
  background:var(--soft);color:var(--deep);padding:5px 10px;border-radius:999px}
.product-name{font-size:1.16rem;font-weight:800;color:var(--deep)}
.product-what{color:var(--muted);font-size:.95rem}
.product-prob{display:flex;align-items:center;gap:7px;font-size:.86rem;color:var(--teal);font-weight:600}
.product-prob .ic{width:17px;height:17px}
.product-go{margin-top:auto;padding:14px 20px;border-top:1px solid var(--line);font-weight:700;color:var(--teal);font-size:.92rem}

/* filter bar */
.filterbar{display:flex;flex-wrap:wrap;gap:10px;justify-content:center;margin-bottom:34px}
.filter-btn{border:1px solid var(--line);background:#fff;color:var(--deep);font-weight:600;
  padding:10px 18px;border-radius:999px;cursor:pointer;font-size:.92rem}
.filter-btn.active{background:var(--teal);color:#fff;border-color:var(--teal)}

/* principal card */
.principal-card{display:flex;flex-direction:column;gap:14px;background:#fff;border:1px solid var(--line);
  border-radius:var(--radius);padding:28px;box-shadow:var(--shadow-sm)}
.principal-head{display:flex;align-items:center;gap:14px}
.principal-flag{width:54px;height:54px;border-radius:14px;background:var(--grad);color:#fff;
  display:flex;align-items:center;justify-content:center}
.principal-flag .ic{width:28px;height:28px}
.cert-badge{display:inline-flex;align-items:center;gap:6px;background:var(--soft);color:var(--deep);
  font-weight:700;font-size:.8rem;padding:5px 12px;border-radius:999px}
.cert-badge .ic{width:15px;height:15px;color:var(--teal)}

/* leader card — photo on top, then name, designation, description */
.leader-card{display:flex;flex-direction:column;background:#fff;border:1px solid var(--line);
  border-radius:var(--radius);overflow:hidden;box-shadow:var(--shadow-sm)}
.leader-photo-img{width:100%;height:420px;object-fit:cover;object-position:center top;
  display:block;background:var(--soft)}
.leader-body{padding:26px;text-align:center}
.leader-card h3{margin:0;font-size:1.25rem}
.leader-role{color:var(--teal);font-weight:700;font-size:.98rem;margin:5px 0 12px}
.leader-card p{margin:0;color:var(--muted);font-size:.94rem;line-height:1.65}
@media (max-width:760px){.leader-photo-img{height:360px}}

/* segments */
.segment-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.segment-card{position:relative;background:#fff;border:1px solid var(--line);border-radius:var(--radius);
  padding:26px;text-align:center}
.segment-card.now{background:var(--grad);color:#fff;border-color:transparent}
.segment-card.now h3{color:#fff}
.segment-card .seg-ic{width:60px;height:60px;border-radius:16px;background:var(--soft);color:var(--teal);
  display:flex;align-items:center;justify-content:center;margin:0 auto 16px}
.segment-card.now .seg-ic{background:rgba(255,255,255,.18);color:#fff}
.segment-card .seg-ic .ic{width:30px;height:30px}
.tag-now,.tag-soon{display:inline-block;font-size:.72rem;font-weight:700;letter-spacing:.05em;
  text-transform:uppercase;padding:4px 12px;border-radius:999px;margin-bottom:12px}
.tag-now{background:var(--bright);color:var(--deep)}
.tag-soon{background:var(--soft);color:var(--muted)}
.segment-card p{color:var(--muted);font-size:.9rem;margin:0}
.segment-card.now p{color:#eafbfb}

/* testimonials */
.quote-card{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:28px;position:relative}
.quote-card .mark{font-size:3rem;color:var(--soft);line-height:.6;font-weight:800}
.quote-card p{font-size:1rem;color:var(--ink)}
.quote-by{display:flex;align-items:center;gap:12px;margin-top:14px}
.quote-av{width:46px;height:46px;border-radius:50%;background:var(--grad);color:#fff;display:flex;
  align-items:center;justify-content:center;font-weight:700}
.quote-by b{display:block;color:var(--deep)}
.quote-by span{font-size:.84rem;color:var(--muted)}

/* CTA band */
.cta-band{background:var(--grad);color:#fff;text-align:center;padding:64px 0}
.cta-band h2{color:#fff;font-size:clamp(1.7rem,3.6vw,2.4rem)}
.cta-band p{color:#e9fbfb;max-width:620px;margin:0 auto 26px;font-size:1.08rem}
.cta-band .btn-row{justify-content:center}
.cta-band .btn-outline{color:#fff;border-color:rgba(255,255,255,.6)}
.cta-band .btn-outline:hover{background:rgba(255,255,255,.14)}

/* placeholders */
.ph-card{background:var(--grad);border-radius:var(--radius);color:#fff;display:flex;align-items:center;
  justify-content:center;text-align:center;padding:24px;position:relative;overflow:hidden;min-height:120px}
.ph-card::after{content:"";position:absolute;inset:0;background:
  repeating-linear-gradient(45deg,rgba(255,255,255,.06) 0 12px,transparent 12px 24px)}
.ph-card .ph-cap{position:relative;font-weight:600;font-size:.92rem;opacity:.95}
.gallery-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.gallery-grid .ph-card{aspect-ratio:1/1}

/* footer */
.site-footer{background:var(--deep);color:#dbeeee}
.footer-top{background:var(--teal)}
.footer-top-in{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:16px;padding:18px 0}
.footer-top-in p{margin:0;color:#fff;font-weight:600;display:flex;align-items:center;gap:10px}
.footer-top-in .ic{color:#fff}
.footer-top .btn-wa{background:#fff;color:var(--deep)}
.footer-top .btn-wa:hover{background:var(--soft)}
.footer-cols{display:grid;grid-template-columns:1.4fr 1fr 1fr 1.1fr;gap:34px;padding:54px 22px}
.footer-col h4{color:#fff;font-size:1rem;margin-bottom:1em}
.footer-mark{width:54px;height:54px;border-radius:13px;display:block;margin-bottom:14px}
.footer-tag{font-weight:800;color:var(--bright);font-size:1.1rem;margin:0 0 .5em}
.footer-desc{color:#bfe0e0;font-size:.9rem}
.footer-social{display:flex;gap:11px;margin-top:18px}
.footer-social a{width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;
  background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18);color:#dbeeee;
  transition:background .2s ease,color .2s ease,transform .15s ease}
.footer-social a:hover{background:var(--bright);color:var(--deep);transform:translateY(-2px)}
.footer-social svg{width:19px;height:19px}
.footer-links{list-style:none;margin:0;padding:0;display:grid;gap:9px}
.footer-links a,.footer-contact a{color:#cfe8e8}
.footer-links a:hover,.footer-contact a:hover,.footer-getintouch:hover{color:#fff}
.footer-getintouch{color:var(--bright);font-weight:700}
.footer-contact{list-style:none;margin:0;padding:0;display:grid;gap:12px}
.footer-contact li{display:flex;gap:11px;align-items:flex-start;font-size:.9rem;color:#cfe8e8}
.footer-contact .ic{color:var(--bright);width:20px;height:20px;flex:none;margin-top:1px}
.legal-bar{border-top:1px solid rgba(255,255,255,.12)}
.legal-in{display:flex;flex-wrap:wrap;justify-content:space-between;gap:8px;padding:18px 22px;font-size:.82rem;color:#a9d3d3}
.legal-in a{color:#cfe8e8}
.legal-fine{margin:0}

/* floating whatsapp */
.float-wa{position:fixed;right:20px;bottom:20px;width:58px;height:58px;border-radius:50%;
  background:var(--teal);color:#fff;display:flex;align-items:center;justify-content:center;z-index:90;
  box-shadow:0 12px 30px -8px rgba(14,86,96,.6);transition:transform .15s ease,background .2s ease}
.float-wa:hover{transform:scale(1.08);background:var(--deep)}
.float-wa .wa-ic{width:32px;height:32px}

/* breadcrumb */
.breadcrumb{font-size:.85rem;color:var(--muted);padding:18px 0 0}
.breadcrumb a{color:var(--teal)}

/* page hero (inner) */
.page-hero{background:var(--grad);color:#fff;padding:64px 0 56px;text-align:center}
.page-hero h1{color:#fff;font-size:clamp(2rem,4.6vw,3rem);margin-bottom:.3em}
.page-hero p{color:#e7fafa;max-width:680px;margin:0 auto;font-size:1.1rem}
.page-hero .eyebrow{color:var(--bright)}

/* problem detail blocks (solutions) */
.prob-block{display:grid;grid-template-columns:auto 1fr;gap:22px;background:#fff;border:1px solid var(--line);
  border-radius:var(--radius);padding:26px;box-shadow:var(--shadow-sm)}
.prob-block .card-icon{margin:0}
.prob-meta{display:grid;gap:8px;margin:6px 0 14px}
.prob-meta div{font-size:.92rem;color:var(--muted)}
.prob-meta b{color:var(--deep)}
.prob-products{display:flex;flex-wrap:wrap;gap:10px}
.pill{display:inline-flex;align-items:center;gap:7px;border:1px solid var(--teal);color:var(--deep);
  padding:7px 14px;border-radius:999px;font-weight:600;font-size:.86rem;background:var(--wash)}
.pill .ic{width:16px;height:16px;color:var(--teal)}

/* steps */
.steps{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;counter-reset:step}
.step{background:#fff;border:1px solid var(--line);border-radius:14px;padding:24px;position:relative}
.step::before{counter-increment:step;content:counter(step);position:absolute;top:-16px;left:24px;
  width:38px;height:38px;border-radius:50%;background:var(--teal);color:#fff;font-weight:800;
  display:flex;align-items:center;justify-content:center}
.step h3{margin:10px 0 .3em;font-size:1.05rem}
.step p{margin:0;color:var(--muted);font-size:.92rem}

/* checklist */
.checklist{list-style:none;margin:0;padding:0;display:grid;gap:14px}
.checklist li{display:flex;gap:12px;align-items:flex-start}
.checklist .ic{color:var(--teal);flex:none;margin-top:2px}
.checklist b{color:var(--deep)}

/* lifecycle */
.lifecycle{display:flex;flex-wrap:wrap;gap:14px;justify-content:center}
.life-stage{flex:1;min-width:160px;background:#fff;border:1px solid var(--line);border-radius:14px;padding:20px;text-align:center}
.life-stage .ic{color:var(--teal);width:30px;height:30px;margin:0 auto 8px}
.life-stage h3{font-size:1rem;margin:0 0 .2em}
.life-stage p{font-size:.85rem;color:var(--muted);margin:0}

/* faq */
.faq{max-width:820px;margin:0 auto;display:grid;gap:12px}
.faq-item{background:#fff;border:1px solid var(--line);border-radius:14px;overflow:hidden}
.faq-q{width:100%;text-align:left;background:none;border:0;cursor:pointer;padding:20px 22px;
  font-weight:700;color:var(--deep);font-size:1.02rem;display:flex;justify-content:space-between;gap:14px;align-items:center}
.faq-q .tw{transition:transform .2s ease;color:var(--teal);font-size:1.4rem;line-height:1}
.faq-item.open .faq-q .tw{transform:rotate(45deg)}
.faq-a{padding:0 22px 20px;color:var(--muted)}
.js-on .faq-a{max-height:0;padding:0 22px;overflow:hidden;transition:max-height .25s ease,padding .25s ease}
.js-on .faq-item.open .faq-a{max-height:600px;padding:0 22px 20px}

/* product detail */
.pd-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:40px;align-items:start}
.pd-hero-thumb{background:var(--grad);border-radius:var(--radius);min-height:260px;color:#fff;
  display:flex;align-items:center;justify-content:center}
.pd-hero-thumb .ic{width:90px;height:90px}
.when-chips{display:flex;flex-wrap:wrap;gap:9px;margin:14px 0 0}
.dosage-card{background:var(--grad);color:#fff;border-radius:var(--radius);padding:26px;margin:24px 0}
.dosage-card h3{color:#fff;margin-bottom:.3em}
.dosage-card p{margin:0;color:#eafbfb}
.meta-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:24px 0}
.meta-grid .card{padding:18px;box-shadow:none}
.meta-grid h4{margin:0 0 .2em;font-size:.78rem;text-transform:uppercase;letter-spacing:.07em;color:var(--teal)}
.meta-grid p{margin:0;color:var(--muted);font-size:.92rem}
.comp-table{width:100%;border-collapse:collapse;background:#fff;border:1px solid var(--line);border-radius:var(--radius);overflow:hidden}
.comp-table th,.comp-table td{text-align:left;padding:14px 18px;border-bottom:1px solid var(--line);font-size:.95rem}
.comp-table th{background:var(--wash);color:var(--deep);font-weight:700}
.comp-table tr:last-child td{border-bottom:0}
.comp-table td:first-child{font-weight:600;color:var(--deep)}
.disclaimer{background:var(--wash);border:1px solid var(--line);border-left:4px solid var(--teal);
  border-radius:10px;padding:16px 18px;color:var(--muted);font-size:.9rem;margin-top:24px}

/* network map */
.network-grid{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:start}
.map-wrap{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:20px}
.map-wrap svg{width:100%;height:auto}
.map-legend{display:flex;flex-wrap:wrap;gap:16px;margin-top:14px;font-size:.85rem;color:var(--muted)}
.map-legend span{display:inline-flex;align-items:center;gap:7px}
.lg-swatch{width:16px;height:16px;border-radius:4px;display:inline-block}
.region{background:#fff;border:1px solid var(--line);border-radius:14px;padding:20px;margin-bottom:16px}
.region h3{font-size:1.05rem;margin:0 0 4px;display:flex;align-items:center;gap:10px}
.region .status{font-size:.7rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em;padding:3px 10px;border-radius:999px}
.region .status.active{background:var(--soft);color:var(--deep)}
.region .status.upcoming{background:var(--bright);color:var(--deep)}
.area-chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:10px}
.area-chips span{background:var(--wash);border:1px solid var(--line);color:var(--muted);
  font-size:.82rem;padding:5px 11px;border-radius:999px}

/* forms */
.form{background:#fff;border:1px solid var(--line);border-radius:var(--radius);padding:28px;box-shadow:var(--shadow-sm)}
.field{margin-bottom:16px}
.field label{display:block;font-weight:600;color:var(--deep);margin-bottom:6px;font-size:.92rem}
.field input,.field select,.field textarea{width:100%;padding:12px 14px;border:1px solid var(--line);
  border-radius:10px;font-family:inherit;font-size:.96rem;color:var(--ink);background:var(--wash)}
.field input:focus,.field select:focus,.field textarea:focus{border-color:var(--teal);background:#fff}
.field textarea{min-height:110px;resize:vertical}
.form .note{font-size:.82rem;color:var(--muted);margin:6px 0 0}

/* legal pages */
.legal-doc{max-width:820px;margin:0 auto}
.legal-doc h2{margin-top:1.6em;font-size:1.3rem}
.legal-doc p,.legal-doc li{color:var(--muted)}

/* reveal animation (only under .js-on) */
.js-on .reveal{opacity:0;transform:translateY(26px)}
.js-on .reveal.in{opacity:1;transform:none;transition:opacity .6s ease,transform .6s ease}
@media (prefers-reduced-motion:reduce){
  .js-on .reveal{opacity:1;transform:none}
  .hero canvas{display:none}
}

/* responsive */
@media (max-width:980px){
  .grid-4,.problem-grid,.segment-grid,.stats,.steps,.gallery-grid{grid-template-columns:repeat(2,1fr)}
  .grid-3{grid-template-columns:repeat(2,1fr)}
  .split,.pd-grid,.network-grid{grid-template-columns:1fr}
  .footer-cols{grid-template-columns:1fr 1fr}
}
@media (max-width:760px){
  .nav-links,.nav-cta{display:none}
  .hamburger{display:flex}
  .nav{height:64px}
  main{padding-top:64px}
  .hero{margin-top:-64px;padding-top:120px}
  .grid-2,.grid-3,.grid-4,.problem-grid,.segment-grid,.stats,.steps,.gallery-grid,.meta-grid{grid-template-columns:1fr}
  .footer-cols{grid-template-columns:1fr;gap:28px;padding:40px 22px}
  .section{padding:54px 0}
  .prob-block{grid-template-columns:1fr}
}
"""

# ---------------------------------------------------------------------------
# 7) JAVASCRIPT  (progressive enhancement only — site works fully without it)
# ---------------------------------------------------------------------------

JS = r"""// Meezab Z. International — progressive enhancement
(function () {
  'use strict';

  // Footer year
  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  // Sticky header: scrolled + at-top (home hero) states
  var header = document.getElementById('siteHeader');
  var isHome = document.body.classList.contains('home');
  function onScroll() {
    if (!header) return;
    var s = window.scrollY || window.pageYOffset;
    header.classList.toggle('scrolled', s > 8);
    if (isHome) header.classList.toggle('at-top', s < 60);
  }
  if (isHome && header) header.classList.add('at-top');
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Mobile menu
  var burger = document.getElementById('hamburger');
  var menu = document.getElementById('mobileMenu');
  var scrim = document.getElementById('scrim');
  var close = document.getElementById('mmClose');
  function openMenu() {
    if (!menu) return;
    menu.hidden = false; scrim.hidden = false;
    requestAnimationFrame(function () { document.body.style.overflow = 'hidden'; });
    burger.setAttribute('aria-expanded', 'true');
  }
  function closeMenu() {
    if (!menu) return;
    menu.hidden = true; scrim.hidden = true;
    document.body.style.overflow = '';
    burger.setAttribute('aria-expanded', 'false');
  }
  if (burger) burger.addEventListener('click', openMenu);
  if (close) close.addEventListener('click', closeMenu);
  if (scrim) scrim.addEventListener('click', closeMenu);
  if (menu) menu.querySelectorAll('a').forEach(function (a) { a.addEventListener('click', closeMenu); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeMenu(); });

  // Reveal on scroll
  var reveals = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('in'); });
  }

  // Count-up stats
  var nums = document.querySelectorAll('[data-count]');
  function countUp(el) {
    var raw = el.getAttribute('data-count');
    var target = parseInt(raw, 10);
    if (isNaN(target)) { el.textContent = raw; return; }
    var suffix = el.getAttribute('data-suffix') || '';
    var prefix = el.getAttribute('data-prefix') || '';
    var start = null, dur = 1200;
    function tick(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      el.textContent = prefix + Math.floor(p * target) + suffix;
      if (p < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }
  if (nums.length && 'IntersectionObserver' in window) {
    var io2 = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { countUp(en.target); io2.unobserve(en.target); }
      });
    }, { threshold: 0.5 });
    nums.forEach(function (el) { io2.observe(el); });
  }

  // Product filter
  var filterBtns = document.querySelectorAll('.filter-btn');
  var cards = document.querySelectorAll('.product-card[data-cat]');
  filterBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      var f = btn.getAttribute('data-filter');
      filterBtns.forEach(function (b) { b.classList.toggle('active', b === btn); });
      cards.forEach(function (c) {
        var show = (f === 'all' || c.getAttribute('data-cat') === f);
        c.style.display = show ? '' : 'none';
      });
    });
  });

  // FAQ accordion
  document.querySelectorAll('.faq-q').forEach(function (q) {
    q.addEventListener('click', function () {
      q.parentElement.classList.toggle('open');
    });
  });

  // Forms -> WhatsApp prefill
  document.querySelectorAll('form.wa-form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var lines = [];
      var title = form.getAttribute('data-title');
      if (title) { lines.push(title); lines.push(''); }
      form.querySelectorAll('input,select,textarea').forEach(function (f) {
        if (!f.name || !f.value) return;
        var label = f.getAttribute('data-label') || f.name;
        lines.push(label + ': ' + f.value);
      });
      var num = form.getAttribute('data-wa') || '923336875033';
      var url = 'https://wa.me/' + num + '?text=' + encodeURIComponent(lines.join('\n'));
      window.open(url, '_blank', 'noopener');
    });
  });

  // Hero canvas — teal particle network
  var canvas = document.getElementById('heroCanvas');
  if (canvas && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var ctx = canvas.getContext('2d');
    var pts = [], W, H, raf;
    function size() {
      W = canvas.width = canvas.offsetWidth;
      H = canvas.height = canvas.offsetHeight;
      var n = Math.min(70, Math.floor(W / 22));
      pts = [];
      for (var i = 0; i < n; i++) {
        pts.push({ x: Math.random() * W, y: Math.random() * H,
          vx: (Math.random() - 0.5) * 0.4, vy: (Math.random() - 0.5) * 0.4 });
      }
    }
    function draw() {
      ctx.clearRect(0, 0, W, H);
      for (var i = 0; i < pts.length; i++) {
        var p = pts[i];
        p.x += p.vx; p.y += p.vy;
        if (p.x < 0 || p.x > W) p.vx *= -1;
        if (p.y < 0 || p.y > H) p.vy *= -1;
        ctx.beginPath();
        ctx.arc(p.x, p.y, 2, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(212,236,236,0.9)';
        ctx.fill();
        for (var j = i + 1; j < pts.length; j++) {
          var q = pts[j], dx = p.x - q.x, dy = p.y - q.y, d = Math.sqrt(dx * dx + dy * dy);
          if (d < 130) {
            ctx.beginPath();
            ctx.moveTo(p.x, p.y); ctx.lineTo(q.x, q.y);
            ctx.strokeStyle = 'rgba(127,214,214,' + (0.5 - d / 260) + ')';
            ctx.lineWidth = 1;
            ctx.stroke();
          }
        }
      }
      if (running) raf = requestAnimationFrame(draw);
    }
    var running = false;
    function start() { if (!running) { running = true; raf = requestAnimationFrame(draw); } }
    function stop() { running = false; cancelAnimationFrame(raf); }
    size(); start();
    window.addEventListener('resize', function () { stop(); size(); start(); });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(function (e) {
        if (e[0].isIntersecting && !document.hidden) start(); else stop();
      }, { threshold: 0 }).observe(canvas);
    }
    document.addEventListener('visibilitychange', function () {
      if (document.hidden) stop(); else start();
    });
  }
})();
"""

# ---------------------------------------------------------------------------
# 8) SHARED SECTION HELPERS
# ---------------------------------------------------------------------------

import re

PROBLEM_ICONS = ["sun", "gut", "drop", "flask", "lungs", "kidney", "egg"]
SEGMENT_ICONS = {"Poultry": "egg", "Livestock": "leaf", "Pets": "hands", "Aqua": "drop"}


def slugify(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


def stat_item(value, label):
    inner, attrs = value, ""
    if value.endswith("+") and value[:-1].isdigit():
        attrs = f' data-count="{value[:-1]}" data-suffix="+"'
    elif value.endswith("%") and value[:-1].isdigit():
        attrs = f' data-count="{value[:-1]}" data-suffix="%"'
    elif value.isdigit():
        attrs = f' data-count="{value}"'
    return (f'<div class="stat"><div class="stat-num"{attrs}>{inner}</div>'
            f'<div class="stat-label">{label}</div></div>')


def stats_row():
    return '<div class="stats">' + "".join(stat_item(v, l) for v, l in STATS) + "</div>"


def ph(caption, cls=""):
    return f'<div class="ph-card {cls}"><span class="ph-cap">{caption}</span></div>'


def segments_section(heading=True):
    cards = ""
    for name, status, desc in SEGMENTS:
        now = status == "Now"
        tag = (f'<span class="tag-now">Now</span>' if now else f'<span class="tag-soon">Coming Soon</span>')
        cards += f"""<div class="segment-card {'now' if now else ''} reveal">
      <span class="seg-ic">{icon(SEGMENT_ICONS.get(name, 'check'))}</span>
      {tag}<h3>{name}</h3><p>{desc}</p>
    </div>"""
    head = ""
    if heading:
        head = f"""<div class="section-head reveal">{eyebrow('Our Segments')}
      <h2 class="h2">Built around animal health</h2>
      <p class="sub">Leading with poultry today — and growing into more of animal health over time.</p></div>"""
    return f'<section class="section wash"><div class="container">{head}<div class="segment-grid">{cards}</div></div></section>'


def principals_cards():
    out = ""
    for slug_, pr in PRINCIPALS.items():
        out += f"""<div class="principal-card reveal">
      <div class="principal-head">
        <span class="principal-flag">{icon('globe')}</span>
        <div><h3>{pr['name']}</h3><span class="cert-badge">{icon('award')} {pr['cert']} · {pr['country']}</span></div>
      </div>
      <p>{pr['intro']}</p>
      <a class="card-link" href="{slug_}.html">View Principal <span aria-hidden="true">→</span></a>
    </div>"""
    return f'<div class="grid grid-2">{out}</div>'


def leadership_cards():
    out = ""
    for name, role, desc, img in LEADERSHIP:
        out += f"""<div class="leader-card reveal">
      <img class="leader-photo-img" src="assets/img/{quote(img)}" alt="{name} — {role}, Meezab Z. International" loading="lazy">
      <div class="leader-body">
        <h3>{name}</h3>
        <div class="leader-role">{role}</div>
        <p>{desc}</p>
      </div>
    </div>"""
    return f'<div class="grid grid-2">{out}</div>'


def map_svg():
    """Inline the real geographic Pakistan distribution map (assets/img/pakistan-map.svg).
    The SVG is self-contained (its own <style> + hatch <pattern id="upcoming">) and is
    inlined — not <img>'d — so the district hover states work. District classes:
    .sv = served (teal), .ns = other districts, .up = upcoming (hatched). Recolour the
    map by re-running _extract_map.py, or edit the .svg directly."""
    path = os.path.join(OUT, "assets", "img", "pakistan-map.svg")
    with open(path, encoding="utf-8") as f:
        svg = f.read()
    return re.sub(r"^\s*<\?xml[^>]*\?>\s*", "", svg)


def map_legend():
    return ('<div class="map-legend">'
            '<span><i class="lg-swatch" style="background:#187986"></i> Areas we serve</span>'
            '<span><i class="lg-swatch" style="background:repeating-linear-gradient('
            '45deg,#5FC8CB,#5FC8CB 3px,#0E5660 3px,#0E5660 4px)"></i> '
            'Upcoming — available for distribution</span>'
            '<span><i class="lg-swatch" style="background:#D2EBEE"></i> Other districts</span>'
            '<span>★ Multan — Head Office</span></div>')


# ---------------------------------------------------------------------------
# 9) PAGE BUILDERS
# ---------------------------------------------------------------------------

def page_home():
    # 5. Why cards
    why_icons = ["award", "compass", "chat"]
    why = "".join(
        f"""<div class="card reveal"><div class="card-icon">{icon(why_icons[i])}</div>
        <h3>{t}</h3><p>{d}</p></div>""" for i, (t, d) in enumerate(WHY_CARDS))

    # 6. Problem grid
    probs = ""
    for i, pr in enumerate(PROBLEMS):
        probs += f"""<a class="problem-card reveal" href="solutions.html#{slugify(pr['title'])}">
      <div class="card-icon">{icon(PROBLEM_ICONS[i])}</div>
      <h3>{pr['title']}</h3>
      <p style="color:var(--muted);font-size:.88rem;margin:0">{pr['signs']}</p>
      <span class="season">{pr['season']}</span></a>"""

    # 7. Featured products
    feats = "".join(product_card(p) for p in PRODUCTS if p["featured"])

    # 12. Testimonials
    tcards = ""
    for quote, who, where in TESTIMONIALS:
        av = "".join(w[0] for w in who.split()[:2]).upper()
        tcards += f"""<div class="quote-card reveal"><div class="mark">&ldquo;</div>
      <p>{quote}</p><div class="quote-by"><span class="quote-av">{av}</span>
      <span><b>{who}</b><span>{where}</span></span></div></div>"""

    hero_lead = ("Internationally certified WHO-GMP &amp; HACCP-GMP animal-health products, "
                 "delivered to 100+ areas across Pakistan — currently specialising in poultry.")

    body = f"""
<section class="hero">
  <canvas id="heroCanvas" aria-hidden="true"></canvas>
  <div class="hero-glow" aria-hidden="true"></div>
  <div class="container hero-inner">
    <span class="hero-badge"><span class="brand-mark">{LOGO_SVG}</span><span>{SLOGAN}</span></span>
    <p class="slogan">Importer &amp; Distributor of Certified Animal Health</p>
    <h1>{MASTER_TAG}</h1>
    <p class="lead">{hero_lead}</p>
    <div class="hero-cta">
      {wa_btn("WhatsApp Us Now", "Hi Meezab Z., I'd like to know more about your products.", big=True)}
      {link_btn("Explore Products", "products.html", outline=True, big=True)}
    </div>
    <div class="trust-chips">
      <span class="chip">{icon('award')} WHO-GMP</span>
      <span class="chip">{icon('award')} HACCP-GMP</span>
      <span class="chip">{icon('pin')} 100+ areas</span>
      <span class="chip">{icon('shield')} Certified sourcing</span>
    </div>
  </div>
</section>

<section class="trust-strip"><div class="container">
  <span class="trust-item">{icon('award')} REEFCO · WHO-GMP · Jordan</span>
  <span class="trust-item">{icon('award')} Lexington · HACCP-GMP · Singapore</span>
  <span class="trust-item">{icon('pin')} 100+ areas across Pakistan</span>
  <span class="trust-item">{icon('shield')} 100% certified sourcing</span>
</div></section>

<section class="section"><div class="container split">
  <div class="reveal">
    {eyebrow(SLOGAN)}
    <h2 class="h2">Trusted animal health, backed by global science</h2>
    <p style="color:var(--muted);font-size:1.06rem">Meezab Z. International is an importer and distributor of
      internationally certified animal-health products, currently specialising in poultry. Since 2014 we’ve
      connected Pakistani farms with certified science from trusted global principals.</p>
    {link_btn("Learn more about us", "about.html", outline=True, arrow=True)}
  </div>
  <div class="reveal">{stats_row()}</div>
</div></section>

<section class="section wash"><div class="container">
  <div class="section-head reveal">{eyebrow('Why Meezab Z')}
    <h2 class="h2">Built for one job — healthier flocks</h2>
    <p class="sub">A focused, certified, problem-first approach to animal health.</p></div>
  <div class="grid grid-3">{why}</div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head reveal">{eyebrow('Solutions')}
    <h2 class="h2">Find your flock’s problem</h2>
    <p class="sub">Seven everyday shed problems — and the certified products matched to each.</p></div>
  <div class="problem-grid">{probs}</div>
  <div class="center mt reveal">{link_btn("See all solutions", "solutions.html", outline=True, arrow=True)}</div>
</div></section>

<section class="section wash"><div class="container">
  <div class="section-head reveal">{eyebrow('Top Sellers')}
    <h2 class="h2">Trusted in the shed</h2>
    <p class="sub">A few of the certified products farmers reach for most.</p></div>
  <div class="grid grid-4">{feats}</div>
  <div class="center mt reveal">{link_btn("Browse all products", "products.html", outline=True, arrow=True)}</div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head reveal">{eyebrow('Our Principals')}
    <h2 class="h2">Certified science from trusted partners</h2>
    <p class="sub">We are the exclusive Pakistan distributor for two internationally certified principals.</p></div>
  {principals_cards()}
</div></section>

<section class="section wash"><div class="container">
  <div class="section-head reveal">{eyebrow('Leadership')}
    <h2 class="h2">A team rooted in poultry</h2>
    <p class="sub">Industry experience across imports, supply chain, field and technical engagement.</p></div>
  {leadership_cards()}
  <div class="center mt reveal">{link_btn("More about the team", "about.html", outline=True, arrow=True)}</div>
</div></section>

{segments_section()}

<section class="section"><div class="container">
  <div class="section-head reveal">{eyebrow('Distribution Network')}
    <h2 class="h2">100+ areas across Pakistan</h2>
    <p class="sub">Active across Punjab, Sindh and Balochistan — with Khyber Pakhtunkhwa upcoming.</p></div>
  <div class="network-grid">
    <div class="map-wrap reveal">{map_svg()}
      {map_legend()}
    </div>
    <div class="reveal">
      <h3>Reaching farms in every active province</h3>
      <p style="color:var(--muted)">From our Multan headquarters, our distributor network serves Southern &amp;
        Central Punjab, Northern Punjab &amp; the Capital, and Sindh &amp; Balochistan — with Khyber Pakhtunkhwa
        coming next.</p>
      {link_btn("See full network", "network.html", outline=True, arrow=True)}
    </div>
  </div>
</div></section>

<section class="section wash"><div class="container">
  <div class="section-head reveal">{eyebrow('Testimonials')}
    <h2 class="h2">Trusted in the shed</h2>
    <p class="sub">Placeholder quotes — real testimonials coming soon.</p></div>
  <div class="grid grid-3">{tcards}</div>
</div></section>

{cta_band("Grow with a certified animal-health partner",
          "Become a Meezab Z. distributor, or message us to match the right product to your flock’s problem.")}
"""
    return doc("Meezab Z. International — Science That Works.",
               "Importer & distributor of internationally certified animal-health products in Pakistan, "
               "currently specialising in poultry. WHO-GMP & HACCP-GMP principals, 100+ areas.",
               body, "index.html", body_class="home")


def page_about():
    defines_icons = ["compass", "shield", "check", "truck"]
    defines = "".join(
        f"""<div class="card reveal"><div class="card-icon">{icon(defines_icons[i])}</div>
        <h3>{t}</h3><p>{d}</p></div>""" for i, (t, d) in enumerate(DEFINES))
    values_icons = ["shield", "flask", "leaf", "check"]
    values = "".join(
        f"""<div class="card reveal"><div class="card-icon">{icon(values_icons[i])}</div>
        <h3>{t}</h3><p>{d}</p></div>""" for i, (t, d) in enumerate(VALUES))
    framework = "".join(f"""<li>{icon('check')}<span><b>{b}</b> — {d}</span></li>""" for b, d in [
        ("Listen to the shed", "We start with the farmer’s real problem, not a catalogue."),
        ("Source certified science", "We import only from WHO-GMP and HACCP-GMP principals."),
        ("Match the protocol", "We map each product to the problem it actually solves."),
        ("Support in the field", "Our team stays reachable on WhatsApp and on the ground."),
    ])

    body = f"""
<section class="page-hero">{eyebrow('About Meezab Z. International')}
  <div class="container"><h1>{SLOGAN}</h1>
  <p>An importer and distributor of internationally certified animal-health products, currently specialising in poultry — since 2014.</p></div>
</section>

<section class="section"><div class="container split">
  <div class="reveal">
    <h2 class="h2">Who we are</h2>
    <p style="color:var(--muted);font-size:1.05rem">Meezab Z. International imports and distributes internationally
      certified animal-health products across Pakistan. We currently specialise in poultry — broilers, layers and
      breeders — and partner exclusively with certified global principals. We are an importer and distributor: our
      principals manufacture to international standards, and we bring that certified science to the Pakistani farm.</p>
    <p style="color:var(--muted);font-size:1.05rem">Our promise is simple — {SLOGAN.lower()}.</p>
  </div>
  <div class="reveal">{stats_row()}</div>
</div></section>

<section class="section wash"><div class="container split">
  <div class="reveal"><img class="img-card" src="assets/img/Leaders%20Group%20Photo.jpg"
    alt="The Meezab Z. International leadership team" loading="lazy" width="1280" height="853"></div>
  <div class="reveal">
    {eyebrow('History & Origin')}
    <h2 class="h2">From Multan, since 2014</h2>
    <p style="color:var(--muted)">Founded on 18 October 2014 in Multan, Meezab Z. International began with a clear
      idea: bring internationally certified animal-health science to Pakistani poultry farmers, honestly and
      reliably. From a single city, our certified range now reaches 100+ areas across the country.</p>
  </div>
</div></section>

<section class="cta-band reveal"><div class="container">
  <h2>Built on Science. Focused on Results.</h2>
  <p>Certified sourcing, problem-first protocols, and support that reaches the shed.</p>
</div></section>

<section class="section"><div class="container">
  <div class="section-head reveal">{eyebrow('What Defines Us')}<h2 class="h2">Four things we never compromise on</h2></div>
  <div class="grid grid-4">{defines}</div>
</div></section>

<section class="section wash"><div class="container split">
  <div class="reveal">{eyebrow('How We Work')}<h2 class="h2">A simple, repeatable framework</h2>
    <p style="color:var(--muted)">Every recommendation follows the same path — from the farmer’s problem to a certified solution.</p>
    <ul class="checklist">{framework}</ul></div>
  <div class="reveal"><img class="img-card" src="assets/img/Team%20Group%20Photo.jpg"
    alt="The Meezab Z. International field and technical team" loading="lazy" width="915" height="660"></div>
</div></section>

<section class="section"><div class="container">
  <div class="grid grid-2">
    <div class="card reveal"><div class="card-icon">{icon('compass')}</div><h3>Our Mission</h3>
      <p>To protect and improve animal health in Pakistan by delivering internationally certified products and
        honest, problem-first support — starting with poultry.</p></div>
    <div class="card reveal"><div class="card-icon">{icon('globe')}</div><h3>Our Vision</h3>
      <p>To be Pakistan’s most trusted partner in animal health — growing from poultry into livestock, pets and
        aqua, without ever compromising on certified science.</p></div>
  </div>
</div></section>

<section class="section wash"><div class="container">
  <div class="section-head reveal">{eyebrow('Our Values')}<h2 class="h2">What we stand for</h2></div>
  <div class="grid grid-4">{values}</div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head reveal">{eyebrow('Our Principals')}<h2 class="h2">Certified science from trusted partners</h2></div>
  {principals_cards()}
</div></section>

<section class="section wash"><div class="container">
  <div class="section-head reveal">{eyebrow('Leadership & Management')}<h2 class="h2">The team behind Meezab Z</h2></div>
  {leadership_cards()}
</div></section>

{segments_section()}

<section class="section"><div class="container split">
  <div class="reveal">{eyebrow('Future Outlook')}<h2 class="h2">Poultry-led, and growing</h2>
    <p style="color:var(--muted)">We lead with poultry today because that’s where we deliver the most value. But
      animal health is bigger than one segment — and so is our ambition. Livestock, pets and aqua are on our
      roadmap, and our certified, problem-first model is built to grow with them.</p>
    {link_btn("Talk to us", "contact.html", outline=True, arrow=True)}
  </div>
  <div class="reveal"><img class="img-card" src="assets/img/Chicken.jpg"
    alt="Poultry — Meezab Z. International’s flagship animal-health segment" loading="lazy" width="720" height="716"></div>
</div></section>

{cta_band("Partner with a certified animal-health distributor",
          "Whether you farm, distribute or advise — we’d love to work with you.")}
"""
    return doc("About — Meezab Z. International",
               "Meezab Z. International is an importer and distributor of internationally certified animal-health "
               "products, currently specialising in poultry. Founded 2014 in Multan.",
               body, "about.html")


def page_solutions():
    blocks = ""
    for i, pr in enumerate(PROBLEMS):
        pills = "".join(
            f'<a class="pill" href="product-{s}.html">{icon("bottle")} {PRODUCT_BY_SLUG[s]["name"]}</a>'
            for s in pr["products"])
        blocks += f"""<div class="prob-block reveal" id="{slugify(pr['title'])}">
      <div class="card-icon">{icon(PROBLEM_ICONS[i])}</div>
      <div>
        <h3>{pr['title']}</h3>
        <div class="prob-meta">
          <div><b>Signs:</b> {pr['signs']}</div>
          <div><b>Cause:</b> {pr['cause']}</div>
          <div><b>Season:</b> {pr['season']}</div>
        </div>
        <div style="font-weight:700;color:var(--deep);margin-bottom:8px">Matched protocol</div>
        <div class="prob-products">{pills}</div>
      </div>
    </div>"""

    steps = "".join(f"""<div class="step reveal"><h3>{t}</h3><p>{d}</p></div>""" for t, d in [
        ("Identify the problem", "Match what you see in the shed to one of the seven core problems."),
        ("Pick the protocol", "Use the matched certified products for that problem."),
        ("Dose correctly", "Follow the label and our guidance via drinking water."),
        ("Support & monitor", "Track recovery and message us for technical help anytime."),
    ])

    life = "".join(f"""<div class="life-stage reveal">{icon(ic)}<h3>{t}</h3><p>{d}</p></div>""" for ic, t, d in [
        ("egg", "Chick & brooding", "Strong start: vitamins, gut and kidney support."),
        ("gut", "Grower", "FCR, gut health and water hygiene."),
        ("sun", "Finisher", "Heat-stress and recovery support."),
        ("award", "Lay / harvest", "Eggshell, fertility and performance."),
    ])

    faq = "".join(f"""<div class="faq-item reveal"><button class="faq-q" type="button">
      <span>{q}</span><span class="tw" aria-hidden="true">+</span></button>
      <div class="faq-a"><p>{a}</p></div></div>""" for q, a in FAQ)

    body = f"""
<section class="page-hero">{eyebrow('Solutions')}
  <div class="container"><h1>Find your flock’s problem</h1>
  <p>Seven everyday poultry problems — each with its signs, cause, season and a matched protocol of certified products.</p></div>
</section>

<section class="section"><div class="container">
  <div class="grid" style="gap:18px">{blocks}</div>
</div></section>

<section class="section wash"><div class="container">
  <div class="section-head reveal">{eyebrow('How to use the range')}<h2 class="h2">A simple four-step process</h2></div>
  <div class="steps">{steps}</div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head reveal">{eyebrow('Lifecycle')}<h2 class="h2">From chick to harvest</h2>
    <p class="sub">Support that matches each stage of the flock.</p></div>
  <div class="lifecycle">{life}</div>
</div></section>

<section class="section wash"><div class="container">
  <div class="section-head reveal">{eyebrow('FAQ')}<h2 class="h2">Common questions</h2></div>
  <div class="faq">{faq}</div>
</div></section>

{cta_band("Not sure which protocol fits?",
          "Send us a photo or describe the problem on WhatsApp — we’ll guide you to the right certified product.",
          "Hi Meezab Z., I need help choosing the right product for my flock’s problem.")}
"""
    return doc("Solutions — Meezab Z. International",
               "Seven core poultry problems and the certified products matched to each — heat stress, FCR, gut "
               "health, liver, respiratory, kidney and eggshell support.",
               body, "solutions.html")


def page_products():
    cards = "".join(product_card(p) for p in PRODUCTS)
    body = f"""
<section class="page-hero">{eyebrow('Products')}
  <div class="container"><h1>Certified animal-health products</h1>
  <p>Our full poultry range from REEFCO (Jordan · WHO-GMP) and Lexington Enterprises (Singapore · HACCP-GMP).</p></div>
</section>

<section class="section"><div class="container">
  <div class="filterbar" role="group" aria-label="Filter products">
    <button class="filter-btn active" data-filter="all">All</button>
    <button class="filter-btn" data-filter="reefco">REEFCO · Jordan</button>
    <button class="filter-btn" data-filter="lexington">Lexington · Singapore</button>
  </div>
  <div class="grid grid-4">{cards}</div>
  <div class="center mt reveal">
    <p style="color:var(--muted)">Not sure what you need?</p>
    {wa_btn("Ask us on WhatsApp", "Hi Meezab Z., I'd like help choosing the right product.", big=True)}
  </div>
</div></section>
"""
    return doc("Products — Meezab Z. International",
               "Browse the certified poultry product range from REEFCO (Jordan, WHO-GMP) and Lexington Enterprises "
               "(Singapore, HACCP-GMP), distributed across Pakistan by Meezab Z. International.",
               body, "products.html")


def page_distributors():
    benefits_icons = ["award", "chat", "compass", "truck", "shield", "globe"]
    benefits = "".join(
        f"""<div class="card reveal"><div class="card-icon">{icon(benefits_icons[i])}</div>
        <h3>{t}</h3><p>{d}</p></div>""" for i, (t, d) in enumerate([
            ("Certified range", "Sell only internationally certified WHO-GMP and HACCP-GMP products."),
            ("Demand-pull support", "We build farmer awareness so product moves through your area."),
            ("Field & technical help", "Our team supports you and your customers on the ground and on WhatsApp."),
            ("Reliable supply", "Dependable stock and dispatch from our Multan base."),
            ("Territory-first approach", "We grow areas thoughtfully, respecting existing distributors."),
            ("A trusted brand", "Partner with a name farmers associate with certified science."),
        ]))
    steps = "".join(f"""<div class="step reveal"><h3>{t}</h3><p>{d}</p></div>""" for t, d in [
        ("Apply", "Send your details via the form or WhatsApp."),
        ("Talk", "We discuss your area, experience and goals."),
        ("Launch", "We set you up with products, materials and support."),
    ])
    body = f"""
<section class="page-hero">{eyebrow('Become a Distributor')}
  <div class="container"><h1>Grow your business with certified animal health</h1>
  <p>Join a growing network distributing internationally certified poultry products across Pakistan.</p>
  <div class="mt" style="display:flex;justify-content:center">{wa_btn("Apply on WhatsApp", "Hi Meezab Z., I'd like to become a distributor.", big=True)}</div></div>
</section>

<section class="section"><div class="container split">
  <div class="reveal">{eyebrow('The Idea')}<h2 class="h2">Demand-pull, not push</h2>
    <p style="color:var(--muted)">We don’t just hand you stock. We build farmer awareness around real problems and
      certified solutions — so demand pulls product through your area. You get a trusted, certified range and a
      partner that helps you sell it.</p></div>
  <div class="reveal">{ph('Distributor partnership (placeholder)', 'ph-card')}</div>
</div></section>

<section class="section wash"><div class="container">
  <div class="section-head reveal">{eyebrow('What You Get')}<h2 class="h2">Six reasons to partner with us</h2></div>
  <div class="grid grid-3">{benefits}</div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head reveal">{eyebrow('How It Works')}<h2 class="h2">Three simple steps</h2></div>
  <div class="steps" style="grid-template-columns:repeat(3,1fr)">{steps}</div>
</div></section>

<section class="section wash"><div class="container" style="max-width:920px">
  <div class="section-head reveal">{eyebrow('Your Territory')}
    <h2 class="h2">See where we’re growing</h2>
    <p class="sub">We already serve 100+ areas across Punjab, Sindh and Balochistan — and Khyber
      Pakhtunkhwa is upcoming and open for distribution. Find your area, then let’s talk.</p></div>
  <div class="map-wrap reveal">{map_svg()}</div>
  {map_legend()}
  <div class="center mt reveal">{link_btn("See the full distribution network", "network.html", outline=True, arrow=True)}</div>
</div></section>

<section class="section"><div class="container" style="max-width:760px">
  <div class="section-head reveal">{eyebrow('Apply')}<h2 class="h2">Distributor application</h2>
    <p class="sub">Fill this in and we’ll continue the conversation on WhatsApp.</p></div>
  <form class="form wa-form reveal" data-title="New distributor application (from website)" data-wa="{WA_NUMBER}">
    <div class="field"><label for="d-name">Full name</label><input id="d-name" name="name" data-label="Name" required></div>
    <div class="field"><label for="d-phone">Phone / WhatsApp</label><input id="d-phone" name="phone" data-label="Phone" required></div>
    <div class="field"><label for="d-city">City / Area</label><input id="d-city" name="city" data-label="City/Area" required></div>
    <div class="field"><label for="d-exp">Experience in poultry / distribution</label>
      <select id="d-exp" name="experience" data-label="Experience">
        <option>New to distribution</option><option>1–3 years</option><option>3–5 years</option><option>5+ years</option>
      </select></div>
    <div class="field"><label for="d-msg">Anything else?</label><textarea id="d-msg" name="message" data-label="Message"></textarea></div>
    <button class="btn btn-wa btn-lg" type="submit">{WA_GLYPH}<span>Send on WhatsApp</span></button>
    <p class="note">This opens WhatsApp with your details pre-filled — no data is stored on this site.</p>
  </form>
</div></section>

{cta_band("Ready to represent certified animal health?",
          "Apply today and let’s grow your area together.",
          "Hi Meezab Z., I'd like to become a distributor.")}
"""
    return doc("Become a Distributor — Meezab Z. International",
               "Join the Meezab Z. International distributor network and sell internationally certified poultry "
               "products across Pakistan. Demand-pull support, reliable supply, field help.",
               body, "distributors.html")


def page_contact():
    body = f"""
<section class="page-hero">{eyebrow('Contact')}
  <div class="container"><h1>Let’s talk animal health</h1>
  <p>WhatsApp is the fastest way to reach us — we respond during business hours.</p>
  <div class="mt" style="display:flex;justify-content:center">{wa_btn("Chat on WhatsApp", "Hi Meezab Z., I have an enquiry.", big=True)}</div></div>
</section>

<section class="section"><div class="container split">
  <form class="form wa-form reveal" data-title="New enquiry (from website)" data-wa="{WA_NUMBER}">
    <h2 class="h2" style="margin-top:0">Send an enquiry</h2>
    <div class="field"><label for="c-name">Full name</label><input id="c-name" name="name" data-label="Name" required></div>
    <div class="field"><label for="c-phone">Phone / WhatsApp</label><input id="c-phone" name="phone" data-label="Phone" required></div>
    <div class="field"><label for="c-city">City</label><input id="c-city" name="city" data-label="City"></div>
    <div class="field"><label for="c-msg">Your message</label><textarea id="c-msg" name="message" data-label="Message" required></textarea></div>
    <button class="btn btn-wa btn-lg" type="submit">{WA_GLYPH}<span>Send on WhatsApp</span></button>
    <p class="note">This opens WhatsApp with your message pre-filled — no data is stored on this site.</p>
  </form>
  <div class="reveal">
    <div class="card" style="margin-bottom:18px"><h3>Office</h3>
      <ul class="footer-contact" style="color:var(--muted)">
        <li>{icon('phone')}<a href="tel:{PHONE.replace('-', '')}">{PHONE}</a></li>
        <li>{icon('chat')}<a href="{WA_URL}" target="_blank" rel="noopener">{WA_DISPLAY}</a></li>
        <li>{icon('mail')}<a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li>{icon('pin')}<span>{ADDRESS}</span></li>
        <li>{icon('clock')}<span>{HOURS}</span></li>
      </ul>
    </div>
    {ph('Map pin — Multan HQ (placeholder)', 'ph-card')}
  </div>
</div></section>

{cta_band("Prefer to talk now?",
          "Tap below and message us directly on WhatsApp.",
          "Hi Meezab Z., I'd like to talk to your team.")}
"""
    return doc("Contact — Meezab Z. International",
               "Contact Meezab Z. International, Multan. WhatsApp +92 333 6875033, phone 061-2111031, "
               "email info@meezabz.com. Mon–Sat, 9 AM – 6 PM.",
               body, "contact.html")


def page_network():
    regions = ""
    for name, status, areas in REGIONS:
        chips = "".join(f"<span>{a}</span>" for a in areas)
        regions += f"""<div class="region reveal">
      <h3>{name} <span class="status {status}">{'Upcoming' if status == 'upcoming' else 'Active'}</span></h3>
      <div class="area-chips">{chips}</div></div>"""
    body = f"""
<section class="page-hero">{eyebrow('Distribution Network')}
  <div class="container"><h1>100+ areas across Pakistan</h1>
  <p>Active across Punjab, Sindh and Balochistan — with Khyber Pakhtunkhwa upcoming. Headquartered in Multan.</p></div>
</section>

<section class="section"><div class="container" style="max-width:920px">
  <div class="map-wrap reveal">{map_svg()}</div>
  {map_legend()}
</div></section>

<section class="section wash"><div class="container">
  <div class="section-head reveal">{eyebrow('Coverage by region')}
    <h2 class="h2">Where we deliver</h2>
    <p class="sub">Active across Punjab, Sindh and Balochistan — Khyber Pakhtunkhwa upcoming.</p></div>
  <div class="grid grid-2">{regions}</div>
</div></section>

{cta_band("Don’t see your area yet?",
          "We’re expanding fast. Message us and we’ll tell you about coverage near you — or how to bring Meezab Z. to your region.",
          "Hi Meezab Z., is there coverage in my area?")}
"""
    return doc("Distribution Network — Meezab Z. International",
               "Meezab Z. International serves 100+ areas across Punjab, Sindh and Balochistan, with Khyber "
               "Pakhtunkhwa upcoming. Headquartered in Multan.",
               body, "network.html")


def page_gallery():
    tiles = "".join(ph(cap) for cap in GALLERY)
    body = f"""
<section class="page-hero">{eyebrow('Gallery')}
  <div class="container"><h1>From the field</h1>
  <p>Farm visits, products and our team in action. Placeholder tiles — real photos coming soon.</p></div>
</section>

<section class="section"><div class="container">
  <div class="gallery-grid">{tiles}</div>
</div></section>

{cta_band("Want to see more?",
          "Follow our journey or get in touch — we love hearing from farmers and partners.",
          "Hi Meezab Z., I'd like to see more about your work.")}
"""
    return doc("Gallery — Meezab Z. International",
               "Photos from the field — farm visits, certified products and the Meezab Z. International team.",
               body, "gallery.html")


def page_principal(slug_):
    pr = PRINCIPALS[slug_]
    prods = [p for p in PRODUCTS if p["principal_slug"] == slug_]
    pcards = "".join(product_card(p) for p in prods)
    milestones = "".join(
        f"""<div class="step reveal"><h3>{t}</h3><p>{d}</p></div>""" for t, d in pr["milestones"])
    body = f"""
<section class="page-hero">{eyebrow('Our Principal')}
  <div class="container"><h1>{pr['name']}</h1>
  <p>{pr['intro']}</p>
  <div class="mt" style="display:flex;justify-content:center;gap:10px;flex-wrap:wrap">
    <span class="chip" style="background:rgba(255,255,255,.15);border-color:rgba(255,255,255,.3)">{icon('award')} {pr['cert']}</span>
    <span class="chip" style="background:rgba(255,255,255,.15);border-color:rgba(255,255,255,.3)">{icon('globe')} {pr['country']}</span>
  </div></div>
</section>

<section class="section"><div class="container split">
  <div class="reveal">{eyebrow('Partnership')}<h2 class="h2">Exclusive Pakistan distributor</h2>
    <p style="color:var(--muted)">Meezab Z. International is the exclusive Pakistan distributor of {pr['name']}.
      Together we bring {pr['cert']} certified science to Pakistani poultry farms — backed by field and technical support.</p>
    <p style="font-style:italic;color:var(--deep);font-weight:600">“{pr['quote']}”</p>
  </div>
  <div class="reveal">{ph(pr['name'] + ' — facility (placeholder)', 'ph-card')}</div>
</div></section>

<section class="section wash"><div class="container split">
  <div class="reveal">{ph('Quality & certification (placeholder)', 'ph-card')}</div>
  <div class="reveal">{eyebrow('About & Quality')}<h2 class="h2">Certified to international standards</h2>
    <p style="color:var(--muted)">{pr['about']}</p>
    <span class="cert-badge">{icon('award')} {pr['cert']} certified</span>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="section-head reveal">{eyebrow('What We Distribute')}<h2 class="h2">The {pr['name'].split(' — ')[0]} range</h2></div>
  <div class="grid grid-3">{pcards}</div>
</div></section>

<section class="section wash"><div class="container">
  <div class="section-head reveal">{eyebrow('Milestones')}<h2 class="h2">The partnership at a glance</h2></div>
  <div class="steps" style="grid-template-columns:repeat(4,1fr)">{milestones}</div>
</div></section>

{cta_band(f"Interested in the {pr['name'].split(' — ')[0]} range?",
          "Message us to learn which products fit your flock — or to stock them in your area.")}
"""
    return doc(f"{pr['name']} — Meezab Z. International",
               f"{pr['name']} ({pr['country']}, {pr['cert']}). Meezab Z. International is the exclusive Pakistan "
               f"distributor of {pr['name']}.",
               body, slug_ + ".html")


def page_product(p):
    when = "".join(f'<span class="chip" style="background:var(--soft);border-color:var(--line);color:var(--deep)">'
                   f'{icon("check")} {w}</span>' for w in p["when"])
    comp_rows = "".join(f"<tr><td>{c}</td><td>{r}</td></tr>" for c, r in p["composition"])
    works = "".join(product_card(PRODUCT_BY_SLUG[s]) for s in p["works_with"])
    pr = PRINCIPALS[p["principal_slug"]]

    schema = {
        "@context": "https://schema.org/", "@type": "Product", "name": p["name"],
        "description": p["what"], "category": "Animal health / Poultry",
        "brand": {"@type": "Brand", "name": p["principal"]},
        "manufacturer": {"@type": "Organization", "name": pr["name"], "address": pr["country"]},
    }
    head = '<script type="application/ld+json">' + json.dumps(schema) + "</script>\n"

    body = f"""
<section class="section" style="padding-bottom:0"><div class="container">
  <nav class="breadcrumb" aria-label="Breadcrumb">
    <a href="index.html">Home</a> · <a href="products.html">Products</a> · {p['name']}</nav>
</div></section>

<section class="section"><div class="container pd-grid">
  <div class="reveal">
    {eyebrow(p['problem'])}
    <h1 style="font-size:clamp(1.8rem,4vw,2.6rem)">{p['name']}</h1>
    <span class="badge badge-{p['cat']}">{p['principal']} · {p['origin']} · {p['cert']}</span>
    <p style="color:var(--muted);font-size:1.08rem;margin-top:16px">{p['what']}</p>
    <div style="font-weight:700;color:var(--deep);margin-top:18px">When to use</div>
    <div class="when-chips">{when}</div>
    <div class="dosage-card">
      <h3>{icon('drop')} Dosage</h3>
      <p>{p['dosage']}</p>
    </div>
    <div style="display:flex;flex-wrap:wrap;gap:12px">
      {wa_btn("Order on WhatsApp", "Hi Meezab Z., I'd like to order " + p['name'] + ".", big=True)}
      {link_btn("View principal", p['principal_slug'] + '.html', outline=True, arrow=True)}
    </div>
  </div>
  <div class="reveal">
    <div class="pd-hero-thumb">{icon('bottle')}</div>
    <div class="meta-grid">
      <div class="card"><h4>Pack</h4><p>Oral liquid solution — see label</p></div>
      <div class="card"><h4>Storage</h4><p>Cool, dry place, away from sunlight; keep closed</p></div>
      <div class="card"><h4>Principal</h4><p><a href="{p['principal_slug']}.html">{pr['name'].split(' — ')[0]}</a> · {p['cert']}</p></div>
    </div>
  </div>
</div></section>

<section class="section wash"><div class="container">
  <div class="section-head left reveal">{eyebrow('Composition')}<h2 class="h2">What’s inside</h2></div>
  <table class="comp-table reveal"><thead><tr><th>Active ingredient</th><th>Role</th></tr></thead>
    <tbody>{comp_rows}</tbody></table>
  <p class="disclaimer reveal">{icon('shield')} This information is for general guidance only. Always follow the
    product label and the advice of a qualified veterinarian. This is not a substitute for professional veterinary advice.</p>
</div></section>

<section class="section"><div class="container">
  <div class="section-head reveal">{eyebrow('Works Well With')}<h2 class="h2">Build a complete protocol</h2></div>
  <div class="grid grid-3" style="grid-template-columns:repeat(2,1fr);max-width:740px;margin:0 auto">{works}</div>
</div></section>

{cta_band(f"Need {p['name']} for your flock?",
          "Message us to order, check availability, or get dosing guidance for your situation.",
          "Hi Meezab Z., I'd like to order " + p['name'] + ".")}
"""
    return doc(f"{p['name']} — {p['principal']} · {p['cert']} | Meezab Z. International",
               f"{p['name']} by {p['principal']} ({p['origin']}, {p['cert']}): {p['what']} Distributed in "
               f"Pakistan by Meezab Z. International.",
               body, "products.html", extra_head=head)


def _legal(title, intro, sections, active):
    secs = "".join(f"<h2>{h}</h2>" + "".join(f"<p>{para}</p>" for para in paras)
                   for h, paras in sections)
    body = f"""
<section class="page-hero">{eyebrow('Legal')}
  <div class="container"><h1>{title}</h1><p>{intro}</p></div>
</section>
<section class="section"><div class="container legal-doc">
  <p style="color:var(--muted)">Last updated: June 2026.</p>
  {secs}
</div></section>
"""
    return doc(f"{title} — Meezab Z. International",
               f"{title} for Meezab Z. International.", body, active)


def page_privacy():
    return _legal(
        "Privacy Policy",
        "How Meezab Z. International handles your information.",
        [
            ("Overview", ["Meezab Z. International (“we”, “us”) respects your privacy. This website is a static, "
                          "informational site and does not run a backend database or store form submissions on our servers."]),
            ("Information we collect", ["When you use the contact or distributor forms, your details are placed into a "
                                        "pre-filled WhatsApp message that you choose to send to us. We only receive what you send. "
                                        "We do not collect personal data automatically through this site beyond what your browser and "
                                        "any embedded fonts ordinarily request."]),
            ("How we use information", ["We use the information you send us to respond to your enquiry, process distributor "
                                        "applications, and provide product guidance during business hours."]),
            ("Third-party services", ["This site loads the Inter font from Google Fonts and uses WhatsApp (Meta) for "
                                      "messaging. Their use of data is governed by their own privacy policies."]),
            ("Veterinary disclaimer", ["Product information on this site is for general guidance only and is not a substitute "
                                       "for professional veterinary advice. Always follow product labels and consult a qualified veterinarian."]),
            ("Contact", [f"For privacy questions, email {EMAIL} or call {PHONE}."]),
        ],
        "privacy.html")


def page_terms():
    return _legal(
        "Terms & Conditions",
        "The terms governing your use of this website.",
        [
            ("Acceptance", ["By using this website you agree to these terms. If you do not agree, please do not use the site."]),
            ("About us", ["Meezab Z. International is an importer and distributor of internationally certified animal-health "
                          "products in Pakistan, currently specialising in poultry. We are the exclusive Pakistan distributor of "
                          "REEFCO (Jordan) and Lexington Enterprises (Singapore)."]),
            ("Product information", ["We aim to keep product information accurate, but content is provided “as is” for general "
                                     "guidance. Composition and dosage details must always be confirmed against the product label and used "
                                     "under the advice of a qualified veterinarian."]),
            ("No medical/veterinary advice", ["Nothing on this site constitutes veterinary advice. Always consult a qualified "
                                              "veterinarian before treating animals."]),
            ("Intellectual property", ["The Meezab Z. International name, logo and site content are owned by Meezab Z. International "
                                       "and may not be used without permission."]),
            ("Governing law", ["These terms are governed by the laws of Pakistan, and any disputes are subject to the jurisdiction "
                               "of the courts of Multan, Pakistan."]),
            ("Contact", [f"Questions about these terms? Email {EMAIL} or call {PHONE}."]),
        ],
        "terms.html")


# ---------------------------------------------------------------------------
# 10) COMBINED OFFLINE PREVIEW + README + ASSET WRITERS
# ---------------------------------------------------------------------------

def complete_website(page_list):
    """A single launcher that loads each page in an iframe — for offline preview."""
    opts = "".join(f'<option value="{fn}">{label}</option>' for label, fn in page_list)
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Meezab Z. International — Complete Website (offline preview)</title>
<style>
  :root{{--teal:#187986;--deep:#0E5660;--soft:#D2EBEE}}
  *{{box-sizing:border-box}} body{{margin:0;font-family:Inter,system-ui,Arial,sans-serif;background:#F1FAFB}}
  .bar{{display:flex;align-items:center;gap:14px;flex-wrap:wrap;background:var(--deep);color:#fff;padding:12px 18px}}
  .bar b{{letter-spacing:.06em}} .bar i{{font-style:normal;opacity:.7;font-size:.85rem}}
  select{{padding:9px 12px;border-radius:9px;border:0;font:inherit;min-width:240px}}
  .frame{{width:100%;height:calc(100vh - 56px);border:0;background:#fff}}
  a.open{{color:#5FC8CB;font-weight:700;text-decoration:none;margin-left:auto}}
</style></head>
<body>
  <div class="bar">
    <b>MEEZAB Z</b><i>Complete Website — offline preview</i>
    <label for="sel" style="font-size:.85rem;opacity:.85">Page:</label>
    <select id="sel" onchange="document.getElementById('f').src=this.value">{opts}</select>
    <a class="open" id="ext" href="index.html" target="_blank" rel="noopener">Open page in new tab ↗</a>
  </div>
  <iframe class="frame" id="f" src="index.html" title="Page preview"></iframe>
  <script>
    var sel=document.getElementById('sel'),ext=document.getElementById('ext');
    sel.addEventListener('change',function(){{ext.href=sel.value;}});
  </script>
</body></html>"""


README = f"""# Meezab Z. International — Website

Static, framework-free website for **Meezab Z. International** — an importer &
distributor of internationally certified animal-health products in Pakistan,
currently specialising in poultry.

## Structure

```
index.html              Home (landing page)
about.html              About
solutions.html          Solutions (7 problems)
products.html           Products (filterable)
distributors.html       Become a distributor
contact.html            Contact
network.html            Distribution network (map + areas)
gallery.html            Gallery
principal-reefco.html   REEFCO (Jordan, WHO-GMP)
principal-lexington.html Lexington (Singapore, HACCP-GMP)
privacy.html / terms.html  Legal
product-*.html          9 product detail pages
Complete_Website.html   Offline preview launcher (all pages via a picker)
assets/css/style.css    Single stylesheet (teal tokens)
assets/js/main.js       Progressive-enhancement JS
assets/img/Logo.svg     Brand logo (user-supplied; also favicon — keep exact casing)
assets/img/pakistan-map.svg  Geographic distribution map (inlined into Home + Network)
```

## Regenerate

This site is generated by `build.py` (an authoring tool only — the emitted HTML
is what deploys). Edit the DATA / TEMPLATE sections at the top of `build.py`, then:

```
py build.py
```

(`python` may hit the Microsoft Store shim on Windows — use `py`.)

## Deploy

- **Netlify:** drag-and-drop this folder onto the Netlify dashboard. No build command.
- **cPanel / any static host:** upload the files (keep the `assets/` folder) to `public_html`.

Everything uses relative links and works from `file://` too (open `index.html`
or `Complete_Website.html` directly).

## Brand rules baked in

Teal + white only · importer & distributor (never "manufacturer") · no product
counts / no "approved" / no "Form-7" · "Distributor(s)" never "Dealer(s)" ·
WhatsApp-first CTA · honest stats · no-JS safe · future-proof (poultry-led, not
poultry-bound).
"""


def write(path, content):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)


# ---------------------------------------------------------------------------
# 11) MAIN — emit everything
# ---------------------------------------------------------------------------

def main():
    pages = []  # (label, filename) for nav of Complete_Website

    def emit(fn, html, label):
        write(fn, html)
        pages.append((label, fn))

    emit("index.html", page_home(), "Home")
    emit("about.html", page_about(), "About")
    emit("solutions.html", page_solutions(), "Solutions")
    emit("products.html", page_products(), "Products")
    emit("distributors.html", page_distributors(), "Distributors")
    emit("contact.html", page_contact(), "Contact")
    emit("network.html", page_network(), "Distribution Network")
    emit("gallery.html", page_gallery(), "Gallery")
    emit("principal-reefco.html", page_principal("principal-reefco"), "Principal — REEFCO")
    emit("principal-lexington.html", page_principal("principal-lexington"), "Principal — Lexington")
    emit("privacy.html", page_privacy(), "Privacy")
    emit("terms.html", page_terms(), "Terms")
    for p in PRODUCTS:
        emit(f"product-{p['slug']}.html", page_product(p), f"Product — {p['name']}")

    # assets (the brand logo at assets/img/Logo.svg is user-supplied and is NOT
    # generated here — build.py must never overwrite it)
    write("assets/css/style.css", CSS)
    write("assets/js/main.js", JS)

    # combined preview + readme
    write("Complete_Website.html", complete_website(pages))
    write("README.md", README)

    print(f"build.py: wrote {len(pages)} HTML pages + assets + Complete_Website.html + README.md")
    print("Done. Open index.html or Complete_Website.html.")


if __name__ == "__main__":
    main()
