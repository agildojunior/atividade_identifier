import pytest

import src.identifier.identifier as identifier

class Test:

    def teste1(self):
        assert identifier.identifier("af42u5") == "Entrada valida"

    def teste2(self):
        assert identifier.identifier("5fa4gf") == "Entrada invalida"

    def teste3(self):
        assert identifier.identifier("g&h282") == "Entrada invalida"

    def teste4(self):
        assert identifier.identifier(' ') == "Entrada invalida"

    def teste5(self):
        assert identifier.identifier('g') == "Entrada valida"

    def teste6(self):
        assert identifier.identifier('t654321') == "Entrada invalida"

