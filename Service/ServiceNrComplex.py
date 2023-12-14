from Domain.NrComplex import NrComplex
from Repository.RepoNrComplex import RepoNrComplex


def is_prime(x):
    """
    Checks if the number is Prime
    :param x:  the number that the function checks
    :return: True daca numarul e prim sau False in caz contrar
    """
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(2, x + 1 // 2):
        if x % i == 0:
            return False
    return True


def get_max_from_list(lista: list):
    """
    Gaseste maximul intr-o lista
    :param lista:
    :return: maximul
    """
    maxim = 0
    for nr in lista:
        if nr.get_pi() > maxim:
            maxim = nr.get_pi()
    return maxim


def find_nr_max(lista: list):
    """

    :param lista:
    :return: numarul maxim din lista
    """
    maxim = get_max_from_list(lista)
    for nr in lista:
        if nr.get_pi() == maxim:
            return nr


def remove_max_from_list(lista: list):
    """
    Scoate numarul maxim din lista
    :param lista:
    :return: none
    """
    result = []
    maxim = get_max_from_list(lista)
    for nr in lista:
        if nr.get_pi() != maxim:
            result.append(nr)
    return result


class ServiceNrComplex:
    def __init__(self, repo: RepoNrComplex):
        self.__repo = repo
        self.undo = []

    def add(self, pr: int, pi: int):
        """
        Creeaza si adauga un nr complex in Repository
        :param pr: partea reala
        :param pi: partea imaginara
        :return:
        """
        self.update_undo(self.__repo.get_all())
        nr = NrComplex(pr, pi)
        self.__repo.add(nr)

    def add_poz(self, pr, pi, poz):
        """
        Creeaza si adauga un nr complex in Repository pe o pozitie
        :param pr: partea reala
        :param pi: partea imaginara
        :param poz: pozitia pe care se adauga
        :return:
        """
        self.update_undo(self.__repo.get_all())
        nr = NrComplex(pr, pi)
        self.__repo.add_poz(nr, poz)

    def dell(self, pr: int, pi: int):
        """
        Creeaza si sterge un nr complex in Repository
        :param pr:
        :param pi:
        :return:
        """
        self.update_undo(self.__repo.get_all())
        nr = NrComplex(pr, pi)
        self.__repo.delete(nr)

    def dell_poz(self, poz: int):
        """
        Creeaza si sterge un nr complex in Repository pe o pozitie
        :param pr: partea reala
        :param pi: partea imaginara
        :param poz: pozitia pe care se adauga
        :return:
        """
        self.update_undo(self.__repo.get_all())
        self.__repo.delete_poz(poz)

    def dell_interval(self, a: int, b: int):
        """
        Sterge Numere dintr-un anumit interval
        :param a:inceputul intervalului
        :param b: sfarsitul intervalului
        :return: lista cu ce ramane
        """
        result = []
        deleted = []
        self.update_undo(self.__repo.get_all())
        for i in range(b, a - 1, -1):
            deleted.append(self.__repo.get_all()[i])
        for elem in self.get_all():
            if elem not in deleted:
                result.append(elem)
        self.__repo.set(result)

    def sum_sequence(self, a: int, b: int):
        """
        Calculeaza suma numerelor complexe aflate pe un interval
       :param a:inceputul intervalului
        :param b: sfarsitul intervalului
        :return: suma
        """
        nr = NrComplex(0, 0)
        for i in range(a, b):
            nr = nr.sum(self.__repo.get_all()[i])
        return nr

    def prod_sequence(self, a: int, b: int):
        """
        Calculeaza produsul numerelor complexe aflate pe un interval
        :param a:inceputul intervalului
        :param b: sfarsitul intervalului
        :return: produsul
        """
        nr = self.get_all()[a]
        for i in range(a + 1, b):
            nr = nr.prod(self.__repo.get_all()[i])
        return nr

    def sort_by_pi(self):
        """
        Ordoneaza descrescator numerele complexe
        :return: o lista cu numerele ordonate
        """
        lista = []
        for nr in self.get_all():
            lista.append(nr)
        result = []
        while len(lista) > 0:
            result.append(find_nr_max(lista))
            lista = remove_max_from_list(lista)
        return result

    def filter_pr_prim(self):
        self.update_undo(self.__repo.get_all())
        for nr in self.get_all():
            if not is_prime(nr.get_pr()):
                self.__repo.delete(nr)

    def filter_sign_modul(self, sign: str, mod: int):
        self.update_undo(self.__repo.get_all())
        result = []
        match sign:
            case "<":
                for nr in self.get_all():
                    if nr.get_modul_square() < mod:
                        result.append(nr)
            case ">":
                for nr in self.get_all():
                    if nr.get_modul_square() > mod:
                        result.append(nr)
            case "=":
                for nr in self.get_all():
                    print(nr.get_modul_square())
                    if nr.get_modul_square() == mod:
                        result.append(nr)
        self.__repo.set(result)

    def update_undo(self, lista: list):
        """
        Actualizeaza lista de undo
        :param lista:
        :return:
        """
        self.undo = []
        for elem in lista:
            self.undo.append(elem)

    def do_undo(self):
        """
        Modifica vechea repository-ul cu lista undo
        :return:
        """
        if self.get_size() == len(self.undo):
            for i in range(0, self.get_size()):
                if self.get_all()[i] != self.undo[i]:
                    self.__repo.set(self.undo)
                    return True
            return False
        self.__repo.set(self.undo)
        return True

    def get_all(self):
        """

        :return: Repository-ul
        """
        return self.__repo.get_all()

    def get_size(self):
        """

        :return: Lungimea Repository-ului
        """
        return self.__repo.get_size()
