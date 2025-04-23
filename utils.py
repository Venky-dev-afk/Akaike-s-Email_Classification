import re

#define regex patterns
PII_PATTERNS = {
    "full_name": r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)+\b',
    "email": r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
    "phone_number": r'\b(?:\+91[-\s]?|0)?[6-9]\d{9}\b',
    "dob": r'\b(?:\d{2}[/-]){2}\d{4}\b',
    "aadhar_num": r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}\b',
    "credit_debit_no": r'\b(?:\d[ -]?){13,16}\b',
    "cvv_no": r'\b\d{3}\b',
    "expiry_no": r'\b(0[1-9]|1[0-2])\/(\d{2}|\d{4})\b'
}

def mask_pii(email_text):
    masked_email = email_text
    list_of_masked_entities = []

    for entity_type, pattern in PII_PATTERNS.items():
        for match in re.finditer(pattern, masked_email):
            original_value = match.group()
            start, end = match.start(), match.end()
            placeholder = f"[{entity_type}]"

            list_of_masked_entities.append({
                "position": [start, end],
                "classification": entity_type,
                "entity": original_value

            })

            #replacae in masked_email(avoid overlapping by doing after loop)
            masked_email = masked_email.replace(original_value, placeholder)

    return masked_email, list_of_masked_entities


if __name__ == "__main__":
    sample_email = "Hi, my name is Alice Smith. My email is alice.smith@example.com and my phone number is +91 9876543210. My aadhar is 1234-5678-9012."
    masked_email, entities = mask_pii(sample_email)
    print("Masked:", masked_email)
    print("Entities:", entities)
