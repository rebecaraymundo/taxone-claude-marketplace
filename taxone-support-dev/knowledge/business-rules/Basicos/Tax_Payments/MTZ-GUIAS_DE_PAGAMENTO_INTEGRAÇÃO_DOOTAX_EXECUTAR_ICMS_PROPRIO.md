# MTZ-GUIAS DE PAGAMENTO_INTEGRAÇÃO_DOOTAX _EXECUTAR_ ICMS PROPRIO

- **Fonte:** MTZ-GUIAS DE PAGAMENTO_INTEGRAÇÃO_DOOTAX _EXECUTAR_ ICMS PROPRIO.docx
- **Modificado:** 2025-12-03
- **Tamanho:** 203 KB

---

THOMSON REUTERS

Novo Módulo Integração Guias de Pagamento DOOTAX

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS XXX

Paloma Dias Brondi/Millys

Novo Módulo Integração Guias de Pagamento DOOTAX \- __Função EXECUTAR e Procedures Relacionadas__

13\.02\.2025

##### DOCUMENTO DE REQUISITO

Sumário

[1\.	Objetivo	4](#_Toc190295261)

[2\.	Introdução da função Executar	5](#_Toc190295262)

[3\.	Contexto Inicial da Função EXECUTAR	5](#_Toc190295263)

[4\.	Detalhamento da Função EXECUTAR	6](#_Toc190295264)

[5\.	Inserção de dados em tabelas temporárias	6](#_Toc190295265)

[5\.1\. Dependências	6](#_Toc190295266)

[6\.	Procedure GERA\_ICMS\_NORMAL	7](#_Toc190295267)

[7\.1 Função Interna json	7](#_Toc190295268)

[7\.2 Declaração de Variáveis e Cursores	7](#_Toc190295269)

[7\.3 Processamento Principal	8](#_Toc190295270)

[7\.4\. Regras Específicas	8](#_Toc190295271)

[8\. Função calcula\_data\_vencimento	8](#_Toc190295272)

[8\.1\. Lógica de Cálculo	9](#_Toc190295273)

[9\. Fluxo Principal	9](#_Toc190295274)

[9\.1\. Select 1	9](#_Toc190295275)

[9\.2\. Select 2	10](#_Toc190295276)

[9\.3\. Select 3	10](#_Toc190295277)

[10\. Campos Necessários para Requisição de Envio	11](#_Toc190295278)

[10\.1 De/PARA integração DOOTAX – Campos para Requisição de Envio:	11](#_Toc190295279)

[11\. Melhorias e Diferenciais na Jornada do Usuário	16](#_Toc190295280)

[11\.1\. Controle de Versão	16](#_Toc190295281)

[11\.2\. Segurança na Integração	16](#_Toc190295282)

[11\.3\. Detalhamento de Requisições e Respostas	17](#_Toc190295283)

[11\.4\. Monitoramento e Suporte	17](#_Toc190295284)

[12\. Conclusão	17](#_Toc190295285)

# <a id="_Toc190295261"></a>Objetivo

O novo módulo de “Guia de Pagamento” foi desenvolvido com base na estrutura de um processo customizado já existente “DOOTAX”\. Essa estrutura será reaproveitada e integrada a outro menu dentro do Onesource Tax One e Onesource BR\.

O reaproveitamento visa otimizar a implementação, mantendo a lógica de negócio previamente validada e adaptando\-a às especificidades do menu onde será inserido\. Essa abordagem visa reduzir esforços de implementação, garantir a consistência operacional e facilitar a manutenção futura, assegurando que o novo módulo atenda às necessidades específicas de processamento de Guias de Pagamento\.

Deverá transformar a funcionalidade customizada em um módulo produtizável \(Produtização = Preparado para comercialização\), garantindo que não contenha dados ou referências específicas ao cliente original\.

Todas as tabelas, procedures, views e outros objetos do banco de dados relacionados à funcionalidade deverão ser renomeados para evitar conflitos e manter a independência do novo módulo\. Os dados existentes associados ao cliente original deverão ser descartados ou tratados para garantir que a nova função seja limpa e genérica\. É necessário garantir que nenhuma referência explícita aos dados ou padrões do cliente original permaneça na implementação\. Desta forma, é necessário ajustar todas as chamadas de procedures, tabelas e views para refletir os novos nomes, garantindo compatibilidade total com o novo módulo\.

# <a id="_Toc190295262"></a>Introdução da função Executar

A função __EXECUTAR__ tem como objetivo principal processar guias de pagamento de impostos, registrando processos e manipulando informações fiscais\. Esta documentação detalha sua estrutura, dependências e funcionamento\.

# <a id="_Toc190295263"></a>Contexto Inicial da Função EXECUTAR

A função recebe os seguintes parâmetros de entrada:

__Parâmetro__

__Descrição__

p\_periodo

Representa um período de tempo para cálculos ou consultas\.

p\_grp\_imp

Grupo de imposto utilizado na execução de regras fiscais\.

p\_uf\_estab

Unidade federativa do estabelecimento\.

p\_cod\_estab

Código do estabelecimento, do tipo Lib\_Proc\.Vartab\.

Dentro da função, é inicializado um identificador de processo \(mproc\_id\), e um novo processo é criado no sistema por meio da biblioteca interna __LIB\_PROC__\.

# <a id="_Toc190295264"></a>Detalhamento da Função EXECUTAR

A função __EXECUTAR__ realiza as seguintes operações:

1. __Criação de um processo__
2. __Adição de logs__
3. __Recuperação de parâmetros__
4. __Validação de módulo e diretório__
	- Recupera valores do módulo para uso no processamento\.
	- Valida se o módulo e o diretório existem, gerando logs de atenção quando não encontrados\.

# <a id="_Toc190295265"></a>Inserção de dados em tabelas temporárias 

- 
	- Insere dados de estabelecimentos na tabela temporária FLUX\_HEINEKEN\_ESTAB\_TEMP\_CPROC\.

# <a id="_Toc190295266"></a>5\.1\. Dependências

A função depende das seguintes bibliotecas e tabelas:

__Dependência__

__Finalidade__

LIB\_PROC

Criação de processos, logs e manipulação de parâmetros\.

LIB\_PARAMETROS

Recupera e salva parâmetros como códigos de empresas e usuários\.

FPAR\_PARAMETROS

Tabela de configurações usada em consultas SQL\.

PRT\_DIRETORIOS\_SERVIDOR

Valida existência de diretórios\.

FLUX\_HEINEKEN\_ESTAB\_TEMP\_CPROC

Armazena dados temporários de estabelecimentos\.

# <a id="_Toc190295267"></a>Procedure GERA\_ICMS\_NORMAL

A procedure __GERA\_ICMS\_NORMAL__ tem como objetivo processar dados fiscais e estruturá\-los no formato JSON ou armazená\-los em tabelas específicas\.

# <a id="_Toc190295268"></a>7\.1 Função Interna json

- Formata strings como campos JSON\.
- Parâmetros: 
	- nome\_campo: Nome do campo JSON\.
	- valor: Valor do campo\.
	- último: Indica se é o último campo \(para evitar vírgulas\)\.

# <a id="_Toc190295269"></a>7\.2 Declaração de Variáveis e Cursores

- __Cursor geraJSON1__: Consulta várias tabelas fiscais e retorna informações como: 
	- Grupo de imposto, códigos de arrecadação e receita\.
	- Período, código do estabelecimento\.
	- Valores de apuração, vencimento e pagamento\.
	- Regras tributárias e empresariais\.

# <a id="_Toc190295270"></a>7\.3 Processamento Principal

- AItera sobre o cursor geraJSON1\.
- Valida e estrutura os dados para JSON ou tabela\.
- Insere registros processados em tabelas específicas\.

# <a id="_Toc190295271"></a>7\.4\. Regras Específicas

- __Mapeamento de Parâmetros__: Utiliza fpar\_parametros e fpar\_param\_det\.
- __Integração com Outras Procedures__: Como calcula\_data\_vencimento\.

# <a id="_Toc190295272"></a>8\. Função calcula\_data\_vencimento

Calcula datas de vencimento baseadas em regras tributárias e empresariais\.

__Parâmetro__

__Descrição__

pCod\_Tp\_Dt

Tipo de cálculo para a data \(ex\.: "DU" para dia útil, "DF" para data fixa\)\.

pDia\_Vc

Dia base para o cálculo\.

pMesano

Período no formato mês/ano\.

pIdent\_estado

Identificador do estado\.

pCod\_Municipio

Código do município\.

# <a id="_Toc190295273"></a>8\.1\. Lógica de Cálculo

1. __Dia Útil \(DU\)__
	1. Usa a tabela FLUX\_VW\_CALENDARIO\_CPROC para identificar dias úteis\.
2. __Data fixa \(DF\)__
	1. Constrói uma data fixa com base nos parâmetros\.
3. __Feriados \(DA ou FA\)__
	- Ajusta vencimentos considerando feriados municipais ou estaduais\.

# <a id="_Toc190295274"></a>9\. Fluxo Principal

A execução principal utiliza três SELECTs para recuperar informações fiscais:

# <a id="_Toc190295275"></a>9\.1\. Select 1

- __Tabelas:__ ITEM\_APURAC\_CALC, ZFLUX\_VW\_UF\_CD\_RC\_GP\_IMP\_CPROC
- __Condições:__ 
	- COD\_TIPO\_LIVRO = '108'
	- COD\_OPER\_APUR = '013'
	- VAL\_APURACAO > 0
	- GRUPO\_IMPOSTO = 'ICMS\_NORMAL'
	- REGRA\_IMPOSTO = 'REGRA\_ICMS\_NORMAL\_1'

# <a id="_Toc190295276"></a>9\.2\. Select 2

- Acrescenta ITEM\_APURAC\_DISCR para regras adicionais\.

# <a id="_Toc190295277"></a>9\.3\. Select 3

- Inclui FLUX\_HEINEKEN\_ESTAB\_TEMP\_CPROC\.

# <a id="_Toc190295278"></a>10\. Campos Necessários para Requisição de Envio

Abaixo estão os campos obrigatórios e opcionais exigidos para a integração, com seus respectivos formatos e origens na base de dados da Tax One\.

 

# <a id="_Toc190295279"></a>10\.1 De/PARA integração DOOTAX – Campos para Requisição de Envio:  

__Campos DOOTAX__ 

__Dados do campo__ 

__Formato __ 

__Obrig\.__ 

__DE/PARA TAX ONE__ 

cod\_empresa 

 

Código da empresa conforme informado no cadastro da empresa no Dootax 

Alfanumérico 

 

Sim 

cod\_estab 

 

Código do estabelecimento conforme informado no cadastro da empresa no Dootax 

Alfanumérico 

 

periodo 

 

Data da ocorrência ou do encerramento do período 

Data 

 

 

Sim 

cod\_arrecadacao 

 

Tipo de documento utilizado na arrecadação, conforme cadastro no Dootax\. \(ex\.: DARF; GNRE\) 

Número 

Sim 

Regras incluir Lista para desenvolvimento

cod\_receita 

Código da receita que está sendo paga, de acordo com o tipo de documento de arrecadação\. 

Número 

Sim 

Incluir safx2080 

det\_receita 

 

Código do detalhamento da receita\. 

Alfanumérico 

Sim 

Millys Verificar

num\_doc\_origem 

Número do documento que deu origem ao pagamento\. 

Número 

 

- Regra por imposto  para preenchimento do NUM DOC ORIGEM

Serie 

Série do documento 

Alfanumérico 

 

Regra De número sequencial

uf\_favorecida 

 

Sigla da UF favorecida\. 

Texto 

Sim 

cnpj\_favorecido 

 

CNPJ do favorecido\. Esse campo é usado para identificar o favorecido, quando o recolhimento é feito pela empresa, em nome de terceiros\. 

Número 

 

- SAFX 07\-Arquivo de Notas Fiscais 
- SAFX08 \-Itens Notas Fiscais Mercadorias e Produtos 
- SAFX 09\-Itens Notas Fiscais de Serviços 

 

ie\_favorecida 

 

Inscrição Estadual do favorecido\.  Esse campo é usado para identificar o favorecido, quando o recolhimento é feito pela empresa, em nome de terceiros\. 

Número 

 

- SAFX 07\-Arquivo de Notas Fiscais 
- SAFX08 \-Itens Notas Fiscais Mercadorias e Produtos 

 

vlr\_principal 

Valor principal do título\. 

Número 

Sim 

- SAFX07 \- Arquivo de Notas Fiscais 
- SAFX08 \- Itens Notas Fiscais Mercadorias e Produtos 
- SAFX09 \- Itens Notas Fiscais de Serviços 
- Tabelas de Apurações  
- SAFX 163 \-Guia de Recolhimento de Tributos Estaduais – GNRE\. 
- Tabela das Guias de Recolhimento da Apuração\. 

data\_vencimento 

Data do Vencimento\. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração\. 

Data 

Sim 

- SAFX 163 \-Guia de Recolhimento de Tributos Estaduais – GNRE\. 
- Tabela das Guias de Recolhimento da Apuração\. 

data\_pagamento 

Data do Pagamento\. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração\. 

Data 

 

ICMS Próprio REGRA data

vlr\_multa 

Valor da multa quando o pagamento ocorrer em atraso\. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração\. 

Número 

 

- SAFX 163 \-Guia de Recolhimento de Tributos Estaduais – GNRE\. 
- Tabela das Guias de Recolhimento da Apuração\. 

vlr\_juros 

Valor dos juros quando o pagamento ocorrer em atraso\. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração\. 

Número 

 

- SAFX 163 \-Guia de Recolhimento de Tributos Estaduais – GNRE\. 
- Tabela das Guias de Recolhimento da Apuração\. 

info\_complementar 

Informação complementar a ser incluída na emissão do título a pagar\. 

Alfanumérico 

 

- SAFX 163 \-Guia de Recolhimento de Tributos Estaduais – GNRE\. 
- Tabela das Guias de Recolhimento da Apuração 

vlr\_fecp 

Valor do recolhimento ao Fundo Estadual de Combate à Pobreza\. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr\_principal com o valor da guia excluído o valor do recolhimento ao FECP\. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr\_principal\. 

Número 

 

- SAFX 08 \- Itens Notas Fiscais Mercadorias e Produtos 

 

vlr\_fecp\_multa 

Valor da multa sobre o recolhimento ao Fundo Estadual de Combate à Pobreza, quando o pagamento ocorrer em atraso\. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr\_multa com o valor da multa excluído o valor da multa referente ao FECP\. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr\_multa\. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração\. 

Número 

 

- SAFX 08 \- Itens Notas Fiscais Mercadorias e Produtos 

 

vlr\_fecp\_juros 

Valor dos juros sobre o recolhimento ao Fundo Estadual de Combate à Pobreza, quando o pagamento ocorrer em atraso\. Esse campo deve ser preenchido na hipótese de o ICMS normal e o valor referente ao FECP serem recolhidos utilizando a mesma guia, quando isso acontecer, preencha o vlr\_juros com o valor dos juros excluído o valor dos juros referente ao FECP\. Para estados onde o recolhimento do valor referente ao FECP é feito em uma guia própria, preencha somente o campo vlr\_juros\. Esse campo será calculado automaticamente pelo sistema caso não seja informado na integração\. 

Número 

 

- SAFX 07\-Arquivo de Notas Fiscais 
- SAFX08 \-Itens Notas Fiscais Mercadorias e Produtos 

 

convenio 

Convênio ou protocolo ICMS que regulamenta a forma de recolhimento do tributo\. Esse campo é utilizado na geração da GNRE por apuração\. 

Número 

 

- SAFX 07\-Arquivo de Notas Fiscais 
- SAFX08 \-Itens Notas Fiscais Mercadorias e Produtos 

 

cod\_produto 

Na emissão da GNRE, algumas UFs exigem o preenchimento do código do produto no recolhimento do ICMS por apuração\. Consulte a UF para obter a lista de códigos de produtos válidos\. 

Alfanumérico 

 

- SAFX 07\-Arquivo de Notas Fiscais 
- SAFX08 \-Itens Notas Fiscais Mercadorias e Produtos 

 

chave\_dfe 

Chave de acesso do documento fiscal:   
Para documentos fiscais eletrônicos, informar a chave com 44 dígitos\. 

Alfanumérico 

 

- SAFX 07\-Arquivo de Notas Fiscais 

 

cad\_part 

Informações do participante \(destinatário, emitente, transportador, etc\)\. Esse campo deve ser informado quando os dados do participante são exigidos na emissão ou visualização da guia\.   
Ver layout do campo na aba "Cadastros", tabela "cad\_part"\. 

Alfanumérico 

 

- SAFX04\-Arquivo de Cadastro de Pessoas Físicas/Jurídicas 
- SAFX 07\-Arquivo de Notas Fiscais 
- SAFX 08\- Itens Notas Fiscais Mercadorias e Produtos 
- SAFX 09 \-Itens Notas Fiscais de Serviços 

cod\_mun\_favorecido 

Código do municipio \- Este campo deve ser informado quando a guia a ser emitida utilize o código de município diferente do que está no cadastro da empresa 

Número 

 

- SAFX 07\-Arquivo de Notas Fiscais 
- SAFX 09 \-Itens Notas Fiscais de Serviços  

vlr\_outros 

Valor de outras despesas que devam ser utilizadas na geração da guia 

Número 

 

- SAFX 163 \-Guia de Recolhimento de Tributos Estaduais – GNRE\. 
- Tabela das Guias de Recolhimento da Apuração 

vlr\_base\_calc 

Valor de base de cálculo\. Utilizado nas guias que utilizam deste valor para calcular o valor da guia 

Número 

 

- SAFX 07\- Arquivo de Notas Fiscais 
- SAFX 08 \-Itens Notas Fiscais Mercadorias e Produtos 
- SAFX 09 \- Itens Notas Fiscais de Serviços 
- Tabela de Apuração 

campos\_extras 

Utilizado para enviar um json com campos adicionais 

Alfanumérico 

 

- SAFX07 \- Arquivo de Notas Fiscais 
- SAFX08 \- Itens Notas Fiscais Mercadorias e Produtos 
- SAFX09 \- Itens Notas Fiscais de Serviços 
- Tabelas de Apurações  
- SAFX 163 \-Guia de Recolhimento de Tributos Estaduais – GNRE\. 
- Tabela das Guias de Recolhimento da Apuração\. 

conta\_contabil 

Código da empresa conforme informado no cadastro da empresa no Dootax 

Alfanumérico 

 

- SAFX 2002\- Tabela do Plano de Contas 

 

 

# <a id="_Toc190295280"></a>11\. Melhorias e Diferenciais na Jornada do Usuário

Para otimizar a experiência dos usuários, recomendamos implementar os seguintes itens:

# <a id="_Toc190295281"></a>11\.1\. Controle de Versão

- Registrar a versão da API e manter um histórico de atualizações\.
- Exemplo: Versão 1\.0 \- Lançamento inicial \- Versão 1\.1 \- Inclusão do campo "cod\_mun\_favorecido"

# <a id="_Toc190295282"></a>11\.2\. Segurança na Integração

- Utilizar __tokens de autenticação__ para garantir acesso seguro\.
- Aplicar __validação de dados__ para evitar ataques como SQL Injection\.
- Restringir acessos via __IP autorizado__ ou credenciais personalizadas\.

# <a id="_Toc190295283"></a>11\.3\. Detalhamento de Requisições e Respostas

- Indicar os métodos HTTP utilizados \(POST, GET, etc\.\)\.
- Exemplificar as respostas da API para sucesso e erro\.

# <a id="_Toc190295284"></a>11\.4\. Monitoramento e Suporte

- Possibilitar acompanhamento dos envios através de logs e dashboards\.

# <a id="_Toc190295285"></a>12\. Conclusão

A integração da API do Tax One com o Dootax oferece um fluxo automatizado e eficiente para a importação e processamento de guias de pagamento de tributos\. A padronização dos campos de requisição e a implementação de validações estruturadas garantem maior confiabilidade e segurança na transmissão dos dados, reduzindo erros operacionais\.

A funcionalidade __Executar__ desempenha um papel essencial ao permitir a automação do processamento das guias importadas, reduzindo a necessidade de intervenção manual e agilizando o cumprimento das obrigações fiscais\. 

Além disso, as melhorias sugeridas, como feedback em tempo real, logs detalhados e flexibilidade no envio de dados, aprimoram a experiência do usuário, tornando o sistema mais intuitivo e transparente\.

Com essas otimizações, espera\-se um ganho expressivo em produtividade, segurança e conformidade fiscal, proporcionando uma solução robusta e alinhada às necessidades das empresas\.

= = = = = =

