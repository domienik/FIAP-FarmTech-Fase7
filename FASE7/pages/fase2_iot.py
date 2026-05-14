from pathlib import Path
import re
import pandas as pd

import streamlit as st


FASE7_DIR = Path(__file__).resolve().parents[1]
FASE2_DIR = FASE7_DIR / "assets" / "fase2"

ESP32_DIR = FASE2_DIR / "cap1" / "ESP32"
CODIGO_ESP32 = ESP32_DIR / "codigo_esp32.ino"
GALERIA_DIR = ESP32_DIR / "assets"

DATA_SCIENCE_DIR = FASE2_DIR / "cap1" / "data_science"

ARQUIVO_RDATA = DATA_SCIENCE_DIR / ".RData"
ARQUIVO_RHISTORY = DATA_SCIENCE_DIR / ".Rhistory"
ARQUIVO_DADOS_SENSORES = DATA_SCIENCE_DIR / "dados_sensores.csv"
ARQUIVO_MODELO_RDS = DATA_SCIENCE_DIR / "modelo_bomba.rds"

st.title("📡 Fase 2 - IoT, Sensores e ESP32")

st.write("""
Nesta seção estão os materiais da Fase 2 relacionados à aplicação com ESP32,
sensores, links de apoio e evidências visuais do projeto.
""")

st.divider()

tab_links, tab_esp32, tab_galeria, tab_data_science = st.tabs([
    "🔗 Links",
    "🤖 Código ESP32",
    "🖼️ Galeria",
    "📊 Data Science"
])

# =========================
# ABA LINKS
# =========================
with tab_links:
    with tab_links:
        st.header("🔗 Links do Projeto")

        st.subheader("🎥 Vídeo de demonstração")
        st.video("https://www.youtube.com/watch?v=ZCE25_D37qg")

        st.divider()

        st.subheader("🖼️ Imagem do projeto")
        st.image(
            "https://i.imgur.com/hiLPUVm.png",
            caption="Imagem demonstrativa do projeto ESP32",
            use_container_width=True
        )

        st.divider()

        st.subheader("📎 Links adicionais")

        links_files = list(FASE2_DIR.rglob("links.txt"))

    if not links_files:
        st.warning("Nenhum arquivo links.txt encontrado dentro de assets/fase2.")
        st.code(str(FASE2_DIR))
    else:
        links_file = links_files[0]

        st.success(f"Arquivo encontrado: {links_file.relative_to(FASE7_DIR)}")

        conteudo = links_file.read_text(encoding="utf-8", errors="ignore")
        links = re.findall(r"https?://[^\s]+", conteudo)

        if links:
            st.subheader("Links encontrados")

            for i, link in enumerate(links, start=1):
                st.markdown(f"{i}. [{link}]({link})")
        else:
            st.info("Nenhum link no formato http/https foi encontrado.")

        with st.expander("Ver conteúdo completo do links.txt"):
            st.code(conteudo, language="text")


# =========================
# ABA ESP32
# =========================
with tab_esp32:
    st.header("🤖 Código ESP32")

    st.write("""
    Esta aba apresenta o código utilizado no ESP32 para leitura de sensores,
    controle de lógica do sistema e apoio à automação agrícola.
    """)

    if CODIGO_ESP32.exists():
        st.success(f"Arquivo encontrado: {CODIGO_ESP32.relative_to(FASE7_DIR)}")

        codigo = CODIGO_ESP32.read_text(encoding="utf-8", errors="ignore")

        st.subheader("📄 codigo_esp32.ino")
        st.code(codigo, language="cpp")

        st.info("Este arquivo deve ser aberto na Arduino IDE, PlatformIO ou simulador como Wokwi.")

        with open(CODIGO_ESP32, "rb") as f:
            st.download_button(
                label="📥 Baixar código ESP32",
                data=f,
                file_name=CODIGO_ESP32.name,
                mime="text/plain"
            )
    else:
        st.warning("Arquivo codigo_esp32.ino não encontrado.")
        st.code(str(CODIGO_ESP32))


# =========================
# ABA GALERIA
# =========================
with tab_galeria:
    st.header("🖼️ Galeria do Projeto ESP32")

    st.write("""
    Esta galeria reúne as imagens do projeto, como montagem do circuito,
    simulação, sensores, dashboard ou evidências visuais da aplicação.
    """)

    if not GALERIA_DIR.exists():
        st.warning("Pasta de galeria não encontrada.")
        st.code(str(GALERIA_DIR))
    else:
        imagens = sorted(GALERIA_DIR.glob("*.png"))

        if not imagens:
            st.info("Nenhuma imagem PNG encontrada na pasta de galeria.")
        else:
            st.success(f"{len(imagens)} imagem(ns) encontrada(s).")

            # Imagem em destaque
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

            st.subheader("📁 Todas as imagens")

            # Galeria em grade com 3 colunas
            colunas = st.columns(3)

            for index, imagem in enumerate(imagens):
                with colunas[index % 3]:
                    st.image(
                        str(imagem),
                        caption=imagem.name,
                        use_container_width=True
                    )

                    with open(imagem, "rb") as f:
                        st.download_button(
                            label="Baixar",
                            data=f,
                            file_name=imagem.name,
                            mime="image/png",
                            key=f"download_{imagem.name}"
                        )

