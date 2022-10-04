from Bots.Bot import Bot

class BotTriste(Bot):
    def __init__(self, nome):
        super().__init__(nome)
        self.__comandos = {'1': 
                           f"--> {self.nome} diz: Você disse 'Bom dia'\n--> Eu te respondo: 'Bom dia? Diria que é um dia muito triste...'",
                           '2':
                           f"--> {self.nome} diz: Você disse 'Qual o seu nome?'\n--> Eu te respondo: 'Estou triste demais para repetir... (É {self.nome}...)'",
                           '3':
                           f"--> {self.nome} diz: Você disse 'Quero um conselho'\n--> Eu te respondo: 'Eu também...'",
                           '4':
                           f"--> {self.nome} diz: Você disse 'Adeus'\n--> Eu te respondo: 'Já estou acostumado... Adeus... :'('"}

    def apresentacao(self):
        return f"Psicologicamente triste, fisicamente cansado e emocionalmente confuso: Eu sou {self.nome}"
 
    def mostra_comandos(self):
        return "1 - Bom dia\n2 - Qual o seu nome?\n3 - Quero um conselho\n4 - Adeus\n\n"
    
    def executa_comando(self,cmd):
        return self.__comandos.get(cmd, "Comando não encontrado")

    def boas_vindas(self):
        return f"--> {self.nome} diz: 'Acho que é o dia mais feliz da minha vida... :('"

    def despedida(self):
        return f"--> {self.nome} diz: 'Não acredito que você vai me abandonar, tudo bem. Só achei que você fosse diferente...'"