from Bots.Bot import Bot


class NenhumBotEscolhidoError(Exception):
    pass


class SistemaChatBot:
    def __init__(self, nomeEmpresa, lista_bots):
        self.__empresa = nomeEmpresa
        if all(isinstance(bot, Bot) for bot in lista_bots):
            self.__lista_bots = lista_bots
        else:
            raise TypeError("A lista de bots deve conter apenas objetos da classe Bot.")
        self.__bot = None

    def __get_bot(self):
        if (self.__bot is None):
            raise NenhumBotEscolhidoError("Nenhum bot foi escolhido")
        return self.__bot

    def boas_vindas(self):
        # mostra mensagem de boas vindas do sistema
        print("Bem-vindo ao Sistema de chatbots da empresa "+self.__empresa)

    def mostra_menu(self):
        for i, bot in enumerate(self.__lista_bots):
            print(f'{i} - Bot: {bot.apresentacao()}')

    def escolhe_bot(self):
        # faz a entrada de dados do usuário e atribui o objeto ao atributo __bot
        while True:
            try:
                bot = input("\nEscolha um bot ou -1 para sair: ")
                index = int(bot)
                if index == -1:
                    return False
                self.__bot = self.__lista_bots[index]
                return True
            except ValueError:
                print("Digite um número válido.")
            except IndexError:
                if len(self.__lista_bots) == 0:
                    print("Não há bots cadastrados.")
                else:
                    print("Digite um número entre 0 e", len(self.__lista_bots)-1)

    def mostra_comandos_bot(self):
        # mostra os comandos disponíveis no bot escolhido
        print(self.__get_bot().mostra_comandos())

    def le_envia_comando(self):
        # faz a entrada de dados do usuário e executa o comando no bot ativo
        cmd = input("Digite um comando ou -1 para sair: ")
        if cmd == "-1":
            print(self.__get_bot().despedida())
            return False
        print(self.__get_bot().executa_comando(cmd))
        return True

    def inicio(self):
        # mostra mensagem de boas-vindas do sistema
        # mostra o menu ao usuário
        # escolha do bot
        # mostra mensagens de boas-vindas do bot escolhido
        # entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        # ao sair mostrar a mensagem de despedida do bot
        self.boas_vindas()
        while True:
            self.mostra_menu()
            if not self.escolhe_bot():
                return
            self.__get_bot().boas_vindas()
            continuar_bot = True
            while continuar_bot:
                self.mostra_comandos_bot()
                continuar_bot = self.le_envia_comando()
