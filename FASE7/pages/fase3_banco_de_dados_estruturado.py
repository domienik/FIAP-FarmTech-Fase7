from pathlib import Path
import re

import pandas as pd
import streamlit as st


FASE7_DIR = Path(__file__).resolve().parents[1]
FASE3_DIR = FASE7_DIR / "assets" / "fase3"
CAP1_DIR = FASE3_DIR / "cap1"

DATA_DIR = CAP1_DIR / "data"
DOCS_DIR = CAP1_DIR / "docs"
SRC_DIR = CAP1_DIR / "src"

CSV_SENSORES = DATA_DIR / "dados_sensores.csv"
SQL_FILE = SRC_DIR / "consultas.sql"
README_FILE = CAP1_DIR / "README.md"
IR_ALEM_2 = CAP1_DIR / "ir-alem-2.ipynb"


st.title("🗄️ Fase 3 - Banco de Dados Estruturado")

st.write("""
Nesta fase, o foco foi estruturar um banco de dados Oracle para armazenar,
consultar e analisar dados agrícolas coletados por sensores. A etapa também
inclui entregas do Programa Ir Além com dashboard em Python e Machine Learning.
""")

st.divider()

tab_cap1, tab_cap10, tab_gs = st.tabs([
    "📌 CAP1",
    "📌 CAP10",
    "🌎 GS - Global Solution"
])


