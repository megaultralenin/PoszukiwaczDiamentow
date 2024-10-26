import random


punkty_zycia = 10
punkty = 0 
print("hello", "teraz dostaniesz zasady gry") 
name = input("jak masz na imię?") 
print("hello!", name) 
print("twoim celem jest zdobycie 10 punktów zanim nie umrzesz") 
print("masz 10 punktów życia i startujes z 0 punktami") 
print("powodzenia!\n") 

while punkty_zycia > 0 and punkty < 10 : 
    kierunek = input("wybierz: \n prosto - w \n do tyłu - s \n lewo - a \n wprawo - d \n sklep - q \n wpisz: ") 
    if kierunek == "q": 
        if punkty >= 2:
            print("kup coś, proszę") 
            print("1. mała potka życia (+ 1 hp) - koszt 2 diamenty") 
            print("2. duża lotka życia (+ 4 hp) - koszt 5 diamenty") 
            print("3. Wykrywacz diamentów (zwiększa szansę znałezienia diaxów) - koszt 5 diamenty")
            wybor = input("kup coś proszę: 1, 2 lub 3: ") 
            if wybor == "1" and punkty >2 : 
                punkty -=2 
                punkty_zycia += 1 
                print("masz malą lotkę, masz", {punkty_zycia}) 
            elif wybor == "2" and punkty >5 :
                punkty -=5 
                punkty_zycia += 4 
                print("masz dużą lotkę, masz", {punkty_zycia}") 
            elif wybor == "3" and punkty >5 : 
                punkty -= 2 
                wydarzenie.append("diament")
                print("kupiłeś wykrywać diamentów. powodzenia w szukaniu1") 
            else: 
                print("zła odpowiedż") 
        else: 
            ("nie masz wystarczającej liczby punktów") 
    if kierunek == "w" or kierunek == "s" or kierunek == "a" or kierunek == "d" : 
        wydarzenie = random.choice(["diament", "potwor", "apteczka", "npc", "npc", "npc", "npc", "apteczka", "apteczka", "potwor"]) 

    if wydarzenie == "diament" : 
        punkty += 1 
        print(f"znałazłeś diament, masz teraz {punkty} punktów") 
    elif wydarzenie == "potwór" : 
        punkty_zycia -= 1 
        print(f"spotkałeś potwora i tracisz 1 punkt życia. masz {punkty_zycia} punktów życia") 
    elif wydarzenie == "apteczka": 
        punkty_zycia += 5 
        print(f"znałazłeś apteczkę i zyskujesz 5 punktów życia. masz {punkty_zycia} punktów życia") 
    else: 
        print("pusty korytarz. żyjesz jeszcze")
print() 
if punkty >= 10 :
    print("congartulations") 
elif punkty <= 0 : 
    print("LLLLLLLLLL") 
