from banner import banner
from banner import baner1
from banner import baner_pasword
from banner import banner2
import os
import gdown
import requests
from pystyle import *
from pystyle import Anime, Colors, Colorate, Center
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

"BLUE": "\033[34m",
}

def clearconsole():
 if os.name=='posix':
     os.system('clear')
 if os.name=='nt':
     os.system('cls')


def save_file_100m(link,filename):
    import gdown
    file = os.path.dirname(os.path.abspath(__file__))
    if os.name == 'posix':
        file = file + "/get/" + filename
    elif os.name == 'nt':
        file = file + "\get\\"  + filename
    gdown.download(link,file, quiet=False, fuzzy=True)
   
def save_file_google_drive(link, filename):
    import gdown
    file = os.path.dirname(os.path.abspath(__file__))
    if os.name == 'posix':
        file = file + "/mash/" + filename
    elif os.name == 'nt':
        file = file + "\mash\\"  + filename
    gdown.download(link,file, quiet=False, fuzzy=True)


def save_file_from_google_drive(link, filename):
    import gdown
    file = os.path.dirname(os.path.abspath(__file__))
    if os.name == 'posix':
        file = file + "/src/" + filename
    elif os.name == 'nt':
        file = file + "\src\\"  + filename
    gdown.download(link,file, quiet=False, fuzzy=True)

def save_from_google_drive(link, filename):
    import gdown

    file = os.path.dirname(os.path.abspath(__file__))
    
    if os.name == 'posix':
        file = file + "/id/" + filename
    elif os.name == 'nt':
        file = file + "\id\\"  + filename
    gdown.download(link,file, quiet=False, fuzzy=True)



Anime.Fade(Center.Center(baner_pasword), Colors.black_to_red, Colorate.Vertical, interval=0.045, enter=True)
print(Colors.red, Center.XCenter(banner2))
pasword=input(f'{COLOR_CODE["BLUE"]} Pasword {COLOR_CODE["RED"]} ')

if pasword=='trick4040':
      clearconsole()
else:
    print('ERROR')
    exit()

baners=input(f'{COLOR_CODE["BLUE"]} Ваша система 1-termux   2-linux,windows {COLOR_CODE["RED"]} ')
if baners=='1':
 clearconsole()
 print(Colorate.Vertical(Colors.blue_to_purple,Center.XCenter(baner1)))


elif baners=='2':
 clearconsole()
 print(Colorate.Vertical(Colors.blue_to_purple, Center.XCenter(banner)))
else:
    print('ERROR')

select = input(f'{COLOR_CODE["BLUE"]} Выбрать >{COLOR_CODE["RED"]} ')
if select == '1':
    from get import get100_number
    from deanon import get_number
    from deanon import tdat
    from deanon import hdat
    from deanon import dat
    from deanon import tele
    from deanon import meg
    from deanon import tyr
    from deanon import russ
    from deanon import getcont
    from deanon import bilane
    from deanon import getc
    from deanon import vk
    from deanon import vk1
    from deanon import sport
    from get import lukoul
    from get import podruzhka
    from get import get1
    from get import get2
    get1_file='get//getcontact-2.csv'
    get2_file='get//getcontact-3.csv'
    podruzhka_file='src//podruzhka.sql'
    luk_file='src//luk.txt'
    sport_file='src//sportmaster_1.txt'
    sport1_file='src//sportmaster_2.txt'
    sport2_file='src//sportmaster_3.txt'
    vk_file='src//vk1.csv'
    vk1_file='src//vk (1).txt'
    m100_file='get//100mln_0.csv'
    m2100_file='get//100mln_1.csv'
    m3100_file='get//100mln_3.csv'
    data_file = 'src//aliy.csv'
    datat_file="src//rit.csv"
    datar_file = "src//viм.csv"
    datah_file = "src//russkoe-slovo.ru_cleaned.csv"
    tele_file="src//tele2.csv"
    mega_file="src//ny.csv"
    tyr_file="src//tyr.sql.csv"
    russ_file="src//772.csv"
    bilane_file='src//Beeline2019.csv'

    getc_file='src//Get1.csv'
    getc1_file='src//Get2.csv'
    getc2_file='src//Get3.csv'
    getcon_file = "src//Getcontact .csv"
    search_value =input(f'{COLOR_CODE["RED"]}Введите номер телефона:')
    search_value = search_value[1:]
    get1(get1_file,search_value)
    get2(get2_file,search_value)
    sport(sport_file,sport1_file,sport2_file,search_value)
    podruzhka(podruzhka_file,search_value)
    lukoul(luk_file,search_value)

    get100_number(m100_file,m2100_file,m3100_file,search_value)
    vk1(vk1_file,search_value)
    get_number(data_file, search_value)
    tdat(datat_file,search_value)
    hdat(datah_file,search_value)
    dat(datar_file,search_value)
    meg(mega_file,search_value)
    tele(tele_file,search_value)
    tyr(tyr_file,search_value)
    russ(russ_file,search_value)
    vk(vk_file,search_value)
    getcont(getcon_file,search_value)
    getc(getc_file,getc1_file,getc2_file,search_value)
    bilane(bilane_file, search_value)
