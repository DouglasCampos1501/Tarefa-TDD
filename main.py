## CÁLCULO DE IMPOSTO DE RENDA

# Requisito 01 - Se salário for até 1.900 - mostrar "Isento de pagamento"
# Requisito 02 - Se salário for até 2.800 - mostrar "Aliquota de 7%"
# Requisito 03 - Se salário for até 3.700 - mostrar "Aliquota de 15%"
# Requisito 04 - Se salário for até 4.600 - mostrar "Aliquota de 25%"
# Requisito 05 - Se salário for acima de 4.600 - mostrar "Aliquota de 27%"
# Requisito 06 - Multiplicar Nº dependentes por 190.00 e ter saida formatada
# Requisito 07 - Formatar a saída de outras deduções
# Requisito 08 - Mostrar Isento de pagamento para um salário de 2000,00 - zero dependentes - 100,00 outras deduções
# Requisito 09 - Mostrar Isento de pagamento para um salário de 2000,00 - 2 dependentes - zero outras deduções
# Requisito 10 - Mostrar Aliquota de 7% para um salário de 2800,00 - zero dependentes - zero outras deduções
# Requisito 11 - Mostrar Aliquota de 15% para um salário de 5.000,00 - 5 dependentes - 900,00 outras deduções
# Requisito 12 - Mostrar Aliquota de 25% para um salário de 5.000,00 - 0 dependentes - 500,00 outras deduções
# Requisito 13 - Mostrar Aliquota de 27% para um salário de 10.000,00 - 5 dependentes - 300,00 outras deduções
# Requisito 14 - Mostrar Erro no valor informado caso salário seja negativo
# Requisito 15 - Mostrar Erro no valor informado caso salário seja zero
# Requisito 16 - Mostrar Erro no número de dependentes informado caso dependente seja negativo
# Requisito 17 - Mostrar Não há dependentes caso dependente seja zero
# Requisito 18 - Mostrar Erro no valor das deduções informado caso deduções seja negativo
# Requisito 19 - Mostrar Não há deduções caso deduções seja zero


def valor_salario(n_salario):
    if n_salario <= 0:
        return "Erro no valor informado"
    elif n_salario <= 1900:
        return "Isento de pagamento"
    elif n_salario <= 2800:
        return "Aliquota de 7%"
    elif n_salario <= 3700:
        return "Aliquota de 15%"
    elif n_salario <= 4600:
        return "Aliquota de 22%"
    else:
        return "Aliquota de 27%"


def dependentes(n_dependentes):
    if n_dependentes == 0:
        return "Não há dependentes"
    elif n_dependentes < 0:
        return "Erro no número de dependentes informado"
    else:
        calculo_dependentes = n_dependentes * 190.00
        valor_dependentes = "{:.2f}".format(calculo_dependentes)
        return valor_dependentes


def deducoes(valor_deducao):
    if valor_deducao == 0:
        return "Não há deduções"
    elif valor_deducao < 0:
        return "Erro no valor das deduções informado"
    else:
        saida_deducao = "{:.2f}".format(valor_deducao)
        return saida_deducao


def calculo_ir(salario, dependente, deducoes):
    calculo_final = salario - (dependente * 190) - deducoes
    return valor_salario(calculo_final)


def test_deve_mostrar_isento_se_abaixo_19000():
    assert valor_salario(1900) == "Isento de pagamento"


def test_deve_mostrar_aliquota_7_ate_2800():
    assert valor_salario(2800) == "Aliquota de 7%"


def test_deve_mostrar_aliquota_15_ate_3700():
    assert valor_salario(3700) == "Aliquota de 15%"


def test_deve_mostrar_aliquota_22_ate_4600():
    assert valor_salario(4600) == "Aliquota de 22%"


def test_deve_mostrar_aliquota_27_acima_4600():
    assert valor_salario(4601) == "Aliquota de 27%"


def test_deve_mostrar_valor_dependentes_formatado():
    assert dependentes(2) == "380.00"


def test_mostrar_valor_das_deduções_formatado():
    assert deducoes(200) == "200.00"


def test_mostrar_alicota_sal_2000_dep_zero_ded_100():
    assert calculo_ir(2000, 0, 100) == "Isento de pagamento"


def test_mostrar_alicota_sal_2000_dep_2_ded_zero():
    assert calculo_ir(2000, 2, 0) == "Isento de pagamento"


def test_mostrar_alicota_sal_2800_dep_0_ded_0():
    assert calculo_ir(2800, 0, 0) == "Aliquota de 7%"


def test_mostrar_alicota_sal_5000_dep_5_ded_900():
    assert calculo_ir(5000, 5, 900) == "Aliquota de 15%"


def test_mostrar_alicota_sal_5000_dep_0_ded_500():
    assert calculo_ir(5000, 0, 500) == "Aliquota de 22%"


def test_mostrar_alicota_sal_10000_dep_5_ded_300():
    assert calculo_ir(10000, 5, 300) == "Aliquota de 27%"


def test_deve_mostrar_erro_se_salario_negativo():
    assert valor_salario(-1) == "Erro no valor informado"


def test_deve_mostrar_erro_se_salario_zero():
    assert valor_salario(0) == "Erro no valor informado"


def test_deve_mostrar_erro_se_dependentes_negativo():
    assert dependentes(-1) == "Erro no número de dependentes informado"


def test_deve_mostrar_nao_ha_dependentes_caso_zero():
    assert dependentes(0) == "Não há dependentes"


def test_deve_mostrar_erro_se_deducoes_negativo():
    assert deducoes(-1) == "Erro no valor das deduções informado"


def test_deve_mostrar_nao_ha_deducoes_caso_zero():
    assert deducoes(0) == "Não há deduções"