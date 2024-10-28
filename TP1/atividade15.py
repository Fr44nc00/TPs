# Crie um programa que apresente ao usuário uma série
# de escolhas (como em uma história) e conduza a diferentes
# resultados com base nessas escolhas.

def aventura():
    opcao1 = int(input("Numa noite fria de dezembro, você acorda de noite com o barulho de algo parecido com passos no teto. Você:\n1- Volta a dormir // 2- Vai investigar o que é\nOpção: "))
    
    match(opcao1):
        case 1:
            print("\nVocê decide ignorar o barulho e volta a dormir. Devia ser um gato, né?")
        case 2:
            opcao2 = int(input("\nAo sair do seu quarto, você escuta um barulho de algo grande e pesado caindo em sua sala de estar. Você:\n1- Vai descobrir a origem do barulho // 2- Passa na cozinha para pegar algo para se defender\nOpção:"))
            
            match(opcao2):
                case 1:
                    opcao3 = int(input("\nVocê desce as escadas e se dirige à sala. Após ver um par de botas subindo por dentro da lareira, você percebe que os biscoitos ao lado de sua árvore de Natal foram comidos. Ao lado deles, uma grande caixa de presentes. Você:\n1- Tenta ver quem está subindo a chaminé // 2- Corre pra fora de casa para ter uma visão melhor da situação\nOpção: "))
                
                    match(opcao3):
                        case 1:
                            opcao4 = int(input("\nVocê vai até a lareira e coloca sua cabeça debaixo dela. Inicialmente não consegue ver nada, mas a luz forte da Lua entra de supetão, como se antes estivesse tampada por algo. Você ouve o barulho de sininhos vindo do lado de fora de sua casa. Você:\n1- Corre pra fora pra ver o que é // 2- Ignora e volta pro seu quarto\nOpção: "))
                            
                            match(opcao4):
                                case 1:
                                    print("\nVocê corre para fora de casa, mas não vê nada de diferente. Você fica confuso sobre o que pode ter acontecido, mas mesmo assim volta para seu quarto e dorme.")
                                case 2:
                                    print("\nVocê acha que já entendeu a situação e que não há perigo. Você volta para seu quarto e dorme.")
                        case 2:
                            print('\nAo sair de casa, você fica surpreso em ver um homem com um gorro e vestido de vermelho dos pés à cabeça. Ele te dá uma piscada de olho e vai embora voando, com os sinhos de seu trenó soando com o vento, rindo "hohoho!". Você decide voltar a dormir, feliz de saber que está na lista dos comportados.')
                case 2:
                    opcao3 = int(input("\nVocê desce as escadas e se dirige à cozinha. O que quer usar como arma?\n1- Um garfo // 2- Uma faca // 3- Um batedor // 4- Uma colher???\nOpção: "))
                    
                    match(opcao3):
                        case 1:
                            opcao4 = int(input("\nVocê pega o garfo e se dirige a sala, vendo que nada foi roubado, porém os biscoitos ao lado da árvore de Natal foram comidos, além de agora ter uma grande caixa de presentes ao lado dela. Você escuta o som de sininhos vindo do lado de fora de sua casa. Você:\n1- Corre pra fora pra ver o que é // 2- Ignora e volta pro seu quarto\nOpção: "))
                            
                            match(opcao4):
                                case 1:
                                    print("\nVocê corre para fora de casa, mas não vê nada de diferente. Você fica confuso sobre o que pode ter acontecido, mas mesmo assim volta para seu quarto e dorme.")
                                case 2:
                                    print("\nVocê acha que já entendeu a situação e que não há perigo. Você volta para seu quarto e dorme.")
                        case 2:
                            opcao4 = int(input("\nVocê pega a faca e se dirige a sala, vendo que nada foi roubado, porém os biscoitos ao lado da árvore de Natal foram comidos, além de agora ter uma grande caixa de presentes ao lado dela. Você escuta o som de sininhos vindo do lado de fora de sua casa. Você:\n1- Corre pra fora pra ver o que é // 2- Ignora e volta pro seu quarto\nOpção: "))
                            
                            match(opcao4):
                                case 1:
                                    print("\nVocê corre para fora de casa, mas não vê nada de diferente. Você fica confuso sobre o que pode ter acontecido, mas mesmo assim volta para seu quarto e dorme.")
                                case 2:
                                    print("\nVocê acha que já entendeu a situação e que não há perigo. Você volta para seu quarto e dorme.")
                        case 3:
                            opcao4 = int(input("\nVocê pega o batedor e se dirige a sala, vendo que nada foi roubado, porém os biscoitos ao lado da árvore de Natal foram comidos, além de agora ter uma grande caixa de presentes ao lado dela. Você escuta o som de sininhos vindo do lado de fora de sua casa. Você:\n1- Corre pra fora pra ver o que é // 2- Ignora e volta pro seu quarto\nOpção: "))
                            
                            match(opcao4):
                                case 1:
                                    print("\nVocê corre para fora de casa, mas não vê nada de diferente. Você fica confuso sobre o que pode ter acontecido, mas mesmo assim volta para seu quarto e dorme.")
                                case 2:
                                    print("\nVocê acha que já entendeu a situação e que não há perigo. Você volta para seu quarto e dorme.")
                        case 4:
                            opcao4 = int(input("\nVocê pega uma colher???? Como você vai se defender com isso?? Enfim, você se dirige a sala, vendo que nada foi roubado, porém os biscoitos ao lado da árvore de Natal foram comidos, além de agora ter uma grande caixa de presentes ao lado dela. Você escuta o som de sininhos vindo do lado de fora de sua casa. Você:\n1- Corre pra fora pra ver o que é // 2- Ignora e volta pro seu quarto\nOpção: "))
                            
                            match(opcao4):
                                case 1:
                                    print("\nVocê corre para fora de casa, mas não vê nada de diferente. Você fica confuso sobre o que pode ter acontecido, mas mesmo assim volta para seu quarto e dorme.")
                                case 2:
                                    print("\nVocê acha que já entendeu a situação e que não há perigo. Você volta para seu quarto e dorme.")
    
aventura()