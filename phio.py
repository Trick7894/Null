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




def phi(phio1_file, search_value):
            found = False

            with open(phio1_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()

            for line in lines:
                data = line.strip().split('	')
                if len(data) >= 4:
                    phone = data[1]
                    if search_value in phone:
                        user_id = data[3]
                        registration_date = data[2]

                        print(f'''{COLOR_CODE["RED"]}

                             {COLOR_CODE["RED"]}
                             ФИО: {phone}
                             ИНформация: {registration_date + user_id}

                                ''')
                        found = True

            if not found:
                print("not base")












