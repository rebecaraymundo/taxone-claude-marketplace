# MTZ_Funcionalidade_Upload

- **Fonte:** MTZ_Funcionalidade_Upload.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 58 KB

---

<a id="OLE_LINK3"></a><a id="OLE_LINK4"></a>__Fucionalidade Upload –__<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a>__ Dentro das Telas de Apuração PIS/PASEP  e Apuração COFINS__

__\(EFD\- Escrituração Fiscal Digital das Contribuições\)__

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3619

Ajustes do crédito de PIS/PASEP e COFINS \(Registros M220/M620\)

Será criada a funcionalidade Upload para carregar as informações dos ajustes do crédito de PIS/PASEP e COFINS \(Registros M220/M620\)

25/05/2012

OS4584

Detalhamento por Código de Receita PIS/PASEP e COFINS \(M205/M605\)

Será criada a funcionalidade Upload para carregar as informações de Detalhamento por Código de Receita PIS/PASEP e COFINS \(Registros M205/M605\)\.

23/10/2014

OS4753

Detalhamento dos Ajustes da Contribuição para o PIS/PASEP e Cofins apurada\.

Carregar as informações do Detalhamento dos Ajustes da Contribuição para o PIS/PASEP e Cofins apurada\. \(Registros M225/M625\)\.

18/03/2015

MFS\-19941

Ajustes da BC do PIS/PASEP e da COFINS \(Registros M215/M615\)

Será criada a funcionalidade Upload para carregar as informações dos ajustes da BC do PIS/PASEP e da COFINS \(Registros M215/M615\)

03/08/2018

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN01__

Inclusão da funcionalidade Upload na tela Apuração PIS/PASEP no Módulo: SPED EFD – Escrituração Fiscal Digital das Contribuições, Menu: Obrigações  🡪 Manutenção, dentro da opção Contribuição para PIS/PASEP no Período – M200 / Detalhamento da Contribuição – M210

OS3619

__RN02__

Estabelecimento: Será exibido o estabelecimento da apuração selecionado\.

Obrigação Fiscal: Indica o nome da Obrigação importada

Período: Será exibido o período da apuração selecionada\.

Layout: Indica o layout utilizado na apuração selecionada\.

Situação: Indica a situação da apuração selecionada\.

Pasta: Neste campo o usuário deverá informar o diretório que será usado para considerar o arquivo XML 

Esta funcionalidade se comportará conforme a tela de importação de TFIX/TACES, com a diferença de que ao invés de mostrarmos a tela de diretórios na abertura da tela de Upload, estaremos mostrando no click da pastinha, não permitindo a digitação da pasta\.

Importar: O usuário define quais arquivos serão importados\.

OS3619

__RN03__

__Processos:__ Permite ao usuário visualizar os processos gerados de acordo com a quantidade de dias informados\. Sendo exibido o Número do Processo, Descrição, Situação do Processo, Início e Fim da Execução, Usuário\. O usuário ao selecionar um processo, poderá emitir o relatório e até fazer a sua exclusão\. 

OS3169

__RN04__

__Log:__ Nesta opção é possível visualizar o Relatório de críticas de dados dos registros M220\. Ele será exibido após a execução\. 

__Considerações: __

 1 – Só será aceito arquivo com formato e extensão XML\.

OS3619

__RN05__

Este relatório possui duas quebras, onde são demonstradas as seguintes colunas: 

__Registros Rejeitados __  
Informação: Informa o campo que foi apresentado erro\.   
Rejeição: Informa para o usuário o motivo da rejeição\. 

__Resumo de Importação__   
Registros Lidos: Informa a quantidade de registros que foram considerados\. Se não foi encontrado o registro PAI os registros filhos serão desconsiderados, portanto os mesmos não serão considerados como LIDOS\.  
Registros Rejeitados: Informa a quantidade de registros rejeitados \(que foram lidos e possuíram alguma inconsistência\)\. 

__Modelo do relatório: __

            

OS3619

__RN05__

           RELATORIO DE LOG \-  DETALHAMENTO DA CONTRIBUIÇÃO 

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*EMPRESA/ESTABELECIMENTOMATRIZ\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

EMPRESA: 076 – DEMOSTRACAO TSL – TECNOLOGIA EM SISTEMAS DE LEGISLACAO

ESTABELECIMENTO MATRIZ: 001AL – ESTABELECIMENTO ALAGOAS

CNPJ: 00000000000                                                      

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*PROCESSO\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

IMPORTACAO DE INFORMACOES DO DETALHAMENTO DA CONTRIBUICAO

PERIODO DE: 01/01/2011  A 31/01/2011             

  PROCESSO Nº: 111111              

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*ARQUIVO\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

ARQUIVO:\\\\ARQUIVOTESTE\.XML

DATA DO PROCESSAMENTO: 20/06/2012	

