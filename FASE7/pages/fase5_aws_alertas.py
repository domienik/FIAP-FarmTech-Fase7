from pathlib import Path

import pandas as pd
import streamlit as st


FASE7_DIR = Path(__file__).resolve().parents[1]
FASE5_DIR = FASE7_DIR / "assets" / "fase5"
CAP1_DIR = FASE5_DIR / "cap1"

README_FILE = CAP1_DIR / "README.md"
CROP_YIELD = CAP1_DIR / "crop_yield.csv"
NOTEBOOK_EXECUTED = CAP1_DIR / "executed_notebook.ipynb"
NOTEBOOK_PBL = CAP1_DIR / "RivandoBezerra_rm568235_pbl_fase4.ipynb"
IR_ALEM = CAP1_DIR / "ir_alem"
ROTEIRO_VIDEO = CAP1_DIR / "ROTEIRO_VIDEO.md"
IMAGENS_DIR = CAP1_DIR / "ATV5_2"


st.title("☁️ Fase 5 - AWS, Cloud e Alertas")

st.write("""
Nesta fase, foram trabalhados conceitos de Machine Learning aplicado à previsão
de rendimento de safra e análise de infraestrutura em nuvem com AWS.
""")

st.divider()

tab_alertas, tab_cap1 = st.tabs([
    "🚨 Alertas Fase 7",
    "📌 CAP1 - Machine Learning e AWS"
])


# =========================
# ALERTAS FASE 7
# =========================
with tab_alertas:
    st.header("🚨 Alertas da Fase 7")

    st.info("""
    Esta aba será preenchida pelo grupo com o serviço de alerta solicitado na Fase 7,
    usando AWS para envio de e-mail ou SMS a partir de sensores ou análises visuais.
    """)


