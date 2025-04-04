import pandas as pd
from fastapi import FastAPI, HTTPException

app = FastAPI()
CSV_FILE = "./Relatorio_cadop.csv"

try:
    df = pd.read_csv(CSV_FILE, sep=";", encoding="utf-8", dtype=str)
    df.fillna("", inplace=True)

    df["Data_Registro_ANS"] = pd.to_datetime(df["Data_Registro_ANS"], errors='coerce')

except Exception as e:
    print(f"Erro ao carregar o CSV: {e}")
    df = pd.DataFrame()

@app.get("/buscar/{termo}/{ordem}")
def buscar_operadora(termo: str, ordem: str):
    if df.empty:
        raise HTTPException(status_code=500, detail="Erro ao carregar o arquivo CSV")

    if ordem not in ["crescente", "decrescente"]:
        raise HTTPException(status_code=400, detail="Parâmetro 'ordem' deve ser 'crescente' ou 'decrescente'")

    resultados = df[df["Razao_Social"].str.contains(termo, case=False, na=False)]

    if resultados.empty:
        raise HTTPException(status_code=404, detail="Nenhuma operadora encontrada com esse termo")

    ordem_crescente = True if ordem == "crescente" else False
    resultados = resultados.sort_values(by="Data_Registro_ANS", ascending=ordem_crescente)

    return resultados.head(10).to_dict(orient="records")

@app.get("/cnpj/{cnpj}")
def buscar_por_cnpj(cnpj: str):
    if df.empty:
        raise HTTPException(status_code=500, detail="Erro ao carregar o arquivo CSV")

    resultado = df[df["CNPJ"] == cnpj]

    if resultado.empty:
        raise HTTPException(status_code=404, detail="Nenhuma operadora encontrada com esse CNPJ")
    return resultado.to_dict(orient="records")

@app.get("/estado/{uf}")
def buscar_por_estado(uf: str):
    if df.empty:
        raise HTTPException(status_code=500, detail="Erro ao carregar o arquivo CSV")

    uf = uf.upper()
    resultados = df[df["UF"] == uf]

    if resultados.empty:
        raise HTTPException(status_code=404, detail=f"Nenhuma operadora encontrada no estado {uf}")
    return resultados.to_dict(orient="records")

@app.get("/ano/{ano}")
def contar_por_ano(ano: int):
    if df.empty:
        raise HTTPException(status_code=500, detail="Erro ao carregar o arquivo CSV")

    if "Data_Registro_ANS" not in df.columns:
        raise HTTPException(status_code=500, detail="A coluna 'Data_Registro_ANS' não foi encontrada no CSV")

    registros_no_ano = df[df["Data_Registro_ANS"].dt.year == ano]

    if registros_no_ano.empty:
        raise HTTPException(status_code=404, detail=f"Nenhuma operadora registrada no ano {ano}")

    registros_ordenados = registros_no_ano.sort_values(by="Data_Registro_ANS", ascending=True)

    primeiros_10 = registros_ordenados.head(10).to_dict(orient="records")

    return {
        "ano": ano,
        "quantidade_total": len(registros_no_ano),
        "primeiros_10_registros": primeiros_10
    }