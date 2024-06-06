import re

def remove_date_formats(text):
    # Define the regex pattern to match the date format
    date_pattern = r'[A-Z][a-z]{2} \d{1,2}, \d{4}, \d{1,2}:\d{2} [AP]M'

    # Use re.sub to replace all occurrences of the date format with an empty string
    cleaned_text = re.sub(date_pattern, '', text)

    return cleaned_text
