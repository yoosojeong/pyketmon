import models
import my_pyketmon
import menu

def intro():
    #Introduce
    user_name = input("이름을 입력해주세요:")
    print(f"{models.ch_names_list[0]}: 파켓몬 세계에 잘 왔다! ♥ {user_name}!")
    print(f"{models.ch_names_list[0]}: 파켓몬을 고르도록 하지!")

def select():
    #Select first_paket
    for i in range(0,len(models.mon_names_list)):
        if i != len(models.mon_names_list)-1:
            print(f"{models.mon_names_list[i]},", end="")
        else:
            print(f"{models.mon_names_list[i]}")

    my_pyketmon.my_paket.append(input("선택: "))



if (models.start):
    # intro()
    select()

    choice = input("1.가방 2.이동 3.내포켓몬 4.나가기")
    menu

    models.start = False

else:
    choice = input("1.가방 2.이동 3.내포켓몬 4.나가기")
    menu
