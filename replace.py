# Open and read the HTML file.
with open('1-letnik.txt', 'rb') as file:
    html_content = file.read().decode(errors='replace')

# List of placeholders
placeholders    = [
'[FMF-smer]',
'[subject-1]',
'[subject-2]',
'[subject-3]',
'[subject-4]',
'[subject-5]',
'[subject-6]',
'[subject-7]',
'[subject-8]',
'[subject-9]',
'[subject-10]',
'[subject-11]',
'[subject-12]',
'[subject-13]',
'[subject-14]',
'[subject-15]',
'[subject-16]',
'[subject-17]',
]

# List of replacements
replacements = [
'Uni FIZ 1. letnik',
'Fizikalni praktikum I',
'Fizikalni praktikum II',
'Kemija I',
'Klasična fizika',
'Matematika I',
'Matematika II',
'Proseminar A/B',
'Računalniški praktikum',
'Astronomska opazovanja',
'Dodatni izbirni predmet',
'Kako stvari delujejo?',
'Kemija II',
'Projektno delo I',
'Računalniška orodja v fiziki',
'Tehnično projektiranje',
'.',
'.',

    ]

# Check if both lists have same length
if len(placeholders) != len(replacements):
    print(len(placeholders))
    print(len(replacements))

    raise ValueError("Both lists should have same number of elements")

# Replace placeholders with replacements
for i in range(len(placeholders)):
    if(placeholders[i] in html_content ):
        html_content = html_content.replace(placeholders[i], replacements[i])

# Write the new HTML to a file.
with open('1-letnik.html', 'wb') as file:
    file.write(html_content.encode())
 


