Here is the complete `README.md` content — copy everything below the line:

---

# 🏗️ Excel-to-Django Generator

> **One Excel sheet in → Full-stack web app out.**
> Generate domain-aware Excel databases with demo data, then auto-generate a complete Django + DRF backend and responsive frontend.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 📊 **Excel Generator** | Generate multi-sheet Excel databases with realistic demo data |
| 🏭 **26 Domains** | Pre-built schemas for 26 industry categories |
| 🏢 **400+ Business Types** | Generate for specific businesses (Restaurant, Clinic, Law Firm, etc.) |
| 🐍 **Django Backend** | Auto-generated models, views, serializers, URLs, admin |
| 🖥️ **Frontend** | Responsive HTML templates with domain-themed CSS |
| 🔐 **Permissions** | Role-based access control with DRF permission classes |
| 📈 **Analytics** | Charts dashboard + CSV export |
| 🐳 **Docker** | Dockerfile + docker-compose + Makefile |
| 📱 **PWA** | Manifest + service worker for offline support |
| 🧪 **Tests** | Auto-generated auth, permissions, API, and model tests |

---

## 🚀 Quick Start

### 1. Generate Excel Database

```bash
# By business name
python excel_generator.py --business "Restaurant" --rows 50

# By domain
python excel_generator.py --domain healthcare --rows 100

# All domains at once
python excel_generator.py --domain all --rows 50

# List all 26 domains + 400 businesses
python excel_generator.py --list
```

### 2. Generate Django App from Excel

```bash
python app.py \
  --input generated_excel/Restaurant_Database.xlsx \
  --output myapp \
  --project-name MyRestaurant
```

### 3. Run

```bash
cd myapp
pip install -r requirements.txt
python manage.py makemigrations portal
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0.0.0.0:8000
```

### 4. Open Browser

- **Frontend**: `http://localhost:8000`
- **Admin Panel**: `http://localhost:8000/admin`
- **API Root**: `http://localhost:8000/api/`
- **Analytics**: `http://localhost:8000/charts/`

---

## 📂 Project Structure

```
excel_to_django_generator/
│
├── excel_generator.py          # Excel database generator CLI
├── app.py                      # Excel → Django app generator
├── excel2frontend.py           # Excel → Frontend-only generator
│
├── data_pools.py               # Shared demo data (names, cities, etc.)
├── gen_excel_engine.py         # Excel generation engine
├── gen_excel_biztypes.py       # 400 business type mappings
├── gen_excel_schemas.py        # Domain schemas (core)
├── gen_excel_schemas2.py       # Domain schemas (extended)
├── gen_excel_schemas3.py       # Domain schemas (final)
├── gen_excel_cat1.py           # Accounting, Retail, Food, Education, Logistics
├── gen_excel_cat2.py           # IT, Personal, Manufacturing, Agriculture, Automotive
├── gen_excel_cat3.py           # Agency, Creative, Travel, Pets, Industrial, Government
│
├── gen_models.py               # Django models generator
├── gen_views.py                # Django views generator
├── gen_api.py                  # DRF serializers + viewsets
├── gen_templates.py            # HTML templates generator
├── gen_frontend.py             # Frontend generator
├── gen_css.py                  # Domain-themed CSS generator
├── gen_pages.py                # Pages generator
├── gen_permissions.py          # Role-based permissions
├── gen_charts.py               # Analytics charts
├── gen_tests.py                # Test suite generator
├── gen_docker.py               # Docker config generator
├── gen_pwa.py                  # PWA manifest + service worker
├── gen_project.py              # Django project scaffolding
│
├── helpers.py                  # Shared utilities
├── analyser.py                 # Excel analyser
│
├── generated_excel/            # All generated Excel files
└── excel_files/                # Sample Excel files
```

---

## 📊 Supported Domains (26)

### Original (10)

| Domain | Title | Sheets |
|--------|-------|:------:|
| `dating` | Dating App | 12 |
| `legal` | Law Firm / Legal Practice | 8 |
| `health` | Health Vault | 8 |
| `ecommerce` | E-Commerce Platform | 8 |
| `finance` | Loan Marketplace | 7 |
| `business` | Business Management | 7 |
| `skill` | Skill Market | 6 |
| `marketing` | Marketing Sales Portal | 7 |
| `property` | Property Construction | 6 |
| `creator` | FansXcluziv | 9 |

### Business Categories (16)

