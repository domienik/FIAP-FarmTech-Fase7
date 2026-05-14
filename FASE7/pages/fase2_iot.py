from pathlib import Path
import re

import streamlit as st


# Esta página está em: FASE7/pages/fase2_iot.py
FASE7_DIR = Path(__file__).resolve().parents[1]

# Caminho onde você colocou os arquivos da Fase 2
FASE2_DIR = FASE7_DIR / "assets" / "fase2"

st.title("📡 Fase 2 - IoT, Sensores e ESP32")

st.write("""
Nesta seção estão os materiais da Fase 2 relacionados à aplicação com ESP32,
sensores e links de apoio do projeto.
""")

st.divider()

st.header("🔗 Links do Projeto")

# Procura qualquer arquivo links.txt dentro de assets/fase2
links_files = list(FASE2_DIR.rglob("links.txt"))

if not links_files:
    st.warning("Nenhum arquivo links.txt encontrado dentro de assets/fase2.")
    st.code(str(FASE2_DIR))
else:
    links_file = links_files[0]

    st.success(f"Arquivo encontrado: {links_file.relative_to(FASE7_DIR)}")

    conteudo = links_file.read_text(encoding="utf-8", errors="ignore")

    # Captura links http/https do arquivo
    links = re.findall(r"https?://[^\s]+", conteudo)

    if links:
        st.subheader("Links encontrados")

        for i, link in enumerate(links, start=1):
            st.markdown(f"{i}. [{link}]({link})")
    else:
        st.info("Nenhum link no formato http/https foi encontrado. Exibindo o conteúdo do arquivo:")

    with st.expander("Ver conteúdo completo do links.txt"):
        st.code(conteudo, language="text")

st.divider()

st.header("Integração com a Fase 7")

st.write("""
Esta página integra os links e materiais da Fase 2 dentro do dashboard central
da Fase 7, mantendo os arquivos organizados dentro da pasta assets.
""")