REGISTRO M220 – LINHA OCORRENCIA:1 

Data de Referencia er pertence ao eríodo da apuracao\. Valor informado: 01/01/2011

REGISTRO M220 – LINHA OCORRENCIA:2 

Data de Referencia er pertence ao eríodo da apuracao\. Valor informado: 15/01/2011

RESUMO DE IMPORTACAO

*REGISTRO M210:*

*Registros Lidos:* 002  
*Registros Rejeitados:* 000

REGISTRO M220:

*Registros Lidos:* 002   
*Registros Rejeitados:* 002 

OS3619

__RN06__

Na tela Apuração PIS/PASEP no Módulo: SPED EFD – Escrituração Fiscal Digital das Contribuições, Menu: Obrigações  🡪 Manutenção, dentro da opção Contribuição para PIS/PASEP no Período – M200 / Detalhamento da Contribuição – M210, só serão lidos / rejeitados os arquivos de PIS/PASEP\. Ou seja, registros com informações do registro PAI \(M210\) e dos filhos \(M220\), os demais serão desprezados\.

OS3619

__RN07__

Se o status da obrigação for fechada e o usuário acionar a funcionalidade Upload, exibir a msg: Só é permitido usar esta funcionalidade se o Status da Apuração for “Realizada” ou “Reaberta”\.

OS3619

__RN08__

Cada arquivo deve o tamanho máximo de 2Mb, caso contrário exibir a seguinte msg: “O arquivo selecionado ultrapassou o tamanho máximo de 2Mb”\.

OS3619

__RN09__

Inclusão da funcionalidade Upload na tela Apuração COFINS no Módulo: SPED EFD – Escrituração Fiscal Digital das Contribuições, Menu: Obrigações  🡪 Manutenção, dentro da opção Contribuição para COFINS no Período – M600 / Detalhamento da Contribuição – M610

OS3619

__RN10__

Estabelecimento: Será exibido o estabelecimento da apuração selecionado\.

Obrigação Fiscal: Indica o nome da Obrigação importada

Período: Será exibido o período da apuração selecionada\.

Layout: Indica o layout utilizado na apuração selecionada\.

Situação: Indica a situação da apuração selecionada\.

Pasta: Neste campo o usuário deverá informar o diretório que será usado para considerar o arquivo XML 

Esta funcionalidade se comportará conforme a tela de importação de TFIX/TACES, com a diferença de que ao invés de mostrarmos a tela de diretórios na abertura da tela de Upload, estaremos mostrando no click da pastinha, não permitindo a digitação da pasta\.

Importar: O usuário define quais arquivos serão importados\.

OS3619

__RN11__

__Processos:__ Permite ao usuário visualizar os processos gerados de acordo com a quantidade de dias informados\. Sendo exibido o Número do Processo, Descrição, Situação do Processo, Início e Fim da Execução, Usuário\. O usuário ao selecionar um processo, poderá emitir o relatório e até fazer a sua exclusão\. 

OS3619

__RN12__

__Log: __Nesta opção é possível visualizar o Relatório de críticas de dados dos registros M620\. Ele será exibido após a execução\. 

__Considerações: __

 1 – Só será aceito arquivo com formato e extensão XML\.

OS3619

__RN13__

Este relatório possui duas quebras, onde são demonstradas as seguintes colunas: 

__Registros Rejeitados __  
Informação: Informa o campo que foi apresentado erro\.   
Rejeição: Informa para o usuário o motivo da rejeição\. 

__Resumo de Importação__   
Registros Lidos: Informa a quantidade de registros que foram considerados\. Se não foi encontrado o registro PAI os registros filhos serão desconsiderados, portanto não serão considerados como LIDOS\.  
Registros Rejeitados: Informa a quantidade de registros rejeitados \(que foram lidos e possuíram alguma inconsistência\)\. 

__Modelo do relatório: __

OS3619

__RN13__

           RELATORIO DE LOG \-  DETALHAMENTO DA CONTRIBUIÇÃO 

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*EMPRESA/ESTABELECIMENTOMATRIZ\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

EMPRESA: 076 – DEMOSTRACAO TSL – TECNOLOGIA EM SISTEMAS DE LEGISLACAO

ESTABELECIMENTO MATRIZ: 001AL – ESTABELECIMENTO ALAGOAS

CNPJ: 00000000000                                                      

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*PROCESSO\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

IMPORTACAO DE INFORMACOES DO DETALHAMENTO DA CONTRIBUICAO

PERIODO DE: 01/01/2011  A 31/01/2011             

  PROCESSO Nº: 111111              

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*ARQUIVO\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

ARQUIVO:\\\\ARQUIVOTESTE\.XML

DATA DO PROCESSAMENTO: 20/06/2012	

REGISTRO M620 – LINHA OCORRENCIA:1 

Data de Referencia nao pertence ao periodo da apuracao\. Valor informado: 01/01/2011

