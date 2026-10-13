"""Category schemas: agency, creative, travel, pets, industrial, government."""
import random
from data_pools import name, email, phone, city, address, date, timestamp, price, num, pick, bool_val, lorem, STATUS, PAYMENT, CITIES

SCHEMAS = {
"agency": {
    "title": "Agency_Database",
    "sheets": {
        "Clients": {"cols": ["id","company_name","contact_name","email","phone","industry","contract_value","status","created_at"], "gen": lambda i: [i,pick("Tech Corp","Global Inc","ABC Company","XYZ Ltd","Innovation Co"),name(),email(),phone(),pick("Technology","Healthcare","Finance","Retail"),price(5000,500000),pick(*STATUS),timestamp()]},
        "Projects": {"cols": ["id","client_id","name","type","budget","spent","status","start_date","end_date","progress"], "gen": lambda i: [i,num(1,100),lorem(6),pick("campaign","branding","research","consulting","training"),price(5000,200000),price(2000,180000),pick(*STATUS),date("2025-01-01","2025-06-30"),date("2025-07-01","2025-12-31"),num(0,100)]},
        "Staff": {"cols": ["id","name","email","role","department","salary","hire_date","is_active"], "gen": lambda i: [i,name(),email(),pick("Manager","Designer","Developer","Analyst","Writer","Account"),pick("creative","tech","strategy","account","operations"),price(30000,200000),date("2018-01-01","2025-01-01"),bool_val()]},
        "Proposals": {"cols": ["id","client_id","title","description","amount","status","submitted_at","decided_at"], "gen": lambda i: [i,num(1,100),lorem(6),lorem(15),price(5000,100000),pick("draft","submitted","accepted","rejected"),timestamp(),timestamp()]},
        "Invoices": {"cols": ["id","client_id","project_id","amount","tax","total","status","date","due_date"], "gen": lambda i: [i,num(1,100),num(1,50),price(1000,50000),price(100,5000),price(1100,55000),pick(*STATUS),date("2025-01-01","2025-06-30"),date("2025-07-01","2025-12-31")]},
        "Tasks": {"cols": ["id","project_id","assigned_to","title","due_date","priority","status"], "gen": lambda i: [i,num(1,50),num(1,30),lorem(6),date("2025-01-01","2025-12-31"),pick("low","medium","high","urgent"),pick(*STATUS)]},
    }
},
"creative": {
    "title": "Creative_Studio_Database",
    "sheets": {
        "Projects": {"cols": ["id","title","client_id","type","budget","status","deadline","description","created_at"], "gen": lambda i: [i,lorem(6),num(1,50),pick("video","photo","animation","design","music","film"),price(1000,200000),pick(*STATUS),date("2025-01-01","2025-12-31"),lorem(15),timestamp()]},
        "Clients": {"cols": ["id","name","email","phone","company","project_count","total_spent","status"], "gen": lambda i: [i,name(),email(),phone(),pick("Brand Co","Music Label","Film Studio","Agency"),num(1,20),price(1000,500000),pick(*STATUS)]},
        "Team": {"cols": ["id","name","email","role","skills","rate_per_day","is_active"], "gen": lambda i: [i,name(),email(),pick("Director","Editor","Designer","Sound Engineer","VFX Artist","Producer"),pick("Adobe,Final Cut","Maya,Blender","Photoshop,Illustrator","Pro Tools,Logic"),price(500,5000),bool_val()]},
        "Assets": {"cols": ["id","project_id","type","file_name","file_size_mb","format","status","created_at"], "gen": lambda i: [i,num(1,50),pick("video","audio","image","3d_model","script"),f"asset_{i}.mp4",round(random.uniform(1,5000),1),pick("mp4","wav","png","blend","pdf"),pick(*STATUS),timestamp()]},
        "Deliverables": {"cols": ["id","project_id","name","type","deadline","status","client_feedback","delivered_at"], "gen": lambda i: [i,num(1,50),lorem(4),pick("final_cut","draft","preview","revision"),date("2025-01-01","2025-12-31"),pick(*STATUS),lorem(10),timestamp()]},
        "Invoices": {"cols": ["id","project_id","amount","tax","total","status","date","paid_at"], "gen": lambda i: [i,num(1,50),price(500,100000),price(50,10000),price(550,110000),pick(*STATUS),date("2025-01-01","2025-12-31"),date("2025-01-01","2025-12-31")]},
    }
},
"travel": {
    "title": "Travel_Tourism_Database",
    "sheets": {
        "Customers": {"cols": ["id","name","email","phone","address","passport_number","nationality","created_at"], "gen": lambda i: [i,name(),email(),phone(),address(),f"P{random.randint(1000000,9999999)}",pick("US","UK","IN","AU","CA","DE","JP","FR"),timestamp()]},
        "Bookings": {"cols": ["id","customer_id","package_id","travel_date","return_date","travellers","total_cost","status","created_at"], "gen": lambda i: [i,num(1,200),num(1,30),date("2025-01-01","2025-06-30"),date("2025-07-01","2025-12-31"),num(1,10),price(500,50000),pick(*STATUS),timestamp()]},
        "Packages": {"cols": ["id","name","destination","duration","price","type","description","max_travellers","is_active"], "gen": lambda i: [i,lorem(4),pick("Paris","Bali","Dubai","Switzerland","Thailand","Goa","Kerala","Rajasthan"),f"{num(3,15)} days",price(500,10000),pick("adventure","luxury","budget","family","honeymoon"),lorem(15),num(2,50),bool_val()]},
        "Hotels": {"cols": ["id","name","city","stars","price_per_night","rooms_available","amenities","is_active"], "gen": lambda i: [i,pick("Grand Palace","Seaside Resort","Mountain View","City Inn","Royal Stay"),city()[0],num(1,5),price(50,2000),num(5,200),pick("pool,spa,gym","wifi,parking","restaurant,bar"),bool_val()]},
        "Payments": {"cols": ["id","booking_id","amount","method","status","paid_at","transaction_id"], "gen": lambda i: [i,num(1,200),price(500,50000),pick(*PAYMENT),pick(*STATUS),timestamp(),f"TXN-{random.randint(100000,999999)}"]},
        "Reviews": {"cols": ["id","customer_id","booking_id","rating","comment","would_recommend","created_at"], "gen": lambda i: [i,num(1,200),num(1,200),num(1,5),lorem(15),bool_val(),timestamp()]},
    }
},
"pets": {
    "title": "Pet_Services_Database",
    "sheets": {
        "Owners": {"cols": ["id","name","email","phone","address","pet_count","created_at"], "gen": lambda i: [i,name(),email(),phone(),address(),num(1,5),timestamp()]},
        "Pets": {"cols": ["id","owner_id","name","species","breed","age","weight","health_status","is_vaccinated"], "gen": lambda i: [i,num(1,100),pick("Buddy","Max","Luna","Charlie","Bella","Rocky","Daisy","Milo"),pick("dog","cat","bird","fish","rabbit"),pick("Labrador","Persian","Golden","Siamese","Poodle","Mixed"),num(1,15),round(random.uniform(1,50),1),pick("healthy","sick","recovering"),bool_val()]},
        "Services": {"cols": ["id","name","category","price","duration","description","is_active"], "gen": lambda i: [i,pick("Grooming","Boarding","Daycare","Walking","Training","Vet Check"),pick("grooming","boarding","daycare","walking","training","medical"),price(10,200),pick("30m","1h","2h","1d","1w"),lorem(10),bool_val()]},
        "Appointments": {"cols": ["id","pet_id","service_id","date","time","status","notes","cost"], "gen": lambda i: [i,num(1,100),num(1,10),date("2025-01-01","2025-12-31"),f"{random.randint(9,18):02d}:00",pick(*STATUS),lorem(5),price(10,200)]},
        "Products": {"cols": ["id","name","category","brand","price","stock","is_active"], "gen": lambda i: [i,pick("Dog Food","Cat Food","Leash","Collar","Toy","Bed","Shampoo"),pick("food","accessory","health","toy","grooming"),pick("Pedigree","Whiskas","Royal Canin","Hills"),price(5,200),num(0,500),bool_val()]},
        "Vaccinations": {"cols": ["id","pet_id","vaccine_name","date","next_due","veterinarian","notes"], "gen": lambda i: [i,num(1,100),pick("Rabies","DHPP","FVRCP","Bordetella","Lyme"),date("2025-01-01","2025-12-31"),date("2026-01-01","2026-12-31"),name(),lorem(5)]},
        "Payments": {"cols": ["id","owner_id","appointment_id","amount","method","status","paid_at"], "gen": lambda i: [i,num(1,100),num(1,200),price(10,500),pick(*PAYMENT),pick(*STATUS),timestamp()]},
    }
},
"industrial": {
    "title": "Industrial_Services_Database",
    "sheets": {
        "Equipment": {"cols": ["id","name","type","model","purchase_date","cost","condition","location","is_active"], "gen": lambda i: [i,pick("Crane","Generator","Welding Machine","CNC Machine","Compressor","Forklift"),pick("heavy","medium","light"),f"MDL-{random.randint(1000,9999)}",date("2015-01-01","2025-01-01"),price(10000,500000),pick("excellent","good","fair","needs_repair"),pick(*CITIES),bool_val()]},
        "Clients": {"cols": ["id","company_name","contact_name","email","phone","industry","status","created_at"], "gen": lambda i: [i,pick("Steel Corp","BuildCo","Mfg Industries","Power Ltd","ChemWorks"),name(),email(),phone(),pick("construction","manufacturing","energy","chemical"),pick(*STATUS),timestamp()]},
        "Services": {"cols": ["id","client_id","equipment_id","service_type","description","cost","date","status"], "gen": lambda i: [i,num(1,50),num(1,30),pick("maintenance","repair","calibration","inspection","installation"),lorem(15),price(500,50000),date("2025-01-01","2025-12-31"),pick(*STATUS)]},
        "Parts": {"cols": ["id","name","sku","category","price","stock","supplier","is_active"], "gen": lambda i: [i,pick("Bearing","Belt","Filter","Valve","Sensor","Motor","Gear"),f"IND-{random.randint(10000,99999)}",pick("mechanical","electrical","hydraulic","pneumatic"),price(10,5000),num(0,500),pick("IndParts Co","SupplyMax"),bool_val()]},
        "Invoices": {"cols": ["id","client_id","service_id","amount","tax","total","status","date","paid_at"], "gen": lambda i: [i,num(1,50),num(1,100),price(500,50000),price(50,5000),price(550,55000),pick(*STATUS),date("2025-01-01","2025-12-31"),date("2025-01-01","2025-12-31")]},
        "Inspections": {"cols": ["id","equipment_id","inspector","date","result","notes","next_inspection"], "gen": lambda i: [i,num(1,30),name(),date("2025-01-01","2025-12-31"),pick("pass","fail","conditional"),lorem(10),date("2025-07-01","2026-06-30")]},
    }
},
"government": {
    "title": "Legal_Compliance_Database",
    "sheets": {
        "Clients": {"cols": ["id","name","email","phone","company","type","pan_number","status","created_at"], "gen": lambda i: [i,name(),email(),phone(),pick("ABC Corp","XYZ Ltd","Smith & Co","Global Inc"),pick("individual","company","llp","partnership"),f"PAN{random.randint(10000,99999)}A",pick(*STATUS),timestamp()]},
        "Cases": {"cols": ["id","client_id","case_number","type","title","description","status","filing_date","court","hearing_date"], "gen": lambda i: [i,num(1,100),f"CASE-{2025}-{random.randint(1000,9999)}",pick("civil","criminal","tax","labour","corporate","ip"),lorem(8),lorem(15),pick(*STATUS),date("2025-01-01","2025-06-30"),pick("District Court","High Court","Supreme Court","Tribunal"),date("2025-07-01","2025-12-31")]},
        "Documents": {"cols": ["id","case_id","type","title","file_name","uploaded_by","uploaded_at","is_verified"], "gen": lambda i: [i,num(1,100),pick("petition","affidavit","evidence","order","notice","contract"),lorem(6),f"doc_{i}.pdf",name(),timestamp(),bool_val()]},
        "Filings": {"cols": ["id","client_id","filing_type","authority","reference_number","status","filed_date","deadline","fee"], "gen": lambda i: [i,num(1,100),pick("GST","ROC","Income Tax","Trademark","Patent","FSSAI"),pick("MCA","GST Portal","Income Tax","Trademark Registry"),f"REF-{random.randint(100000,999999)}",pick(*STATUS),date("2025-01-01","2025-06-30"),date("2025-07-01","2025-12-31"),price(500,50000)]},
        "Fees": {"cols": ["id","case_id","description","amount","paid","balance","due_date","status"], "gen": lambda i: [i,num(1,100),lorem(8),price(500,50000),price(250,25000),price(250,25000),date("2025-01-01","2025-12-31"),pick(*STATUS)]},
        "Compliance": {"cols": ["id","client_id","requirement","due_date","status","completed_date","penalty","notes"], "gen": lambda i: [i,num(1,100),pick("Annual Filing","GST Return","Tax Audit","Board Meeting","ROC Filing"),date("2025-01-01","2025-12-31"),pick(*STATUS),date("2025-01-01","2025-12-31"),price(0,100000),lorem(10)]},
        "Deadlines": {"cols": ["id","client_id","description","due_date","reminder_date","status","priority"], "gen": lambda i: [i,num(1,100),lorem(8),date("2025-01-01","2025-12-31"),date("2025-01-01","2025-12-31"),pick(*STATUS),pick("low","medium","high","urgent")]},
    }
},
}
