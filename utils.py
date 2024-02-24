import re

def process_text(text):
    removed_non_english_text = re.sub(r'[^a-zA-Z0-9\s\.,;:\'"!?-]', '', text)

    lower_text = removed_non_english_text.lower()

    replaced_text = lower_text.replace(" u ", " you ").replace(" ur ", " your ").replace(" y ", " why ").replace(" 2 ", " to ").replace("thx", "thanks")

    removed_repeat_text = re.sub(r'(\w)\1{2,}', r'\1', replaced_text)
    modified_text = re.sub(r'(@\w+)', r"\1", removed_repeat_text)

    return modified_text