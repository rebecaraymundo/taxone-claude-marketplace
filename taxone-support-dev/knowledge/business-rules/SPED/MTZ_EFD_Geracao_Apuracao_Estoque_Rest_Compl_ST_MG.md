# MTZ_EFD_Geracao_Apuracao_Estoque_Rest_Compl_ST_MG

> Fonte: MTZ_EFD_Geracao_Apuracao_Estoque_Rest_Compl_ST_MG.docx




THOMSON REUTERS

Módulo Sped Fiscal

Geração do arquivo digital – Portaria 165 – 27/11/2018
Geração da Apuração de Estoque, Restituição e Complementação ST - MG



Localização: Menu Sped, Módulo EFD - Escrituração Fiscal Digital, item Pré-Geração à Ressarcimento ICMS-ST – (Específico MG) à Geração do Arquivo Digital (Portaria 165/2018)


DOCUMENTO DE REQUISITO







Sumário

1.	Parâmetros da Tela	3
2.	Recuperação dos Dados do arquivo 4 – Restituição ST	4
3.	Geração do arquivo 4 – Restituição ST	4
4.	Recuperação dos Dados do arquivo 5 – Complementação e/ou Restituição ST	7
5.	Geração do arquivo 5 – Complementação e/ou Restituição ST	7















## Parâmetros da Tela


Esta geração foi criada com o objetivo de gerar o arquivo digital da Apuração de Estoque, Restituição e Complementação ST – MG, conforme definições da Portaria SRE n° 165, de 27 de novembro de 2018. Conforme alinhado com o PM (Marcos de Paula), será criada a funcionalidade para a geração dessas informações em excel, mas somente serão geradas as finalidades 4 (“4 – Restituição ST (ART. 23 – ANEXO XV)”) e 5 (“5 – Complementação e/ou Restituição ST (ARTS. 31-A a 31-I DO ANEXO XV)”).

A geração do arquivo digital tem como pré-requisito a carga da SAFX296, que pode ser feita através da pré-geração do ressarcimento ICMS-ST/MG ou através da importação ou manutenção da SAFX296.

Serão gerados dois arquivos no formato excel, um arquivo para a finalidade 4 – Restituição ST e outro arquivo para a finalidade 5 – Complementação e/ou Restituição ST.


Parâmetros da geração:




## Recuperação dos Dados do arquivo 4 – Restituição ST



Este processo irá recuperar as informações da tabela de Informações Complementares das Operações Sujeitas ao ST (SAFX296) e da tabela de cadastro do produto (SAFX2013), que atendam aos seguintes critérios:

Empresa igual a empresa selecionada na geração;

Estabelecimento igual ao estabelecimento selecionado na geração;

A data fiscal da nota deve ser referente ao período (mês/ano) informado em tela;

O Código Motivo (Saídas) deve ser igual “MG200”;

Os registros recuperados serão agrupados por empresa, estabelecimento e produto, sendo assim as suas quantidades e valores serão totalizados.


## Geração do arquivo 4 – Restituição ST


[MFS570956] Inclusão da geração do arquivo único por finalidade

[MFS570966] Inclusão da geração do arquivo particionados por operações


Regra de criação do nome do arquivo em excel:

Se o parâmetro “Gerar Arquivo Único por Finalidade” estiver desmarcado
Se o parâmetro “Gerar arquivo particionado por operações” estiver marcardo o arquivo deve ser gerado particionado por Operações.
As operações estão parametrizadas no Menu: Parâmetros >> Ressarcimento ICMS-ST >> Operações >> CFOP / Natureza de Operação.
Identificar as operações parametrizadas no parâmetro acima e gerar os aquivos por tipo de operação.

Num_processo_Estab_MMAAAA_Fin4, onde:
Num_processo: representa o número do processo da geração.
Estab: representa o código do estabelecimento da geração.
MMAAAA: representa o período da geração.
Fin4: representa o tipo de arquivo que está sendo gerado, 4 – Restituição ST.
Ex:00000001_001MG_012023_Fin4.XLS

Quando a geração do arquivo ocorrer particionado por tipo de operação, necessário acrescentar o código de operação na  nomenclatura do arquivo gerado. EX:  00000001_001MG_012023_Fin4_767.XLS


Se o parâmetro “Gerar Arquivo Único por Finalidade” estiver marcado
Se o parâmetro “Gerar arquivo particionado por operações” estiver marcardo o arquivo deve ser gerado particionado por Operações.
As operações estão parametrizadas no Menu: Parâmetros >> Ressarcimento ICMS-ST >> Operações >> CFOP / Natureza de Operação.
Identificar as operações parametrizadas no parâmetro acima e gerar os aquivos por tipo de operação.