| Domain | Title | Sheets |
|--------|-------|:------:|
| `accounting` | Accounting Firm | 7 |
| `retail` | Retail Store | 7 |
| `food` | Restaurant | 7 |
| `education` | Education Institute | 7 |
| `logistics` | Logistics Transport | 7 |
| `it_digital` | IT Digital Services | 7 |
| `personal` | Personal Services | 7 |
| `manufacturing` | Manufacturing | 7 |
| `agriculture` | Agriculture Farm | 7 |
| `automotive` | Automotive | 7 |
| `agency` | Agency | 6 |
| `creative` | Creative Studio | 6 |
| `travel` | Travel Tourism | 6 |
| `pets` | Pet Services | 7 |
| `industrial` | Industrial Services | 6 |
| `government` | Legal Compliance | 7 |

---

## 🏢 400+ Business Types

Generate Excel for any specific business:

### Finance & Accounting (1-20)

```bash
python excel_generator.py --business "Accounting Firm"
python excel_generator.py --business "GST Practitioner"
python excel_generator.py --business "Tax Consultant"
python excel_generator.py --business "CA Practice"
python excel_generator.py --business "Bookkeeping Service"
python excel_generator.py --business "Payroll Service"
python excel_generator.py --business "Invoice Management Business"
python excel_generator.py --business "Billing Software Business"
python excel_generator.py --business "Financial Consultancy"
python excel_generator.py --business "Loan Consultancy"
python excel_generator.py --business "Insurance Agency"
python excel_generator.py --business "Investment Advisory"
python excel_generator.py --business "Mutual Fund Distribution"
python excel_generator.py --business "Credit Consultancy"
python excel_generator.py --business "Debt Recovery Agency"
python excel_generator.py --business "Audit Firm"
python excel_generator.py --business "Company Registration Service"
python excel_generator.py --business "Trademark Consultancy"
python excel_generator.py --business "Business Compliance Service"
python excel_generator.py --business "Virtual CFO Service"
```

### Retail & Trading (21-40)

```bash
python excel_generator.py --business "Grocery Store"
python excel_generator.py --business "Supermarket"
python excel_generator.py --business "Pharmacy"
python excel_generator.py --business "Electronics Shop"
python excel_generator.py --business "Mobile Shop"
python excel_generator.py --business "Computer Shop"
python excel_generator.py --business "Hardware Store"
python excel_generator.py --business "Furniture Store"
python excel_generator.py --business "Clothing Store"
python excel_generator.py --business "Footwear Store"
python excel_generator.py --business "Jewellery Store"
python excel_generator.py --business "Automobile Parts Store"
python excel_generator.py --business "Stationery Store"
python excel_generator.py --business "Book Store"
python excel_generator.py --business "Toy Store"
python excel_generator.py --business "Sports Shop"
python excel_generator.py --business "Hardware & Sanitary Store"
python excel_generator.py --business "Paint Store"
python excel_generator.py --business "Electrical Store"
python excel_generator.py --business "Building Material Store"
```

### Food & Hospitality (41-60)

```bash
python excel_generator.py --business "Restaurant"
python excel_generator.py --business "Cafe"
python excel_generator.py --business "Bakery"
python excel_generator.py --business "Cloud Kitchen"
python excel_generator.py --business "Tiffin Service"
python excel_generator.py --business "Catering Business"
python excel_generator.py --business "Food Truck"
python excel_generator.py --business "Sweet Shop"
python excel_generator.py --business "Juice Shop"
python excel_generator.py --business "Fast Food Shop"
python excel_generator.py --business "Hotel"
python excel_generator.py --business "Guest House"
python excel_generator.py --business "Homestay"
python excel_generator.py --business "Hostel"
python excel_generator.py --business "Resort"
python excel_generator.py --business "Banquet Hall"
python excel_generator.py --business "Wedding Catering"
python excel_generator.py --business "Event Catering"
python excel_generator.py --business "Restaurant Delivery"
python excel_generator.py --business "Restaurant Franchise"
```

### Healthcare (61-80)

