# MTZ_REINF_Regra_Geracao_Calculo_CPRB

- **Fonte:** MTZ_REINF_Regra_Geracao_Calculo_CPRB.docx
- **Modificado:** 2025-07-16
- **Tamanho:** 68 KB

---

THOMSON REUTERS

EFD \- REINF

Regra de geração SAFX185

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-7718

Elenilson Coutinho

Regra de recuperação das informações para carregar a SAFX185

MFS\-7561

Elenilson Coutinho

Inclusão das informações de serviços para cálculo

MFS\-8485

Elenilson Coutinho

Regra para cálculo dos ajustes

MFS14998

Lara Aline

Ajuste no campo VLR\_REC\_BRT, recuperando da tela Receita Bruta do Estabelecimento\.

MFS16427

Lara Aline

Ajuste no campo VLR\_REC\_BRT\_ATIV\.

MFS16610

Lara Aline

Ajuste no campo VLR\_REC\_BRT\_DEMAIS\_ATIV

MFS21178

Lara Aline

Ajuste no campo VLR\_CONT\_PREV

MFS23185

Vânia Mattos

Alteração na geração do campo VLR\_REC\_BRT\_ATIV para utilizar a nova parametrização por Natureza de Operação \(ver RN0010\)

MFS639116

Rogério Ohashi

Alteração na geração do campo COD\_CONTA para recuperar a informação do item da Nota Fiscal \(SAFX08 ou SAFX09\) \- ver RN0007

MFS\-797217

Bruna Ribeiro

Inclusão de parâmetro para escolha da data base para geração do evento R\-2060\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN0000

Rotina “Geração do Cálculo \- CPRB” irá carregar a SAFX185\. Haverá um indicador na x185\_contrib\_prev onde este será carregado com “1” para geração ou “0” importação SAFX\.

MFS7718

RN0002

Campo COD\_ESTAB

Gerar com a informação do estabelecimento carregado na tela “Geração do Cálculo \- CPRB”\.

MFS7718

RN0003

Campo DATA\_INI

Gerar com a informação da data inicial carregada na tela “Geração do Cálculo \- CPRB”\.

MFS7718

RN0004

Campo DATA\_FIM

Gerar com a informação da data final carregada na tela “Geração do Cálculo \- CPRB”\.

MFS7718

RN0005

Campo COD\_ATIV\_CONT\_PREV

Gerar com a informação do código de atividade parametrizado na tela de “Código de Atividade X NCM” e/ou “Código de Atividade X Serviços”

MFS7718

MFS7561

RN0006

Campo COD\_RECEITA

Gerar com a informação do código da receita parametrizado na tela de “Código de Atividade X NCM” e/ou “Código de Atividade X Serviços”

MFS7718

MFS7561

RN0007

Campo COD\_CONTA

\[__ALTERADO\-MFS639116__\] Tratamento para recuperar a conta contábil do Item da Nota Fiscal

A Conta Contábil deverá ser recuperada do Campo de COD\_CONTA das notas de saída da SAFX08 ou SAFX09, por se tratar de um registo totalizador, recuperar a primeira conta utilizando o critério de Código de Atividade e Código de Receita, sendo:

__SAFX08:__ Recuperar a informação da conta contábil, conforme código de atividade e código da receita parametrizado na tela de “Código de Atividade X NCM”;

__SAFX09:__ Recuperar a informação da conta contábil, conforme código de atividade e código da receita parametrizado na tela de “Código de Atividade X Serviços”\.

MFS7718

MFS639116

RN0008

Campo COD\_CUSTO

MFS7718

RN0009

Campo VLR\_REC\_BRT 

__\[MFS14998\]__

Gerar com o valor informado no campo ‘Valor Receita Bruta – Total’ do menu  Cálculo da CPRB , tela “Receita Bruta do Estabelecimento” \. Esse valor será gerado para todos os códigos de atividades gerados nesse processo de cálculo na SAFX185\.

Gerar com a informação do Valor da Receita Total Bruta do estabelecimento no período\. Valores serão recuperados a partir da somatória dos campos VLR\_CONTAB\_ITEM das notas de saída SAFX08 e VLR\_TOT das notas de saída SAFX09, considerando as parametrizações por “CFOP´s” tela \(Identificador das Receitas \(Por CFOP\)\) e “Serviços” tela \(Código de Atividade x Serviços\)\.

Caso não informado valor em tela apresentar a mensagem no log:

Valor Receita Bruta – Total não informado\. Campo Obrigatório\.

Cálculo da CPRB > Receita Bruta do Estabelecimento

MFS7718

MFS14998

RN0010

Campo VLR\_REC\_BRT\_ATIV

