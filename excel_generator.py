#!/usr/bin/env python3
"""Generate domain-aware Excel databases with demo data.

Usage:
    python excel_generator.py --domain dating --rows 50
    python excel_generator.py --business "Accounting Firm" --rows 30
    python excel_generator.py --domain all --rows 50
    python excel_generator.py --business-all --rows 30
    python excel_generator.py --list
"""
import argparse, random, sys

random.seed(42)

def main():
    p = argparse.ArgumentParser(description="Generate domain-aware Excel databases")
    p.add_argument("--domain", default="", help="Domain name or 'all'")
    p.add_argument("--business", default="", help="Business name e.g. 'Accounting Firm'")
    p.add_argument("--business-all", action="store_true", help="Generate all 400 businesses")
    p.add_argument("--rows", type=int, default=50, help="Rows per sheet")
    p.add_argument("--output", default=None, help="Output .xlsx file")
    p.add_argument("--output-dir", default="generated_excel", help="Output dir")
    p.add_argument("--list", action="store_true", help="List domains + businesses")
    a = p.parse_args()

    from gen_excel_engine import generate_excel, generate_business, generate_all, generate_all_businesses, list_domains, list_all, ALL_SCHEMAS
    from gen_excel_biztypes import BIZ_TYPES, list_businesses

    if a.list:
        list_all()
        return

    if a.business_all:
        generate_all_businesses(a.rows, a.output_dir)
        return

    if a.business:
        cat = BIZ_TYPES.get(a.business)
        if not cat:
            print(f"Unknown business: {a.business}")
            print("Use --list to see all 400 businesses")
            sys.exit(1)
        output = a.output or f"generated_excel/{a.business.replace(' ','_')}_Database.xlsx"
        generate_business(a.business, a.rows, output)
        return

    if not a.domain:
        list_all()
        return

    if a.domain == "all":
        generate_all(a.rows, a.output_dir)
        return

    if a.domain not in ALL_SCHEMAS:
        print(f"Unknown domain: {a.domain}")
        print(f"Available: {', '.join(ALL_SCHEMAS.keys())}")
        sys.exit(1)

    output = a.output or f"generated_excel/{ALL_SCHEMAS[a.domain]['title']}_Demo.xlsx"
    generate_excel(a.domain, a.rows, output)

if __name__ == "__main__":
    main()
