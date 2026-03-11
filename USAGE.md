# Guia de Uso do Bot Eureka SAS

## Instalação

1. **Clone o repositório:**  
   Abra seu terminal e clone o repositório utilizando o comando:  
   ```bash  
   git clone https://github.com/eurekasas10/eureka-sas-bot.git  
   ```  

2. **Instale as dependências:**  
   Navegue até o diretório do projeto e execute:  
   ```bash  
   npm install  
   ```  

## Configuração

Para configurar o bot, crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis de ambiente:  

```plaintext
TOKEN=seu_token_aqui
OUTRO_PARAM=valor
```

## Configurações de Intervalo

O bot permite que você configure intervalos para as operações. Para definir o intervalo, edite a seção correspondente no seu arquivo de configuração (geralmente `config.js`):  

```javascript
const interval = {
    min: 5,  // mínimo em minutos
    max: 60  // máximo em minutos
};
```

## Exemplos

### Exemplo 1: Enviar uma Mensagem

Você pode enviar uma mensagem para um canal específico com o seguinte comando:  

```javascript
bot.sendMessage(channelId, 'Olá, mundo!');
```

### Exemplo 2: Atribuir Tarefas

Para atribuir uma tarefa a um usuário, use:  

```javascript
bot.assignTask(userId, taskDetails);
```

## Conclusão

Certifique-se de revisar toda a documentação do código e dos exemplos para aproveitar ao máximo o bot.  
Essa é uma visão geral para ajudar no uso do bot Eureka SAS. Se precisar de mais ajuda, consulte a documentação ou entre em contato com o suporte.