```bash
python excel_generator.py --business "General Clinic"
python excel_generator.py --business "Dental Clinic"
python excel_generator.py --business "Eye Clinic"
python excel_generator.py --business "Physiotherapy Clinic"
python excel_generator.py --business "Diagnostic Lab"
python excel_generator.py --business "Pathology Lab"
python excel_generator.py --business "Pharmacy"
python excel_generator.py --business "Veterinary Clinic"
python excel_generator.py --business "Nursing Home"
python excel_generator.py --business "Hospital"
python excel_generator.py --business "Ambulance Service"
python excel_generator.py --business "Home Healthcare"
python excel_generator.py --business "Medical Equipment Rental"
python excel_generator.py --business "Medical Distributor"
python excel_generator.py --business "Healthcare Consultancy"
python excel_generator.py --business "Elder Care Service"
python excel_generator.py --business "Fitness & Wellness Centre"
python excel_generator.py --business "Nutrition Consultancy"
python excel_generator.py --business "Medical Appointment Service"
python excel_generator.py --business "Healthcare Staffing Agency"
```

### Education (81-100)

```bash
python excel_generator.py --business "School"
python excel_generator.py --business "Coaching Institute"
python excel_generator.py --business "Computer Institute"
python excel_generator.py --business "Skill Training Centre"
python excel_generator.py --business "Tuition Centre"
python excel_generator.py --business "Language Institute"
python excel_generator.py --business "Competitive Exam Institute"
python excel_generator.py --business "Music School"
python excel_generator.py --business "Dance Academy"
python excel_generator.py --business "Art School"
python excel_generator.py --business "Vocational Training Centre"
python excel_generator.py --business "Driving School"
python excel_generator.py --business "Online Course Business"
python excel_generator.py --business "EdTech Startup"
python excel_generator.py --business "Educational Consultancy"
python excel_generator.py --business "Study Abroad Consultancy"
python excel_generator.py --business "Career Counselling"
python excel_generator.py --business "Home Tutor Agency"
python excel_generator.py --business "Exam Preparation Business"
python excel_generator.py --business "Corporate Training Business"
```

### Logistics & Transport (101-120)

```bash
python excel_generator.py --business "Courier Company"
python excel_generator.py --business "Local Delivery Service"
python excel_generator.py --business "Transport Company"
python excel_generator.py --business "Trucking Business"
python excel_generator.py --business "Fleet Management Company"
python excel_generator.py --business "Taxi Service"
python excel_generator.py --business "Cab Agency"
python excel_generator.py --business "Car Rental"
python excel_generator.py --business "Bike Rental"
python excel_generator.py --business "Bus Operator"
python excel_generator.py --business "Travel Agency"
python excel_generator.py --business "Tour Operator"
python excel_generator.py --business "Freight Forwarder"
python excel_generator.py --business "Warehouse Business"
python excel_generator.py --business "Cold Storage"
python excel_generator.py --business "Packers & Movers"
python excel_generator.py --business "E-commerce Delivery"
python excel_generator.py --business "Last-Mile Delivery"
python excel_generator.py --business "Logistics Consultancy"
python excel_generator.py --business "Driver Recruitment Agency"
```

### Property & Construction (121-140)

```bash
python excel_generator.py --business "Real Estate Agency"
python excel_generator.py --business "Property Dealer"
python excel_generator.py --business "Property Rental Agency"
python excel_generator.py --business "Property Management"
python excel_generator.py --business "Construction Company"
python excel_generator.py --business "Civil Contractor"
python excel_generator.py --business "Electrical Contractor"
python excel_generator.py --business "Plumbing Contractor"
python excel_generator.py --business "Interior Design Business"
python excel_generator.py --business "Architecture Firm"
python excel_generator.py --business "Building Material Supplier"
python excel_generator.py --business "Paint Contractor"
python excel_generator.py --business "Furniture Contractor"
python excel_generator.py --business "Modular Kitchen Business"
python excel_generator.py --business "Home Renovation Business"
python excel_generator.py --business "Facility Management"
python excel_generator.py --business "Security Agency"
python excel_generator.py --business "Cleaning Service"
python excel_generator.py --business "Pest Control Business"
python excel_generator.py --business "Landscaping Business"
```

### IT & Digital Services (141-160)

