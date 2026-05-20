import streamlit as st
from urllib.parse import quote


st.title("🌱 FarmTech Solutions - Integração Fase 7")

st.write("""
Esta dashboard reúne as principais entregas desenvolvidas nas fases anteriores
do projeto FarmTech Solutions, organizando os serviços em uma aplicação única
para consulta, análise e demonstração.
""")

st.divider()


def link_pagina(nome_pagina):
    return f"?pagina={quote(nome_pagina)}"

# =========================
# OBJETIVO
# =========================
st.header("🎯 Objetivo da Fase 7")

st.write("""
O objetivo da Fase 7 é consolidar as entregas anteriores em uma solução integrada
para gestão e análise no contexto do agronegócio. A aplicação centraliza dados,
modelos, simulações, dashboards, visão computacional e serviços em nuvem.
""")

st.info("""
A Fase 7 funciona como uma camada final de integração, conectando os conteúdos
das Fases 1, 2, 3, 4, 5 e 6 em uma dashboard única.
""")

st.divider()


# =========================
# BOTÕES DE NAVEGAÇÃO
# =========================
col1, col2, col3 = st.columns(3)

with col1:
    st.link_button(
        "📊 Fase 1 - Base de Dados",
        link_pagina("Fase 1 - Base de Dados"),
        use_container_width=True
    )

with col2:
    st.link_button(
        "🌡️ Fase 2 - IoT",
        link_pagina("Fase 2 - IoT"),
        use_container_width=True
    )

with col3:
    st.link_button(
        "🗄️ Fase 3 - Banco de Dados",
        link_pagina("Fase 3 - Banco de Dados Estruturado"),
        use_container_width=True
    )

col4, col5, col6 = st.columns(3)

with col4:
    st.link_button(
        "📈 Fase 4 - Data Science",
        link_pagina("Fase 4 - Dashboard e Data Science"),
        use_container_width=True
    )

with col5:
    st.link_button(
        "☁️ Fase 5 - AWS e Alertas",
        link_pagina("Fase 5 - AWS e Alertas"),
        use_container_width=True
    )

with col6:
    st.link_button(
        "👁️ Fase 6 - Visão Computacional",
        link_pagina("Fase 6 - Visão Computacional"),
        use_container_width=True
    )

# =========================
# RESUMO DAS FASES
# =========================
st.header("📌 Resumo das fases integradas")

fases = [
    {
        "fase": "Fase 1",
        "titulo": "Base de Dados e Lavouras",
        "descricao": "Sistema de cadastro de lavouras, cálculos agrícolas, análise estatística em R e introdução à IA.",
        "status": "Integrada"
    },
    {
        "fase": "Fase 2",
        "titulo": "IoT e Sensores",
        "descricao": "Projetos com ESP32, sensores simulados, dados agrícolas, scripts e análises complementares.",
        "status": "Integrada"
    },
    {
        "fase": "Fase 3",
        "titulo": "Banco de Dados Estruturado",
        "descricao": "Integração com Oracle, consultas SQL, dataset de sensores e materiais de Machine Learning.",
        "status": "Integrada"
    },
    {
        "fase": "Fase 4",
        "titulo": "Dashboard e Data Science",
        "descricao": "Dashboard em Streamlit, exploração de dados, modelagem preditiva e classificação de sementes.",
        "status": "Integrada"
    },
    {
        "fase": "Fase 5",
        "titulo": "AWS, Cloud e Alertas",
        "descricao": "Previsão de rendimento de safra, análise de custos AWS e espaço reservado para os alertas da Fase 7.",
        "status": "Parcialmente integrada"
    },
    {
        "fase": "Fase 6",
        "titulo": "Visão Computacional",
        "descricao": "Projeto com YOLOv5 para detecção de vacas e cachorros, comparação entre épocas e Ir Além com Transfer Learning.",
        "status": "Integrada"
    },
]

for item in fases:
    with st.container(border=True):
        col_a, col_b = st.columns([3, 1])

        with col_a:
            st.subheader(f"{item['fase']} - {item['titulo']}")
            st.write(item["descricao"])

        with col_b:
            if item["status"] == "Integrada":
                st.success(item["status"])
            else:
                st.warning(item["status"])


st.divider()


# =========================
# STATUS GERAL
# =========================
st.header("✅ Status geral da integração")

col1, col2, col3 = st.columns(3)

col1.metric("Fases integradas", "6")
col2.metric("Dashboard", "Streamlit")
col3.metric("Organização", "FASE7/assets")

st.markdown("""
| Item | Status |
|---|---|
| Fase 1 integrada | ✅ Concluído |
| Fase 2 integrada | ✅ Concluído |
| Fase 3 integrada | ✅ Concluído |
| Fase 4 integrada | ✅ Concluído |
| Fase 5 integrada | ✅ Parcial |
| Fase 6 integrada | ✅ Concluído |
| Alertas AWS da Fase 7 | ⏳ Pendente |
| README final | ⏳ Pendente |
| Vídeo final | ⏳ Pendente |
""")


st.divider()


# =========================
# ORGANIZAÇÃO
# =========================
st.header("🗂️ Como a dashboard está organizada")

st.write("""
A aplicação foi organizada em uma pasta central chamada `FASE7`, separando as
páginas do Streamlit dos arquivos usados por cada fase.
""")

st.code("""
FASE7/
├── app.py
├── pages/
│   ├── home_fase7.py
│   ├── fase1_base_dados.py
│   ├── fase2_iot.py
│   ├── fase3_banco_de_dados_estruturado.py
│   ├── fase4_dashboard_data_science.py
│   ├── fase5_aws_alertas.py
│   └── fase6_visao_computacional.py
└── assets/
    ├── fase1/
    ├── fase2/
    ├── fase3/
    ├── fase4/
    ├── fase5/
    └── fase6/
""", language="text")


st.divider()


# =========================
# ALERTAS AWS
# =========================
st.header("🚨 Aviso sobre os alertas AWS")

st.warning("""
A seção de alertas AWS ainda será finalizada pelo grupo. A ideia é demonstrar
um fluxo em que sensores, modelos ou análises visuais possam gerar notificações
por e-mail ou SMS usando serviços da AWS.
""")

st.write("""
Exemplo de fluxo esperado:
""")

st.code("""
Sensor ou modelo detecta problema
        ↓
Regra de alerta é ativada
        ↓
Serviço AWS processa o evento
        ↓
E-mail ou SMS é enviado para o responsável
""", language="text")


st.divider()


# =========================
# TECNOLOGIAS
# =========================
st.header("🛠️ Tecnologias utilizadas")

st.markdown("""
- **Python**
- **Streamlit**
- **Pandas**
- **Jupyter Notebook**
- **R**
- **Oracle Database**
- **ESP32**
- **YOLOv5**
- **TensorFlow / Keras**
- **AWS**
- **GitHub**
""")


st.divider()

st.success("Dashboard de integração da Fase 7 carregada com sucesso.")