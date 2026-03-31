# MTZ-Importacao_SAFX149

- **Fonte:** MTZ-Importacao_SAFX149.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 39 KB

---

    

# Módulo Job Servidor – Importação – Operações da Atividade Imobiliária – Unidade Imobiliária Vendida \(SAFX149\)

*\(Obs: As regras descritas neste documento são numeradas de acordo com os campos da SAFX149, conforme o Manual de Layout, o que facilita a consulta\)*

*\(Qualquer regra que não diga respeito a campos específicos, deve ser incluída na regra numerada como RN00\)*

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3169\-DW4

Criação da SAFX149

Será criada uma tabela para atendimento do Bloco F200 do Anexo Único do Ato Declaratório Executivo COFINS Nº 31, de 08 de julho de 2010

08/12/2010

OS3169\-DW23

Alteração no tamanho de campo

Alterado o tamanho do campo “Código da unidade imobiliária”

18/11/2011

OS4316

Criação de Campos

Criação dos campos Código e Descrição da SCP

30/12/2013

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

__Regras gerais__

As rotinas de Carga, Importação, Importação Batch e Exportação do módulo Job Servidor deverão ser alterados para contemplar os campos descritos abaixo na tabela SAFX149\.

OS3169\-DW4

__RN01__

__Campo 01 \- Código da empresa__

 

__Item: __01

__Nome do Campo: __COD\_EMPRESA

__Descrição: __Código da empresa

__Tipo:__ A

__Tamanho: __003

__Comentário: __Campo destinado ao código da Empresa\.

__Chave Primária__

__Obrigatório__

OS3169\-DW4

__RN02__

__Campo 02 \- Código do estabelecimento__

__Item: __02

__Nome do Campo: __COD\_ESTAB

__Descrição: __Código do estabelecimento

__Tipo:__ A

__Tamanho: __006

__Comentário: __Campo destinado ao código do Estabelecimento\.

__Chave Primária__

__Obrigatório__

OS3169\-DW4

__RN03__

__Campo 03 \- Código da unidade imobiliária__

__Item: 03__

__Nome do Campo: __Será definido pelo A&D

__Descrição:__ Código da unidade imobiliária

__Tipo__: A

\[Alterado – OS3169\-DW23\]

__Tamanho:__ 009

__Tamanho__: 011

C__omentário__:

Deverá ser preenchido com o conteúdo do cadastro do Código da Unidade Imobiliária no módulo: Básicos/Mastersaf DW/Manutenção/Códigos\. O código da Unidade Imobiliária foi criado para relacionar a venda da unidade imobiliária com os custos 

ocorridos ou orçados\.

__Chave Primária__

__Obrigatório__

OS3169\-DW4 / OS3169\-DW23

__RN04__

__Campo 04 \- Data da Operação da venda da unidade imobiliária __

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Data da Operação da venda da unidade imobiliária

__Tipo:__ N

__Tamanho: __008

__Comentário: __

Data da operação de venda da unidade imobiliária no formato DDMMAAAA

__Chave Primária__

OS3169\-DW4

__RN05__

__Campo 05 \- Indicador do Tipo da Operação__

__Item: __05

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Indicador do Tipo da Operação

__Tipo:__ N

__Tamanho: __002

__Comentário: __

Indicador do Tipo da Operação de acordo com o Manual do leiaute da EFD\-PIS/COFINS:  
 01 – Venda a Vista de Unidade Concluída;  
 02 – Venda a Prazo de Unidade Concluída;  
 03 – Venda a Vista de Unidade em Construção;  
 04 – Venda a Prazo de Unidade em Construção;  
 05 – Outras\.

__Obrigatório__

OS3169\-DW4

__RN06__

__Campo 06 – Número de Contrato/Documento__

__Item: __06

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Número de Contrato

__Tipo:__ A

__Tamanho: __090

__Comentário:__

__ __Número de Contrato/documento que formaliza a venda da unidade imobiliária vendida

__Não Obrigatório__

OS3169\-DW4

__RN07__

__Campo 07 – Indicador da Pessoa Fis/Jur Adquirente__

__Item: __07

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Indicador da pessoa física \(CPF\) ou da pessoa jurídica \(CNPJ\) previamente cadastrada na SAFX04, adquirente da unidade imobiliária\.

__Tipo:__ A

__Tamanho: __001

__Comentário: __

Informar o indicador da pessoa fis/jur cadastrada na SAFX04, adquirente da unidade imobiliária

__Obrigatório__

__RN08__

__Campo 08 – Código da Pessoa Fis/Jur Adquirente__

__Item: __08

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Código da pessoa física \(CPF\) ou da pessoa jurídica \(CNPJ\) previamente cadastrada na SAFX04, adquirente da unidade imobiliária\.

__Tipo:__ A

__Tamanho: __014

__Comentário: __

Código da pessoa física \(CPF\) ou da pessoa jurídica \(CNPJ\) adquirente da unidade imobiliária\.

__Obrigatório__

OS3169\-DW4

__RN09__

__Campo 09 – Informações Complementares__

__Item: __09

__Nome do Campo: __Será definido pelo A&D

__Descrição: __Informações Complementares da unidade imobiliária vendida

__Tipo:__ A

__Tamanho: __090

__Comentário: __

Informações Complementares da unidade imobiliária vendida\.

__Não Obrigatório__

OS3169\-DW4

__RN10__

__Campo Código da SCP__

Alterar a rotina de importação para que seja considerado o novo campo:

Tabela: SAFX149

Item: A ser reservado pelo A&D

Nome do Campo: Código da SCP

Tipo: A

Tamanho: 014

Comentário: Código da Sociedade em Conta de Participação

Deverá existir um cadastro correspondente na SAFX2057 para o código informado\. Caso não exista, retornar a mensagem: “Cadastro da SCP não encontrado”\.

__OS4316__

