from abc import ABC, abstractmethod
import uuid

# -------------------------------------------------
# 1) Interface                                   🡇
# -------------------------------------------------
class Logavel(ABC):
    """Qualquer classe logável DEVE implementar logar_entrada()."""
    @abstractmethod
    def logar_entrada(self):
        pass


# -------------------------------------------------
# 2) Mixins                                      🡇
# -------------------------------------------------
class IdentificavelMixin:
    """Gera um ID único; combine-o com outras classes."""
    def __init__(self):
        self._id = uuid.uuid4()
    def get_id(self):
        return self._id


class AuditavelMixin:
    """Fornece logs simples ao console."""
    def log_evento(self, evento: str):
        print(f"[Log] {evento}")


# -------------------------------------------------
# 3) Classe base Pessoa                          🡇
# -------------------------------------------------
class Pessoa:
    def __init__(self, nome: str, cpf: str):
        self._nome = nome
        self._cpf = cpf
    
    @property
    def nome(self):
        return self._nome
    
    def __str__(self):
        return f"{self._nome} ({self._cpf})"
    
    
# -------------------------------------------------
# 4) Bagagem — classe simples                    🡇
# -------------------------------------------------
class Bagagem:
    def __init__(self, descricao: str, peso: float):
        self.descricao = descricao
        self.peso = peso  # kg
    def __str__(self):
        return f"{self.descricao} – {self.peso} kg"
    
    
# -------------------------------------------------
# 5) Passageiro                                  🡇
# -------------------------------------------------
class Passageiro(Pessoa):
    """Herda de Pessoa e possui bagagens."""
    def __init__(self, nome: str, cpf: str):
        super().__init__(nome, cpf) 
        self._bagagem = []
    
    
    def adicionar_bagagem(self, bagagem: Bagagem):
        if bagagem in self._bagagem:
            print(f"{self._nome} já colocou esta mala!")
        else:
            self._bagagem.append(bagagem)
            
    def listar_bagagens(self):
        if len(self._bagagem) == 0:
            print("Lista de bagagens vazia.")
        
        else:
            for bagagens in self._bagagem:
                print(bagagens)


# -------------------------------------------------
# 6) Funcionario (herança múltipla + mixins)     🡇
# -------------------------------------------------
class Funcionario(Pessoa, IdentificavelMixin, AuditavelMixin, Logavel):
    def __init__(self,nome, cpf, cargo, matricula):
        Pessoa.__init__(self,nome,cpf)
        IdentificavelMixin.__init__(self)
        self._cargo = cargo
        self._matricula = matricula

    def exibir_dados(self):
        print(f"O funcionário {self._nome} é {self._cargo}. Matrícula: {self._matricula} | ID: {self.get_id()}")
        
    def logar_entrada(self):
        self.log_evento(f"Funcionário(a) {self._nome}({self._cargo}) fez login.")
        

# -------------------------------------------------
# 7) MiniAeronave                                🡇
# -------------------------------------------------
class MiniAeronave:
    """Objeto da composição dentro de Voo."""
    def __init__(self, modelo: str, capacidade: int):
        self.modelo = modelo
        self.capacidade = capacidade
        
    def resumo_voo(self):
        return f"Aeronave: {self.modelo} – Capacidade: {self.capacidade}"


# -------------------------------------------------
# 8) Voo (composição com MiniAeronave)           🡇
# -------------------------------------------------
class Voo:
    def __init__(self, numero_voo= str, origem = str, destino = str, aeronave = MiniAeronave):
        self.numero_voo = numero_voo
        self.origem = origem
        self.destino = destino
        self._passageiros = []
        self._tripulacao = []
        self.aeronave = aeronave
    
    def adicionar_passageiro(self, passageiro : Passageiro):
        if passageiro in self._passageiros:
            print(f"O passageiro {passageiro} já está abordo.")

        else:
            if self.aeronave.capacidade <= len(self._passageiros):
                print("Quantidade de passageiros máxima alcançada.")        
        
            else:
                self._passageiros.append(passageiro)
                print("Passageiro adicionado.")
        
    def adicicionar_tripulantes(self, tripulante):
        if tripulante in self._tripulacao:
            print(f"O tripulante {tripulante} já está abordo.")
                
        else:
            if len(self._tripulacao) >= 5:
                    print("Capacidade máxima de tripulates!")
            else:
                    self._tripulacao.append(tripulante)
                    print("Tripulante adicionado.")


    def listar_passageiros(self):
        print(f"Passageiros do {self.numero_voo}:")
        for listando in self._passageiros:
            print(f"{listando._nome} - {listando._cpf}")
                
        
    def listar_tripulantes(self):
        print(f"Tripulação do voo {self.numero_voo}:")
        for listando in self._tripulacao:
            print(f"{listando._nome} - {listando._cpf} - {listando._matricula} - {listando._cargo}")


