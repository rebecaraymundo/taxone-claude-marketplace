# MTZ-EFD_Contribuicoes_Financeiras_Assemelhadas-Geracao_do_Meio_Magnetico

> Fonte: MTZ-EFD_Contribuicoes_Financeiras_Assemelhadas-Geracao_do_Meio_Magnetico.docx


## EFD - Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas - Geração do Meio Magnético





DOCUMENTO DE REQUISITO


Relação de Registros que serão gerados

Bloco 0 - Abertura, Identificação e Referências

Registro 0000 – Abertura do Arquivo Digital e Identificação da Pessoa Jurídica



Registro 0001 – Abertura Bloco 0



Registro 0100 – Dados do Contabilista



Registro 0110 – Regimes de Apuração da Contribuição Social



Registro 0140 – Tabela de Cadastro do Estabelecimento



Registro 0500 – Plano de Contas Contábeis



Registro 0990 – Encerramento do Bloco 0




Bloco A - Documentos Fiscais - Serviços (ISS)

Registro A001 – Abertura Bloco A



Registro A990 – Encerramento do Bloco A



Bloco C - Documentos Fiscais I – Mercadorias (ICMS/IPI)

Registro C001 – Abertura Bloco C



Registro C990 – Encerramento do Bloco C



Bloco D - Documentos Fiscais II – Serviços (ICMS)

Registro D001 – Abertura Bloco D



Registro D990 – Encerramento do Bloco D



Bloco F - Demais Documentos e Operações

Registro F001 – Abertura Bloco F


Registro F600 – Contribuição Retida na Fonte



Registro F700 – Deduções Diversas




Registro F990 – Encerramento do Bloco F



Bloco 1 - Complemento da Escrituração – Controle de Saldos de Créditos e de Retenções, Operações Extemporâneas e Outras Informações

Registro I001 – Abertura Bloco I



Registro I100 – Consolidação das Operações do Período




Registro I200 – Composição das Receitas, Deduções e/ou Exclusões do Período



Registro I300 – Complemento das Operações – Detalhamento das Receitas, Deduções e/ou Exclusões do Período



Registro I990 – Encerramento do Bloco I



Bloco M - Apuração da Contribuição e Crédito de PIS/PASEP e da COFINS

Registro M001 – Abertura Bloco M



Registro M200 – Consolidação da Contribuição para o PIS/PASEP do Período
















Registro  M205 – Contribuição para o PIS/PASEP a recolher detalhamento por código de receita



Registro M210 – Detalhamento da Contribuição para o PIS/PASEP do Período (Período de apuração anterior a 01/2019)



Alteração para acrescentar os campos VL_AJUS_ACRES_BC_PIS, VL_AJUS_REDUC_BC_PIS e VL_BC_CONT_AJUS através da MFS-25094:

Registro M210 – Detalhamento da Contribuição para o PIS/PASEP do Período (Período de apuração 01/2019)



Alteração para incluir o registro M215 através da MFS25094:
Registro M215 – Ajustes da Base de Cálculo do PIS/Pasep Apurada (Período de apuração 01/2019)




Registro M225 – Detalhamento dos Ajustes da Contribuição do PIS/PASEP Apurado


Registro M400 – Consolidação da Contribuição para o PIS/PASEP do Período



Registro M410 – Consolidação da Contribuição para o PIS/PASEP do Período



Registro M600 – Consolidação da Contribuição para o PIS/PASEP do Período



















- Registro M605 – COFINS a recolher – Detalhamento por código de receita











Registro M610 – Detalhamento da Contribuição para o PIS/PASEP do Período (Período de apuração anterior a 01/2019)



Alteração para acrescentar os campos VL_AJUS_ACRES_BC_PIS, VL_AJUS_REDUC_BC_PIS e VL_BC_CONT_AJUS através da MFS-25094:

Registro M610 – Detalhamento da Contribuição para o PIS/PASEP do Período (Período de apuração 01/2019)



Alteração para incluir o registro M615 através da MFS25094:
Registro M615 – Ajustes da Base de Cálculo da Cofins Apurada (Período de apuração 01/2019)







Registro M625 – Detalhamento dos Ajustes da Contribuição da COFINS Apurada


Registro M800 – Consolidação da Contribuição para o PIS/PASEP do Período



Registro M810 – Consolidação da Contribuição para o PIS/PASEP do Período



Registro M990 – Encerramento do Bloco M



Bloco P - Apuração da Contribuição Previdenciária sobre a Receita Bruta

Registro P001 – Abertura Bloco P







Registro P990 – Encerramento do Bloco P



Bloco 1 - Complemento da Escrituração – Controle de Saldos de Créditos e de Retenções, Operações Extemporâneas e Outras Informações

Registro 1001 – Abertura Bloco I


Alteração para incluir o registro 1050 através da MFS-25094 :

Registro 1050 – Detalhamento de Ajustes de Base de Cálculo – Valores Extra Escrituração (Período de apuração 01/2019)





Registro 1300 – Controle dos Valores Retidos na Fonte – PIS/Pasep


Registro 1700 – Controle dos Valores Retidos na Fonte – COFINS


Registro 1990 – Encerramento do Bloco P




Bloco 9 - Controle e Encerramento do Arquivo Digital

Considerações deste modelo:


Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:


Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:



| DR | DR | Nome | Descrição | Descrição |
| --- | --- | --- | --- | --- |
| OS3810-D | OS3810-D | EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas – Geração do Meio Magnético | Essa OS tem por objetivo permitir a geração do meio magnético do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas. | Essa OS tem por objetivo permitir a geração do meio magnético do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas. |
| OS3810-E | OS3810-E | EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas – Geração do Meio Magnético | Ajustes nas regras da apuração para contemplar valores de retenção e dedução. | Ajustes nas regras da apuração para contemplar valores de retenção e dedução. |
| OS4316-D | OS4316-D | EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas – Geração do Meio Magnético | Esta OS tem por objetivo incluir na geração os registros M225 - Detalhamento dos Ajustes da Contribuição para o Pis/Pasep Apurada e M625 - Detalhamento dos Ajustes da Cofins Apurada. | Esta OS tem por objetivo incluir na geração os registros M225 - Detalhamento dos Ajustes da Contribuição para o Pis/Pasep Apurada e M625 - Detalhamento dos Ajustes da Cofins Apurada. |
| MFS25094 | MFS25094 | Andréa Rocha | Inclusão da geração dos registros 1050, M215 e M615 e alteração da geração dos registros M210 e M610. | Inclusão da geração dos registros 1050, M215 e M615 e alteração da geração dos registros M210 e M610. |
| Cód. | Descrição | Descrição | Descrição | DR |
| RN01 | Deverá ser criada uma tela chamada “Geração do Meio Magnético”.   Essa tela será responsável pela geração do meio magnético (arquivo TXT) do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas.  O submenu “Geração do Meio Magnético” deverá ser disponibilizado como o último menu “Obrigações”. | Deverá ser criada uma tela chamada “Geração do Meio Magnético”.   Essa tela será responsável pela geração do meio magnético (arquivo TXT) do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas.  O submenu “Geração do Meio Magnético” deverá ser disponibilizado como o último menu “Obrigações”. | Deverá ser criada uma tela chamada “Geração do Meio Magnético”.   Essa tela será responsável pela geração do meio magnético (arquivo TXT) do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas.  O submenu “Geração do Meio Magnético” deverá ser disponibilizado como o último menu “Obrigações”. | OS3810-D |
| RN02 | EXCLUÍDA – OSXPTO estas informações foram retiradas e constam no MTZ - EFD Contribuições Financeira e Assemelhadas - Geracao do Meio Magnético Tela, referente a OS 4498.  Serão disponibilizados na tela os seguintes campos:  Estabelecimento: nesse campo, será exibido o Estabelecimento que foi gerado a apuração. Essa informação deverá ser recuperada da tela Apuração PIS (menu: Obrigações >> Manutenção >> Apuração PIS/PASEP) e Apuração COFINS (menu: Obrigações >> Manutenção >> Apuração PIS/PASEP) do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas. Obrigação Fiscal: nesse campo, será exibida a informação “EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas – PIS/PASEP e COFINS”. Período: nesse campo será exibido o periodo da apuração do PIS/PASEP e da COFINS. Essa informação será recuperada da tela Apuração PIS (menu: Obrigações >> Manutenção >> Apuração PIS/PASEP) e Apuração COFINS (menu: Obrigações >> Manutenção >> Apuração PIS/PASEP) do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas. Layout: nesse campo será exibido o layout que foi gerado a apuração. Essa informação será recuperada do campo “Leiaute” da tela Obrigações >> Bloco I (Operações dos Período) >> Geração dos Registros do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas. Gravação do Arquivo Magnético no Servidor: nesse campo o usuário poderá informar se o arquivo gerado será gravado no servidor ou não. Esse campo por default será exibido desmarcado.  Nome: nesse campo, o usuário irá informar o nome do arquivo. Diretório: nesse campo, o usuário poderá selecionar o diretório para gravação. Caso o parâmetro “Gravação do Arquivo Magnético no Servidor” esse campo deverá ser informado como “ARQ_PISCOF_DIR”.  O campo “Situação” não deverá ser incluído nessa tela. | EXCLUÍDA – OSXPTO estas informações foram retiradas e constam no MTZ - EFD Contribuições Financeira e Assemelhadas - Geracao do Meio Magnético Tela, referente a OS 4498.  Serão disponibilizados na tela os seguintes campos:  Estabelecimento: nesse campo, será exibido o Estabelecimento que foi gerado a apuração. Essa informação deverá ser recuperada da tela Apuração PIS (menu: Obrigações >> Manutenção >> Apuração PIS/PASEP) e Apuração COFINS (menu: Obrigações >> Manutenção >> Apuração PIS/PASEP) do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas. Obrigação Fiscal: nesse campo, será exibida a informação “EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas – PIS/PASEP e COFINS”. Período: nesse campo será exibido o periodo da apuração do PIS/PASEP e da COFINS. Essa informação será recuperada da tela Apuração PIS (menu: Obrigações >> Manutenção >> Apuração PIS/PASEP) e Apuração COFINS (menu: Obrigações >> Manutenção >> Apuração PIS/PASEP) do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas. Layout: nesse campo será exibido o layout que foi gerado a apuração. Essa informação será recuperada do campo “Leiaute” da tela Obrigações >> Bloco I (Operações dos Período) >> Geração dos Registros do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas. Gravação do Arquivo Magnético no Servidor: nesse campo o usuário poderá informar se o arquivo gerado será gravado no servidor ou não. Esse campo por default será exibido desmarcado.  Nome: nesse campo, o usuário irá informar o nome do arquivo. Diretório: nesse campo, o usuário poderá selecionar o diretório para gravação. Caso o parâmetro “Gravação do Arquivo Magnético no Servidor” esse campo deverá ser informado como “ARQ_PISCOF_DIR”.  O campo “Situação” não deverá ser incluído nessa tela. | EXCLUÍDA – OSXPTO estas informações foram retiradas e constam no MTZ - EFD Contribuições Financeira e Assemelhadas - Geracao do Meio Magnético Tela, referente a OS 4498.  Serão disponibilizados na tela os seguintes campos:  Estabelecimento: nesse campo, será exibido o Estabelecimento que foi gerado a apuração. Essa informação deverá ser recuperada da tela Apuração PIS (menu: Obrigações >> Manutenção >> Apuração PIS/PASEP) e Apuração COFINS (menu: Obrigações >> Manutenção >> Apuração PIS/PASEP) do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas. Obrigação Fiscal: nesse campo, será exibida a informação “EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas – PIS/PASEP e COFINS”. Período: nesse campo será exibido o periodo da apuração do PIS/PASEP e da COFINS. Essa informação será recuperada da tela Apuração PIS (menu: Obrigações >> Manutenção >> Apuração PIS/PASEP) e Apuração COFINS (menu: Obrigações >> Manutenção >> Apuração PIS/PASEP) do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas. Layout: nesse campo será exibido o layout que foi gerado a apuração. Essa informação será recuperada do campo “Leiaute” da tela Obrigações >> Bloco I (Operações dos Período) >> Geração dos Registros do módulo EFD – Escrituração Fiscal Digital das Contribuições Financeiras e Assemelhadas. Gravação do Arquivo Magnético no Servidor: nesse campo o usuário poderá informar se o arquivo gerado será gravado no servidor ou não. Esse campo por default será exibido desmarcado.  Nome: nesse campo, o usuário irá informar o nome do arquivo. Diretório: nesse campo, o usuário poderá selecionar o diretório para gravação. Caso o parâmetro “Gravação do Arquivo Magnético no Servidor” esse campo deverá ser informado como “ARQ_PISCOF_DIR”.  O campo “Situação” não deverá ser incluído nessa tela. | OS3810-D |


