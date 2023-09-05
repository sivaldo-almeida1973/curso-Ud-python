"""
Constante = que não vai mudar


"""

velocidade_atual = 50
local_carro_esta = 102

#VAR CONST DEVE SER MAIÚSCULAS===================================
VEL_MAX_RADAR_1 = 60
LOCAL_RADAR_1 = 100
RADAR_RANGER = 1

vel_carro_passou_radar_1 = velocidade_atual > VEL_MAX_RADAR_1

if velocidade_atual > VEL_MAX_RADAR_1:
  print(f'Velocidade atual carro è: {velocidade_atual}Km/h')

if local_carro_esta >= (LOCAL_RADAR_1 - RADAR_RANGER) and local_carro_esta <= (LOCAL_RADAR_1 + RADAR_RANGER) and velocidade_atual > VEL_MAX_RADAR_1:
  print('Carro multado em rada 1!')
else:
  print('Faça uma boa viagem!')