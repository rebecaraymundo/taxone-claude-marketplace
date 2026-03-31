# MTZ-GUIAS DE PAGAMENTO_INTEGRAÇÃO_DOOTAX _EXECUTAR_GERA_FUNDO_ICMS_NORMAL

> Fonte: MTZ-GUIAS DE PAGAMENTO_INTEGRAÇÃO_DOOTAX _EXECUTAR_GERA_FUNDO_ICMS_NORMAL.docx






THOMSON REUTERS

Novo Módulo Integração Guias de Pagamento DOOTAX

















DOCUMENTO DE REQUISITO

Sumário

1.	Objetivo	4
2.	Introdução da função Executar	5
3.	Contexto Inicial da Função EXECUTAR	5
4.	Detalhamento da Função EXECUTAR	6
5.	Inserção de dados em tabelas temporárias	6
5.1. Dependências	6
6.	Procedure GERA_ICMS_NORMAL	7
7.1 Função Interna json	7
7.2 Declaração de Variáveis e Cursores	7
7.3 Processamento Principal	8
7.4. Regras Específicas	8
8. Função calcula_data_vencimento	8
8.1. Lógica de Cálculo	9
9. Fluxo Principal	9
9.1. Select 1	9
9.2. Select 2	10
9.3. Select 3	10
10. Campos Necessários para Requisição de Envio	11
10.1 De/PARA integração DOOTAX – Campos para Requisição de Envio:	11
11. Melhorias e Diferenciais na Jornada do Usuário	16
11.1. Controle de Versão	16
11.2. Segurança na Integração	16
11.3. Detalhamento de Requisições e Respostas	17
11.4. Monitoramento e Suporte	17
12. Conclusão	17






















## Objetivo


O novo módulo de “Guia de Pagamento” foi desenvolvido com base na estrutura de um processo customizado já existente “DOOTAX”. Essa estrutura será reaproveitada e integrada a outro menu dentro do Onesource Tax One e Onesource BR.

O reaproveitamento visa otimizar a implementação, mantendo a lógica de negócio previamente validada e adaptando-a às especificidades do menu onde será inserido. Essa abordagem visa reduzir esforços de implementação, garantir a consistência operacional e facilitar a manutenção futura, assegurando que o novo módulo atenda às necessidades específicas de processamento de Guias de Pagamento.

Deverá transformar a funcionalidade customizada em um módulo produtizável (Produtização = Preparado para comercialização), garantindo que não contenha dados ou referências específicas ao cliente original.

Todas as tabelas, procedures, views e outros objetos do banco de dados relacionados à funcionalidade deverão ser renomeados para evitar conflitos e manter a independência do novo módulo. Os dados existentes associados ao cliente original deverão ser descartados ou tratados para garantir que a nova função seja limpa e genérica. É necessário garantir que nenhuma referência explícita aos dados ou padrões do cliente original permaneça na implementação. Desta forma, é necessário ajustar todas as chamadas de procedures, tabelas e views para refletir os novos nomes, garantindo compatibilidade total com o novo módulo.










## Introdução da função Executar


A função EXECUTAR tem como objetivo principal processar guias de pagamento de impostos, registrando processos e manipulando informações fiscais. Esta documentação detalha sua estrutura, dependências e funcionamento.


## Contexto Inicial da Função EXECUTAR


A função recebe os seguintes parâmetros de entrada:


Dentro da função, é inicializado um identificador de processo (mproc_id), e um novo processo é criado no sistema por meio da biblioteca interna LIB_PROC.









## Detalhamento da Função EXECUTAR


A função EXECUTAR realiza as seguintes operações:

Criação de um processo
Adição de logs
Recuperação de parâmetros
Validação de módulo e diretório

Recupera valores do módulo para uso no processamento.
Valida se o módulo e o diretório existem, gerando logs de atenção quando não encontrados.


## Inserção de dados em tabelas temporárias


Insere dados de estabelecimentos na tabela temporária FLUX_HEINEKEN_ESTAB_TEMP_CPROC.


## 5.1. Dependências


A função depende das seguintes bibliotecas e tabelas:


## Procedure GERA_FUNDO_ICMS_NORMAL


A procedure GERA_FUNDO_ICMS_NORMAL tem como objetivo processar dados fiscais e estruturá-los no formato JSON ou armazená-los em tabelas específicas.

