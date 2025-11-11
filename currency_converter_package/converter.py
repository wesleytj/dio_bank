# dio_bank/currency_converter_package/converter.py (SUGESTÃO DE MELHORIA)
from .taxas import TAXAS_CAMBIO

def converter(valor: float, moeda_origem: str, moeda_destino: str) -> float:
    origem = moeda_origem.upper()
    destino = moeda_destino.upper()

    if origem == destino:
        return round(valor, 2)

    # 1. Validação de moedas e taxas
    try:
        taxa_origem = TAXAS_CAMBIO[origem]
        taxa_destino = TAXAS_CAMBIO[destino]
    except KeyError as e:
        raise ValueError(f"Taxa de câmbio não disponível para {e.args[0]}") from e

    # 2. Converte origem -> BRL
    # O valor em BRL é: (valor original / taxa_origem) * taxa_origem
    valor_em_brl = valor * taxa_origem 

    # 3. Converte BRL -> Destino
    # Valor no Destino = Valor em BRL / Taxa de Destino
    resultado = valor_em_brl / taxa_destino

    return round(resultado, 2)