```bash
python excel_generator.py --business "Web Development Agency"
python excel_generator.py --business "Software Development Company"
python excel_generator.py --business "SaaS Startup"
python excel_generator.py --business "Digital Marketing Agency"
python excel_generator.py --business "SEO Agency"
python excel_generator.py --business "Social Media Agency"
python excel_generator.py --business "Graphic Design Agency"
python excel_generator.py --business "Video Production Agency"
python excel_generator.py --business "IT Support Company"
python excel_generator.py --business "Cloud Consultancy"
python excel_generator.py --business "Cybersecurity Service"
python excel_generator.py --business "Data Analytics Consultancy"
python excel_generator.py --business "AI Consultancy"
python excel_generator.py --business "Software Training Institute"
python excel_generator.py --business "Hosting Business"
python excel_generator.py --business "Domain Reseller"
python excel_generator.py --business "WordPress Agency"
python excel_generator.py --business "App Development Agency"
python excel_generator.py --business "Automation Agency"
python excel_generator.py --business "Freelancing Agency"
```

### Personal & Professional Services (161-180)

```bash
python excel_generator.py --business "Salon"
python excel_generator.py --business "Beauty Parlour"
python excel_generator.py --business "Spa"
python excel_generator.py --business "Gym"
python excel_generator.py --business "Yoga Studio"
python excel_generator.py --business "Photography Studio"
python excel_generator.py --business "Wedding Photographer"
python excel_generator.py --business "Event Planner"
python excel_generator.py --business "Makeup Artist"
python excel_generator.py --business "Tailoring Business"
python excel_generator.py --business "Laundry Service"
python excel_generator.py --business "Dry Cleaning Service"
python excel_generator.py --business "Car Wash"
python excel_generator.py --business "Automobile Service Centre"
python excel_generator.py --business "Bike Service Centre"
python excel_generator.py --business "Driving Instructor"
python excel_generator.py --business "Security Guard Agency"
python excel_generator.py --business "Domestic Help Agency"
python excel_generator.py --business "Repair Service Business"
python excel_generator.py --business "Appliance Repair Business"
```

### Manufacturing & B2B (181-200)

```bash
python excel_generator.py --business "Garment Manufacturer"
python excel_generator.py --business "Furniture Manufacturer"
python excel_generator.py --business "Food Manufacturer"
python excel_generator.py --business "Packaging Company"
python excel_generator.py --business "Printing Press"
python excel_generator.py --business "Pharmaceutical Distributor"
python excel_generator.py --business "FMCG Distributor"
python excel_generator.py --business "Electrical Manufacturer"
python excel_generator.py --business "Electronics Manufacturer"
python excel_generator.py --business "Auto Parts Manufacturer"
python excel_generator.py --business "Machine Manufacturer"
python excel_generator.py --business "Steel Fabrication Business"
python excel_generator.py --business "Plastic Manufacturing"
python excel_generator.py --business "Chemical Manufacturing"
python excel_generator.py --business "Construction Material Manufacturer"
python excel_generator.py --business "Wholesale Distributor"
python excel_generator.py --business "Import-Export Business"
python excel_generator.py --business "B2B Marketplace"
python excel_generator.py --business "Procurement Agency"
python excel_generator.py --business "Industrial Supply Business"
```

### Agriculture & Farming (201-225)

```bash
python excel_generator.py --business "Dairy Farm"
python excel_generator.py --business "Poultry Farm"
python excel_generator.py --business "Goat Farm"
python excel_generator.py --business "Fish Farming"
python excel_generator.py --business "Beekeeping Business"
python excel_generator.py --business "Mushroom Farming"
python excel_generator.py --business "Organic Farm"
python excel_generator.py --business "Hydroponic Farm"
python excel_generator.py --business "Nursery & Plant Business"
python excel_generator.py --business "Seed Supplier"
python excel_generator.py --business "Fertilizer Dealer"
python excel_generator.py --business "Pesticide Dealer"
python excel_generator.py --business "Agricultural Equipment Rental"
python excel_generator.py --business "Tractor Rental"
python excel_generator.py --business "Farm Machinery Repair"
python excel_generator.py --business "Irrigation Equipment Business"
python excel_generator.py --business "Agricultural Consultancy"
python excel_generator.py --business "Crop Trading Business"
python excel_generator.py --business "Grain Wholesale Business"
python excel_generator.py --business "Cold Chain Business"
python excel_generator.py --business "Dairy Collection Centre"
python excel_generator.py --business "Milk Delivery Business"
python excel_generator.py --business "Animal Feed Business"
python excel_generator.py --business "Farm Produce Marketplace"
python excel_generator.py --business "Agricultural Export Business"
```

### E-commerce & Online Commerce (226-250)

