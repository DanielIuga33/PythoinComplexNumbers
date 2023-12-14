from Service import ServiceNrComplex


def print_menu():
    print("1. Adauga Numar Complex")
    print("2. Sterge Numar Complex")
    print("3. Cautare Numere")
    print("4. Operatii cu numere din lista")
    print("5. Filtrare")
    print("u. Undo")
    print("a. Afiseaza Numere Complexe")
    print("x. Iesire")


def filters_menu():
    print("{1} Filtrare parte reala prim – elimină din listă"
          " numerele complexe la care partea reala este prim.")
    print("{2} Filtrare modul – elimina din lista"
          " numerele complexe la care modululeste <,= sau > decât un număr dat.")


def operations_menu():
    print("[a] Suma numerelor dintr-o subsecventă dată (se da poziția de început și sfârșit).")
    print("[b] Produsul numerelor dintr-o subsecventă dată (se da poziția de început și sfârșit).")
    print("[c] Tipărește lista sortată descrescător după partea imaginara")


def search_menu():
    print("|1| Tipărește partea imaginara pentru numerele "
          "din listă. Se dă intervalul de poziții (sub secvența).")
    print("|2| Tipărește toate numerele complexe care au modulul mai mic decât 10")
    print("|3| Tipărește toate numerele complexe care au modulul egal cu 10")


class UserInterface:
    def __init__(self, srv: ServiceNrComplex):
        self.srv = srv

    # MENUS

    def run_menu(self):
        print("\tWELCOME !")
        for i in range(1, 5):
            self.srv.add(i, i)
        while True:
            print_menu()
            option = input("Alegeti optiunea: ")
            match option:
                case "1":
                    self.add_nr()
                case "2":
                    self.del_nr()
                case "3":
                    search_menu()
                    self.manage_search()
                case "4":
                    operations_menu()
                    self.manage_operations()
                case "5":
                    filters_menu()
                    self.manage_filters()
                case "u":
                    if not self.srv.do_undo():
                        print("Nu s-a efectut nicio schimbare"
                              " dupa care sa se faca undo !")
                case "a":
                    self.show_all()
                case "x":
                    return
                case _:
                    print("Optiune gresita !")

    def manage_search(self):
        option = input("Alege optiunea: ")
        match option:
            case "1":
                self.print_pi_interval()
            case "2":
                self.print_mod_less10()
            case "3":
                self.print_mod_eq10()
            case _:
                return

    def manage_operations(self):
        option = input("Alege optiunea: ")
        match option:
            case "a":
                self.operation_sum_sequence()
            case "b":
                self.operation_prod_sequence()
            case "c":
                self.operation_sort_by_pi()
            case _:
                return

    def manage_filters(self):
        option = input("Alege optiunea: ")
        match option:
            case "1":
                self.srv.filter_pr_prim()
            case "2":
                self.manage_filter_sign_mod()
            case _:
                return

    def manage_filter_sign_mod(self):
        try:
            sign = input("Choose sign(< or = or >): ")
            if sign not in ["<", "=", ">"]:
                print("Your sign must be < or = or > !")
                return
            mod = int(input("Give here your number: "))
            if mod < 0:
                print("The number must be positive !")
                return
            self.srv.filter_sign_modul(sign, mod*mod)
        except Exception as e:
            print(e)

    # ADD OPERATIONS
    def add_nr(self):
        try:
            pr = int(input("Dati partea reala a nr-lui: "))
            pi = int(input("Dati partea imaginara a nr-lui: "))
            if len(self.srv.get_all()) > 0:
                print("Vreti sa adaugati numarul la sfarsitul")
                print("listei sau pe o pozitie anume ?")
                print(" [1] La sfarsit")
                print(" [2] Pe o pozitie anume")
                i = input("  Dati aici optiunea: ")
                if i == "2":
                    self.show_all()
                    poz = int(input("Precizati Pozitia: "))
                    if poz - 1 < 0 or poz - 1 > self.srv.get_size():
                        print("Pozitia data este invalida !")
                        return
                    self.srv.add_poz(pr, pi, poz - 1)
                    return
            self.srv.add(pr, pi)
        except Exception as e:
            print(e)

    # DELETE OPERATIONS

    def del_nr(self):
        try:
            i = self.show_all()
            if i == 0:
                return
            if self.srv.get_size() > 1:
                print("Vreti sa stergeti mai multe numere intr-un interval?")
                print(" [1] DA")
                print(" [2] NU")
                i = input("  Dati aici optiunea: ")
                if i == "1":
                    self.dell_nr_interval()
                    return
            self.dell_un_nr()
            return
        except Exception as e:
            print(e)

    def dell_nr_interval(self):
        seq = self.choose_the_sequence()
        self.srv.dell_interval(seq[0] - 1, seq[1] - 1)

    def dell_un_nr(self):
        i = int(input("Alege numarul pe care vrei sa il stergi: "))
        if i - 1 < 0 or i - 1 > self.srv.get_size():
            print("Optiune invalida !")
            return
        self.srv.dell_poz(i - 1)

    # PRINTS

    def show_all(self):
        """
        Afiseaza toate nr-le Complexe din Repository
        :return: none
        """
        if self.srv.get_size() == 0:
            print("Nu exista niciun numar complex momentan !")
            return 0
        i = 1
        for nr in self.srv.get_all():
            print(f"[{i}]. {nr}")
            i = i + 1
        return 1

    def print_pi_interval(self):
        """
         Afiseaza partea imaginara a nr-lor Complexe dintr-un interval din Repository
        :return:
        """
        self.show_all()
        seq = self.choose_the_sequence()
        for i in range(seq[0] - 1, seq[1]):
            print(f"Partea imaginara a numarului {self.srv.get_all()[i]} este {self.srv.get_all()[i].get_pi()}")

    def print_mod_less10(self):
        """
        Afiseaza numerele ce au modulul mai mic decat 10
        :return:
        """
        for nr in self.srv.get_all():
            if nr.get_modul_square() <= 100:
                print(nr)

    def print_mod_eq10(self):
        """
        Afiseaza numerele ce au modulul egal cu 10
        :return:
        """
        for nr in self.srv.get_all():
            if round(nr.get_modul_square()) == 100:
                print(nr)

    # OPERATIONS

    def operation_sum_sequence(self):
        self.show_all()
        seq = self.choose_the_sequence()
        print(self.srv.sum_sequence(seq[0] - 1, seq[1]))

    def operation_prod_sequence(self):
        self.show_all()
        seq = self.choose_the_sequence()
        print(self.srv.prod_sequence(seq[0] - 1, seq[1]))

    def operation_sort_by_pi(self):
        for nr in self.srv.sort_by_pi():
            print(nr)

    def choose_the_sequence(self):
        try:
            a = int(input("Alege inceputul: "))
            b = int(input("Alege sfarsitul: "))
            if a > b:
                c = a
                a = b
                b = c
            if a < 1 or b - 1 > self.srv.get_size():
                print("Intervalul dat este invalid !")
                return
            return [a, b]
        except Exception as e:
            print(e)
