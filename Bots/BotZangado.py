from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__comandos = {'1': 
                            f"--> {self.nome} diz: Você disse 'Bom dia'\n--> Eu te respondo: 'BOM DIA?! Só se for para você.'",
                            '2':
                            f"--> {self.nome} diz: Você disse 'Qual o seu nome?'\n--> Eu te respondo: 'É sério que você quer que eu repita? É {self.nome}!!!'",
                            '3':
                            f"--> {self.nome} diz: Você disse 'Quero um conselho'\n--> Eu te respondo: 'Tenho cara de psicólogo? >:('",
                            '4':
                            f"--> {self.nome} diz: Você disse 'Adeus'\n--> Eu te respondo: 'Já vai tarde!'"}

    def apresentacao(self):
        return f"Ódio no coração, raiva de mim e da vida: Eu sou {self.__nome}"
 
    def mostra_comandos(self):
        return "1 - Bom dia\n2 - Qual o seu nome?\n3 - Quero um conselho\n4 - Adeus\n\n"
    
    def executa_comando(self,cmd):
        return self.__comandos.get(cmd, "Comando não encontrado")

    def boas_vindas(self):
        return f"--> {self.nome} diz: 'Não acredito que você teve a cara de pau de me escolher. GRRRR'"

    def despedida(self):
        return f"--> {self.nome} diz: 'Graças a Deus, já era a hora.'"
