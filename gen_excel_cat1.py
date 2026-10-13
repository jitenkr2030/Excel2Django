"""Category schemas: accounting, retail, food, education, logistics."""
import random
from data_pools import name, email, phone, city, address, date, timestamp, price, num, pick, bool_val, lorem, STATUS, PAYMENT, CITIES

SCHEMAS = {
"accounting": {
    "title": "Accounting_Firm_Database",
    "sheets": {
        "Clients": {"cols": ["id","name","email","phone","company","type","status","created_at"], "gen": lambda i: [i,name(),email(),phone(),pick("ABC Corp","XYZ Ltd","Tech Co","Smith & Co","Global Inc"),pick("individual","business","corporate"),pick(*STATUS),timestamp()]},
        "Services": {"cols": ["id","service_name","category","rate","duration","is_active"], "gen": lambda i: [i,pick("Tax Filing","Audit","Bookkeeping","Payroll","GST Filing","Compliance","Advisory"),pick("tax","audit","compliance","advisory","payroll","gst"),price(100,5000),pick("1h","2h","1d","1w","1m"),bool_val()]},
        "Invoices": {"cols": ["id","client_id","invoice_number","amount","tax","total","status","date"], "gen": lambda i: [i,num(1,200),f"INV-{2025}-{random.randint(10000,99999)}",price(100,50000),price(10,5000),price(110,55000),pick(*STATUS),date("2025-01-01","2025-12-31")]},
        "Tax_Filings": {"cols": ["id","client_id","filing_type","tax_year","amount","status","filed_date","deadline"], "gen": lambda i: [i,num(1,200),pick("GST","Income Tax","TDS","Corporate","VAT"),pick(2023,2024,2025),price(1000,500000),pick(*STATUS),date("2025-01-01","2025-06-30"),date("2025-07-01","2025-12-31")]},
        "Appointments": {"cols": ["id","client_id","date","time","purpose","status","notes"], "gen": lambda i: [i,num(1,200),date("2025-01-01","2025-12-31"),f"{random.randint(9,17):02d}:{random.choice(['00','30'])}",pick("consultation","review","filing","audit"),pick(*STATUS),lorem(10)]},
        "Staff": {"cols": ["id","name","email","role","specialization","hire_date","is_active"], "gen": lambda i: [i,name(),email(),pick("CA","Accountant","Auditor","Admin","Junior"),pick("tax","audit","compliance","payroll"),date("2018-01-01","2025-01-01"),bool_val()]},
        "Expenses": {"cols": ["id","category","description","amount","date","status"], "gen": lambda i: [i,pick("office","travel","software","training","advertising"),lorem(10),price(10,5000),date("2025-01-01","2025-12-31"),pick(*STATUS)]},
    }
},
"retail": {
    "title": "Retail_Store_Database",
    "sheets": {
        "Products": {"cols": ["id","name","sku","category","price","cost","stock","brand","is_active","created_at"], "gen": lambda i: [i,f"Product {i}",f"SKU-{random.randint(10000,99999)}",pick("Electronics","Clothing","Home","Food","Sports"),price(5,2000),price(2,1000),num(0,1000),pick("Nike","Adidas","Samsung","Apple","Sony"),bool_val(),timestamp()]},
        "Customers": {"cols": ["id","name","email","phone","address","loyalty_points","tier","created_at"], "gen": lambda i: [i,name(),email(),phone(),address(),num(0,5000),pick("Bronze","Silver","Gold","Platinum"),timestamp()]},
        "Orders": {"cols": ["id","customer_id","order_number","total","status","payment_method","created_at","shipped_at"], "gen": lambda i: [i,num(1,200),f"ORD-{random.randint(10000,99999)}",price(10,5000),pick(*STATUS),pick(*PAYMENT),timestamp(),timestamp()]},
        "Order_Items": {"cols": ["id","order_id","product_id","quantity","unit_price","total"], "gen": lambda i: [i,num(1,200),num(1,100),num(1,5),price(5,500),price(5,1000)]},
        "Inventory": {"cols": ["id","product_id","warehouse","quantity","reorder_level","last_restocked"], "gen": lambda i: [i,num(1,100),pick("Main","East","West","Central"),num(0,500),num(10,50),date("2025-01-01","2025-12-31")]},
        "Suppliers": {"cols": ["id","name","contact","email","phone","rating","is_active"], "gen": lambda i: [i,pick("Global Supply","Tech Parts","Fast Delivery","Quality Goods","Pro Supplies"),name(),email(),phone(),round(random.uniform(1,5),1),bool_val()]},
        "Payments": {"cols": ["id","order_id","amount","method","status","paid_at","transaction_id"], "gen": lambda i: [i,num(1,200),price(10,5000),pick(*PAYMENT),pick(*STATUS),timestamp(),f"TXN-{random.randint(100000,999999)}"]},
    }
},
"food": {
    "title": "Restaurant_Database",
    "sheets": {
        "Menu_Items": {"cols": ["id","name","category","description","price","is_veg","is_active"], "gen": lambda i: [i,pick("Pizza","Burger","Pasta","Salad","Sushi","Tacos","Steak","Curry"),pick("appetizer","main","dessert","beverage","special"),lorem(10),price(5,50),bool_val(),bool_val()]},
        "Customers": {"cols": ["id","name","email","phone","address","loyalty_points","created_at"], "gen": lambda i: [i,name(),email(),phone(),address(),num(0,500),timestamp()]},
        "Orders": {"cols": ["id","customer_id","order_number","items","total","status","type","created_at"], "gen": lambda i: [i,num(1,200),f"ORD-{random.randint(10000,99999)}",num(1,10),price(10,200),pick(*STATUS),pick("dine_in","takeaway","delivery"),timestamp()]},
        "Reservations": {"cols": ["id","customer_id","date","time","guests","table","status","notes"], "gen": lambda i: [i,num(1,200),date("2025-01-01","2025-12-31"),f"{random.randint(11,22):02d}:00",num(1,12),f"T{random.randint(1,30)}",pick(*STATUS),lorem(5)]},
        "Staff": {"cols": ["id","name","role","email","phone","shift","salary","is_active"], "gen": lambda i: [i,name(),pick("Chef","Waiter","Manager","Cashier","Cleaner","Bartender"),email(),phone(),pick("morning","evening","night"),price(15000,80000),bool_val()]},
        "Suppliers": {"cols": ["id","name","product","email","phone","rating","is_active"], "gen": lambda i: [i,pick("Fresh Farm","Ocean Catch","Green Valley","Quality Meats","Dairy Plus"),pick("vegetables","meat","dairy","beverages","spices"),email(),phone(),round(random.uniform(1,5),1),bool_val()]},
        "Reviews": {"cols": ["id","customer_id","rating","comment","food_rating","service_rating","created_at"], "gen": lambda i: [i,num(1,200),num(1,5),lorem(15),num(1,5),num(1,5),timestamp()]},
    }
},
"education": {
    "title": "Education_Institute_Database",
    "sheets": {
        "Students": {"cols": ["id","name","email","phone","course_id","enrollment_date","status","grade"], "gen": lambda i: [i,name(),email(),phone(),num(1,20),date("2025-01-01","2025-06-30"),pick(*STATUS),pick("A+","A","B+","B","C","D","F")]},
        "Courses": {"cols": ["id","name","category","description","duration","fee","max_students","is_active"], "gen": lambda i: [i,pick("Python","Java","Math","English","Physics","Chemistry","Biology","Design"),pick("tech","science","language","arts","business"),lorem(10),pick("1 month","3 months","6 months","1 year"),price(500,50000),num(10,100),bool_val()]},
        "Enrollments": {"cols": ["id","student_id","course_id","date","status","payment_status"], "gen": lambda i: [i,num(1,200),num(1,20),date("2025-01-01","2025-12-31"),pick(*STATUS),pick("paid","pending","partial","refunded")]},
        "Teachers": {"cols": ["id","name","email","phone","specialization","experience","is_active"], "gen": lambda i: [i,name(),email(),phone(),pick("Math","Science","English","Computer","Arts"),f"{num(1,25)} years",bool_val()]},
        "Payments": {"cols": ["id","student_id","amount","type","status","date","method"], "gen": lambda i: [i,num(1,200),price(500,50000),pick("tuition","exam","materials","registration"),pick(*STATUS),date("2025-01-01","2025-12-31"),pick(*PAYMENT)]},
        "Attendance": {"cols": ["id","student_id","course_id","date","status","notes"], "gen": lambda i: [i,num(1,200),num(1,20),date("2025-01-01","2025-12-31"),pick("present","absent","late","excused"),lorem(5)]},
        "Exams": {"cols": ["id","course_id","name","date","max_marks","pass_marks","is_active"], "gen": lambda i: [i,num(1,20),pick("Midterm","Final","Quiz","Assignment","Project"),date("2025-01-01","2025-12-31"),num(50,100),num(25,50),bool_val()]},
    }
},
"logistics": {
    "title": "Logistics_Transport_Database",
    "sheets": {
        "Customers": {"cols": ["id","name","email","phone","company","address","status"], "gen": lambda i: [i,name(),email(),phone(),pick("ABC Corp","XYZ Ltd","Tech Co","Global Inc"),address(),pick(*STATUS)]},
        "Shipments": {"cols": ["id","tracking_number","sender_id","receiver_id","origin","destination","weight","status","created_at"], "gen": lambda i: [i,f"TRK-{random.randint(100000,999999)}",num(1,200),num(1,200),city()[0],city()[0],round(random.uniform(0.1,500),2),pick(*STATUS),timestamp()]},
        "Vehicles": {"cols": ["id","type","plate_number","capacity","driver_id","status","last_service"], "gen": lambda i: [i,pick("truck","van","car","bike","trailer"),f"ABC-{random.randint(1000,9999)}",f"{num(1,50)} tons",num(1,50),pick("active","maintenance","idle"),date("2025-01-01","2025-12-31")]},
        "Drivers": {"cols": ["id","name","phone","license_number","experience","is_active"], "gen": lambda i: [i,name(),phone(),f"DL-{random.randint(100000,999999)}",f"{num(1,25)} years",bool_val()]},
        "Routes": {"cols": ["id","origin","destination","distance_km","estimated_time","status"], "gen": lambda i: [i,city()[0],city()[0],num(10,5000),f"{num(1,48)} hours",pick(*STATUS)]},
        "Invoices": {"cols": ["id","customer_id","shipment_id","amount","tax","total","status","date"], "gen": lambda i: [i,num(1,200),num(1,200),price(50,5000),price(5,500),price(55,5500),pick(*STATUS),date("2025-01-01","2025-12-31")]},
        "Maintenance": {"cols": ["id","vehicle_id","type","description","cost","date","status"], "gen": lambda i: [i,num(1,50),pick("oil_change","tire","brake","engine","body"),lorem(10),price(50,5000),date("2025-01-01","2025-12-31"),pick(*STATUS)]},
    }
},
}