# =========================
# CAP1
# =========================
with tab_cap1:
    st.header("📌 CAP1 - Previsão de Rendimento de Safra com Machine Learning")

    st.write("""
    O CAP1 apresenta uma solução para previsão de rendimento de safra usando dados
    climáticos e agrícolas. A atividade também inclui uma análise de custos na AWS
    para hospedar o modelo em uma API.
    """)

    col1, col2, col3 = st.columns(3)
    col1.metric("Registros", "155")
    col2.metric("Culturas", "4")
    col3.metric("Modelos", "5")

    st.divider()

    tab_resumo, tab_dataset, tab_notebooks, tab_aws, tab_readme = st.tabs([
        "📌 Resumo",
        "🌾 Dataset",
        "📓 Notebooks",
        "☁️ AWS",
        "📘 README"
    ])

    # =========================
    # RESUMO
    # =========================
    with tab_resumo:
        st.subheader("📌 Objetivo do Projeto")

        st.write("""
        O objetivo foi analisar uma base com condições de solo e clima relacionadas
        ao rendimento agrícola, explorando os dados, identificando padrões com
        clusterização e criando modelos supervisionados para prever o rendimento
        das safras.
        """)

        st.subheader("🧠 Modelos utilizados")

        st.markdown("""
        - Regressão Linear
        - Ridge Regression
        - Lasso Regression
        - Random Forest Regressor
        - Gradient Boosting Regressor
        """)

        st.subheader("🎥 Vídeos demonstrativos")

        st.markdown("""
        - [Entrega 1 - Machine Learning](https://youtu.be/rW4sRL_B4HM)
        - [Entrega 2 - AWS](https://youtu.be/Pp_OM9_DHxg)
        """)

    # =========================
    # DATASET
    # =========================
    with tab_dataset:
        st.subheader("🌾 Dataset crop_yield.csv")

        if CROP_YIELD.exists():
            st.success(f"Arquivo encontrado: {CROP_YIELD.relative_to(FASE7_DIR)}")

            try:
                df = pd.read_csv(CROP_YIELD)

                st.dataframe(df, use_container_width=True)

                col1, col2, col3 = st.columns(3)
                col1.metric("Linhas", df.shape[0])
                col2.metric("Colunas", df.shape[1])
                col3.metric("Arquivo", CROP_YIELD.name)

                st.subheader("📈 Prévia estatística")
                st.dataframe(df.describe(include="all"), use_container_width=True)

            except Exception as erro:
                st.error("Não foi possível carregar o CSV.")
                st.code(str(erro))

            with open(CROP_YIELD, "rb") as f:
                st.download_button(
                    label="📥 Baixar crop_yield.csv",
                    data=f,
                    file_name=CROP_YIELD.name,
                    mime="text/csv"
                )
        else:
            st.warning("Arquivo crop_yield.csv não encontrado.")
            st.code(str(CROP_YIELD))

    # =========================
    # NOTEBOOKS
    # =========================
    with tab_notebooks:
        st.subheader("📓 Notebooks do Projeto")

        notebooks = [
            NOTEBOOK_EXECUTED,
            NOTEBOOK_PBL,
        ]

        for notebook in notebooks:
            if notebook.exists():
                st.success(f"Arquivo encontrado: {notebook.relative_to(FASE7_DIR)}")

                with open(notebook, "rb") as f:
                    st.download_button(
                        label=f"📥 Baixar {notebook.name}",
                        data=f,
                        file_name=notebook.name,
                        mime="application/octet-stream"
                    )
            else:
                st.info(f"Notebook não encontrado: {notebook.name}")

        st.divider()

        st.subheader("🔧 Ir Além - Arduino")

        if IR_ALEM.exists():
            st.success(f"Arquivo encontrado: {IR_ALEM.relative_to(FASE7_DIR)}")

            try:
                conteudo = IR_ALEM.read_text(encoding="utf-8", errors="ignore")
                st.code(conteudo, language="text")
            except Exception:
                st.write(f"✅ `{IR_ALEM.relative_to(FASE7_DIR)}`")

            with open(IR_ALEM, "rb") as f:
                st.download_button(
                    label="📥 Baixar Ir Além",
                    data=f,
                    file_name=IR_ALEM.name,
                    mime="application/octet-stream"
                )
        else:
            st.info("Arquivo do Ir Além não encontrado.")

    # =========================
    # AWS
    # =========================
    with tab_aws:
        st.subheader("☁️ Entrega AWS - Estimativa de Custo")

        st.write("""
        A entrega de AWS estimou o custo para hospedar o modelo de Machine Learning
        em uma instância EC2, comparando as regiões São Paulo e Virgínia do Norte.
        """)

        col1, col2 = st.columns(2)
        col1.metric("São Paulo", "$18,62/mês")
        col2.metric("Virgínia", "$10,86/mês")

        st.info("""
        Apesar de Virgínia ser mais barata, São Paulo foi escolhida por motivos
        de LGPD, menor latência e soberania dos dados.
        """)

        if IMAGENS_DIR.exists():
            imagens = sorted(
                list(IMAGENS_DIR.glob("*.png")) +
                list(IMAGENS_DIR.glob("*.jpg")) +
                list(IMAGENS_DIR.glob("*.jpeg"))
            )

            if imagens:
                st.success(f"{len(imagens)} imagem(ns) encontrada(s).")

                imagem_destaque = st.selectbox(
                    "Selecione uma imagem para visualizar",
                    imagens,
                    format_func=lambda x: x.name
                )

                st.image(
                    str(imagem_destaque),
                    caption=imagem_destaque.name,
                    use_container_width=True
                )

                st.divider()

                st.subheader("📁 Galeria AWS")

                colunas = st.columns(2)

                for index, imagem in enumerate(imagens):
                    with colunas[index % 2]:
                        st.image(
                            str(imagem),
                            caption=imagem.name,
                            use_container_width=True
                        )
            else:
                st.info("Nenhuma imagem encontrada em ATV5_2.")
        else:
            st.warning("Pasta ATV5_2 não encontrada.")
            st.code(str(IMAGENS_DIR))

        st.divider()

        st.subheader("📝 Roteiro do Vídeo")

        if ROTEIRO_VIDEO.exists():
            conteudo = ROTEIRO_VIDEO.read_text(encoding="utf-8", errors="ignore")
            st.markdown(conteudo)
        else:
            st.info("ROTEIRO_VIDEO.md não encontrado.")

    # =========================
    # README
    # =========================
    with tab_readme:
        st.subheader("📘 README do CAP1")

        if README_FILE.exists():
            conteudo = README_FILE.read_text(encoding="utf-8", errors="ignore")
            st.markdown(conteudo)
        else:
            st.warning("README.md não encontrado.")
            st.code(str(README_FILE))