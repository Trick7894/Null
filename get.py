COLOR_CODE = {
    "RESET": "\033[0m",
    "UNDERLINE": "\033[04m",
    "GREEN": "\033[32m",
    "YELLOW": "\033[93m",
    "RED": "\033[31m",
    "CYAN": "\033[36m",
    "BOLD": "\033[01m",
    "PINK": "\033[95m",
    "URL_L": "\033[36m",
    "LI_G": "\033[92m",
    "F_CL": "\033[0m",
    "DARK": "\033[90m",
}


def get100_number(m100_file, m2100_file, m3100_file, search_value):
    found = False

    with open(m100_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 2:
            phone = data[0]
            if search_value in phone:
                user_id = data[1]

                print(f'''{COLOR_CODE["RED"]}

                {COLOR_CODE["YELLOW"]}ТЕЛЕФОН: {phone}{COLOR_CODE["RED"]}
                     |---Теги: {user_id}     
                                                     
                                      
                      ''')
                found = True
    if not found:
        found = False

        with open(m2100_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for line in lines:
            data = line.strip().split(';')
            if len(data) >= 2:
                phone = data[0]
                if search_value in phone:
                    user_id = data[1]

                    print(f'''{COLOR_CODE["RED"]}

                {COLOR_CODE["YELLOW"]}ТЕЛЕФОН: {phone}{COLOR_CODE["RED"]}
                     |---Теги: {user_id}  
                             ''')
                    found = True
        if not found:
            found = False

            with open(m3100_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            for line in lines:
                data = line.strip().split(';')
                if len(data) >= 2:
                    phone = data[0]
                    if search_value in phone:
                        user_id = data[1]

                        print(f'''{COLOR_CODE["RED"]}

                {COLOR_CODE["YELLOW"]}ТЕЛЕФОН: {phone}{COLOR_CODE["RED"]}
                     |---Теги: {user_id}  
                                 ''')
                        found = True
            if not found:
                print("not base")


def lukoul(luk_file, search_value):
    found = False

    with open(luk_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 3:
            phone = data[2]
            if search_value in phone:
                registration_date = data[1]

                print(f'''{COLOR_CODE["RED"]}

                                  {COLOR_CODE["YELLOW"]} Телефон: {phone}{COLOR_CODE["RED"]}
                                     |
                                     |---ФИО: {registration_date}

                                    ''')
                found = True

    if not found:
        print('not Base')


def podruzhka(podruzhka_file, search_value):
    found = False

    with open(podruzhka_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(',')
        if len(data) >= 9:
            phone = data[2]
            if search_value in phone:
                registration_date = data[6]
                name = data[7]
                email = data[8]
                print(f'''{COLOR_CODE["RED"]}

                                  {COLOR_CODE["YELLOW"]} Телефон: {phone}{COLOR_CODE["RED"]}
                                     |
                                     |---ФИО: {registration_date + name}
                                     |---Почта:{email} 
                                    ''')
                found = True

    if not found:
        print('not Base')


def get2(get2_file, search_value):
    found = False

    with open(get2_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 2:
            phone = data[0]
            if search_value in phone:
                registration_date = data[1]
                print(f'''{COLOR_CODE["RED"]}

                                  {COLOR_CODE["YELLOW"]} Телефон: {phone}{COLOR_CODE["RED"]}
                                     |
                                     |---Теги: {registration_date}
                                    ''')
                found = True

    if not found:
        print('not Base')


def get1(get1_file, search_value):
    found = False

    with open(get1_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        data = line.strip().split(';')
        if len(data) >= 2:
            phone = data[0]
            if search_value in phone:
                registration_date = data[1]
                print(f'''{COLOR_CODE["RED"]}

                                  {COLOR_CODE["YELLOW"]} Телефон: {phone}{COLOR_CODE["RED"]}
                                     |
                                     |---Теги: {registration_date}
                                    ''')
                found = True

    if not found:
        print('not Base')