```bash
python excel_generator.py --business "Fashion Marketplace"
python excel_generator.py --business "Handmade Products Store"
python excel_generator.py --business "Organic Products Store"
python excel_generator.py --business "Pet Products Store"
python excel_generator.py --business "Subscription Box Business"
python excel_generator.py --business "Gift Marketplace"
python excel_generator.py --business "Custom Merchandise Business"
python excel_generator.py --business "Print-on-Demand Business"
python excel_generator.py --business "Second-Hand Marketplace"
python excel_generator.py --business "Used Electronics Marketplace"
python excel_generator.py --business "Used Furniture Marketplace"
python excel_generator.py --business "Local Products Marketplace"
python excel_generator.py --business "B2B Wholesale Marketplace"
python excel_generator.py --business "Digital Products Store"
python excel_generator.py --business "E-book Marketplace"
python excel_generator.py --business "Online Art Marketplace"
python excel_generator.py --business "Handmade Jewellery Marketplace"
python excel_generator.py --business "Customized Gift Business"
python excel_generator.py --business "Wedding Products Marketplace"
python excel_generator.py --business "Rental Marketplace"
python excel_generator.py --business "Equipment Rental Marketplace"
python excel_generator.py --business "Office Supply Marketplace"
python excel_generator.py --business "Restaurant Supply Marketplace"
python excel_generator.py --business "Local Farmer Marketplace"
python excel_generator.py --business "Social Commerce Platform"
```

### Automotive (251-275)

```bash
python excel_generator.py --business "Car Dealership"
python excel_generator.py --business "Used Car Dealer"
python excel_generator.py --business "Used Bike Dealer"
python excel_generator.py --business "Car Detailing Business"
python excel_generator.py --business "Car Accessories Shop"
python excel_generator.py --business "Tyre Shop"
python excel_generator.py --business "Battery Shop"
python excel_generator.py --business "Car Insurance Agency"
python excel_generator.py --business "Vehicle Inspection Service"
python excel_generator.py --business "Car Modification Garage"
python excel_generator.py --business "Bike Modification Garage"
python excel_generator.py --business "EV Charging Station"
python excel_generator.py --business "EV Service Centre"
python excel_generator.py --business "EV Battery Service"
python excel_generator.py --business "Car Washing Franchise"
python excel_generator.py --business "Vehicle Recovery Service"
python excel_generator.py --business "Roadside Assistance"
python excel_generator.py --business "Driving School"
python excel_generator.py --business "Vehicle Registration Consultancy"
python excel_generator.py --business "Vehicle Fitness Consultancy"
python excel_generator.py --business "Fleet Leasing Business"
python excel_generator.py --business "Commercial Vehicle Rental"
python excel_generator.py --business "Luxury Car Rental"
python excel_generator.py --business "Self-Drive Rental"
python excel_generator.py --business "Automobile Marketplace"
```

### Freelance & Agency (276-300)

```bash
python excel_generator.py --business "Recruitment Agency"
python excel_generator.py --business "Staffing Agency"
python excel_generator.py --business "Freelance Marketplace"
python excel_generator.py --business "Virtual Assistant Agency"
python excel_generator.py --business "Data Entry Agency"
python excel_generator.py --business "Translation Agency"
python excel_generator.py --business "Content Writing Agency"
python excel_generator.py --business "Copywriting Agency"
python excel_generator.py --business "PR Agency"
python excel_generator.py --business "Branding Agency"
python excel_generator.py --business "Market Research Agency"
python excel_generator.py --business "Business Consultancy"
python excel_generator.py --business "Management Consultancy"
python excel_generator.py --business "HR Consultancy"
python excel_generator.py --business "Legal Consultancy"
python excel_generator.py --business "Export Consultancy"
python excel_generator.py --business "Franchise Consultancy"
python excel_generator.py --business "Startup Consultancy"
python excel_generator.py --business "Tender Consultancy"
python excel_generator.py --business "Government Scheme Consultancy"
python excel_generator.py --business "Training Consultancy"
python excel_generator.py --business "Sales Consultancy"
python excel_generator.py --business "Procurement Consultancy"
python excel_generator.py --business "Outsourcing Agency"
python excel_generator.py --business "Back-Office Service Company"
```

### Creative, Media & Entertainment (301-325)