| RNG-0000 | Deve ser gerado um registro 0000 por arquivo, com os dados de identificação do estabelecimento.  OBS: Na geração centralizada (Parâmetros > Preliminares > Centralização de Escrituração, deve-se utilizar os dados do Estabelecimento centralizador.  Registro de nível 0, ocorrência de 1 por arquivo e obrigatório. | OS3810-B |
| --- | --- | --- |
| RN0000-02 | Campo COD_VER  Gerar com a informação 003, se o leiaute utilizado (na tela de Geração dos Registros) for EPC201 | OS3810-B |
| RN0000-03 | Campo TIPO_ESCRIT:  Verificar o parâmetro “Tipo de Escrituração” informado na tela de geração:  Se Tipo de Escrituração = “Original”       Gravar “0” Senão                   Gravar “1” (Retificadora) | OS3810-B |
| RN0000-04 | Campo IND_SIT_ESP:  Se a data de início de atividade (campo DAT_ INI_ATIVIDADE da tabela estabelecimento) estiver entre a data inicial e final de geração do arquivo = ‘0’  Se a data de cisão (campo DATA_CISAO da tabela estabelecimento) estiver entre a data inicial e final da geração do arquivo ou se o dia inicial for diferente de “01” e a data da cisão for igual a data inicial de geração “-1”,preencher com  ‘1’  Se a data de fusão (campo DATA_FUSAO da tabela estabelecimento) estiver entre a data inicial e final da geração do arquivo ou se o dia inicial for diferente de “01” e a data da fusão for igual a data inicial de geração “-1”, igual = ‘2’  Se a data de incorporação (campo DATA_INCORPORACAO da tabela estabelecimento) estiver entre a data inicial e final da geração do arquivo ou se o dia inicial for diferente de “01” e a data da incorporação for igual a data inicial de geração “-1”, igual = ‘3’  Se a data de encerramento (campo DT_ENCERRAMENTO da tabela estabelecimento) estiver entre a data inicial e final de geração do arquivo, preencher com “4”. | OS3810-B |
| RN0000-05 | Campo NUM_REC_ANTERIOR:  Este campo deve ser preenchido com o conteúdo do campo Número do Recibo da Escrituração Anterior, informado na tela de geração. | OS3810-B |
| RN0000-06 | Campo DT_INI:  Este campo deve ser preenchido com o dia, mês e ano inicial através do parâmetro Data Inicial, informado na tela de geração. | OS3810-B |
| RN0000-07 | Campo DT_FIN:  Este campo deve ser preenchido com o dia, mês e ano final através do parâmetro Data Final, informado na tela de geração. | OS3810-B |
| RN0000-13 | Campo IND_NAT_PJ:  Esse campo deve ser preenchido de acordo com as opções selecionadas no campo Natureza de pessoa jurídica da tela de manutenção do Estabelecimento, localizado no módulo: Básicos  Parâmetros  Preliminares  Estabelecimento/Companhia, com o seguinte critério:  Se a opção selecionada for igual ‘’Sociedade empresária em geral’’, gravar ‘’00’’ Se a opção selecionada for igual ‘’Sociedade cooperativa’’, gravar ‘’01’’ Se a opção selecionada for igual ‘’Entidade sujeita ao PIS/Pasep exclusivamente Folha de Salários’’, gravar ‘’02’’. | OS3810-B |
| RN0000-14 | Campo IND_ATIV:  Esse campo deve ser preenchido de acordo com as opções selecionadas no campo Tipo de Atividade de pessoa jurídica da tela de manutenção do Estabelecimento, localizado no módulo: Básicos Parâmetros  Preliminares  Estabelecimento/Companhia, com o seguinte critério: Se a opção selecionada for igual ‘Industrial ou equiparado a industrial’’, gravar ‘’0’’ Se a opção selecionada for igual ‘’Prestador de serviços’’, gravar ‘’1’’ Se a opção selecionada for igual “’Atividade de comércio”, gravar ‘’2’’ Se a opção selecionada for igual “’Atividade financeira”, gravar “3’’ Se a opção selecionada for igual ‘”Atividade imobiliária”, gravar “4’’ Se a opção selecionada for igual “’Outros”, gravar “9’’ | OS3810-B |


| RNG-0001 | Deve ser gerado um registro 0001 por arquivo.  Registro de nível 1, ocorrência de 1 por arquivo e obrigatório. | OS3810-B |
| --- | --- | --- |
| RN0001-02 | Campo IND_MOV  Gerar fixo “0”. | OS3810-B |


| RN0100 | Um registro por arquivo. Conterá os dados do contabilista responsável, parametrizado no módulo EFD-PIS/COFINS, menu: Sped → EFD – Escrituração Fiscal Digital - PIS/PASEP-COFINS → Parâmetros  Dados Iniciais.  OBS: Na geração centralizada, deve-se utilizar o contabilista parametrizado para o Estabelecimento centralizador. | OS3810-B |
| --- | --- | --- |
| RN0100-03 RN0100-05 | Quanto aos campos 03 e 05 (CNPJ/CPF), preencher apenas um deles, dependendo do conteúdo do campo “CPF/CNPJ” do contabilista. Se for um CPF, gravar o campo 03, e se for um CNPJ, gravar o campo 05. | OS3810-B |
| RN0100-14 | Campo COD_MUN:  Concatenação do Código da UF (campo COD_UF da tabela MUNICIPIO) + Código do município do contabilista responsável (para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve-se completar com zeros à esquerda quando necessário). | OS3810-B |


| RNG-0110 | Deve ser gerado um registro 0001 por arquivo.  Registro de nível 2, ocorrência de 1 por arquivo e obrigatório. | OS3810-B |
| --- | --- | --- |
| RN0110-02 | Campo COD_INC_TRIB:  Gerar com “2”. | OS3810-B |
| RN0110-03 | Campo IND_APRO_CRED:  Gerar nulo (“||”). | OS3810-B |
| RN0110-04 | Campo COD_TIPO_CONT:  Gerar com “1”. | OS3810-B |
| RN0110-05 | Campo IND_REG_CUM:  Gerar nulo (“||”). | OS3810-B |


| RN0140 | Na geração centralizada, será gerado um registro para o estabelecimento centralizador, e um registro para cada estabelecimento centralizado.  Se o estabelecimento centralizado não possuir movimento e/ou estejam encerrados (caso o campo Data Encerramento do cadastro do Estabelecimento seja anterior à data de geração do EFD-Contribuições Financeira/Assemelhada) não devem ser gerados registros 0140 para esse estabelecimento.  Para o estabelecimento centralizador que possua ou não movimento sempre deve ser gerado o registro 0140 no período de geração do EFD-Contribuições Financeira/Assemelhada.  Registro de nível 2, ocorrência de vários por arquivo e obrigatório. | OS3810-B |
| --- | --- | --- |
| RN0140-01 | Registro 0140 – 01 – REG:  Deverá ser gravado no campo 01 – REG o texto fixo “0140”. | OS3810-B |
| RN0140-02 | Registro 0140 – 02 – COD_EST:  Deverá ser gravado no campo 02 – COD_EST o Código do Estabelecimento. Essa informação deverá ser recuperada do campo “Código Estabelecimento” do cadastro de Empresa/Estabelecimento (menu: Preliminares >> Empresa/Estabelecimento) do módulo Parâmetros. | OS3810-B |
| RN0140-03 | Registro 0140 – 03 – NOME:  Deverá ser gravado no campo 03 – NOME a Razão Social do Estabelecimento. Essa informação deverá ser recuperada do campo “Razão Social” do cadastro de Empresa/Estabelecimento (menu: Preliminares >> Empresa/Estabelecimento) do módulo Parâmetros. | OS3810-B |
| RN0140-04 | Registro 0140 – 04 – CNPJ:  Deverá ser gravado no campo 04 – CNPJ a Razão Social do Estabelecimento. Essa informação deverá ser recuperada do campo “CNPJ” do cadastro de Empresa/Estabelecimento (menu: Preliminares >> Empresa/Estabelecimento) do módulo Parâmetros. | OS3810-B |
| RN0140-05 | Registro 0140 – 05 – UF:  Deverá ser gravado no campo 05 – UF o Código do Estado (Unidade Federativa) do Estabelecimento. Essa informação deverá ser recuperada do campo “UF” do cadastro de Empresa/Estabelecimento (menu: Preliminares >> Empresa/Estabelecimento) do módulo Parâmetros. | OS3810-B |
| RN0140-06 | Registro 0140 – 06 – IE:  Deverá ser gravado no campo 06 – IE a Inscrição Estadual do Estabelecimento. Essa informação deverá ser recuperada do campo “Inscrição Estadual” do cadastro de Inscrição Estadual (menu: Preliminares >> Inscrições Estaduais) do módulo Parâmetros.  Caso a Inscrição estadual do Estabelecimento possua o conteúdo = “ISENTO”, gravar o campo sem informação “||”. | OS3810-B |
| RN0140-07 | Registro 0140 – 07 – COD_MUN:  Deverá ser gravado no campo 07 – COD_MUN o Código do Município do Estabelecimento. Essa informação deverá ser recuperada da concatenação dos campos Código UF + Código Município. Para fazer a concatenação, o código do município deve ter 5 dígitos, por isso, deve-se completar com zeros a esquerda quando necessário. | OS3810-B |
| RN0140-08 | Registro 0140 – 08 – IM:  Deverá ser gravado no campo 08 – IM a Inscrição Municipal do Estabelecimento. Essa informação deverá ser recuperada do campo “Inscrição Municipal” do cadastro de Estabelecimento (menu: Preliminares >> Empresa/Estabelecimento) do módulo Parâmetros. | OS3810-B |
| RN0140-09 | Registro 0140 – 09 – SUFRAMA:  Deverá ser gravado no campo 09 – SUFRAMA o Número de Inscrição do Estabelecimento na SUFRAMA. Essa informação deverá ser recuperada do campo “Inscrição SUFRAMA” do cadastro de Estabelecimento (menu: Preliminares >> Empresa/Estabelecimento) do módulo Parâmetros. | OS3810-B |


| RNG-0500 | Este registro deve ser gerado a partir das contas contábeis referenciadas nos diversos registros da EFD-PIS/COFINS.  Gravar um registro 0500 para cada conta contábil (campo COD_CTA constante na movimentação do período)  O registro da SAFX2002 (Tabela do Plano de Contas) a ser considerado, deve ser sempre o de maior data de validade, que seja <= a data final do período.  OBS1: Na geração centralizada, gravar as observações envolvidas nos documentos de todos os Estabelecimentos. Nesse caso, os registros 0500 serão gerados abaixo do registro 0140 do estabelecimento centralizador.  Registro de nível 2, ocorrência de vários por arquivo e obrigatório se houver. | OS3810-B |
| --- | --- | --- |
| RN0500-02 | Campo DT_ALT:  Campo Data Início/Inclusão/Alteração da SAFX2002. | OS3810-B |
| RN0500-03 | Campo COD_ NAT_CC:  Este campo deve ser preenchido de acordo com o conteúdo do campo “07-Indicador de Natureza” da SAFX2002, da seguinte forma:  Se Indicador = 0 (Compensação)     gravar 05 (Contas de Compensação);  Se Indicador = 1 (Ativo)      gravar 01 (Contas de Ativo);  Se Indicador = 2 (Passivo)      gravar 02 (Contas de Passivo);  Se Indicador = 3 (Despesa), 4 (Receita) ou 8 (Custo)       gravar 04 (Contas de Resultado);  Se Indicador = 7 (Patrimônio Líquido)      gravar 03 (Patrimônio Líquido);  Se Indicador = 5 (Mutações Ativas), 6 (Mutações  Passivas) ou 9 (Outros)      gravar 09 (Outras); | OS3810-B |
| RN0500-04 | Campo IND_CTA:  Campo Indicador de Conta da SAFX2002. | OS3810-B |
| RN0500-05 | Campo NÍVEL:  Campo Nível da SAFX2002. | OS3810-B |
| RN0500-06 | Campo COD_CTA:  Campo Código da Conta da SAFX2002. | OS3810-B |
| RN0500-07 | Campo NOME_CTA:  Campo Descrição da Conta da SAFX2002. | OS3810-B |
| RN0500-08 | Campo COD_CTA_REF:  Buscar na tabela SAFX2101 o código da conta referencial associada ao código da conta gerada no campo 06. Se existir mais de uma conta referencial (ou seja, mais de um registro na SAFX2101) para uma mesma conta contábil, gerar um registro 0500 para cada conta referencial encontrada.  Somente deverá ser gravada a Conta Referencial parametrizada pela Empresa (DE/PARA) de acordo com a entidade responsável pelo Plano, ou seja, Receita Federal, SUSEP ou COSIF, dessa forma, a rotina deverá verificar a qual Plano a Conta Referencial pertence.  Se a Conta Referencial pertencer a determinado Plano (Entidade) cujo Estabelecimento centralizador não está parametrizado, o campo será em branco. | OS3810-B |
| RN0500-09 | Campo CNPJ_EST:  Verificar se a conta contábil está relacionada a um grupo que possua somente um Estabelecimento associado (e que este esteja vinculado à empresa de geração do meio magnético), se sim, trazer o conteúdo do campo CNPJ do Estabelecimento que está associado a esse grupo.  Caso contrário, deixar em branco. | OS3810-B |


| RNG-0990 | Deve ser gerado um registro 0990 por arquivo.  Registro de nível 1, ocorrência de 1 por arquivo e obrigatório. | OS3810-B |
| --- | --- | --- |
| RN0990-02 | Campo QTD_LIN_0:  Quantidade de registros do Bloco 0. | OS3810-B |


| RNG-A001 | Deve ser gerado um registro A001 por arquivo.  Registro de nível 1, ocorrência de 1 por arquivo e obrigatório. | OS3810-B |
| --- | --- | --- |
| RNA001-02 | Campo IND_MOV  Gerar fixo “1”. | OS3810-B |


| RNG-A990 | Deve ser gerado um registro A990 por arquivo.  Registro de nível 1, ocorrência de 1 por arquivo e obrigatório. | OS3810-B |
| --- | --- | --- |
| RNA990-02 | Campo QTD_LIN_A:  Quantidade de registros do Bloco A. | OS3810-B |


| RNG-C001 | Deve ser gerado um registro C001 por arquivo.  Registro de nível 1, ocorrência de 1 por arquivo e obrigatório. | OS3810-B |
| --- | --- | --- |
| RNC001-02 | Campo IND_MOV  Gerar fixo “1”. | OS3810-B |


| RNG-C990 | Deve ser gerado um registro C990 por arquivo.  Registro de nível 1, ocorrência de 1 por arquivo e obrigatório. | OS3810-B |
| --- | --- | --- |
| RNC990-02 | Campo QTD_LIN_C:  Quantidade de registros do Bloco C. | OS3810-B |


| RNG-D001 | Deve ser gerado um registro D001 por arquivo.  Registro de nível 1, ocorrência de 1 por arquivo e obrigatório. | OS3810-B |
| --- | --- | --- |
| RND001-02 | Campo IND_MOV  Gerar fixo “1”. | OS3810-B |


| RNG-D990 | Deve ser gerado um registro D990 por arquivo.  Registro de nível 1, ocorrência de 1 por arquivo e obrigatório. | OS3810-B |
| --- | --- | --- |
| RND990-02 | Campo QTD_LIN_D:  Quantidade de registros do Bloco D. | OS3810-B |


| RNG-F001 | Deve ser gerado um registro F001 por arquivo.  Registro de nível 1, ocorrência de 1 por arquivo e obrigatório. | OS3810-B |
| --- | --- | --- |
| RNF001-02 | Campo IND_MOV  Deverá ser gravado no campo 02 – IND_MOV se esse registro possui informações ou não.  Gravar “0”, caso existam informações a serem demonstradas nos registros F600 ou F700. Gravar “1”, caso não existam informações a serem demonstradas nos registros F600 ou F700. | OS3810-B OS3810-E |


| RNG-F600 | Gerar um registro F600 para cada registro informado através do módulo: EFD Contribuições Financeiras e Assemelhadas, menu: Manutenção >> Registro do Bloco F >> Contribuição Retida na Fonte (F600), que atenda ao critério abaixo:  Data de Pagamento:  Entre a Data Inicial e Data Final de geração do arquivo ou anterior.  O agrupamento dos registros deve ser feito de acordo com os campos chaves deste registro:  Indicador de Natureza da Retenção na Fonte (Campo 02) Data da Pagamento (Campo 14) Código da Receita (Campo 04) Indicador da Natureza da Receita (Campo 07) CNPJ (Campo 08)  OBS: a partir da OS3590 o agrupamento será a partir da Data de Pagamento e não mais da Data de Retenção. A Data de Pagamento deverá sempre ser igual ou menor que a DT_FIM do arquivo, gerado no registro 0000. | OS3810-D |
| --- | --- | --- |
| RNF600-01 | No campo REG deverá ser gravado o texto fixo “F600”. | OS3810-D |
| RNF600-02 | No campo IND_NAT_REC deverá ser gravado o indicador da Natureza da Receita, de acordo com a informação selecionada no campo “Natureza da Retenção na Fonte” da tela “Nova Contribuição na Fonte (F600)”.  Gravar “01”, caso a opção seja “01 - Retenção por Órgãos, Autarquias e Fundações Federais; Gravar “02”, caso a opção seja “02 - Retenção por outras Entidades da Administração Pública Federal”; Gravar “03”, caso a opção seja “03 - Retenção por Pessoas Jurídicas de Direito Privado”; Gravar “04”, caso a opção seja “04 - Recolhimento por Sociedade Cooperativa”; Gravar “05”, caso a opção seja “05 - Retenção por Fabricante de Máquinas e Veículos”; Gravar “99”, caso a opção seja “99 - Outras Retenções”. | OS3810-D |
| RNF600-03 | A data gerada nesse campo será a “Data de Pagamento” da SAFX145. | OS3810-D |
| RNF600-04 | Deverá ser gravado no campo VL_BC_RET, a informação contida no campo “Base de Cálculo Retenção ou Recolhimento” da tela “Nova Contribuição na Fonte (F600)”. | OS3810-D |
| RNF600-05 | Deverá ser gravado no campo VL_RET, a informação contida no campo “Valor Total na Fonte/Recolhido” da tela “Nova Contribuição na Fonte (F600)”. | OS3810-D |
| RNF600-06 | Ao gerar o campo 06 – COD_REC do registro F600, a informação deverá ser recuperada do campo “Código da Receita” (12/SAFX145) da tela de manutenção do registro F600 através do menu Manutenção >> Registro do Bloco F >> Contribuição Retida na Fonte (F600).  Deverão ser recuperados e gravados no arquivo os 4 (quatro) primeiros dígitos do Código de Receita. | OS3810-D |
| RNF600-07 | Deverá ser gravado no campo IND_NAT_REC, a informação contida no campo “Natureza da Receita” da tela “Nova Contribuição na Fonte (F600)”.  Gravar “0”, caso a opção seja “Não Cumulativa” Gravar “1”, caso a opção seja “Cumulativa”; | OS3810-D |
| RNF600-08 | Deverá ser gravado no campo CNPJ, o CNPJ com 14 posições de acordo com o campo “Responsável/Beneficiário da Retenção” da tela “Nova Contribuição na Fonte (F600)”. | OS3810-D |
| RNF600-09 | Deverá ser gravado no campo VL_RET_PIS, a informação que estiver contida no campo “Valor Retido na Fonte – Parcela Referente ao PIS” da tela “Nova Contribuição na Fonte (F600)”. | OS3810-D |
| RNF600-10 | Deverá ser gravado no campo VL_RET_COFINS, a informação que estiver contida no campo “Valor Retido na Fonte – Parcela Referente ao COFINS” da tela “Nova Contribuição na Fonte (F600)”. | OS3810-D |
| RNF600-11 | Deverá ser gravado no campo IND_REC, a informação que estiver contida no campo “Condição da PJ Declarante (Ind)” da tela “Nova Contribuição na Fonte (F600)”.  Gravar “0”, caso a opção seja “Beneficiária da Retenção / Recolhimento” Gravar “1”, caso a opção seja “Responsável da Retenção / Recolhimento”; | OS3810-D |


| RNG-F700 | Gerar um registro F700 para cada registro informado através do módulo: EFD-Contribuições Financeira/Assemelhada, menu: Manutenção → Registro do Bloco F → Deduções Diversas, que atenda ao critério abaixo:  Competência: Igual a competência (mês/ano) da geração do arquivo. Empresa e Estabelecimento: igual a parametrizada para geração. No caso de geração com estabelecimento centralizador, considerar dados de todos os centralizados. | OS3810-E |
| --- | --- | --- |
| RNF700-01 | Registro F700 - 01 - REG  Deverá ser gravado no campo 01 – REG o texto fixo “F700”. | OS3810-E |
| RNF700-02 | Registro F700 - 02 - IND_ORI_DED  Será gravado o conteúdo do campo “Origem da Dedução” da SAFX193. | OS3810-E |
| RNF700-03 | Registro F700 - 03 - IND_NAT_DED  Será gravado o conteúdo do campo “Natureza da Dedução” da SAFX193, realizando a seguinte conversão: Indicador da Natureza da Dedução = “N” - Não Cumulativa, gera “0”; Indicador da Natureza da Dedução = “C” - Cumulativa, gera “1”; | OS3810-E |
| RNF700-04 | Registro F700 - 04 - VL_DED_PIS  Será gravado o conteúdo do campo “Valor a Deduzir - PIS” da SAFX193. | OS3810-E |
| RNF700-05 | Registro F700 - 05 - VL_DED_COFINS  Será gravado o conteúdo do campo “Valor a Deduzir – COFINS” da SAFX193. | OS3810-E |
| RNF700-06 | Registro F700 - 06 - VL_BC_OPER  Será gravado o conteúdo do campo “Valor da Base de Cálculo a deduzir PIS/PASEP – COFINS” da SAFX193. | OS3810-E |
| RNF700-07 | Registro F700 - 07 – CNPJ  Será gravado o conteúdo do campo “CNPJ” da SAFX193. | OS3810-E |
| RNF700-08 | Registro F700 - 08 - INF_COMP  Será gravado o conteúdo do campo “Informações complementares” da SAFX193. | OS3810-E |


| RNG-F990 | Deve ser gerado um registro F990 por arquivo.  Registro de nível 1, ocorrência de 1 por arquivo e obrigatório. | OS3810-B |
| --- | --- | --- |
| RNF990-02 | Campo QTD_LIN_F:  Quantidade de registros do Bloco F. | OS3810-B |


| RNI001 | As informações serão recuperadas da tela de Operações do Período do módulo EFD-Contribuições Financeiras/Assemelhadas.  Registro de nível 1, ocorrência de 1 por arquivo e obrigatório. | OS3810-B |
| --- | --- | --- |
| RNI001-01 | Registro I001 – 01 – REG:  Deverá ser gravado no campo 01 – REG o texto fixo “I001”. | OS3810-B |
| RNI001-02 | Registro I001 – 02 – IND_MOV:  Deverá ser gravado no campo 02 – IND_MOV se esse registro possui informações ou não.  Gravar “0”, caso existam informações a serem recuperadas na tela de Operações do Período. Gravar “1”, caso não existam informações a serem recuperadas na tela de Operações do Período. | OS3810-B |


| Registro I010 – Identificação da Pessoa JurídicaRNI010 | As informações do registro I010 deverão ser recuperadas do cadastro de Empresa/Estabelecimento (menu: Preliminares >> Empresa/Estabelecimento) do módulo Parâmetros.   Caso o parâmetro “Multiempresa” não esteja selecionado, deverá ser recuperado o Estabelecimento que está selecionado. Caso o parâmetro “Multiempresa” esteja selecionado, deverá ser recuperado o Estabelecimento Centralizador – estabelecimento informado como Centralizador no menu: Preliminares >> Centralização de Escrituração de Obrigações Federais do módulo Parâmetros. Será recuperado o Estabelecimento Centralizador de acordo com a Empresa selecionada.  Registro de nível 2, ocorrência de vários por arquivo e obrigatório. | OS3810-B |
| --- | --- | --- |
| RNI010-01 | Registro I010 – 01 – REG  Deverá ser gravado no campo 01 – REG o texto fixo “I010”. | OS3810-B |
| RNI010-02 | Registro I010 – 02 – CNPJ  Deverá ser gravado no campo 02 – CNPJ o CNPJ da Pessoa Jurídica que está declarando a informação. Essa informação deverá ser recuperada da seguinte forma:  Caso o parâmetro “Multi-Empresa” não esteja selecionado, deverá ser recuperado o CNPJ do Estabelecimento que está selecionado – ver campo CNPJ do cadastro de Empresa/Estabelecimento do módulo Parâmetros (menu: Preliminares >> Empresa/Estabelecimento). Caso o parâmetro “Multi-Empresa” esteja selecionado, deverá ser recuperado o CNPJ do Estabelecimento Centralizador – estabelecimento informado como Centralizador no menu: Preliminares >> Centralização de Escrituração de Obrigações Federais do módulo Parâmetros. Será recuperado o CNPJ de acordo com a Empresa selecionada  – ver campo CNPJ do cadastro de Empresa/Estabelecimento do módulo Parâmetros (menu: Preliminares >> Empresa/Estabelecimento). | OS3810-B |
| RNI010-03 | Registro I010 – 03 – IND_ATIV  Deverá ser gravado no campo 03 – IND_ATIV o tipo de Atividade do ramo Financeiro ou Assemelhado ao qual o Estabelecimento está enquadrado. Essa informação deverá ser recuperada do campo “Tipo de Atividade Financeira” do cadastro de Empresa/Estabelecimento (menu: Preliminares >> Empresa/Estabelecimento) do módulo Parâmetros.  A informação deverá ser gravada da seguinte maneira:  Gravar “01” caso a opção selecionada seja “1 – Operações de Instituições Financeiras e Assemelhadas”; Gravar “02” caso a opção selecionada seja “2 – Operações de Seguros Privados”; Gravar “03” caso a opção selecionada seja “3 – Operações de Previdência Complementar”; Gravar “04” caso a opção selecionada seja “4 – Operações de Capitalização”; Gravar “05” caso a opção selecionada seja “5 – Operações de Planos de Assistência à Saúde”; Gravar “06” caso a opção selecionada seja “6 – Operações referentes a mais de um dos indicadores acima”. | OS3810-B |
| RNI010-04 | Registro I010 – 04 – INFO_COMPL  Deverá ser gravado no campo 04 – INFO_COMPL a Informação Complementar do Estabelecimento. Essa informação deverá ser recuperada do campo “Informação Complementar” do cadastro de Empresa/Estabelecimento (menu: Preliminares >> Empresa/Estabelecimento) do módulo Parâmetros. | OS3810-B |


| RNI100-00 | As informações do registro I100 deverão ser recuperadas da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período do módulo EFD-Contribuições Financeiras/Assemelhadas.  Registro de nível 3, para cada ocorrência do registro I010 podem existir “N” I100 e é obrigatório se houver. | OS3810-B |
| --- | --- | --- |
| RNI100-01 | Registro I100 – 01 – REG  Deverá ser gravado no campo 01 – REG o texto fixo “I100”. | OS3810-B |
| RNI100-02 | Registro I100 – 02 – VL_REC  Deverá ser gravado no campo 02 – VL_REC o Valor da Receita das Operações do Período. Essa informação deverá ser recuperada do campo “Valor Receita” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período (menu: Manutenção >> Operações do Período) do módulo EFD-Contribuições Financeira/Assemelhada. | OS3810-B |
| RNI100-03 | Registro I100 – 03 – CST_PIS_COFINS  Deverá ser gravado no campo 03 – CST_PIS_COFINS o Código de Situação Tributária PIS ou COFINS das Operações do Período. Essa informação deverá ser recuperada do campo “Cód. Sit. Trib. PIS/COFINS” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período (menu: Manutenção >> Operações do Período) do módulo EFD-Contribuições Financeira/Assemelhada. | OS3810-B |
| RNI100-04 | Registro I100 – 04 – VL_TOT_DED_GER  Deverá ser gravado no campo 04 – VL_TOT_DED_GER o Valor Total das Deduções e Exclusões de Caráter Geral. Essa informação deverá ser recuperada do campo “Valor Total Ded./Excl. Caráter Geral” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período (menu: Manutenção >> Operações do Período) do módulo EFD-Contribuições Financeira/Assemelhada. | OS3810-B |
| RNI100-05 | Registro I100 – 05 – VL_TOT_DED_ESP  Deverá ser gravado no campo 05 – VL_TOT_DED_ESP o Valor Total das Deduções e Exclusões de Caráter Específico. Essa informação deverá ser recuperada do campo “Valor Total Ded./Excl. Caráter Específico” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período (menu: Manutenção >> Operações do Período) do módulo EFD-Contribuições Financeira/Assemelhada. | OS3810-B |
| RNI100-06 | Registro I100 – 06 – VL_BC_PIS  Deverá ser gravado no campo 06 – VL_BC_PIS o Valor da Base de Cálculo do PIS. Essa informação deverá ser recuperada do campo “Valor Base de Cálculo PIS” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período (menu: Manutenção >> Operações do Período) do módulo EFD-Contribuições Financeira/Assemelhada. | OS3810-B |
| RNI100-07 | Registro I100 – 07 – ALIQ_PIS  Deverá ser gravado no campo 07 – ALIQ_PIS o Valor da Alíquota do PIS. Essa informação deverá ser recuperada do campo “Alíquota PIS” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período (menu: Manutenção >> Operações do Período) do módulo EFD-Contribuições Financeira/Assemelhada. | OS3810-B |
| RNI100-08 | Registro I100 – 08 – VL_PIS  Deverá ser gravado no campo 08 – VL_PIS o Valor do PIS. Essa informação deverá ser recuperada do campo “Valor PIS” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período (menu: Manutenção >> Operações do Período) do módulo EFD-Contribuições Financeira/Assemelhada. | OS3810-B |
| RNI100-09 | Registro I100 – 09 – VL_BC_COFINS  Deverá ser gravado no campo 09 – VL_BC_COFINS o Valor da Base de Cálculo do COFINS. Essa informação deverá ser recuperada do campo “Valor Base de Cálculo COFINS” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período (menu: Manutenção >> Operações do Período) do módulo EFD-Contribuições Financeira/Assemelhada. | OS3810-B |
| RNI100-10 | Registro I100 – 10 – ALIQ_COFINS  Deverá ser gravado no campo 10 – ALIQ_COFINS o Valor da Alíquota do COFINS. Essa informação deverá ser recuperada do campo “Alíquota COFINS” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período (menu: Manutenção >> Operações do Período) do módulo EFD-Contribuições Financeira/Assemelhada. | OS3810-B |
| RNI100-11 | Registro I100 – 11 – VL_COFINS  Deverá ser gravado no campo 11 – VL_COFINS o Valor do COFINS. Essa informação deverá ser recuperada do campo “Valor COFINS” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período (menu: Manutenção >> Operações do Período) do módulo EFD-Contribuições Financeira/Assemelhada. | OS3810-B |
| RNI100-12 | Registro I100 – 12 – INFO_COMPL  Deverá ser gravado no campo 12 – INFO_COMPL a Informação Complementar. Essa informação deverá ser recuperada do campo “Inf. Complementar” da tela “Operações do Período” – aba: I100 – Consolidação das Operações do Período (menu: Manutenção >> Operações do Período) do módulo EFD-Contribuições Financeira/Assemelhada. | OS3810-B |


| RNI200-00 | As informações do registro I200 deverão ser recuperadas da tela “Operações do Período” – aba: I200 – Composição das Receitas/Deduções/Exclusões do módulo EFD-Contribuições Financeiras/Assemelhadas.  Registro de nível 4, para cada ocorrência do registro I100 podem existir “N” I200 e é obrigatório se houver. | OS3810-B |
| --- | --- | --- |
| RNI200-01 | Registro I200 – 01 – REG  Deverá ser gravado no campo 01 – REG o texto fixo “I200”. | OS3810-B |
| RNI200-02 | Registro I200 – 02 – NUM_CAMPO  Deverá ser gravado no campo 02 – NUM_CAMPO o Número do Campo referente à Composição das Receitas/Deduções/Exclusões. A informação deverá ser gravada da seguinte forma:  Gravar “02”, caso a opção selecionada seja “Valor da Receita”; Gravar “04”, caso a opção selecionada seja “Valor Total Ded./Excl. Caráter Geral”; Gravar “05”, caso a opção selecionada seja “Valor Total Ded./Excl. Caráter Específico”. | OS3810-B |
| RNI200-03 | Registro I200 – 03 – COD_DET  Deverá ser gravado no campo 03 – COD_DET o Código de Detalhamento. Essa informação deverá ser recuperada do campo “Código Receita/Dedução/Exclusão” da tela “Operações do Período” – aba: I200 – Composição das Receitas/Deduções/Exclusões (menu: Manutenção >> Operações do Período) do módulo EFD-Contribuições Financeira/Assemelhada. | OS3810-B |
| RNI200-04 | Registro I200 – 04 – DET_VALOR  Deverá ser gravado no campo 04 – DET_VALOR o Detalhamento do Valor. Essa informação deverá ser recuperada do campo “Valor Detalhado” da tela “Operações do Período” – aba: I200 – Composição das Receitas/Deduções/Exclusões (menu: Manutenção >> Operações do Período) do módulo EFD-Contribuições Financeira/Assemelhada. | OS3810-B |
| RNI200-05 | Registro I200 – 05 – COD_CTA  Deverá ser gravado no campo 05 – COD_CTA o Código da Conta Contábil. Essa informação deverá ser recuperada do campo “Código Conta Contábil” da tela “Operações do Período” – aba: I200 – Composição das Receitas/Deduções/Exclusões (menu: Manutenção >> Operações do Período) do módulo EFD-Contribuições Financeira/Assemelhada.  O cadastro desta conta contábil deverá ser informado no registro 0500. | OS3810-B |
| RNI200-06 | Registro I200 – 06 – INFO_COMPL  Deverá ser gravado no campo 06 – INFO_COMPL a Informação Complementar. Essa informação deverá ser recuperada do campo “Informação Complementar” da tela “Operações do Período” – aba: I200 – Composição das Receitas/Deduções/Exclusões (menu: Manutenção >> Operações do Período) do módulo EFD-Contribuições Financeira/Assemelhada. | OS3810-B |


| RNI300-00 | As informações do registro I300 deverão ser recuperadas da tela “Operações do Período” – aba: I300 – Complemento das Operações do módulo EFD-Contribuições Financeiras/Assemelhadas.  Registro de nível 5, para cada ocorrência do registro I200 podem existir “N” I300 e é obrigatório se houver. | OS3810-B |
| --- | --- | --- |
| RNI300-01 | Registro I300 – 01 – REG  Deverá ser gravado no campo 01 – REG o texto fixo “I300”. | OS3810-B |
| RNI300-02 | Registro I300 – 02 – COD_COMP  Deverá ser gravado no campo 02 – COD_COMP o Código de Complemento. Essa informação deverá ser recuperada do campo “Cód. Complemento Receita/Dedução/Exclusão” da tela “Operações do Período” – aba: I300 – Complemento das Operações (menu: Manutenção >> Operações do Período) do módulo EFD-Contribuições Financeira/Assemelhada. | OS3810-B |
| RNI300-03 | Registro I300 – 03 – DET_VALOR  Deverá ser gravado no campo 03 – DET_VALOR o Valor Detalhado. Essa informação deverá ser recuperada do campo “Valor Detalhado” da tela “Operações do Período” – aba: I300 – Complemento das Operações (menu: Manutenção >> Operações do Período) do módulo EFD-Contribuições Financeira/Assemelhada. | OS3810-B |
| RNI300-04 | Registro I300 – 04 – COD_CTA  Deverá ser gravado no campo 04 – COD_CTA o Código da Conta Contábil. Essa informação deverá ser recuperada do campo “Cód. Conta Contábil” da tela “Operações do Período” – aba: I300 – Complemento das Operações (menu: Manutenção >> Operações do Período) do módulo EFD-Contribuições Financeira/Assemelhada.  O cadastro desta conta contábil deverá ser informado no registro 0500. | OS3810-B |
| RNI300-05 | Registro I300 – 05 – INFO_COMPL  Deverá ser gravado no campo 05 – INFO_COMPL a Informação Complementar. Essa informação deverá ser recuperada do campo “Informação Complementar” da tela “Operações do Período” – aba: I300 – Complemento das Operações (menu: Manutenção >> Operações do Período) do módulo EFD-Contribuições Financeira/Assemelhada. | OS3810-B |


| RNG-I990 | Deve ser gerado um registro I990 por arquivo.  Registro de nível 1, ocorrência de 1 por arquivo e obrigatório. | OS3810-B |
| --- | --- | --- |
| RNI990-02 | Campo QTD_LIN_I:  Quantidade de registros do Bloco I. | OS3810-B |


| RNG-M001 | Deve ser gerado um registro M001 por arquivo.  Registro de nível 1, ocorrência de 1 por arquivo e obrigatório. | OS3810-B |
| --- | --- | --- |
| RNM001-02 | Campo IND_MOV  Gerar fixo “0”. | OS3810-B |


| RNG-M200 | Deve ser gerado um registro M200 por arquivo, demonstrando o valor da contribuição apurada no período.  Este registro será gerado com base nos valores apurados no registro filho M210 e no registro F600 e F700 do mesmo período de apuração. Se não existir um destes registros que o originam, ele será gerado com valores zerados.  Para utilização e seleção dos valores informados nos Registros F600 e F700, as seguintes regras devem ser seguidas:  Se o parâmetro “Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS”, estiver desmarcado (em dados iniciais), realizar a ordem do desconto e deduções do valor da contribuição a recolher, conforme segue:  1. Através da totalização das informações dos registros M210, obtem-se o valor do campo 09 do registro M200. 2. Desse valor descontam-se as deduções do período (campo 04 do registro F700 quando o campo “03- Indicador da Natureza da Dedução” for igual a “1”). 3. Se ainda restar contribuição a pagar, desconta-se desse valor as retenções do período (campo 09 do registro F600 quando o campo “07 – Indicador da Natureza da Receita” for igual a 1 e o campo “11 – Indicador da Condição da PJ Declarante” for igual a “0”). 4. Se ainda restar contribuição a pagar, o usuário poderá indicar o valor da retenção a utilizar do saldo de períodos anteriores, informado na tela de “Retenções a Utilizar na Apuração”.  Obs.: Os descontos/deduções da contribuição apurada listados acima devem ser feitos na sequência indicada, até que não reste contribuição a pagar, ou até que não restem mais créditos/retenções/deduções a descontar/deduzir.  Se o parâmetro “Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS” estiver marcado (em dados iniciais):  1. Através da totalização das informações dos registros M210, obtem-se o valor do campo 09 do registro M200. 2. Desse valor descontam-se as deduções do período (campo 04 do registro F700 quando o campo “03- Indicador da Natureza da Dedução” for igual a “1”). 3. Se ainda restar contribuição a pagar, o usuário poderá indicar o valor da retenção a utilizar apurado no período através da tela “Retenção na Fonte PIS/PASEP Apurada no Período” ou poderá indicar o valor da retenção a utilizar do saldo de períodos anteriores, informado na tela de “Retenções a Utilizar na Apuração”.  Registro de nível 2, ocorrência de 1 por arquivo e obrigatório. | OS3810-B OS3810-E |
| --- | --- | --- |
| RNM200-02 | Campo VL_TOT_CONT_NC_PER:  Gerar “0,00”. | OS3810-B |
| RNM200-03 | Campo VL_TOT_CRED_DESC:  Gerar “0,00”. | OS3810-B |
| RNM200-04 | Campo VL_TOT_CRED_DESC_ANT:  Gerar “0,00”. | OS3810-B |
| RNM200-05 | Campo VL_TOT_CONT_NC_DEV:  Gerar “0,00”. | OS3810-B |
| RNM200-06 | Campo VL_RET_NC:  Gerar “0,00”. | OS3810-B |
| RNM200-07 | Campo VL_OUT_DED_NC:  Gerar “0,00”. | OS3810-B |
| RNM200-08 | Campo VL_CONT_NC_REC:  Gerar “0,00”. | OS3810-B |
| RNM200-09 | Campo VL_TOT_CONT_CUM_PER:  Este campo será resultado da soma dos valores lançados no campo 13 - VL_CONT_PER dos registros M210 filhos deste registro. | OS3810-B |
| RNM200-10 | Campo VL_RET_CUM:  Se o parâmetro “Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS” estiver desmarcado (em dados iniciais) O valor do campo deve ser igual ao somatório do campo “09 – Valor Retido na Fonte-PIS” do registro F600 quando o campo “07 – Indicador da Natureza da Receita” for igual a 1 e o campo “11 – Indicador da Condição da PJ Declarante” for igual a “0”, considerando a ordem para dedução da contribuição indicado na RNG-M200.  Se ainda restar valor de contribuição a recolher, o usuário poderá indicar o valor da retenção a utilizar do saldo de períodos anteriores, informado na tela de “Retenções a Utilizar na Apuração”, campo “Retenção Deduzida da Contribuição” quando o campo Natureza da Receita  for igual “1 – Receita da Natureza Cumulativa”, contanto que não exceda o valor da contribuição disponível.  Se o parâmetro “Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS” estiver marcado (em dados iniciais): Esse campo deve ser preenchido com o resultado da somatória dos valores do campo “Retenção Deduzida na Contribuição’’, quando o campo Natureza da Receita  for igual “1 – Receita da Natureza Cumulativa” das telas Apuração PIS/PASEP → Pasta Retenção na Fonte Apurada no Período” e da tela de “Retenção a utilizar na apuração” | OS3810-B OS3810-E |
| RNM200-11 | Campo VL_OUT_DED_CUM:  Observar a ordem para realização da utilização do valor da retenção informada na RNG-M200. O valor do campo deve ser igual ao somatório do campo “04 – Valor a Deduzir-PIS” do registro F700 quando o campo “03 – Indicador da Natureza da Dedução” for igual a “1” | OS3810-B OS3810-E |
| RNM200-12 | Campo VL_CONT_CUM_REC:  Este campo será resultado do cálculo: (Campo VL_TOT_CONT_CUM_PER menos Campo VL_RET_CUM menos Campo VL_OUT_DED_CUM). | OS3810-B |
| RNM200-13 | Campo VL_TOT_CONT_REC:  Este campo será resultado do cálculo: (Campo VL_CONT_NC_REC mais Campo VL_CONT_CUM_REC). | OS3810-B |


| RNG-M205 | Será gerado com base no informado na tela de “Detalhamento por Código de Receita (Visão Débito DCTF) - M205” (Menu: Obrigações >> Manutenção >> Apuração PIS/PASEP ou Menu: Obrigações SCP >> Manutenção >> Apuração PIS/PASEP), considerando o registro vinculado ao M200 que está sendo gerado.  Este registro deve ser gerado apenas quando a data inicial de geração for maior ou igual a 01/01/2014. | OS3810-H1 |
| --- | --- | --- |
| RNM205-01 | Gerar conteúdo fixo: “M205” | OS3810-H1 |
| RNM205-02 | Gerar o conteúdo informado no campo “Nº do Campo”, considerando:  “08”, quando for selecionada a opção 08 – Valor da Contribuição Não-Cumulativa; “12”, quando for selecionada a opção 12 – Valor da Contribuição Cumulativa; | OS3810-H1 |
| RNM205-03 | Gerar o conteúdo informado no campo “Cód. de Receita”. | OS3810-H1 |
| RNM205-04 | Gerar o conteúdo informado no campo “Valor do Débito”; | OS3810-H1 |


| RNG-M210 | Este registro será gerado com base nos valores demonstrados nos registros I100 gerados no período, cujo conteúdo do campo 03 - CST_PIS_COFINS seja igual a “01”. Ele será uma consolidação das informações por COD_CONT e ALIQ_PIS.  Registro de nível 3, para cada ocorrência do registro M200 poderão existir “N” M210 por arquivo e obrigatório quando existir o M200. | OS3810-B |
| --- | --- | --- |
| RNM210-02 | Campo COD_CONT:  Fixar “51”. | OS3810-B |
| RNM210-03 | Campo VL_REC_BRT:  Este campo será resultado da soma dos valores lançados no campo 02 - VL_REC de todos os registros I100 do arquivo, cujo conteúdo do campo 03 - CST_PIS_COFINS seja igual a “01”, considerando o agrupamento deste registro que é por COD_CONT e ALIQ_PIS. | OS3810-B |
| RNM210-04 | Campo VL_BC_CONT:  Este campo será resultado da soma dos valores lançados no campo 06 - VL_BC_PIS de todos os registros I100 do arquivo, cujo conteúdo do campo 03 - CST_PIS_COFINS seja igual a “01”, considerando o agrupamento deste registro que é por COD_CONT e ALIQ_PIS. | OS3810-B |
| RNM210-05 | Campo ALIQ_PIS:  Neste campo será demonstrada a alíquota informada no campo 07 - ALIQ_PIS de todos os registros I100 do arquivo, cujo conteúdo do campo 03 - CST_PIS_COFINS seja igual a “01”. | OS3810-B |
| RNM210-06 | Campo QUANT_BC_PIS:  Gerar nulo (“||”). | OS3810-B |
| RNM210-07 | Campo ALIQ_PIS_QUANT:  Gerar nulo (“||”). | OS3810-B |
| RNM210-08 | Campo VL_CONT_APUR:  Este campo será resultado do seguinte cálculo: Valor informado no campo VL_BC_CONT multiplicado pelo resultado do cálculo (valor do campo ALIQ_PIS dividido por 100) | OS3810-B |
| RNM210-09 | Campo VL_AJUS_ACRES:  RNG46.3.2.1.189 O valor deste campo deverá ser igual ao somatório do VL_AJ do registro M220 quando IND_AJ = 1. | OS3810-B OS3810-E |
| RNM210-10 | Campo VL_AJUS_REDUC:  O valor deste campo deverá ser igual ao somatório do VL_AJ do registro M220 quando IND_AJ = 0. | OS3810-B OS3810-E |
| RNM210-11 | Campo VL_CONT_DIFER:  RNG46.3.2.1.191 O valor deste campo deverá ser igual ao somatório do VL_CONT_DIF dos registros M230 relacionados a esse registro M210, informado através do módulo: SPED → EFD-Contribuição Financeira/Assemelhada → Obrigações → Manutenção → Apuração – PIS/PASEP → pasta Contribuição para o PIS/PASEP no Período (aba “Informações Adicionais de Diferimento – M230”). | OS3810-B OS3810-E |
| RNM210-12 | Campo VL_CONT_DIFER_ANT:  O valor deste campo deverá ser igual ao somatório dos campos VL_CONT_DIFER_ANT do registro M300 relacionados à esse registro M210, informado através do módulo: SPED → EFD-Contribuição Financeira/Assemelhada → Obrigações → Manutenção → Apuração – PIS → pasta Contribuição para o PIS/PASEP no Período (‘’ Contribuição de PIS/PASEP Diferida em Períodos Anteriores – M300’’). | OS3810-B OS3810-E |
| RNM210-13 | Campo VL_CONT_PER:  Este campo será resultado do cálculo: (Valor do campo VL_CONT_APUR mais valor do campo VL_AJUS_ACRES menos valor do campo VL_AJUS_REDUC menos valor do campo VL_CONT_DIFER mais valor do campo VL_CONT_DIFER_ANT). | OS3810-B |


| RNG-M210 | Este registro será gerado com base nos valores demonstrados nos registros I100 gerados no período, cujo conteúdo do campo 03 - CST_PIS_COFINS seja igual a “01”. Ele será uma consolidação das informações por COD_CONT e ALIQ_PIS.  Registro de nível 3, para cada ocorrência do registro M200 poderão existir “N” M210 por arquivo e obrigatório quando existir o M200. | MFS25094 |
| --- | --- | --- |
| RNM210-02 | Campo COD_CONT:  Fixar “51”. | MFS25094 |
| RNM210-03 | Campo VL_REC_BRT:  Este campo será resultado da soma dos valores lançados no campo 02 - VL_REC de todos os registros I100 do arquivo, cujo conteúdo do campo 03 - CST_PIS_COFINS seja igual a “01”, considerando o agrupamento deste registro que é por COD_CONT e ALIQ_PIS. | MFS25094 |
| RNM210-04 | Campo VL_BC_CONT:  Este campo será resultado da soma dos valores lançados no campo 06 - VL_BC_PIS de todos os registros I100 do arquivo, cujo conteúdo do campo 03 - CST_PIS_COFINS seja igual a “01”, considerando o agrupamento deste registro que é por COD_CONT e ALIQ_PIS. | MFS25094 |
| RNM210-05 | Campo  VL_AJUS_ACRES_BC_PIS:  RNG46.3.2.1.190 O valor deste campo deverá ser igual ao somatório do VL_AJ_BC do registro M215 quando IND_AJ_BC = 1. | MFS25094 |
| RNM210-06 | Campo VL_AJUS_REDUC_BC_PIS:  RNG46.3.2.1.190 O valor deste campo deverá ser igual ao somatório do VL_AJ_BC do registro M215 quando IND_AJ_BC = 0. | MFS25094 |
| RNM210-07 | Campo VL_BC_CONT_AJUS:  O valor deste campo é igual à VL_BC_CONT (+) VL_AJUS_ACRES_BC_PIS (-) VL_AJUS_REDUC_BC_PIS. | MFS25094 |
| RNM210-08 | Campo ALIQ_PIS:  Neste campo será demonstrada a alíquota informada no campo 07 - ALIQ_PIS de todos os registros I100 do arquivo, cujo conteúdo do campo 03 - CST_PIS_COFINS seja igual a “01”. | MFS25094 |
| RNM210-09 | Campo QUANT_BC_PIS:  Gerar nulo (“||”). | MFS25094 |
| RNM210-10 | Campo ALIQ_PIS_QUANT:  Gerar nulo (“||”). | MFS25094 |
| RNM210-11 | Campo VL_CONT_APUR:  Este campo será resultado do seguinte cálculo: Valor informado no campo VL_BC_CONT multiplicado pelo resultado do cálculo (valor do campo ALIQ_PIS dividido por 100) | MFS25094 |
| RNM210-12 | Campo VL_AJUS_ACRES:  RNG46.3.2.1.189 O valor deste campo deverá ser igual ao somatório do VL_AJ do registro M220 quando IND_AJ = 1. | MFS25094 |
| RNM210-13 | Campo VL_AJUS_REDUC:  O valor deste campo deverá ser igual ao somatório do VL_AJ do registro M220 quando IND_AJ = 0. | MFS25094 |
| RNM210-14 | Campo VL_CONT_DIFER:  RNG46.3.2.1.191 O valor deste campo deverá ser igual ao somatório do VL_CONT_DIF dos registros M230 relacionados a esse registro M210, informado através do módulo: SPED → EFD-Contribuição Financeira/Assemelhada → Obrigações → Manutenção → Apuração – PIS/PASEP → pasta Contribuição para o PIS/PASEP no Período (aba “Informações Adicionais de Diferimento – M230”). | MFS25094 |
| RNM210-15 | Campo VL_CONT_DIFER_ANT:  O valor deste campo deverá ser igual ao somatório dos campos VL_CONT_DIFER_ANT do registro M300 relacionados a esse registro M210, informado através do módulo: SPED → EFD-Contribuição Financeira/Assemelhada → Obrigações → Manutenção → Apuração – PIS → pasta Contribuição para o PIS/PASEP no Período (‘’ Contribuição de PIS/PASEP Diferida em Períodos Anteriores – M300’’). | MFS25094 |
| RNM210-16 | Campo VL_CONT_PER:  Este campo será resultado do cálculo: (Valor do campo VL_CONT_APUR mais valor do campo VL_AJUS_ACRES menos valor do campo VL_AJUS_REDUC menos valor do campo VL_CONT_DIFER mais valor do campo VL_CONT_DIFER_ANT). | MFS25094 |


| RNG-M215 | Este registro será utilizado pela pessoa jurídica para detalhar os totais de ajustes da base de cálculo, informados nos campos 05 e 06 do registro pai M210.  Gerar um registro M215 para cada registro informado através do módulo: EFD-Financeira, menu: Obrigações → Manutenção → Apuração – PIS/PASEP  pasta “Contribuição para o PIS/PASEP do Período – M200”  (aba Detalhamento dos Ajustes da BC do PIS/PASEP Apurado – M215), que atenda ao critério abaixo:  Período da Apuração Entre a data inicial e data final de geração do arquivo. 	 Este registro será um agrupamento de informações através dos campos IND_AJ_BC, COD_AJ_BC e NUM_DOC. | MFS25094 |
| --- | --- | --- |
| RNM215-01 | Campo REG  Gravar o conteúdo fixo “M215”. | MFS25094 |
| RNM215-02 | Campo IND_AJ_BC  Campo Tipo de Ajuste da tela de Detalhamento dos Ajustes da BC da Contribuição para o PIS/PASEP Apurado – M215. | MFS25094 |
| RNM215-03 | Campo VL_AJ_BC  Campo Valor do Ajuste da tela de Detalhamento dos Ajustes da BC da Contribuição para o PIS/PASEP Apurado – M215. | MFS25094 |
| RNM215-04 | Campo COD_AJ_BC  Campo Código do Ajuste da tela de Detalhamento dos Ajustes da BC da Contribuição para o PIS/PASEP Apurado – M215. | MFS25094 |
| RNM215-05 | Campo NUM_DOC  Campo Número do processo, documento ou ato concessório da tela de Detalhamento dos Ajustes da BC da Contribuição para o PIS/PASEP Apurado – M215. | MFS25094 |
| RNM215-06 | Campo DESCR_AJ_BC  Campo Descrição Resumida da tela de Detalhamento dos Ajustes da BC da Contribuição para o PIS/PASEP Apurado – M215. | MFS25094 |
| RNM215-07 | Campo DT_REF  Campo Data Referência da tela de Detalhamento dos Ajustes da BC da Contribuição para o PIS/PASEP Apurado – M215. | MFS25094 |
| RNM215-08 | Campo COD_CTA  Campo Conta Analítica da tela de Detalhamento dos Ajustes da BC da Contribuição para o PIS/PASEP Apurado – M215. | MFS25094 |
| RNM215-09 | Campo CNPJ  Campo CNPJ da tela de Detalhamento dos Ajustes da BC da Contribuição para o PIS/PASEP Apurado – M215. | MFS25094 |
| RNM215-10 | Campo INFO_COMPL  Campo Informação Complementar da tela de Detalhamento dos Ajustes da BC da Contribuição para o PIS/PASEP Apurado – M215. | MFS25094 |


| RNG-M225 | Deve ser gerado um registro M225 para cada registro incluído através de manutenção no menu: Obrigações > Manutenção > Apuração PIS/PASEP > Detalhamento dos Ajustes da Contribuição para o PIS/Pasep Apurado – M225 ou Obrigações SCP > Manutenção > Apuração PIS/PASEP > Detalhamento dos Ajustes da Contribuição para o PIS/Pasep Apurado – M225 e que esteja vinculado ao registro pai, M220.  Este registro será um agrupamento de informações através dos campos DET_VALOR_AJ, CST_PIS, DET_ALIQ, DT_OPER_AJ e COD_CTA. | OS4316-D |
| --- | --- | --- |
| RNM225-01 | Campo REG  Gravar o conteúdo fixo “M225”. | OS4316-D |
| RNM225-02 | Campo DET_VALOR_AJ  Campo Detalhamento do Valor da tela de Detalhamento dos Ajustes da Contribuição para o PIS/Pasep Apurado – M225. | OS4316-D |
| RNM225-03 | Campo CST_PIS  Campo CST da tela de Detalhamento dos Ajustes da Contribuição para o PIS/Pasep Apurado – M225. | OS4316-D |
| RNM225-04 | Campo DET_BC_CRED  Campo Detalhamento da BC da tela de Detalhamento dos Ajustes da Contribuição para o PIS/Pasep Apurado – M225. | OS4316-D |
| RNM225-05 | Campo DET_ALIQ  Campo Detalhamento da Alíquota da tela de Detalhamento dos Ajustes da Contribuição para o PIS/Pasep Apurado – M225. | OS4316-D |
| RNM225-06 | Campo DT_OPER_AJ  Campo Data da Operação da tela de Detalhamento dos Ajustes da Contribuição para o PIS/Pasep Apurado – M225. | OS4316-D |
| RNM225-07 | Campo DESC_AJ  Campo Descrição da Operação da tela de Detalhamento dos Ajustes da Contribuição para o PIS/Pasep Apurado – M225. | OS4316-D |
| RNM225-08 | Campo COD_CTA  Campo Conta Contábil da tela de Detalhamento dos Ajustes da Contribuição para o PIS/Pasep Apurado – M225. A partir da conta contábil informada neste campo deve ser gerado um registro 0500, para demonstrar as informações do cadastro da conta. | OS4316-D |
| RNM225-09 | Campo INFO_COMPL  Campo Informação Complementar da tela de Detalhamento dos Ajustes da Contribuição para o PIS/Pasep Apurado – M225. | OS4316-D |


| RNG-M400 | Este registro será gerado com base na parametrização realizada na tela de Parametrização por Conta Contábil, considerando o agrupamento das informações por Código de Situação Tributária do PIS e Conta Contábil. Ele só existirá quando o Código de Natureza da Receita da parametrização for diferente de nulo e o Código de Situação Tributária do PIS for igual a “06” ou “07” ou “08” ou “09”.  Este registro é pai do M410. No M410 as informações serão detalhadas por Natureza da Receita e Conta Contábil e aqui por CST e Conta Contábil, sendo que, a conta contábil aqui informada será a sintética das contas analíticas demonstradas no M410.  Registro de nível 2, existirão vários por arquivo e obrigatório quando o Código de Situação Tributária do PIS for igual a “06” ou “07” ou “08” ou “09”. | OS3810-B |
| --- | --- | --- |
| RNM400-02 | Campo CST_PIS:  Campo Situação Tributária do PIS informada na parametrização. | OS3810-B |
| RNM400-03 | Campo VL_TOT_REC:  Este campo será a soma dos valores lançados no campo 03 - VL_REC do registro M410 que são filhos deste registro. | OS3810-B |
| RNM400-04 | Campo COD_CTA:  Será gerado com o código da Conta Contábil do tipo “Sintética” de nível anterior à conta informada no registro filho M410.  Exemplo – Contas: 1.00 (sintética – nível 2) 1.00.00 (sintética – nível 3) 1.00.00.01 (analítica – nível 4) 1.00.00.02 (analítica – nível 4) 1.00.00.00.01 (analítica – nível 5)  No registro filho, M410, estarão as contas analíticas. Neste registro será gerada a conta sintética de nível anterior à conta informada no registro filho. Sendo assim, com base no exemplo, será gerada a conta “1.00.00”.  O cadastro desta conta contábil deverá ser informado no registro 0500. | OS3810-B |
| RNM400-05 | Campo DESC_COMPL:  Gerar nulo (“||”). | OS3810-B |


| RNG-M410 | Este registro será gerado com base na parametrização realizada na tela de Parametrização por Conta Contábil, considerando o agrupamento das informações por Código de Natureza da Receita e Conta Contábil. Ele só existirá quando o Código de Natureza da Receita da parametrização for diferente de nulo e o Código de Situação Tributária do PIS for igual a “06” ou “07” ou “08” ou “09”.  Serão considerados registros da tabela SAFX01 – Arquivo Contábil das Contas Contábeis parametrizadas cuja Data da Operação compreenda o período de geração do arquivo.  Registro de nível 3, para cada ocorrência do registro M400 poderão existir “N” M410 por arquivo e obrigatório quando existir o M400. | OS3810-B |
| --- | --- | --- |
| RNM410-02 | Campo NAT_REC:  Informar neste campo o Código de Natureza da Receita vinculado à parametrização. | OS3810-B |
| RNM410-03 | Campo VL_REC:  Este campo será resultado do cálculo: (soma do Valor do Lançamento Contábil de todos os lançamentos existentes para o período cujo Indicador de Débito/Crédito seja igual a “C”) menos (soma do Valor do Lançamento Contábil de todos os lançamentos existentes para o período cujo Indicador de Débito/Crédito seja igual a “D”).  Mesmo que o resultado apurado seja negativo, deve ser apresentado o valor absoluto (positivo). | OS3810-B |
| RNM410-04 | Campo COD_CTA:  Informar neste campo a Conta Contábil vinculada à parametrização.  O cadastro desta conta contábil deverá ser informado no registro 0500. | OS3810-B |
| RNM410-05 | Campo DESC_COMPL:  Gerar nulo (“||”). | OS3810-B |


| RNG-M600 | Deve ser gerado um registro M600 por arquivo, demonstrando o valor da contribuição apurada no período.  Este registro será gerado com base nos valores apurados no registro filho M610, no registro F600 e F700 do mesmo período de apuração. Se não existir um destes registros que o originam, ele será gerado com valores zerados.  Para utilização e seleção dos valores informados nos Registros F600 e F700, as seguintes regras devem ser seguidas:  Se o parâmetro “Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS”, estiver desmarcado (em dados iniciais), realizar a ordem do desconto e deduções do valor da contribuição a recolher, conforme segue:  1. Através da totalização das informações dos registros M610, obtem-se o valor do campo 09 do registro M600. 2. Desse valor descontam-se as deduções do período (campo 05 do registro F700 quando o campo “03- Indicador da Natureza da Dedução” for igual a “1”). 3. Se ainda restar contribuição a pagar, desconta-se desse valor as retenções do período (campo 10 do registro F600 quando o campo “07 – Indicador da Natureza da Receita” for igual a 1 e o campo “11 – Indicador da Condição da PJ Declarante” for igual a “0”). 4. Se ainda restar contribuição a pagar, o usuário poderá indicar o valor da retenção a utilizar do saldo de períodos anteriores, informado na tela de “Retenções a Utilizar na Apuração”.  Obs.: Os descontos/deduções da contribuição apurada listados acima devem ser feitos na sequência indicada, até que não reste contribuição a pagar, ou até que não restem mais créditos/retenções/deduções a descontar/deduzir.  Se o parâmetro “Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS” estiver marcado (em dados iniciais):  1. Através da totalização das informações dos registros M610, obtem-se o valor do campo 09 do registro M600. 2. Desse valor descontam-se as deduções do período (campo 05 do registro F700 quando o campo “03- Indicador da Natureza da Dedução” for igual a “1”). 3. Se ainda restar contribuição a pagar, o usuário poderá indicar o valor da retenção a utilizar apurado no período através da tela “Retenção na Fonte PIS/PASEP Apurada no Período” ou poderá indicar o valor da retenção a utilizar do saldo de períodos anteriores, informado na tela de “Retenções a Utilizar na Apuração”.  Registro de nível 2, ocorrência de 1 por arquivo e obrigatório. | OS3810-B OS3810-E |
| --- | --- | --- |
| RNM600-02 | Campo VL_TOT_CONT_NC_PER:  Gerar “0,00”. | OS3810-B |
| RNM600-03 | Campo VL_TOT_CRED_DESC:  Gerar “0,00”. | OS3810-B |
| RNM600-04 | Campo VL_TOT_CRED_DESC_ANT:  Gerar “0,00”. | OS3810-B |
| RNM600-05 | Campo VL_TOT_CONT_NC_DEV:  Gerar “0,00”. | OS3810-B |
| RNM600-06 | Campo VL_RET_NC:  Gerar “0,00”. | OS3810-B |
| RNM600-07 | Campo VL_OUT_DED_NC:  Gerar “0,00”. | OS3810-B |
| RNM600-08 | Campo VL_CONT_NC_REC:  Gerar “0,00”. | OS3810-B |
| RNM600-09 | Campo VL_TOT_CONT_CUM_PER:  Este campo será resultado da soma dos valores lançados no campo 13 - VL_CONT_PER dos registros M610 filhos deste registro. | OS3810-B |
| RNM600-10 | Campo VL_RET_CUM:  Se o parâmetro “Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS” estiver desmarcado (em dados iniciais) O valor do campo deve ser igual ao somatório do campo “10 – Valor Retido na Fonte-COFINS” do registro F600 quando o campo “07 – Indicador da Natureza da Receita” for igual a 1 e o campo “11 – Indicador da Condição da PJ Declarante” for igual a “0”, considerando a ordem para dedução da contribuição indicado na RNG-M600.  Se ainda restar valor de contribuição a recolher, o usuário poderá indicar o valor da retenção a utilizar do saldo de períodos anteriores, informado na tela de “Retenções a Utilizar na Apuração”, campo “Retenção Deduzida da Contribuição” quando o campo Natureza da Receita  for igual “1 – Receita da Natureza Cumulativa”, contanto que não exceda o valor da contribuição disponível.  Se o parâmetro “Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS” estiver marcado (em dados iniciais): Esse campo deve ser preenchido com o resultado da somatória dos valores do campo “Retenção Deduzida na Contribuição’’, quando o campo Natureza da Receita  for igual “1 – Receita da Natureza Cumulativa” das telas Apuração PIS/PASEP → Pasta Retenção na Fonte Apurada no Período” e da tela de “Retenção a utilizar na apuração” | OS3810-B OS3810-E |
| RNM600-11 | Campo VL_OUT_DED_CUM:  Observar a ordem para realização da utilização do valor da retenção informada na RNG-M600. O valor do campo deve ser igual ao somatório do campo “05 – Valor a Deduzir-COFINS” do registro F700 quando o campo “03 – Indicador da Natureza da Dedução” for igual a “1” | OS3810-B OS3810-E |
| RNM600-12 | Campo VL_CONT_CUM_REC:  Este campo será resultado do cálculo: (Campo VL_TOT_CONT_CUM_PER menos Campo VL_RET_CUM menos Campo VL_OUT_DED_CUM). | OS3810-B |
| RNM600-13 | Campo VL_TOT_CONT_REC:  Este campo será resultado do cálculo: (Campo VL_CONT_NC_REC mais Campo VL_CONT_CUM_REC). | OS3810-B |


| RNG-M605 | Será gerado com base no informado na tela de “Detalhamento por Código de Receita (Visão Débito DCTF) – M605” (Menu: Obrigações >> Manutenção >> Apuração COFINS ou Menu: Obrigações SCP >> Manutenção >> Apuração COFINS), considerando o registro vinculado ao M200 que está sendo gerado.  Este registro deve ser gerado apenas quando a data inicial de geração for maior ou igual a 01/01/2014. | OS3810-H1 |
| --- | --- | --- |
| RNM605-01 | Gerar conteúdo fixo: “M605” | OS3810-H1 |
| RNM605-02 | Gerar o conteúdo informado no campo “Nº do Campo”, considerando:  “08”, quando for selecionada a opção 08 – Valor da Contribuição Não-Cumulativa; “12”, quando for selecionada a opção 12 – Valor da Contribuição Cumulativa; | OS3810-H1 |
| RNM605-03 | Gerar o conteúdo informado no campo “Cód. de Receita”. | OS3810-H1 |
| RNM605-04 | Gerar o conteúdo informado no campo “Valor do Débito”; | OS3810-H1 |


| RNG-M610 | Este registro será gerado com base nos valores demonstrados nos registros I100 gerados no período, cujo conteúdo do campo 03 - CST_PIS_COFINS seja igual a “01”. Ele será uma consolidação das informações por COD_CONT e ALIQ_COFINS.  Registro de nível 3, para cada ocorrência do registro M600 poderão existir “N” M610 por arquivo e obrigatório quando existir o M600. | OS3810-B |
| --- | --- | --- |
| RNM610-02 | Campo COD_CONT:  Fixar “51”. | OS3810-B |
| RNM610-03 | Campo VL_REC_BRT:  Este campo será resultado da soma dos valores lançados no campo 02 - VL_REC de todos os registros I100 do arquivo, cujo conteúdo do campo 03 - CST_PIS_COFINS seja igual a “01”, considerando o agrupamento deste registro que é por COD_CONT e ALIQ_COFINS. | OS3810-B |
| RNM610-04 | Campo VL_BC_CONT:  Este campo será resultado da soma dos valores lançados no campo 09 - VL_BC_COFINS de todos os registros I100 do arquivo, cujo conteúdo do campo 03 - CST_PIS_COFINS seja igual a “01”, considerando o agrupamento deste registro que é por COD_CONT e ALIQ_COFINS. | OS3810-B |
| RNM610-05 | Campo ALIQ_COFINS:  Neste campo será demonstrada a alíquota informada no campo 10 - ALIQ_COFINS de todos os registros I100 do arquivo, cujo conteúdo do campo 03 - CST_PIS_COFINS seja igual a “01”. | OS3810-B |
| RNM610-06 | Campo QUANT_BC_COFINS:  Gerar nulo (“||”). | OS3810-B |
| RNM610-07 | Campo ALIQ_COFINS_QUANT:  Gerar nulo (“||”). | OS3810-B |
| RNM610-08 | Campo VL_CONT_APUR:  Este campo será resultado do seguinte cálculo: Valor informado no campo VL_BC_CONT multiplicado pelo resultado do cálculo (valor do campo ALIQ_COFINS dividido por 100) | OS3810-B |
| RNM610-09 | Campo VL_AJUS_ACRES:  RNG46.3.2.1.189 O valor deste campo deverá ser igual ao somatório do VL_AJ do registro M620 quando IND_AJ = 1. | OS3810-B OS3810-E |
| RNM610-10 | Campo VL_AJUS_REDUC:  RNG46.3.2.1.189 O valor deste campo deverá ser igual ao somatório do VL_AJ do registro M620 quando IND_AJ = 0. | OS3810-B OS3810-E |
| RNM610-11 | Campo VL_CONT_DIFER:  RNG46.3.2.1.191 O valor deste campo deverá ser igual ao somatório do VL_CONT_DIF dos registros M630 relacionados a esse registro M610, informado através do módulo: SPED → EFD-Contribuição Financeira/Assemelhada → Obrigações → Manutenção → Apuração – COFINS → pasta Contribuição para a COFINS no Período (aba “Informações Adicionais de Diferimento – M630”). | OS3810-B OS3810-E |
| RNM610-12 | Campo VL_CONT_DIFER_ANT:  O valor deste campo deverá ser igual ao somatório dos campos VL_CONT_DIFER_ANT do registro M700 relacionados à esse registro M610, informado através do módulo: SPED → EFD-Contribuição Financeira/Assemelhada → Obrigações → Manutenção → Apuração – COFINS → pasta Contribuição para a COFINS no Período (“Contribuição de COFINS Diferida em Períodos Anteriores – M700”). | OS3810-B OS3810-E |
| RNM610-13 | Campo VL_CONT_PER:  Este campo será resultado do cálculo: (Valor do campo VL_CONT_APUR mais valor do campo VL_AJUS_ACRES menos valor do campo VL_AJUS_REDUC menos valor do campo VL_CONT_DIFER mais valor do campo VL_CONT_DIFER_ANT). | OS3810-B |


| RNG-M610 | Este registro será gerado com base nos valores demonstrados nos registros I100 gerados no período, cujo conteúdo do campo 03 - CST_PIS_COFINS seja igual a “01”. Ele será uma consolidação das informações por COD_CONT e ALIQ_COFINS.  Registro de nível 3, para cada ocorrência do registro M600 poderão existir “N” M610 por arquivo e obrigatório quando existir o M600. | MFS25094 |
| --- | --- | --- |
| RNM610-02 | Campo COD_CONT:  Fixar “51”. | MFS25094 |
| RNM610-03 | Campo VL_REC_BRT:  Este campo será resultado da soma dos valores lançados no campo 02 - VL_REC de todos os registros I100 do arquivo, cujo conteúdo do campo 03 - CST_PIS_COFINS seja igual a “01”, considerando o agrupamento deste registro que é por COD_CONT e ALIQ_COFINS. | MFS25094 |
| RNM610-04 | Campo VL_BC_CONT:  Este campo será resultado da soma dos valores lançados no campo 09 - VL_BC_COFINS de todos os registros I100 do arquivo, cujo conteúdo do campo 03 - CST_PIS_COFINS seja igual a “01”, considerando o agrupamento deste registro que é por COD_CONT e ALIQ_COFINS. | MFS25094 |
| RNM610-05 | Campo VL_AJUS_ACRES_BC_COFINS:  O valor deste campo deverá ser igual ao somatório do VL_AJ_BC do registro M215 quando IND_AJ_BC = 1. | MFS25094 |
| RNM610-06 | Campo VL_AJUS_REDUC_BC_COFINS:  O valor deste campo deverá ser igual ao somatório do VL_AJ_BC do registro M215 quando IND_AJ_BC = 0. | MFS25094 |
| RNM610-07 | Campo VL_BC_CONT_AJUS:  O valor deste campo é igual à VL_BC_CONT (+) VL_AJUS_ACRES_BC_COFINS (-) VL_AJUS_REDUC_BC_COFINS. | MFS25094 |
| RNM610-08 | Campo ALIQ_COFINS:  Neste campo será demonstrada a alíquota informada no campo 10 - ALIQ_COFINS de todos os registros I100 do arquivo, cujo conteúdo do campo 03 - CST_PIS_COFINS seja igual a “01”. | MFS25094 |
| RNM610-09 | Campo QUANT_BC_COFINS:  Gerar nulo (“||”). | MFS25094 |
| RNM610-10 | Campo ALIQ_COFINS_QUANT:  Gerar nulo (“||”). | MFS25094 |
| RNM610-11 | Campo VL_CONT_APUR:  Este campo será resultado do seguinte cálculo: Valor informado no campo VL_BC_CONT multiplicado pelo resultado do cálculo (valor do campo ALIQ_COFINS dividido por 100) | MFS25094 |
| RNM610-12 | Campo VL_AJUS_ACRES:  RNG46.3.2.1.189 O valor deste campo deverá ser igual ao somatório do VL_AJ do registro M620 quando IND_AJ = 1. | MFS25094 |
| RNM610-13 | Campo VL_AJUS_REDUC:  RNG46.3.2.1.189 O valor deste campo deverá ser igual ao somatório do VL_AJ do registro M620 quando IND_AJ = 0. | MFS25094 |
| RNM610-14 | Campo VL_CONT_DIFER:  RNG46.3.2.1.191 O valor deste campo deverá ser igual ao somatório do VL_CONT_DIF dos registros M630 relacionados a esse registro M610, informado através do módulo: SPED → EFD-Contribuição Financeira/Assemelhada → Obrigações → Manutenção → Apuração – COFINS → pasta Contribuição para a COFINS no Período (aba “Informações Adicionais de Diferimento – M630”). | MFS25094 |
| RNM610-15 | Campo VL_CONT_DIFER_ANT:  O valor deste campo deverá ser igual ao somatório dos campos VL_CONT_DIFER_ANT do registro M700 relacionados à esse registro M610, informado através do módulo: SPED → EFD-Contribuição Financeira/Assemelhada → Obrigações → Manutenção → Apuração – COFINS → pasta Contribuição para a COFINS no Período (“Contribuição de COFINS Diferida em Períodos Anteriores – M700”). | MFS25094 |
| RNM610-16 | Campo VL_CONT_PER:  Este campo será resultado do cálculo: (Valor do campo VL_CONT_APUR mais valor do campo VL_AJUS_ACRES menos valor do campo VL_AJUS_REDUC menos valor do campo VL_CONT_DIFER mais valor do campo VL_CONT_DIFER_ANT). | MFS25094 |


| RNG-M615 | Este registro será utilizado pela pessoa jurídica para detalhar os totais de ajustes da base de cálculo, informados nos campos 05 e 06 do registro pai M610.  Gerar um registro M615 para cada registro informado através do módulo: EFD-PIS/COFINS, menu: Obrigações → Manutenção → Apuração – COFINS  pasta “Contribuição para o COFINS do Período – M600”  (aba Detalhamento dos Ajustes da BC da COFINS Apurada – M615) ou Obrigações SCP → Manutenção → Apuração – COFINS  pasta “Contribuição para o COFINS do Período – M600”  (aba Detalhamento dos Ajustes da BC da COFINS Apurada – M615), que atenda ao critério abaixo:  Período da Apuração Entre a data inicial e data final de geração do arquivo. 	 Este registro será um agrupamento de informações através dos campos IND_AJ_BC, COD_AJ_BC e NUM_DOC. | MFS25094 |
| --- | --- | --- |
| RNM615-01 | Campo REG  Gravar o conteúdo fixo “M615”. | MFS25094 |
| RNM615-02 | Campo IND_AJ_BC  Campo Tipo de Ajuste da tela de Detalhamento dos Ajustes da BC da COFINS Apurada – M615. | MFS25094 |
| RNM615-03 | Campo VL_AJ_BC  Campo Valor do Ajuste da tela de Detalhamento dos Ajustes da BC da COFINS Apurada – M615. | MFS25094 |


| RNM615-04 | Campo COD_AJ_BC  Campo Código do Ajuste da tela de Detalhamento dos Ajustes da BC da COFINS Apurada – M615. | MFS25094 |
| --- | --- | --- |
| RNM615-05 | Campo NUM_DOC  Campo Número do processo, documento ou ato concessório da tela de Detalhamento dos Ajustes da BC da COFINS Apurada – M615. | MFS25094 |
| RNM615-06 | Campo DESCR_AJ_BC  Campo Descrição Resumida da tela de Detalhamento dos Ajustes da BC da COFINS Apurada – M615. | MFS25094 |
| RNM615-07 | Campo DT_REF  Campo Data Referência da tela de Detalhamento dos Ajustes da BC da COFINS Apurada – M615. | MFS25094 |
| RNM615-08 | Campo COD_CTA  Campo Conta Analítica da tela de Detalhamento dos Ajustes da BC da COFINS Apurada – M615. | MFS25094 |
| RNM615-09 | Campo CNPJ  Campo CNPJ da tela de Detalhamento dos Ajustes da BC da COFINS Apurada – M615. | MFS25094 |
| RNM615-10 | Campo INFO_COMPL  Campo Informação Complementar da tela de Detalhamento dos Ajustes da BC da COFINS Apurada – M615. | MFS25094 |


| RNG-M625 | Deve ser gerado um registro M625 para cada registro incluído através de manutenção no menu: Obrigações > Manutenção > Apuração COFINS > Detalhamento dos Ajustes da Contribuição para a COFINS Apurada – M625 ou Obrigações SCP > Manutenção > Apuração COFINS > Detalhamento dos Ajustes da Contribuição para a COFINS Apurada – M625 e que esteja vinculado ao registro pai, M620.  Este registro será um agrupamento de informações através dos campos DET_VALOR_AJ, CST_COFINS, DET_ALIQ, DT_OPER_AJ e COD_CTA. | OS4316-D |
| --- | --- | --- |
| RNM625-01 | Campo REG  Gravar o conteúdo fixo “M625”. | OS4316-D |
| RNM625-02 | Campo DET_VALOR_AJ  Campo Detalhamento do Valor da tela de Detalhamento dos Ajustes da Contribuição para a COFINS Apurada – M625. | OS4316-D |
| RNM625-03 | Campo CST_PIS  Campo CST da tela de Detalhamento dos Ajustes da Contribuição para a COFINS Apurada – M625. | OS4316-D |
| RNM625-04 | Campo DET_BC_CRED  Campo Detalhamento da BC da tela de Detalhamento dos Ajustes da Contribuição para a COFINS Apurada – M625. | OS4316-D |
| RNM625-05 | Campo DET_ALIQ  Campo Detalhamento da Alíquota da tela de Detalhamento dos Ajustes da Contribuição para a COFINS Apurada – M625. | OS4316-D |
| RNM625-06 | Campo DT_OPER_AJ  Campo Data da Operação da tela de Detalhamento dos Ajustes da Contribuição para a COFINS Apurada – M625. | OS4316-D |
| RNM625-07 | Campo DESC_AJ  Campo Descrição da Operação da tela de Detalhamento dos Ajustes da Contribuição para a COFINS Apurada – M625. | OS4316-D |
| RNM625-08 | Campo COD_CTA  Campo Conta Contábil da tela de Detalhamento dos Ajustes da Contribuição para a COFINS Apurada – M625. A partir da conta contábil informada neste campo deve ser gerado um registro 0500, para demonstrar as informações do cadastro da conta. | OS4316-D |
| RNM625-09 | Campo INFO_COMPL  Campo Informação Complementar da tela de Detalhamento dos Ajustes da Contribuição para a COFINS Apurada – M625. | OS4316-D |


| RNG-M800 | Este registro será gerado com base na parametrização realizada na tela de Parametrização por Conta Contábil, considerando o agrupamento das informações por Código de Situação Tributária da COFINS e Conta Contábil. Ele só existirá quando o Código de Natureza da Receita da parametrização for diferente de nulo e o Código de Situação Tributária da COFINS for igual a “06” ou “07” ou “08” ou “09”.  Este registro é pai do M810. No M810 as informações serão detalhadas por Natureza da Receita e Conta Contábil e aqui por CST e Conta Contábil, sendo que, a conta contábil aqui informada será a sintética das contas analíticas demonstradas no M810.  Registro de nível 2, existirão vários por arquivo e obrigatório quando o Código de Situação Tributária da COFINS for igual a “06” ou “07” ou “08” ou “09”. | OS3810-B |
| --- | --- | --- |
| RNM800-02 | Campo CST_COFINS:  Campo Situação Tributária da COFINS informada na parametrização. | OS3810-B |
| RNM800-03 | Campo VL_TOT_REC:  Este campo será a soma dos valores lançados no campo 03 - VL_REC do registro M810 que são filhos deste registro. | OS3810-B |
| RNM800-04 | Campo COD_CTA:  Será gerado com o código da Conta Contábil do tipo “Sintética” de nível anterior à conta informada no registro filho M810.  Exemplo – Contas: 1.00 (sintética – nível 2) 1.00.00 (sintética – nível 3) 1.00.00.01 (analítica – nível 4) 1.00.00.02 (analítica – nível 4) 1.00.00.00.01 (analítica – nível 5)  No registro filho, M810, estarão as contas analíticas. Neste registro será gerada a conta sintética de nível anterior à conta informada no registro filho. Sendo assim, com base no exemplo, será gerada a conta “1.00.00”.  O cadastro desta conta contábil deverá ser informado no registro 0500. | OS3810-B |
| RNM800-05 | Campo DESC_COMPL:  Gerar nulo (“||”). | OS3810-B |


| RNG-M810 | Este registro será gerado com base na parametrização realizada na tela de Parametrização por Conta Contábil, considerando o agrupamento das informações por Código de Natureza da Receita e Conta Contábil. Ele só existirá quando o Código de Natureza da Receita da parametrização for diferente de nulo e o Código de Situação Tributária do PIS for igual a “06” ou “07” ou “08” ou “09”.  Serão considerados registros da tabela SAFX01 – Arquivo Contábil das Contas Contábeis parametrizadas cuja Data da Operação compreenda o período de geração do arquivo.  Registro de nível 3, para cada ocorrência do registro M800 poderão existir “N” M810 por arquivo e obrigatório quando existir o M800. | OS3810-B |
| --- | --- | --- |
| RNM810-02 | Campo NAT_REC:  Informar neste campo o Código de Natureza da Receita vinculado à parametrização. | OS3810-B |
| RNM810-03 | Campo VL_REC:  Este campo será resultado do cálculo: (soma do Valor do Lançamento Contábil de todos os lançamentos existentes para o período cujo Indicador de Débito/Crédito seja igual a “C”) menos (soma do Valor do Lançamento Contábil de todos os lançamentos existentes para o período cujo Indicador de Débito/Crédito seja igual a “D”).  Mesmo que o resultado apurado seja negativo, deve ser apresentado o valor absoluto (positivo). | OS3810-B |
| RNM810-04 | Campo COD_CTA:  Informar neste campo a Conta Contábil vinculada à parametrização.  O cadastro desta conta contábil deverá ser informado no registro 0500. | OS3810-B |
| RNM810-05 | Campo DESC_COMPL:  Gerar nulo (“||”). | OS3810-B |


| RNG-M990 | Deve ser gerado um registro M990 por arquivo.  Registro de nível 1, ocorrência de 1 por arquivo e obrigatório. | OS3810-B |
| --- | --- | --- |
| RNM990-02 | Campo QTD_LIN_M:  Quantidade de registros do Bloco P. | OS3810-B |


| RNG-P001 | Deve ser gerado um registro P001 por arquivo.  Registro de nível 1, ocorrência de 1 por arquivo e obrigatório.  Ao gerar os registros de abertura e encerramento do bloco P – P001 e P990 – o registro 0145 não deve ser gerado. | OS3810-B |
| --- | --- | --- |
| RNP001-02 | Campo IND_MOV  Gerar fixo “1”. | OS3810-B |


| RNG-P990 | Deve ser gerado um registro P990 por arquivo.  Registro de nível 1, ocorrência de 1 por arquivo e obrigatório.  Ao gerar os registros de abertura e encerramento do bloco P – P001 e P990 – o registro 0145 não deve ser gerado. | OS3810-B |
| --- | --- | --- |
| RNP990-02 | Campo QTD_LIN_P:  Quantidade de registros do Bloco P. | OS3810-B |


| RN1001 | Deve ser gerado um registro 1001 por arquivo.  Registro de nível 1, ocorrência de 1 por arquivo e obrigatório. | OS3810-E |
| --- | --- | --- |
| RN1001-01 | Campo IND_MOV  Deverá ser gravado no campo 02 – IND_MOV se esse registro possui informações ou não.  Gravar “0”, caso existam informações a serem demonstradas nos registros 1300 ou 1700. Gravar “1”, caso não existam informações a serem demonstradas nos registros 1300 ou 1700. | OS3810-E |


| RNG-1050 | Este registro será utilizado pela pessoa jurídica para detalhar os totais de valores extra apuração, objeto de ajustes no Bloco M. Poderá existir um detalhamento com data de referência, indicador de natureza e apropriação de ajuste para a mesma apuração. Esse registro será gerado de acordo com o cadastro efetuado através da tela de  Detalhamento de Ajustes de BC - Valores Extra Escrituração - 1050, localizado no módulo: SPED   EFD-Escrituração Fiscal Digital das Contribuições, menu:  Obrigações  Manutenção   Registros do Bloco I   Ajustes BC - Valores Extra Escrituração – (1050). | MFS25094 |
| --- | --- | --- |
| RN1050-01 | Campo REG Gerar o texto fixo “1050”. | MFS25094 |
| RN1050-02 | Campo DT_REF Preencher com o conteúdo informado no campo Data Referência considerando a tela descrita na RNG-1050. Formato DDMMAAAA. Observação: Esse campo não é obrigatório, então quando estiver nulo na tabela deverá ser gravado nulo na geração do arquivo magnético. | MFS25094 |
| RN1050-03 | Campo IND_AJ_BC Preencher com o conteúdo informado no campo Indicador Natureza considerando a tela descrita na RNG-1050. | MFS25094 |


| RN1050-04 | Campo CNPJ Preencher com o conteúdo informado no campo CNPJ considerando a tela descrita na RNG-1050. Formato XXXXXXXXXXXXXX. | MFS25094 |
| --- | --- | --- |
| RN1050-05 | Campo VL_AJ_TOT Preencher com o conteúdo informado no campo Valor Total Ajuste considerando a tela descrita na RNG-1050. | MFS25094 |
| RN1050-06 | Campo VL_AJ_CST01 Preencher com o conteúdo informado no campo Valor Ajuste CST01 considerando a tela descrita na RNG-1050. | MFS25094 |
| RN1050-07 | Campo VL_AJ_CST02 Preencher com o conteúdo informado no campo Valor Ajuste CST02 considerando a tela descrita na RNG-1050. | MFS25094 |
| RN1050-08 | Campo VL_AJ_CST03 Preencher com o conteúdo informado no campo Valor Ajuste CST03 considerando a tela descrita na RNG-1050. | MFS25094 |
| RN1050-09 | Campo VL_AJ_CST04 Preencher com o conteúdo informado no campo Valor Ajuste CST04 considerando a tela descrita na RNG-1050. | MFS25094 |
| RN1050-10 | Campo VL_AJ_CST05 Preencher com o conteúdo informado no campo Valor Ajuste CST05 considerando a tela descrita na RNG-1050. | MFS25094 |
| RN1050-11 | Campo VL_AJ_CST06 Preencher com o conteúdo informado no campo Valor Ajuste CST06 considerando a tela descrita na RNG-1050. | MFS25094 |
| RN1050-12 | Campo VL_AJ_CST07 Preencher com o conteúdo informado no campo Valor Ajuste CST07 considerando a tela descrita na RNG-1050. | MFS25094 |
| RN1050-13 | Campo VL_AJ_CST08 Preencher com o conteúdo informado no campo Valor Ajuste CST08 considerando a tela descrita na RNG-1050. | MFS25094 |
| RN1050-14 | Campo VL_AJ_CST09 Preencher com o conteúdo informado no campo Valor Ajuste CST09 considerando a tela descrita na RNG-1050. | MFS25094 |
| RN1050-15 | Campo VL_AJ_CST49 Preencher com o conteúdo informado no campo Valor Ajuste CST49 considerando a tela descrita na RNG-1050. | MFS25094 |
| RN1050-16 | Campo VL_AJ_CST99 Preencher com o conteúdo informado no campo Valor Ajuste CST99 considerando a tela descrita na RNG-1050. | MFS25094 |


| RN1050-17 | Campo IND_APROP Preencher com o conteúdo informado no campo Apropriação Ajuste considerando a tela descrita na RNG-1050. | MFS25094 |
| --- | --- | --- |
| RN1050-18 | Campo NUM_REC Preencher com o conteúdo informado no campo Nº Recibo considerando a tela descrita na RNG-1050. | MFS25094 |
| RN1050-19 | Campo INFO_COMPL Preencher com o conteúdo informado no campo Informação Complementar considerando a tela descrita na RNG-1050. | MFS25094 |


| RNG-1300 | Este registro tem por objetivo realizar o controle dos saldos de valores retidos na fonte de períodos anteriores ao da atual escrituração, bem como totalizar os respectivos valores retidos no atual período da escrituração e que foram devidamente detalhados no registro F600, que atendam os critérios:  Se for retenção na fonte da escrituração atual: No registro F600, o campo VL_RET_PIS esteja preenchido.  Se for uma Retenção na Fonte da Escrituração Períodos Anterior: Somente as retenções na fonte que estejam com o valor maior que zero no campo ‘’Retenção Disponível’’ apresentada na tela, localizada no módulo: SPED → EFD-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – PIS/PASEP → Retenções Disponíveis Demonstrar os créditos disponíveis cujo Mês/Ano seja menor que DT_FIN do registro 0000.  O agrupamento desse registro deve ser feito com base das informações dos seguintes campos: 02 – Indicador de Natureza da Retenção na Fonte (IND_NAT_RET) 03 – Período do Recebimento e da Retenção (PR_REC_RET) | OS3810-E |
| --- | --- | --- |
| RN1300-01 | Registro 1300 - 01 - REG  Deverá ser gravado no campo 01 – REG o texto fixo “1300”. | OS3810-E |
| RN1300-02 | Registro 1300 - 02 - IND_NAT_RET  Se for retenção na fonte da escrituração atual: Neste campo deve ser recuperado o dado do campo IND_NAT_RET do registro F600, considerando as restrições da regra RNG-1300  Se for uma Retenção na Fonte da Escrituração de Períodos Anterior: Neste campo deve ser recuperado o dado informado no campo ‘’Natureza da Retenção na Fonte’’ na tela, localizada no Módulo: SPED → EFD-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – PIS/PASEP → Retenções Disponíveis, considerando as restrições da regra RNG-1300. | OS3810-E |
| RN1300-03 | Registro 1300 - 03 - PR_REC_RET  Se for retenção na fonte da escrituração atual: Esse campo deve ser preenchido com o mês/ano do campo Data do recebimento e retenção, considerando as restrições definidas na regra geral RNG 1300.  Se for uma Retenção na Fonte da Escrituração de Períodos Anterior: Neste campo deve ser recuperado o dado informado no campo ‘’Mês/Ano’’ na tela, localizada no Módulo: SPED → EFD-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – PIS/PASEP → Retenções Disponíveis, considerando as restrições da regra RNG-1300. | OS3810-E |
| RN1300-04 | Registro 1300 - 04 - VL_RET_APU  Se for retenção na fonte da escrituração atual: Esse campo deve ser preenchido com a somatória do campo VL_RET_PIS do registro F600.  Se for uma Retenção na Fonte da Escrituração de Períodos Anterior: Esse campo deve preenchido com o resultado da somatória do campo ‘’Retenção Apurada’’ na tela, localizada: Módulo: SPED → EFD-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – PIS/PASEP → Retenções Disponíveis, considerando as restrições da regra RNG-1300. | OS3810-E |
| RN1300-05 | Registro 1300 - 05 - VL_RET_DED  Se for retenção na fonte da escrituração atual: Esse campo deve ser preenchido com a retenção na fonte gerada no registro F600, que foi utilizada na dedução da contribuição, conforme a regra RNG do registro M200, considerando a restrição da regra RNG 1300.   Se for uma Retenção na Fonte da Escrituração de Períodos Anterior: Esse campo deve ser preenchido com o resultado da somatória do valor dos campos ‘’Retenção Deduzida na Contribuição’’ apresentada na parte Retenção(s) Disponível(s) e na parte Retenção(s) a ser Utilizada(s) no Período na tela do módulo abaixo, considerando as restrições da regra RNG-1300.  SPED → EFD-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – PIS/PASEP → Retenções a Utilizar na Apuração. | OS3810-E |
| RN1300-06 | Registro 1300 - 06 - VL_RET_PER  Se for retenção na fonte da escrituração atual: Deve ser preenchido com zeros “0,00’’  Se for uma Retenção na Fonte da Escrituração de Períodos Anterior: Esse campo deve ser preenchido com a somatória do valor dos campos ‘‘Retenção Utilizada por Pedido de Restituição ’’ apresentado na parte Retenção(s) Disponível(s) e na parte Retenção(s) a ser Utilizada(s) no Período na tela do módulo abaixo, considerando as restrições da regra RNG-1300.   SPED → EFD-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – PIS/PASEP → Retenções a Utilizar na Apuração. | OS3810-E |
| RN1300-07 | Registro 1300 - 07 - VL_RET_DCOMP  Se for retenção na fonte da escrituração atual: Deve ser preenchido com zeros “0.00’’  Se for uma Retenção na Fonte da Escrituração de Períodos Anterior: Esse campo deve ser preenchido com o valor informado no campo ‘’Retenção Utilizada por Declaração da Compensação’’, apresentado parte Retenção(s) Disponível(s) e na parte Retenção(s) a ser Utilizada(s) no Período na tela do módulo abaixo, considerando as restrições da regra RNG-1300.   SPED → EFD-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – PIS/PASEP → Retenções a Utilizar na Apuração, considerando as restrições da regra RNG-1300. | OS3810-E |
| RN1300-08 | Registro 1300 - 08 - SLD_RET  Esse campo deve ser igual 04-VL_RET_APU menos 05-VL_RET_DED menos 06-VL_RET_PER menos 07-VL_RET_DCOMP. | OS3810-E |


| RNG-1700 | Este registro tem por objetivo realizar o controle dos saldos de valores retidos na fonte de períodos anteriores ao da atual escrituração, bem como totalizar os respectivos valores retidos no atual período da escrituração e que foram devidamente detalhados no registro F600, que atendam os critérios:  Se for retenção na fonte da escrituração atual: No registro F600, o campo VL_RET_COFINS esteja preenchido.  Se for uma Retenção na Fonte da Escrituração Períodos Anterior: Somente as retenções na fonte que estejam com o valor maior que zero no campo ‘’Retenção Disponível’’ apresentada na tela, localizada no módulo: SPED → EFD-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – COFINS → Retenções Disponíveis Demonstrar os créditos disponíveis cujo Mês/Ano seja menor que DT_FIN do registro 0000.  O agrupamento desse registro deve ser feito com base das informações dos seguintes campos: 02 – Indicador de Natureza da Retenção na Fonte (IND_NAT_RET) 03 – Período do Recebimento e da Retenção (PR_REC_RET) | OS3810-E |
| --- | --- | --- |
| RN1700-01 | Registro 1700 - 01 - REG  Deverá ser gravado no campo 01 – REG o texto fixo “1700”. | OS3810-E |
| RN1700-02 | Registro 1700 - 02 - IND_NAT_RET  Se for retenção na fonte da escrituração atual: Neste campo deve ser recuperado o dado do campo IND_NAT_RET do registro F600, considerando as restrições da regra RNG-1700  Se for uma Retenção na Fonte da Escrituração de Períodos Anterior: Neste campo deve ser recuperado o dado informado no campo ‘’Natureza da Retenção na Fonte’’ na tela, localizada no Módulo: SPED → EFD-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – COFINS → Retenções Disponíveis, considerando as restrições da regra RNG-1700. | OS3810-E |
| RN1700-03 | Registro 1700 - 03 - PR_REC_RET  Se for retenção na fonte da escrituração atual: Esse campo deve ser preenchido com o mês/ano do campo Data do recebimento e retenção, considerando as restrições definidas na regra geral RNG 1700.  Se for uma Retenção na Fonte da Escrituração de Períodos Anterior: Neste campo deve ser recuperado o dado informado no campo ‘’Mês/Ano’’ na tela, localizada no Módulo: SPED → EFD-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – COFINS → Retenções Disponíveis, considerando as restrições da regra RNG-1700. | OS3810-E |
| RN1700-04 | Registro 1700 - 04 - VL_RET_APU  Se for retenção na fonte da escrituração atual: Esse campo deve ser preenchido com a somatória do campo VL_RET_COFINS do registro F600.  Se for uma Retenção na Fonte da Escrituração de Períodos Anterior: Esse campo deve preenchido com o resultado da somatória do campo ‘’Retenção Apurada’’ na tela, localizada: Módulo: SPED → EFD-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – COFINS → Retenções Disponíveis, considerando as restrições da regra RNG-1700. | OS3810-E |
| RN1700-05 | Registro 1700 - 05 - VL_RET_DED  Se for retenção na fonte da escrituração atual: Esse campo deve ser preenchido com a retenção na fonte gerada no registro F600, que foi utilizada na dedução da contribuição, conforme a regra RNG do registro M200, considerando a restrição da regra RNG 1700.   Se for uma Retenção na Fonte da Escrituração de Períodos Anterior: Esse campo deve ser preenchido com o resultado da somatória do valor dos campos ‘’Retenção Deduzida na Contribuição’’ apresentada na parte Retenção(s) Disponível(s) e na parte Retenção(s) a ser Utilizada(s) no Período na tela do módulo abaixo, considerando as restrições da regra RNG-1700.  SPED → EFD-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – COFINS → Retenções a Utilizar na Apuração. | OS3810-E |
| RN1700-06 | Registro 1700 - 06 - VL_RET_PER  Se for retenção na fonte da escrituração atual: Deve ser preenchido com zeros “0,00’’  Se for uma Retenção na Fonte da Escrituração de Períodos Anterior: Esse campo deve ser preenchido com a somatória do valor dos campos ‘‘Retenção Utilizada por Pedido de Restituição ’’ apresentado na parte Retenção(s) Disponível(s) e na parte Retenção(s) a ser Utilizada(s) no Período na tela do módulo abaixo, considerando as restrições da regra RNG-1700.   SPED → EFD-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – COFINS → Retenções a Utilizar na Apuração. | OS3810-E |
| RN1700-07 | Registro 1700 - 07 - VL_RET_DCOMP  Se for retenção na fonte da escrituração atual: Deve ser preenchido com zeros “0.00’’  Se for uma Retenção na Fonte da Escrituração de Períodos Anterior: Esse campo deve ser preenchido com o valor informado no campo ‘’Retenção Utilizada por Declaração da Compensação’’, apresentado parte Retenção(s) Disponível(s) e na parte Retenção(s) a ser Utilizada(s) no Período na tela do módulo abaixo, considerando as restrições da regra RNG-1700.   SPED → EFD-Contribuições Financeira/Assemelhada → Obrigações → Manutenção → Controle de Retenções na Fonte – COFINS → Retenções a Utilizar na Apuração, considerando as restrições da regra RNG-1700. | OS3810-E |
| RN1700-08 | Registro 1700 - 08 - SLD_RET  Esse campo deve ser igual 04-VL_RET_APU menos 05-VL_RET_DED menos 06-VL_RET_PER menos 07-VL_RET_DCOMP. | OS3810-E |


| RNG-P990 | Deve ser gerado um registro 1990 por arquivo.  Registro de nível 1, ocorrência de 1 por arquivo e obrigatório. | OS3810-E |
| --- | --- | --- |
| RNP990-02 | Campo QTD_LIN_1:  Quantidade de registros do Bloco 1. | OS3810-E |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |


| RN01 | [ALTERADA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |
