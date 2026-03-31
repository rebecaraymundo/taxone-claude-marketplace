# MTZ-Job-Servidor-Importacao_SAFX245

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX245.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 69 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX245

Tabela dos Valores Declaratórios do Sped Fiscal \(E115/1925\)

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

\- Importação 🡪 Execução

\- Importação Batch 🡪 Programação 🡪 Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS8105

Vânia Mattos 

Criação da SAFX245 para a importação dos dados dos valores declaratórios da Apuração, que originam os registros E115 e 1925 do Sped Fiscal\. 

24/03/2017

CH20937\_2018 \(MFS\-20388\)

Julyana Perrucini

Essa MFS tem como objetivo alterar a obrigatoriedade do campo “Valor da Informação Adicional”\.

23/08/2018

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX245__ 🡪 vide manual de layout

A SAFX245 foi criada na __MFS8105__, para a importação dos dados dos Valores Declaratórios da Apuração, que originam os registros E115 e 1925 do Sped Fiscal\.

Esta SAFX atende a importação de duas tabelas definitivas:

__Tabela__

__Chave__

__Menu da manutenção \(Módulo EFD\)__

__EFD\_REG\_E115__

Empresa

Estabelecimento

Data Inicial

Data Final

Sequencial

Menu “__Geração__ 🡪 Manutenção 🡪 Registro E115/1925 \(Valores Declaratórios\)” 

__EFD\_REG\_E115\_IES__

Empresa

Estabelecimento

__Inscrição Estadual__

Data Inicial

Data Final

Sequencial

Menu “__Geração \- PIM__ 🡪 Manutenção 🡪 Registro E115/1925 \(Valores Declaratórios\)”

A diferença entre as duas tabelas é apenas a inscrição estadual, que existe somente na tabela EFD\_REG\_E115\_IES, e compõe a sua chave\.

Na SAFX245 o campo da inscrição estadual é um campo de preenchimento *não obrigatório*, e a importação dos dados funciona da seguinte forma:

     \- Quando a inscrição estadual for informada, o registro será gravado na __EFD\_REG\_E115\_IES__;

     \- Quando a inscrição estadual não for informada, o registro será gravado na __EFD\_REG\_E115__;

__RN01__

__Campo Código da Empresa__

Campo de preenchimento obrigatório\.

* \(registros das tabelas SAFX sem a informação da Empresa são desconsiderados\)*

__RN02__

__Campo Código do Estabelecimento__

Campo de preenchimento obrigatório\.

*\(registros das tabelas SAFX sem a informação do Estabelecimento são desconsiderados\)*

__RN03__

__Campo Inscrição Estadual __

Campo de preenchimento __não__ obrigatório\.

Quando o campo for preenchido com @ ou brancos, considerar que a inscrição estadual *não* foi informada\.

Caso contrário, o conteúdo informado será validado no Cadastro das Inscrições Estaduais por Estabelecimento __\(\*\)__, e quando não encontrado, o registro não será importado, e será gravada a seguinte mensagem de erro no log: “*Inscrição Estadual – AM não cadastrada na Tabela das Inscrições Estaduais do AM \(consultar o Manual de Layout\)*”\.

__\(\*\)__ *Módulo PIM, menu “Cadastro > Inscrição Estadual por Estabelecimento”, ou Módulo Parâmetros, menu “Funcionais > Inscrições Estaduais do Estabelecimento \(AM\); *

__RN04__

__Campo Data Inicial do Período__

Campo de preenchimento obrigatório\.

Deve ser uma data válida\.

Quando não preenchido, ou quando for uma data inválida, o registro não será importado, e no log de erros será gravada a seguinte mensagem: *“Data Inicial do Período não preenchida ou inválida”\.*

__RN05__

__Campo Data Final do Período__

Campo de preenchimento obrigatório\.

Deve ser uma data válida e superior à data inicial informada\.

Quando não preenchido, quando for uma data inválida, ou quando <= à Data Inicial, o registro não será importado, e no log de erros será gravada a seguinte mensagem: *“Data Final do Período não preenchida ou inválida”\.*

__RN06__

__Campo Sequencial __

Campo de preenchimento obrigatório\.

Quando não preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem: *“O Sequencial deve ser preenchido”\.*

__RN07__

__Campo Código da Informação Adicional __

Campo de preenchimento obrigatório\.

Validação do código informado:

     \- As duas primeiras posições devem ser = sigla da UF do estabelecimento informado no campo 02\-Estabelecimento;

     \- O código informado deve existir na Tabela de Códigos das Informações Adicionais da Apuração \(módulo Sped Fiscal, menu

       “Parâmetros > Informações Adicionais da Apuração \(Registro E115/1925\)”\)\. Esta tabela de códigos é por UF, cada estado tem

       seus códigos próprios, e a identificação da UF é feita pelas duas primeiras posições do código\.

Quando não preenchido, ou não atender aos requisitos acima, o registro não será importado, e no log de erros será gravada a seguinte mensagem: *“Código da Informação Adicional não informado ou inválido\. Consultar o manual de layout da SAFX245”\.*

__RN08__

__Campo Valor da Informação Adicional __

__\[ALTERADA – CH20937\_2018 \(MFS\-20388\)\]__

Campo de preenchimento não obrigatório\.

Deve ser um valor maior que zero\.

Quando não preenchido ou inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem: *“O Valor da Informação Adicional deve ser informado \(e diferente de zero\)”\.*

CH20937\_2018 \(MFS\-20388\)

__RN09__

__Campo Descrição Complementar __

Campo de preenchimento __não__ obrigatório\.

__RN10__

__Campo Sub\-Apuração do Sped Fiscal __

Campo de preenchimento __não__ obrigatório\.

Quando o campo for preenchido, deve ter um dos seguintes valores: '1', '2', '3', '4', '5', ou '6'\. Caso contrário, o registro não será importado, e no log de erros será gravada a seguinte mensagem: *“Sub\-Apuração do Sped Fiscal inválida\. Os valores válidos são: 1, 2, 3, 4, 5, ou 6”\.*

