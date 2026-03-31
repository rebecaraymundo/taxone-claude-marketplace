# MTZ-Funcionalidade_Upload

- **Fonte:** MTZ-Funcionalidade_Upload.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 39 KB

---

<a id="OLE_LINK3"></a><a id="OLE_LINK4"></a>Fucionalidade Upload –<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a> Dentro das Telas de Apuração PIS/PASEP  e Apuração COFINS

\(EFD\- Escrituração Fiscal Digital das Contribuições\)

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3619

Ajustes do crédito de PIS/PASEP e COFINS \(Registros M220/M620\)

Será criada a funcionalidade Upload para carregar as informações dos ajustes do crédito de PIS/PASEP e COFINS \(Registros M220/M620\)

25/05/2012

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

