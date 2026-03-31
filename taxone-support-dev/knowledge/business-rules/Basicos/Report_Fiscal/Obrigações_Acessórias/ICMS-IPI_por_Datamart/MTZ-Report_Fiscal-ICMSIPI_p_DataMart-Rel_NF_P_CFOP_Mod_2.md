# MTZ-Report_Fiscal-ICMSIPI_p_DataMart-Rel_NF_P_CFOP_Mod_2

- **Fonte:** MTZ-Report_Fiscal-ICMSIPI_p_DataMart-Rel_NF_P_CFOP_Mod_2.docx
- **Modificado:** 2025-12-16
- **Tamanho:** 37 KB

---

# REPORT FISCAL  

# Relatório de NF p/ CFOP Modelo 2 

##### Menu: Básicos \- Report Fiscal > Obrigações Acessórias 🡪 ICMS/IPI por DataMart 🡪Relatório de NF p/ CFOP Modelo 2 

# DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__CH71351__

DW \- RF \- Inclusão de Modelo Doc e Chave de Acesso no relatório por CFOP Modelo 2

Criados das colunas: Chave de Acesso e Modelo de Documento no relatório\.

__OS3629__

Criação e remanejamento de colunas 

Criação e remanejamento de colunas do Relatório

__OS4260__

Criação de campo Nº Item NF

Alteração do relatório para criação do campo Nº Item NF

__MFS32994__

Andréa Rocha

Incluir novas colunas no relatório, mostrando os campos BC ICMS ST, Base do PIS e COFINS, Valores PIS e COFINS\.

__MFS__[__575466__](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/575466)

Rogério Ohashi

Inclusão de Regra para recuperar os valores da Capa para Notas Fiscais sem Item\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Regras da tela:__

Criar “Flag” com a opção “Inscrição Estadual Única”\.

Se o flag for habilitado recuperar os estabelecimentos relacionados ao selecionado na opção de seleção “Estabelecimento” através da tabela ICP\_INSC\_EST\_CENTR \(CONTROLE DE OBRIGAÇÕES ESTADUAIS => OBRIGAÇÕES => EMPRESAS/ESTABELECIMENTOS I\. E\. U\.\) campo cod\_estab que estiverem com o campo cod\_estab\_centr igual ao selecionado na opção “Estabelecimento” desde que eles estejam na mesma UF da selecionada na opção “UF”\.

Caso o Estabelecimento selecionado não seja Centralizador e o cliente flegue a opção “Inscrição Estadual Única” deverá ser exibida a seguinte mensagem de erro:

“O Estabelecimento selecionado não é Centralizador, verificar se o parâmetro selecionado \(Inscrição Estadual Única\) está correto\.”

Na listbox “ESTABELECIMENTO”, deverão aparecer somente os Estabelecimentos situados na UF selecionada na listbox anterior “UF”;

Caso o usuário a selecione a opção “TODOS”, deverão ser gerados os dados de todos os Estabelecimentos daquela determinada UF previamente selecionada\.

__CH72444__

__CH72452__

__RN01__

Diminuir a coluna: __*Nº/Série/SubSérie/Nota Fiscal*__ em 5 posições;

Caso as informações ultrapassem o espaço do relatório, as mesmas deverão ser quebradas para continuar na próxima linha;

O nome da coluna deve ser abreviada da seguinte forma: __*Nº/Série/SubSérie/NF*__

__CH71351__

__RN02__

Diminuir a coluna: __*Produto*__ em 21 posições;

Caso as informações ultrapassem o espaço do relatório, as mesmas deverão ser quebradas para continuar na próxima linha;

__CH71351__

__RN03__

Diminuir a coluna: __*Código Razão Social*__ em 7 posições;

Caso as informações ultrapassem o espaço do relatório, as mesmas deverão ser quebradas para continuar na próxima linha;

__CH71351__

__RN04__

Criar a coluna: __Mod\. NF __com 3 posições \(embora sejam duas posições, é necessário caber o título\) será preenchida com a informação cadastrada no campo 13 da SAFX07

__CH71351__

__RN05__

Criar a coluna: __Chave de Acesso __com 30 posições e será preenchido com a informação cadastrada no campo 226 da SAFX07\.

Caso as informações ultrapassem o espaço do relatório, as mesmas deverão ser quebradas para continuar na próxima linha;

__CH71351__

__RN06__

Deverá ser alterada a ordem das colunas do Relatório utilizando a lista descrita abaixo: 

1. UF Cliente/Fornecedor
2. Nº/Série/Subserie NF
3. NF AR 
4. Data Fiscal
5. Produto \(código \+ descrição\)
6. Nº Item NF
7. Descrição Complementar
8. CFOP
9. Extensão CFOP
10. NBM
11. Pessoa Física/Jurídica: Código – Razão Social
12. Pessoa Física/Jurídica: CNPJ/CPF
13. Valor Líquido
14. Vlr Unit\.
15. Quant\.
16. Vlr Base ICMS
17. Vlr ICMS 
18. Alíq\. ICMS 
19. Base PIS e Vlr PIS \[MFS32994\]
20. ICMS ST 
21. Base ICMS ST  \[MFS32994\]
22. Vlr ICMS ñ escrit\.
23. Vlr IPI ñ escrit\. 
24. Vlr IPI
25. Vlr Base IPI
26. Aliq\. IPI
27. Base COFINS e Vlr COFINS \[MFS32994\]
28. Mod\. NF
29. Chave de Acesso

