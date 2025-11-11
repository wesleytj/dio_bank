from .taxas import TAXAS_CAMBIO

def converter(valor: float, moeda_origem: str, moeda_destino: str) -> float:
    origem = moeda_origem.upper()
    destino = moeda_destino.upper()

    if origem == destino:
        return round(valor, 2)

    if origem not in TAXAS_CAMBIO:
        raise ValueError(f"Taxa de câmbio não disponível para {origem}")
    if destino not in TAXAS_CAMBIO:
        raise ValueError(f"Taxa de câmbio não disponível para {destino}")

    # converte origem -> BRL
    valor_em_brl = valor * TAXAS_CAMBIO[origem] if origem != "BRL" else valor

    # BRL -> destino
    if destino == "BRL":
        resultado = valor_em_brl
    else:
        resultado = valor_em_brl / TAXAS_CAMBIO[destino]

    return round(resultado, 2)