Num_processo_MMAAAA_Fin4, onde:
Num_processo: representa o número do processo da geração.
MMAAAA: representa o período da geração.
Fin4: representa o tipo de arquivo que está sendo gerado, 4 – Restituição ST.
Ex: 00000001_012023_Fin4.XLS

Quando a geração do arquivo ocorrer particionado por tipo de operação, necessário acrescentar o código de operação na nomenclatura do arquivo gerado. EX:  00000001_012023_Fin4_767.XLS


Layout do arquivo em excel:



## Recuperação dos Dados do arquivo 5 – Complementação e/ou Restituição ST



Este processo irá recuperar as informações da tabela de Informações Complementares das Operações Sujeitas ao ST (SAFX296) e da tabela de cadastro do produto (SAFX2013), que atendam aos seguintes critérios:

Empresa igual a empresa selecionada na geração;

Estabelecimento igual ao estabelecimento selecionado na geração;

A data fiscal da nota deve ser referente ao período (mês/ano) informado em tela;

O Código Motivo (Saídas) deve ser igual “MG100” ou “MG300”;

Os registros recuperados serão agrupados por empresa, estabelecimento e produto, sendo assim as suas quantidades e valores serão totalizados.


## Geração do arquivo 5 – Complementação e/ou Restituição ST


[MFS570956] Inclusão da geração do arquivo único por finalidade

Regra de criação do nome do arquivo em excel:

Se o parâmetro “Gerar Arquivo Único por Finalidade” estiver desmarcado
Num_processo_Estab_MMAAAA_Fin5, onde:
Num_processo: representa o número do processo da geração.
Estab: representa o código do estabelecimento da geração.
MMAAAA: representa o período da geração.
Fin5: representa o tipo de arquivo que está sendo gerado, 5 – Complementação e/ou Restituição ST.

Se o parâmetro “Gerar Arquivo Único por Finalidade” estiver marcado
Num_processo_MMAAAA_Fin5, onde:
Num_processo: representa o número do processo da geração.
MMAAAA: representa o período da geração.
Fin5: representa o tipo de arquivo que está sendo gerado, 5 – Complementação e/ou Restituição ST.
Ex: 00000001_012023_Fin5.XLS

Layout do arquivo em excel:




| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS422889 | Andréa Rocha | Criação da geração do arquivo digital da Apuração de Estoque, Restituição e Complementação ST - MG, conforme definições da  Portaria 165 – 27/11/2018. | 27/02/2023 (criação do documento) |
| MFS570956 | Andréa Rocha | Inclusão de um parâmetro para definir se será gerado um arquivo único para os estabelecimentos selecionados para a geração. | 03/10/2023 |
| MFS570966 | Graciela Soares | Inclusão de um parâmetro para gerar um arquivo particionado de Restituição ST, quando a opção sleecionada for igual a “4”, ativar o check-box para gerar arquivos separados considerando a parametrização de Operações. | 20/05/2024 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Período | Data | S | S |  | Neste campo o usuário informará o mês/ano do período da geração | MFS422889 |
| Finalidade | Radiobutton | S | S | Opção = Todos | Este campo é do tipo Radiobutton, com as seguintes opções: - Todos; - 4 – Restituição ST; - 5 – Complementação e/ou Restituição ST | MFS422889 |
| Gerar arquivo particionado por operações | Radiobutton | S | N |  | Este campo é do tipo Checkbox. Default = desmarcado Habilitar campo apenas quando a opção do campo Finalidade for igual a “4” | MFS570966 |
|  |  |  |  |  |  |  |
| Gerar Arquivo Único por Finalidade | Radiobutton | S | N |  | Este campo é do tipo Checkbox. Default = desmarcado | MFS570956 |
| Estabelecimentos | Alfanumérico | S | S |  | Neste campo será exibida a lista dos estabelecimentos da Empresa do login para seleção do usuário e que seja da UF = MG.  Deverá ter a opção de selecionar todos os estabelecimentos. | MFS422889 |