REGISTRO M620 – LINHA OCORRENCIA:2 

Data de Referencia nao pertence ao periodo da apuracao\. Valor informado: 15/01/2011

RESUMO DE IMPORTACAO

*REGISTRO M610:*

*Registros Lidos:* 002  
*Registros Rejeitados:* 000

REGISTRO M220:

*Registros Lidos:* 002   
*Registros Rejeitados:* 002 

OS3619

__RN14__

Na tela Apuração COFINS  no Módulo: SPED EFD – Escrituração Fiscal Digital das Contribuições, Menu: Obrigações  🡪 Manutenção, dentro da opção Contribuição para COFINS no Período – M200 / Detalhamento da Contribuição – M610, só serão lidos / rejeitados os arquivos de COFINS\. Ou seja, registros com informações do registro PAI \(M610\) e dos filhos \(M620\), os demais serão desprezados\.

OS3619

__RN15__

Se o status da obrigação for fechada e o usuário acionar a funcionalidade Upload, exibir a msg: Só é permitido usar esta funcionalidade se o Status da Apuração for “Realizada” ou “Reaberta”\.

OS3619

__RN16__

Cada arquivo deve o tamanho máximo de 2Mb, caso contrário exibir a seguinte msg: “O arquivo selecionado ultrapassou o tamanho máximo de 2Mb”\.

OS3619

REGISTRO M205

__RN17__

<a id="OLE_LINK25"></a><a id="OLE_LINK26"></a>Inclusão da funcionalidade Upload na tela Apuração PIS/PASEP no Módulo: SPED EFD – Escrituração Fiscal Digital das Contribuições, Menu: Obrigações  🡪 Manutenção, dentro da opção Contribuição para PIS/PASEP no Período – M200, <a id="OLE_LINK11"></a><a id="OLE_LINK12"></a><a id="OLE_LINK13"></a>Detalhamento por Código de Receita PIS/PASEP – M205

OS4584

__RN18__

<a id="OLE_LINK30"></a><a id="OLE_LINK31"></a><a id="OLE_LINK32"></a>Estabelecimento: Será exibido o estabelecimento da apuração selecionado\.

Obrigação Fiscal: Indica o nome da Obrigação importada

Período: Será exibido o período da apuração selecionada\.

Layout: Indica o layout utilizado na apuração selecionada\.

Situação: Indica a situação da apuração selecionada\.

Pasta: Neste campo o usuário deverá informar o diretório que será usado para considerar o arquivo XML 

Esta funcionalidade se comportará conforme a tela de importação de TFIX/TACES, com a diferença de que ao invés de mostrarmos a tela de diretórios na abertura da tela de Upload, estaremos mostrando no click da pastinha, não permitindo a digitação da pasta\.

Importar: O usuário define quais arquivos serão importados\.

OS4584

<a id="_Hlk401913569"></a>__RN19__

__Processos:__ Permite ao usuário visualizar os processos gerados de acordo com a quantidade de dias informados\. Sendo exibido o Número do Processo, Descrição, Situação do Processo, Início e Fim da Execução, Usuário\. O usuário ao selecionar um processo, poderá emitir o relatório e até fazer a sua exclusão\. 

OS4584

__RN20__

__Log:__ Nesta opção é possível visualizar o Relatório de críticas de dados dos registros M205\. Ele será exibido após a execução\. 

__Considerações: __

 1 – Só será aceito arquivo com formato e extensão XML\.

OS4584

<a id="_Hlk401908956"></a>__RN21__

Este relatório possui duas quebras, onde são demonstradas as seguintes colunas: 

__Registros Rejeitados __  
Informação: Informa o campo que foi apresentado erro\.   
Rejeição: Informa para o usuário o motivo da rejeição\. 

__Resumo de Importação__   
Registros Lidos: Informa a quantidade de registros que foram considerados\. Registros Rejeitados: Informa a quantidade de registros rejeitados \(que foram lidos e possuíram alguma inconsistência\)\. 

__Modelo do relatório: __

<a id="OLE_LINK59"></a><a id="OLE_LINK60"></a><a id="OLE_LINK61"></a>OS4584

__RN21__

<a id="OLE_LINK46"></a><a id="OLE_LINK47"></a><a id="OLE_LINK48"></a>          RELATORIO DE LOG \-  DETALHAMENTO POR CÓDIGO DE RECEITA

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*EMPRESA/ESTABELECIMENTOMATRIZ\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

EMPRESA: 076 – DEMOSTRACAO TSL – TECNOLOGIA EM SISTEMAS DE LEGISLACAO

ESTABELECIMENTO MATRIZ: 001AL – ESTABELECIMENTO ALAGOAS

CNPJ: 00000000000                                                      

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*PROCESSO\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*IMPORTACAO DE INFORMACOES DO DETALHAMENTO DA CONTRIBUICAO