GERA_FUNDO_ICMS_NORMAL
GRUPO_IMPOSTO: FUNDO_ICMS_NORMAL
COD_OPER_APUR: 007, 012
Filtragem:
DSC_ITEM_APURACAO LIKE %REF. FUNDO DE COMBATE A POBREZA%
DSC_ITEM_APURACAO LIKE %INCENTIVO FISCAL%
DSC_ITEM_APURACAO LIKE %INCENTIVO PRO GOIAS%
DSC_ITEM_APURACAO) LIKE %BENEFICIO INCENTIVO DESENVOLVE 90% - CONF. RESOLUCAO 72/2010%
DSC_ITEM_APURACAO LIKE %FECEP 2% INCENTIVO B01%
DSC_ITEM_APURACAO) LIKE %FECEP 2% INCENTIVO B02%

## 7.1 Função Interna json


Formata strings como campos JSON.
Parâmetros:
nome_campo: Nome do campo JSON.
valor: Valor do campo.
último: Indica se é o último campo (para evitar vírgulas).

## 7.2 Declaração de Variáveis e Cursores


Cursor geraJSON1: Consulta várias tabelas fiscais e retorna informações como:
Grupo de imposto, códigos de arrecadação e receita.
Período, código do estabelecimento.
Valores de apuração, vencimento e pagamento.
Regras tributárias e empresariais.









## 7.3 Processamento Principal


Itera sobre o cursor geraJSON1.
Valida e estrutura os dados para JSON ou tabela.
Insere registros processados em tabelas específicas.


## 7.4. Regras Específicas


Mapeamento de Parâmetros: Utiliza fpar_parametros e fpar_param_det.
Integração com Outras Procedures: Como calcula_data_vencimento.



## 8. Função calcula_data_vencimento


Calcula datas de vencimento baseadas em regras tributárias e empresariais.





## 8.1. Lógica de Cálculo


Dia Útil (DU)
Usa a tabela FLUX_VW_CALENDARIO_CPROC para identificar dias úteis.
Data fixa (DF)
Constrói uma data fixa com base nos parâmetros.
Feriados (DA ou FA)

Ajusta vencimentos considerando feriados municipais ou estaduais.


## 9. Fluxo Principal


A execução principal utiliza três SELECTs para recuperar informações fiscais:


## 9.1. Select 1


Tabelas: ITEM_APURAC_CALC, ZFLUX_VW_UF_CD_RC_GP_IMP_CPROC

Condições:
COD_TIPO_LIVRO = '108'
COD_OPER_APUR = '013'
VAL_APURACAO > 0
GRUPO_IMPOSTO = 'ICMS_NORMAL'
REGRA_IMPOSTO = 'REGRA_ICMS_NORMAL_1'


## 9.2. Select 2


Acrescenta ITEM_APURAC_DISCR para regras adicionais.

## 9.3. Select 3

Inclui FLUX_HEINEKEN_ESTAB_TEMP_CPROC.























## 10. Campos Necessários para Requisição de Envio


Abaixo estão os campos obrigatórios e opcionais exigidos para a integração, com seus respectivos formatos e origens na base de dados da Tax One.

## 10.1 De/PARA integração DOOTAX – Campos para Requisição de Envio:





## 11. Melhorias e Diferenciais na Jornada do Usuário


Para otimizar a experiência dos usuários, recomendamos implementar os seguintes itens:

## 11.1. Controle de Versão

Registrar a versão da API e manter um histórico de atualizações.
Exemplo: Versão 1.0 - Lançamento inicial - Versão 1.1 - Inclusão do campo "cod_mun_favorecido"


## 11.2. Segurança na Integração


Utilizar tokens de autenticação para garantir acesso seguro.
Aplicar validação de dados para evitar ataques como SQL Injection.
Restringir acessos via IP autorizado ou credenciais personalizadas.





## 11.3. Detalhamento de Requisições e Respostas


Indicar os métodos HTTP utilizados (POST, GET, etc.).
Exemplificar as respostas da API para sucesso e erro.

## 11.4. Monitoramento e Suporte

Possibilitar acompanhamento dos envios através de logs e dashboards.


## 12. Conclusão


A integração da API do Tax One com o Dootax oferece um fluxo automatizado e eficiente para a importação e processamento de guias de pagamento de tributos. A padronização dos campos de requisição e a implementação de validações estruturadas garantem maior confiabilidade e segurança na transmissão dos dados, reduzindo erros operacionais.

A funcionalidade Executar desempenha um papel essencial ao permitir a automação do processamento das guias importadas, reduzindo a necessidade de intervenção manual e agilizando o cumprimento das obrigações fiscais.

Além disso, as melhorias sugeridas, como feedback em tempo real, logs detalhados e flexibilidade no envio de dados, aprimoram a experiência do usuário, tornando o sistema mais intuitivo e transparente.

Com essas otimizações, espera-se um ganho expressivo em produtividade, segurança e conformidade fiscal, proporcionando uma solução robusta e alinhada às necessidades das empresas.




= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS XXX | Paloma Dias Brondi | Novo Módulo Integração Guias de Pagamento DOOTAX - Função EXECUTAR e Procedures Relacionadas | 13.02.2025 |
|  |  |  |  |


| Parâmetro | Descrição |
| --- | --- |
| p_periodo | Representa um período de tempo para cálculos ou consultas. |
| p_grp_imp | Grupo de imposto utilizado na execução de regras fiscais. |
| p_uf_estab | Unidade federativa do estabelecimento. |
| p_cod_estab | Código do estabelecimento, do tipo Lib_Proc.Vartab. |


| Dependência | Finalidade |
| --- | --- |
| LIB_PROC | Criação de processos, logs e manipulação de parâmetros. |
| LIB_PARAMETROS | Recupera e salva parâmetros como códigos de empresas e usuários. |
| FPAR_PARAMETROS | Tabela de configurações usada em consultas SQL. |
| PRT_DIRETORIOS_SERVIDOR | Valida existência de diretórios. |
| FLUX_HEINEKEN_ESTAB_TEMP_CPROC | Armazena dados temporários de estabelecimentos. |


| Parâmetro | Descrição |
| --- | --- |
| pCod_Tp_Dt | Tipo de cálculo para a data (ex.: "DU" para dia útil, "DF" para data fixa). |
| pDia_Vc | Dia base para o cálculo. |
| pMesano | Período no formato mês/ano. |
| pIdent_estado | Identificador do estado. |
| pCod_Municipio | Código do município. |


