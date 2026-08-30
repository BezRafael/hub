# HUB
Ambiente onde concentra ferramentas que estou estudando

Após o clone, é necessário instalar as bibliotecas para poder utilizar. Então...
```
python -m venv venv

ou

python3 -m venv venv
```
- Para instalar o ambiente virtual

```
pip install -r requirements.txt 
```
- Para instalar as bibliotecas listadas no arquivo ``requirements.txt``

> Lembrando de usar o segundo comando, somente quando o ambiente estiver ativado


# Estrutura do Projeto
```
──────────────────────────────────|
tmo_hub/
├── pages/          
├─────── abrir_chamado.py                      # tela para abrir chamados
├─────── inicio.py                             # tela início/apresentação   
├─────── r2-d2.py                              # Agente de IA
├─────── tars.py                               # Agente de IA
├── app.py                                     # configuração e navegação das páginas
├── requirements.txt                           # bibliotecas do projeto
└─────────────────────────────────|           
```

# Inicialização

Para rodar a aplicação, rode esse comando
```
streamlit run app.py
```
