class Pessoa:
    def __init__(self, nome, idade, peso, perfil, aparencia):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.perfil = perfil
        self.aparencia = aparencia
        self.energia = 100

    def comer(self, comida):
        print(f"{self.nome} está comendo {comida}.")
        self.energia += 10
        if self.energia > 100:
            self.energia = 100
        print(f"Agora {self.nome} tem {self.energia} de energia.")

    def andar(self, distancia):
        print(f"{self.nome} está andando {distancia} metros.")
        self.energia -= distancia * 0.1
        if self.energia < 0:
            self.energia = 0
        print(f"Agora {self.nome} tem {self.energia} de energia.")

    def falar(self, frase):
        print(f"{self.nome} diz: {frase}")

    def beber_agua(self, quantidade):
        print(f"{self.nome} está bebendo {quantidade}ml de água.")
        ganho_energia = quantidade * 0.02  # Cada 100ml dá 2% de energia
        self.energia += ganho_energia
        if self.energia > 100:
            self.energia = 100
        print(f"Agora {self.nome} tem {self.energia:.2f} de energia.")

    def mostrar_perfil(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso} kg")
        print(f"Perfil: {self.perfil}")
        print(f"Aparência: {self.aparencia}")

maria = Pessoa(
    "Maria",
    23,
    44,
    "Perfil Exemplo",
    "Cabelos ondulados"
)
maria.mostrar_perfil()
maria.comer("maçã")
maria.andar(50)
maria.falar("Olá, tudo bem?")
maria.beber_agua(500)
