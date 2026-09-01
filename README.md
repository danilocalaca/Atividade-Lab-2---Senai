# Lab 2
## 📚 Descrição

Este projeto foi desenvolvido como atividade prática do Lab 2, com o objetivo de aplicar conceitos de manutenção de software, documentação técnica e utilização de Inteligência Artificial como ferramenta de apoio.

O estudo de caso apresenta um sistema de autenticação de um e-commerce que possuía uma falha crítica de segurança no armazenamento das senhas.

---

## 🤖 Prompt utilizado na IA

Foi utilizado o seguinte prompt para auxiliar na análise e documentação da manutenção:

> Atue como um Engenheiro de Software responsável pela manutenção e segurança de sistemas.
>
> Analise o código Python fornecido e elabore um Plano de Manutenção de Emergência contendo:
>
> 1. Tipo de manutenção necessária (corretiva, preventiva, adaptativa ou perfectiva) e sua justificativa;
> 2. Diagnóstico dos problemas e vulnerabilidades encontrados;
> 3. Avaliação dos impactos da falha;
> 4. Procedimento passo a passo para correção;
> 5. Estratégia de rollback caso a correção apresente problemas;
> 6. Plano de testes para validar a solução;
> 7. Sugestão de refatoração do código utilizando boas práticas de segurança, incluindo armazenamento de senhas com hash;
> 8. Recomendações de manutenção preventiva para evitar que o problema volte a ocorrer.
>
> Apresente o resultado de forma clara, técnica e organizada.

---

## 🛠️ Plano de Manutenção Gerado

### 1. Tipo de Manutenção

A manutenção necessária é principalmente **corretiva**, pois existe uma falha de segurança no módulo de autenticação que precisa ser corrigida imediatamente.

Também possui caráter **preventivo**, pois as melhorias implementadas ajudam a evitar problemas semelhantes no futuro.

### 2. Diagnóstico

Foram identificados os seguintes problemas:

- Senhas armazenadas em texto puro.
- Senhas fracas e previsíveis.
- Ausência de logs das tentativas de login.
- Credenciais diretamente no código.
- Falta de mecanismos de proteção contra tentativas de acesso indevidas.

### 3. Impactos

A falha poderia permitir que pessoas não autorizadas obtivessem acesso ao sistema de retaguarda do e-commerce.

Isso poderia resultar em:

- Acesso indevido a informações;
- Alteração de dados;
- Manipulação de pedidos e produtos;
- Comprometimento de informações de clientes;
- Prejuízos financeiros e à reputação da empresa.

A prioridade da correção foi considerada **crítica**.

### 4. Procedimento de Correção

O procedimento definido foi:

1. Realizar backup da versão original.
2. Criar uma versão corrigida do módulo.
3. Substituir o armazenamento de senhas em texto puro por hashes.
4. Implementar logs das tentativas de autenticação.
5. Realizar testes com diferentes situações de login.
6. Validar o funcionamento da nova versão.
7. Fazer a implantação da correção.
8. Monitorar o sistema após a alteração.

### 5. Plano de Testes

Foram definidos testes para:

- Login com usuário e senha corretos.
- Login com senha incorreta.
- Login com usuário inexistente.
- Tentativa de login com dados vazios.
- Registro das tentativas de autenticação.

O resultado esperado é que somente usuários com credenciais válidas consigam acessar o sistema.

### 6. Rollback

Caso a correção apresente problemas, a estratégia definida é restaurar a versão anterior utilizando o backup realizado antes da alteração.

Após isso, o problema deve ser analisado, corrigido e testado novamente antes de uma nova implantação.

### 7. Manutenção Preventiva

Como medidas preventivas, recomenda-se:

- Não armazenar senhas em texto puro.
- Utilizar métodos seguros de armazenamento de senhas.
- Evitar credenciais diretamente no código.
- Utilizar variáveis de ambiente ou gerenciadores de segredos.
- Manter registros de autenticação.
- Realizar testes automatizados.
- Fazer revisões periódicas de segurança.
- Manter bibliotecas e dependências atualizadas.

---

## 🔧 Correção Realizada no Código

A falha foi corrigida substituindo as senhas em texto puro por hashes, evitando que as senhas ficassem expostas diretamente no sistema.

Também foram adicionados logs para registrar as tentativas de autenticação, incluindo acessos bem-sucedidos e tentativas com falha.

Foram realizados testes com senhas corretas, incorretas e usuários inexistentes para verificar o funcionamento da autenticação.

---

## 📁 Estrutura do Projeto

```text
├── autenticacao.py
├── autenticacao_corrigido.py
└── README.md
