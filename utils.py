import re

def process_text(text):
    removed_username_text = re.sub(r'@\w+', '@user', text)  
    removed_url_text = re.sub(r'http\S+', 'http', removed_username_text)  
    
    removed_non_english_text = re.sub(r'[^a-zA-Z0-9\s\.,;:\'"!?-]', '', removed_url_text)

    lower_text = removed_non_english_text.lower()

    replaced_text = lower_text.replace(" u ", " you ").replace(" ur ", " your ").replace(" y ", " why ").replace(" 2 ", " to ").replace(" 4 ", " for ").replace("thx", "thanks")

    removed_repeat_text = re.sub(r'(\w)\1{2,}', r'\1', replaced_text)
    
    return removed_repeat_text