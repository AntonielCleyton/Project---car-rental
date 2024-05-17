import time
import os

class Locadora:

  carros = {
      '0':  'Chevrolet Tracker - $ 120 /dia',
      '1': 'Chevrolet Onix - $ 90 /dia',
      '2': 'Chevrolet Spin - $ 150 /dia',
      '3': 'Hyundai HB20 - $ 85 /dia',
      '4': 'Hyundai Tuckson - $ 120 /dia',
      '5': 'Fiat Uno - $ 60 /dia',
      '6': 'Fiat Mobi - $ 70 /dia',
      '7': 'Fiat Pulse - $ 130 /dia'

    }

  carros_alugados = {}

  def __init__(self):
    self.nome = 'nome'


  def saudacoes(self):
      os.system('cls')
      print('-------------------------------')
      print('Bem-vindo à locadora de carros!')
      print('-------------------------------')
      self.nome = str(input('Qual é o seu nome? '))
      os.system('cls')
      barra = '='
      for i in range(10):
        teste = barra * i
        print(f'Prazer {self.nome}!')
        print('Iniciando o sistema...')
        print(teste)
        time.sleep(1)
        os.system('cls')
      print('Sistema carregado!')
      time.sleep(1)
      os.system('cls')  


  def portifolio(self):
    os.system('cls')
    while True:
      print('Bem-vindo à locadora de carros!')
      print('--------------------------------')
      print('-------Carros para alugar-------')
      print('--------------------------------')
      menu = int(input('0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro\nResposta: '))
      print('Entrando no menu escolhido...')
      time.sleep(1)
      os.system('cls')
      if menu == 0:
        print('-----PORTIFOLIO DE CARROS-----')
        for i, n in self.carros.items():
          print(f'[{i}] - {n}\n')
        print('------------------------------')
        escolha = int(input('0 - Continue | 1 - Sair\nResposta: '))  
        if escolha == 0:
          print(f'Certo {self.nome}! Voltando para o menu inicial...')
          time.sleep(1)
          os.system('cls')
          continue
        else:
          os.system('cls')
          print(f'Ok {self.nome}! Estamos saindo do programa...')
          time.sleep(1)
          break    
      elif menu == 1:
        while True:
            print('-----CARROS PARA ALUGAR-----')
            for i, n in self.carros.items():
                print(f'[{i}] - {n}\n')
            print('------------------------------')
            escolha = int(input('0 - Continue | 1 - Sair\nResposta: '))
            if escolha == 0:
                escolha1 = int(input('Escolha o código do carro:\nResposta: '))
                if escolha1 == 0:
                    carro_escolha = self.carros['0']
                    del self.carros['0']
                    self.carros_alugados['0'] = 'Chevrolet Tracker - $ 120 /dia'
                    dias = int(input('Escolha por quantos dias deseja alugar: '))
                    print(f'Você alugou o {carro_escolha} por {dias}')
                    valor = 120 * dias
                    escolha2 = int(input(f'O aluguel totalizara ${valor}. Deseja Continuar? 1-SIM | 2-NÃO\nResposta:  '))
                    if escolha2 == 1:
                        print(f'Certo {self.nome}! Voltando para o menu de carros para alugar...')
                        time.sleep(1)
                        os.system('cls')
                        continue
                    else:
                        os.system('cls')
                        print(f'Ok {self.nome}! Voltando para o menu principal...')
                        time.sleep(1)
                        break
                elif escolha1 == 1:
                    carro_escolha = self.carros['1']
                    del self.carros['1']
                    self.carros_alugados['1'] = 'Chevrolet Onix - $ 90 /dia'
                    dias = int(input('Escolha por quantos dias deseja alugar: '))
                    print(f'Você alugou o {carro_escolha} por {dias}')
                    valor = 90 * dias
                    escolha2 = int(input(f'O aluguel totalizara ${valor}. Deseja Continuar? 1-SIM | 2-NÃO\nResposta:  '))
                    if escolha2 == 1:
                        print(f'Certo {self.nome}! Voltando para o menu de carros para alugar...')
                        time.sleep(1)
                        os.system('cls')
                        continue
                    else:
                        os.system('cls')
                        print(f'Ok {self.nome}! Voltando para o menu principal...')
                        time.sleep(1)
                        break
                elif escolha1 == 2:
                    carro_escolha = self.carros['2']
                    del self.carros['2']
                    self.carros_alugados['2'] = 'Chevrolet Spin - $ 150 /dia'
                    dias = int(input('Escolha por quantos dias deseja alugar: '))
                    print(f'Você alugou o {carro_escolha} por {dias}')
                    valor = 90 * dias
                    escolha2 = int(input(f'O aluguel totalizara ${valor}. Deseja Continuar? 1-SIM | 2-NÃO\nResposta:  '))
                    if escolha2 == 1:
                        print(f'Certo {self.nome}! Voltando para o menu de carros para alugar...')
                        time.sleep(1)
                        os.system('cls')
                        continue
                    else:
                        os.system('cls')
                        print(f'Ok {self.nome}! Voltando para o menu principal...')
                        time.sleep(1)
                        break
                elif escolha1 == 3:
                    carro_escolha = self.carros['3']
                    del self.carros['3']
                    self.carros_alugados['3'] = 'Hyundai HB20 - $ 85 /dia'
                    dias = int(input('Escolha por quantos dias deseja alugar: '))
                    print(f'Você alugou o {carro_escolha} por {dias}')
                    valor = 90 * dias
                    escolha2 = int(input(f'O aluguel totalizara ${valor}. Deseja Continuar? 1-SIM | 2-NÃO\nResposta:  '))
                    if escolha2 == 1:
                        print(f'Certo {self.nome}! Voltando para o menu de carros para alugar...')
                        time.sleep(1)
                        os.system('cls')
                        continue
                    else:
                        os.system('cls')
                        print(f'Ok {self.nome}! Voltando para o menu principal...')
                        time.sleep(1)
                        break
                elif escolha1 == 4:
                    carro_escolha = self.carros['4']
                    del self.carros['4']
                    self.carros_alugados['4'] = 'Hyundai Tucson - $ 120 /dia'
                    dias = int(input('Escolha por quantos dias deseja alugar: '))
                    print(f'Você alugou o {carro_escolha} por {dias}')
                    valor = 90 * dias
                    escolha2 = int(input(f'O aluguel totalizara ${valor}. Deseja Continuar? 1-SIM | 2-NÃO\nResposta:  '))
                    if escolha2 == 1:
                        print(f'Certo {self.nome}! Voltando para o menu de carros para alugar...')
                        time.sleep(1)
                        os.system('cls')
                        continue
                    else:
                        os.system('cls')
                        print(f'Ok {self.nome}! Voltando para o menu principal...')
                        time.sleep(1)
                        break
                elif escolha1 == 5:
                    carro_escolha = self.carros['5']
                    del self.carros['5']
                    self.carros_alugados['5'] = 'Fiat Uno - $ 60 /dia'
                    dias = int(input('Escolha por quantos dias deseja alugar: '))
                    print(f'Você alugou o {carro_escolha} por {dias}')
                    valor = 90 * dias
                    escolha2 = int(input(f'O aluguel totalizara ${valor}. Deseja Continuar? 1-SIM | 2-NÃO\nResposta:  '))
                    if escolha2 == 1:
                        print(f'Certo {self.nome}! Voltando para o menu de carros para alugar...')
                        time.sleep(1)
                        os.system('cls')
                        continue
                    else:
                        os.system('cls')
                        print(f'Ok {self.nome}! Voltando para o menu principal...')
                        time.sleep(1)
                        break
                elif escolha1 == 6:
                    carro_escolha = self.carros['6']
                    del self.carros['6']
                    self.carros_alugados['6'] = 'Fiat Mobi - $ 70 /dia'
                    dias = int(input('Escolha por quantos dias deseja alugar: '))
                    print(f'Você alugou o {carro_escolha} por {dias}')
                    valor = 90 * dias
                    escolha2 = int(input(f'O aluguel totalizara ${valor}. Deseja Continuar? 1-SIM | 2-NÃO\nResposta:  '))
                    if escolha2 == 1:
                        print(f'Certo {self.nome}! Voltando para o menu de carros para alugar...')
                        time.sleep(1)
                        os.system('cls')
                        continue
                    else:
                        os.system('cls')
                        print(f'Ok {self.nome}! Voltando para o menu principal...')
                        time.sleep(1)
                        break
                elif escolha1 == 7:
                    carro_escolha = self.carros['7']
                    del self.carros['7']
                    self.carros_alugados['7'] = 'Fiat Pulse - $ 130 /dia'
                    dias = int(input('Escolha por quantos dias deseja alugar: '))
                    print(f'Você alugou o {carro_escolha} por {dias}')
                    valor = 90 * dias
                    escolha2 = int(input(f'O aluguel totalizara ${valor}. Deseja Continuar? 1-SIM | 2-NÃO\nResposta:  '))
                    if escolha2 == 1:
                        print(f'Certo {self.nome}! Voltando para o menu de carros para alugar...')
                        time.sleep(1)
                        os.system('cls')
                        continue
                    else:
                        os.system('cls')
                        print(f'Ok {self.nome}! Voltando para o menu principal...')
                        time.sleep(1)
                        break  
            elif escolha == 1:
                print(f'Certo {self.nome}! Voltando para o menu inicial...')
                time.sleep(1)
                os.system('cls')
                break
            else:
                print(f'{self.nome}, você fez uma escolha invalida! Tente novamente...')
                time.sleep(1)
                os.system('cls')
                continue
      elif menu == 2:
          while True:
            print('-----DEVOLUÇÃO DE CARRO-----')
            for i, n in self.carros_alugados.items():
                print(f'[{i}] - {n}\n')
            print('----------------------------')
            escolha = int(input('0 - Continue | 1 - Sair\nResposta: '))
            if escolha == 0:
                escolha1 = int(input('Escolha o código do carro:\nResposta: '))
                carro_escolha = self.carros_alugados[str(escolha1)]
                self.carros[str(escolha1)] = self.carros_alugados[str(escolha1)]
                del self.carros_alugados[str(escolha1)]
                print(f'{self.nome} você devolveu o {carro_escolha}!')
                print('---------------------------------------------')
                if not self.carros_alugados:
                    print('Não há mais carros para devolver...')
                else:
                    print('Ainda há carros para realizar devolução...')
                print('---------------------------------------')
                escolha2 = int(input('Deseja realizar a devolução de outro carro? 0 - SIM | 1 - NÃO\nResposta: '))
                if escolha2 == 0:
                    print(f'Certo {self.nome}! Estamos voltando para o menu inicial...')
                    time.sleep(1)
                    os.system('cls')
                    continue
                else:
                    print(f'Ok {self.nome}! Voltando para o menu inicial...')
                    time.sleep(1)
                    os.system('cls')
                    break
            elif escolha == 1:
                print(f'Ok {self.nome}! Voltando para o menu inicial...')
                time.sleep(1)
                os.system('cls')
                break
            else:
                print(f'{self.nome} você escolheu uma opção invalida! Voltando para as opções...')
                time.sleep(1)
                os.system('cls')
                continue




user = Locadora()

user.saudacoes()

user.portifolio()