```bash
python excel_generator.py --business "YouTube Production Agency"
python excel_generator.py --business "Podcast Studio"
python excel_generator.py --business "Influencer Agency"
python excel_generator.py --business "Creator Management Agency"
python excel_generator.py --business "Music Production Studio"
python excel_generator.py --business "Recording Studio"
python excel_generator.py --business "Animation Studio"
python excel_generator.py --business "VFX Studio"
python excel_generator.py --business "Game Development Studio"
python excel_generator.py --business "Esports Organisation"
python excel_generator.py --business "Esports Tournament Business"
python excel_generator.py --business "Live Streaming Agency"
python excel_generator.py --business "Talent Management Agency"
python excel_generator.py --business "Casting Agency"
python excel_generator.py --business "Modeling Agency"
python excel_generator.py --business "Advertising Production House"
python excel_generator.py --business "News Portal"
python excel_generator.py --business "Digital Magazine"
python excel_generator.py --business "Newsletter Business"
python excel_generator.py --business "Stock Photography Business"
python excel_generator.py --business "Stock Video Business"
python excel_generator.py --business "Meme Marketing Agency"
python excel_generator.py --business "Community Management Agency"
python excel_generator.py --business "Social Media Creator Studio"
python excel_generator.py --business "Digital Publishing Business"
```

### Travel & Tourism (326-350)

```bash
python excel_generator.py --business "Hotel Booking Agency"
python excel_generator.py --business "Homestay Marketplace"
python excel_generator.py --business "Hostel Booking Platform"
python excel_generator.py --business "Tour Package Business"
python excel_generator.py --business "Pilgrimage Tour Business"
python excel_generator.py --business "Adventure Tourism Business"
python excel_generator.py --business "Trekking Company"
python excel_generator.py --business "Camping Business"
python excel_generator.py --business "Bike Tour Business"
python excel_generator.py --business "Wildlife Tour Business"
python excel_generator.py --business "Local Guide Service"
python excel_generator.py --business "Tourist Transport Service"
python excel_generator.py --business "Airport Transfer Service"
python excel_generator.py --business "Visa Consultancy"
python excel_generator.py --business "Travel Insurance Agency"
python excel_generator.py --business "Foreign Exchange Service"
python excel_generator.py --business "Travel Planning Service"
python excel_generator.py --business "Corporate Travel Management"
python excel_generator.py --business "Group Travel Business"
python excel_generator.py --business "Honeymoon Travel Business"
python excel_generator.py --business "Backpacker Travel Platform"
python excel_generator.py --business "Rural Tourism Business"
python excel_generator.py --business "Eco-Tourism Business"
python excel_generator.py --business "Cruise Booking Agency"
python excel_generator.py --business "Travel Experience Marketplace"
```

### Pets & Animal Services (351-365)

```bash
python excel_generator.py --business "Pet Grooming"
python excel_generator.py --business "Pet Boarding"
python excel_generator.py --business "Pet Daycare"
python excel_generator.py --business "Pet Walking Service"
python excel_generator.py --business "Pet Sitting Service"
python excel_generator.py --business "Pet Adoption Platform"
python excel_generator.py --business "Veterinary Pharmacy"
python excel_generator.py --business "Pet Food Store"
python excel_generator.py --business "Pet Accessories Store"
python excel_generator.py --business "Pet Training Business"
python excel_generator.py --business "Animal Transport Service"
python excel_generator.py --business "Livestock Consultancy"
python excel_generator.py --business "Veterinary Laboratory"
python excel_generator.py --business "Animal Insurance Agency"
python excel_generator.py --business "Pet Marketplace"
```

### Industrial & Specialized Services (366-385)

```bash
python excel_generator.py --business "Industrial Equipment Rental"
python excel_generator.py --business "Crane Rental Business"
python excel_generator.py --business "Construction Equipment Rental"
python excel_generator.py --business "Generator Rental"
python excel_generator.py --business "Welding Service"
python excel_generator.py --business "CNC Machining Business"
python excel_generator.py --business "Industrial Maintenance Company"
python excel_generator.py --business "Factory Automation Company"
python excel_generator.py --business "Industrial Safety Consultancy"
python excel_generator.py --business "Quality Inspection Company"
python excel_generator.py --business "Calibration Service"
python excel_generator.py --business "Industrial Cleaning Service"
python excel_generator.py --business "Waste Management Company"
python excel_generator.py --business "Scrap Trading Business"
python excel_generator.py --business "Recycling Business"
python excel_generator.py --business "E-waste Recycling"
python excel_generator.py --business "Water Treatment Business"
python excel_generator.py --business "Solar Installation Company"
python excel_generator.py --business "Solar Maintenance Business"
python excel_generator.py --business "Renewable Energy Consultancy"
```

