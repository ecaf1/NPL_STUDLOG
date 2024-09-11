# NPL_STUDLOG: Estudo e Implementação de Processamento de Linguagem Natural

Este repositório contém implementações práticas de diversas técnicas de Processamento de Linguagem Natural (PLN) e aprendizado de máquina aplicadas a dados textuais. O objetivo é registrar meu aprendizado e resolução de questões relacionadas a PLN e modelos baseados em texto, juntamente com o uso de diferentes algoritmos e métodos de análise.

## Estrutura do Repositório

```
/notebooks
    ├── Text Processing and Analysis.ipynb
    ├── Dimensionality Reduction and Clustering.ipynb
    ├── Text Classification.ipynb
    └── Topic Modeling.ipynb
```
```
/Data
    └── bbc_data.csv
```

## Principais Notebooks

### Text Processing and Analysis.ipynb
Realiza o pré-processamento dos dados textuais, aplicando tokenização, remoção de stopwords e lematização. Este notebook utiliza a biblioteca nltk para a manipulação e limpeza dos textos.

### Dimensionality Reduction and Clustering.ipynb
Aplicamos a redução de dimensionalidade com PCA (Principal Component Analysis) e agrupamento utilizando K-means para encontrar padrões nos dados. O método elbow é usado para identificar o número ideal de clusters.

### Text Classification.ipynb
Neste notebook, classificadores como Regressão Logística, Naive Bayes, e SVM são treinados usando representações vetoriais como Bag of Words e TF-IDF. As métricas de avaliação incluem acurácia, precisão, recall e F1-score.

### Topic Modeling.ipynb
Aqui são explorados métodos de modelagem de tópicos como LDA, NMF e SVD. As métricas de avaliação incluem coerência e perplexidade, fornecendo uma análise detalhada dos tópicos gerados.

## Conjunto de Dados
* **bbc_data.csv:** Este arquivo contém notícias da BBC em cinco categorias principais: business, entertainment, politics, sport, e tech. É a base principal para as análises e experimentos desenvolvidos nos notebooks.

## Tecnologias e Bibliotecas Utilizadas
* Python 3.9+
* Jupyter Notebooks
* Bibliotecas: pandas, numpy, matplotlib, seaborn, nltk, scikit-learn, gensim

## Como Executar
1. Clone este repositório:
```bash
git clone https://github.com/seu-usuario/NPL_STUDLOG.git
```
2. Instale as dependências com Poetry:
```bash
poetry install
```
2.1. Instale as depedências com pip:
```bash
pip install requirements.txt
```
3. Execute os notebooks diretamente no Jupyter Notebook ou JupyterLab.

## Objetivo do Repositório
Este repositório foi criado para servir como um registro do meu aprendizado em PLN e para resolver exercícios práticos e listas de questões do curso. Além disso, os notebooks aqui presentes exemplificam a aplicação de técnicas avançadas de processamento e modelagem de dados textuais.

## Contribuições
Contribuições são bem-vindas! Se você quiser sugerir melhorias ou corrigir algo, sinta-se à vontade para abrir issues ou enviar pull requests.


