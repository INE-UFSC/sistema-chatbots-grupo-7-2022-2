from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome):
        super().__init(nome)
        self.__comandos = {'1': 
                           f"--> {self.nome} diz: Você disse 'Bom dia'\n--> Eu te respondo: 'Bom dia? Dia MA-RA-VI-LHO-SO!'",
                           '2':
                           f"--> {self.nome} diz: Você disse 'Qual o seu nome?'\n--> Eu te respondo: 'Que bom que perguntou! Meu nome é {self.nome}!!!!'",
                           '3':
                           f"--> {self.nome} diz: Você disse 'Quero um conselho'\n--> Eu te respondo: 'Se você quer encontrar a felicidade, encontre a gratidão!'",
                           '4':
                           f"--> {self.nome} diz: Você disse 'Adeus'\n--> Eu te respondo: 'Até a proxima!'"}

    def apresentacao(self):
        return f"É um prazer conhece-lo! meu nome é {self.nome}"
 
    def mostra_comandos(self):
        return "1 - Bom dia\n2 - Qual o seu nome?\n3 - Quero um conselho\n4 - Adeus\n\n"
    
    def executa_comando(self,cmd):
        return self.__comandos.get(cmd, "Comando não encontrado")

    def boas_vindas(self):
        return f"--> {self.nome} diz: 'Esse é definitivamente o dia mais feliz da minha vida!!! :D'"

    def despedida(self):
        return f"--> {self.nome} diz: 'Adorei você! Sentirei saudades! :)'"