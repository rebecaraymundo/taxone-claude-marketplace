# MTZ_ICMS_Convenio_ICMS_201_Geracao_Meio_Magnetico_Pre_Pago

- **Fonte:** MTZ_ICMS_Convenio_ICMS_201_Geracao_Meio_Magnetico_Pre_Pago.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 69 KB

---

THOMSON REUTERS

Geração Arquivo Magnético  
Convênio ICMS 201/2017 – Carregamento de Créditos em Terminais Telefônicos Pré\-pagos

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS\-16140

Julyana Perrucini

Este documento tem como objetivo incluir a geração do arquivo magnético auxiliar contendo informações obtidas diretamente da plataforma de controle de créditos, devendo espelhar os valores totais das recargas realizadas pelos usuários, em atendimento ao Convênio ICMS 201/2017\.

MFS\-17767

Julyana Perrucini

Este documento tem como objetivo atender o Convênio ICMS n° 31/2018\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN00

__Regras Gerais__

A geração de o arquivo magnético auxiliar referente aos terminais telefônicos pré\-pagos foi criada pela MFS\-16140 para contribuintes prestadores de serviços de comunicação que emitem seus documentos fiscais nos termos do Convênio ICMS 115/03, que dispõe sobre a uniformização e disciplina a emissão, escrituração, manutenção e prestação das informações dos documentos fiscais emitidos em via única por sistema eletrônico de processamento de dados para contribuintes prestadores de serviços de comunicação e fornecedores de energia elétrica\.

Esse arquivo somente será gerado quando o campo Convênio ICMS 201 – Pré\-Pago no item “Gerar Arquivo Auxiliar” estiver marcado na tela de Geração dos Arquivos Magnéticos para o Convênio 115, do módulo ICMS\.

MFS\-16140

RN01

__Dados Técnicos da Geração dos Arquivos__

__*Formato do Arquivo:*__

- Formatação: compatível com MS\-DOS;
- Tamanho do arquivo: 238 bytes, acrescidos de CR/LF \(Carriage Return/Line Feed\) ao final de cada registro;
- Organização: sequencial;
- Codificação: ASCII \- ISO 8859\-1 \(Latin\-1\)\.

MFS\-16140

RN02

__Regra para Identificação do Arquivo__

Se o__ __item “Gerar Arquivo Auxiliar” da tela de Geração dos Arquivos Magnéticos para o Convênio 115 do módulo ICMS estiver marcado com a opção igual a Convênio ICMS 201 – Pré\-Pago, os arquivos serão identificados no formato:

__UUCCCCCCCCCCCCCCAAMMPPSV\.TXT__

- __UU:__ UF – preencher com sigla da unidade federada do emitente dos documentos fiscais;
- __CCCCCCCCCCCCCC: __CNPJ – preencher com o CNPJ do contribuinte emitente dos documentos fiscais;
- __AA: __Ano – preencher com o ano de emissão dos documentos fiscais;
- __MM: __Mês – preencher com o mês do período de apuração dos documentos fiscais;
- __PP: __Tipo – informação fixa “PP”, significando pré\-pago;
- __S: __Situação – indica se o arquivo é normal \(N\) ou substituto \(S\) de acordo com o status do arquivo principal;
- __V: __Volume – quantidade de registros do arquivo, em que cada volume será composto por até um milhão de faturas comerciais, devendo o volume ser indicado em ordem crescente a partir de 1;
- __\.TXT: __Extensão – a extensão do arquivo deverá ser TXT\.

A quebra do arquivo magnético seguirá por estabelecimento\. Neste contexto, não se aplica a “Geração para Empresas c/ Inscrição Estadual Única”, uma vez que será gerado um arquivo para cada estabelecimento\. Sempre ocorrerá a quebra do arquivo considerando os campos que compõe a nomenclatura do mesmo\.

MFS\-16140

RN03

__Regra p/ Recuperação dos Dados__

__*Origem das Informações para geração:*__

- Tela de Empresa/Estabelecimento do módulo Básicos – Parâmetros \(tabela estabelecimento\), localizado no item de menu: Preliminares >> Empresa/Estabelecimento;
- SAFX261 – Terminais Telefônicos Pré\-pagos do módulo Básicos – MasterSAF DW, localizado no item de menu: Manutenção Telecom\.

__*Regra de seleção geral: *__

Selecionar os registros processados das tabelas dadas como origem, com os seguintes filtros:

- Código da Empresa = Código da Empresa \(relacionado ao Estabelecimento selecionado na tela de geração\);
- Código do Estabelecimento = Código do Estabelecimento selecionado na tela de geração;
- Data de requisição da recarga enquadrada no mês e ano da apuração informada na tela de geração \(campo 06\- DATA\_RECARGA da SAFX261\);

__*Regra de gravação geral:* __Verificar documento de DEPARA\_Convenio\_ICMS\_201\_Fatura\_e\_Pre\-Pago\.xls \(aba DExPARA PRE\-PAGO\) para obtenção dos resultados, as regras contidas a seguir são campos que necessitam de tratamento e mensagem de log\.

__*Regra de agrupamento:* __Não se aplica\.

__*Ordenação:* __Ordem crescente por data da recarga e CPF/CNPJ \(Usuário, Vendedor e Responsável pelo Repasse\)\.

__*Considerações:*__ Não se aplica\.

MFS\-16140

<a id="_Hlk506977735"></a>RNPP\-03

__Campo 03\-NOME/RAZÃO SOCIAL DO USUÁRIO__

__Tratamento:__

- Considerar as 35 primeiras posições\.

MFS\-16140

<a id="_Hlk506978042"></a>RNPP\-04

__Campo 04\-Nº DO TERMINAL TELEFÔNICO__

__\[ALTERADA – MFS\-17767\]__

__Tratamento:__

- Se o campo estiver preenchido com mais de 11 12 posições, truncar considerando apenas as 11 12 primeiras e emitir a mensagem de log: “O campo Nº do Terminal Telefônico precisa ter até 11 12 posições, favo verificar <<PFJ Usuário>>, <<Data da Recarga>>, <<PFJ Vendedor>>, <<Produto>>”\.

MFS\-16140

MFS\-17767

<a id="_Hlk506978187"></a>RNPP\-07

__Campo 07\-NOME/RAZÃO SOCIAL DO VENDEDOR DO CRÉDITO__

__Tratamento:__

- Considerar as 35 primeiras posições\.

MFS\-16140

RNPP\-09

__Campo 09\-NOME/RAZÃO SOCIAL DO RESPONSÁVEL PELO REPASSE__

__Tratamento:__

- Considerar as 35 primeiras posições\.

MFS\-16140

RNPP\-10

__Campo 10\-CÓDIGO DO ITEM DE ATIVAÇÃO__

__Tratamento:__

- Considerar as 10 primeiras posições\.

MFS\-16140

RNPP\-11

__Campo 11\-DESCRIÇÃO DO ITEM DE ATIVAÇÃO__

__\[ALTERADA – MFS\-17767\]__

__Tratamento:__

- Considerar as 30 40 primeiras posições\.

MFS\-16140

MFS\-17767

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

