# Classificação da Saúde Fetal por Cardiotocograma (CTG)

Este repositório contém um projeto de Machine Learning para classificar a saúde fetal em três categorias (Normal, Suspeito e Patológico) utilizando dados de Cardiotocogramas (CTG).

O objetivo principal deste estudo é desenvolver e avaliar modelos de classificação com foco na **segurança clínica**, priorizando a minimização de Falsos Negativos nas classes de alto risco (Suspeito e Patológico).

---

## Fonte de Dados e Atribuição

O dataset utilizado para este estudo é de acesso público, e a condição para seu uso é a correta atribuição de crédito aos autores originais.

**Por favor, cite o seguinte trabalho:**

> Ayres de Campos et al. (2000) SisPorto 2.0 A Program for Automated Analysis of Cardiotocograms. J Matern Fetal Med 5:311-318 [(link)](https://onlinelibrary.wiley.com/doi/10.1002/1520-6661(200009/10)9:5<311::AID-MFM12>3.0.CO;2-9)

**Atribuições de Mídia:**
* **Splash banner:** Photo by Aditya Romansa on Unsplash.
* **Splash icon:** Icon by Freepik available on Flaticon.

---

## Modelos e Metodologia

Três modelos de classificação foram treinados e comparados: Random Forest (RF), Regressão Logística (LR) e K-Nearest Neighbors (KNN).

**Distribuição dos Dados:**
* **Total de Amostras:** 2126
* **Classes:** Normal (77.84%), Suspeito (13.87%), Patológico (8.27%)
* **Divisão:** 70% Treino (`train_size=0.7`), 30% Teste (`test_size=0.3`, $\approx 638$ amostras), com estratificação.

### Matrizes de Confusão (Dados de Teste - 30%)

| Modelo | Normal (N) | Suspeito (S) | Patológico (P) |
| :---: | :---: | :---: | :---: |
| **Random Forest** | `[[483, 13, 1], [20, 66, 2], [7, 2, 44]]` |
| **Logistic Regression** | `[[478, 12, 7], [53, 32, 3], [8, 8, 37]]` |
| **K-Nearest Neighbors** | `[[475, 19, 3], [42, 43, 3], [9, 6, 38]]` |

---

## Análise de Desempenho e Modelo Escolhido

Em um problema de classificação de saúde fetal, o **Recall (Sensibilidade)** nas classes de risco (Suspeito e Patológico) é a métrica mais crítica, pois mede a capacidade do modelo de identificar corretamente os casos que *realmente* precisam de atenção.

| Modelo | Recall (Suspeito) | Recall (Patológico) | FN Perigosos (P → N) |
| :---: | :---: | :---: | :---: |
| **Random Forest** | **75.0%** (66/88) | **83.0%** (44/53) | **7** |
| **Logistic Regression** | 36.4% (32/88) | 69.8% (37/53) | 8 |
| **K-Nearest Neighbors** | 48.9% (43/88) | 71.7% (38/53) | 9 |

### Conclusão

O modelo **Random Forest** foi selecionado como o melhor preditor, apresentando o desempenho mais robusto e seguro:

1.  **Melhor Detecção de Risco:** Demonstrou o maior Recall nas classes Suspeito e Patológico.
2.  **Minimização de Falsos Negativos:** Cometeu o menor número de Falsos Negativos Patológico → Normal (**7** casos), o erro de classificação de maior risco clínico.

---

## Como Executar o Projeto

1.  **Clonar o Repositório:**
    ```bash
    git clone https://github.com/Mokekinho/FetalHealthAI.git
    ```

2.  **Instalar Dependências:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Executar o Notebook:**
    Abra o arquivo `notebook.ipynb` para replicar o treinamento e a análise dos modelos.