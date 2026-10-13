"""Shared demo data generation functions."""
import random
from datetime import datetime, timedelta

FIRST_NAMES = ["James","Mary","John","Patricia","Robert","Jennifer","Michael","Linda","William","Elizabeth","David","Barbara","Richard","Susan","Joseph","Jessica","Thomas","Sarah","Charles","Karen","Emma","Olivia","Noah","Ava","Liam","Sophia","Ethan","Isabella","Mason","Mia","Lucas","Charlotte","Aiden","Amelia","Oliver","Harper","Elijah","Evelyn","Logan","Abigail","Cody","Madison","Ryan","Sofia","Daniel","Avery","Tyler","Ella","Aaron","Scarlett"]
LAST_NAMES = ["Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Rodriguez","Martinez","Hernandez","Lopez","Gonzalez","Wilson","Anderson","Thomas","Taylor","Moore","Jackson","Martin","Lee","Perez","Thompson","White","Harris","Sanchez","Clark","Ramirez","Lewis","Robinson","Walker","Young","Allen","King","Wright","Scott","Torres","Nguyen","Hill","Flores"]
CITIES = ["New York","Los Angeles","Chicago","Houston","Phoenix","Philadelphia","San Antonio","San Diego","Dallas","San Jose","Austin","Jacksonville","Fort Worth","Columbus","Charlotte","Indianapolis","San Francisco","Seattle","Denver","Boston","Nashville","Portland","Las Vegas","Miami","Atlanta"]
STATES = ["NY","CA","IL","TX","AZ","PA","TX","CA","TX","CA","TX","FL","TX","OH","NC","IN","CA","WA","CO","MA","TN","OR","NV","FL","GA"]
STATUS = ["active","pending","completed","cancelled","draft","archived","approved","rejected"]
PAYMENT = ["credit_card","debit_card","bank_transfer","paypal","crypto","cash"]
COLORS = ["Red","Blue","Green","Black","White","Yellow","Purple","Orange","Pink","Brown"]
SIZES = ["XS","S","M","L","XL","XXL"]

def name():
    return random.choice(FIRST_NAMES) + " " + random.choice(LAST_NAMES)

def email(fn="", ln=""):
    fn = (fn or random.choice(FIRST_NAMES)).lower()
    ln = (ln or random.choice(LAST_NAMES)).lower()
    return f"{fn}.{ln}{random.randint(1,999)}@example.com"

def phone():
    return f"+1-{random.randint(200,999)}-{random.randint(200,999)}-{random.randint(1000,9999)}"

def city():
    i = random.randint(0, len(CITIES)-1)
    return CITIES[i], STATES[i]

def address():
    c, s = city()
    streets = ["Main","Oak","Park","Elm","Maple","Cedar","Pine","Walnut","Chestnut","Birch"]
    return f"{random.randint(100,9999)} {random.choice(streets)} St, {c}, {s} {random.randint(10000,99999)}"

def date(start="2024-01-01", end="2025-12-31"):
    s = datetime.strptime(start, "%Y-%m-%d")
    e = datetime.strptime(end, "%Y-%m-%d")
    return (s + timedelta(days=random.randint(0, (e-s).days))).strftime("%Y-%m-%d")

def timestamp():
    return date() + f" {random.randint(8,22):02d}:{random.randint(0,59):02d}:{random.randint(0,59):02d}"

def price(lo=1, hi=999):
    return round(random.uniform(lo, hi), 2)

def num(lo=1, hi=100):
    return random.randint(lo, hi)

def pick(*opts):
    return random.choice(opts)

def bool_val():
    return random.choice([True, False])

def lorem(n=3):
    words = "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor in reprehenderit".split()
    return " ".join(random.sample(words, min(n, len(words))))
