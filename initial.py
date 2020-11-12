def ppv(x):
    nx = x.replace(',', '.')
    if nx.count('.') == 0:
        fx = int(nx)
    else:
        fx = float(nx)
    return fx


def msv(k):
    mf = '{:.2f}'.format(k)
    dec = mf[-2:]
    intf = '{:,}'.format(int(k))
    antes = str(intf).replace(',', '.')
    fn = '{}{}{}'.format(antes, ',', dec)
    return fn


def ciclo(m):
    try:
        v = ppv(str(m))
        return v
    except ValueError:
        print('\nVocê digitou um ou mais caracteres inválidos. '
                'Digite apenas números, separando as casas decimais com ponto ou vírgula!\n')
        pass

def main(valor, tempo):
    """Recebe o valor e o tempo de aplicação e retorna o detalhamento da projeção de investimento."""
    #Parameters:
    #    valor (str):O valor a ser aplicado semanalmente.
    #    tempo (str):A periodicidade.

    #Returns:
    #    calculated(valor, tempo):Retorna o detalhamento da projeção de investimento.

    ad = float(ciclo(valor))
    semanas = int(ciclo(tempo))
    jr = 4.25 / 52
    total = 0
    dep = 0
    for vezes in range(1, (semanas + 1)):
        dep += ad
        total += (total * jr / 100)
        total += ad
    jcom = total - dep
    
    total = msv(total)

    return total
    pass

# main(100, 36)

# ad = ciclo('Digite o valor fixo que deseja depositar toda semana R$ ')
# jr = 4.25
# semanas = ciclo('Digite quantas semanas quer deixar rendendo: ')
# dias = int(semanas)
# total = 0
# dep = 0
# jr = jr / 52

# for vezes in range(1, (semanas + 1)):
#     dep += ad
#     total += (total * jr / 100)
#     total += ad

# jcom = total - dep

# ad = msv(ad)
# jr = msv(jr)
# total = msv(total)
# dep = msv(dep)
# jcom = msv(jcom)

# if dias == 1:
#     man = 'SEMANA'
# else:
#     man = 'SEMANAS'

# print('''DEPÓSITO SEMANAL: R$ {}
# TAXA DOS JUROS COMPOSTOS: {}%
# TOTAL DE SEMANAS: {}

# VALOR ACRESCIDO DO PRÓPRIO DINHEIRO: {}
# VALOR ACRESCIDO EM JUROS COMPOSTOS: {}
# VALOR FINAL APÓS {} {} RENDENDO: R$ {}'''.format(ad, jr, semanas, dep, jcom, dias, man, total))

# input()
