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
        
    def adcicionar_tripulantes(self, tripulante):
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
        self.nome = nome
    
    def logar_entrada(self):
        print(f"O auditor {self.nome} acabou de entrar.")

    def auditar_voo(self,voo = Voo):
        if len(voo.self._passageiros) <= voo.self.capacidade:
            print("A capacidade máxima da aeronave não foi excedida.")
        elif len(voo.self._tripulacao) >= 1:
            print("Tripulação necessária para voo.")
        else:
            print("Não há tripulação na aeronave.") 
        
    def __str__(self):
        print(f"Auditor {self.nome} - (ID: {self.get_id()})")
    

# -------------------------------------------------
# 11) Bloco de teste                             🡇
# -------------------------------------------------
if __name__ == "__main__":
    
    
    
    passageiro1 = Passageiro("Thiago", "20241094010061" )
    passageiro2 = Passageiro("Vitória", "20241094010062" )
    passageiro3 = Passageiro("Marina", "20241094010063" )
    passageiro4 = Passageiro("Robson", "20241094010064" )
    func = Funcionario("Demetrios", "20241094010065", "engenheiro", "1306767733" )

    
    miniaeronave = MiniAeronave("Airbus380", 5)
    aviao = MiniAeronave("Airbus320", 9)
    aircraft = MiniAeronave("Airbus310", 2)     
    
    
    voo1 = Voo("33", "Am", "Rn", miniaeronave)
    voo2 = Voo("22", "Frt", "Rn", aviao)
    voo3 = Voo("22", "Pi", "Rn", aircraft)

    #VOO1
    voo1.adicionar_passageiro(passageiro1)
    voo1.adicionar_passageiro(passageiro2) 
    voo1.adicionar_passageiro(passageiro3)
    voo1.adicionar_passageiro(passageiro4)
    voo1.listar_passageiros()
    voo1.listar_tripulantes()
    
    #VOO2
   
        
        
        
        
    compa = CompanhiaAerea("guarulhos")
    compa.adicionar_voo(voo1)
    compa.listar_voos()
    
    auditor = Auditor("thiago")
    auditor.auditar_voo(voo1)
    
    """    
    TODO:
    • Criar 2 companhias, 2 voos cada, passageiros, funcionários e auditor.
    • Adicionar bagagens, listar passageiros, auditar voos.
    • Mostrar saídas no console para validar implementações.
    """