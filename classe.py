

class Usuario():
    def __init__(self):
        self.id = None
        self.usuario = None
        self.senha = None
        self.adm = None
    def banco_para_modelo(self, usuario_banco):
        self.id = usuario_banco[0]
        self.usuario = usuario_banco[1]
        self.senha = usuario_banco[2]
        self.adm = usuario_banco[3]

class Cliente():
    def __init__(self):
        self.id = None
        self.nome = None
        self.email = None
        self.cpf = None
        self.telefone = None
        self.cliente_id = None
    def banco_para_modelo(self, cliente_banco):
        self.id = cliente_banco[0]
        self.nome = cliente_banco[1]
        self.email = cliente_banco[2]
        self.cpf = cliente_banco[3]
        self.telefone = cliente_banco[4]
        self.cliente_id = cliente_banco[5]

class Macros():
    def __init__(self):
        self.id = None
        self.nome=None
        self.proteina = None
        self.carboidratos = None
        self.gordura = None
        self.kcal = None
    def banco_para_modelo(self,macro_banco):
        self.id = macro_banco[0]
        self.nome = macro_banco[1]
        self.proteina = macro_banco[2]
        self.carboidratos = macro_banco[3]
        self.gordura = macro_banco[4]
        self.kcal = macro_banco[5]
        
class Tmb():
    def __init__(self):
        self.id = None
        self.kcal = None
        self.objetivo = None
        self.peso = None
        self.altura = None
        self.idade = None
        self.genero = None
        self.nivel_de_atividade = None
        self.taxa_metabolica = None
        self.tmb_id = None
    def banco_por_modelo(self,tmb_banco):
        self.id = tmb_banco[0]
        self.kcal = tmb_banco[1]
        self.objetivo = tmb_banco[2]
        self.peso = tmb_banco[3]
        self.altura = tmb_banco[4]
        self.idade = tmb_banco[5]
        self.genero = tmb_banco[6]
        self.nivel_de_atividade = tmb_banco[7]
        self.taxa_metabolica = tmb_banco[8]
        self.tmb_id = tmb_banco[9]

class Alimentos():
    def __init__(self):
        self.id = None
        self.alimento = None
        self.proteina = None
        self.carboidrato = None
        self.gordura = None
        self.quantidade = None
        self.alimento_id = None
    def banco_por_modelo(self,alimentos_banco):
        self.id = alimentos_banco[0]
        self.alimento = alimentos_banco[1]
        self.proteina = alimentos_banco[2]
        self.carboidrato = alimentos_banco[3]
        self.gordura = alimentos_banco[4]
        self.quantidade = alimentos_banco[5]
        self.alimento_id = alimentos_banco[6]