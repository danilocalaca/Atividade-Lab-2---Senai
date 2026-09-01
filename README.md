# Atividade Lab 2

## 📚 Descrição

Este projeto foi desenvolvido como atividade prática do Lab 2, com o objetivo de aplicar conceitos de manutenção de software, documentação técnica e utilização de Inteligência Artificial como ferramenta de apoio.

O estudo de caso apresenta um sistema de autenticação de um e-commerce que possuía uma falha crítica de segurança no armazenamento das senhas.

## ⚠️ Problema Identificado

O sistema armazenava as senhas em texto puro diretamente no código, permitindo que elas fossem visualizadas por qualquer pessoa que tivesse acesso ao arquivo.

Além disso, não existiam registros das tentativas de login.

## 🛠️ Correção Realizada

O problema foi corrigido substituindo as senhas em texto puro por hashes, evitando que as senhas ficassem expostas diretamente no sistema.

Também foram adicionados logs para registrar as tentativas de autenticação, incluindo acessos bem-sucedidos e tentativas com falha.

Foram realizados testes com senhas corretas, incorretas e usuários inexistentes para verificar o funcionamento da autenticação.

## 🤖 Uso da Inteligência Artificial

A Inteligência Artificial foi utilizada como ferramenta de apoio para:

- Análise do código;
- Identificação das vulnerabilidades;
- Elaboração do plano de manutenção;
- Sugestão de melhorias de segurança;
- Auxílio na documentação técnica.

## 📁 Arquivos

- `autenticacao.py` - Código original com a vulnerabilidade.
- `autenticacao_corrigido.py` - Código após a correção.
- `README.md` - Documentação do projeto.

## 🎯 Objetivo

Demonstrar a aplicação de procedimentos de manutenção de software e boas práticas de segurança utilizando a Inteligência Artificial como apoio durante o processo.

## 👨‍💻 Autor

Atividade acadêmica - Lab 2
