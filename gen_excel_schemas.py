"""Domain-aware Excel schemas for demo data generation."""
import random

SCHEMAS = {
"dating": {
    "title": "Dating_App_Database",
    "sheets": {
        "Users": {
            "cols": ["id","username","email","first_name","last_name","phone","date_of_birth","gender","city","state","country","is_active","created_at","updated_at"],
            "gen": lambda i: [i, f"user_{i}", email(), random.choice(["James","Mary","John","Patricia","Robert","Emma","Olivia","Noah","Ava","Liam"]), random.choice(["Smith","Johnson","Williams","Brown","Garcia","Taylor","Lee","Martin"]), phone(), date("1985-01-01","2000-12-31"), pick("male","female","non_binary","other"), city()[0], city()[1], "US", bool_val(), timestamp(), timestamp()]
        },
        "Profiles": {
            "cols": ["id","user_id","display_name","bio","avatar_url","height_cm","relationship_status","occupation","education","income_range","smoking","drinking","pets","has_children","want_children"],
            "gen": lambda i: [i, num(1,200), name(), lorem(10), f"https://picsum.photos/200?r={i}", num(155,195), pick("single","divorced","widowed","separated"), pick("Engineer","Doctor","Teacher","Artist","Manager","Developer","Designer","Nurse","Lawyer","Chef"), pick("High School","Bachelor","Master","PhD","MBA"), pick("$30-50K","$50-80K","$80-120K","$120K+"), pick("never","occasionally","regularly"), pick("never","socially","regularly"), pick("dog","cat","fish","bird","none"), bool_val(), pick("yes","no","maybe")]
        },
        "Likes": {
            "cols": ["id","from_user_id","to_user_id","type","created_at"],
            "gen": lambda i: [i, num(1,200), num(1,200), pick("like","super_like","wave"), timestamp()]
        },
        "Matches": {
            "cols": ["id","user1_id","user2_id","matched_at","status","match_score"],
            "gen": lambda i: [i, num(1,200), num(1,200), timestamp(), pick("active","unmatched","pending"), num(1,100)]
        },
        "Messages": {
            "cols": ["id","match_id","sender_id","content","message_type","is_read","sent_at"],
            "gen": lambda i: [i, num(1,100), num(1,200), lorem(15), pick("text","image","gif","voice"), bool_val(), timestamp()]
        },
        "Conversations": {
            "cols": ["id","match_id","last_message_at","message_count","is_active"],
            "gen": lambda i: [i, num(1,100), timestamp(), num(1,500), bool_val()]
        },
        "Subscriptions": {
            "cols": ["id","user_id","plan_name","price","billing_cycle","start_date","end_date","status","auto_renew"],
            "gen": lambda i: [i, num(1,200), pick("Free","Basic","Premium","Platinum"), price(0,49.99), pick("monthly","quarterly","yearly"), date("2024-01-01","2024-12-31"), date("2025-01-01","2025-12-31"), pick(*STATUS), bool_val()]
        },
        "Payments": {
            "cols": ["id","user_id","amount","currency","payment_method","transaction_id","status","paid_at","description"],
            "gen": lambda i: [i, num(1,200), price(9.99,99.99), "USD", pick(*PAYMENT), f"TXN-{random.randint(100000,999999)}", pick("success","pending","failed","refunded"), timestamp(), pick("subscription","boost","super_like","premium")]
        },
        "Reports": {
            "cols": ["id","reporter_id","reported_id","reason","description","status","created_at","resolved_at"],
            "gen": lambda i: [i, num(1,200), num(1,200), pick("fake_profile","inappropriate","harassment","spam","other"), lorem(8), pick("pending","investigating","resolved","dismissed"), timestamp(), timestamp()]
        },
        "Blocked_Users": {
            "cols": ["id","blocker_id","blocked_id","reason","created_at"],
            "gen": lambda i: [i, num(1,200), num(1,200), pick("harassment","spam","not_interested","other"), timestamp()]
        },
        "Notifications": {
            "cols": ["id","user_id","type","title","message","is_read","created_at"],
            "gen": lambda i: [i, num(1,200), pick("match","message","like","system","payment"), pick("New Match!","New Message","Someone liked you","Profile Boosted","Payment Received"), lorem(10), bool_val(), timestamp()]
        },
        "Profile_Boosts": {
            "cols": ["id","user_id","boost_type","started_at","ended_at","views_gained","matches_gained"],
            "gen": lambda i: [i, num(1,200), pick("standard","premium","spotlight"), timestamp(), timestamp(), num(50,1000), num(1,50)]
        }
    }
},
"legal": {
    "title": "LawFirm_LegalPractice_Database",
    "sheets": {
        "Clients": {
            "cols": ["id","first_name","last_name","email","phone","address","city","state","company","client_type","status","created_at"],
            "gen": lambda i: [i, random.choice(["James","Mary","John","Patricia","Robert","Emma"]), random.choice(["Smith","Johnson","Williams","Brown","Garcia"]), email(), phone(), address(), city()[0], city()[1], pick("Smith & Co","ABC Corp","Global Inc","Tech Solutions","None"), pick("individual","business","government"), pick(*STATUS), timestamp()]
        },
        "Cases": {
            "cols": ["id","case_number","client_id","case_type","title","description","status","priority","filing_date","court_date","assigned_to","outcome"],
            "gen": lambda i: [i, f"CASE-{2024}-{random.randint(1000,9999)}", num(1,100), pick("civil","criminal","family","corporate","immigration","real_estate","tax","ip"), lorem(8), lorem(15), pick(*STATUS), pick("low","medium","high","urgent"), date("2024-01-01","2025-06-30"), date("2025-07-01","2025-12-31"), name(), pick("won","lost","settled","dismissed","pending")]
        },
        "Hearings": {
            "cols": ["id","case_id","hearing_date","hearing_time","court_name","judge_name","hearing_type","status","notes"],
            "gen": lambda i: [i, num(1,100), date("2025-01-01","2025-12-31"), f"{random.randint(9,17):02d}:{random.choice(['00','30'])}", pick("District Court","Superior Court","Federal Court","Appeals Court","Family Court"), name(), pick("initial","status","evidence","sentencing","appeal"), pick(*STATUS), lorem(10)]
        },
        "Documents": {
            "cols": ["id","case_id","document_type","title","file_name","file_size_kb","uploaded_by","uploaded_at","is_confidential"],
            "gen": lambda i: [i, num(1,100), pick("contract","pleading","evidence","correspondence","filing","order","motion"), lorem(6), f"doc_{i}.pdf", num(50,5000), name(), timestamp(), bool_val()]
        },
        "Billing": {
            "cols": ["id","case_id","client_id","invoice_number","description","hours","rate","total_amount","tax","status","invoice_date","due_date","paid_date","payment_method"],
            "gen": lambda i: [i, num(1,100), num(1,100), f"INV-{2025}-{random.randint(10000,99999)}", lorem(8), round(random.uniform(0.5,40),1), price(100,500), price(500,25000), price(50,2000), pick(*STATUS), date("2025-01-01","2025-12-31"), date("2025-01-01","2025-12-31"), date("2025-01-01","2025-12-31"), pick(*PAYMENT)]
        },
        "Appointments": {
            "cols": ["id","client_id","lawyer_id","appointment_date","appointment_time","meeting_type","purpose","status","notes"],
            "gen": lambda i: [i, num(1,100), num(1,20), date("2025-01-01","2025-12-31"), f"{random.randint(9,17):02d}:{random.choice(['00','30'])}", pick("in_person","phone","video","email"), pick("consultation","follow_up","document_review","court_prep"), pick(*STATUS), lorem(8)]
        },
        "Staff": {
            "cols": ["id","first_name","last_name","email","phone","role","specialization","hire_date","bar_number","is_active"],
            "gen": lambda i: [i, random.choice(["James","Mary","John","Patricia"]), random.choice(["Smith","Johnson","Williams","Brown"]), email(), phone(), pick("partner","associate","paralegal","admin","intern"), pick("criminal","corporate","family","real_estate","ip","tax","immigration"), date("2018-01-01","2025-01-01"), f"BAR-{random.randint(100000,999999)}", bool_val()]
        },
        "Tasks": {
            "cols": ["id","case_id","assigned_to","title","description","due_date","priority","status","completed_at"],
            "gen": lambda i: [i, num(1,100), num(1,20), lorem(6), lorem(12), date("2025-01-01","2025-12-31"), pick("low","medium","high","urgent"), pick(*STATUS), timestamp()]
        }
    }
},
"health": {
    "title": "HealthVault_16_Table_Database",
    "sheets": {
        "Patients": {
            "cols": ["id","first_name","last_name","date_of_birth","gender","phone","email","address","city","state","blood_type","insurance_provider","insurance_number","emergency_contact","emergency_phone","created_at"],
            "gen": lambda i: [i, random.choice(["James","Mary","John","Patricia","Emma","Olivia"]), random.choice(["Smith","Johnson","Williams","Brown","Garcia"]), date("1950-01-01","2010-12-31"), pick("male","female","other"), phone(), email(), address(), city()[0], city()[1], pick("A+","A-","B+","B-","AB+","AB-","O+","O-"), pick("Blue Cross","Aetna","UnitedHealth","Cigna","Humana","Kaiser"), f"INS-{random.randint(100000,999999)}", name(), phone(), timestamp()]
        },
        "Doctors": {
            "cols": ["id","first_name","last_name","specialization","license_number","phone","email","hospital","years_experience","rating","is_active"],
            "gen": lambda i: [i, random.choice(["James","Mary","John","Patricia"]), random.choice(["Smith","Johnson","Williams","Brown"]), pick("Cardiology","Neurology","Pediatrics","Orthopedics","Dermatology","Psychiatry","Oncology","General","Emergency","Surgery"), f"MD-{random.randint(100000,999999)}", phone(), email(), pick("City Hospital","Medical Center","Health Clinic","General Hospital","Mayo Clinic"), num(3,35), round(random.uniform(3.0,5.0),1), bool_val()]
        },
        "Appointments": {
            "cols": ["id","patient_id","doctor_id","appointment_date","appointment_time","visit_type","reason","status","notes","follow_up_date"],
            "gen": lambda i: [i, num(1,100), num(1,30), date("2025-01-01","2025-12-31"), f"{random.randint(8,17):02d}:{random.choice(['00','30'])}", pick("consultation","follow_up","checkup","surgery","emergency","lab_test"), lorem(8), pick(*STATUS), lorem(10), date("2025-06-01","2026-06-30")]
        },
        "Medical_Records": {
            "cols": ["id","patient_id","doctor_id","visit_date","diagnosis","treatment","prescription","lab_results","notes","created_at"],
            "gen": lambda i: [i, num(1,100), num(1,30), date("2024-01-01","2025-12-31"), lorem(8), lorem(10), lorem(8), lorem(8), lorem(10), timestamp()]
        },
        "Prescriptions": {
            "cols": ["id","patient_id","doctor_id","medication_name","dosage","frequency","start_date","end_date","refills","status","notes"],
            "gen": lambda i: [i, num(1,100), num(1,30), pick("Aspirin","Metformin","Lisinopril","Amlodipine","Omeprazole","Metoprolol","Losartan","Gabapentin","Atorvastatin","Levothyroxine"), pick("10mg","20mg","25mg","50mg","100mg"), pick("once_daily","twice_daily","three_times","as_needed"), date("2025-01-01","2025-06-30"), date("2025-07-01","2025-12-31"), num(0,5), pick(*STATUS), lorem(5)]
        },
        "Lab_Tests": {
            "cols": ["id","patient_id","doctor_id","test_name","test_date","result","normal_range","unit","status","notes"],
            "gen": lambda i: [i, num(1,100), num(1,30), pick("Blood Count","Glucose","Cholesterol","Thyroid","Liver Function","Kidney Function","Hemoglobin","Vitamin D","Iron","Allergy Panel"), date("2025-01-01","2025-12-31"), round(random.uniform(1,200),2), pick("70-100","10-20","100-200","0.5-5.0","40-70"), pick("mg/dL","mmol/L","g/dL","ng/mL","IU/L"), pick(*STATUS), lorem(5)]
        },
        "Billing": {
            "cols": ["id","patient_id","appointment_id","service","amount","insurance_covered","patient_copay","total_bill","payment_status","paid_date","payment_method"],
            "gen": lambda i: [i, num(1,100), num(1,100), pick("Consultation","Lab Test","X-Ray","MRI","Surgery","Medication","Emergency","Follow-up"), price(50,5000), price(25,2500), price(10,500), price(100,10000), pick(*STATUS), date("2025-01-01","2025-12-31"), pick(*PAYMENT)]
        },
        "Insurance": {
            "cols": ["id","patient_id","provider_name","policy_number","group_number","coverage_type","start_date","end_date","deductible","copay","is_active"],
            "gen": lambda i: [i, num(1,100), pick("Blue Cross","Aetna","UnitedHealth","Cigna","Humana","Kaiser"), f"POL-{random.randint(100000,999999)}", f"GRP-{random.randint(1000,9999)}", pick("individual","family","group","medicare","medicaid"), date("2024-01-01","2024-12-31"), date("2025-01-01","2025-12-31"), price(500,5000), price(10,75), bool_val()]
        }
    }
}
}
from data_pools import name, email, phone, city, address, date, timestamp, price, num, pick, bool_val, lorem, STATUS, PAYMENT, COLORS, SIZES, CITIES

print(f"Loaded {len(SCHEMAS)} domain schemas")