### Government, Legal & Compliance (386-400)

```bash
python excel_generator.py --business "Legal Documentation Service"
python excel_generator.py --business "Court Case Management Service"
python excel_generator.py --business "Legal Notice Service"
python excel_generator.py --business "Contract Management Business"
python excel_generator.py --business "Intellectual Property Consultancy"
python excel_generator.py --business "Labour Law Consultancy"
python excel_generator.py --business "Compliance Consultancy"
python excel_generator.py --business "ROC Compliance Service"
python excel_generator.py --business "FSSAI Consultancy"
python excel_generator.py --business "Import-Export Compliance Service"
python excel_generator.py --business "Tender Management Service"
python excel_generator.py --business "Government Procurement Consultancy"
python excel_generator.py --business "RTI Consultancy"
python excel_generator.py --business "Document Verification Service"
python excel_generator.py --business "Digital Signature Service"
```

---

## 🛠️ CLI Reference

### Excel Generator

```bash
python excel_generator.py [OPTIONS]
```

| Flag | Type | Default | Description |
|------|------|---------|-------------|
| `--domain` | str | — | Domain name or `all` |
| `--business` | str | — | Business name (e.g. `"Restaurant"`) |
| `--business-all` | flag | — | Generate all 400 businesses |
| `--rows` | int | `50` | Rows per sheet |
| `--output` | str | `generated_excel/` | Custom output file path |
| `--output-dir` | str | `generated_excel` | Output directory for `all` |
| `--list` | flag | — | List all domains and businesses |

### Django Generator

```bash
python app.py --input <excel_file> --output <project_dir> --project-name <Name>
```

| Flag | Type | Description |
|------|------|-------------|
| `--input` | str | Path to Excel file |
| `--output` | str | Output project directory |
| `--project-name` | str | Django project name |

### Frontend-Only Generator

```bash
python excel2frontend.py --input <excel_file> --output <dir>
```

---

## 🔄 Full Pipeline

```
┌─────────────────────────────────────────────────────────┐
│                    PIPELINE FLOW                         │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  ┌──────────────┐    ┌──────────────┐    ┌───────────┐ │
│  │  Excel       │    │  Django      │    │  Frontend │ │
│  │  Generator   │───▶│  Generator   │───▶│  (HTML)   │ │
│  │              │    │  (app.py)    │    │           │ │
│  └──────────────┘    └──────────────┘    └───────────┘ │
│         │                  │                  │        │
│         ▼                  ▼                  ▼        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │ .xlsx with   │  │ Models       │  │ Dashboard    │ │
│  │ demo data    │  │ Views/API    │  │ CRUD Pages   │ │
│  │ (50-10000    │  │ Serializers  │  │ Analytics    │ │
│  │  rows)       │  │ Admin        │  │ Login/Auth   │ │
│  └──────────────┘  │ Tests        │  │ Responsive   │ │
│                    │ Docker       │  └──────────────┘ │
│                    │ PWA          │                    │
│                    └──────────────┘                    │
│                                                         │
│  Time: < 10 seconds for complete full-stack app         │
└─────────────────────────────────────────────────────────┘
```

---

## 📊 What Gets Generated

### From Excel Generator

- Multi-sheet `.xlsx` file
- Realistic demo data (names, emails, phones, addresses, dates, prices)
- Styled headers (bold, colored)
- Per-domain custom columns and data types

### From Django Generator (app.py)

```
myapp/
├── manage.py
├── requirements.txt
├── README.md
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── run.sh / run.bat
├── gunicorn.conf.py
├── SCHEMA_REPORT.md
│
├── portalproj/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── portal/
│   ├── models.py          # Django models from Excel columns
│   ├── views.py           # Template + API views
│   ├── serializers.py     # DRF serializers
│   ├── urls.py            # URL routing
│   ├── admin.py           # Admin registrations
│   ├── permissions.py     # Role-based permissions
│   ├── tests.py           # Test suite
│   ├── forms.py           # Django forms
│   ├── middleware.py      # Custom middleware
│   │
│   ├── templates/
│   │   ├── base.html      # Base template
│   │   ├── dashboard.html # Dashboard
│   │   ├── login.html     # Auth
│   │   ├── charts.html    # Analytics
│   │   └── <model>.html   # CRUD pages per model
│   │
│   └── static/
│       ├── css/style.css  # Domain-themed CSS
│       └── js/app.js      # Interactive JS
│
├── templates/
│   └── registration/      # Auth templates
│
├── manifest.json          # PWA manifest
├── sw.js                  # Service worker
└── logs/                  # Log directory
```