PERIODO DE: 01/01/2011  A 31/01/2011             

  PROCESSO Nº: 111111              

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*ARQUIVO\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

ARQUIVO:\\\\ARQUIVOTESTE\.XML

DATA DO PROCESSAMENTO: 20/06/2012

REGISTRO M205– LINHA OCORRENCIA:1 

Data de Referencia nao pertence ao periodo da apuracao\. Valor informado: 01/01/2011

REGISTRO M205 – LINHA OCORRENCIA:2 

Data de Referencia nao pertence ao periodo da apuracao\. Valor informado: 15/01/2011

RESUMO DE IMPORTACAO

*REGISTRO M205:*

*Registros Lidos:* 002  
*Registros Rejeitados:* 00

OS4584

<a id="_Hlk401921484"></a>__RN22__

__ __Na tela Apuração PIS/PASEP no Módulo: SPED EFD – Escrituração Fiscal Digital das Contribuições, Menu: Obrigações  🡪 Manutenção, Apuração PIS/PASEP dentro da opção Contribuição para PIS/PASEP no Período – M200, só serão lidos / rejeitados os arquivos de PIS/PASEP\. Ou seja, apenas registros com informações do registro M205 demais serão desprezados\.

<a id="OLE_LINK17"></a><a id="OLE_LINK18"></a>OS4584

__RN23__

Se o status da obrigação for fechada e o usuário acionar a funcionalidade Upload, exibir a msg: Só é permitido usar esta funcionalidade se o Status da Apuração for “Realizada” ou ‘Reaberta’\.

<a id="OLE_LINK19"></a><a id="OLE_LINK20"></a><a id="OLE_LINK21"></a>OS4584

__RN24__

Cada arquivo deve o tamanho máximo de 2Mb, caso contrário exibir a seguinte msg: “O arquivo selecionado ultrapassou o tamanho máximo de 2Mb”\.

<a id="OLE_LINK27"></a><a id="OLE_LINK28"></a><a id="OLE_LINK29"></a>OS4584

REGISTRO M605

__RN25__

Inclusão da funcionalidade Upload na tela Apuração COFINS no Módulo: SPED EFD – Escrituração Fiscal Digital das Contribuições, Menu: Obrigações  🡪 Manutenção, Apuração COFINS dentro da opção Contribuição para COFINS no Período – M600 Detalhamento por Código de Receita COFINS – M605

OS4584

__RN26__

Estabelecimento: Será exibido o estabelecimento da apuração selecionado\.

Obrigação Fiscal: Indica o nome da Obrigação importada

Período: Será exibido o período da apuração selecionada\.

Layout: Indica o layout utilizado na apuração selecionada\.

Situação: Indica a situação da apuração selecionada\.

Pasta: Neste campo o usuário deverá informar o diretório que será usado para considerar o arquivo XML 

Esta funcionalidade se comportará conforme a tela de importação de TFIX/TACES, com a diferença de que ao invés de mostrarmos a tela de diretórios na abertura da tela de Upload, estaremos mostrando no click da pastinha, não permitindo a digitação da pasta\.

Importar: O usuário define quais arquivos serão importados\.

<a id="OLE_LINK41"></a><a id="OLE_LINK42"></a><a id="OLE_LINK43"></a><a id="OLE_LINK44"></a><a id="OLE_LINK45"></a>OS4584

__RN27__

__Processos:__ Permite ao usuário visualizar os processos gerados de acordo com a quantidade de dias informados\. Sendo exibido o Número do Processo, Descrição, Situação do Processo, Início e Fim da Execução, Usuário\. O usuário ao selecionar um processo, poderá emitir o relatório e até fazer a sua exclusão\. 

OS4584

__RN28__

__Log:__ Nesta opção é possível visualizar o Relatório de críticas de dados dos registros M605\. Ele será exibido após a execução\. 

__Considerações: __

 1 – Só será aceito arquivo com formato e extensão XML\.

OS4584

<a id="OLE_LINK49"></a><a id="OLE_LINK50"></a><a id="OLE_LINK51"></a>__RN29__

Este relatório possui duas quebras, onde são demonstradas as seguintes colunas: 

__Registros Rejeitados __  
Informação: Informa o campo que foi apresentado erro\.   
Rejeição: Informa para o usuário o motivo da rejeição\. 

__Resumo de Importação__   
Registros Lidos: Informa a quantidade de registros que foram considerados\. Registros Rejeitados: Informa a quantidade de registros rejeitados \(que foram lidos e possuíram alguma inconsistência\)\. 

__Modelo do relatório: __

<a id="OLE_LINK52"></a><a id="OLE_LINK53"></a><a id="OLE_LINK54"></a><a id="OLE_LINK55"></a><a id="OLE_LINK56"></a>OS4584

