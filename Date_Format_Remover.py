import re

def remove_date_formats(text):
    date_pattern = r'[A-Z][a-z]{2} \d{1,2}, \d{4}, \d{1,2}:\d{2} [AP]M'

    cleaned_text = re.sub(date_pattern, '', text)

    return cleaned_text
