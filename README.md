# PerdeuAchou

Achados e perdidos de escola, no estilo do Google Sala de Aula.

## Como rodar

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations achados   # só confirma que está tudo em dia
python manage.py migrate
python manage.py runserver
```

Abra http://127.0.0.1:8000/

## Fluxo de navegação

1. `/` — "Bem vindo(a)" + botão **Seguir** (canto inferior direito)
2. `/salas/` — salas do usuário, uma abaixo da outra (pede login; há `/cadastro/`)
3. `/salas/<id>/` — objetos da sala. Só quem criou a sala pode adicionar/excluir
4. `/perfil/` — página "nada aqui" (avatar na navbar)

O botão **+** na navbar cria uma sala ou entra em uma por código.

## Banco de dados (`achados/models.py`)

- **Sala**: nome, descrição, criador, membros, código de entrada
- **Objeto**: sala, nome, descrição, local encontrado, quem adicionou, data
