# MTZ_ICMS_Lanctos_Complementares_Copiar_Lançamentos_ICMS-ST

- **Fonte:** MTZ_ICMS_Lanctos_Complementares_Copiar_Lançamentos_ICMS-ST.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 66 KB

---

THOMSON REUTERS

Módulo ICMS

__Menu: Apuração >> Apuração do ICMS >> Lançamentos Complementares ICMS\-ST__

__Botão > Copiar Lançamentos__

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS1943

Criação do documento

Cópia das parametrizações já efetuadas nos Lançamentos Complementares para apuração e livro corrente\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN00

RN01

__Processamento dos Dados__

Origem dos dados da aba __Lançamentos de Valores__ dos Lançamentos Complementares:

\- Módulo ICMS > menu “Apuração > Apuração do ICMS > Lançamentos Complementares > Apuração ICMS Subst\. Tributária > Ajuste SINIEF > __Aba Lançamentos de Valores__”, campos 🡪 “Data Apuração, Operação Apuração, Descrição, UF, Classe Lançamento, Amparo/Texto/Ocorrencia, Subitem Amp\./Texto/Ocor\. e Código de Ajuste \(Sped Fiscal – Reg E11/E220\)\.”

\- Tabela Item Apuração Substituição Tributária \(ITEM\_APURAC\_SUBST\) para o Tipo de Livro = ‘165’ \- Apuração por Inscrição Estadual Única \(COD\_TIPO\_LIVRO = ‘165’\)

__O processamento é por Estabelecimento\.__

MFS1943

RN02

__Critérios para a recuperação dos Lançamentos:__

__Para cada Estabelecimento e Período selecionado em tela__:

 

__Passo 1__: Recuperação dos parâmetros da aba Lançamentos de Valores:

Serão recuperados os dados da parametrização \(ITEM\_APURAC\_SUBST\) do estabelecimento: DAT\_APURACAO, COD\_OPER\_APUR, DSC\_ITEM\_APURACAO, IDENT\_ESTADO, COD\_CLASSE, COD\_AMPARO\_LEGAL, COD\_SUB\_ITEM\_OCORR, COD\_AJUSTE\_ICMS considerando os seguintes critérios:

    COD\_EMPRESA 🡪 código da Empresa do login 

    COD\_ESTAB 🡪 código do estabelecimento selecionado 

    DAT\_APURACAO 🡪 de acordo com o mês/ano informado em tela

Caso todos os campos sejam iguais deverá ser consolidado e apresentado apenas um lançamento para seleção\.

__Passo 2__: Gravar na tabela Item de Apuração \(ITEM\_APURAC\_SUBST\) e efetuar um novo lançamento a cada registro de lançamento selecionado em tela, com os seguintes dados:

__CAMPO__

__CONTEÚDO__

__OBSERVAÇÃO__

COD\_EMPRESA

Empresa do login

COD\_ESTAB

Estabelecimento selecionado em tela\.

DAT\_APURACAO

Campo DAT\_APURACAO da parametrização dos Lançamentos de Valores

Lançamento Complementar

COD\_OPER\_APUR

Campo COD\_OPER\_APUR da parametrização dos Lançamentos de Valores

DSC\_ITEM\_APURACAO

Campo DSC\_ITEM\_APURACAO da parametrização dos Lançamentos de Valores

IDENT\_ESTADO

Campo IDENT\_ESTADO da parametrização dos Lançamentos de Valores

COD\_CLASSE

Campo COD\_CLASSE da parametrização dos Lançamentos de Valores

COD\_AMPARO\_LEGAL

Campo COD\_AMPARO\_LEGAL da parametrização dos Lançamentos de Valores

COD\_SUB\_ITEM\_OCORR

Campo COD\_SUB\_ITEM\_OCORR da parametrização dos Lançamentos de Valores

COD\_AJUSTE\_ICMS

Campo COD\_AJUSTE\_ICMS da parametrização dos Lançamentos de Valores

MFS1943

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