---

## 🎨 Domain Themes

Each domain gets a unique color scheme and typography:

| Domain | Primary Color | Font |
|--------|:------------:|------|
| dating | `#ff6b9d` | Playfair Display |
| health | `#34d399` | Inter |
| legal | `#1e40af` | Merriweather |
| finance | `#f59e0b` | Source Sans Pro |
| ecommerce | `#8b5cf6` | Poppins |
| education | `#3b82f6` | Open Sans |
| food | `#ef4444` | Quicksand |
| automotive | `#6b7280` | Roboto |
| creative | `#ec4899` | Outfit |
| travel | `#06b6d4` | DM Sans |

---

## 💻 Tech Stack

| Layer | Technology |
|-------|-----------|
| **Language** | Python 3.13 |
| **Backend** | Django 5.x, Django REST Framework |
| **Frontend** | HTML5, CSS3, JavaScript, Chart.js |
| **Database** | SQLite (default), PostgreSQL (Docker) |
| **Excel** | openpyxl |
| **Container** | Docker, Docker Compose |
| **Server** | Gunicorn + Nginx |
| **PWA** | Service Worker, Web App Manifest |

---

## 📦 Installation

```bash
# Clone
git clone <repo-url>
cd excel_to_django_generator

# Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
# .venv\Scripts\activate    # Windows

# Install dependencies
pip install openpyxl django djangorestframework

# Verify
python excel_generator.py --list
```

---

## 🐳 Docker Usage

```bash
# Generate app
python app.py --input generated_excel/Restaurant_Database.xlsx --output myapp --project-name MyRestaurant

# Build & run with Docker
cd myapp
docker-compose up --build
```

Or use Makefile:

```bash
cd myapp
make build      # Build Docker image
make run        # Run container
make migrate    # Run migrations
make superuser  # Create admin
make logs       # View logs
make down       # Stop container
```

---

## 📖 Examples

### Example 1: Restaurant Management System

```bash
python excel_generator.py --business "Restaurant" --rows 100
python app.py --input generated_excel/Restaurant_Database.xlsx --output restaurant_app --project-name RestaurantOS
cd restaurant_app
python manage.py makemigrations portal
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Example 2: Healthcare Platform

```bash
python excel_generator.py --domain health --rows 200
python app.py --input generated_excel/HealthVault_16_Table_Database_Demo.xlsx --output healthapp --project-name HealthVault
cd healthapp
python manage.py makemigrations portal && python manage.py migrate
python manage.py runserver
```

### Example 3: Law Firm Portal

```bash
python excel_generator.py --domain legal --rows 50
python app.py --input generated_excel/LawFirm_LegalPractice_Database_Demo.xlsx --output lawapp --project-name LawFirm
cd lawapp
python manage.py makemigrations portal && python manage.py migrate
python manage.py runserver
```

### Example 4: Generate All 26 Domains

```bash
python excel_generator.py --domain all --rows 50
ls generated_excel/  # 26 Excel files
```

---

## 🧪 Testing

Generated projects include auto-created tests:

```bash
cd myapp
python manage.py test portal
```

Tests cover:

- Authentication (login/logout)
- Permission checks (role-based)
- API endpoints (CRUD)
- Page rendering
- Model validation

---

## 🔧 Customization

### Add Custom Demo Data Pools

Edit `data_pools.py` to add custom name lists, product categories, etc.

### Add New Domain Schemas

Create a new `gen_excel_cat4.py` with your `SCHEMAS` dict, then register it in `gen_excel_engine.py`:

```python
from gen_excel_cat4 import SCHEMAS as C4
ALL_SCHEMAS = {**S1, **S2, **S3, **C1, **C2, **C3, **C4}
```

### Add New Business Types

Edit `gen_excel_biztypes.py`:

```python
BIZ_CATEGORIES["your_category"] = ["Business 1", "Business 2", ...]
```

---

## 📄 License

MIT License — free for commercial and personal use.

---

## 🙌 Credits

Built with Python, Django, and openpyxl.
Generates complete full-stack applications from Excel spreadsheets in seconds.
