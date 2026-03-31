# MTZ_ESTORNO_DE_DEBITOS_Geracao_Recibo_de_Entrega_Ato_Cot24

- **Fonte:** MTZ_ESTORNO_DE_DEBITOS_Geracao_Recibo_de_Entrega_Ato_Cot24.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 68 KB

---

THOMSON REUTERS

Estorno de Débitos – Modelo 21/22

Geração dos Documentos Fiscais de Estorno de Débitos para Empresas Prestadoras de Serviços de Comunicação e Telecomunicação

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

OS2890

Marcos Roberto de Oliveira

Este documento de requisito tem por objetivo permitir a criação de novos campos na tabela SAFX42, além de criar o novo módulo intitulado “Portaria CAT 06/09” para geração do arquivo eletrônico contendo o estorno do valor do imposto indevidamente debitado em Notas Fiscais de Serviço de Comunicações \(modelo 21\) ou Telecomunicações \(modelo 22\), emitidas a partir de maio de 2004\.

MFS1676

Julyana Perrucini

Revisão do documento, separado do arquivo de geração do arquivo magnético\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN00

__Anexo II – Recibo de Entrega__

__\[ALTERADA – MFS1676\]__

Este anexo pertence ao Ato Cotepe 24/2010 e os campos deverão ser preenchidos de acordo com as RN do documento: 

__MTZ\_ESTORNO\_DE\_DEBITOS\_Geracao\_Arquivo\_Magnetico\.docx\.__

Ao selecionar a opção do parâmetro Base Legal: “Ato COTEPE 24/2010”, na tela de Meio Magnético >> Geração, deverá emitir o relatório Recibo de Entrega no padrão Framework\.

__Cabeçalho__: Preencher com o conteúdo a seguir\. Verificar o layout do Recibo de Entrega no item 2\.2\.3\.2 do documento de requisito da OS2890\.

Anexo II

 

Recibo de Entrega

 

 

Governo do Estado de __XXXXXX__

 

Secretaria da Fazenda

 

Recibo de Entrega de Arquivo – Convênio ICMS 126/98 – Ato Cotepe 24/2010

\- __XXXXXX__: O conteúdo que complementa o “Governo do Estado de” deve ser recuperado através do campo DESCRIÇÃO da tabela ESTADO\. 

OS2890

MFS1676

1. __EMPRESA PRESTADORA DE SERVIÇO DE TELECOMUNICAÇÃO__

RN01

__Razão Social__

Recuperar o campo conforme __RNR1\-04\.__

OS2890

MFS1676

RN02

__IE __

Recuperar o campo conforme __RNR1\-05\.__

OS2890

MFS1676

RN03

__CNPJ__

Recuperar o campo conforme __RNR1\-06\.__

OS2890

MFS1676

1. __DADOS DO ARQUIVO__

RN04

__Nome do Arquivo__

Essa informação deve ser recuperada da Aba Arquivos: 

Conforme documento MTZ\_ESTORNO\_DE\_DEBITOS\_Tela\_Geracao\_Arquivo\_Magnetico\.docx\.

OS2890

MFS1676

RN05

__Código de Autenticação Digital do arquivo__

Espaço em branco\. Fora do escopo\.

OS2890

RN06

__Somatório do Valor Total dos Serviços__

Efetuar o somatório do campo 17 “Valor Total dos Itens” de acordo com a regra __RNR2\-17\.A__\.

OS2890

MFS1676

RN07

__Somatório do Valor da Base de Cálculo do ICMS dos Serviços__

Efetuar o somatório do campo 18 “Base de Cálculo do ICMS” de acordo com a regra __RNR2\-18\.A__\.

OS2890

MFS1676

RN08

__Somatório do Valor do ICMS dos Serviços__

Efetuar o somatório do campo 19 “ICMS dos itens” de acordo com a regra __RNR2\-19\.A__\.

OS2890

MFS1676

RN09

__Somatório do Valor do ICMS Recuperado ou a Recuperar__

Efetuar o somatório do campo 20 “ICMS a Recuperar ou Recuperado” de acordo com a regra __RNR2\-20\.A__\.

OS2890

MFS1676

RN10

__Nome do Responsável pelas Informações__

Recuperar o campo conforme __RNR1\-10\.__

OS2890

MFS1676

RN11

__Cargo__

Recuperar o campo conforme __RNR1\-11\.__

OS2890

MFS1676

RN12

__Assinatura__

Espaço em branco para o responsável assinar\.

OS2890

RN13

__Telefone__

Recuperar o campo conforme__ RNR1\-12\.__

OS2890

MFS1676

RN14

__E\-mail__

Recuperar o campo conforme __RNR1\-13\.__

OS2890

MFS1676

RN15

__Data__

Informar a data de geração do relatório no formato DD/MM/AAAA\.

OS2890

1. __RECEBIMENTO__

RN16

__Local e Data__

Espaço em branco para o responsável escrever\.

OS2890

RN17

__Assinatura e Carimbo__

Espaço em branco para o responsável assinar\.

OS2890

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

