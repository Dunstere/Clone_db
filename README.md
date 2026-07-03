# Projeto de Importação e Migração de Dados Espaciais (PostGIS)

Este projeto consiste em um conjunto de scripts automatizados em Python para a manipulação de dados geográficos (Shapefiles) e sua integração com bancos de dados espaciais PostgreSQL utilizando a extensão **PostGIS**.

O objetivo principal é ler um arquivo de mapa local, tratá-lo, inseri-lo em um banco de dados de origem e, posteriormente, realizar a migração/clone desses dados para um segundo banco de dados em um servidor diferente.

---

## 🗺️ Fluxo do Projeto



1. **Script 1 (`load_shp_db1.py`):** * Lê um arquivo Shapefile local (`.shp`).
   * Valida/aplica o Sistema de Referência de Coordenadas correto (EPSG:4674 - SIRGAS 2000).
   * Conecta ao **Banco de Dados 1 (Porta 5432)** e salva os dados na tabela `regions`.

2. **Script 2 (`clone_regions.py`):**
   * Conecta ao **Banco de Dados 1** e extrai todos os registros da tabela `regions`.
   * Conecta ao **Banco de Dados 2 (Porta 5433)**.
   * Transfere/clona os dados criando uma tabela idêntica no novo servidor.

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

* **Python 3.x**
* **GeoPandas:** Para leitura, manipulação e escrita de dados geográficos.
* **SQLAlchemy:** Para a criação dos motores de conexão com os bancos de dados.
* **GeoAlchemy2 & Psycopg2:** Suporte de bastidores para comunicação com o PostgreSQL/PostGIS.

---

## 🚀 Como Configurar e Executar

### 1. Pré-requisitos
Certifique-se de ter o Python instalado (recomenda-se o uso do Miniconda/Anaconda) e os dois bancos de dados PostgreSQL/PostGIS ativos nas portas correspondentes.

### 2. Instalação das Dependências
Abra o seu terminal ou prompt de comando e instale as bibliotecas necessárias executando:

```bash
pip install geopandas sqlalchemy psycopg2-binary geoalchemy2 pyogrio
