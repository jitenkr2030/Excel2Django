"""Category schemas: it_digital, personal, manufacturing, agriculture, automotive."""
import random
from data_pools import name, email, phone, city, address, date, timestamp, price, num, pick, bool_val, lorem, STATUS, PAYMENT, CITIES

SCHEMAS = {
"it_digital": {
    "title": "IT_Digital_Services_Database",
    "sheets": {
        "Projects": {"cols": ["id","name","client_id","description","budget","status","start_date","end_date","tech_stack","created_at"], "gen": lambda i: [i,lorem(4),num(1,100),lorem(15),price(5000,500000),pick(*STATUS),date("2025-01-01","2025-06-30"),date("2025-07-01","2025-12-31"),pick("React/Node","Django/Python","Vue/Laravel","Flutter/Firebase"),timestamp()]},
        "Clients": {"cols": ["id","company_name","contact_name","email","phone","industry","website","status","created_at"], "gen": lambda i: [i,pick("Tech Corp","StartupXYZ","Global Inc","Digital Co","Smart Solutions"),name(),email(),phone(),pick("Technology","Healthcare","Finance","Retail","Education"),f"https://client{i}.com",pick(*STATUS),timestamp()]},
        "Developers": {"cols": ["id","name","email","role","skills","experience","hourly_rate","is_active"], "gen": lambda i: [i,name(),email(),pick("Frontend","Backend","Full Stack","DevOps","Mobile","UI/UX"),pick("Python,React","Java,Spring","Node,Vue","PHP,Laravel","Flutter,Dart"),f"{num(1,20)} years",price(20,200),bool_val()]},
        "Tasks": {"cols": ["id","project_id","assigned_to","title","description","priority","status","due_date"], "gen": lambda i: [i,num(1,50),num(1,30),lorem(6),lorem(15),pick("low","medium","high","critical"),pick(*STATUS),date("2025-01-01","2025-12-31")]},
        "Invoices": {"cols": ["id","client_id","project_id","amount","tax","total","status","date","due_date"], "gen": lambda i: [i,num(1,100),num(1,50),price(1000,100000),price(100,10000),price(1100,110000),pick(*STATUS),date("2025-01-01","2025-06-30"),date("2025-07-01","2025-12-31")]},
        "Sprints": {"cols": ["id","project_id","name","start_date","end_date","velocity","status","goals"], "gen": lambda i: [i,num(1,50),f"Sprint {i}",date("2025-01-01","2025-06-30"),date("2025-07-01","2025-12-31"),num(10,100),pick(*STATUS),lorem(10)]},
        "Technologies": {"cols": ["id","name","category","version","is_active","usage_count"], "gen": lambda i: [i,pick("Python","JavaScript","React","Django","PostgreSQL","Docker","AWS","Node.js"),pick("language","framework","database","devops","cloud"),pick("3.13","18.0","17.0","5.2","16.0","24.0","v2","22.0"),bool_val(),num(1,50)]},
    }
},
"personal": {
    "title": "Personal_Services_Database",
    "sheets": {
        "Customers": {"cols": ["id","name","email","phone","address","membership_type","loyalty_points","created_at"], "gen": lambda i: [i,name(),email(),phone(),address(),pick("basic","premium","vip","none"),num(0,2000),timestamp()]},
        "Services": {"cols": ["id","name","category","description","price","duration","is_active"], "gen": lambda i: [i,pick("Haircut","Massage","Facial","Manicure","Pedicure","Waxing","Makeup","Spa"),pick("hair","skin","body","nails","beauty","wellness"),lorem(10),price(10,500),pick("30m","1h","1.5h","2h"),bool_val()]},
        "Appointments": {"cols": ["id","customer_id","service_id","staff_id","date","time","status","notes"], "gen": lambda i: [i,num(1,200),num(1,20),num(1,15),date("2025-01-01","2025-12-31"),f"{random.randint(9,20):02d}:{random.choice(['00','30'])}",pick(*STATUS),lorem(5)]},
        "Staff": {"cols": ["id","name","email","phone","specialization","rating","is_active"], "gen": lambda i: [i,name(),email(),phone(),pick("Hair","Skin","Nails","Massage","Makeup","Spa"),round(random.uniform(3,5),1),bool_val()]},
        "Payments": {"cols": ["id","customer_id","appointment_id","amount","tip","total","method","status","paid_at"], "gen": lambda i: [i,num(1,200),num(1,200),price(10,500),price(0,100),price(10,600),pick(*PAYMENT),pick(*STATUS),timestamp()]},
        "Products": {"cols": ["id","name","brand","category","price","stock","is_active"], "gen": lambda i: [i,pick("Shampoo","Conditioner","Face Cream","Perfume","Hair Oil","Serum","Lotion"),pick("L'Oreal","Dove","Olay","Pantene","Nivea"),pick("hair","skin","fragrance","body"),price(5,200),num(0,500),bool_val()]},
        "Reviews": {"cols": ["id","customer_id","service_id","rating","comment","created_at"], "gen": lambda i: [i,num(1,200),num(1,20),num(1,5),lorem(15),timestamp()]},
    }
},
"manufacturing": {
    "title": "Manufacturing_Database",
    "sheets": {
        "Products": {"cols": ["id","name","sku","category","unit_cost","selling_price","min_order","is_active","created_at"], "gen": lambda i: [i,f"Product {i}",f"MFG-{random.randint(10000,99999)}",pick("garment","furniture","food","packaging","electrical","chemical"),price(5,500),price(10,1000),num(10,1000),bool_val(),timestamp()]},
        "Orders": {"cols": ["id","customer_id","product_id","quantity","unit_price","total","status","delivery_date","created_at"], "gen": lambda i: [i,num(1,100),num(1,50),num(10,10000),price(5,500),price(50,500000),pick(*STATUS),date("2025-01-01","2025-12-31"),timestamp()]},
        "Suppliers": {"cols": ["id","name","material","email","phone","rating","lead_time","is_active"], "gen": lambda i: [i,pick("Raw Materials Co","Supply Chain Inc","Quality Parts","Metal Works","Chem Base"),pick("steel","plastic","fabric","wood","chemical"),email(),phone(),round(random.uniform(1,5),1),f"{num(1,30)} days",bool_val()]},
        "Raw_Materials": {"cols": ["id","name","supplier_id","unit","cost_per_unit","stock","reorder_level","last_ordered"], "gen": lambda i: [i,pick("Steel","Plastic","Fabric","Wood","Rubber","Glass","Aluminum"),num(1,30),pick("kg","ton","liter","meter","piece"),price(1,100),num(0,10000),num(100,1000),date("2025-01-01","2025-12-31")]},
        "Production": {"cols": ["id","product_id","quantity","start_date","end_date","status","quality_check","notes"], "gen": lambda i: [i,num(1,50),num(10,10000),date("2025-01-01","2025-06-30"),date("2025-07-01","2025-12-31"),pick(*STATUS),pick("passed","failed","pending"),lorem(10)]},
        "Quality": {"cols": ["id","product_id","batch_number","inspector","result","defects","score","date"], "gen": lambda i: [i,num(1,50),f"BATCH-{random.randint(1000,9999)}",name(),pick("passed","failed","conditional"),num(0,50),num(1,100),date("2025-01-01","2025-12-31")]},
        "Shipments": {"cols": ["id","order_id","carrier","tracking","status","shipped_at","delivered_at","weight"], "gen": lambda i: [i,num(1,100),pick("DHL","FedEx","UPS","Local"),f"TRK-{random.randint(100000,999999)}",pick(*STATUS),timestamp(),timestamp(),round(random.uniform(1,500),2)]},
    }
},
"agriculture": {
    "title": "Agriculture_Farm_Database",
    "sheets": {
        "Crops": {"cols": ["id","name","variety","area_acres","planted_date","harvest_date","yield_kg","status"], "gen": lambda i: [i,pick("Wheat","Rice","Corn","Soybean","Cotton","Sugarcane","Potato","Tomato"),pick("hybrid","organic","local","improved"),round(random.uniform(1,100),1),date("2025-01-01","2025-06-30"),date("2025-07-01","2025-12-31"),num(100,50000),pick(*STATUS)]},
        "Livestock": {"cols": ["id","type","breed","quantity","health_status","feed_type","last_vet_check","is_active"], "gen": lambda i: [i,pick("cattle","poultry","goat","sheep","fish","pig"),pick("local","hybrid","imported","desi"),num(1,200),pick("healthy","sick","recovering","quarantine"),pick("grass","grain","mixed","commercial"),date("2025-01-01","2025-12-31"),bool_val()]},
        "Equipment": {"cols": ["id","name","type","purchase_date","cost","condition","last_service","is_active"], "gen": lambda i: [i,pick("Tractor","Harvester","Plough","Sprayer","Thresher","Pump"),pick("heavy","medium","light"),date("2015-01-01","2025-01-01"),price(5000,500000),pick("excellent","good","fair","needs_repair"),date("2025-01-01","2025-12-31"),bool_val()]},
        "Sales": {"cols": ["id","product","buyer","quantity","unit_price","total","date","payment_status"], "gen": lambda i: [i,pick("Wheat","Rice","Corn","Vegetables","Milk","Eggs"),name(),num(1,10000),price(1,50),price(10,500000),date("2025-01-01","2025-12-31"),pick("paid","pending","partial")]},
        "Suppliers": {"cols": ["id","name","product","email","phone","rating","is_active"], "gen": lambda i: [i,pick("AgriSupply","FarmPlus","GreenGrow","SeedCorp","FertilMax"),pick("seeds","fertilizer","pesticide","equipment","feed"),email(),phone(),round(random.uniform(1,5),1),bool_val()]},
        "Workers": {"cols": ["id","name","phone","role","daily_wage","start_date","is_active"], "gen": lambda i: [i,name(),phone(),pick("farmer","laborer","supervisor","driver","cook"),price(200,1500),date("2025-01-01","2025-12-31"),bool_val()]},
        "Expenses": {"cols": ["id","category","description","amount","date","status"], "gen": lambda i: [i,pick("seeds","fertilizer","labor","fuel","irrigation","pesticide"),lorem(10),price(100,50000),date("2025-01-01","2025-12-31"),pick(*STATUS)]},
    }
},
"automotive": {
    "title": "Automotive_Database",
    "sheets": {
        "Vehicles": {"cols": ["id","make","model","year","color","vin","price","status","mileage","created_at"], "gen": lambda i: [i,pick("Toyota","Honda","Ford","BMW","Mercedes","Hyundai","Mahindra","Tata"),pick("Sedan","SUV","Hatchback","Truck","Coupe"),num(2010,2025),pick("Red","Blue","White","Black","Silver"),f"VIN{random.randint(100000,999999)}",price(5000,100000),pick(*STATUS),num(0,200000),timestamp()]},
        "Customers": {"cols": ["id","name","email","phone","address","license_number","created_at"], "gen": lambda i: [i,name(),email(),phone(),address(),f"DL-{random.randint(100000,999999)}",timestamp()]},
        "Services": {"cols": ["id","vehicle_id","customer_id","service_type","description","cost","date","status","mechanic_id"], "gen": lambda i: [i,num(1,100),num(1,200),pick("oil_change","tire_rotation","brake_repair","engine_repair","inspection","wash"),lorem(10),price(50,5000),date("2025-01-01","2025-12-31"),pick(*STATUS),num(1,30)]},
        "Parts": {"cols": ["id","name","sku","category","price","stock","supplier","is_active"], "gen": lambda i: [i,pick("Brake Pad","Oil Filter","Spark Plug","Battery","Tire","Alternator","Radiator"),f"PT-{random.randint(10000,99999)}",pick("engine","brake","electrical","body","interior"),price(5,500),num(0,500),pick("AutoParts Inc","CarSupply Co","MechParts"),bool_val()]},
        "Appointments": {"cols": ["id","customer_id","vehicle_id","date","time","type","status","notes"], "gen": lambda i: [i,num(1,200),num(1,100),date("2025-01-01","2025-12-31"),f"{random.randint(8,18):02d}:00",pick("service","inspection","repair","wash"),pick(*STATUS),lorem(5)]},
        "Invoices": {"cols": ["id","customer_id","service_id","parts_cost","labor_cost","tax","total","status","date"], "gen": lambda i: [i,num(1,200),num(1,200),price(10,2000),price(20,1000),price(5,300),price(35,3300),pick(*STATUS),date("2025-01-01","2025-12-31")]},
        "Mechanics": {"cols": ["id","name","email","phone","specialization","experience","rating","is_active"], "gen": lambda i: [i,name(),email(),phone(),pick("engine","electrical","body","transmission","general"),f"{num(1,25)} years",round(random.uniform(3,5),1),bool_val()]},
    }
},
}