__RN29__

          RELATORIO DE LOG \-  DETALHAMENTO POR CÓDIGO DE RECEITA

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*EMPRESA/ESTABELECIMENTOMATRIZ\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

EMPRESA: 076 – DEMOSTRACAO TSL – TECNOLOGIA EM SISTEMAS DE LEGISLACAO

ESTABELECIMENTO MATRIZ: 001AL – ESTABELECIMENTO ALAGOAS

CNPJ: 00000000000                                                      

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*PROCESSO\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*IMPORTACAO DE INFORMACOES DO DETALHAMENTO DA CONTRIBUICAO

PERIODO DE: 01/01/2011  A 31/01/2011             

  PROCESSO Nº: 111111              

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*ARQUIVO\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

ARQUIVO:\\\\ARQUIVOTESTE\.XML

DATA DO PROCESSAMENTO: 20/06/2012

REGISTRO M605– LINHA OCORRENCIA:1 

Data de Referencia nao pertence ao periodo da apuracao\. Valor informado: 01/01/2011

REGISTRO M605 – LINHA OCORRENCIA:2 

Data de Referencia nao pertence ao periodo da apuracao\. Valor informado: 15/01/2011

RESUMO DE IMPORTACAO

*REGISTRO M605:*

*Registros Lidos:* 002  
*Registros Rejeitados:* 00

OS4584

__RN30__

__ __Na tela Apuração COFINS no Módulo: SPED EFD – Escrituração Fiscal Digital das Contribuições, Menu: Obrigações  🡪 Manutenção, Apuração COFINS dentro da opção Contribuição para COFINS no Período – M600, só serão lidos / rejeitados os arquivos de COFINS\. Ou seja, apenas registros com informações do registro M605 demais serão desprezados\.

OS4584

__RN31__

Se o status da obrigação for fechada e o usuário acionar a funcionalidade Upload, exibir a msg: Só é permitido usar esta funcionalidade se o Status da Apuração for “Realizada” ou “Reaberta”\.

OS4584

__RN32__

Cada arquivo deve o tamanho máximo de 2Mb, caso contrário exibir a seguinte msg: “O arquivo selecionado ultrapassou o tamanho máximo de 2Mb”\.

OS4584

REGISTRO M225

__RN33__

A importação deste registro será através do botão “Upload” do registro “M210’\.

__RN34__

Estabelecimento: Será exibido o estabelecimento da apuração selecionado\.

Obrigação Fiscal: Indica o nome da Obrigação importada

Período: Será exibido o período da apuração selecionada\.

Layout: Indica o layout utilizado na apuração selecionada\.

Situação: Indica a situação da apuração selecionada\.

Pasta: Neste campo o usuário deverá informar o diretório que será usado para considerar o arquivo XML 

Esta funcionalidade se comportará conforme a tela de importação de TFIX/TACES, com a diferença de que ao invés de mostrarmos a tela de diretórios na abertura da tela de Upload, estaremos mostrando no click da pastinha, não permitindo a digitação da pasta\.

Importar: O usuário define quais arquivos serão importados\.

OS4753

__RN35__

__Processos:__ Permite ao usuário visualizar os processos gerados de acordo com a quantidade de dias informados\. Sendo exibido o Número do Processo, Descrição, Situação do Processo, Início e Fim da Execução, Usuário\. O usuário ao selecionar um processo, poderá emitir o relatório e até fazer a sua exclusão\. 

OS4753

__RN36__

__Log:__ Nesta opção é possível visualizar o Relatório de críticas de dados dos registros M225\. Ele será exibido após a execução\. 

__Considerações: __

 1 – Só será aceito arquivo com formato e extensão XML\.

OS4753

__RN37__

Este relatório possui duas quebras, onde são demonstradas as seguintes colunas: 

__Registros Rejeitados __  
Informação: Informa o campo que foi apresentado erro\.   
Rejeição: Informa para o usuário o motivo da rejeição\. 

__Resumo de Importação__   
Registros Lidos: Informa a quantidade de registros que foram considerados\. Registros Rejeitados: Informa a quantidade de registros rejeitados \(que foram lidos e possuíram alguma inconsistência\)\. 

__Modelo do relatório: __

OS4753

__RN37__

          RELATORIO DE LOG \-  DETALHAMENTO DOS AJUSTES DA CONTRIBUIÇÃO PARA O PIS/PASEP APURADA 

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*EMPRESA/ESTABELECIMENTOMATRIZ\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

EMPRESA: 076 – DEMOSTRACAO TSL – TECNOLOGIA EM SISTEMAS DE LEGISLACAO

ESTABELECIMENTO MATRIZ: 001AL – ESTABELECIMENTO ALAGOAS

CNPJ: 00000000000                                                      

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*PROCESSO\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*IMPORTACAO DE INFORMACOES DO DETALHAMENTO DA CONTRIBUICAO

PERIODO DE: 01/01/2011  A 31/01/2011             

  PROCESSO Nº: 111111              

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*ARQUIVO\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