# =========================
# CAP1
# =========================
with tab_cap1:
    tab_oracle, tab_dados, tab_sql, tab_evidencias, tab_ir_alem = st.tabs([
        "🗄️ Oracle",
        "📄 Dados",
        "💻 Consultas SQL",
        "🖼️ Evidências",
        "🚀 Ir Além"
    ])

    # =========================
    # ORACLE
    # =========================
    with tab_oracle:
        st.header("🗄️ Banco Oracle - SENSORES_FARMTECH")

        st.write("""
        A Fase 3 criou uma tabela relacional no Oracle para armazenar as leituras
        dos sensores agrícolas. Os dados importados vieram de um CSV gerado na fase
        anterior e foram usados em consultas de validação, filtros e estatísticas.
        """)

        col1, col2, col3 = st.columns(3)
        col1.metric("Tabela", "SENSORES_FARMTECH")
        col2.metric("Leituras", "48")
        col3.metric("Intervalo", "5 min")

        st.subheader("📌 Estrutura da tabela")

        st.code(
            """
CREATE TABLE SENSORES_FARMTECH (
  CREATED_AT        TIMESTAMP,
  PH_SOLO           NUMBER(4,2),
  UMIDADE_SOLO      NUMBER(5,1),
  NITROGENIO        NUMBER(5,0),
  FOSFORO           NUMBER(5,0),
  POTASSIO          NUMBER(5,0),
  STATUS_BOMBA      NUMBER(1,0),
  TEMPERATURA       NUMBER(4,1),
  SENSACAO_TERMICA  NUMBER(4,1),
  UMIDADE_AR        NUMBER(4,1)
);
""",
            language="sql"
        )

        st.subheader("🎥 Vídeo demonstrativo")
        st.video("https://youtu.be/Txpuv0JD0wU")

    # =========================
    # DADOS
    # =========================
    with tab_dados:
        st.header("📄 Base de Dados dos Sensores")

        st.write("""
        A base contém leituras simuladas de sensores agrícolas, incluindo pH do solo,
        umidade do solo, temperatura, sensação térmica, umidade do ar, nutrientes NPK
        e status da bomba.
        """)

        if CSV_SENSORES.exists():
            st.success(f"Arquivo encontrado: {CSV_SENSORES.relative_to(FASE7_DIR)}")

            try:
                df = pd.read_csv(CSV_SENSORES)

                st.dataframe(df, use_container_width=True)

                col1, col2, col3 = st.columns(3)
                col1.metric("Linhas", df.shape[0])
                col2.metric("Colunas", df.shape[1])
                col3.metric("Arquivo", CSV_SENSORES.name)

                st.subheader("📈 Prévia estatística")
                st.dataframe(df.describe(include="all"), use_container_width=True)

                colunas_numericas = df.select_dtypes(include="number").columns.tolist()

                if colunas_numericas:
                    coluna = st.selectbox(
                        "Selecione uma variável numérica para visualizar",
                        colunas_numericas
                    )

                    st.line_chart(df[coluna])

            except Exception as erro:
                st.error("Não foi possível carregar o CSV.")
                st.code(str(erro))
        else:
            st.warning("Arquivo dados_sensores.csv não encontrado.")
            st.code(str(CSV_SENSORES))

    # =========================
    # SQL
    # =========================
    with tab_sql:
        st.header("💻 Consultas SQL")

        st.write("""
        As consultas SQL validam a importação dos dados, filtram leituras relevantes
        e calculam estatísticas como média, máximo e mínimo de umidade do solo.
        """)

        if SQL_FILE.exists():
            st.success(f"Arquivo encontrado: {SQL_FILE.relative_to(FASE7_DIR)}")

            codigo_sql = SQL_FILE.read_text(encoding="utf-8", errors="ignore")
            st.code(codigo_sql, language="sql")

            with open(SQL_FILE, "rb") as f:
                st.download_button(
                    label="📥 Baixar consultas.sql",
                    data=f,
                    file_name=SQL_FILE.name,
                    mime="text/plain"
                )
        else:
            st.warning("Arquivo consultas.sql não encontrado.")
            st.code(str(SQL_FILE))

        st.subheader("📌 Consultas principais")

        st.markdown("""
        - `SELECT * FROM SENSORES_FARMTECH FETCH FIRST 20 ROWS ONLY`
        - `WHERE UMIDADE_SOLO > 70`
        - `ORDER BY PH_SOLO DESC`
        - `AVG`, `MAX` e `MIN` para análise estatística
        """)

    # =========================
    # EVIDÊNCIAS
    # =========================
    with tab_evidencias:
        st.header("🖼️ Evidências e Prints")

        st.write("""
        Esta aba reúne os prints do Oracle SQL Developer, importação dos dados,
        consultas SQL e resultados obtidos.
        """)

        if DOCS_DIR.exists():
            imagens = sorted(
                list(DOCS_DIR.glob("*.png")) +
                list(DOCS_DIR.glob("*.jpg")) +
                list(DOCS_DIR.glob("*.jpeg"))
            )

            if imagens:
                st.success(f"{len(imagens)} imagem(ns) encontrada(s).")

                imagem_destaque = st.selectbox(
                    "Selecione uma imagem para visualizar em destaque",
                    imagens,
                    format_func=lambda x: x.name
                )

                st.image(
                    str(imagem_destaque),
                    caption=imagem_destaque.name,
                    use_container_width=True
                )

                st.divider()

                st.subheader("📁 Galeria completa")

                colunas = st.columns(3)

                for index, imagem in enumerate(imagens):
                    with colunas[index % 3]:
                        st.image(
                            str(imagem),
                            caption=imagem.name,
                            use_container_width=True
                        )
            else:
                st.info("Nenhuma imagem encontrada na pasta docs.")
        else:
            st.warning("Pasta docs não encontrada.")
            st.code(str(DOCS_DIR))

    # =========================
    # IR ALÉM
    # =========================
    with tab_ir_alem:
        st.header("🚀 Programa Ir Além")

        tab_ir1, tab_ir2, tab_readme = st.tabs([
            "📊 Ir Além 1 - Dashboard",
            "🧠 Ir Além 2 - Machine Learning",
            "📘 README"
        ])

        with tab_ir1:
            st.subheader("📊 Ir Além 1 - Dashboard em Python")

            st.write("""
            O Ir Além 1 apresenta uma dashboard em Python para visualização das
            métricas principais dos sensores, gráficos interativos e recomendações
            de irrigação.
            """)

            st.video("https://youtu.be/J9iB4t9So8U")

            imagens_ir1 = [
                DOCS_DIR / "print1.png",
                DOCS_DIR / "print2.png",
                DOCS_DIR / "print3.png",
            ]

            for imagem in imagens_ir1:
                if imagem.exists():
                    st.image(str(imagem), caption=imagem.name, use_container_width=True)

        with tab_ir2:
            st.subheader("🧠 Ir Além 2 - Machine Learning no Agro")

            st.write("""
            O Ir Além 2 apresenta uma entrega com Machine Learning aplicada ao contexto
            agrícola, enviada em formato de notebook.
            """)

            st.video("https://youtu.be/pic7SCPDPn0")

            notebooks = sorted(CAP1_DIR.glob("*.ipynb"))

            if notebooks:
                st.write("Notebook(s) encontrado(s):")
                for notebook in notebooks:
                    st.write(f"✅ `{notebook.relative_to(FASE7_DIR)}`")

                    with open(notebook, "rb") as f:
                        st.download_button(
                            label=f"📥 Baixar {notebook.name}",
                            data=f,
                            file_name=notebook.name,
                            mime="application/octet-stream"
                        )
            else:
                st.info("Nenhum notebook .ipynb encontrado na pasta da Fase 3.")

        with tab_readme:
            st.subheader("📘 README da Fase 3")

            if README_FILE.exists():
                conteudo = README_FILE.read_text(encoding="utf-8", errors="ignore")

                st.markdown(conteudo)

                links = re.findall(r"https?://[^\s)]+", conteudo)

                if links:
                    st.subheader("🔗 Links encontrados")
                    for i, link in enumerate(links, start=1):
                        st.markdown(f"{i}. [{link}]({link})")
            else:
                st.warning("README.md da Fase 3 não encontrado.")
                st.code(str(README_FILE))


# =========================
# CAP10
# =========================
with tab_cap10:
    st.header("📌 CAP10")

    st.info("Conteúdo do CAP10 será adicionado posteriormente.")


# =========================
# GS - GLOBAL SOLUTION
# =========================
with tab_gs:
    st.header("🌎 GS - Global Solution")

    st.info("Conteúdo da Global Solution será adicionado posteriormente.")