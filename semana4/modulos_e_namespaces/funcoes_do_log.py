nome_de_usuario = "Andreia"

def imprimir_no_log(texto, nivel='info'):
        if nivel == 'info':
            print(f'[INFO] {texto}')
        elif nivel == 'alerta':
            print(f'[ALERTA] {texto}')
        elif nivel == 'erro':
            print(f'[ERRO] {texto}')
        else:
            print(f'[ERRO] Nível {texto} não é válido!')