import re
text = "Сегодня 23/02/2023, вчера 22/02/2023."

# регулярное выражение для поиска даты в формате "dd/mm/yyyy"
date_pattern = r"\d{2}/\d{2}/\d{4}"

# поиск всех вхождений даты в тексте
dates = re.findall(date_pattern, text)

# вывод найденных дат на консоль
print("Найденные даты:")
for date in dates:
    print(date)





