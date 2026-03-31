# MTZ_DAC_AL_Geracao_das_Obrigacoes_Fiscais_Apuradas

- **Fonte:** MTZ_DAC_AL_Geracao_das_Obrigacoes_Fiscais_Apuradas.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 70 KB

---

THOMSON REUTERS

Módulo DAC \- AL

Geração das Obrigações Fiscais Apuradas

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS2332

Criação do documento

Geração Automática dos valores da Aba GUIA dos Lançamentos Complementares para geração do Registro Tipo 41 – Obrigações Fiscais Apuradas 

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN00

RN01

Caso o parâmetro Efetuar Limpeza dos Registros Digitados na Manutenção estiver selecionado deverá ser excluídos os lançamentos efetuados na manutenção do Registro Tipo 41  \(EST\_AL\_REG\_41\) menu: DAC\-AL > Manutenção > Obrigações Fiscais Apuradas antes da rotina de geração conforme é descrita na RN02\.

MFS2332

RN02

Origem dos dados da GUIA dos Lançamentos Complementares:

\- Módulo ICMS > menu “Apuração > Apuração do ICMS > Lançamentos Complementares > Apuração ICMS > Ajuste SINIEF > __Aba Guia__”, campos 🡪 “Mês e Ano Referencia, Data de Vencimento, Valor Recolhimento e Receita Estadual”

\- Tabela Guia de Recolhimento \(GUIA\_RECOLHIMENTO\) para o Tipo de Livro = ‘108’ \- Apuração Normal \(COD\_TIPO\_LIVRO = ‘108’\) 

\- Módulo ICMS > menu “Apuração > Apuração do ICMS > Lançamentos Complementares > Apuração ICMS Subst\. Tributária > Ajuste SINIEF > __Aba Guia__”, campos 🡪 “Mês e Ano Referencia, Data de Vencimento, Valor Recolhimento e Receita Estadual”

\- Tabela Guia de Recolhimento Substituição Tributária \(GUIA\_REC\_SUBST\) para o Tipo de Livro = ‘108’ \- Apuração Normal \(COD\_TIPO\_LIVRO = ‘108’\) 

Caso o campo Geração para Empresas c/ Inscrição Estadual Única estiver selecionado a origem dos dados será:

\- Módulo ICMS > menu “Apuração > Apuração do ICMS > Lançamentos Complementares > Apuração ICMS > Empresas c/ Insc\. Estadual Única > __Aba Guia__”, campos 🡪 “Mês e Ano Referencia, Data de Vencimento, Valor Recolhimento e Receita Estadual”

\- Tabela Guia de Recolhimento \(GUIA\_RECOLHIMENTO\) para o Tipo de Livro = ‘165’ \- Apuração por Inscrição Estadual Única \(COD\_TIPO\_LIVRO = ‘165’\) 

\- Módulo ICMS > menu “Apuração > Apuração do ICMS > Lançamentos Complementares > Apuração ICMS Subst\. Tributária > Empresas c/ Insc\. Estadual Única > __Aba Guia__”, campos 🡪 “Mês e Ano Referencia, Data de Vencimento, Valor Recolhimento e Receita Estadual”

\- Tabela Guia de Recolhimento Substituição Tributária \(GUIA\_REC\_SUBST\) para o Tipo de Livro = ‘165’ \- Apuração por Inscrição Estadual Única \(COD\_TIPO\_LIVRO = ‘165’\) 

__Para cada Estabelecimento e Período selecionado em tela__:

 

__Passo 1__: Recuperação dos parâmetros da GUIA:

Serão recuperados os dados da parametrização \(GUIA\_RECOLHIMENTO ou GUIA\_REC\_SUBST\) do estabelecimento: MÊS\_ANO\_REF, DAT\_VENCTO, IDENT\_RECEITA\_EST, VALOR\_GUIA\_RECOL considerando os seguintes critérios:

    COD\_EMPRESA 🡪 código da Empresa do login 

    COD\_ESTAB 🡪 código do estabelecimento selecionado 

    MÊS\_ANO\_REF 🡪 de acordo com o mês/ano informado em tela

    IDENT\_RECEITA\_EST 🡪 código de receita que corresponda ao estado de AL – ‘Alagoas’\.

Caso os Códigos de Receita \(campo IDENT\_RECEITA\_EST\) sejam iguais e a Data de Vencimento \(campo DAT\_VENCTO\) diferentes não deverá ser consolidado o registro, será gravado um registro para cada Data de Vencimento diferente\.

Caso os Códigos de Receita \(campo IDENT\_RECEITA\_EST\) sejam diferentes e a Data de Vencimento \(campo DAT\_VENCTO\) iguais não deverá ser consolidado o registro, será gravado um registro para cada Código de receita diferente\.

Caso os Códigos de Receita \(campo IDENT\_RECEITA\_EST\) sejam iguais e a Data de Vencimento \(campo DAT\_VENCTO\) iguais deverá ser consolidado o registro, somar os valores e lançar apenas um registro\.

Caso seja utilizado o mesmo Código de Receita para Guia ICMS Normal e para Guia ICMS\-ST gerar um log de erro conforme abaixo:

‘O Código de Receita utilizado já existe em outra GUIA\. Favor verificar o código de receita das GUIAS \(ICMS Normal e ICMS\-ST\)’ 

__Passo 2__: Gravar na tabela do Registro Tipo 41 \(EST\_AL\_REG\_41\) um novo registro, com os seguintes dados:

__CAMPO__

__CONTEÚDO__

__OBSERVAÇÃO__

COD\_EMPRESA

Empresa do login

COD\_ESTAB

Estabelecimento selecionado em tela\.

DATA\_REF

Campo MÊS\_ANO\_REF da parametrização da GUIA

Lançamento Complementar

DATA\_VENCIMENTO

Campo DAT\_VENCTO da parametrização da GUIA

IDENT\_RECEITA\_EST

Campo IDENT\_RECEITA\_EST da parametrização da GUIA

VLR\_RECEITA

Campo VLR\_GUIA\_RECOL da parametrização da GUIA\.

MFS2332

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

