from pathlib import Path
import streamlit as st


FASE7_DIR = Path(__file__).resolve().parents[1]
FASE3_DIR = FASE7_DIR / "assets" / "fase3"

st.title("🗄️ Fase 3 - Banco de Dados Estruturado")

st.write("""
Nesta fase, o foco foi estruturar o ambiente de banco de dados, preparar a
integração dos dados agrícolas das fases anteriores e organizar as entregas
relacionadas ao Programa do Ir Além.
""")

st.divider()

tab_oracle, tab_integracao, tab_ir_alem = st.tabs([
    "🗄️ Oracle",
    "🌱 Integração dos Dados",
    "🚀 Ir Além"
])

with tab_oracle:
    st.header("🗄️ Instalação do Ambiente Oracle")

    st.write("""
    Esta seção reúne os materiais relacionados à instalação e configuração do
    ambiente de banco de dados Oracle utilizado no projeto.
    """)

    pasta = FASE3_DIR / "cap_oracle"

    if pasta.exists():
        arquivos = [a for a in pasta.rglob("*") if a.is_file()]
        if arquivos:
            for arquivo in arquivos:
                st.write(f"✅ `{arquivo.relative_to(FASE7_DIR)}`")
        else:
            st.info("Nenhum arquivo encontrado nesta pasta.")
    else:
        st.warning("Pasta ainda não encontrada.")
        st.code(str(pasta))

with tab_integracao:
    st.header("🌱 Integração dos Dados Agrícolas")

    st.write("""
    Esta seção representa a integração dos dados de manejo agrícola das Fases 1
    e 2 dentro do banco de dados estruturado.
    """)

    pasta = FASE3_DIR / "integracao_dados"

    if pasta.exists():
        arquivos = [a for a in pasta.rglob("*") if a.is_file()]
        if arquivos:
            for arquivo in arquivos:
                st.write(f"✅ `{arquivo.relative_to(FASE7_DIR)}`")
        else:
            st.info("Nenhum arquivo encontrado nesta pasta.")
    else:
        st.warning("Pasta ainda não encontrada.")
        st.code(str(pasta))

with tab_ir_alem:
    st.header("🚀 Programa do Ir Além")

    st.write("""
    Esta seção reúne as duas entregas do Programa do Ir Além relacionadas à Fase 3.
    """)

    pasta = FASE3_DIR / "ir_alem"

    if pasta.exists():
        arquivos = [a for a in pasta.rglob("*") if a.is_file()]
        if arquivos:
            for arquivo in arquivos:
                st.write(f"✅ `{arquivo.relative_to(FASE7_DIR)}`")
        else:
            st.info("Nenhum arquivo encontrado nesta pasta.")
    else:
        st.warning("Pasta ainda não encontrada.")
        st.code(str(pasta))