| Campos DOOTAX | Dados do campo | Formato | Obrig. | DE/PARA TAX ONE |
| --- | --- | --- | --- | --- |
| cod_empresa | Código da empresa conforme informado no cadastro da empresa no Dootax | Alfanumérico | Sim | SAFX 07-Arquivo de Notas Fiscais  SAFX08 -Itens Notas Fiscais Mercadorias e Produtos  SAFX 09-Itens Notas Fiscais de Serviços  Tabelas de Apurações |
| cod_estab | Código do estabelecimento conforme informado no cadastro da empresa no Dootax | Alfanumérico |  | SAFX 07-Arquivo de Notas Fiscais  SAFX08 -Itens Notas Fiscais Mercadorias e Produtos  SAFX 09-Itens Notas Fiscais de Serviços  Tabelas de Apurações |
| periodo | Data da ocorrência ou do encerramento do período | Data | Sim | SAFX07 - Arquivo de Notas Fiscais  SAFX08 - Itens Notas Fiscais Mercadorias e Produtos  SAFX09 - Itens Notas Fiscais de Serviços  Tabelas de Apurações   SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração. |
| cod_arrecadacao | Tipo de documento utilizado na arrecadação, conforme cadastro no Dootax. (ex.: DARF; GNRE) | Número | Sim | SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração do ICMS |
| cod_receita | Código da receita que está sendo paga, de acordo com o tipo de documento de arrecadação. | Número | Sim | SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração do ICMS |
| det_receita | Código do detalhamento da receita. | Alfanumérico | Sim | SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração. |
| num_doc_origem | Número do documento que deu origem ao pagamento. | Número |  | SAFX 07-Arquivo de Notas Fiscais  SAFX08 -Itens Notas Fiscais Mercadorias e Produtos  SAFX 09-Itens Notas Fiscais de Serviços  Tabelas de Apurações |
| Serie | Série do documento | Alfanumérico |  | SAFX 07-Arquivo de Notas Fiscais  SAFX08 -Itens Notas Fiscais Mercadorias e Produtos  SAFX 09-Itens Notas Fiscais de Serviços |
| uf_favorecida | Sigla da UF favorecida. | Texto | Sim | SAFX 07-Arquivo de Notas Fiscais  SAFX08 -Itens Notas Fiscais Mercadorias e Produtos |
| cnpj_favorecido | CNPJ do favorecido. Esse campo é usado para identificar o favorecido, quando o recolhimento é feito pela empresa, em nome de terceiros. | Número |  | SAFX 07-Arquivo de Notas Fiscais  SAFX08 -Itens Notas Fiscais Mercadorias e Produtos  SAFX 09-Itens Notas Fiscais de Serviços |
| ie_favorecida | Inscrição Estadual do favorecido.  Esse campo é usado para identificar o favorecido, quando o recolhimento é feito pela empresa, em nome de terceiros. | Número |  | SAFX 07-Arquivo de Notas Fiscais  SAFX08 -Itens Notas Fiscais Mercadorias e Produtos |
| vlr_principal | Valor principal do título. | Número | Sim | SAFX07 - Arquivo de Notas Fiscais  SAFX08 - Itens Notas Fiscais Mercadorias e Produtos  SAFX09 - Itens Notas Fiscais de Serviços  Tabelas de Apurações   SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração. |
| data_vencimento | Data do Vencimento. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração. | Data | Sim | SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração. |
| data_pagamento | Data do Pagamento. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração. | Data |  | SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração. |
| vlr_multa | Valor da multa quando o pagamento ocorrer em atraso. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração. | Número |  | SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração. |
| vlr_juros | Valor dos juros quando o pagamento ocorrer em atraso. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração. | Número |  | SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração. |
| info_complementar | Informação complementar a ser incluída na emissão do título a pagar. | Alfanumérico |  | SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração |
| vlr_fecp | Valor do recolhimento ao Fundo Estadual de Combate à Pobreza. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr_principal com o valor da guia excluído o valor do recolhimento ao FECP. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr_principal. | Número |  | SAFX 08 - Itens Notas Fiscais Mercadorias e Produtos |
| vlr_fecp_multa | Valor da multa sobre o recolhimento ao Fundo Estadual de Combate à Pobreza, quando o pagamento ocorrer em atraso. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr_multa com o valor da multa excluído o valor da multa referente ao FECP. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr_multa. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração. | Número |  | SAFX 08 - Itens Notas Fiscais Mercadorias e Produtos |
| vlr_fecp_juros | Valor dos juros sobre o recolhimento ao Fundo Estadual de Combate à Pobreza, quando o pagamento ocorrer em atraso. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr_juros com o valor dos juros excluído o valor dos juros referente ao FECP. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr_juros. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração. | Número |  | SAFX 07-Arquivo de Notas Fiscais  SAFX08 -Itens Notas Fiscais Mercadorias e Produtos |
| convenio | Convênio ou protocolo ICMS que regulamenta a forma de recolhimento do tributo. Esse campo é utilizado na geração da GNRE por apuração. | Número |  | SAFX 07-Arquivo de Notas Fiscais  SAFX08 -Itens Notas Fiscais Mercadorias e Produtos |
| cod_produto | Na emissão da GNRE, algumas UFs exigem o preenchimento do código do produto no recolhimento do ICMS por apuração. Consulte a UF para obter a lista de códigos de produtos válidos. | Alfanumérico |  | SAFX 07-Arquivo de Notas Fiscais  SAFX08 -Itens Notas Fiscais Mercadorias e Produtos |
| chave_dfe | Chave de acesso do documento fiscal:  Para documentos fiscais eletrônicos, informar a chave com 44 dígitos. | Alfanumérico |  | SAFX 07-Arquivo de Notas Fiscais |
| cad_part | Informações do participante (destinatário, emitente, transportador, etc). Esse campo deve ser informado quando os dados do participante são exigidos na emissão ou visualização da guia.  Ver layout do campo na aba "Cadastros", tabela "cad_part". | Alfanumérico |  | SAFX04-Arquivo de Cadastro de Pessoas Físicas/Jurídicas  SAFX 07-Arquivo de Notas Fiscais  SAFX 08- Itens Notas Fiscais Mercadorias e Produtos  SAFX 09 -Itens Notas Fiscais de Serviços |
| cod_mun_favorecido | Código do municipio - Este campo deve ser informado quando a guia a ser emitida utilize o código de município diferente do que está no cadastro da empresa | Número |  | SAFX 07-Arquivo de Notas Fiscais  SAFX 09 -Itens Notas Fiscais de Serviços |
| vlr_outros | Valor de outras despesas que devam ser utilizadas na geração da guia | Número |  | SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração |
| vlr_base_calc | Valor de base de cálculo. Utilizado nas guias que utilizam deste valor para calcular o valor da guia | Número |  | SAFX 07- Arquivo de Notas Fiscais  SAFX 08 -Itens Notas Fiscais Mercadorias e Produtos  SAFX 09 - Itens Notas Fiscais de Serviços  Tabela de Apuração |
| campos_extras | Utilizado para enviar um json com campos adicionais | Alfanumérico |  | SAFX07 - Arquivo de Notas Fiscais  SAFX08 - Itens Notas Fiscais Mercadorias e Produtos  SAFX09 - Itens Notas Fiscais de Serviços  Tabelas de Apurações   SAFX 163 -Guia de Recolhimento de Tributos Estaduais – GNRE.  Tabela das Guias de Recolhimento da Apuração. |
| conta_contabil | Código da empresa conforme informado no cadastro da empresa no Dootax | Alfanumérico |  | SAFX 2002- Tabela do Plano de Contas |
