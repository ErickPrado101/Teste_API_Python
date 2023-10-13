# Teste_API_Python


---

# Projeto de Envio de E-mails com Django

Este é um projeto de exemplo que demonstra como criar uma API Django com autenticação OAuth2 para enviar e-mails automaticamente. Este README fornecerá instruções sobre como configurar e executar o projeto em sua máquina.

## Pré-requisitos

Certifique-se de ter Python e Django instalados em sua máquina. Se você não os tiver, você pode instalá-los usando os seguintes comandos:

```bash
pip install django
```

## Configuração do Projeto

1. Clone este repositório do GitHub para sua máquina local.

```bash
git clone https://github.com/seu-usuario/meu_projeto.git
cd meu_projeto
```

2. Crie um ambiente virtual para o projeto (opcional, mas recomendado).

```bash
python -m venv env
```

3. Ative o ambiente virtual.

- No Windows:

```bash
env\Scripts\activate
```

- No macOS e Linux:

```bash
source env/bin/activate
```

4. Instale as dependências do projeto.

```bash
pip install -r requirements.txt
```

5. Aplique as migrações para criar as tabelas no banco de dados.

```bash
python manage.py makemigrations
python manage.py migrate
```

6. Crie um superusuário para acessar a área de administração.

```bash
python manage.py createsuperuser
```

7. Inicie o servidor de desenvolvimento do Django.

```bash
python manage.py runserver
```

Agora, você pode acessar a API em `http://localhost:8000/` e a área de administração em `http://localhost:8000/admin/`. Use o superusuário criado anteriormente para fazer login na área de administração.

## Uso da API

A API permite que você envie e-mails automaticamente. Para enviar um e-mail, você pode usar uma ferramenta como [curl](https://curl.se/) ou [Postman](https://www.postman.com/) ou criar seu próprio cliente. 

Exemplo de solicitação POST para enviar um e-mail:

```bash
curl -X POST http://localhost:8000/envio_email/emails/ -H "Content-Type: application/json" -d '{
  "subject": "Assunto do E-mail",
  "message": "Mensagem do E-mail",
  "recipient": "destinatario@example.com"
}'
```

Isso é apenas um exemplo básico de como usar a API. Você pode personalizar a API de acordo com suas necessidades.

Lembre-se de ajustar as configurações de autenticação OAuth2 de acordo com suas necessidades e considerar a adição de autenticação e autorização adequadas para proteger a API, especialmente se você estiver lidando com informações sensíveis.

## Contribuindo

Se você deseja contribuir para este projeto, sinta-se à vontade para criar um fork e enviar um pull request com suas alterações. Ficaremos felizes em revisar e mesclar suas contribuições.

Esperamos que este projeto seja útil para você como desenvolvedor iniciante e que você possa aprender com ele. Se tiver alguma dúvida ou encontrar problemas, sinta-se à vontade para abrir uma issue no repositório.

--- 

Esse README fornecerá instruções claras para os desenvolvedores iniciantes que desejam configurar e executar o seu projeto em suas máquinas locais. Certifique-se de personalizar as seções com as informações específicas do seu projeto, como os pré-requisitos e as instruções de uso da API.