ARQUIVO:\\\\ARQUIVOTESTE\.XML

DATA DO PROCESSAMENTO: 20/06/2014

REGISTRO M225– LINHA OCORRENCIA:1 

Data de Referencia nao pertence ao periodo da apuracao\. Valor informado: 01/01/2013

REGISTRO M205 – LINHA OCORRENCIA:2 

Data de Referencia nao pertence ao periodo da apuracao\. Valor informado: 15/01/2013

RESUMO DE IMPORTACAO

*REGISTRO M225:*

*Registros Lidos:* 002  
*Registros Rejeitados:* 00

OS4753

__RN38__

Na tela Apuração PIS/PASEP no Módulo: SPED EFD – Escrituração Fiscal Digital das Contribuições, Menu: Obrigações  🡪 Manutenção, Apuração PIS/PASEP dentro da opção Contribuição para PIS/PASEP no Período – M200, Aba Ajustes da Contribuição para o PIS/PASEP Apurada – M220 >> Detalhamento dos Ajustes da Contribuição para o PIS/PASEP – M225\. Ou seja, apenas registros com informações do registro M225 demais serão desprezados\.

OS4753

__RN39__

Se o status da obrigação for fechada e o usuário acionar a funcionalidade Upload, exibir a msg: Só é permitido usar esta funcionalidade se o Status da Apuração for “Realizada” ou “Reaberta”

OS4753

__RN40__

Cada arquivo deve o tamanho máximo de 2Mb, caso contrário exibir a seguinte msg: “O arquivo selecionado ultrapassou o tamanho máximo de 2Mb”\.

OS4753

REGISTRO M625

__RN41__

A importação deste registro será através do botão “Upload” do registro “M610’\.

OS4753

__RN42__

Estabelecimento: Será exibido o estabelecimento da apuração selecionado\.

Obrigação Fiscal: Indica o nome da Obrigação importada

Período: Será exibido o período da apuração selecionada\.

Layout: Indica o layout utilizado na apuração selecionada\.

Situação: Indica a situação da apuração selecionada\.

Pasta: Neste campo o usuário deverá informar o diretório que será usado para considerar o arquivo XML 

Esta funcionalidade se comportará conforme a tela de importação de TFIX/TACES, com a diferença de que ao invés de mostrarmos a tela de diretórios na abertura da tela de Upload, estaremos mostrando no click da pastinha, não permitindo a digitação da pasta\.

Importar: O usuário define quais arquivos serão importados\.

OS4753

__RN43__

__Processos:__ Permite ao usuário visualizar os processos gerados de acordo com a quantidade de dias informados\. Sendo exibido o Número do Processo, Descrição, Situação do Processo, Início e Fim da Execução, Usuário\. O usuário ao selecionar um processo, poderá emitir o relatório e até fazer a sua exclusão\. 

OS4753

__RN44__

__Log:__ Nesta opção é possível visualizar o Relatório de críticas de dados dos registros M625\. Ele será exibido após a execução\. 

__Considerações: __

 1 – Só será aceito arquivo com formato e extensão XML\.

OS4753

__RN45__

Este relatório possui duas quebras, onde são demonstradas as seguintes colunas: 

__Registros Rejeitados __  
Informação: Informa o campo que foi apresentado erro\.   
Rejeição: Informa para o usuário o motivo da rejeição\. 

__Resumo de Importação__   
Registros Lidos: Informa a quantidade de registros que foram considerados\. Registros Rejeitados: Informa a quantidade de registros rejeitados \(que foram lidos e possuíram alguma inconsistência\)\. 

__Modelo do relatório: __

OS4753

__RN45__

          RELATORIO DE LOG \-  Detalhamento dos Ajustes da Contribuição da COFINS Apurada 

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*EMPRESA/ESTABELECIMENTOMATRIZ\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

EMPRESA: 076 – DEMOSTRACAO TSL – TECNOLOGIA EM SISTEMAS DE LEGISLACAO

ESTABELECIMENTO MATRIZ: 001AL – ESTABELECIMENTO ALAGOAS

CNPJ: 00000000000                                                      

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*PROCESSO\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*IMPORTACAO DE INFORMACOES DO DETALHAMENTO DA CONTRIBUICAO

PERIODO DE: 01/01/2011  A 31/01/2011             

  PROCESSO Nº: 111111              

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*ARQUIVO\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

ARQUIVO:\\\\ARQUIVOTESTE\.XML

DATA DO PROCESSAMENTO: 20/06/2014

REGISTRO M625– LINHA OCORRENCIA:1 

Data de Referencia nao pertence ao periodo da apuracao\. Valor informado: 01/01/2013

REGISTRO M605 – LINHA OCORRENCIA:2 

Data de Referencia nao pertence ao periodo da apuracao\. Valor informado: 15/01/2013