__OS3629__

__OS4260__

__MFS32994__

__RN07__

Criar a coluna: __UF Cliente/Fornecedor__ com 2 posições e será preenchido com a informação cadastrada no campo 19 da SAFX04\. Para seleção do campo, deverá buscar a informação que estiver contida no campo IDENT\_FIS\_JUR da tabela SAFX07 e comparar com a mesma do campo IND\_FIS\_JUR da SAFX04\.

__OS3629__

__RN08__

Criar a coluna: __NF AR __com 12 posições e será preenchido com a informação cadastrada no campo 69 da SAFX07\.

__OS3629__

__RN09__

Criar a coluna: __Vlr__ __Base de Cálculo __com 17 posições \(015V002\) e será preenchido com a informação cadastrada no campo 56 da SAFX08 ou Campo 51 da SAFX07\.

__OS3629__

__MFS__[__575466__](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/575466)

__RN10__

Criar a coluna: __Alíquota ICMS __com 07 posições \(003V004\) e será preenchido com a informação cadastrada no campo 42 da SAFX08 ou Campo 34 da SAFX07\.

__OS3629__

__MFS__[__575466__](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/575466)

__RN11__

Criar a coluna: __ICMS ST__ com 17 posições \(015V002\) e será preenchido com a informação cadastrada no campo 52 da SAFX08 ou Campo 48 da SAFX07\.

__OS3629__

__MFS__[__575466__](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/575466)

__RN12__

Criar a coluna: __Vlr__ __ICMS ñ escrit\.__ com 17 posições \(015V002\) e será preenchido com a informação cadastrada no campo 80 da SAFX08 ou Campo 83 da SAFX07\.

__OS3629__

__MFS__[__575466__](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/575466)

__RN13__

Criar a coluna: __Vlr__ __IPI ñ escrit\.__ com 17 posições \(015V002\) e será preenchido com a informação cadastrada no campo 81 da SAFX08 ou Campo 84 da SAFX07\.

__OS3629__

__MFS__[__575466__](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/575466)

__RN14__

Criar a coluna: __IE__ com 14 posições e será preenchido com a informação cadastrada no campo 08 da SAFX04\. Para seleção do campo, deverá buscar a informação que estiver contida no campo IDENT\_FIS\_JUR da tabela SAFX07 e comparar com a mesma do campo IND\_FIS\_JUR da SAFX04\.

__OS3629__

__RN15__

Criar a coluna: __Nº Item NF__ com tamanho de 05 posições \(005\) de tipo numérico que será preenchido com a informação cadastrada no campo 18 \(NUM\_ITEM\) da SAFX08\. 

__OS4260__

__RN16__

Criar nova coluna no relatório de NF p/ CFOP \- Modelo 2, o campo deve receber concatenado o código da situação tributária A \(CST – ICMS \- Origem da Mercadoria\) – TACES03 \+ o código da situação tributária B, \(CST – ICMS \- Tributação pelo ICMS\) \- TACES04\. \(Campo 179 e 180 da SAFX07 ou Campo 30 e 31 da SAFX08\)

__OS4406__

__MFS__[__575466__](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/575466)

__RN17__

Criar nova coluna no relatório de NF p/ CFOP \- Modelo 2, o campo deve receber a Unidade de Medida utilizado no item de Notas Fiscais de Mercadorias e Produtos, coluna COD\_MEDIDA item 25 da SAFX08\.   

__OS4527__

__RN18__

Incluir campo de descrição complementar no relatório\. Este campo é descricao\_compl da tabela x08\_itens\_merc\.

A coluna terá como título: “DESCRIÇÃO COMPLEMENTAR” e será colocada logo após a coluna de Produto\.

__CH73529__

__RN19__

Nova Coluna: Base ICMS\-ST:

Preencher com o campo 61\- Base ICMS Substituição Tributária da SAFX08 ou Campo 64 da SAFX07\.

__MFS32994__

__MFS__[__575466__](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/575466)

__RN20__

Nova Coluna: Base PIS:

Preencher com o campo 86\- Base PIS da SAFX08 ou campo 102 – Base PIS da SAFX07\.

__MFS32994__

__MFS__[__575466__](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/575466)

__RN21__

Nova Coluna: Valor PIS:

Preencher com o campo 87\- Valor PIS da SAFX08 ou campo 103 – Valor PIS da SAFX07\.

__MFS32994__

__MFS__[__575466__](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/575466)

__RN22__

Nova Coluna: Base COFINS:

Preencher com o campo 88\- Base COFINS da SAFX08 ou campo 104 – Base COFINS da SAFX07\.

__MFS32994__

__MFS__[__575466__](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/575466)

__RN23__

Nova Coluna: Valor COFINS:

Preencher com o campo 89\- Valor COFINS da SAFX08 ou campo 105 – Valor COFINS da SAFX07\.

__MFS32994__

__MFS__[__575466__](https://dev.azure.com/tr-ggo/Mastersaf%20Fiscal%20Solutions/_workitems/edit/575466)

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