# =========================
# ABA DATA SCIENCE
# =========================
with tab_data_science:
    st.header("📊 Data Science - Sensores e Modelo da Bomba")

    st.write("""
    Esta aba apresenta os arquivos de Data Science usados na Fase 2,
    incluindo dados de sensores, histórico do R e arquivos do modelo treinado.
    """)

    tab_rdata, tab_rhistory, tab_dados, tab_modelo = st.tabs([
        "📦 .RData",
        "📜 .Rhistory",
        "🌡️ dados_sensores",
        "🧠 modelo_bomba.rds"
    ])

    # -------------------------
    # .RData
    # -------------------------
    with tab_rdata:
        st.subheader("📦 Arquivo .RData")

        if ARQUIVO_RDATA.exists():
            st.success(f"Arquivo encontrado: {ARQUIVO_RDATA.relative_to(FASE7_DIR)}")

            st.info("""
            O arquivo `.RData` armazena objetos do ambiente R, como datasets,
            variáveis, modelos ou resultados salvos durante a análise.
            """)

            st.write("Tamanho do arquivo:")
            st.code(f"{ARQUIVO_RDATA.stat().st_size / 1024:.2f} KB")

            with open(ARQUIVO_RDATA, "rb") as f:
                st.download_button(
                    label="📥 Baixar .RData",
                    data=f,
                    file_name=ARQUIVO_RDATA.name,
                    mime="application/octet-stream"
                )
        else:
            st.warning("Arquivo .RData não encontrado.")
            st.code(str(ARQUIVO_RDATA))

    # -------------------------
    # .Rhistory
    # -------------------------
    with tab_rhistory:
        st.subheader("📜 Histórico de comandos R")

        if ARQUIVO_RHISTORY.exists():
            st.success(f"Arquivo encontrado: {ARQUIVO_RHISTORY.relative_to(FASE7_DIR)}")

            conteudo = ARQUIVO_RHISTORY.read_text(encoding="utf-8", errors="ignore")

            if conteudo.strip():
                st.code(conteudo, language="r")
            else:
                st.info("O arquivo .Rhistory está vazio.")

            with open(ARQUIVO_RHISTORY, "rb") as f:
                st.download_button(
                    label="📥 Baixar .Rhistory",
                    data=f,
                    file_name=ARQUIVO_RHISTORY.name,
                    mime="text/plain"
                )
        else:
            st.warning("Arquivo .Rhistory não encontrado.")
            st.code(str(ARQUIVO_RHISTORY))

    # -------------------------
    # dados_sensores
    # -------------------------
    with tab_dados:
        st.subheader("🌡️ Dados dos Sensores")

        if ARQUIVO_DADOS_SENSORES.exists():
            st.success(f"Arquivo encontrado: {ARQUIVO_DADOS_SENSORES.relative_to(FASE7_DIR)}")

            try:
                df = pd.read_csv(ARQUIVO_DADOS_SENSORES)

                st.dataframe(df, use_container_width=True)

                col1, col2, col3 = st.columns(3)
                col1.metric("Linhas", df.shape[0])
                col2.metric("Colunas", df.shape[1])
                col3.metric("Arquivo", ARQUIVO_DADOS_SENSORES.name)

                st.subheader("📈 Prévia estatística")
                st.dataframe(df.describe(include="all"), use_container_width=True)

            except Exception as erro:
                st.error("Não foi possível carregar o arquivo como CSV.")
                st.code(str(erro))

                st.info("Exibindo conteúdo bruto:")
                conteudo = ARQUIVO_DADOS_SENSORES.read_text(encoding="utf-8", errors="ignore")
                st.code(conteudo[:5000], language="text")

            with open(ARQUIVO_DADOS_SENSORES, "rb") as f:
                st.download_button(
                    label="📥 Baixar dados_sensores",
                    data=f,
                    file_name=ARQUIVO_DADOS_SENSORES.name,
                    mime="text/csv"
                )
        else:
            st.warning("Arquivo dados_sensores não encontrado.")
            st.code(str(ARQUIVO_DADOS_SENSORES))

    # -------------------------
    # modelo_bomba.rds
    # -------------------------

    with tab_modelo:
        st.subheader("🧠 Modelo da Bomba - RDS")

        if ARQUIVO_MODELO_RDS.exists():
            st.success(f"Arquivo encontrado: {ARQUIVO_MODELO_RDS.relative_to(FASE7_DIR)}")

            st.info("""
            O arquivo `.rds` é um objeto salvo pelo R. Ele pode conter um modelo treinado,
            neste caso relacionado à lógica de acionamento/previsão da bomba.
            """)

            st.write("Tamanho do arquivo:")
            st.code(f"{ARQUIVO_MODELO_RDS.stat().st_size / 1024:.2f} KB")

            st.write("Exemplo de comando para carregar no R:")
            st.code(
                'modelo <- readRDS("modelo_bomba.rds")',
                language="r"
            )

            with open(ARQUIVO_MODELO_RDS, "rb") as f:
                st.download_button(
                    label="📥 Baixar modelo_bomba.rds",
                    data=f,
                    file_name=ARQUIVO_MODELO_RDS.name,
                    mime="application/octet-stream"
                )
        else:
            st.warning("Arquivo modelo_bomba.rds não encontrado.")
            st.code(str(ARQUIVO_MODELO_RDS))


st.divider()

st.header("📌 Integração com a Fase 7")

st.write("""
Esta página integra os links, o código ESP32 e as evidências visuais da Fase 2
dentro do dashboard central da Fase 7, mantendo os arquivos organizados dentro
da pasta assets.
""")