RESUMO DE IMPORTACAO

*REGISTRO M625:*

*Registros Lidos:* 002  
*Registros Rejeitados:* 00

OS4753

__RN46__

__ __Na tela Apuração COFINS no Módulo: SPED EFD – Escrituração Fiscal Digital das Contribuições, Menu: Obrigações  🡪 Manutenção, Apuração COFINS dentro da opção Contribuição para COFINS no Período – M600, Aba Ajustes da Contribuição para o PIS/PASEP Apurada – M220 >> Detalhamento dos Ajustes da Contribuição para o PIS/PASEP – M225 só serão lidos / rejeitados os arquivos de COFINS\. Ou seja, apenas registros com informações do registro M605 demais serão desprezados\.

OS4753

__RN47__

Se o status da obrigação for fechada e o usuário acionar a funcionalidade Upload, exibir a msg: Só é permitido usar esta funcionalidade se o Status da Apuração for “Realizada” ou “Reaberta”\.

OS4753

__RN48__

Cada arquivo deve o tamanho máximo de 2Mb, caso contrário exibir a seguinte msg: “O arquivo selecionado ultrapassou o tamanho máximo de 2Mb”\.

OS4753

REGISTRO M215

__RN49__

A importação deste registro será através do botão “Upload” do registro “M210’\.

MFS\-19941

__RN50__

Estabelecimento: Será exibido o estabelecimento da apuração selecionado\.

Obrigação Fiscal: Indica o nome da Obrigação importada

Período: Será exibido o período da apuração selecionada\.

Layout: Indica o layout utilizado na apuração selecionada\.

Situação: Indica a situação da apuração selecionada\.

Pasta: Neste campo o usuário deverá informar o diretório que será usado para considerar o arquivo XML 

Esta funcionalidade se comportará conforme a tela de importação de TFIX/TACES, com a diferença de que ao invés de mostrarmos a tela de diretórios na abertura da tela de Upload, estaremos mostrando no click da pastinha, não permitindo a digitação da pasta\.

Importar: O usuário define quais arquivos serão importados\.

MFS\-19941

__RN51__

__Processos:__ Permite ao usuário visualizar os processos gerados de acordo com a quantidade de dias informados\. Sendo exibido o Número do Processo, Descrição, Situação do Processo, Início e Fim da Execução, Usuário\. O usuário ao selecionar um processo, poderá emitir o relatório e até fazer a sua exclusão\. 

MFS\-19941

__RN52__

__Log:__ Nesta opção é possível visualizar o Relatório de críticas de dados dos registros M215\. Ele será exibido após a execução\. 

__Considerações: __

 1 – Só será aceito arquivo com formato e extensão XML\.

MFS\-19941

__RN53__

Este relatório possui duas quebras, onde são demonstradas as seguintes colunas: 

__Registros Rejeitados __  
Informação: Informa o campo que foi apresentado erro\.   
Rejeição: Informa para o usuário o motivo da rejeição\. 

__Resumo de Importação__   
Registros Lidos: Informa a quantidade de registros que foram considerados\. Registros Rejeitados: Informa a quantidade de registros rejeitados \(que foram lidos e possuíram alguma inconsistência\)\. 

__Modelo do relatório: __

MFS\-19941

__RN54__

          RELATORIO DE LOG \-  Detalhamento dos Ajustes da BC da Contribuição para o Pis/Pasep Apurada

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*EMPRESA/ESTABELECIMENTOMATRIZ\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

EMPRESA: XXX – XXXXXXXXXX

ESTABELECIMENTO MATRIZ: XXXXXX – XXXXXXXXXX

CNPJ: 00000000000                                                      

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*PROCESSO\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*IMPORTACAO DE INFORMACOES DO DETALHAMENTO DA CONTRIBUICAO

PERIODO DE: DD/MM/AAAA  A DD/MM/AAAA             

  PROCESSO Nº: 000000              

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*ARQUIVO\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

ARQUIVO:\\\\ARQUIVOTESTE\.XML

DATA DO PROCESSAMENTO: DD/MM/AAAA

REGISTRO M215– LINHA OCORRENCIA:1 

Data de Referencia nao pertence ao periodo da apuracao\. Valor informado: DD/MM/AAAA

REGISTRO M215 – LINHA OCORRENCIA:2 

Data de Referencia nao pertence ao periodo da apuracao\. Valor informado: DD/MM/AAAA

RESUMO DE IMPORTACAO

*REGISTRO M215:*

*Registros Lidos:* 002  
*Registros Rejeitados:* 00

MFS\-19941

__RN55__

Na tela Apuração PIS/PASEP no Módulo: SPED EFD – Escrituração Fiscal Digital das Contribuições, Menu: Obrigações  🡪 Manutenção, Apuração PIS/PASEP dentro da opção Contribuição para PIS/PASEP no Período – M200, só serão lidos / rejeitados os arquivos de PIS/PASEP\. Ou seja, apenas registros com informações do registro M215, os demais serão desprezados\.

