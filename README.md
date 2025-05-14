# Teste Técnico - Integração com APIs Farmina (Zendesk)

Este projeto foi desenvolvido como parte de um teste técnico e consiste em uma aplicação web simples usando **Flask** que consome a API:

- **API Farmina**  para listar "Cuidados Especiais" (`specialcares`) e buscar produtos com base em filtros como espécie, tipo de produto, estágio da vida, gestação, lactação e cuidados especiais

---

## Tecnologias Utilizadas

- Python 3.10+
- Flask
- Requests
- HTML (Jinja2)
- CSS (customizado)

---

## Instalação

### 1. Clone o projeto

```bash
git clone https://github.com/GabrielRibeiroBatista/teste_farmina_zendesk.git
cd teste_farmina_zendesk
```

### 2. Crie um ambiente virtual (recomendado)
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```
# ou
```bash
source venv/bin/activate  # Linux/macOS
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente
Crie um arquivo .env na raiz do projeto com as seguintes variáveis:
```env
API_USER=wsfarmina_zendesk
API_PASS=test
API_BASE_URL=https://gw-c.petgenius.info/wfservice/z1
```

### 5. Execute a aplicação
```bash
python app.py
```

Abra no navegador: http://localhost:5000

## Estrutura do Projeto
```bash
.
├── app.py                  # Script principal do Flask
├── templates/
│   ├── index.html          # Página inicial com o formulário
│   └── results.html        # Página com os resultados
├── static/
│   └── style.css           # Estilo CSS
├── .env                    # Variáveis de ambiente (não versionar)
├── requirements.txt        # Dependências do projeto
└── README.md               # Este arquivo
```

## Funcionalidades
- Formulário de busca com campos:

 - Tipo de Produto (dry, wet)

 - Espécie (dog, cat)

 - Estágio de Vida

 - Gestação e Lactação

 - Cuidados Especiais (populado dinamicamente via API)

- Busca de produtos na API da Farmina com base nos filtros

- Exibição dos resultados em tela

- Logs para facilitar debug e integração

## Autor
Gabriel Batista