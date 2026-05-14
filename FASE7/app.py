import os
import sys
import runpy
from pathlib import Path

import streamlit as st


# app.py está dentro de ANO1/FASE7
FASE7_DIR = Path(__file__).resolve().parent
ANO1_DIR = FASE7_DIR.parent

FASE7_PAGES_DIR = FASE7_DIR / "pages"
FASE4_DIR = ANO1_DIR / "FASE4" / "CAP1"

PAGINAS = {
    "Fase 4 - Home": FASE7_PAGES_DIR / "fase4_home.py",
    "Fase 4 - Exploração": FASE7_PAGES_DIR / "fase4_exploracao.py",
    "Fase 4 - Modelagem": FASE7_PAGES_DIR / "fase4_modelagem.py",
    "Fase 1 - Base de Dados": FASE7_PAGES_DIR / "fase1_base_dados.py",
}

st.set_page_config(
    page_title="FarmTech Solutions - Fase 7",
    page_icon="🌱",
    layout="wide"
)

st.sidebar.title("Navegação")

pagina = st.sidebar.selectbox(
    "Selecione uma página",
    list(PAGINAS.keys())
)

arquivo = PAGINAS[pagina]

if not arquivo.exists():
    st.error("Arquivo não encontrado.")
    st.code(str(arquivo))
    st.stop()

# Permite imports das páginas da Fase 7
if str(FASE7_PAGES_DIR) not in sys.path:
    sys.path.insert(0, str(FASE7_PAGES_DIR))

# Permite imports antigos da Fase 4, como utils.py
if str(FASE4_DIR) not in sys.path:
    sys.path.insert(0, str(FASE4_DIR))

# Evita conflito se alguma página antiga tiver st.set_page_config()
st.set_page_config = lambda *args, **kwargs: None

# Para páginas copiadas/adaptadas da Fase 4, usamos a pasta original como base
pasta_atual = Path.cwd()

try:
    if pagina.startswith("Fase 4"):
        os.chdir(FASE4_DIR)
    else:
        os.chdir(FASE7_DIR)

    runpy.run_path(str(arquivo), run_name="__main__")

finally:
    os.chdir(pasta_atual)