import re


def clean_barcode_string(barcode_string):
    if barcode_string.startswith('$#') :
        cleaned_string = barcode_string[2:-2]
        cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', cleaned_string)
        return cleaned_string
    else:
        return barcode_string


barcode1 = '$##stringhere$##'
barcode2 = '$####secondstring$###'

cleaned_barcode1 = clean_barcode_string(barcode1)
cleaned_barcode2 = clean_barcode_string(barcode2)

print(cleaned_barcode1)  # Output: stringhere
print(cleaned_barcode2)  # Output: secondstring