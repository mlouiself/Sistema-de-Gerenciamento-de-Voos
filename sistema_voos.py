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
    def __init__(self, nome: str, cpf: str):
<<<<<<< HEAD
        super().__init__(nome, cpf) 
        self._bagagem = []
    
    
=======
        super().__init__(nome, cpf)
        self._bagagens = []
    
>>>>>>> 77d2e55a8e28aac27364fb305502eed338ceb046
    def adicionar_bagagem(self, bagagem: Bagagem):
<<<<<<< HEAD
        if bagagem in self._bagagem:
            print(f"{self._nome} já colocou está mala!")
        else:
            self._bagagem.append(bagagem)
            print("bagagem adicionada")
            
            
=======
        if bagagem in self._bagagens:
            print("Esta bagagem já foi adicionada!")
        else:
            self._bagagens.append(bagagem)
    
>>>>>>> 77d2e55a8e28aac27364fb305502eed338ceb046
    def listar_bagagens(self):
<<<<<<< HEAD
        if len(self._bagagem) == 0:
            print("Lista de bagagens vazia")
        
        else:
            for bagagens in self._bagagem:
                print(bagagens)
=======
        if len(self._bagagens) == 0:
            print(f"{self.nome} não possui bagagens.")
        else:
            print(f"Bagagens de {self.nome}:")
            for bagagem in self._bagagens:
                print(bagagem)
>>>>>>> 77d2e55a8e28aac27364fb305502eed338ceb046


# -------------------------------------------------
# 6) Funcionario (herança múltipla + mixins)     🡇
# -------------------------------------------------
<<<<<<< HEAD
class Funcionario(Pessoa, IdentificavelMixin, AuditavelMixin, Logavel):
    def __init__(self,nome, cpf, cargo, matricula):
        Pessoa.__init__(self,nome,cpf)
        IdentificavelMixin.__init__(self)
        self._cargo = cargo
        self._matricula = matricula
        
    
    def exibir_dados(self):
        print(f"{self._nome} é {self._cargo}. Matricula: {self._matricula} | ID: {self.get_id}")
                
    def logar_entrada(self):
        pass


# TODO: Implementar a classe Funcionario
# - Herda de Pessoa, IdentificavelMixin e Logavel (pode usar AuditavelMixin)
# - Atributos: cargo, matricula
# - Métodos:
#   • exibir_dados() → imprime nome, cargo, matrícula e ID
#   • logar_entrada() → registra no log
=======
class Funcionario(Pessoa, IdentificavelMixin, AuditavelMixin):
    def __init__(self, nome: str, cpf: str, cargo: str, matricula: str):
        Pessoa.__init__(self, nome, cpf)
        IdentificavelMixin.__init__(self)
        self._cargo = cargo
        self._matricula = matricula
    
    def exibir_dados(self):
        print(f"Funcionário: {self.nome}")
        print(f"  Cargo: {self._cargo}")
        print(f"  Matrícula: {self._matricula}")
        print(f"  ID: {self.get_id()}")
    
    def logar_entrada(self):
        self.log_evento(f"Funcionário {self.nome} ({self._cargo}) fez login.")
>>>>>>> 77d2e55a8e28aac27364fb305502eed338ceb046


# -------------------------------------------------
# 7) MiniAeronave                                🡇
# -------------------------------------------------
class MiniAeronave:
    """Objeto da composição dentro de Voo."""
    def __init__(self, modelo: str, capacidade: int):
        self.modelo = modelo
        self.capacidade = capacidade
        
    def resumo_voo(self):
        return f'Modelo: {self.modelo}; Capacidade: {self.capacidade}'


# -------------------------------------------------
# 8) Voo (composição com MiniAeronave)           🡇
# -------------------------------------------------
# TODO: Implementar a classe Voo
# - Atributos: numero_voo, origem, destino, aeronave
# - Listas: passageiros, tripulacao
# - Métodos:
#   • adicionar_passageiro()  (verificar duplicidade e capacidade)
#   • adicionar_tripulante()
#   • listar_passageiros()
#   • listar_tripulacao()


# -------------------------------------------------
# 9) CompanhiaAerea                              🡇
# -------------------------------------------------
class CompanhiaAerea:
    """Agrupa seus voos (has-a)."""
    def __init__(self, nome: str):
        # TODO: validar nome (≥ 3 letras) e criar lista vazia de voos
        pass
    @property
    def nome(self):
        # TODO: retornar nome
        pass
    @nome.setter
    def nome(self, novo_nome: str):
        # TODO: validar + atualizar nome
        pass
    def adicionar_voo(self, voo):
        # TODO: adicionar voo à lista
        pass
    def buscar_voo(self, numero: str):
        # TODO: retornar voo ou None
        pass
    def listar_voos(self):
        # TODO: imprimir todos os voos
        pass


# -------------------------------------------------
# 10) Auditor (Identificável + Logável)          🡇
# -------------------------------------------------
# TODO: Implementar a classe Auditor
# - Herda de IdentificavelMixin e Logavel
# - Atributo: nome
# - Métodos:
#   • logar_entrada() → registra entrada no sistema
#   • auditar_voo(voo) → verifica:
#       ▸ passageiros ≤ capacidade
#       ▸ existe ao menos 1 tripulante
#     imprime relatório de conformidade
#   • __str__() → "Auditor <nome> (ID: ...)"


# -------------------------------------------------
# 11) Bloco de teste                             🡇
# -------------------------------------------------
if __name__ == "__main__":

    funciona = Funcionario()
    funciona.exibir_dados()
"""
=======
    f = Funcionario('m', '1', 'estagiaria', '2024')
    f.logar_entrada()
    


    """
    
    """TODO:
      • Criar 2 companhias, 2 voos cada, passageiros, funcionários e auditor.
      • Adicionar bagagens, listar passageiros, auditar voos.
      • Mostrar saídas no console para validar implementações."""