MFS\-19941

__RN56__

Se o status da obrigação for fechada e o usuário acionar a funcionalidade Upload, exibir a msg: Só é permitido usar esta funcionalidade se o Status da Apuração for “Realizada” ou “Reaberta”\.

MFS\-19941

__RN57__

Cada arquivo deve o tamanho máximo de 2Mb, caso contrário exibir a seguinte msg: “O arquivo selecionado ultrapassou o tamanho máximo de 2Mb”\.

MFS\-19941

REGISTRO M615

__RN58__

A importação deste registro será através do botão “Upload” do registro “M610’\.

MFS\-19941

__RN59__

Estabelecimento: Será exibido o estabelecimento da apuração selecionado\.

Obrigação Fiscal: Indica o nome da Obrigação importada

Período: Será exibido o período da apuração selecionada\.

Layout: Indica o layout utilizado na apuração selecionada\.

Situação: Indica a situação da apuração selecionada\.

Pasta: Neste campo o usuário deverá informar o diretório que será usado para considerar o arquivo XML 

Esta funcionalidade se comportará conforme a tela de importação de TFIX/TACES, com a diferença de que ao invés de mostrarmos a tela de diretórios na abertura da tela de Upload, estaremos mostrando no click da pastinha, não permitindo a digitação da pasta\.

Importar: O usuário define quais arquivos serão importados\.

MFS\-19941

__RN60__

__Processos:__ Permite ao usuário visualizar os processos gerados de acordo com a quantidade de dias informados\. Sendo exibido o Número do Processo, Descrição, Situação do Processo, Início e Fim da Execução, Usuário\. O usuário ao selecionar um processo, poderá emitir o relatório e até fazer a sua exclusão\. 

MFS\-19941

__RN61__

__Log:__ Nesta opção é possível visualizar o Relatório de críticas de dados dos registros M615\. Ele será exibido após a execução\. 

__Considerações: __

 1 – Só será aceito arquivo com formato e extensão XML\.

MFS\-19941

__RN62__

Este relatório possui duas quebras, onde são demonstradas as seguintes colunas: 

__Registros Rejeitados __  
Informação: Informa o campo que foi apresentado erro\.   
Rejeição: Informa para o usuário o motivo da rejeição\. 

__Resumo de Importação__   
Registros Lidos: Informa a quantidade de registros que foram considerados\. Registros Rejeitados: Informa a quantidade de registros rejeitados \(que foram lidos e possuíram alguma inconsistência\)\. 

__Modelo do relatório: __

MFS\-19941

__RN63__

          RELATORIO DE LOG \-  Detalhamento dos Ajustes da BC da COFINS Apurada

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*EMPRESA/ESTABELECIMENTOMATRIZ\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

EMPRESA: XXX – XXXXXXXXXX

ESTABELECIMENTO MATRIZ: XXXXXX – XXXXXXXXXX

CNPJ: 00000000000                                                      

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*PROCESSO\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*IMPORTACAO DE INFORMACOES DO DETALHAMENTO DA CONTRIBUICAO

PERIODO DE: DD/MM/AAAA  A DD/MM/AAAA             

  PROCESSO Nº: 000000              

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*ARQUIVO\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

ARQUIVO:\\\\ARQUIVOTESTE\.XML

DATA DO PROCESSAMENTO: DD/MM/AAAA

REGISTRO M615– LINHA OCORRENCIA:1 

Data de Referencia nao pertence ao periodo da apuracao\. Valor informado: DD/MM/AAAA

REGISTRO M615 – LINHA OCORRENCIA:2 

Data de Referencia nao pertence ao periodo da apuracao\. Valor informado: DD/MM/AAAA

RESUMO DE IMPORTACAO

*REGISTRO M615:*

*Registros Lidos:* 002  
*Registros Rejeitados:* 00

MFS\-19941

__RN64__

Na tela Apuração COFINS no Módulo: SPED EFD – Escrituração Fiscal Digital das Contribuições, Menu: Obrigações  🡪 Manutenção, Apuração COFINS dentro da opção Contribuição para COFINS no Período – M600, só serão lidos / rejeitados os arquivos de COFINS\. Ou seja, apenas registros com informações do registro M615, os demais serão desprezados\.

MFS\-19941

__RN65__

Se o status da obrigação for fechada e o usuário acionar a funcionalidade Upload, exibir a msg: Só é permitido usar esta funcionalidade se o Status da Apuração for “Realizada” ou “Reaberta”\.

MFS\-19941

__RN66__

Cada arquivo deve o tamanho máximo de 2Mb, caso contrário exibir a seguinte msg: “O arquivo selecionado ultrapassou o tamanho máximo de 2Mb”\.

MFS\-19941

