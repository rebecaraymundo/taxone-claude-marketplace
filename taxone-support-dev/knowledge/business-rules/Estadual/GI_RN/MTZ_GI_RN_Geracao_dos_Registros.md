# MTZ_GI_RN_Geracao_dos_Registros

- **Fonte:** MTZ_GI_RN_Geracao_dos_Registros.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 78 KB

---

THOMSON REUTERS

Guia de Informação das Operações e Prestações Interestaduais – RN

GI\-RN

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS624

Julyana Perrucini

Este documento tem como objetivo criar o módulo GI\-RN\.

Sumário

[1\.	REGRAS DOS CAMPOS	3](#_Toc427077977)

[2\.	REGRAS DE GERAÇÃO DO RELATÓRIO	3](#_Toc427077978)

[2\.1\.	Layout do Relatório	15](#_Toc427077979)

# <a id="_Toc350763252"></a><a id="_Toc427077977"></a>REGRAS DOS CAMPOS 

Verificar documento Matriz: MTZ\_GI\_RN\_Tela\_Geracao\_dos\_Registros\.docx\.

# <a id="_Toc427077978"></a>REGRAS DE GERAÇÃO DO RELATÓRIO 

__Origem das informações para geração:__ 

- Tela de Empresa/Estabelecimento do módulo Básicos – Parâmetros \(tabela estabelecimento\), localizado no item de menu: Preliminares >> Empresa/Estabelecimento\.
- Tela de Inscrições Estaduais do módulo Básicos – Parâmetros \(tabela registro\_estadual\), localizado no item de menu: Preliminares >> Inscrições Estaduais\.
- Tela de <a id="OLE_LINK13"></a><a id="OLE_LINK14"></a><a id="OLE_LINK15"></a>Empresas/Estabelecimentos c/ Insc\. Estadual Única do módulo Estadual – <a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a>Controle de Obrigações Acessórias \(tabela icp\_insc\_est\_centr\), localizado no item de menu: Obrigações >> Empresas/Estabelecimentos c/ Insc\. Estadual Única\.
- Parâmetros p/Geração dos Dados Acessórios do módulo Estadual – GI\-RN \(tabela est\_par\_dados\_acs\), localizado no item de menu: Parâmetros >> Parâmetros p/Geração dos Dados\.
- Resumo por UF – Entradas e UF – Saídas do módulo Estadual – Obrigações Acessórias \(tabela est\_res\_uf\_01\), localizado no item de menu: Relatórios >> Resumo das Operações\.

__Regra de seleção: __

- <a id="OLE_LINK8"></a><a id="OLE_LINK9"></a>Considerar os campos necessários da tabela est\_res\_uf\_01 para utilização na Guia, mas seguir os seguintes critérios:
	- A empresa e o estabelecimento devem compreender a empresa e o estabelecimento preenchidos na tela de geração dos registros;
	- A apuração do resumo por UF deve compreender a data inicial e final preenchidas na tela de geração dos registros;
	- Para indicador igual a E \(UF – Entradas\), consolidar as informações no quadro de Entradas de Mercadorias, Bens e/ou Aquisições de Serviços;
	- Para indicador igual a S \(UF – Saídas\), inserir as informações no quadro de Entradas de Mercadorias, Bens e/ou Aquisições de Serviços;
- Quando o parâmetro “__Geração centralizada por Inscrição Estadual Única__” estiver selecionado, recuperar as informações de todos os estabelecimentos cadastrados na tabela icp\_insc\_est\_centr referentes ao estabelecimento centralizador escolhido na tela de geração\.

__Regra de gravação: __Os dados a ser considerados são do estabelecimento em questão, exceto se a geração for por Inscrição Estadual Única, pois nesse caso de geração, os dados cadastrais a ser considerados são do estabelecimento centralizador e deverá ser realizados os acúmulos de valores de seus centralizados\.

__Regra de agrupamento: __Não se aplica\.

__Ordenação: __Não se aplica\.

__Considerações: __Não é obrigatório o cliente ter o módulo “Obrigações Acessórias”, então o intuito é executar a geração a partir da GI\-RN, de acordo com o parâmetro Gerar Dados Acessórios da tela de geração dos registros, para obtenção das informações do Resumo por UF \(tabela est\_res\_uf\_01\), sendo necessária a parametrização em Parâmetros p/Geração dos Dados Acessórios do módulo Estadual – GI\-RN, pois essa rotina é padrão e utilizada nas demais obrigações estaduais\. Por esse motivo, no preenchimento dos campos utilizaremos a forma “funcional” e “técnica”, ou seja, resumo e a tabela do resumo\.

__Campo/Coluna__

__Tipo__

__Formato/Default__

__Regra__

__MFS/CH__

__Dados do Cabeçalho__

Identificação da Unidade Federada

Texto

Formato: 

Text Area

Default:

Fixo

Conteúdo fixo “IDENTIFICAÇÃO DA UNIDADE FEDERADA”\.

MFS624

Guia de Informação das Operações e Prestações Interestaduais

Texto

Formato: 

Text Area

Default:

Fixo

Conteúdo fixo “GUIA DE INFORMAÇÃO DAS OPERAÇÕES E PRESTAÇÕES INTERESTADUAIS \- GI/ICMS”\.

MFS624

Firma ou Razão Social

Texto

Formato: 

Text Area

Default:

Não se aplica

Preencher com o conteúdo do campo Razão Social da tela de Empresa/Estabelecimento do estabelecimento selecionado na geração dos registros\.

MFS624

Inscrição Estadual

Texto

Formato: 

Text Area

Default:

Não se aplica

Preencher com o conteúdo do campo Inscrição Estadual quando o campo U\.F for igual a RN da tela de Inscrições Estaduais do estabelecimento selecionado na geração dos registros\.

MFS624

CGC/MF

Texto

Formato: 

99\.999\.999/9999\-99

Default:

Não se aplica

Preencher com o conteúdo do campo CNPJ da tela de Empresa/Estabelecimento do estabelecimento selecionado na geração dos registros\.

MFS624

Período de Referência de \_\_ a \_\_

Texto

Formato: 

DD/MM/AAAA a DD/MM/AAAA

Default:

Não se aplica

Preencher com o conteúdo dos campos Data Inicial e Data Final da tela de geração dos registros\.

MFS624

Endereço \(Logradouro, rua, av\. etc\)

Texto

Formato: 

Text Area

Default:

Não se aplica

Preencher com o conteúdo dos campos Tipo Logradouro e Endereço da tela de Empresa/Estabelecimento do estabelecimento selecionado na geração dos registros\.

MFS624

Nº

Texto

Formato: 

Text Area

Default:

Não se aplica

Preencher com o conteúdo do campo Número da tela de Empresa/Estabelecimento do estabelecimento selecionado na geração dos registros\.

MFS624

Complemento

Texto

Formato: 

Text Area

Default:

Não se aplica

Preencher com o conteúdo do campo Complemento da tela de Empresa/Estabelecimento do estabelecimento selecionado na geração dos registros\.

MFS624

Bairro ou Distrito

Texto

Formato: 

Text Area

Default:

Não se aplica

Preencher com o conteúdo do campo Bairro da tela de Empresa/Estabelecimento do estabelecimento selecionado na geração dos registros\.

__Tratamento:__

- Se o campo Bairro não estiver preenchido, considerar o conteúdo do campo Distrito\.

MFS624

Município

Texto

Formato: 

Text Area

Default:

Não se aplica

Preencher com a descrição do conteúdo do campo Município da tela de Empresa/Estabelecimento do estabelecimento selecionado na geração dos registros\.

MFS624

CEP

Texto

Formato: 

Text Area

Default:

Não se aplica

Preencher com o conteúdo do Cep da tela de Empresa/Estabelecimento do estabelecimento selecionado na geração dos registros\.

MFS624

__Corpo do Relatório \- ENTRADAS DE MERCADORIAS, BENS E/OU AQUISIÇÕES DE SERVIÇOS__

Entradas de Mercadorias, Bens e/ou Aquisições de Serviços

Texto

Formato: 

Text Area

Default:

Fixo

Conteúdo fixo “ENTRADAS DE MERCADORIAS, BENS E/OU AQUISIÇÕES DE SERVIÇOS:”\.

Esse quadro de entradas receberá as informações do Resumo por UF – Entradas \(campo IND\_E\_S igual a E da tabela\)\.

MFS624

Código e Unidade da Federação de Origem

Texto

Formato: 

Text Area

Default:

Fixo

Essa coluna deve vir com o conteúdo fixo “CÓDIGO E UNIDADE DA FEDERAÇÃO DE ORIGEM”\.

Tem como objetivo listar todos os códigos e unidades de federação utilizadas na GI/ICMS\.

__Campos fixos da coluna:__

01\. ACRE			

02\. ALAGOAS			

03\. AMAPÁ			

04\. AMAZONAS			

05\. BAHIA			

06\. CEARÁ			

07\. DISTRITO FEDERAL		

08\. ESPÍRITO SANTO			

10\. GOIÁS			

12\. MARANHÃO			

13\. MATO GROSSO			

28\. MATRO GROSSO DO SUL	

14\. MINAS GERAIS			

15\. PARÁ			

16\. PARAÍBA			

17\. PARANÁ			

18\. PERNAMBUCO			

19\. PIAUÍ			

20\. RIO GRANDE DO NORTE

21\. RIO GRANDE DO SUL

22\. RIO DE JANEIRO			

23\. RONDÔNIA			

24\. RORAIMA			

25\. SANTA CATARINA			

26\. SÃO PAULO			

27\. SERGIPE			

29\. TOCANTINS			

TOTAIS		

MFS624

Valor Contábil

Numérico

Formato: 

0,00

Default:

Não se aplica

Preencher com o conteúdo do campo Valor Contábil do Resumo por UF – Entradas \(campo VLR\_CONTABIL da tabela\) para a UF correspondente \(campo IDENT\_ESTADO\) ao Código e Unidade da Federação de Origem da Guia\.

*Exemplo:*

IDENT\_ESTADO = 76 \(SP\) correspondente ao código “26\. SÃO PAULO” da Guia\.

__Tratamento:__

- Quando não houver resultado para os códigos e unidades de federação utilizadas na GI/ICMS, preencher com zeros \(0,00\)\.

MFS624

Base de Cálculo

Numérico

Formato: 

0,00

Default:

Não se aplica

Preencher com o conteúdo do campo Base de Cálculo do Resumo por UF – Entradas \(campo VLR\_BASE\_ICMS da tabela\) para a UF correspondente \(campo IDENT\_ESTADO\) ao Código e Unidade da Federação de Origem da Guia\.

*Exemplo:*

IDENT\_ESTADO = 76 \(SP\) correspondente ao código “26\. SÃO PAULO” da Guia\.

__Tratamento:__

- Quando não houver resultado para os códigos e unidades de federação utilizadas na GI/ICMS, preencher com zeros \(0,00\)\.

MFS624

Outras

Numérico

Formato: 

0,00

Default:

Não se aplica

Preencher com o conteúdo do campo Outras do Resumo por UF – Entradas \(campo VLR\_BASE\_OUTRAS da tabela\) para a UF correspondente \(campo IDENT\_ESTADO\) ao Código e Unidade da Federação de Origem da Guia\.

*Exemplo:*

IDENT\_ESTADO = 76 \(SP\) correspondente ao código “26\. SÃO PAULO” da Guia\.

__Tratamento:__

- Quando não houver resultado para os códigos e unidades de federação utilizadas na GI/ICMS, preencher com zeros \(0,00\)\.

MFS624

ICMS Cobrado por Substituição Tributária – Petróleo/Energia

Numérico

Formato: 

0,00

Default:

Não se aplica

Preencher com o conteúdo do campo Petróleo / Energia do Resumo por UF – Entradas \(campo VLR\_ICMS\_PET da tabela\) para a UF correspondente \(campo IDENT\_ESTADO\) ao Código e Unidade da Federação de Origem da Guia\.

*Exemplo:*

IDENT\_ESTADO = 76 \(SP\) correspondente ao código “26\. SÃO PAULO” da Guia\.

__Tratamento:__

- Quando não houver resultado para os códigos e unidades de federação utilizadas na GI/ICMS, preencher com zeros \(0,00\)\.

*Observação:* a coluna ICMS Cobrado por Substituição Tributária será fixa para indicar o resultado das colunas Petróleo/Energia e Outros Produtos\.

MFS624

ICMS Cobrado por Substituição Tributária – Outros Produtos

Numérico

Formato: 

0,00

Default:

Não se aplica

Preencher com o conteúdo do campo Petróleo / Energia do Resumo por UF – Entradas \(campo VLR\_ICMS\_OUT da tabela\) para a UF correspondente \(campo IDENT\_ESTADO\) ao Código e Unidade da Federação de Origem da Guia\.

*Exemplo:*

IDENT\_ESTADO = 76 \(SP\) correspondente ao código “26\. SÃO PAULO” da Guia\.

__Tratamento:__

- Quando não houver resultado para os códigos e unidades de federação utilizadas na GI/ICMS, preencher com zeros \(0,00\)\.

*Observação:* a coluna ICMS Cobrado por Substituição Tributária será fixa para indicar o resultado das colunas Petróleo/Energia e Outros Produtos\.

MFS624

Local e Data

Texto

Formato: 

0,00

Default:

Fixo

Conteúdo fixo “LOCAL E DATA”\.

Esse campo deverá vir no final do relatório, após o campo TOTAIS\.

Será deixado em branco para preenchimento manual do usuário\.

MFS624

Nome e Assinatura

Texto

Formato: 

0,00

Default:

Fixo

Conteúdo fixo “NOME E ASSINATURA DO RESPONSÁVEL”\.

Esse campo deverá vir no final do relatório, após as colunas de valores\.

Será deixado em branco para preenchimento manual do usuário\.

MFS624

__Corpo do Relatório \- SAÍDAS DE MERCADORIAS E/OU PRESTAÇÃO DE SERVIÇOS__

Saídas de Mercadorias e/ou Prestação de Serviços

Texto

Formato: 

Text Area

Default:

Fixo

Conteúdo fixo “SAÍDAS DE MERCADORIAS E/OU PRESTAÇÃO DE SERVIÇOS:”\.

Esse quadro de entradas receberá as informações do Resumo por UF – Entradas \(campo IND\_E\_S igual a S da tabela\)\.

MFS624

Código e Unidade da Federação de Origem

Texto

Formato: 

Text Area

Default:

Fixo

Essa coluna deve vir com o conteúdo fixo “CÓDIGO E UNIDADE DA FEDERAÇÃO DE ORIGEM”\.

Tem como objetivo listar todos os códigos e unidades de federação utilizadas na GI/ICMS\.

__Campos fixos da coluna:__

01\. ACRE			

02\. ALAGOAS			

03\. AMAPÁ			

04\. AMAZONAS			

05\. BAHIA			

06\. CEARÁ			

07\. DISTRITO FEDERAL		

08\. ESPÍRITO SANTO			

10\. GOIÁS			

12\. MARANHÃO			

13\. MATO GROSSO			

28\. MATRO GROSSO DO SUL		

14\. MINAS GERAIS			

15\. PARÁ			

16\. PARAÍBA			

17\. PARANÁ			

18\. PERNAMBUCO			

19\. PIAUÍ			

20\. RIO GRANDE DO NORTE

21\. RIO GRANDE DO SUL

22\. RIO DE JANEIRO			

23\. RONDÔNIA			

24\. RORAIMA			

25\. SANTA CATARINA			

26\. SÃO PAULO			

27\. SERGIPE			

29\. TOCANTINS			

TOTAIS		

MFS624

Valor Contábil – Não Contrib\.

Numérico

Formato: 

0,00

Default:

Não se aplica

Preencher com o conteúdo do campo Não Contribuinte da coluna Valor Contábil do Resumo por UF – Saídas \(campo VLR\_CONTABIL\_NC da tabela\) para a UF correspondente \(campo IDENT\_ESTADO\) ao Código e Unidade da Federação de Origem da Guia\.

*Exemplo:*

IDENT\_ESTADO = 76 \(SP\) correspondente ao código “26\. SÃO PAULO” da Guia\.

__Tratamento:__

- Quando não houver resultado para os códigos e unidades de federação utilizadas na GI/ICMS, preencher com zeros \(0,00\)\.

MFS624

Valor Contábil – Contrib\.

Numérico

Formato: 

0,00

Default:

Não se aplica

Preencher com o conteúdo do campo Contribuinte da coluna Valor Contábil do Resumo por UF – Saídas \(campo VLR\_CONTABIL\_C da tabela\) para a UF correspondente \(campo IDENT\_ESTADO\) ao Código e Unidade da Federação de Origem da Guia\.

*Exemplo:*

IDENT\_ESTADO = 76 \(SP\) correspondente ao código “26\. SÃO PAULO” da Guia\.

__Tratamento:__

- Quando não houver resultado para os códigos e unidades de federação utilizadas na GI/ICMS, preencher com zeros \(0,00\)\.

MFS624

Base de Cálculo – Não Contrib\.

Numérico

Formato: 

0,00

Default:

Não se aplica

Preencher com o conteúdo do campo Não Contribuinte da coluna Base de Cálculo do Resumo por UF – Saídas \(campo VLR\_BASE\_ICMS\_NC da tabela\) para a UF correspondente \(campo IDENT\_ESTADO\) ao Código e Unidade da Federação de Origem da Guia\.

*Exemplo:*

IDENT\_ESTADO = 76 \(SP\) correspondente ao código “26\. SÃO PAULO” da Guia\.

__Tratamento:__

- Quando não houver resultado para os códigos e unidades de federação utilizadas na GI/ICMS, preencher com zeros \(0,00\)\.

MFS624

Base de Cálculo – Contrib\.

Numérico

Formato: 

0,00

Default:

Não se aplica

Preencher com o conteúdo do campo Contribuinte da coluna Base de Cálculo do Resumo por UF – Saídas \(campo VLR\_BASE\_ICMS\_C da tabela\) para a UF correspondente \(campo IDENT\_ESTADO\) ao Código e Unidade da Federação de Origem da Guia\.

*Exemplo:*

IDENT\_ESTADO = 76 \(SP\) correspondente ao código “26\. SÃO PAULO” da Guia\.

__Tratamento:__

- Quando não houver resultado para os códigos e unidades de federação utilizadas na GI/ICMS, preencher com zeros \(0,00\)\.

MFS624

Outras

Numérico

Formato: 

0,00

Default:

Não se aplica

Preencher com o conteúdo do campo Outras do Resumo por UF – Saídas \(campo VLR\_BASE\_OUTRAS da tabela\) para a UF correspondente \(campo IDENT\_ESTADO\) ao Código e Unidade da Federação de Origem da Guia\.

*Exemplo:*

IDENT\_ESTADO = 76 \(SP\) correspondente ao código “26\. SÃO PAULO” da Guia\.

__Tratamento:__

- Quando não houver resultado para os códigos e unidades de federação utilizadas na GI/ICMS, preencher com zeros \(0,00\)\.

MFS624

ICMS Cobrado por Sub\. Trib\.

Numérico

Formato: 

0,00

Default:

Não se aplica

Preencher com o conteúdo do campo ICMS Cobrado p/Sub\. Trib\. do Resumo por UF – Saídas \(campo VLR\_ICMS\_S da tabela\) para a UF correspondente \(campo IDENT\_ESTADO\) ao Código e Unidade da Federação de Origem da Guia\.

*Exemplo:*

IDENT\_ESTADO = 76 \(SP\) correspondente ao código “26\. SÃO PAULO” da Guia\.

__Tratamento:__

- Quando não houver resultado para os códigos e unidades de federação utilizadas na GI/ICMS, preencher com zeros \(0,00\)\.

*Observação:* a coluna ICMS Cobrado por Substituição Tributária será fixa para indicar o resultado das colunas Petróleo/Energia e Outros Produtos\.

MFS624

Local e Data

Texto

Formato: 

0,00

Default:

Fixo

Conteúdo fixo “LOCAL E DATA”\.

Esse campo deverá vir no final do relatório, após o campo TOTAIS\.

Será deixado em branco para preenchimento manual do usuário\.

MFS624

Nome e Assinatura

Texto

Formato: 

0,00

Default:

Fixo

Conteúdo fixo “NOME E ASSINATURA DO RESPONSÁVEL”\.

Esse campo deverá vir no final do relatório, após as colunas de valores\.

Será deixado em branco para preenchimento manual do usuário\.

MFS624

## <a id="_Toc427077979"></a>Layout do Relatório

Verificar o documento LAYOUT\_GI\_RN\.xls\.

