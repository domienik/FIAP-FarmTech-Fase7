import os
import sys
import runpy
from pathlib import Path

import streamlit as st


FASE7_DIR = Path(__file__).resolve().parent
PAGES_DIR = FASE7_DIR / "pages"

# Assets da Fase 4
FASE4_ASSETS_DIR = FASE7_DIR / "assets" / "fase4" / "cap1"

PAGINAS = {
    "Home - Integração Fase 7": PAGES_DIR / "home_fase7.py",
    "Fase 1 - Base de Dados": PAGES_DIR / "fase1_base_dados.py",
    "Fase 2 - IoT": PAGES_DIR / "fase2_iot.py",
    "Fase 3 - Banco de Dados Estruturado": PAGES_DIR / "fase3_banco_de_dados_estruturado.py",
    "Fase 4 - Dashboard e Data Science": PAGES_DIR / "fase4_dashboard_data_science.py",
    "Fase 5 - AWS e Alertas": PAGES_DIR / "fase5_aws_alertas.py",
    "Fase 6 - Visão Computacional": PAGES_DIR / "fase6_visao_computacional.py",
}

st.set_page_config(
    page_title="FarmTech Solutions - Fase 7",
    page_icon="🌱",
    layout="wide"
)

# Permite importar páginas da FASE7/pages
if str(PAGES_DIR) not in sys.path:
    sys.path.insert(0, str(PAGES_DIR))

# Permite importar utils.py da Fase 4
if str(FASE4_ASSETS_DIR) not in sys.path:
    sys.path.insert(0, str(FASE4_ASSETS_DIR))


# =========================
# NAVEGAÇÃO
# =========================
st.sidebar.title("Navegação")


def atualizar_url():
    st.query_params["pagina"] = st.session_state["selectbox_pagina"]


pagina_url = st.query_params.get("pagina", "Home - Integração Fase 7")

if pagina_url not in PAGINAS:
    pagina_url = "Home - Integração Fase 7"

# Sincroniza a URL com o selectbox antes de criar o widget
if "selectbox_pagina" not in st.session_state:
    st.session_state["selectbox_pagina"] = pagina_url
elif st.session_state["selectbox_pagina"] != pagina_url:
    st.session_state["selectbox_pagina"] = pagina_url

st.sidebar.selectbox(
    "Selecione uma página",
    list(PAGINAS.keys()),
    key="selectbox_pagina",
    on_change=atualizar_url
)

pagina = st.session_state["selectbox_pagina"]
arquivo = PAGINAS[pagina]

if not arquivo.exists():
    st.error("Arquivo não encontrado.")
    st.code(str(arquivo))
    st.stop()


# Evita conflito se alguma página também usar st.set_page_config()
st.set_page_config = lambda *args, **kwargs: None

# Algumas páginas da Fase 4 podem depender do CSV no diretório atual
pasta_atual = Path.cwd()

try:
    if pagina.startswith("Fase 4"):
        os.chdir(FASE4_ASSETS_DIR)
    else:
        os.chdir(FASE7_DIR)

    runpy.run_path(str(arquivo), run_name="__main__")

finally:
    os.chdir(pasta_atual)