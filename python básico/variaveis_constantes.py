velocidade = 61
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_geral =  velocidade > RADAR_1

multar = local_carro >=(LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 +RADAR_RANGE)



if velocidade_geral:
    print('carro passou do radar')
    
if  multar and velocidade_geral:
    print('carro multado em radar 1')    
    