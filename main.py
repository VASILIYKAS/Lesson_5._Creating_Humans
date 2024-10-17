from faker import Faker
import file_operations
import random
import os

# Создаем папку где будут храниться готовые карточки
output_dir = 'output/svg'
os.makedirs(output_dir, exist_ok=True)

# Открываем файл со скилами
file = open('skills.txt', 'r', encoding="utf-8")
skills = file.readlines()
file.close()

# Словарь с буквами для названия скилов
runic_symbol = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}

runic_skills = []  # создаем список с новыми стилизованными названиями скилов

# Заменяем буквы в названии скилов на буквы из словаря
for i in skills:
    runic_skill = i
    for key, value in runic_symbol.items():
        runic_skill = runic_skill.replace(key, value)
    runic_skills.append(runic_skill)

if __name__ == '__main__':
    for i in range(1, 11):
        # Генерируем карточку со случайными характеристиками
        fake = Faker("ru_RU")
        last_name = fake.last_name_male()
        first_name = fake.first_name_male()
        city = fake.city()
        job = fake.job()
        strength = random.randint(3, 18)
        agility = random.randint(3, 18)
        endurance = random.randint(3, 18)
        intelligence = random.randint(3, 18)
        luck = random.randint(3, 18)

        # Выбираем три случайных скила из списка со скилами
        random.shuffle(runic_skills)
        random.sample(runic_skills, 3)
        skill1 = runic_skills[0]
        skill2 = runic_skills[1]
        skill3 = runic_skills[2]

        # Вносим сгенерированные данные в новую карточку
        context = {
            'first_name': first_name,
            'last_name': last_name,
            'town': city,
            'job': job,
            'strength': strength,
            'agility': agility,
            'endurance': endurance,
            'intelligence': intelligence,
            'luck': luck,
            'skill_1': skill1,
            'skill_2': skill2,
            'skill_3': skill3
        }

        # Путь откуда берется шаблон и куда сохраняется готовые карточки
        file_operations.render_template(
            "src/charsheet.svg",
            "output/svg/output-{}.svg".format(i), context)