Gerar com a informação do Valor da Receita Bruta por Atividade do estabelecimento no período\. 

__Produtos:__

Valores serão recuperados a partir da somatória do campo VLR\_CONTAB\_ITEM das notas de saída SAFX08, considerando as 

parametrizações por NCM tela \(Código de Atividade X NCM\) e parametrização dos Identificadores de Receita \(Por CFOP e Por CFOP/Natureza\)\.

Alteração __MFS23185__: Além de utilizar a parametrização dos identificadores de receita por CFOP, a geração deste campo passou a usar também a nova parametrização por Natureza de Operação \(menu “Parâmetros > CPRB > Apuração da CPRB > Identificador das Receitas \- Por CFOP/Natureza de Operação”\); 

__Serviços:__

Valores serão recuperados a partir da somatória do campo e VLR\_TOT das notas de saída SAFX09, considerando a parametrização por “Serviços” tela \(Código de Atividade x Serviços\)\.

MFS7718

MFS16427

__MFS23185__

RN0011

Campo VLR\_EXC\_REC\_BRT

Caso não houver valor preencher com “0”\.

MFS\-8485

RN0012

Campo VLR\_ALIQ\_CONT\_PREV

Gerar com o valor da Alíquota vinculada ao código de atividade da TACES75, considerando o código de atividade parametrizado na tela de “Código de Atividade X NCM” e/ou “Código de Atividade X Serviços”\.

MFS7718

\*VALORES EFD – CONTRIBUIÇÕES

RN0013

Campo VLR\_REC\_BRT\_DEMAIS\_ATIV

\[Alteração MFS16610\]

Gerar com o valor do seguinte cálculo: ‘Valor Receita Bruta – Total’ \(\-\) Somatório do ‘Valor Receita Bruta – Atividade’ de todas as atividades do estabelecimento\.

MFS7718

MFS16610

RN0014

Campo VLR\_BASE\_CONT\_PREV

Gerar com o valor do seguinte cálculo VLR\_REC\_BRT\_ATIV \(\-\) Campo VLR\_EXC\_REC\_BRT\. 

MFS\-8485

RN0015

Campo VLR\_CONT\_PREV

Gerar com o valor do seguinte cálculo: VLR\_BASE\_CONT\_PREV \(\*\) VLR\_ALIQ\_CONT\_PREV\. 

\[MFS21178\]

O valor deve ser truncado na segunda casa decimal\.

MFS7718

MFS7561

MFS21178

\*VALORES EFD – REINF

RN0016

Campo Valor Ajuste Adição

 Caso não houver valor preencher com “0”\.

MFS8485

RN0017

Campo Valor Ajuste Exclusão 

 Caso não houver valor preencher com “0”\.

MFS8485

RN0018

Campo Valor Base de Cálculo – Contrib\. Prev\. sobre Receita Bruta

Gerar com o valor do seguinte cálculo VLR\_REC\_BRT\_ATIV \(\-\) Valor Ajuste Exclusão \(\+\) Valor Ajuste Adição\.

MFS8485

RN0019

Campo Valor Contrib\. Prev\. sobre Receita Bruta:

Gerar com o valor do seguinte cálculo: Valor Base de Cálculo – Contrib\. Prev\. sobre Receita Bruta \(\*\) VLR\_ALIQ\_CONT\_PREV\.

MFS8485

RN0020

Campo DSC\_COMPLEMENTAR

MFS7718

RN0021

Campo COD\_SCP

MFS7718

RN0022

Data base para a geração do registro\.

Menu: SPED > EFD \- Reinf > Cálculo da CPRB > Geração do Cálculo\.

Este parâmetro definirá a data base para a geração do registro\. Deverão ser listadas as seguintes opções: 

1 – Data emissão: Utiliza a data de emissão do documento fiscal, proveniente do campo 11 \(Data de Emissão\) da tabela SAFX07\.

2 – Data de Pagamento da Nota Fiscal: Utiliza a data de pagamento da nota fiscal, proveniente do campo 175 \(Data de Pagamento\) da tabela SAFX07\.

Tipo: Checkbox\.

Default marcado: Data de emissão\.

Criado esse parâmetro para definição da data de seleção da geração dos registros R\-2060 \(CPRB\)\.

MFS\- 797217

S

Default: Data de Emissão

Este parâmetro definirá a data base para a geração do registro\. Deverão ser listadas as seguintes opções: 

1 – Data emissão: Utiliza a data de emissão do documento fiscal, proveniente do campo 11 \(Data de Emissão\) da tabela SAFX07\.

2 – Data de Pagamento da Nota Fiscal: Utiliza a data de pagamento da nota fiscal, proveniente do campo 175 \(Data de Pagamento\) da tabela SAFX07\.

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

