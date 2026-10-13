"""More domain schemas."""
import random

SCHEMAS = {
"ecommerce": {
    "title": "Ecommerce_Platform_Database",
    "sheets": {
        "Products": {
            "cols": ["id","name","sku","description","category","brand","price","cost","stock_quantity","weight_kg","color","size","is_active","rating","created_at"],
            "gen": lambda i: [i, f"Product {i}", f"SKU-{random.randint(10000,99999)}", lorem(15), pick("Electronics","Clothing","Home","Sports","Books","Beauty","Toys","Food"), pick("Apple","Samsung","Nike","Adidas","Sony","LG","Dell","HP"), price(5,2000), price(2,1000), num(0,1000), round(random.uniform(0.1,20),2), pick(*COLORS), pick(*SIZES), bool_val(), round(random.uniform(1,5),1), timestamp()]
        },
        "Orders": {
            "cols": ["id","customer_id","order_number","total_amount","tax","shipping_cost","discount","status","payment_method","shipping_address","city","state","zip","created_at","shipped_at","delivered_at"],
            "gen": lambda i: [i, num(1,200), f"ORD-{2025}-{random.randint(10000,99999)}", price(10,5000), price(1,200), price(0,25), price(0,50), pick(*STATUS), pick(*PAYMENT), address(), city()[0], city()[1], random.randint(10000,99999), timestamp(), timestamp(), timestamp()]
        },
        "Customers": {
            "cols": ["id","first_name","last_name","email","phone","address","city","state","total_orders","total_spent","loyalty_points","tier","created_at"],
            "gen": lambda i: [i, random.choice(["James","Mary","John","Patricia","Emma"]), random.choice(["Smith","Johnson","Williams","Brown"]), email(), phone(), address(), city()[0], city()[1], num(0,50), price(0,10000), num(0,5000), pick("Bronze","Silver","Gold","Platinum"), timestamp()]
        },
        "Order_Items": {
            "cols": ["id","order_id","product_id","quantity","unit_price","total_price","discount"],
            "gen": lambda i: [i, num(1,200), num(1,100), num(1,5), price(5,500), price(5,1000), price(0,50)]
        },
        "Reviews": {
            "cols": ["id","product_id","customer_id","rating","title","comment","is_verified","helpful_count","created_at"],
            "gen": lambda i: [i, num(1,100), num(1,200), num(1,5), lorem(6), lorem(15), bool_val(), num(0,200), timestamp()]
        },
        "Categories": {
            "cols": ["id","name","description","parent_id","is_active","product_count","created_at"],
            "gen": lambda i: [i, pick("Electronics","Clothing","Home & Garden","Sports","Books","Beauty","Toys","Food & Beverage","Automotive","Health"), lorem(10), num(0,10), bool_val(), num(0,200), timestamp()]
        },
        "Inventory": {
            "cols": ["id","product_id","warehouse","quantity_in","quantity_out","quantity_available","reorder_level","last_restocked"],
            "gen": lambda i: [i, num(1,100), pick("Main Warehouse","East Warehouse","West Warehouse","Central Hub"), num(10,500), num(5,300), num(0,200), num(10,50), date("2025-01-01","2025-12-31")]
        },
        "Shipping": {
            "cols": ["id","order_id","carrier","tracking_number","shipping_method","estimated_delivery","actual_delivery","status","weight_kg"],
            "gen": lambda i: [i, num(1,200), pick("UPS","FedEx","USPS","DHL","Amazon"), f"TRK-{random.randint(100000,999999)}", pick("standard","express","overnight","two_day"), date("2025-01-01","2025-12-31"), date("2025-01-01","2025-12-31"), pick(*STATUS), round(random.uniform(0.1,30),2)]
        }
    }
},
"finance": {
    "title": "Loan_Marketplace_Database",
    "sheets": {
        "Borrowers": {
            "cols": ["id","first_name","last_name","email","phone","date_of_birth","ssn_last4","annual_income","employment_status","employer","job_title","credit_score","address","city","state","created_at"],
            "gen": lambda i: [i, random.choice(["James","Mary","John","Patricia","Emma"]), random.choice(["Smith","Johnson","Williams","Brown"]), email(), phone(), date("1970-01-01","2000-12-31"), f"{random.randint(1000,9999)}", price(30000,200000), pick("full_time","part_time","self_employed","retired","unemployed"), pick("Tech Corp","Health Inc","Finance Group","Education Ltd","Retail Co"), pick("Manager","Developer","Analyst","Director","Specialist"), num(300,850), address(), city()[0], city()[1], timestamp()]
        },
        "Loans": {
            "cols": ["id","borrower_id","loan_type","amount","interest_rate","term_months","monthly_payment","total_interest","status","purpose","approved_at","start_date","end_date","lender_name","created_at"],
            "gen": lambda i: [i, num(1,100), pick("personal","auto","home","student","business","debt_consolidation"), price(1000,500000), round(random.uniform(2.5,15.5),2), pick(12,24,36,60,120,180,360), price(100,5000), price(500,50000), pick(*STATUS), pick("home_purchase","car","education","debt_consolidation","business","medical","vacation","wedding"), timestamp(), date("2025-01-01","2025-06-30"), date("2026-01-01","2035-12-31"), pick("Chase","Wells Fargo","Bank of America","Capital One","Ally","Discover"), timestamp()]
        },
        "Payments": {
            "cols": ["id","loan_id","payment_number","amount","principal_amount","interest_amount","remaining_balance","payment_date","payment_method","status"],
            "gen": lambda i: [i, num(1,100), num(1,60), price(100,5000), price(50,3000), price(10,2000), price(0,500000), date("2025-01-01","2025-12-31"), pick(*PAYMENT), pick(*STATUS)]
        },
        "Lenders": {
            "cols": ["id","name","type","license_number","min_loan","max_loan","min_rate","max_rating","specialization","is_active","created_at"],
            "gen": lambda i: [i, pick("Chase Bank","Wells Fargo","Ally Financial","Capital One","Discover","Lending Club","Prosper","SoFi","Marcus","Upstart"), pick("bank","credit_union","online_lender","p2p"), f"LIC-{random.randint(100000,999999)}", price(1000,10000), price(50000,1000000), round(random.uniform(2,8),2), round(random.uniform(8,18),2), pick("personal","auto","home","business","student"), bool_val(), timestamp()]
        },
        "Credit_Scores": {
            "cols": ["id","borrower_id","score","bureau","report_date","previous_score","change","factors_positive","factors_negative","created_at"],
            "gen": lambda i: [i, num(1,100), num(300,850), pick("Experian","Equifax","TransUnion"), date("2025-01-01","2025-12-31"), num(300,850), num(-50,50), lorem(10), lorem(10), timestamp()]
        },
        "Applications": {
            "cols": ["id","borrower_id","loan_type","requested_amount","purpose","status","submitted_at","reviewed_at","decision","decision_notes","credit_check_score"],
            "gen": lambda i: [i, num(1,100), pick("personal","auto","home","student","business"), price(1000,500000), lorem(10), pick(*STATUS), timestamp(), timestamp(), pick("approved","rejected","pending","withdrawn"), lorem(10), num(300,850)]
        },
        "Transactions": {
            "cols": ["id","borrower_id","loan_id","type","amount","description","balance_after","created_at"],
            "gen": lambda i: [i, num(1,100), num(1,100), pick("payment","disbursement","fee","refund","adjustment"), price(10,10000), lorem(8), price(0,500000), timestamp()]
        }
    }
},
"business": {
    "title": "Business_Management_Database",
    "sheets": {
        "Employees": {
            "cols": ["id","first_name","last_name","email","phone","department","position","salary","hire_date","manager_id","status","address","city","state","created_at"],
            "gen": lambda i: [i, random.choice(["James","Mary","John","Patricia","Emma"]), random.choice(["Smith","Johnson","Williams","Brown"]), email(), phone(), pick("Engineering","Sales","Marketing","HR","Finance","Operations","IT","Customer Support"), pick("Junior","Mid","Senior","Lead","Manager","Director","VP","C-Level"), price(35000,250000), date("2018-01-01","2025-06-30"), num(1,20), pick(*STATUS), address(), city()[0], city()[1], timestamp()]
        },
        "Projects": {
            "cols": ["id","name","description","start_date","end_date","budget","actual_cost","status","priority","manager_id","progress_percent","created_at"],
            "gen": lambda i: [i, lorem(4), lorem(15), date("2025-01-01","2025-06-30"), date("2025-07-01","2025-12-31"), price(10000,500000), price(5000,450000), pick(*STATUS), pick("low","medium","high","critical"), num(1,20), num(0,100), timestamp()]
        },
        "Tasks": {
            "cols": ["id","project_id","assigned_to","title","description","due_date","status","priority","estimated_hours","actual_hours","created_at"],
            "gen": lambda i: [i, num(1,50), num(1,100), lorem(6), lorem(15), date("2025-01-01","2025-12-31"), pick(*STATUS), pick("low","medium","high","critical"), num(1,40), num(1,40), timestamp()]
        },
        "Invoices": {
            "cols": ["id","invoice_number","client_name","amount","tax","total","issue_date","due_date","paid_date","status","payment_method","notes"],
            "gen": lambda i: [i, f"INV-{2025}-{random.randint(10000,99999)}", name(), price(500,50000), price(25,2500), price(525,52500), date("2025-01-01","2025-06-30"), date("2025-07-01","2025-12-31"), date("2025-07-01","2025-12-31"), pick(*STATUS), pick(*PAYMENT), lorem(8)]
        },
        "Expenses": {
            "cols": ["id","category","description","amount","expense_date","submitted_by","approved_by","status","receipt_number","created_at"],
            "gen": lambda i: [i, pick("travel","meals","equipment","office","software","training","advertising","utilities","rent","other"), lorem(10), price(10,5000), date("2025-01-01","2025-12-31"), name(), name(), pick(*STATUS), f"RCP-{random.randint(10000,99999)}", timestamp()]
        },
        "Clients": {
            "cols": ["id","company_name","contact_name","email","phone","industry","website","address","city","state","status","total_revenue","created_at"],
            "gen": lambda i: [i, pick("Tech Corp","Global Inc","Smart Solutions","Innovation Labs","Data Analytics Co","Digital Media Ltd"), name(), email(), phone(), pick("Technology","Healthcare","Finance","Retail","Education","Manufacturing"), f"https://company{i}.com", address(), city()[0], city()[1], pick(*STATUS), price(10000,500000), timestamp()]
        },
        "Departments": {
            "cols": ["id","name","head_id","budget","employee_count","location","created_at"],
            "gen": lambda i: [i, pick("Engineering","Sales","Marketing","HR","Finance","Operations","IT","Customer Support","R&D","Legal"), num(1,20), price(50000,2000000), num(5,50), pick(*CITIES), timestamp()]
        }
    }
},
"skill": {
    "title": "SkillMarket_Database",
    "sheets": {
        "Workers": {
            "cols": ["id","first_name","last_name","email","phone","skills","hourly_rate","experience_years","rating","total_jobs","availability","city","state","bio","created_at"],
            "gen": lambda i: [i, random.choice(["James","Mary","John","Patricia","Emma"]), random.choice(["Smith","Johnson","Williams","Brown"]), email(), phone(), pick("Plumbing,Electrical","Carpentry,Painting","Cleaning,Organizing","Gardening,Landscaping","Moving,Delivery","Computer Repair,Tech","Tutoring,Teaching","Fitness,Coaching"), price(15,150), num(1,25), round(random.uniform(1,5),1), num(0,200), pick("full_time","part_time","weekends","evenings","on_demand"), city()[0], city()[1], lorem(15), timestamp()]
        },
        "Gigs": {
            "cols": ["id","client_id","title","description","category","budget_min","budget_max","duration_hours","location","status","posted_at","deadline","worker_id","assigned_at"],
            "gen": lambda i: [i, num(1,100), lorem(8), lorem(15), pick("plumbing","electrical","cleaning","gardening","moving","tech","tutoring","fitness","painting","carpentry"), price(20,200), price(200,5000), num(1,40), pick(*CITIES), pick(*STATUS), timestamp(), date("2025-01-01","2025-12-31"), num(1,100), timestamp()]
        },
        "Reviews": {
            "cols": ["id","gig_id","reviewer_id","reviewee_id","rating","title","comment","would_recommend","created_at"],
            "gen": lambda i: [i, num(1,100), num(1,100), num(1,100), num(1,5), lorem(6), lorem(15), bool_val(), timestamp()]
        },
        "Skills": {
            "cols": ["id","name","category","description","demand_level","avg_rate","certification_required","is_active"],
            "gen": lambda i: [i, pick("Plumbing","Electrical","Carpentry","Painting","Cleaning","Gardening","Moving","Computer Repair","Tutoring","Fitness","Photography","Web Design"), pick("trade","tech","creative","education","health","service"), lorem(10), pick("low","medium","high","very_high"), price(15,150), bool_val(), bool_val()]
        },
        "Bookings": {
            "cols": ["id","gig_id","worker_id","client_id","booking_date","start_time","end_time","status","total_amount","platform_fee","worker_payout","payment_method","created_at"],
            "gen": lambda i: [i, num(1,100), num(1,100), num(1,100), date("2025-01-01","2025-12-31"), f"{random.randint(7,18):02d}:00", f"{random.randint(10,22):02d}:00", pick(*STATUS), price(50,2000), price(5,200), price(45,1800), pick(*PAYMENT), timestamp()]
        },
        "Certifications": {
            "cols": ["id","worker_id","certification_name","issuing_org","issue_date","expiry_date","certificate_number","is_verified","created_at"],
            "gen": lambda i: [i, num(1,100), pick("EPA Certification","OSHA Safety","Master Plumber","Licensed Electrician","CPR/First Aid","CompTIA A+","TEFL","NASM CPT"), pick("State Board","National Board","Union","Online Academy"), date("2020-01-01","2025-01-01"), date("2025-06-01","2030-12-31"), f"CERT-{random.randint(100000,999999)}", bool_val(), timestamp()]
        }
    }
}
}
print("Extended schemas loaded")
from data_pools import name, email, phone, city, address, date, timestamp, price, num, pick, bool_val, lorem, STATUS, PAYMENT, COLORS, SIZES, CITIES