# -------------------------------------------------
# 9) CompanhiaAerea                              🡇
# -------------------------------------------------
class CompanhiaAerea:
    """Agrupa seus voos (has-a)."""
    def __init__(self, nome: str):
        if len(nome) < 3:
            raise ValueError("O nome da companhia deve ter pelo menos 3 letras.")
        self._nome = nome
        self._voos = []

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome: str):
        if len(novo_nome) < 3:
            raise ValueError("O nome da companhia deve ter pelo menos 3 letras.")
        self._nome = novo_nome

    def adicionar_voo(self, voo):
        if voo in self._voos:
            print(f'O voo {voo.numero_voo} já foi adicionado.')
        else:
            self._voos.append(voo)
            print(f"Voo {voo.numero_voo} adicionado à {self._nome}")

    def buscar_voo(self, numero: str):
        for voo in self._voos:
            if voo.numero_voo == numero:
                return voo
        return None
    
    def listar_voos(self):
        print(f"Voos da {self._nome}:")
        if len(self._voos) == 0:
            print("Nenhum voo cadastrado.")
        else:
            for voo in self._voos:
                print(f"{voo.numero_voo}: {voo.origem} → {voo.destino}")
                print(f"{voo.aeronave.resumo_voo()}")
                print(f"Passageiros: {len(voo._passageiros)}/{voo.aeronave.capacidade}")


# -------------------------------------------------
# 10) Auditor (Identificável + Logável)          🡇
# -------------------------------------------------
class Auditor(IdentificavelMixin, Logavel):
    def __init__(self, nome):
        IdentificavelMixin.__init__(self)
        self.nome = nome
    
    def logar_entrada(self):
        print(f"O auditor {self.nome} acabou de entrar.")

    def auditar_voo(self, voo: Voo):
        if len(voo._passageiros) <= voo.aeronave.capacidade:
            print("A capacidade máxima da aeronave não foi excedida.")
        elif len(voo._tripulacao) >= 1:
            print("Tripulação necessária para voo.")
        else:
            print("Não há tripulação na aeronave.")
    
    def __str__(self):
        return f"Auditor {self.nome} - (ID: {self.get_id()})"
    

# -------------------------------------------------
# 11) Bloco de teste                             🡇
# -------------------------------------------------
if __name__ == "__main__":
    print("🛫 SISTEMA DE GERENCIAMENTO DE COMPANHIAS AÉREAS 🛫")
    print("=" * 60)
    # Companhias
    azul = CompanhiaAerea("Azul")
    gol = CompanhiaAerea("GOL")
    
    # Aeronaves
    aeronave1 = MiniAeronave("Bravo 700", 2)
    aeronave2 = MiniAeronave("Cessna 172", 4)
    
    # Voos
    voo1 = Voo("AZ001", "São Paulo", "Rio de Janeiro", aeronave1)
    voo2 = Voo("AZ002", "Brasília", "Salvador", aeronave2)
    voo3 = Voo("GOL123", "Recife", "Fortaleza", aeronave1)
    voo4 = Voo("GOL456", "Porto Alegre", "Manaus", aeronave2)
    
    azul.adicionar_voo(voo1)
    azul.adicionar_voo(voo2)
    gol.adicionar_voo(voo3)
    gol.adicionar_voo(voo4)
    
    # Passageiros
    p1 = Passageiro("Vitória", "123.456.789-01")
    p2 = Passageiro("Marina", "987.654.321-02")
    p3 = Passageiro("Thiago", "456.789.123-03")
    
    # Bagagens
    bagagem1 = Bagagem("Mala de viagem", 23.5)
    bagagem2 = Bagagem("Mochila", 8.2)
    bagagem3 = Bagagem("Mala pequena", 15.0)
    
    p1.adicionar_bagagem(bagagem1)
    p1.adicionar_bagagem(bagagem2)
    p2.adicionar_bagagem(bagagem3)

    # Criando funcionários
    piloto1 = Funcionario("Maycon", "111.222.333-44", "Piloto", "P001")
    comissaria1 = Funcionario("Cristina", "999.888.777-66", "Comissária", "C001")
    pilota2 = Funcionario("Louise", "222.333.444-55", "Piloto", "P002")
    
    # Adicionando aos voos
    voo1.adicionar_passageiro(p1)
    voo1.adicionar_passageiro(p2)
    voo1.adicicionar_tripulantes(piloto1)

    voo2.adicionar_passageiro(p3)
    voo2.adicicionar_tripulantes(pilota2)
    voo2.adicicionar_tripulantes(comissaria1)

    # Criando auditor
    auditor = Auditor("Demetrios")

    # Teste
    print("LISTAGEM DE VOOS")
    azul.listar_voos()
    gol.listar_voos()
    
    print("\nBAGAGENS DA MARINA")
    p2.listar_bagagens()
    
    print("\nPASSAGEIROS DO VOO AZ001")
    voo1.listar_passageiros()
    
    print("\nTRIPULAÇÃO DO VOO AZ002")
    voo2.listar_tripulantes()
    
    print("\nDADOS DO FUNCIONÁRIO")
    piloto1.exibir_dados()
    
    print("\nLOGS DE ENTRADA")
    piloto1.logar_entrada()
    auditor.logar_entrada()
    
    print("\nAUDITORIA")
    auditor.auditar_voo(voo1)
    auditor.auditar_voo(voo4)
    print(auditor)
    """    
    TODO:
    • Criar 2 companhias, 2 voos cada, passageiros, funcionários e auditor.
    • Adicionar bagagens, listar passageiros, auditar voos.
    • Mostrar saídas no console para validar implementações.
    """