elif select == '2':
      print("не доступно")
elif select == '3':
    from get_ip import get_ip
    get_ip()
elif select =='4':
    from ddos import get_link
    from ddos import get_content
    print("Ctrl + z stop atack")
    lin = input(str('Link: '))
    get_link(lin)
    get_content(link)
elif select == '5':
    from iddeanon import get_tg
    from iddeanon import bog
    from iddeanon import tg
    tg_file='id//telegram users 520k, 10k numbers.txt'
    databases_file = 'id//csv.fixed.txt'
    bog_file='id//id.csv'
    searchs_value = input(f'{COLOR_CODE["RED"]}Введите id:')
    get_tg(databases_file, searchs_value)
    bog(bog_file,searchs_value)
    tg(tg_file,searchs_value)


elif select =='6':
      from indeanon import get_in
      databased_file='src//number2.csv'
      searchd_value = input(f'{COLOR_CODE["RED"]}Введите instagram:')
      get_in( databased_file, searchd_value )
elif select == '8':
        from phio import phi
        phio1_file="mash//1.csv"

        search_value = input(f'{COLOR_CODE["RED"]}Введите ФИО:')
        phi(phio1_file,search_value)

elif select == '9':
         print(f'''
                                  Base
                  ______________________________________
                  +    b-bilane               sport    +
                  +    g-getcontact           base6    +
                  +    base1                  vk       +
                  +    tele2                  100m     +
                  +    avto                   all      + 
                  +    tg                              + 
                  +____________________________________+ 
                       
                          ''')
         search_value = input(f'{COLOR_CODE["RED"]}Введите базу:')

         try:
            if search_value=='b':
                save_file_from_google_drive('https://drive.google.com/file/d/1iasG4fD8nidNLQtHY_r67CANA2PR8U-o/view?usp=sharing', 'Beeline2019.csv')

         except:
           print("ERROR")
         try:
            if search_value=='g':
                save_file_from_google_drive('https://drive.google.com/file/d/1YBTJqibhavl50EnReyUlMl3dQJ0JCKq5/view?usp=sharing', 'Get1.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/13L8uq0RxriK7v9wbpbtAUAFSXoxix8by/view?usp=sharing','Get2.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1YANpC9jrQzCQ6B2EA3ExrfKgC6cYSmjl/view?usp=sharing','Get3.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1rMrfs2UeYq4F5mizZ3XYJX4Gzpf3Vurt/view?usp=sharing','Getcontact .csv')
         except:
           print("ERROR")
         try:
            if search_value=='base1':
                save_file_from_google_drive('https://drive.google.com/file/d/1B2qdnCN4juTt2-GwZsvyGnnqxNLxzJIM/view?usp=sharing', 'ny.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1mG9pbuLWR8uiHOy5pr07bSqWkpBxX5pN/view?usp=sharing','rit.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1WXU9CMvnTV8xXnQdf0sFkEakYTXc768C/view?usp=sharing','viм.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1G6vrfgt8c36F-Bw3S376sVoquR6Gl4iw/view?usp=sharing','772.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1YMRlYlVwO2ZdqyY6AtZ38QECkYhMg6tn/view?usp=sharing','russkoe-slovo.ru_cleaned.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1_enul5KW7wAxRzd5Y0qNYcVJHtEOGKV3/view?usp=sharing', 'number2.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1-bkQ3Zpr8xXXI4I8r2FV0-Qsq8ABgq6i/view?usp=sharing', 'tele2.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/17X9Q_wMrHNRx7r4FNhpGAgNCZuIYhERM/view?usp=sharing', 'Beeline2019.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1YBTJqibhavl50EnReyUlMl3dQJ0JCKq5/view?usp=sharing', 'Get1.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/13L8uq0RxriK7v9wbpbtAUAFSXoxix8by/view?usp=sharing','Get2.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1YANpC9jrQzCQ6B2EA3ExrfKgC6cYSmjl/view?usp=sharing','Get3.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1rMrfs2UeYq4F5mizZ3XYJX4Gzpf3Vurt/view?usp=sharing','Getcontact .csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1-t5NDGmOP8ZLyMBktbxhMyturLjpa_Bv/view?usp=sharing','podruzhka.sql')
                save_file_from_google_drive('https://drive.google.com/file/d/1-xCpjkvQHlHCBYTfQx09tXA-MkKjftcg/view?usp=sharing', 'luk.txt')
                save_file_from_google_drive('https://drive.google.com/file/d/1iuLKhLilKkUAOjMXUqfqr3w2QZrwNmWF/view?usp=sharing','sportmaster_1.txt')
                save_file_from_google_drive('https://drive.google.com/file/d/1XFOjBt3HQFMVRoAa90CcHpzrjiU8xRYW/view?usp=sharing','sportmaster_2.txt')
                save_file_from_google_drive('https://drive.google.com/file/d/16dronJMv2qgoj6cJzuXmQd4cP_URursM/view?usp=sharing','sportmaster_3.txt')
                save_file_from_google_drive('https://drive.google.com/file/d/1uaXey-fzVTRqwbgMNNZpVCx0tZ_HczL-/view?usp=sharing', 'aliy.csv')
                save_file_from_google_drive('https://drive.google.com/file/d/1uY8i_uwXwruDGN6KuNdRKm6UQj_S-OuU/view?usp=sharing','tyr.sql.csv') 
                save_file_from_google_drive('https://drive.google.com/file/d/1PbudIa8b6rA7Ds2vmrjZQTq3iZ_T8GXo/view?usp=sharing','vk (1).txt')
                save_file_from_google_drive('https://drive.google.com/file/d/1YiRiLE_EaQ4g_pM_pYBZEvbLkAt2ZdUE/view?usp=sharing', 'vk1.csv') 
 
         except:
           print("ERROR")
         try:
            if search_value=='tele2':
                save_file_from_google_drive('https://drive.google.com/file/d/1-bkQ3Zpr8xXXI4I8r2FV0-Qsq8ABgq6i/view?usp=sharing', 'tele2.csv')
         except:
           print("ERROR")
         try:
            if search_value=='base6':
                save_file_from_google_drive('https://drive.google.com/file/d/1-t5NDGmOP8ZLyMBktbxhMyturLjpa_Bv/view?usp=sharing','podruzhka.sql')
                save_file_from_google_drive('https://drive.google.com/file/d/1-xCpjkvQHlHCBYTfQx09tXA-MkKjftcg/view?usp=sharing', 'luk.txt')
         except:
           print("ERROR")
         try:
            if search_value == 'avto':
                save_file_google_drive('https://drive.google.com/file/d/16eh99quOxYGWTfyTEKkBlPvUug9FfXKi/view?usp=sharing','1.csv')

         except:
             print("ERROR")
         try:
               if search_value == 'tg':
                   save_from_google_drive('https://drive.google.com/file/d/1vTzYRJoMq8t1KcvPHnMPfs3Xdl2DLUZg/view?usp=sharing','id.csv')
                   save_from_google_drive('https://drive.google.com/file/d/1k_GzqyCou2NSlGsLdt_Jve-Ss0Ig4DQQ/view?usp=sharing','csv.fixed.txt')
                   save_from_google_drive('https://drive.google.com/file/d/1s_IUEAd3K1A5cN3y41d3B356Sk9ZAfyi/view?usp=sharing','telegram users 520k, 10k numbers.txt')
         except:
            print("ERROR")
         try:
             if search_value == 'sport':
                 save_file_from_google_drive('https://drive.google.com/file/d/1iuLKhLilKkUAOjMXUqfqr3w2QZrwNmWF/view?usp=sharing','sportmaster_1.txt')
                 save_file_from_google_drive('https://drive.google.com/file/d/1XFOjBt3HQFMVRoAa90CcHpzrjiU8xRYW/view?usp=sharing','sportmaster_2.txt')
                 save_file_from_google_drive('https://drive.google.com/file/d/16dronJMv2qgoj6cJzuXmQd4cP_URursM/view?usp=sharing','sportmaster_3.txt')
         except:
            print("ERROR")
         try:
                if search_value == 'aliv':
                    save_file_from_google_drive('https://drive.google.com/file/d/1uaXey-fzVTRqwbgMNNZpVCx0tZ_HczL-/view?usp=sharing', 'aliy.csv')
                    save_file_from_google_drive('https://drive.google.com/file/d/1uY8i_uwXwruDGN6KuNdRKm6UQj_S-OuU/view?usp=sharing','tyr.sql.csv')
         except:
                print("ERROR")
         try:
            if search_value == '100m':
                    save_file_100m('https://drive.google.com/file/d/1hbTiyRBAPnOvhFmR2XyHKvSMBdqrf4rO/view?usp=sharing', '100mln_0.csv')
                    save_file_100m('https://drive.google.com/file/d/1dH4tghxRUu5DV4etb0liFPZqmehwPtPX/view?usp=sharing','100mln_1.csv')
                    save_file_100m('https://drive.google.com/file/d/1m5jhOAUvlh4GVXc3VE-_HDwFI9bU2wmK/view?usp=sharing', '100mln_3.csv')
                    save_file_100m('https://drive.google.com/file/d/1VoVC1GFYBuVuInfZHL5DYqDiPuDkJ28t/view?usp=sharing','getcontact-2.csv')
                    save_file_100m('https://drive.google.com/file/d/10qdcsv71e096HpDy9p5gXo1geaPTT1hW/view?usp=sharing','getcontact-3.csv')
         except:
                print("ERROR")
         try:
                if search_value == 'vk':
                    save_file_from_google_drive('https://drive.google.com/file/d/1PbudIa8b6rA7Ds2vmrjZQTq3iZ_T8GXo/view?usp=sharing','vk (1).txt')
                    save_file_from_google_drive('https://drive.google.com/file/d/1YiRiLE_EaQ4g_pM_pYBZEvbLkAt2ZdUE/view?usp=sharing', 'vk1.csv')
         except:
                print("ERROR")
         try:
                if search_value == 'all':
                    save_file_from_google_drive('https://drive.google.com/file/d/1iasG4fD8nidNLQtHY_r67CANA2PR8U-o/view?usp=sharing','Beeline2019.csv')
                    save_file_from_google_drive('https://drive.google.com/file/d/1YBTJqibhavl50EnReyUlMl3dQJ0JCKq5/view?usp=sharing','Get1.csv')
                    save_file_from_google_drive('https://drive.google.com/file/d/13L8uq0RxriK7v9wbpbtAUAFSXoxix8by/view?usp=sharing','Get2.csv')
                    save_file_from_google_drive('https://drive.google.com/file/d/1YANpC9jrQzCQ6B2EA3ExrfKgC6cYSmjl/view?usp=sharing','Get3.csv')
                    save_file_from_google_drive('https://drive.google.com/file/d/1rMrfs2UeYq4F5mizZ3XYJX4Gzpf3Vurt/view?usp=sharing','Getcontact .csv')
                    save_file_from_google_drive('https://drive.google.com/file/d/1B2qdnCN4juTt2-GwZsvyGnnqxNLxzJIM/view?usp=sharing', 'ny.csv')
                    save_file_from_google_drive('https://drive.google.com/file/d/1uY8i_uwXwruDGN6KuNdRKm6UQj_S-OuU/view?usp=sharing',' tyr.sql.csv')
                    save_file_from_google_drive('https://drive.google.com/file/d/1mG9pbuLWR8uiHOy5pr07bSqWkpBxX5pN/view?usp=sharing','rit.csv')
                    save_file_from_google_drive('https://drive.google.com/file/d/1WXU9CMvnTV8xXnQdf0sFkEakYTXc768C/view?usp=sharing','viм.csv')
                    save_file_from_google_drive('https://drive.google.com/file/d/1G6vrfgt8c36F-Bw3S376sVoquR6Gl4iw/view?usp=sharing','772.csv')
                    save_file_from_google_drive('https://drive.google.com/file/d/1uaXey-fzVTRqwbgMNNZpVCx0tZ_HczL-/view?usp=sharing','aliy.csv')
                    save_file_from_google_drive('https://drive.google.com/file/d/1YMRlYlVwO2ZdqyY6AtZ38QECkYhMg6tn/view?usp=sharing','russkoe-slovo.ru_cleaned.csv')
                    save_file_from_google_drive('https://drive.google.com/file/d/1-bkQ3Zpr8xXXI4I8r2FV0-Qsq8ABgq6i/view?usp=sharing','tele2.csv')
                    save_file_google_drive('https://drive.google.com/file/d/16eh99quOxYGWTfyTEKkBlPvUug9FfXKi/view?usp=sharing', '1.csv')
                    save_from_google_drive('https://drive.google.com/file/d/1k_GzqyCou2NSlGsLdt_Jve-Ss0Ig4DQQ/view?usp=sharing','csv.fixed.txt')
                    save_from_google_drive('https://drive.google.com/file/d/1s_IUEAd3K1A5cN3y41d3B356Sk9ZAfyi/view?usp=sharing','telegram users 520k, 10k numbers.txt')
                    save_file_from_google_drive('https://drive.google.com/file/d/1uaXey-fzVTRqwbgMNNZpVCx0tZ_HczL-/view?usp=sharing', 'aliy.csv')
                    save_file_from_google_drive('https://drive.google.com/file/d/1uY8i_uwXwruDGN6KuNdRKm6UQj_S-OuU/view?usp=sharing', 'tyr.sql.csv')
                    save_file_from_google_drive('https://drive.google.com/file/d/1iuLKhLilKkUAOjMXUqfqr3w2QZrwNmWF/view?usp=sharing', 'sportmaster_1.txt')
                    save_file_from_google_drive('https://drive.google.com/file/d/1XFOjBt3HQFMVRoAa90CcHpzrjiU8xRYW/view?usp=sharing', 'sportmaster_2.txt')
                    save_file_from_google_drive('https://drive.google.com/file/d/16dronJMv2qgoj6cJzuXmQd4cP_URursM/view?usp=sharing', 'sportmaster_3.txt')
                    save_file_from_google_drive('https://drive.google.com/file/d/1-t5NDGmOP8ZLyMBktbxhMyturLjpa_Bv/view?usp=sharing', 'podruzhka.sql')
                    save_file_from_google_drive('https://drive.google.com/file/d/1-xCpjkvQHlHCBYTfQx09tXA-MkKjftcg/view?usp=sharing', 'luk.txt')
                    save_file_from_google_drive('https://drive.google.com/file/d/1PbudIa8b6rA7Ds2vmrjZQTq3iZ_T8GXo/view?usp=sharing', 'vk (1).txt')
                    save_file_from_google_drive('https://drive.google.com/file/d/1YiRiLE_EaQ4g_pM_pYBZEvbLkAt2ZdUE/view?usp=sharing', 'vk1.csv')
                    save_file_100m('https://drive.google.com/file/d/1hbTiyRBAPnOvhFmR2XyHKvSMBdqrf4rO/view?usp=sharing','100mln_0.csv')
                    save_file_100m('https://drive.google.com/file/d/1dH4tghxRUu5DV4etb0liFPZqmehwPtPX/view?usp=sharing','100mln_1.csv')
                    save_file_100m('https://drive.google.com/file/d/1m5jhOAUvlh4GVXc3VE-_HDwFI9bU2wmK/view?usp=sharing','100mln_3.csv')
                    save_file_100m('https://drive.google.com/file/d/1VoVC1GFYBuVuInfZHL5DYqDiPuDkJ28t/view?usp=sharing','getcontact-2.csv')
                    save_file_100m('https://drive.google.com/file/d/10qdcsv71e096HpDy9p5gXo1geaPTT1hW/view?usp=sharing','getcontact-3.csv')
                    save_file_from_google_drive('https://drive.google.com/file/d/1_enul5KW7wAxRzd5Y0qNYcVJHtEOGKV3/view?usp=sharing', 'number2.csv')

         except:
                print("ERROR")




elif select =='N':
   exit


