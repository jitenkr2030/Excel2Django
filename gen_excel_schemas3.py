"""More domain schemas."""
import random

SCHEMAS = {
"marketing": {
    "title": "Marketing_Sales_Portal_Database",
    "sheets": {
        "Campaigns": {
            "cols": ["id","name","type","description","budget","spent","start_date","end_date","status","target_audience","platform","impressions","clicks","conversions","roas","created_at"],
            "gen": lambda i: [i, lorem(6), pick("email","social","search","display","video","influencer","content","affiliate"), lorem(15), price(1000,100000), price(500,50000), date("2025-01-01","2025-06-30"), date("2025-07-01","2025-12-31"), pick(*STATUS), pick("18-24","25-34","35-44","45-54","55+","all"), pick("Google","Facebook","Instagram","LinkedIn","Twitter","YouTube","TikTok"), num(1000,5000000), num(100,500000), num(10,50000), round(random.uniform(0.5,8.0),2), timestamp()]
        },
        "Leads": {
            "cols": ["id","first_name","last_name","email","phone","company","source","campaign_id","score","status","assigned_to","last_contact","created_at"],
            "gen": lambda i: [i, random.choice(["James","Mary","John","Patricia","Emma"]), random.choice(["Smith","Johnson","Williams","Brown"]), email(), phone(), pick("Tech Corp","Global Inc","ABC Company","XYZ Ltd","Innovation Co"), pick("website","social_media","referral","cold_call","trade_show","email","ad"), num(1,20), num(1,100), pick("new","contacted","qualified","proposal","negotiation","won","lost"), name(), timestamp(), timestamp()]
        },
        "Sales": {
            "cols": ["id","lead_id","product","amount","commission","sale_date","status","payment_terms","notes","created_at"],
            "gen": lambda i: [i, num(1,100), pick("Software License","Consulting","Training","Support Plan","Custom Solution","Annual Subscription"), price(500,50000), price(50,5000), date("2025-01-01","2025-12-31"), pick(*STATUS), pick("net_30","net_60","immediate","monthly","quarterly"), lorem(8), timestamp()]
        },
        "Email_Campaigns": {
            "cols": ["id","campaign_id","subject","sent_count","open_count","click_count","bounce_count","unsubscribe_count","sent_at","status"],
            "gen": lambda i: [i, num(1,20), lorem(6), num(100,50000), num(10,25000), num(1,5000), num(0,500), num(0,100), timestamp(), pick(*STATUS)]
        },
        "Analytics": {
            "cols": ["id","campaign_id","date","impressions","clicks","ctr","cpc","conversions","conversion_rate","cost_per_conversion","revenue","roas"],
            "gen": lambda i: [i, num(1,20), date("2025-01-01","2025-12-31"), num(100,500000), num(10,50000), round(random.uniform(0.1,10),2), round(random.uniform(0.1,50),2), num(1,5000), round(random.uniform(0.1,15),2), round(random.uniform(1,200),2), price(100,100000), round(random.uniform(0.5,10),2)]
        },
        "Social_Media": {
            "cols": ["id","platform","post_type","content","likes","shares","comments","reach","engagement_rate","posted_at","status"],
            "gen": lambda i: [i, pick("Instagram","Facebook","Twitter","LinkedIn","TikTok","YouTube","Pinterest"), pick("image","video","carousel","story","reel","text"), lorem(15), num(10,50000), num(0,5000), num(0,2000), num(100,500000), round(random.uniform(0.1,15),2), timestamp(), pick(*STATUS)]
        },
        "Customers": {
            "cols": ["id","first_name","last_name","email","phone","company","industry","acquisition_source","lifetime_value","segment","status","created_at"],
            "gen": lambda i: [i, random.choice(["James","Mary","John","Patricia","Emma"]), random.choice(["Smith","Johnson","Williams","Brown"]), email(), phone(), pick("Tech Corp","Global Inc","ABC Company","XYZ Ltd"), pick("Technology","Healthcare","Finance","Retail","Education"), pick("organic","paid","referral","direct","social"), price(100,50000), pick("enterprise","mid_market","small_business","startup"), pick(*STATUS), timestamp()]
        }
    }
},
"property": {
    "title": "Property_Construction_Database",
    "sheets": {
        "Properties": {
            "cols": ["id","title","type","description","price","bedrooms","bathrooms","sqft","lot_size","year_built","address","city","state","zip","status","agent_id","created_at"],
            "gen": lambda i: [i, lorem(8), pick("house","apartment","condo","townhouse","commercial","land","villa"), lorem(15), price(50000,2000000), num(1,8), num(1,6), num(500,8000), num(1000,50000), num(1950,2025), address(), city()[0], city()[1], random.randint(10000,99999), pick(*STATUS), num(1,30), timestamp()]
        },
        "Construction_Projects": {
            "cols": ["id","project_name","property_id","type","budget","actual_cost","start_date","end_date","status","contractor","architect","permit_number","progress_percent","created_at"],
            "gen": lambda i: [i, lorem(6), num(1,50), pick("new_build","renovation","addition","demolition","restoration","commercial"), price(50000,5000000), price(25000,4500000), date("2025-01-01","2025-06-30"), date("2025-07-01","2026-12-31"), pick(*STATUS), name(), name(), f"PERM-{random.randint(10000,99999)}", num(0,100), timestamp()]
        },
        "Agents": {
            "cols": ["id","first_name","last_name","email","phone","license_number","agency","specialization","years_experience","total_sales","avg_rating","is_active","created_at"],
            "gen": lambda i: [i, random.choice(["James","Mary","John","Patricia","Emma"]), random.choice(["Smith","Johnson","Williams","Brown"]), email(), phone(), f"LIC-{random.randint(100000,999999)}", pick("Keller Williams","RE/MAX","Coldwell Banker","Century 21","Sotheby's","Berkshire Hathaway"), pick("residential","commercial","luxury","land","rental"), num(1,30), num(10,500), round(random.uniform(3,5),1), bool_val(), timestamp()]
        },
        "Inspections": {
            "cols": ["id","property_id","inspection_type","inspector_name","inspection_date","result","notes","cost","created_at"],
            "gen": lambda i: [i, num(1,50), pick("home","pest","radon","mold","structural","electrical","plumbing"), name(), date("2025-01-01","2025-12-31"), pick("pass","fail","conditional","pending"), lorem(15), price(200,2000), timestamp()]
        },
        "Maintenance": {
            "cols": ["id","property_id","request_type","description","priority","status","cost","scheduled_date","completed_date","contractor","created_at"],
            "gen": lambda i: [i, num(1,50), pick("plumbing","electrical","hvac","landscaping","cleaning","pest_control","roofing","painting"), lorem(15), pick("low","medium","high","emergency"), pick(*STATUS), price(50,5000), date("2025-01-01","2025-12-31"), date("2025-01-01","2025-12-31"), name(), timestamp()]
        },
        "Rentals": {
            "cols": ["id","property_id","tenant_name","rent_amount","security_deposit","lease_start","lease_end","status","payment_status","monthly_due_day","created_at"],
            "gen": lambda i: [i, num(1,50), name(), price(500,5000), price(500,10000), date("2025-01-01","2025-06-30"), date("2026-01-01","2026-12-31"), pick(*STATUS), pick(*STATUS), num(1,28), timestamp()]
        }
    }
},
"creator": {
    "title": "FansXcluziv_Database",
    "sheets": {
        "Creators": {
            "cols": ["id","username","display_name","email","bio","avatar_url","category","subscription_price","total_fans","total_earnings","is_verified","is_active","created_at"],
            "gen": lambda i: [i, f"creator_{i}", name(), email(), lorem(15), f"https://picsum.photos/200?r={i}", pick("fitness","music","art","gaming","cooking","fashion","tech","lifestyle","comedy","education"), price(4.99,49.99), num(10,50000), price(100,500000), bool_val(), bool_val(), timestamp()]
        },
        "Fans": {
            "cols": ["id","username","display_name","email","country","total_spent","favorite_creator","is_subscribed","is_active","created_at"],
            "gen": lambda i: [i, f"fan_{i}", name(), email(), pick("US","UK","CA","AU","DE","FR","JP","BR","IN","MX"), price(0,5000), num(1,50), bool_val(), bool_val(), timestamp()]
        },
        "Posts": {
            "cols": ["id","creator_id","title","content","post_type","media_url","is_premium","price","likes_count","comments_count","views_count","is_published","created_at"],
            "gen": lambda i: [i, num(1,50), lorem(8), lorem(20), pick("photo","video","text","audio","live","story"), f"https://picsum.photos/400?r={i}", bool_val(), price(0,25), num(0,10000), num(0,5000), num(0,100000), bool_val(), timestamp()]
        },
        "Subscriptions": {
            "cols": ["id","fan_id","creator_id","plan_name","price","billing_cycle","start_date","end_date","status","auto_renew","created_at"],
            "gen": lambda i: [i, num(1,100), num(1,50), pick("monthly","quarterly","yearly","lifetime"), price(4.99,99.99), pick("monthly","quarterly","yearly"), date("2025-01-01","2025-06-30"), date("2025-07-01","2026-12-31"), pick(*STATUS), bool_val(), timestamp()]
        },
        "Tips": {
            "cols": ["id","fan_id","creator_id","amount","message","payment_method","transaction_id","created_at"],
            "gen": lambda i: [i, num(1,100), num(1,50), price(1,500), lorem(10), pick(*PAYMENT), f"TXN-{random.randint(100000,999999)}", timestamp()]
        },
        "Gifts": {
            "cols": ["id","fan_id","creator_id","gift_name","gift_value","gift_icon","message","created_at"],
            "gen": lambda i: [i, num(1,100), num(1,50), pick("Rose","Diamond","Crown","Heart","Star","Rocket","Fire","Music Note","Cake","Flower"), price(1,100), pick("&#127801;","&#128142;","&#128081;","&#128151;","&#11088;","&#128640;","&#128293;","&#127925;","&#127874;","&#127800;"), lorem(10), timestamp()]
        },
        "Messages": {
            "cols": ["id","sender_id","receiver_id","content","message_type","is_read","created_at"],
            "gen": lambda i: [i, num(1,100), num(1,100), lorem(15), pick("text","image","video","voice","gift"), bool_val(), timestamp()]
        },
        "Analytics": {
            "cols": ["id","creator_id","date","views","likes","comments","shares","new_subscribers","revenue","engagement_rate","created_at"],
            "gen": lambda i: [i, num(1,50), date("2025-01-01","2025-12-31"), num(100,100000), num(10,50000), num(1,5000), num(0,2000), num(0,500), price(0,5000), round(random.uniform(0.1,15),2), timestamp()]
        },
        "Withdrawals": {
            "cols": ["id","creator_id","amount","fee","net_amount","bank_name","account_last4","status","requested_at","processed_at","created_at"],
            "gen": lambda i: [i, num(1,50), price(50,10000), price(5,500), price(45,9500), pick("Chase","Wells Fargo","Bank of America","PayPal","Wise"), f"{random.randint(1000,9999)}", pick(*STATUS), timestamp(), timestamp(), timestamp()]
        }
    }
}
}
print("Final schemas loaded")
from data_pools import name, email, phone, city, address, date, timestamp, price, num, pick, bool_val, lorem, STATUS, PAYMENT, COLORS, SIZES, CITIES