| CD_SPED | Código SPED/Sintegra  Campo alfanumérico de 60 posições.  Preencher com o campo 13-Código do Produto da SAFX296. |
| --- | --- |
| CD_NCM | Código NCM  Campo alfanumérico de 8 posições.  Preencher com o campo 05-Código NBM da SAFX2013. |
| CD_EAN13 | Código EAN-13  Campo alfanumérico de 13 posições.  Preencher com o campo 40-Código de Barras da SAFX2013. |
| DS_PRODMERC | Descrição do produto/mercadoria NCM  Campo alfanumérico de 80 posições.  Preencher com o campo 04-Descrição do Produto da SAFX2013. |
| TP_UNIDADE | Tipo de Unidade  Campo alfanumérico de 30 posições.  Preencher com o campo 20-Unidade de Medida Padrão da SAFX2013. |
| QT_PROD_FGP | Quantidade  Campo numérico de 15 posições, sendo 4 casas decimais.  Preencher com o campo 16-Quantidade Convertida da SAFX296. |
| VR_ICMS_FGP_OPC | Valor ICMS OP. Próprias  Campo numérico de 15 posições, sendo 2 casas decimais .  Preencher com o campo 26-Valor Unitário ICMS Estoque Conv. (Saídas) * campo 16-Quantidade Convertida da SAFX296.  Obs.: O resultado do cálculo deve ser arredondado em 2 casas decimais. |
| VR_ICMS_FGP_STR | Valor ICMS-ST  Campo numérico de 15 posições, sendo 2 casas decimais.  Preencher com o campo 29-Valor Unitário ICMS-ST Conv. Rest. (Saídas) da SAFX296 * campo 16-Quantidade Convertida da SAFX296.  Obs.: O resultado do cálculo deve ser arredondado em 2 casas decimais. |
| VR_FEM_FGP_REST | Valor FEM  Campo numérico de 15 posições, sendo 2 casas decimais.  Preencher com o campo 30-Valor Unitário FCP-ST Conv. Rest. (Saídas) da SAFX296 * campo 16-Quantidade Convertida da SAFX296.  Obs.: O resultado do cálculo deve ser arredondado em 2 casas decimais. |


| CD_SPED | Código SPED/Sintegra  Campo alfanumérico de 60 posições.  Preencher com o campo 13-Código do Produto da SAFX296. |
| --- | --- |
| CD_NCM | Código NCM  Campo alfanumérico de 8 posições.  Preencher com o campo 05-Código NBM da SAFX2013. |
| CD_EAN13 | Código EAN-13  Campo alfanumérico de 13 posições.  O contéudo deve ser truncado em 13 posições.  Preencher com o campo 40-Código de Barras da SAFX2013. |
| DS_PRODMERC | Descrição do produto/mercadoria NCM  Campo alfanumérico de 80 posições.  Preencher com o campo 04-Descrição do Produto da SAFX2013. |
| TP_UNIDADE | Tipo de Unidade  Campo alfanumérico de 30 posições.  Preencher com o campo 20-Unidade de Medida Padrão da SAFX2013. |
| QT_PROD_ST_COMP | Quantidade - Complementação  Campo numérico de 15 posições, sendo 4 casas decimais.  Se campo 31-Valor Unitário ICMS-ST Conv. Compl. (Saídas) da SAFX296  for maior que zero      Preencher com o campo 16-Quantidade Convertida da SAFX296. |
| VR_ICMS_ST_COMP | Valor ICMS-ST - Complementação  Campo numérico de 15 posições, sendo 2 casas decimais.  Preencher com o campo 31-Valor Unitário ICMS-ST Conv. Compl. (Saídas) da SAFX296  * campo 16-Quantidade Convertida da SAFX296.  Obs.: O resultado do cálculo deve ser arredondado em 2 casas decimais. |
| VR_FEM_ST_COMP | Valor do FEM - Complementação  Campo numérico de 15 posições, sendo 2 casas decimais.  Preencher com o campo 32-Valor Unitário FCP-ST Conv. Compl. (Saídas) da SAFX296  * campo 16-Quantidade Convertida da SAFX296.  Obs.: O resultado do cálculo deve ser arredondado em 2 casas decimais. |
| QT_PROD_ST_REST | Quantidade - Restituição  Campo numérico de 15 posições, sendo 2 casas decimais.  Se o campo 29-Valor Unitário ICMS-ST Conv. Rest. (Saídas) da SAFX296 for maior que zero       Preencher com o campo 16-Quantidade Convertida da SAFX296. |
| VR_ICMS_ST_RET | Valor do ICMS-ST - Restituição  Campo numérico de 15 posições, sendo 2 casas decimais.  Preencher com o campo 29-Valor Unitário ICMS-ST Conv. Rest. (Saídas) da SAFX296 * campo 16-Quantidade Convertida da SAFX296.  Obs.: O resultado do cálculo deve ser arredondado em 2 casas decimais. |
| VR_FEM_ST_REST | Valor do FEM - Restituição  Campo numérico de 15 posições, sendo 2 casas decimais.  Preencher com o campo 30-Valor Unitário FCP-ST Conv. Rest. (Saídas) da SAFX296 * campo 16-Quantidade Convertida da SAFX296.  Obs.: O resultado do cálculo deve ser arredondado em 2 casas decimais. |
