from CarWash.washer import Washer
from CarWash.abs_body_washing import HandBodyWashing, AutomaticBodyWashing, CreateBodyWashing
from CarWash.abs_tires_washing import HandTiresWashing, AutomaticTiresWashing, CreateTiresWashing


def create_wash(func, washing_list):
    car_name_hand = input("Podaj nazwe samochodu")
    func.set_car = car_name_hand
    wash = Washer(func)
    washing_list.append(wash)


def main():
    washing_list = []

    i = True
    while (i):
        print("Wpisz:\n1.Dodaj mycie\n2.Utworz nowy typ mycia\n3.Wyswietl kolejke\n4.Wyjdz")
        choose = input(">>")
        if choose == "1":
            e = True
            while (e):
                 print("Wpisz:\n1. Mycie karoserii\n2. Mycie opon\n3. Wyjdz")
                 choose2 = input(">>")
                 if choose2 == "1":
                     b = True
                     while b:
                         print("Wpisz:\n1. Mycie reczne\n2. Mycie Automatyczne\n3. Wyjdz")
                         choose2 = input(">>")
                         if choose2 == "1":
                             hand_body = HandBodyWashing()
                             create_wash(hand_body, washing_list)
                         elif choose2 == "2":
                             hand_body = AutomaticBodyWashing()
                             create_wash(hand_body, washing_list)
                         elif choose2 == "3":
                             b = False
                         else:
                             print("\nPodany nieprawidłowy znak\n")
                 elif choose2 == "2":
                     c = True
                     while c:
                         print("Wpisz:\n1. Mycie reczne\n2. Mycie Automatyczne\n3. Wyjdz")
                         choose2 = input(">>")
                         if choose2 == "1":
                             hand_tires = HandTiresWashing()
                             create_wash(hand_tires, washing_list)
                         elif choose2 == "2":
                             hand_tires = AutomaticTiresWashing()
                             create_wash(hand_tires, washing_list)
                         elif choose2 == "3":
                             c = False
                         else:
                             print("\nPodany nieprawidłowy znak\n")
                 elif choose2 == "3":
                     e = False
                 else:
                     print("\nPodany nieprawidłowy znak\n")
        elif choose == "2":
            j = True
            while j:
                try:
                    print("Wpisz:\n1. Mycie karoserri\n2. Mycie opon\n3. Wyjdz")
                    choose2 = input(">>")
                    if choose2 == "1":
                        type_washing = input("Podaj opis")
                        hand_body = CreateBodyWashing(type_washing)
                        create_wash(hand_body, washing_list)
                    elif choose2 == "2":
                        type_washing = input("Podaj opis")
                        hand_tires = CreateTiresWashing(type_washing)
                        create_wash(hand_tires, washing_list)
                    elif choose2 == "3":
                        j = False
                    else:
                        print("\nPodany nieprawidłowy znak\n")
                except:
                    print("\nError: Prawdopodobnie dane sa nie zaladowane\n")
                    j = False
        elif choose == "3":
            for el in washing_list:
                wash = el
                wash()
        elif choose == "4":
            i = False
        else:
            print("Podany nieprawidłowy znak")


if '__main__' == __name__:
    main()