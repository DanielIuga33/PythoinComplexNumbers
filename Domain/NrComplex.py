class NrComplex:
    def __init__(self, pr: int, pi: int):
        self.__pr = pr
        self.__pi = pi

    def __eq__(self, other):
        """
        Verifica daca doua numere complexe sunt egale
        :param other:
        :return: True daca sunt egale sau False in caz contrar
        """
        return self.get_pr() == other.get_pr() and self.get_pi() == other.get_pi()

    def get_pr(self):
        return self.__pr

    def get_pi(self):
        return self.__pi

    def set_pr(self, pr):
        self.__pr = pr

    def set_pi(self, pi):
        self.__pi = pi

    def get_modul_square(self):
        """
        Returneaza modulul numarului la patrat
        :return:
        """
        return self.get_pr()*self.get_pr() + self.get_pi()*self.get_pi()

    def sum(self, other):
        """
        returneaza suma dintre numarul complex si un alt numar
        :param other: alt numar
        :return: un numar ce reprezinta suma celor doua numere
        """
        return NrComplex(self.get_pr() + other.get_pr(), self.get_pi() + other.get_pi())

    def prod(self, other):
        """
        returneaza produsul dintre numarul complex si un alt numar
        :param other: alt numar
        :return: un numar ce reprezinta produsul celor doua numere
        """
        return NrComplex(self.get_pr() * other.get_pr() - self.get_pi() * other.get_pi(),
                         self.get_pi() * other.get_pr() + self.get_pr() * other.get_pi())

    def __str__(self):
        """

        :return: Afiseaza numarul complex
        """
        if self.__pr == 0 and self.__pi == 0:
            return f"Numarul: 0"
        if self.__pi == 0:
            return f"Numarul: {self.__pr}"
        if self.__pr == 0:
            return f"Numarul: {self.__pi}i "
        return f"Numarul: {self.__pr} + {self.__pi}i "
