import ordenador
import pytest
import desempenho_ordenacao


class TestaOrdenador:

    @pytest.fixture
    def o(self):
        return ordenador.Ordenador()

    @pytest.fixture
    def l_quase(self):
        c = desempenho_ordenacao.ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def l_aleat(self):
        c = desempenho_ordenacao.ContaTempos()
        return c.lista_aleatoria(100)

    def esta_ordenada(self, l):
        for i in range(len(l)-1):
            if l[i] > l[i+1]:
                return False
        return True

    def testa_bolha_stop_aleat(self, o, l_aleat):
        o.bolha_stop(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def testa_selecao_direta_aleat(self, o, l_aleat):
        o.selecao_direta(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def testa_bolha_aleat(self, o, l_aleat):
        o.bolha(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def testa_bolha_stop_quase_aleatorio(self, o, l_quase):
        o.bolha_stop(l_quase)
        assert self.esta_ordenada(l_quase)

    def testa_selecao_direta_quase_aleatorio(self, o, l_quase):
        o.selecao_direta(l_quase)
        assert self.esta_ordenada(l_quase)

    def testa_bolha_quase_aleatorio(self, o, l_quase):
        o.bolha(l_quase)
        assert self.esta_ordenada(l_quase)
