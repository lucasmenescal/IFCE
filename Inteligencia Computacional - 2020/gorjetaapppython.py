import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Cria as variáveis do problema
comida = ctrl.Antecedent(np.arange(0, 11, 1), 'comida')
servico = ctrl.Antecedent(np.arange(0, 11, 1), 'servico')
gorjeta = ctrl.Consequent(np.arange(0, 25, 1), 'gorjeta')

# Cria automaticamente o mapeamento entre valores nítidos e difusos 
# usando uma função de pertinência padrão (triângulo)
comida.automf(names=['horrivel', 'mediana', 'otima'])
#comida.view()

# Cria as funções de pertinência usando tipos variados
servico['ruim'] = fuzz.trimf(servico.universe, [0, 0, 5])
servico['aceitável'] = fuzz.trimf(servico.universe, [0, 5, 10])
servico['excelente'] = fuzz.trimf(servico.universe, [5, 10, 10])
servico.view()

gorjeta['baixa'] = fuzz.trimf(gorjeta.universe, [0, 0, 12])
gorjeta['média'] = fuzz.trimf(gorjeta.universe, [0, 12, 24])
gorjeta['alta'] = fuzz.trimf(gorjeta.universe, [12, 24, 24])
#gorjeta.view()

rule1 = ctrl.Rule(servico['excelente'] & comida['otima'], gorjeta['alta'])
rule2 = ctrl.Rule(servico['aceitável'] | comida['mediana'], gorjeta['média'])
rule3 = ctrl.Rule(servico['ruim'] & comida['horrivel'], gorjeta['baixa'])

gorjeta_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
gorjeta_simulador = ctrl.ControlSystemSimulation(gorjeta_ctrl)

# Entrando com alguns valores para qualidade da comida e do serviço
gorjeta_simulador.input['comida'] = float(input("Nota para a comida: "))
gorjeta_simulador.input['servico'] = float(input("Nota para o serviço: "))

# Computando o resultado
gorjeta_simulador.compute()
valorapagar=float(input("Informe o valor da sua conta: "))
resultado = valorapagar*((gorjeta_simulador.output['gorjeta'])/100)+valorapagar
print("Porcentagem da Gorjeta é: ", round(gorjeta_simulador.output['gorjeta'],2 ),"%")
print("O total da sua conta é: R$", round(resultado,2))
comida.view(sim=gorjeta_simulador)
servico.view(sim=gorjeta_simulador)
gorjeta.view(sim=gorjeta_simulador)

