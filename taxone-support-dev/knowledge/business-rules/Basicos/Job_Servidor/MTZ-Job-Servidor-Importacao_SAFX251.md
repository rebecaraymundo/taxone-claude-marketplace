# MTZ-Job-Servidor-Importacao_SAFX251

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX251.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 67 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX251

Tabela das Contribuições Sindicais do Período

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS14409

Criação da SAFX251 

Criação da SAFX249 para a importação dos dados das contribuições sindicais do período, informações utilizadas na geração do evento S\-1300 do eSocial\. 

23/11/2017

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX251__ 🡪 vide manual de layout

A SAFX251 foi criada na __MFS14409__, para a importação dos dados das contribuições sindicais do período\. Estas informações são utilizadas na geração do evento S\-1300 do eSocial\.

__Campos que compõe a chave da tabela \(PK\):__

   Código da Empresa \+ Código do Estabelecimento \+ Ano Referência \+ Mês Referência \+ Código do Sindicato \+ Tipo da Contribuição 

__RN01__

__Campo Código da Empresa__

Campo de preenchimento obrigatório\.

* \(registros das tabelas SAFX sem a informação da Empresa são desconsiderados\)*

__RN02__

__Campo Código do Estabelecimento__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento são desconsiderados\)*

__RN03__

__Campo Ano Referência __

Campo de preenchimento obrigatório\.

Quando não preenchido ou inválido \(= zeros\), será gravada mensagem de erro padrão e o registro não será importado\.

__RN04__

__Campo Mês Referência__

Campo de preenchimento obrigatório\.

Deve ser um mês válido\.

Quando não preenchido ou inválido, será gravada mensagem de erro padrão e o registro não será importado\.

__RN05__

__Campo Código do Sindicato__

Campo de preenchimento obrigatório\.

O código informado deve ser um código existente na Tabela de Cadastro dos Sindicatos \(SAFX2048\)\.

Para pesquisar os códigos na SAFX2048, considerar:

\-Grupo – Grupo obtido conforme regra padrão __\(\*\*\*\)__;

\-Código do Sindicato – código informado neste campo \(campo 05\);

\-Validade Inicial – maior data existente, cujo mês/ano seja <= ao mês/ano de referência informados \(campos 03 e 04\)

__*\(\*\*\*\)*__* O *__*Grupo*__* a ser utilizado será obtido a partir da regra básica, considerando o Grupo \(Relacionamento Tabelas x Grupos\) de maior data de validade, cujo mês/ano seja <= ao mês/ano de referência informado, e para o qual a tabela SAFX2048 esteja associada\.*

Quando o campo não for preenchido, ou o código não existir na SAFX2048, será gravada mensagem de erro padrão e o registro não será importado\.

__RN06__

__Campo Tipo da Contribuição__

Campo de preenchimento obrigatório\.

Valores válidos: “1” \(Contribuição Sindical Compulsória\)

                           “2” \(Contribuição Associativa\)

                           “3” \(Contribuição Assistencial\)

                           “4” \(Contribuição Confederativa\)

Quando não preenchido ou inválido, será gravada mensagem de erro padrão e o registro não será importado\.

__RN07__

__Campo Valor da Contribuição __

Campo de preenchimento obrigatório\.

Deve ser > zero\.

Quando não preenchido ou inválido \(= zeros\), será gravada mensagem de erro padrão e o registro não será importado\.

