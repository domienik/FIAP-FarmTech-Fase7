# 🧠 Fase 1 - CAP2: Reconhecimento de Utensílios com Teachable Machine

## 📚 Graduação ON em Inteligência Artificial - FIAP

## 👩🏻‍💻 Sobre o CAP2

Este capítulo apresenta uma introdução prática ao uso de **Inteligência Artificial aplicada à visão computacional**, utilizando a plataforma **Teachable Machine**, do Google.

A proposta foi desenvolver um modelo capaz de reconhecer e classificar utensílios de cozinha a partir de imagens, demonstrando como ferramentas acessíveis de Machine Learning podem ser usadas para resolver problemas simples do cotidiano.

---

## 🎯 Objetivo

O objetivo principal do CAP2 foi criar um modelo de classificação de imagens capaz de identificar diferentes utensílios de cozinha.

O modelo desenvolvido classifica imagens em três categorias:

- **Panelas**
- **Espátulas**
- **Assadeiras**

Além disso, a atividade teve como objetivo:

- Familiarizar o grupo com conceitos básicos de Machine Learning;
- Introduzir noções de visão computacional;
- Utilizar o Teachable Machine para treinar um modelo interativo;
- Avaliar o desempenho do modelo com imagens de teste;
- Documentar o processo em um relatório PDF.

---

## 🧩 Contexto do Problema

A cozinha é um ambiente com muitos utensílios diferentes. Encontrar ou identificar rapidamente o utensílio correto pode ser uma tarefa difícil em algumas situações, especialmente para pessoas com pouco espaço, baixa organização ou deficiência visual.

Nesse contexto, a Inteligência Artificial pode auxiliar na identificação automática desses objetos por meio de imagens.

---

## 🛠️ Tecnologias Utilizadas

- **Teachable Machine** — criação e treinamento do modelo de imagem;
- **Google Images** — coleta inicial das imagens;
- **Machine Learning** — classificação supervisionada;
- **Visão Computacional** — reconhecimento de padrões visuais;
- **PDF** — documentação do processo;
- **Arquivo `.tm`** — projeto exportado do Teachable Machine.

---

## 📂 Arquivos do CAP2

```text
cap2/
├── relatorio.pdf    # Relatório completo do projeto
├── project.tm       # Arquivo do projeto Teachable Machine
└── README.md        # Documentação do CAP2
```

---

## 🖼️ Coleta de Dados

Foram coletadas imagens de três classes de utensílios:

- Panelas;
- Espátulas;
- Assadeiras.

As imagens foram escolhidas buscando variedade de:

- Formatos;
- Cores;
- Tamanhos;
- Ângulos;
- Modelos;
- Materiais.

Essa diversidade foi importante para ajudar o modelo a aprender características visuais relevantes de cada categoria.

---

## 🏋️ Treinamento do Modelo

O treinamento foi realizado na plataforma **Teachable Machine**, utilizando o modo de **Classificação de Imagem**.

As imagens foram organizadas em três classes:

```text
Panelas
Espátulas
Assadeiras
```

### Configurações utilizadas

| Parâmetro | Valor |
|---|---:|
| Epochs | 50 |
| Batch Size | 16 |
| Learning Rate | 0.001 |

O Teachable Machine processou as imagens e treinou o modelo para reconhecer padrões visuais de cada classe.

---

## 📊 Resultados Obtidos

Após o treinamento, o modelo apresentou alta acurácia nas classes avaliadas.

Segundo o relatório, os testes indicaram bons resultados para as três categorias:

| Classe | Acurácia |
|---|---:|
| Panelas | 100% |
| Espátulas | 100% |
| Assadeiras | 100% |

A matriz de confusão também indicou que as amostras de teste foram classificadas corretamente dentro das categorias previstas.

---

## ✅ Teste e Validação

Após o treinamento, o modelo foi testado com imagens que não haviam sido usadas na etapa de treino.

Os testes mostraram que o modelo conseguiu identificar corretamente:

- Diferentes tipos de panelas;
- Espátulas com formatos variados;
- Assadeiras de tamanhos e materiais diferentes.

A etapa de validação ajudou a verificar se o modelo conseguia aplicar o aprendizado em novas imagens, e não apenas memorizar as imagens usadas no treinamento.

---

## 🔍 Análise Crítica

Apesar do bom desempenho, o modelo possui algumas limitações:

- Pode confundir objetos visualmente parecidos;
- Pode ser sensível a iluminação, fundo e ângulo da imagem;
- Foi treinado com poucas classes;
- Pode ter dificuldade com objetos fora do padrão usado no treinamento.

Exemplo: uma panela muito rasa e aberta poderia ser confundida com uma assadeira, dependendo do ângulo da imagem.

---

## 🚀 Sugestões de Melhorias

Para melhorar o modelo, seriam recomendadas as seguintes ações:

- Aumentar a quantidade de imagens por classe;
- Usar imagens com fundos mais variados;
- Incluir diferentes ângulos e perspectivas;
- Adicionar uma classe extra para “outros objetos”;
- Testar o modelo com imagens reais tiradas em diferentes ambientes;
- Comparar diferentes configurações de treinamento.

---

## 📌 Integração com a Fase 7

Na Fase 7, os materiais deste CAP foram integrados à dashboard central do projeto **FarmTech Solutions**.

A página da Fase 1 permite visualizar:

- O relatório PDF do projeto;
- O arquivo `project.tm`;
- As informações principais sobre classes, treinamento e resultados.

Essa integração demonstra a primeira experiência prática do grupo com visão computacional e classificação de imagens.

---

## ✅ Status

| Item | Status |
|---|---|
| Coleta de imagens | ✅ Concluída |
| Treinamento no Teachable Machine | ✅ Concluído |
| Testes e validação | ✅ Concluídos |
| Relatório PDF | ✅ Concluído |
| Arquivo `.tm` | ✅ Disponível |
| Integração na dashboard Fase 7 | ✅ Concluída |
| Documentação | ✅ Atualizada |

---

## 📋 Licença

Este material segue o modelo acadêmico da FIAP utilizado para organização de projetos da **Graduação ON em Inteligência Artificial**.
