# MTZ-GUIAS DE PAGAMENTO_INTEGRAÇÃO_DOOTAX _EXECUTAR_ ICMS ANTECIPADO

- **Fonte:** MTZ-GUIAS DE PAGAMENTO_INTEGRAÇÃO_DOOTAX _EXECUTAR_ ICMS ANTECIPADO.docx
- **Modificado:** 2025-12-03
- **Tamanho:** 181 KB

---

THOMSON REUTERS

Novo Módulo Integração Guias de Pagamento DOOTAX

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS XXX

Paloma Dias Brondi

Novo Módulo Integração Guias de Pagamento DOOTAX \- __Função EXECUTAR e Procedures Relacionadas__

13\.02\.2025

##### DOCUMENTO DE REQUISITO

Sumário

[1\.	Objetivo	4](#_Toc190696627)

[2\.	Introdução da função Executar	5](#_Toc190696628)

[3\.	Contexto Inicial da Função EXECUTAR	5](#_Toc190696629)

[4\.	Detalhamento da Função EXECUTAR	6](#_Toc190696630)

[5\.	Inserção de dados em tabelas temporárias	6](#_Toc190696631)

[5\.1\. Dependências	6](#_Toc190696632)

[6\.	Procedure GERA\_ICMS\_NORMAL	7](#_Toc190696633)

[7\.1 Função Interna json	7](#_Toc190696634)

[7\.2 Declaração de Variáveis e Cursores	7](#_Toc190696635)

[7\.3 Processamento Principal	8](#_Toc190696636)

[7\.4\. Regras Específicas	8](#_Toc190696637)

[8\. Função calcula\_data\_vencimento	8](#_Toc190696638)

[8\.1\. Lógica de Cálculo	9](#_Toc190696639)

[9\. Fluxo Principal	9](#_Toc190696640)

[9\.1\. Select 1	9](#_Toc190696641)

[9\.2\. Select 2	10](#_Toc190696642)

[9\.3\. Select 3	10](#_Toc190696643)

[10\. Campos Necessários para Requisição de Envio	11](#_Toc190696644)

[10\.1 De/PARA integração DOOTAX – Campos para Requisição de Envio:	11](#_Toc190696645)

[11\. Melhorias e Diferenciais na Jornada do Usuário	16](#_Toc190696646)

[11\.1\. Controle de Versão	16](#_Toc190696647)

[11\.2\. Segurança na Integração	16](#_Toc190696648)

[11\.3\. Detalhamento de Requisições e Respostas	17](#_Toc190696649)

[11\.4\. Monitoramento e Suporte	17](#_Toc190696650)

[12\. Conclusão	17](#_Toc190696651)

# <a id="_Toc190696627"></a>Objetivo

O novo módulo de “Guia de Pagamento” foi desenvolvido com base na estrutura de um processo customizado já existente “DOOTAX”\. Essa estrutura será reaproveitada e integrada a outro menu dentro do Onesource Tax One e Onesource BR\.

O reaproveitamento visa otimizar a implementação, mantendo a lógica de negócio previamente validada e adaptando\-a às especificidades do menu onde será inserido\. Essa abordagem visa reduzir esforços de implementação, garantir a consistência operacional e facilitar a manutenção futura, assegurando que o novo módulo atenda às necessidades específicas de processamento de Guias de Pagamento\.

Deverá transformar a funcionalidade customizada em um módulo produtizável \(Produtização = Preparado para comercialização\), garantindo que não contenha dados ou referências específicas ao cliente original\.

Todas as tabelas, procedures, views e outros objetos do banco de dados relacionados à funcionalidade deverão ser renomeados para evitar conflitos e manter a independência do novo módulo\. Os dados existentes associados ao cliente original deverão ser descartados ou tratados para garantir que a nova função seja limpa e genérica\. É necessário garantir que nenhuma referência explícita aos dados ou padrões do cliente original permaneça na implementação\. Desta forma, é necessário ajustar todas as chamadas de procedures, tabelas e views para refletir os novos nomes, garantindo compatibilidade total com o novo módulo\.

# <a id="_Toc190696628"></a>Introdução da função Executar

A função __EXECUTAR__ tem como objetivo principal processar guias de pagamento de impostos, registrando processos e manipulando informações fiscais\. Esta documentação detalha sua estrutura, dependências e funcionamento\.

# <a id="_Toc190696629"></a>Contexto Inicial da Função EXECUTAR

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

# <a id="_Toc190696630"></a>Detalhamento da Função EXECUTAR

A função __EXECUTAR__ realiza as seguintes operações:

1. __Criação de um processo__
2. __Adição de logs__
3. __Recuperação de parâmetros__
4. __Validação de módulo e diretório__
	- Recupera valores do módulo para uso no processamento\.
	- Valida se o módulo e o diretório existem, gerando logs de atenção quando não encontrados\.

# <a id="_Toc190696631"></a>Inserção de dados em tabelas temporárias 

- 
	- Insere dados de estabelecimentos na tabela temporária FLUX\_HEINEKEN\_ESTAB\_TEMP\_CPROC\.

# <a id="_Toc190696632"></a>5\.1\. Dependências

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

# <a id="_Toc190696633"></a>Procedure GERA\_ICMS\_ANTECIPADO

A procedure GERA\_ICMS\_ANTECIPADO tem como objetivo processar dados fiscais e estruturá\-los no formato JSON ou armazená\-los em tabelas específicas\.

GERA\_ICMS\_ANTECIPADO

GRUPO\_IMPOSTO: ICMS\_ANTECIPADO

COD\_OPER\_APUR: 006

Filtragem: DSC\_ITEM\_APURACAO = Antecipação compra para comercialização

# <a id="_Toc190696634"></a>7\.1 Função Interna json

- Formata strings como campos JSON\.
- Parâmetros: 
	- nome\_campo: Nome do campo JSON\.
	- valor: Valor do campo\.
	- último: Indica se é o último campo \(para evitar vírgulas\)\.

# <a id="_Toc190696635"></a>7\.2 Declaração de Variáveis e Cursores

- __Cursor geraJSON1__: Consulta várias tabelas fiscais e retorna informações como: 
	- Grupo de imposto, códigos de arrecadação e receita\.
	- Período, código do estabelecimento\.
	- Valores de apuração, vencimento e pagamento\.
	- Regras tributárias e empresariais\.

# <a id="_Toc190696636"></a>7\.3 Processamento Principal

- Itera sobre o cursor geraJSON1\.
- Valida e estrutura os dados para JSON ou tabela\.
- Insere registros processados em tabelas específicas\.

# <a id="_Toc190696637"></a>7\.4\. Regras Específicas

- __Mapeamento de Parâmetros__: Utiliza fpar\_parametros e fpar\_param\_det\.
- __Integração com Outras Procedures__: Como calcula\_data\_vencimento\.

# <a id="_Toc190696638"></a>8\. Função calcula\_data\_vencimento

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

# <a id="_Toc190696639"></a>8\.1\. Lógica de Cálculo

1. __Dia Útil \(DU\)__
	1. Usa a tabela FLUX\_VW\_CALENDARIO\_CPROC para identificar dias úteis\.
2. __Data fixa \(DF\)__
	1. Constrói uma data fixa com base nos parâmetros\.
3. __Feriados \(DA ou FA\)__
	- Ajusta vencimentos considerando feriados municipais ou estaduais\.

# <a id="_Toc190696640"></a>9\. Fluxo Principal

PROCEDURE GERA\_ICMS\_ANTECIPADO\(v\_mcod\_id         number,

                                    v\_cod\_empresa     varchar2,

                                    v\_cod\_estab       varchar2,

                                    v\_periodo         date,

                                    v\_grupo\_imposto   varchar2,

                                    v\_uf              varchar2,

                                    v\_tipo\_saida      varchar2\) IS

   FUNCTION json\(nome\_campo varchar2, valor varchar2, ultimo boolean default false\) return varchar2 IS

    v\_retorno varchar2\(200\) := '';

    BEGIN

      IF ultimo THEN

        v\_retorno := '"'||nome\_campo||'":"'||valor||'"';

      ELSE

        v\_retorno := '"'||nome\_campo||'":"'||valor||'",';

      END IF;

    return v\_retorno;

  END json;

   BEGIN

   DECLARE

        vPalet\_Count NUMBER := 0;

        vCount NUMBER := 0;

        v\_arq NUMBER :=0;

        v\_grp VARCHAR2\(30\) := '';

   cursor geraJSON3 is

   SELECT GRUPO\_IMPOSTO,

       DECODE\(\(SELECT TRIM\(VALOR\)

                from fpar\_parametros f,  fpar\_param\_det d

               where nome\_framework  = 'GP\_DE\_MSAF\_PARA\_SAP\_CPAR'

                 AND f\.id\_parametros = d\.id\_parametro

                 AND NOME\_PARAM      = 'DEPARA\_EMPR'

                 AND TRIM\(CONTEUDO\)  = COD\_EMPRESA\),NULL,COD\_EMPRESA,\(SELECT TRIM\(VALOR\)

                                                                        from fpar\_parametros f,  fpar\_param\_det d

                                                                       where nome\_framework  = 'GP\_DE\_MSAF\_PARA\_SAP\_CPAR'

                                                                         AND f\.id\_parametros = d\.id\_parametro

                                                                         AND NOME\_PARAM      = 'DEPARA\_EMPR'

                                                                         AND TRIM\(CONTEUDO\)  = COD\_EMPRESA\)\)   COD\_EMPRESA,

       GRUPO\_FISCAL,

       DECODE\(\(SELECT TRIM\(VALOR\)

                 from fpar\_parametros f,  fpar\_param\_det d

                where nome\_framework    = 'GP\_DE\_MSAF\_PARA\_SAP\_CPAR'

                  AND f\.id\_parametros   = d\.id\_parametro

                  AND NOME\_PARAM        = 'DEPARA\_ESTAB'

                  AND TRIM\(CONTEUDO\)    = COD\_ESTAB

                  AND TRIM\(D\.DESCRICAO\) = COD\_EMPRESA\),NULL,COD\_ESTAB, \(SELECT TRIM\(VALOR\)

                                                                        from fpar\_parametros f,  fpar\_param\_det d

                                                                       where nome\_framework    = 'GP\_DE\_MSAF\_PARA\_SAP\_CPAR'

                                                                         AND f\.id\_parametros   = d\.id\_parametro

                                                                         AND NOME\_PARAM        = 'DEPARA\_ESTAB'

                                                                         AND TRIM\(CONTEUDO\)    = COD\_ESTAB

                                                                         AND TRIM\(D\.DESCRICAO\) = COD\_EMPRESA\)\) COD\_ESTAB,

       PERIODO,

       COD\_ARRECADACAO,

       COD\_RECEITA,

       NUM\_DOC\_ORIGEM,

       SERIE,

       CHAVE\_NFE,

       UF\_FAVORECIDA,

       v\_tipo\_saida P\_TIPO\_SAIDA,

       CONVENIO,

       DETALHAMENTO\_RECEITA,

       PRODUTO,

       INF\_COMPLEMENTAR,

       VALOR\_PRINCIPAL,

       DATA\_VENCIMENTO,

       DATA\_PAGAMENTO,

       REGRA\_IMPOSTO,

       VALOR\_FECP,

       NULL CNPJ\_FAVORECIDO,

       NULL IE\_FAVORECIDO,

       0 VLR\_MULTA,

       0 VLR\_JUROS,

       0 VLR\_FECP\_MULTA,

       0 VLR\_FECP\_JUROS,

       NULL DATA\_EMISSAO

  FROM \(

SELECT GRUPO\_IMPOSTO,

        COD\_EMPRESA,

        GRUPO\_FISCAL,

        COD\_ESTAB,

        PERIODO,

        COD\_ARRECADACAO,

        COD\_RECEITA,

        NUM\_DOC\_ORIGEM,

        SERIE,

        CHAVE\_NFE,

        DATA\_EMISSAO,

        SUM\(VALOR\_PRINCIPAL\) VALOR\_PRINCIPAL,

        MAX\(DATA\_VENCIMENTO\) DATA\_VENCIMENTO,

        DATA\_PAGAMENTO,

        CONVENIO,

        DETALHAMENTO\_RECEITA,

        PRODUTO,

        INF\_COMPLEMENTAR,

        VALOR\_FECP,

        REGRA\_IMPOSTO,

        UF\_FAVORECIDA

  FROM \(

SELECT

       'ICMS\_ANTECIPADO'                                         GRUPO\_IMPOSTO,

       APU\.COD\_EMPRESA                                           COD\_EMPRESA,

       REPLACE\(FLX\.GRUPO\_FISCAL,'',''\)                           GRUPO\_FISCAL,

       APU\.COD\_ESTAB                                             COD\_ESTAB,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)                     PERIODO,

       FLX\.COD\_ARRECADACAO                                       COD\_ARRECADACAO,

       FLX\.COD\_RECEITA                                           COD\_RECEITA,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)||FLX\.COD\_RECEITA||1 NUM\_DOC\_ORIGEM,

       NULL                                                      SERIE,

       NULL                                                      CHAVE\_NFE,

       NULL                                                      DATA\_EMISSAO,

       STD\.COD\_ESTADO                                            UF\_FAVORECIDA,

       apu\.val\_item\_discrim                                      VALOR\_PRINCIPAL,

       TO\_CHAR\(GP\_DT\_GERA\_GUIAS\_CPROC\.calcula\_data\_vencimento\(FLX\.REGRA\_VENCTO,FLX\.DIA\_VENCTO,\(TO\_CHAR\(\(APU\.DAT\_APURACAO \+1\),'MMYYYY'\)\),EST\.IDENT\_ESTADO,EST\.COD\_MUNICIPIO\),'YYYYMMDD'\) DATA\_VENCIMENTO,

       NULL                                                      DATA\_PAGAMENTO,

       FLX\.CONVENIO                                              CONVENIO,

       FLX\.DETALHE\_RECEITA                                       DETALHAMENTO\_RECEITA,

       FLX\.PRODUTO                                               PRODUTO,

       FLX\.INF\_COMPLEMENTAR                                      INF\_COMPLEMENTAR,

       null                                                      VALOR\_FECP,

       'REGRA\_ICMS\_ANTECIPADO\_1'                                 REGRA\_IMPOSTO

  FROM ITEM\_APURAC\_DISCR APU, ZGP\_VW\_UF\_CD\_RC\_GP\_IMP\_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD

 WHERE APU\.COD\_TIPO\_LIVRO = '108'

   AND APU\.COD\_OPER\_APUR  = '006'

   \-\-AND UPPER\(APU\.DSC\_ITEM\_APURACAO\) LIKE UPPER\('Antecipa  o compra para comercializa  o%'\)

   AND UPPER\(APU\.DSC\_ITEM\_APURACAO\) = UPPER\('Antecipa  o compra para comercializa  o'\)

   AND apu\.val\_item\_discrim    > 0

   AND APU\.COD\_EMPRESA    = FLX\.cod\_empresa

   AND APU\.COD\_ESTAB      = FLX\.cod\_estab

   AND UPPER\(FLX\.GRUPO\_IMPOSTO\)  = UPPER\('ICMS\_ANTECIPADO'\)

   AND APU\.COD\_EMPRESA    = EST\.COD\_EMPRESA

   AND APU\.COD\_ESTAB      = EST\.COD\_ESTAB

   AND EST\.IDENT\_ESTADO   = STD\.IDENT\_ESTADO

   AND STD\.COD\_ESTADO     = FLX\.UF

   AND FLX\.REGRA\_IMPOSTO  = 'REGRA\_ICMS\_ANTECIPADO\_1'\)

   GROUP BY GRUPO\_IMPOSTO,

        COD\_EMPRESA,

        GRUPO\_FISCAL,

        COD\_ESTAB,

        PERIODO,

        UF\_FAVORECIDA,

        COD\_ARRECADACAO,

        COD\_RECEITA,

        NUM\_DOC\_ORIGEM,

        SERIE,

        CHAVE\_NFE,

        DATA\_EMISSAO,

        DATA\_PAGAMENTO,

        CONVENIO,

        DETALHAMENTO\_RECEITA,

        PRODUTO,

        INF\_COMPLEMENTAR,

        VALOR\_FECP,

        REGRA\_IMPOSTO\) J, GP\_ESTAB\_TEMP\_CPROC TM

 where TM\.EMPRESA                             = J\.COD\_EMPRESA

   and TM\.ESTAB                               = J\.COD\_ESTAB

   and J\.COD\_EMPRESA                          = MCOD\_EMPRESA

   and to\_char\(last\_day\(tm\.dT\_PERIODO\), 'YYYYMMDD'\) = J\.PERIODO

   and upper\(TRIM\(TM\.GRP\_IMP\)\)                = upper\(J\.GRUPO\_IMPOSTO\)

   and J\.UF\_FAVORECIDA                LIKE DECODE\(tm\.uf\_estab, 'TD', '%', tm\.uf\_estab\)

   and J\.COD\_EMPRESA   = v\_cod\_empresa

   and tm\.saida        = v\_tipo\_saida

   and tm\.id\_proc      = v\_mcod\_id;

    REG geraJSON3%rowtype;

        v\_arquivo sys\.utl\_file\.file\_type;

        vs\_arquivo          varchar2\(32767\);

        mLinha              Varchar2\(2000\);

        v\_saida             varchar2\(1\);

    BEGIN

    loga\('GERA\_ICMS ANTECIPADO',FALSE\);

    FOR r\_pallet IN geraJSON3 LOOP

        vPalet\_Count := geraJSON3%ROWCOUNT;

        v\_saida      := r\_pallet\.p\_tipo\_saida;

    END LOOP;

    loga\('Qtde Registros:'||vPalet\_Count,FALSE\);

    IF vPalet\_Count = 0 then

         lib\_proc\.add\_log\('SEM DADOS PARA GERACAO DO ARQUIVO NO PERIODO E GRUPO SELECIONADO',1\);

         lib\_proc\.add\_log\('PERIODO: '||TO\_CHAR\(v\_periodo, 'MM/YYYY'\) ,1\);

         lib\_proc\.add\_log\('GRUPO DE IMPOSTO: '||v\_grupo\_imposto,1\);

     else

        FOR REG in geraJSON3 loop

        vCount := vCount\+1;

        If geraJSON3%ROWCOUNT = 1 Then

        if reg\.p\_tipo\_saida = 1 then

           v\_arquivo := SYS\.utl\_file\.fopen\(VS\_DIRETORIO,mproc\_id||'\_DOOTAX\_'|| REG\.GRUPO\_IMPOSTO||'\_'||to\_char\(trunc\(sysdate\), 'YYYYMMDD'\) ||'\.txt', 'W',32767\);

           SYS\.utl\_file\.put\_line\(v\_arquivo,\('\{"contas\_a\_pagar":\['\)||CHR\(10\)\);

           SYS\.utl\_file\.put\_line\(v\_arquivo, \('\{'\)||CHR\(10\)\);

           vs\_arquivo := '\{';

        elsif reg\.p\_tipo\_saida = 2 then

              LIB\_PROC\.ADD\_TIPO\(MPROC\_ID, 1, mproc\_id||'\_'|| REG\.GRUPO\_IMPOSTO||'\_'||to\_char\(trunc\(sysdate\), 'YYYYMMDD'\) ||'\.txt', 2\);

              vs\_arquivo := \('\{"contas\_a\_pagar":\['\);

              mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

              LIB\_PROC\.add\(mLinha, null, null, 1\);

              vs\_arquivo := \('\{'\);

              mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

              LIB\_PROC\.add\(mLinha, null, null, 1\);

        end if;

        lib\_proc\.add\_log\('  |Geracao arquivo JSON | NOME DO ARQUIVO: ''  |Geracao arquivo JSON | NOME DO ARQUIVO: '||mproc\_id||'\_'|| REG\.GRUPO\_IMPOSTO||'\_'||to\_char\(trunc\(sysdate\), 'YYYYMMDD'\) ||'\.txt   '||'DIRETORIO: '||VS\_DIRETORIO   ,1\);

        lib\_proc\.add\_log\('\{"contas\_a\_pagar":\[',1\);

        lib\_proc\.add\_log\('\{',1\);

        Else

            if reg\.p\_tipo\_saida = 1 then

               SYS\.utl\_file\.put\_line\(v\_arquivo, \('\{'\)||CHR\(10\)\);

               vs\_arquivo := \('\{'\);

            elsif reg\.p\_tipo\_saida = 2 then

                  vs\_arquivo := \('\{'\);

                  mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                  LIB\_PROC\.add\(mLinha, null, null, 1\);

            end if;

            lib\_proc\.add\_log\('\{',1\);

        End If;

        if reg\.p\_tipo\_saida = 1 then

        sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('cod\_empresa'    , reg\.cod\_empresa\)\)||CHR\(10\)\);

        sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('cod\_estab'      , reg\.cod\_estab\)\)||CHR\(10\)\);

        sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('periodo'        , reg\.periodo\)\)||CHR\(10\)\);

        sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('cod\_arrecadacao', reg\.cod\_arrecadacao\)\)||CHR\(10\)\);

        sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('cod\_receita'    , reg\.cod\_receita\)\)||CHR\(10\)\);

        sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('uf\_favorecida'  , reg\.uf\_favorecida\)\)||CHR\(10\)\);

        if reg\.num\_doc\_origem is not null then

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('num\_doc\_origem' , reg\.num\_doc\_origem\)\)||CHR\(10\)\);

        end if;

        IF REG\.SERIE IS NOT NULL THEN

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('serie' , reg\.serie\)\)||CHR\(10\)\);

        END IF;

        IF REG\.DETALHAMENTO\_RECEITA IS NOT NULL THEN

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('det\_receita' , reg\.detalhamento\_receita\)\)||CHR\(10\)\);

        END IF;

        IF REG\.PRODUTO IS NOT NULL THEN

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('cod\_produto' , reg\.produto\)\)||CHR\(10\)\);

        END IF;

        IF REG\.CONVENIO IS NOT NULL THEN

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('convenio' , reg\.convenio\)\)||CHR\(10\)\);

        END IF;

        IF REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' then

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('vlr\_principal' , replace\(trim\(to\_char\(reg\.valor\_principal,'999999990D99'\)\),',','\.'\),true\)\)||CHR\(10\)\);

        ELSE

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('vlr\_principal' , replace\(trim\(to\_char\(reg\.valor\_principal,'999999990D99'\)\),',','\.'\)\)\)||CHR\(10\)\);

        END IF;

        IF REG\.CHAVE\_NFE IS NOT NULL THEN

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('chave\_dfe' , reg\.chave\_nfe\)\)||CHR\(10\)\);

        END IF;

        \-\-\-\-\-

        CASE WHEN REG\.VALOR\_FECP IS NOT NULL AND REG\.VALOR\_FECP > 0 THEN

           CASE WHEN REG\.INF\_COMPLEMENTAR IS NOT NULL THEN

              CASE WHEN REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                 SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

              ELSE

                 sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_vencimento' , reg\.data\_vencimento\)\)||CHR\(10\)\);

              END CASE;

              CASE WHEN REG\.DATA\_PAGAMENTO IS NOT NULL THEN

                 sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_vencimento' , reg\.data\_vencimento\)\)||CHR\(10\)\);

              ELSE NULL;

              END CASE;

              sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('vlr\_fecp' , replace\(trim\(to\_char\(reg\.valor\_fecp,'999999990D99'\)\),',','\.'\),true\)\)||CHR\(10\)\);

           ELSE

              CASE WHEN REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                 SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)||CHR\(10\)\);

              ELSE

                 sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_vencimento' , reg\.data\_vencimento\)\)||CHR\(10\)\);

              END CASE;

              CASE WHEN REG\.DATA\_PAGAMENTO IS NOT NULL THEN

                 sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_pagamento' , reg\.data\_pagamento\)\)||CHR\(10\)\);

              ELSE NULL;

              END CASE;

             sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('vlr\_fecp' , replace\(trim\(to\_char\(reg\.valor\_fecp,'999999990D99'\)\),',','\.'\)\)\)||CHR\(10\)\);

             sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('inf\_complementar' , to\_char\(reg\.inf\_complementar\),true\)\)||CHR\(10\)\);

          END CASE;

       ELSE

           CASE WHEN REG\.INF\_COMPLEMENTAR IS NULL THEN

              CASE WHEN REG\.DATA\_PAGAMENTO IS NULL THEN

                 IF REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                    SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

                 ELSE

                    sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_vencimento' , to\_char\(reg\.data\_vencimento\),TRUE\)\)||CHR\(10\)\);

                 END IF;

              ELSE

                 CASE WHEN REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' then

                    SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

                 ELSE

                    sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_vencimento' , to\_char\(reg\.data\_vencimento\)\)\)||CHR\(10\)\);

                 END CASE;

                    sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_pagamento' , to\_char\(reg\.data\_pagamento\),TRUE\)\)||CHR\(10\)\);

              END CASE;

           ELSE

              CASE WHEN REG\.UF\_FAVORECIDA = 'AM'  AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                 SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

              ELSE

                    sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_vencimento' , to\_char\(reg\.data\_vencimento\)\)\)||CHR\(10\)\);

              END CASE;

              CASE WHEN REG\.DATA\_PAGAMENTO IS NOT NULL THEN

                        sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_vencimento' , to\_char\(reg\.data\_pagamento\)\)\)||CHR\(10\)\);

              ELSE NULL;

              END CASE;

                    sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('inf\_complementar' , to\_char\(reg\.inf\_complementar\),TRUE\)\)||CHR\(10\)\);

           END CASE;

       END CASE;

       \-\- SERVIDOR LOCAL

        elsif reg\.p\_tipo\_saida = 2 then

        vs\_arquivo := \(json\('cod\_empresa'    , reg\.cod\_empresa\)\);

        mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

        LIB\_PROC\.add\(mLinha, null, null, 1\);

        vs\_arquivo := \(json\('cod\_estab'      , reg\.cod\_estab\)\);

        mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

        LIB\_PROC\.add\(mLinha, null, null, 1\);

        IF REG\.REGRA\_IMPOSTO = 'REGRA\_DIFAL\_2' THEN

           vs\_arquivo := \(json\('periodo'        , reg\.data\_emissao\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        ELSE

           vs\_arquivo := \(json\('periodo'        , reg\.periodo\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        END IF;

        vs\_arquivo := \(json\('cod\_arrecadacao', reg\.cod\_arrecadacao\)\);

        mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

        LIB\_PROC\.add\(mLinha, null, null, 1\);

        vs\_arquivo := \(json\('cod\_receita'    , reg\.cod\_receita\)\);

        mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

        LIB\_PROC\.add\(mLinha, null, null, 1\);

        vs\_arquivo := \(json\('uf\_favorecida'  , reg\.uf\_favorecida\)\);

        mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

        LIB\_PROC\.add\(mLinha, null, null, 1\);

        if reg\.num\_doc\_origem is not null then

           vs\_arquivo := \(json\('num\_doc\_origem' , reg\.num\_doc\_origem\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        end if;

        IF REG\.SERIE IS NOT NULL THEN

           vs\_arquivo := \(json\('serie'  , reg\.serie\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        END IF;

        IF REG\.DETALHAMENTO\_RECEITA IS NOT NULL THEN

           vs\_arquivo := \(json\('det\_receita'  , reg\.detalhamento\_receita\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        END IF;

        IF REG\.PRODUTO IS NOT NULL THEN

           vs\_arquivo := \(json\('cod\_produto'  , reg\.produto\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        END IF;

        IF REG\.CONVENIO IS NOT NULL THEN

           vs\_arquivo := \(json\('convenio'  , reg\.convenio\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        END IF;

        IF REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' then

           vs\_arquivo := \(json\('vlr\_principal'  , replace\(trim\(to\_char\(reg\.valor\_principal,'999999990D99'\)\),',','\.'\),true\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        ELSE

           vs\_arquivo := \(json\('vlr\_principal'  , replace\(trim\(to\_char\(reg\.valor\_principal,'999999990D99'\)\),',','\.'\)\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        END IF;

        IF REG\.CHAVE\_NFE IS NOT NULL THEN

              vs\_arquivo := \(json\('chave\_dfe'  , reg\.chave\_nfe\)\);

              mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

              LIB\_PROC\.add\(mLinha, null, null, 1\);

        END IF;

        CASE WHEN REG\.VALOR\_FECP IS NOT NULL AND REG\.VALOR\_FECP > 0 THEN

           CASE WHEN REG\.INF\_COMPLEMENTAR IS NOT NULL THEN

              CASE WHEN REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                 SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

              ELSE

                 vs\_arquivo := \(json\('data\_vencimento'  , to\_char\(reg\.data\_vencimento\)\)\);

                 mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                 LIB\_PROC\.add\(mLinha, null, null, 1\);

              END CASE;

              CASE WHEN REG\.DATA\_PAGAMENTO IS NOT NULL THEN

                 vs\_arquivo := \(json\('data\_vencimento'  , to\_char\(reg\.data\_pagamento\)\)\);

                 mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                 LIB\_PROC\.add\(mLinha, null, null, 1\);

              ELSE NULL;

              END CASE;

              vs\_arquivo := \(json\('vlr\_fecp'  , replace\(trim\(to\_char\(reg\.valor\_fecp,'999999990D99'\)\),',','\.'\),true\)\);

              mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

              LIB\_PROC\.add\(mLinha, null, null, 1\);

           ELSE

              CASE WHEN REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                 SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

              ELSE

                 vs\_arquivo := \(json\('data\_vencimento'  , to\_char\(reg\.data\_vencimento\)\)\);

                 mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                 LIB\_PROC\.add\(mLinha, null, null, 1\);

              END CASE;

              CASE WHEN REG\.DATA\_PAGAMENTO IS NOT NULL THEN

                 vs\_arquivo := \(json\('data\_pagamento'  , to\_char\(reg\.data\_pagamento\)\)\);

                 mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                 LIB\_PROC\.add\(mLinha, null, null, 1\);

              ELSE NULL;

              END CASE;

             vs\_arquivo := \(json\('vlr\_fecp'  , replace\(trim\(to\_char\(reg\.valor\_fecp,'999999990D99'\)\),',','\.'\)\)\);

             mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

             LIB\_PROC\.add\(mLinha, null, null, 1\);

             vs\_arquivo := \(json\('inf\_complementar'  , to\_char\(reg\.inf\_complementar\),true\)\);

             mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

             LIB\_PROC\.add\(mLinha, null, null, 1\);

          END CASE;

       ELSE

           CASE WHEN REG\.INF\_COMPLEMENTAR IS NULL THEN

              CASE WHEN REG\.DATA\_PAGAMENTO IS NULL THEN

                 CASE WHEN REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                    SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

                 ELSE

                    vs\_arquivo := \(json\('data\_vencimento'  , to\_char\(reg\.data\_vencimento\),TRUE\)\);

                    mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                    LIB\_PROC\.add\(mLinha, null, null, 1\);

                 END CASE;

              ELSE

                 CASE WHEN REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' then

                    SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

                 ELSE

                    vs\_arquivo := \(json\('data\_vencimento'  , to\_char\(reg\.data\_vencimento\)\)\);

                    mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                    LIB\_PROC\.add\(mLinha, null, null, 1\);

                 END CASE;

                    vs\_arquivo := \(json\('data\_pagamento'  , to\_char\(reg\.data\_pagamento\),TRUE\)\);

                    mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                    LIB\_PROC\.add\(mLinha, null, null, 1\);

              END CASE;

           ELSE

              CASE WHEN REG\.UF\_FAVORECIDA = 'AM'  AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                 SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

              ELSE

                    vs\_arquivo := \(json\('data\_vencimento'  , to\_char\(reg\.data\_vencimento\)\)\);

                    mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                    LIB\_PROC\.add\(mLinha, null, null, 1\);

              END CASE;

              CASE WHEN REG\.DATA\_PAGAMENTO IS NOT NULL THEN

                    vs\_arquivo := \(json\('data\_vencimento'  , to\_char\(reg\.data\_pagamento\)\)\);

                    mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                    LIB\_PROC\.add\(mLinha, null, null, 1\);

              ELSE NULL;

              END CASE;

                    vs\_arquivo := \(json\('inf\_complementar'  , to\_char\(reg\.inf\_complementar\),TRUE\)\);

                    mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                    LIB\_PROC\.add\(mLinha, null, null, 1\);

            END CASE;

       END CASE;

        end if;

        lib\_proc\.add\_log\(json\('cod\_empresa'    , reg\.cod\_empresa\),1\);

        lib\_proc\.add\_log\(json\('cod\_estab'      , reg\.cod\_estab\),1\);

        lib\_proc\.add\_log\(json\('periodo'        , reg\.periodo\),1\);

        lib\_proc\.add\_log\(json\('cod\_arrecadacao', reg\.cod\_arrecadacao\),1\);

        lib\_proc\.add\_log\(json\('cod\_receita'    , reg\.cod\_receita\),1\);

        lib\_proc\.add\_log\(json\('uf\_favorecida'  , reg\.uf\_favorecida\),1\);

        if reg\.num\_doc\_origem is not null then

           lib\_proc\.add\_log\(json\('num\_doc\_origem' , reg\.num\_doc\_origem\),1\);

        end if;

        if reg\.serie is not null then

           lib\_proc\.add\_log\(json\('serie' , reg\.serie\),1\);

        end if;

        if reg\.data\_vencimento is not null then

           lib\_proc\.add\_log\(json\('data\_vencimento' , reg\.data\_vencimento\),1\);

        end if;

        if reg\.data\_pagamento is not null then

           lib\_proc\.add\_log\(json\('data\_pagamento' , reg\.data\_pagamento\),1\);

        end if;

        if reg\.convenio is not null then

           lib\_proc\.add\_log\(json\('convenio' , reg\.convenio\),1\);

        end if;

        if reg\.produto is not null then

           lib\_proc\.add\_log\(json\('produto' , reg\.produto\),1\);

        end if;

        if reg\.detalhamento\_receita is not null then

           lib\_proc\.add\_log\(json\('det\_receita' , reg\.detalhamento\_receita\),1\);

        end if;

        if reg\.inf\_complementar is not null then

           lib\_proc\.add\_log\(json\('inf\_complementar' , reg\.inf\_complementar\),1\);

        end if;

        if reg\.chave\_nfe is null then

           if reg\.valor\_fecp is not null then

           lib\_proc\.add\_log\(json\('vlr\_principal'  , reg\.valor\_principal\),1\);

           lib\_proc\.add\_log\(json\('valor\_fecp' , reg\.valor\_fecp,true\),1\);

           else

           lib\_proc\.add\_log\(json\('vlr\_principal'  , reg\.valor\_principal,true\),1\);

           end if;

        else

           if reg\.valor\_fecp is not null then

           lib\_proc\.add\_log\(json\('vlr\_principal'  , reg\.valor\_principal\),1\);

           lib\_proc\.add\_log\(json\('valor\_fecp' , reg\.valor\_fecp\),1\);

           else

           lib\_proc\.add\_log\(json\('vlr\_principal'  , reg\.valor\_principal,true\),1\);

           end if;

           lib\_proc\.add\_log\(json\('vlr\_principal'  , reg\.valor\_principal\),1\);

           lib\_proc\.add\_log\(json\('chave\_dfe' , reg\.chave\_nfe,true\),1\);

        end if;

           if reg\.p\_tipo\_saida = 1 then

              \-\-Se houver mais de 1 bloco no json insere virgula ao final do bloco, exceto no ultimo registro\.

              if vCount < vPalet\_Count then

                 sys\.utl\_file\.put\_line\(v\_arquivo, \('\},'\)\);

              else

                 sys\.utl\_file\.put\_line\(v\_arquivo, \('\}'\)\);

              end if;

           elsif reg\.p\_tipo\_saida = 2 then

                 \-\-Se houver mais de 1 bloco no json insere virgula ao final do bloco, exceto no ultimo registro\.

                 if vCount < vPalet\_Count then

                    vs\_arquivo := \('\},'\);

                    mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                    LIB\_PROC\.add\(mLinha, null, null, 1\);

                    lib\_proc\.add\_log\('\},',1\);

                 else

                     vs\_arquivo := \('\}'\);

                     mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                     LIB\_PROC\.add\(mLinha, null, null, 1\);

                     lib\_proc\.add\_log\('\}',1\);

                 end if;

            end if;

         insert into GP\_LOGS\_JSON\_DT\_CPROC  values \(mproc\_id,

                                                       musuario,

                                                       TO\_CHAR\(SYSDATE, 'DD/MM/YYYY HH24:MI:SS'\),

                                                       reg\.cod\_empresa,

                                                       reg\.cod\_estab,

                                                       reg\.periodo,

                                                       reg\.grupo\_imposto,

                                                       reg\.cod\_arrecadacao,

                                                       reg\.cod\_receita,

                                                       reg\.uf\_favorecida,

                                                       reg\.num\_doc\_origem,

                                                       reg\.serie,

                                                       reg\.chave\_nfe,

                                                       reg\.valor\_principal,

                                                       reg\.valor\_fecp,

                                                       reg\.data\_vencimento,

                                                       reg\.data\_pagamento,

                                                       reg\.inf\_complementar,

                                                       reg\.detalhamento\_receita,

                                                       reg\.convenio,

                                                       reg\.produto\);

        \-\-commit;

        end loop;

        if v\_saida = 1 then

           sys\.utl\_file\.put\_line\(v\_arquivo, \('\]\}'||CHR\(13\)\)\);

        elsif v\_saida = 2 then

              vs\_arquivo := \('\]\}'\);

              mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

              LIB\_PROC\.add\(mLinha, null, null, 1\);

        end if;

        lib\_proc\.add\_log\('\]\}',1\);

        sys\.utl\_file\.fclose\(v\_arquivo\);

           end if;

           delete from GP\_ESTAB\_TEMP\_CPROC where id\_proc = mproc\_id;

           COMMIT;

       END;

END GERA\_ICMS\_ANTECIPADO;

PROCEDURE GERA\_ICMS\_INCENTIVADO\(v\_mcod\_id         number,

                                    v\_cod\_empresa     varchar2,

                                    v\_cod\_estab       varchar2,

                                    v\_periodo         date,

                                    v\_grupo\_imposto   varchar2,

                                    v\_uf              varchar2,

                                    v\_tipo\_saida      varchar2\) IS

   FUNCTION json\(nome\_campo varchar2, valor varchar2, ultimo boolean default false\) return varchar2 IS

    v\_retorno varchar2\(200\) := '';

    BEGIN

      IF ultimo THEN

        v\_retorno := '"'||nome\_campo||'":"'||valor||'"';

      ELSE

        v\_retorno := '"'||nome\_campo||'":"'||valor||'",';

      END IF;

    return v\_retorno;

  END json;

   BEGIN

   DECLARE

        vPalet\_Count NUMBER := 0;

        vCount NUMBER := 0;

        v\_arq NUMBER :=0;

        v\_grp VARCHAR2\(30\) := '';

   cursor geraJSON4 is

   SELECT GRUPO\_IMPOSTO,

       DECODE\(\(SELECT TRIM\(VALOR\)

                from fpar\_parametros f,  fpar\_param\_det d

               where nome\_framework  = 'GP\_DE\_MSAF\_PARA\_SAP\_CPAR'

                 AND f\.id\_parametros = d\.id\_parametro

                 AND NOME\_PARAM      = 'DEPARA\_EMPR'

                 AND TRIM\(CONTEUDO\)  = COD\_EMPRESA\),NULL,COD\_EMPRESA,\(SELECT TRIM\(VALOR\)

                                                                        from fpar\_parametros f,  fpar\_param\_det d

                                                                       where nome\_framework  = 'GP\_DE\_MSAF\_PARA\_SAP\_CPAR'

                                                                         AND f\.id\_parametros = d\.id\_parametro

                                                                         AND NOME\_PARAM      = 'DEPARA\_EMPR'

                                                                         AND TRIM\(CONTEUDO\)  = COD\_EMPRESA\)\)   COD\_EMPRESA,

       GRUPO\_FISCAL,

       DECODE\(\(SELECT TRIM\(VALOR\)

                 from fpar\_parametros f,  fpar\_param\_det d

                where nome\_framework    = 'GP\_DE\_MSAF\_PARA\_SAP\_CPAR'

                  AND f\.id\_parametros   = d\.id\_parametro

                  AND NOME\_PARAM        = 'DEPARA\_ESTAB'

                  AND TRIM\(CONTEUDO\)    = COD\_ESTAB

                  AND TRIM\(D\.DESCRICAO\) = COD\_EMPRESA\),NULL,COD\_ESTAB, \(SELECT TRIM\(VALOR\)

                                                                        from fpar\_parametros f,  fpar\_param\_det d

                                                                       where nome\_framework    = 'GP\_DE\_MSAF\_PARA\_SAP\_CPAR'

                                                                         AND f\.id\_parametros   = d\.id\_parametro

                                                                         AND NOME\_PARAM        = 'DEPARA\_ESTAB'

                                                                         AND TRIM\(CONTEUDO\)    = COD\_ESTAB

                                                                         AND TRIM\(D\.DESCRICAO\) = COD\_EMPRESA\)\) COD\_ESTAB,

       PERIODO,

       COD\_ARRECADACAO,

       COD\_RECEITA,

       NUM\_DOC\_ORIGEM,

       SERIE,

       CHAVE\_NFE,

       UF\_FAVORECIDA,

       v\_tipo\_saida P\_TIPO\_SAIDA,

       CONVENIO,

       DETALHAMENTO\_RECEITA,

       PRODUTO,

       INF\_COMPLEMENTAR,

       VALOR\_PRINCIPAL,

       DATA\_VENCIMENTO,

       DATA\_PAGAMENTO,

       REGRA\_IMPOSTO,

       VALOR\_FECP,

       NULL CNPJ\_FAVORECIDO,

       NULL IE\_FAVORECIDO,

       0 VLR\_MULTA,

       0 VLR\_JUROS,

       0 VLR\_FECP\_MULTA,

       0 VLR\_FECP\_JUROS,

       NULL DATA\_EMISSAO

  FROM \(

        SELECT GRUPO\_IMPOSTO,

        COD\_EMPRESA,

        GRUPO\_FISCAL,

        COD\_ESTAB,

        PERIODO,

        COD\_ARRECADACAO,

        COD\_RECEITA,

        NUM\_DOC\_ORIGEM,

        SERIE,

        CHAVE\_NFE,

        DATA\_EMISSAO,

        UF\_FAVORECIDA,

        SUM\(VALOR\_PRINCIPAL\) VALOR\_PRINCIPAL,

        MAX\(DATA\_VENCIMENTO\) DATA\_VENCIMENTO,

        DATA\_PAGAMENTO,

        CONVENIO,

        DETALHAMENTO\_RECEITA,

        PRODUTO,

        INF\_COMPLEMENTAR,

        VALOR\_FECP,

        REGRA\_IMPOSTO

  FROM \(

SELECT

       'ICMS\_INCENTIVADO'                                        GRUPO\_IMPOSTO,

       APU\.COD\_EMPRESA                                           COD\_EMPRESA,

       REPLACE\(FLX\.GRUPO\_FISCAL,'',''\)                           GRUPO\_FISCAL,

       APU\.COD\_ESTAB                                             COD\_ESTAB,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)                     PERIODO,

       FLX\.COD\_ARRECADACAO                                       COD\_ARRECADACAO,

       FLX\.COD\_RECEITA                                           COD\_RECEITA,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)||FLX\.COD\_RECEITA||1 NUM\_DOC\_ORIGEM,

       NULL                                                      SERIE,

       NULL                                                      CHAVE\_NFE,

       NULL                                                      DATA\_EMISSAO,

       STD\.COD\_ESTADO                                            UF\_FAVORECIDA,

       ROUND\(\(apu\.val\_item\_discrim \* 0\.1\),2\)                     VALOR\_PRINCIPAL,

       TO\_CHAR\(GP\_DT\_GERA\_GUIAS\_CPROC\.calcula\_data\_vencimento\(FLX\.REGRA\_VENCTO,FLX\.DIA\_VENCTO,\(TO\_CHAR\(\(APU\.DAT\_APURACAO \+1\),'MMYYYY'\)\),EST\.IDENT\_ESTADO,EST\.COD\_MUNICIPIO\),'YYYYMMDD'\) DATA\_VENCIMENTO,

       NULL                                                      DATA\_PAGAMENTO,

       FLX\.CONVENIO                                              CONVENIO,

       FLX\.DETALHE\_RECEITA                                       DETALHAMENTO\_RECEITA,

       FLX\.PRODUTO                                               PRODUTO,

       FLX\.INF\_COMPLEMENTAR                                      INF\_COMPLEMENTAR,

       null                                                      VALOR\_FECP,

       'REGRA\_ICMS\_INCENTIVADO\_1'                                 REGRA\_IMPOSTO

  FROM ITEM\_APURAC\_DISCR APU, ZGP\_VW\_UF\_CD\_RC\_GP\_IMP\_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD

 WHERE APU\.COD\_TIPO\_LIVRO = '108'

   AND APU\.COD\_OPER\_APUR  = '012'

   AND apu\.val\_item\_discrim    > 0

   AND APU\.COD\_EMPRESA    = FLX\.cod\_empresa

   AND APU\.COD\_ESTAB      = FLX\.cod\_estab

   AND UPPER\(FLX\.GRUPO\_IMPOSTO\)  = UPPER\('ICMS\_INCENTIVADO'\)

   AND APU\.COD\_EMPRESA    = EST\.COD\_EMPRESA

   AND APU\.COD\_ESTAB      = EST\.COD\_ESTAB

   AND EST\.IDENT\_ESTADO   = STD\.IDENT\_ESTADO

   AND STD\.COD\_ESTADO     = FLX\.UF

   \-\-AND UPPER\(APU\.DSC\_ITEM\_APURACAO\) LIKE '%VLR\_ADIC\_INCENT%'

   AND UPPER\(APU\.DSC\_ITEM\_APURACAO\) LIKE 'VLR\_ADIC\_INCENT'

   AND FLX\.REGRA\_IMPOSTO  = 'REGRA\_ICMS\_INCENTIVADO\_1'\)

   GROUP BY GRUPO\_IMPOSTO,

        COD\_EMPRESA,

        GRUPO\_FISCAL,

        COD\_ESTAB,

        PERIODO,

        COD\_ARRECADACAO,

        COD\_RECEITA,

        NUM\_DOC\_ORIGEM,

        SERIE,

        CHAVE\_NFE,

        UF\_FAVORECIDA,

        DATA\_EMISSAO,

        DATA\_PAGAMENTO,

        CONVENIO,

        DETALHAMENTO\_RECEITA,

        PRODUTO,

        INF\_COMPLEMENTAR,

        VALOR\_FECP,

        REGRA\_IMPOSTO

UNION

SELECT GRUPO\_IMPOSTO,

        COD\_EMPRESA,

        GRUPO\_FISCAL,

        COD\_ESTAB,

        PERIODO,

        COD\_ARRECADACAO,

        COD\_RECEITA,

        NUM\_DOC\_ORIGEM,

        SERIE,

        CHAVE\_NFE,

        DATA\_EMISSAO,

        uf\_favorecida,

        SUM\(VALOR\_PRINCIPAL\) VALOR\_PRINCIPAL,

        MAX\(DATA\_VENCIMENTO\) DATA\_VENCIMENTO,

        DATA\_PAGAMENTO,

        CONVENIO,

        DETALHAMENTO\_RECEITA,

        PRODUTO,

        INF\_COMPLEMENTAR,

        VALOR\_FECP,

        REGRA\_IMPOSTO

  FROM \(

SELECT

       'ICMS\_INCENTIVADO'                                        GRUPO\_IMPOSTO,

       APU\.COD\_EMPRESA                                           COD\_EMPRESA,

       REPLACE\(FLX\.GRUPO\_FISCAL,'',''\)                           GRUPO\_FISCAL,

       APU\.COD\_ESTAB                                             COD\_ESTAB,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)                     PERIODO,

       FLX\.COD\_ARRECADACAO                                       COD\_ARRECADACAO,

       FLX\.COD\_RECEITA                                           COD\_RECEITA,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)||FLX\.COD\_RECEITA||1 NUM\_DOC\_ORIGEM,

       NULL                                                      SERIE,

       NULL                                                      CHAVE\_NFE,

       NULL                                                      DATA\_EMISSAO,

       STD\.COD\_ESTADO                                            UF\_FAVORECIDA,

       ROUND\(\(apu\.val\_item\_discrim  \* 0\.05\),2\)                   VALOR\_PRINCIPAL,

       TO\_CHAR\(GP\_DT\_GERA\_GUIAS\_CPROC\.calcula\_data\_vencimento\(FLX\.REGRA\_VENCTO,FLX\.DIA\_VENCTO,\(TO\_CHAR\(\(APU\.DAT\_APURACAO \+1\),'MMYYYY'\)\),EST\.IDENT\_ESTADO,EST\.COD\_MUNICIPIO\),'YYYYMMDD'\) DATA\_VENCIMENTO,

       NULL                                                      DATA\_PAGAMENTO,

       FLX\.CONVENIO                                              CONVENIO,

       FLX\.DETALHE\_RECEITA                                       DETALHAMENTO\_RECEITA,

       FLX\.PRODUTO                                               PRODUTO,

       FLX\.INF\_COMPLEMENTAR                                      INF\_COMPLEMENTAR,

       null                                                      VALOR\_FECP,

       'REGRA\_ICMS\_INCENTIVADO\_2'                                 REGRA\_IMPOSTO

  FROM ITEM\_APURAC\_DISCR APU, ZGP\_VW\_UF\_CD\_RC\_GP\_IMP\_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD

 WHERE APU\.COD\_TIPO\_LIVRO = '108'

   AND APU\.COD\_OPER\_APUR  = '012'

   AND apu\.val\_item\_discrim    > 0

   AND APU\.COD\_EMPRESA    = FLX\.cod\_empresa

   AND APU\.COD\_ESTAB      = FLX\.cod\_estab

   AND UPPER\(FLX\.GRUPO\_IMPOSTO\)  = UPPER\('ICMS\_INCENTIVADO'\)

   AND APU\.COD\_EMPRESA    = EST\.COD\_EMPRESA

   AND APU\.COD\_ESTAB      = EST\.COD\_ESTAB

   AND EST\.IDENT\_ESTADO   = STD\.IDENT\_ESTADO

   AND STD\.COD\_ESTADO     = FLX\.UF

   \-\-AND UPPER\(APU\.DSC\_ITEM\_APURACAO\) LIKE '%VLR\_PRO\_MARANHAO%'

   AND UPPER\(APU\.DSC\_ITEM\_APURACAO\) = 'VLR\_PRO\_MARANHAO'

   AND FLX\.REGRA\_IMPOSTO  = 'REGRA\_ICMS\_INCENTIVADO\_2'\)

   GROUP BY GRUPO\_IMPOSTO,

        COD\_EMPRESA,

        GRUPO\_FISCAL,

        COD\_ESTAB,

        PERIODO,

        COD\_ARRECADACAO,

        COD\_RECEITA,

        NUM\_DOC\_ORIGEM,

        SERIE,

        CHAVE\_NFE,

        UF\_FAVORECIDA,

        DATA\_EMISSAO,

        DATA\_PAGAMENTO,

        CONVENIO,

        DETALHAMENTO\_RECEITA,

        PRODUTO,

        INF\_COMPLEMENTAR,

        VALOR\_FECP,

        REGRA\_IMPOSTO

  \) J, GP\_ESTAB\_TEMP\_CPROC TM

 where TM\.EMPRESA                             = J\.COD\_EMPRESA

   and TM\.ESTAB                               = J\.COD\_ESTAB

   and J\.COD\_EMPRESA                          = MCOD\_EMPRESA

   and to\_char\(last\_day\(tm\.dT\_PERIODO\), 'YYYYMMDD'\) = J\.PERIODO

   and upper\(TRIM\(TM\.GRP\_IMP\)\)                = upper\(J\.GRUPO\_IMPOSTO\)

   and J\.UF\_FAVORECIDA                LIKE DECODE\(tm\.uf\_estab, 'TD', '%', tm\.uf\_estab\)

   and J\.COD\_EMPRESA   = v\_cod\_empresa

   and tm\.saida        = v\_tipo\_saida

   and tm\.id\_proc      = v\_mcod\_id;

    REG geraJSON4%rowtype;

        v\_arquivo sys\.utl\_file\.file\_type;

        vs\_arquivo          varchar2\(32767\);

        mLinha              Varchar2\(2000\);

        v\_saida             varchar2\(1\);

    BEGIN

    loga\('GERA\_ICMS\_INCENTIVADO',FALSE\);

    FOR r\_pallet IN geraJSON4 LOOP

        vPalet\_Count := geraJSON4%ROWCOUNT;

        v\_saida      := r\_pallet\.p\_tipo\_saida;

    END LOOP;

    loga\('Qtde Registros:'||vPalet\_Count,FALSE\);

    IF vPalet\_Count = 0 then

         lib\_proc\.add\_log\('SEM DADOS PARA GERACAO DO ARQUIVO NO PERIODO E GRUPO SELECIONADO',1\);

         lib\_proc\.add\_log\('PERIODO: '||TO\_CHAR\(v\_periodo, 'MM/YYYY'\) ,1\);

         lib\_proc\.add\_log\('GRUPO DE IMPOSTO: '||v\_grupo\_imposto,1\);

     else

        FOR REG in geraJSON4 loop

        vCount := vCount\+1;

        If geraJSON4%ROWCOUNT = 1 Then

        if reg\.p\_tipo\_saida = 1 then

           v\_arquivo := SYS\.utl\_file\.fopen\(VS\_DIRETORIO,mproc\_id||'\_DOOTAX\_'|| REG\.GRUPO\_IMPOSTO||'\_'||to\_char\(trunc\(sysdate\), 'YYYYMMDD'\) ||'\.txt', 'W',32767\);

           SYS\.utl\_file\.put\_line\(v\_arquivo,\('\{"contas\_a\_pagar":\['\)||CHR\(10\)\);

           SYS\.utl\_file\.put\_line\(v\_arquivo, \('\{'\)||CHR\(10\)\);

           vs\_arquivo := '\{';

        elsif reg\.p\_tipo\_saida = 2 then

              LIB\_PROC\.ADD\_TIPO\(MPROC\_ID, 1, mproc\_id||'\_'|| REG\.GRUPO\_IMPOSTO||'\_'||to\_char\(trunc\(sysdate\), 'YYYYMMDD'\) ||'\.txt', 2\);

              vs\_arquivo := \('\{"contas\_a\_pagar":\['\);

              mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

              LIB\_PROC\.add\(mLinha, null, null, 1\);

              vs\_arquivo := \('\{'\);

              mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

              LIB\_PROC\.add\(mLinha, null, null, 1\);

        end if;

        lib\_proc\.add\_log\('  |Geracao arquivo JSON | NOME DO ARQUIVO: ''  |Geracao arquivo JSON | NOME DO ARQUIVO: '||mproc\_id||'\_'|| REG\.GRUPO\_IMPOSTO||'\_'||to\_char\(trunc\(sysdate\), 'YYYYMMDD'\) ||'\.txt   '||'DIRETORIO: '||VS\_DIRETORIO   ,1\);

        lib\_proc\.add\_log\('\{"contas\_a\_pagar":\[',1\);

        lib\_proc\.add\_log\('\{',1\);

        Else

            if reg\.p\_tipo\_saida = 1 then

               SYS\.utl\_file\.put\_line\(v\_arquivo, \('\{'\)||CHR\(10\)\);

               vs\_arquivo := \('\{'\);

            elsif reg\.p\_tipo\_saida = 2 then

                  vs\_arquivo := \('\{'\);

                  mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                  LIB\_PROC\.add\(mLinha, null, null, 1\);

            end if;

            lib\_proc\.add\_log\('\{',1\);

        End If;

        if reg\.p\_tipo\_saida = 1 then

        sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('cod\_empresa'    , reg\.cod\_empresa\)\)||CHR\(10\)\);

        sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('cod\_estab'      , reg\.cod\_estab\)\)||CHR\(10\)\);

        sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('periodo'        , reg\.periodo\)\)||CHR\(10\)\);

        sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('cod\_arrecadacao', reg\.cod\_arrecadacao\)\)||CHR\(10\)\);

        sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('cod\_receita'    , reg\.cod\_receita\)\)||CHR\(10\)\);

        sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('uf\_favorecida'  , reg\.uf\_favorecida\)\)||CHR\(10\)\);

        if reg\.num\_doc\_origem is not null then

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('num\_doc\_origem' , reg\.num\_doc\_origem\)\)||CHR\(10\)\);

        end if;

        IF REG\.SERIE IS NOT NULL THEN

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('serie' , reg\.serie\)\)||CHR\(10\)\);

        END IF;

        IF REG\.DETALHAMENTO\_RECEITA IS NOT NULL THEN

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('det\_receita' , reg\.detalhamento\_receita\)\)||CHR\(10\)\);

        END IF;

        IF REG\.PRODUTO IS NOT NULL THEN

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('cod\_produto' , reg\.produto\)\)||CHR\(10\)\);

        END IF;

        IF REG\.CONVENIO IS NOT NULL THEN

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('convenio' , reg\.convenio\)\)||CHR\(10\)\);

        END IF;

        IF REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' then

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('vlr\_principal' , replace\(trim\(to\_char\(reg\.valor\_principal,'999999990D99'\)\),',','\.'\),true\)\)||CHR\(10\)\);

        ELSE

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('vlr\_principal' , replace\(trim\(to\_char\(reg\.valor\_principal,'999999990D99'\)\),',','\.'\)\)\)||CHR\(10\)\);

        END IF;

        IF REG\.CHAVE\_NFE IS NOT NULL THEN

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('chave\_dfe' , reg\.chave\_nfe\)\)||CHR\(10\)\);

        END IF;

        \-\-\-\-\-

        CASE WHEN REG\.VALOR\_FECP IS NOT NULL AND REG\.VALOR\_FECP > 0 THEN

           CASE WHEN REG\.INF\_COMPLEMENTAR IS NOT NULL THEN

              CASE WHEN REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                 SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

              ELSE

                 sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_vencimento' , reg\.data\_vencimento\)\)||CHR\(10\)\);

              END CASE;

              CASE WHEN REG\.DATA\_PAGAMENTO IS NOT NULL THEN

                 sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_vencimento' , reg\.data\_vencimento\)\)||CHR\(10\)\);

              ELSE NULL;

              END CASE;

              sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('vlr\_fecp' , replace\(trim\(to\_char\(reg\.valor\_fecp,'999999990D99'\)\),',','\.'\),true\)\)||CHR\(10\)\);

           ELSE

              CASE WHEN REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                 SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)||CHR\(10\)\);

              ELSE

                 sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_vencimento' , reg\.data\_vencimento\)\)||CHR\(10\)\);

              END CASE;

              CASE WHEN REG\.DATA\_PAGAMENTO IS NOT NULL THEN

                 sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_pagamento' , reg\.data\_pagamento\)\)||CHR\(10\)\);

              ELSE NULL;

              END CASE;

             sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('vlr\_fecp' , replace\(trim\(to\_char\(reg\.valor\_fecp,'999999990D99'\)\),',','\.'\)\)\)||CHR\(10\)\);

             sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('inf\_complementar' , to\_char\(reg\.inf\_complementar\),true\)\)||CHR\(10\)\);

          END CASE;

       ELSE

           CASE WHEN REG\.INF\_COMPLEMENTAR IS NULL THEN

              CASE WHEN REG\.DATA\_PAGAMENTO IS NULL THEN

                 CASE WHEN REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                    SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

                 ELSE

                    sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_vencimento' , to\_char\(reg\.data\_vencimento\),TRUE\)\)||CHR\(10\)\);

                 END CASE;

              ELSE

                 CASE WHEN REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' then

                    SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

                 ELSE

                    sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_vencimento' , to\_char\(reg\.data\_vencimento\)\)\)||CHR\(10\)\);

                 END CASE;

                    sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_pagamento' , to\_char\(reg\.data\_pagamento\),TRUE\)\)||CHR\(10\)\);

              END CASE;

           ELSE

              CASE WHEN REG\.UF\_FAVORECIDA = 'AM'  AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                 SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

              ELSE

                    sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_vencimento' , to\_char\(reg\.data\_vencimento\)\)\)||CHR\(10\)\);

              END CASE;

              CASE WHEN REG\.DATA\_PAGAMENTO IS NOT NULL THEN

                        sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_vencimento' , to\_char\(reg\.data\_pagamento\)\)\)||CHR\(10\)\);

              ELSE NULL;

              END CASE;

                    sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('inf\_complementar' , to\_char\(reg\.inf\_complementar\),TRUE\)\)||CHR\(10\)\);

           END CASE;

       END CASE;

       \-\- SERVIDOR LOCAL

        elsif reg\.p\_tipo\_saida = 2 then

        vs\_arquivo := \(json\('cod\_empresa'    , reg\.cod\_empresa\)\);

        mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

        LIB\_PROC\.add\(mLinha, null, null, 1\);

        vs\_arquivo := \(json\('cod\_estab'      , reg\.cod\_estab\)\);

        mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

        LIB\_PROC\.add\(mLinha, null, null, 1\);

        IF REG\.REGRA\_IMPOSTO = 'REGRA\_DIFAL\_2' THEN

           vs\_arquivo := \(json\('periodo'        , reg\.data\_emissao\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        ELSE

           vs\_arquivo := \(json\('periodo'        , reg\.periodo\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        END IF;

        vs\_arquivo := \(json\('cod\_arrecadacao', reg\.cod\_arrecadacao\)\);

        mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

        LIB\_PROC\.add\(mLinha, null, null, 1\);

        vs\_arquivo := \(json\('cod\_receita'    , reg\.cod\_receita\)\);

        mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

        LIB\_PROC\.add\(mLinha, null, null, 1\);

        vs\_arquivo := \(json\('uf\_favorecida'  , reg\.uf\_favorecida\)\);

        mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

        LIB\_PROC\.add\(mLinha, null, null, 1\);

        if reg\.num\_doc\_origem is not null then

           vs\_arquivo := \(json\('num\_doc\_origem' , reg\.num\_doc\_origem\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        end if;

        IF REG\.SERIE IS NOT NULL THEN

           vs\_arquivo := \(json\('serie'  , reg\.serie\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        END IF;

        IF REG\.DETALHAMENTO\_RECEITA IS NOT NULL THEN

           vs\_arquivo := \(json\('det\_receita'  , reg\.detalhamento\_receita\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        END IF;

        IF REG\.PRODUTO IS NOT NULL THEN

           vs\_arquivo := \(json\('cod\_produto'  , reg\.produto\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        END IF;

        IF REG\.CONVENIO IS NOT NULL THEN

           vs\_arquivo := \(json\('convenio'  , reg\.convenio\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        END IF;

        IF REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' then

           vs\_arquivo := \(json\('vlr\_principal'  , replace\(trim\(to\_char\(reg\.valor\_principal,'999999990D99'\)\),',','\.'\),true\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        ELSE

           vs\_arquivo := \(json\('vlr\_principal'  , replace\(trim\(to\_char\(reg\.valor\_principal,'999999990D99'\)\),',','\.'\)\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        END IF;

        IF REG\.CHAVE\_NFE IS NOT NULL THEN

              vs\_arquivo := \(json\('chave\_dfe'  , reg\.chave\_nfe\)\);

              mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

              LIB\_PROC\.add\(mLinha, null, null, 1\);

        END IF;

        CASE WHEN REG\.VALOR\_FECP IS NOT NULL AND REG\.VALOR\_FECP > 0 THEN

           CASE WHEN REG\.INF\_COMPLEMENTAR IS NOT NULL THEN

              CASE WHEN REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                 SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

              ELSE

                 vs\_arquivo := \(json\('data\_vencimento'  , to\_char\(reg\.data\_vencimento\)\)\);

                 mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                 LIB\_PROC\.add\(mLinha, null, null, 1\);

              END CASE;

              CASE WHEN REG\.DATA\_PAGAMENTO IS NOT NULL THEN

                 vs\_arquivo := \(json\('data\_vencimento'  , to\_char\(reg\.data\_pagamento\)\)\);

                 mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                 LIB\_PROC\.add\(mLinha, null, null, 1\);

              ELSE NULL;

              END CASE;

              vs\_arquivo := \(json\('vlr\_fecp'  , replace\(trim\(to\_char\(reg\.valor\_fecp,'999999990D99'\)\),',','\.'\),true\)\);

              mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

              LIB\_PROC\.add\(mLinha, null, null, 1\);

           ELSE

              CASE WHEN REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                 SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

              ELSE

                 vs\_arquivo := \(json\('data\_vencimento'  , to\_char\(reg\.data\_vencimento\)\)\);

                 mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                 LIB\_PROC\.add\(mLinha, null, null, 1\);

              END CASE;

              CASE WHEN REG\.DATA\_PAGAMENTO IS NOT NULL THEN

                 vs\_arquivo := \(json\('data\_pagamento'  , to\_char\(reg\.data\_pagamento\)\)\);

                 mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                 LIB\_PROC\.add\(mLinha, null, null, 1\);

              ELSE NULL;

              END CASE;

             vs\_arquivo := \(json\('vlr\_fecp'  , replace\(trim\(to\_char\(reg\.valor\_fecp,'999999990D99'\)\),',','\.'\)\)\);

             mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

             LIB\_PROC\.add\(mLinha, null, null, 1\);

             vs\_arquivo := \(json\('inf\_complementar'  , to\_char\(reg\.inf\_complementar\),true\)\);

             mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

             LIB\_PROC\.add\(mLinha, null, null, 1\);

          END CASE;

       ELSE

           CASE WHEN REG\.INF\_COMPLEMENTAR IS NULL THEN

              CASE WHEN REG\.DATA\_PAGAMENTO IS NULL THEN

                 CASE WHEN REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                    SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

                 ELSE

                    vs\_arquivo := \(json\('data\_vencimento'  , to\_char\(reg\.data\_vencimento\),TRUE\)\);

                    mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                    LIB\_PROC\.add\(mLinha, null, null, 1\);

                 END CASE;

              ELSE

                 CASE WHEN REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' then

                    SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

                 ELSE

                    vs\_arquivo := \(json\('data\_vencimento'  , to\_char\(reg\.data\_vencimento\)\)\);

                    mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                    LIB\_PROC\.add\(mLinha, null, null, 1\);

                 END CASE;

                    vs\_arquivo := \(json\('data\_pagamento'  , to\_char\(reg\.data\_pagamento\),TRUE\)\);

                    mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                    LIB\_PROC\.add\(mLinha, null, null, 1\);

              END CASE;

           ELSE

              CASE WHEN REG\.UF\_FAVORECIDA = 'AM'  AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                 SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

              ELSE

                    vs\_arquivo := \(json\('data\_vencimento'  , to\_char\(reg\.data\_vencimento\)\)\);

                    mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                    LIB\_PROC\.add\(mLinha, null, null, 1\);

              END CASE;

              CASE WHEN REG\.DATA\_PAGAMENTO IS NOT NULL THEN

                    vs\_arquivo := \(json\('data\_vencimento'  , to\_char\(reg\.data\_pagamento\)\)\);

                    mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                    LIB\_PROC\.add\(mLinha, null, null, 1\);

              ELSE NULL;

              END CASE;

                    vs\_arquivo := \(json\('inf\_complementar'  , to\_char\(reg\.inf\_complementar\),TRUE\)\);

                    mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                    LIB\_PROC\.add\(mLinha, null, null, 1\);

            END CASE;

       END CASE;

        end if;

        lib\_proc\.add\_log\(json\('cod\_empresa'    , reg\.cod\_empresa\),1\);

        lib\_proc\.add\_log\(json\('cod\_estab'      , reg\.cod\_estab\),1\);

        lib\_proc\.add\_log\(json\('periodo'        , reg\.periodo\),1\);

        lib\_proc\.add\_log\(json\('cod\_arrecadacao', reg\.cod\_arrecadacao\),1\);

        lib\_proc\.add\_log\(json\('cod\_receita'    , reg\.cod\_receita\),1\);

        lib\_proc\.add\_log\(json\('uf\_favorecida'  , reg\.uf\_favorecida\),1\);

        if reg\.num\_doc\_origem is not null then

           lib\_proc\.add\_log\(json\('num\_doc\_origem' , reg\.num\_doc\_origem\),1\);

        end if;

        if reg\.serie is not null then

           lib\_proc\.add\_log\(json\('serie' , reg\.serie\),1\);

        end if;

        if reg\.data\_vencimento is not null then

           lib\_proc\.add\_log\(json\('data\_vencimento' , reg\.data\_vencimento\),1\);

        end if;

        if reg\.data\_pagamento is not null then

           lib\_proc\.add\_log\(json\('data\_pagamento' , reg\.data\_pagamento\),1\);

        end if;

        if reg\.convenio is not null then

           lib\_proc\.add\_log\(json\('convenio' , reg\.convenio\),1\);

        end if;

        if reg\.produto is not null then

           lib\_proc\.add\_log\(json\('produto' , reg\.produto\),1\);

        end if;

        if reg\.detalhamento\_receita is not null then

           lib\_proc\.add\_log\(json\('det\_receita' , reg\.detalhamento\_receita\),1\);

        end if;

        if reg\.inf\_complementar is not null then

           lib\_proc\.add\_log\(json\('inf\_complementar' , reg\.inf\_complementar\),1\);

        end if;

        if reg\.chave\_nfe is null then

           if reg\.valor\_fecp is not null then

           lib\_proc\.add\_log\(json\('vlr\_principal'  , reg\.valor\_principal\),1\);

           lib\_proc\.add\_log\(json\('valor\_fecp' , reg\.valor\_fecp,true\),1\);

           else

           lib\_proc\.add\_log\(json\('vlr\_principal'  , reg\.valor\_principal,true\),1\);

           end if;

        else

           if reg\.valor\_fecp is not null then

           lib\_proc\.add\_log\(json\('vlr\_principal'  , reg\.valor\_principal\),1\);

           lib\_proc\.add\_log\(json\('valor\_fecp' , reg\.valor\_fecp\),1\);

           else

           lib\_proc\.add\_log\(json\('vlr\_principal'  , reg\.valor\_principal,true\),1\);

           end if;

           lib\_proc\.add\_log\(json\('vlr\_principal'  , reg\.valor\_principal\),1\);

           lib\_proc\.add\_log\(json\('chave\_dfe' , reg\.chave\_nfe,true\),1\);

        end if;

           if reg\.p\_tipo\_saida = 1 then

              \-\-Se houver mais de 1 bloco no json insere virgula ao final do bloco, exceto no ultimo registro\.

              if vCount < vPalet\_Count then

                 sys\.utl\_file\.put\_line\(v\_arquivo, \('\},'\)\);

              else

                 sys\.utl\_file\.put\_line\(v\_arquivo, \('\}'\)\);

              end if;

           elsif reg\.p\_tipo\_saida = 2 then

                 \-\-Se houver mais de 1 bloco no json insere virgula ao final do bloco, exceto no ultimo registro\.

                 if vCount < vPalet\_Count then

                    vs\_arquivo := \('\},'\);

                    mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                    LIB\_PROC\.add\(mLinha, null, null, 1\);

                    lib\_proc\.add\_log\('\},',1\);

                 else

                     vs\_arquivo := \('\}'\);

                     mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                     LIB\_PROC\.add\(mLinha, null, null, 1\);

                     lib\_proc\.add\_log\('\}',1\);

                 end if;

            end if;

         insert into GP\_LOGS\_JSON\_DT\_CPROC  values \(mproc\_id,

                                                       musuario,

                                                       TO\_CHAR\(SYSDATE, 'DD/MM/YYYY HH24:MI:SS'\),

                                                       reg\.cod\_empresa,

                                                       reg\.cod\_estab,

                                                       reg\.periodo,

                                                       reg\.grupo\_imposto,

                                                       reg\.cod\_arrecadacao,

                                                       reg\.cod\_receita,

                                                       reg\.uf\_favorecida,

                                                       reg\.num\_doc\_origem,

                                                       reg\.serie,

                                                       reg\.chave\_nfe,

                                                       reg\.valor\_principal,

                                                       reg\.valor\_fecp,

                                                       reg\.data\_vencimento,

                                                       reg\.data\_pagamento,

                                                       reg\.inf\_complementar,

                                                       reg\.detalhamento\_receita,

                                                       reg\.convenio,

                                                       reg\.produto\);

        \-\-commit;

        end loop;

        if v\_saida = 1 then

           sys\.utl\_file\.put\_line\(v\_arquivo, \('\]\}'||CHR\(13\)\)\);

        elsif v\_saida = 2 then

              vs\_arquivo := \('\]\}'\);

              mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

              LIB\_PROC\.add\(mLinha, null, null, 1\);

        end if;

        lib\_proc\.add\_log\('\]\}',1\);

        sys\.utl\_file\.fclose\(v\_arquivo\);

           end if;

           delete from GP\_ESTAB\_TEMP\_CPROC where id\_proc = mproc\_id;

           COMMIT;

       END;

END GERA\_ICMS\_INCENTIVADO;

PROCEDURE GERA\_FUNDO\_ICMS\_NORMAL\(v\_mcod\_id         number,

                                    v\_cod\_empresa     varchar2,

                                    v\_cod\_estab       varchar2,

                                    v\_periodo         date,

                                    v\_grupo\_imposto   varchar2,

                                    v\_uf              varchar2,

                                    v\_tipo\_saida      varchar2\) IS

   FUNCTION json\(nome\_campo varchar2, valor varchar2, ultimo boolean default false\) return varchar2 IS

    v\_retorno varchar2\(200\) := '';

    BEGIN

      IF ultimo THEN

        v\_retorno := '"'||nome\_campo||'":"'||valor||'"';

      ELSE

        v\_retorno := '"'||nome\_campo||'":"'||valor||'",';

      END IF;

    return v\_retorno;

  END json;

   BEGIN

   DECLARE

        vPalet\_Count NUMBER := 0;

        vCount NUMBER := 0;

        v\_arq NUMBER :=0;

        v\_grp VARCHAR2\(30\) := '';

   cursor geraJSON5 is

   SELECT GRUPO\_IMPOSTO,

       DECODE\(\(SELECT TRIM\(VALOR\)

                from fpar\_parametros f,  fpar\_param\_det d

               where nome\_framework  = 'GP\_DE\_MSAF\_PARA\_SAP\_CPAR'

                 AND f\.id\_parametros = d\.id\_parametro

                 AND NOME\_PARAM      = 'DEPARA\_EMPR'

                 AND TRIM\(CONTEUDO\)  = COD\_EMPRESA\),NULL,COD\_EMPRESA,\(SELECT TRIM\(VALOR\)

                                                                        from fpar\_parametros f,  fpar\_param\_det d

                                                                       where nome\_framework  = 'GP\_DE\_MSAF\_PARA\_SAP\_CPAR'

                                                                         AND f\.id\_parametros = d\.id\_parametro

                                                                         AND NOME\_PARAM      = 'DEPARA\_EMPR'

                                                                         AND TRIM\(CONTEUDO\)  = COD\_EMPRESA\)\)   COD\_EMPRESA,

       GRUPO\_FISCAL,

       DECODE\(\(SELECT TRIM\(VALOR\)

                 from fpar\_parametros f,  fpar\_param\_det d

                where nome\_framework    = 'GP\_DE\_MSAF\_PARA\_SAP\_CPAR'

                  AND f\.id\_parametros   = d\.id\_parametro

                  AND NOME\_PARAM        = 'DEPARA\_ESTAB'

                  AND TRIM\(CONTEUDO\)    = COD\_ESTAB

                  AND TRIM\(D\.DESCRICAO\) = COD\_EMPRESA\),NULL,COD\_ESTAB, \(SELECT TRIM\(VALOR\)

                                                                        from fpar\_parametros f,  fpar\_param\_det d

                                                                       where nome\_framework    = 'GP\_DE\_MSAF\_PARA\_SAP\_CPAR'

                                                                         AND f\.id\_parametros   = d\.id\_parametro

                                                                         AND NOME\_PARAM        = 'DEPARA\_ESTAB'

                                                                         AND TRIM\(CONTEUDO\)    = COD\_ESTAB

                                                                         AND TRIM\(D\.DESCRICAO\) = COD\_EMPRESA\)\) COD\_ESTAB,

       PERIODO,

       COD\_ARRECADACAO,

       COD\_RECEITA,

       NUM\_DOC\_ORIGEM,

       SERIE,

       CHAVE\_NFE,

       UF\_FAVORECIDA,

       v\_tipo\_saida P\_TIPO\_SAIDA,

       CONVENIO,

       DETALHAMENTO\_RECEITA,

       PRODUTO,

       INF\_COMPLEMENTAR,

       VALOR\_PRINCIPAL,

       DATA\_VENCIMENTO,

       DATA\_PAGAMENTO,

       REGRA\_IMPOSTO,

       VALOR\_FECP,

       NULL CNPJ\_FAVORECIDO,

       NULL IE\_FAVORECIDO,

       0 VLR\_MULTA,

       0 VLR\_JUROS,

       0 VLR\_FECP\_MULTA,

       0 VLR\_FECP\_JUROS,

       NULL DATA\_EMISSAO

  FROM \(

SELECT

       'FUNDO\_ICMS\_NORMAL'                                       GRUPO\_IMPOSTO,

       APU\.COD\_EMPRESA                                           COD\_EMPRESA,

       REPLACE\(FLX\.GRUPO\_FISCAL,'',''\)                           GRUPO\_FISCAL,

       APU\.COD\_ESTAB                                             COD\_ESTAB,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)                     PERIODO,

       FLX\.COD\_ARRECADACAO                                       COD\_ARRECADACAO,

       FLX\.COD\_RECEITA                                           COD\_RECEITA,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)||FLX\.COD\_RECEITA||1 NUM\_DOC\_ORIGEM,

       NULL                                                      SERIE,

       NULL                                                      CHAVE\_NFE,

       NULL                                                      DATA\_EMISSAO,

       STD\.COD\_ESTADO                                            UF\_FAVORECIDA,

       sum\(nvl\(apu\.val\_item\_discrim,0\)\)                                         VALOR\_PRINCIPAL,

       TO\_CHAR\(GP\_DT\_GERA\_GUIAS\_CPROC\.calcula\_data\_vencimento\(FLX\.REGRA\_VENCTO,FLX\.DIA\_VENCTO,\(TO\_CHAR\(\(APU\.DAT\_APURACAO \+1\),'MMYYYY'\)\),EST\.IDENT\_ESTADO,EST\.COD\_MUNICIPIO\),'YYYYMMDD'\) DATA\_VENCIMENTO,

       NULL                                                      DATA\_PAGAMENTO,

       FLX\.CONVENIO                                              CONVENIO,

       FLX\.DETALHE\_RECEITA                                       DETALHAMENTO\_RECEITA,

       FLX\.PRODUTO                                               PRODUTO,

       FLX\.INF\_COMPLEMENTAR                                      INF\_COMPLEMENTAR,

       null                                                      VALOR\_FECP,

       'REGRA\_FUNDO\_ICMS\_NORMAL\_1'                                 REGRA\_IMPOSTO

  FROM ITEM\_APURAC\_DISCR APU, ZGP\_VW\_UF\_CD\_RC\_GP\_IMP\_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD

 WHERE APU\.COD\_TIPO\_LIVRO = '108'

   AND APU\.COD\_OPER\_APUR  = '007'

   AND apu\.val\_item\_discrim    > 0

   AND APU\.COD\_EMPRESA    = FLX\.cod\_empresa

   AND APU\.COD\_ESTAB      = FLX\.cod\_estab

   AND UPPER\(FLX\.GRUPO\_IMPOSTO\)  = UPPER\('FUNDO\_ICMS\_NORMAL'\)

   \-\-AND UPPER\(DSC\_ITEM\_APURACAO\)  LIKE '%FUNDO%DE%COMBATE%A%POBREZA%'

   AND UPPER\(DSC\_ITEM\_APURACAO\)  like '%REF\. FUNDO DE COMBATE A POBREZA%'

   AND APU\.COD\_EMPRESA    = EST\.COD\_EMPRESA

   AND APU\.COD\_ESTAB      = EST\.COD\_ESTAB

   AND EST\.IDENT\_ESTADO   = STD\.IDENT\_ESTADO

   AND STD\.COD\_ESTADO     = FLX\.UF

   AND FLX\.REGRA\_IMPOSTO  = 'REGRA\_FUNDO\_ICMS\_NORMAL\_1'

   group by 'FUNDO\_ICMS\_NORMAL',

   APU\.COD\_EMPRESA,

   REPLACE\(FLX\.GRUPO\_FISCAL,'',''\),

   APU\.COD\_ESTAB,

   TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\),

   FLX\.COD\_ARRECADACAO,

   FLX\.COD\_RECEITA,

   TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)||FLX\.COD\_RECEITA||1,

   NULL, NULL, NULL,

   STD\.COD\_ESTADO,

   TO\_CHAR\(GP\_DT\_GERA\_GUIAS\_CPROC\.calcula\_data\_vencimento\(FLX\.REGRA\_VENCTO,FLX\.DIA\_VENCTO,\(TO\_CHAR\(\(APU\.DAT\_APURACAO \+1\),'MMYYYY'\)\),EST\.IDENT\_ESTADO,EST\.COD\_MUNICIPIO\),'YYYYMMDD'\),

   NULL, FLX\.CONVENIO,

   FLX\.DETALHE\_RECEITA,

   FLX\.PRODUTO, FLX\.INF\_COMPLEMENTAR, null, 'REGRA\_FUNDO\_ICMS\_NORMAL\_1'

UNION

SELECT

       'FUNDO\_ICMS\_NORMAL'                                       GRUPO\_IMPOSTO,

       APU\.COD\_EMPRESA                                           COD\_EMPRESA,

       REPLACE\(FLX\.GRUPO\_FISCAL,'',''\)                           GRUPO\_FISCAL,

       APU\.COD\_ESTAB                                             COD\_ESTAB,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)                     PERIODO,

       FLX\.COD\_ARRECADACAO                                       COD\_ARRECADACAO,

       FLX\.COD\_RECEITA                                           COD\_RECEITA,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)||FLX\.COD\_RECEITA||1 NUM\_DOC\_ORIGEM,

       NULL                                                      SERIE,

       NULL                                                      CHAVE\_NFE,

       NULL                                                      DATA\_EMISSAO,

       STD\.COD\_ESTADO                                            UF\_FAVORECIDA,

       ROUND\(\(apu\.val\_item\_discrim \* 0\.1\),2\)                     VALOR\_PRINCIPAL,

       TO\_CHAR\(GP\_DT\_GERA\_GUIAS\_CPROC\.calcula\_data\_vencimento\(FLX\.REGRA\_VENCTO,FLX\.DIA\_VENCTO,\(TO\_CHAR\(\(APU\.DAT\_APURACAO \+1\),'MMYYYY'\)\),EST\.IDENT\_ESTADO,EST\.COD\_MUNICIPIO\),'YYYYMMDD'\) DATA\_VENCIMENTO,

       NULL                                                      DATA\_PAGAMENTO,

       FLX\.CONVENIO                                              CONVENIO,

       FLX\.DETALHE\_RECEITA                                       DETALHAMENTO\_RECEITA,

       FLX\.PRODUTO                                               PRODUTO,

       FLX\.INF\_COMPLEMENTAR                                      INF\_COMPLEMENTAR,

       null                                                      VALOR\_FECP,

       'REGRA\_FUNDO\_ICMS\_NORMAL\_2'                               REGRA\_IMPOSTO

  FROM ITEM\_APURAC\_DISCR APU, ZGP\_VW\_UF\_CD\_RC\_GP\_IMP\_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD

 WHERE APU\.COD\_TIPO\_LIVRO = '108'

   AND APU\.COD\_OPER\_APUR  = '012'

   AND apu\.val\_item\_discrim    > 0

   AND APU\.COD\_EMPRESA    = FLX\.cod\_empresa

   AND APU\.COD\_ESTAB      = FLX\.cod\_estab

   AND UPPER\(FLX\.GRUPO\_IMPOSTO\)  = UPPER\('FUNDO\_ICMS\_NORMAL'\)

   \-\-AND UPPER\(DSC\_ITEM\_APURACAO\)  LIKE '%VLR\_FEEF%'

   AND UPPER\(DSC\_ITEM\_APURACAO\)  LIKE UPPER\('%INCENTIVO FISCAL%'\)

   AND APU\.COD\_EMPRESA    = EST\.COD\_EMPRESA

   AND APU\.COD\_ESTAB      = EST\.COD\_ESTAB

   AND EST\.IDENT\_ESTADO   = STD\.IDENT\_ESTADO

   AND STD\.COD\_ESTADO     = FLX\.UF

   AND FLX\.REGRA\_IMPOSTO  = 'REGRA\_FUNDO\_ICMS\_NORMAL\_2'

UNION

SELECT

       'FUNDO\_ICMS\_NORMAL'                                       GRUPO\_IMPOSTO,

       APU\.COD\_EMPRESA                                           COD\_EMPRESA,

       REPLACE\(FLX\.GRUPO\_FISCAL,'',''\)                           GRUPO\_FISCAL,

       APU\.COD\_ESTAB                                             COD\_ESTAB,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)                     PERIODO,

       FLX\.COD\_ARRECADACAO                                       COD\_ARRECADACAO,

       FLX\.COD\_RECEITA                                           COD\_RECEITA,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)||FLX\.COD\_RECEITA||1 NUM\_DOC\_ORIGEM,

       NULL                                                      SERIE,

       NULL                                                      CHAVE\_NFE,

       NULL                                                      DATA\_EMISSAO,

       STD\.COD\_ESTADO                                            UF\_FAVORECIDA,

       apu\.val\_item\_discrim                                      VALOR\_PRINCIPAL,

       TO\_CHAR\(GP\_DT\_GERA\_GUIAS\_CPROC\.calcula\_data\_vencimento\(FLX\.REGRA\_VENCTO,FLX\.DIA\_VENCTO,\(TO\_CHAR\(\(APU\.DAT\_APURACAO \+1\),'MMYYYY'\)\),EST\.IDENT\_ESTADO,EST\.COD\_MUNICIPIO\),'YYYYMMDD'\) DATA\_VENCIMENTO,

       NULL                                                      DATA\_PAGAMENTO,

       FLX\.CONVENIO                                              CONVENIO,

       FLX\.DETALHE\_RECEITA                                       DETALHAMENTO\_RECEITA,

       FLX\.PRODUTO                                               PRODUTO,

       FLX\.INF\_COMPLEMENTAR                                      INF\_COMPLEMENTAR,

       null                                                      VALOR\_FECP,

       'REGRA\_FUNDO\_ICMS\_NORMAL\_3'                                 REGRA\_IMPOSTO

  FROM ITEM\_APURAC\_DISCR APU, ZGP\_VW\_UF\_CD\_RC\_GP\_IMP\_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD

 WHERE APU\.COD\_TIPO\_LIVRO = '108'

   AND APU\.COD\_OPER\_APUR  = '012'

   AND apu\.val\_item\_discrim    > 0

   AND APU\.COD\_EMPRESA    = FLX\.cod\_empresa

   AND APU\.COD\_ESTAB      = FLX\.cod\_estab

   AND UPPER\(FLX\.GRUPO\_IMPOSTO\)  = UPPER\('FUNDO\_ICMS\_NORMAL'\)

   \-\-AND UPPER\(DSC\_ITEM\_APURACAO\)  LIKE '%DEDU%REFERENTE%AO%FECOP%ICMS%'

   AND UPPER\(DSC\_ITEM\_APURACAO\)  = 'DEDU  ES REFERENTE AO FECOP ICMS'

   AND APU\.COD\_EMPRESA    = EST\.COD\_EMPRESA

   AND APU\.COD\_ESTAB      = EST\.COD\_ESTAB

   AND EST\.IDENT\_ESTADO   = STD\.IDENT\_ESTADO

   AND STD\.COD\_ESTADO     = FLX\.UF

   AND FLX\.REGRA\_IMPOSTO  = 'REGRA\_FUNDO\_ICMS\_NORMAL\_3'

UNION

SELECT

       'FUNDO\_ICMS\_NORMAL'                                       GRUPO\_IMPOSTO,

       APU\.COD\_EMPRESA                                           COD\_EMPRESA,

       REPLACE\(FLX\.GRUPO\_FISCAL,'',''\)                           GRUPO\_FISCAL,

       APU\.COD\_ESTAB                                             COD\_ESTAB,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)                     PERIODO,

       FLX\.COD\_ARRECADACAO                                       COD\_ARRECADACAO,

       FLX\.COD\_RECEITA                                           COD\_RECEITA,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)||FLX\.COD\_RECEITA||1 NUM\_DOC\_ORIGEM,

       NULL                                                      SERIE,

       NULL                                                      CHAVE\_NFE,

       NULL                                                      DATA\_EMISSAO,

       STD\.COD\_ESTADO                                            UF\_FAVORECIDA,

       ROUND\(\(apu\.val\_item\_discrim \* 0\.1\),2\)                     VALOR\_PRINCIPAL,

       TO\_CHAR\(GP\_DT\_GERA\_GUIAS\_CPROC\.calcula\_data\_vencimento\(FLX\.REGRA\_VENCTO,FLX\.DIA\_VENCTO,\(TO\_CHAR\(\(APU\.DAT\_APURACAO \+1\),'MMYYYY'\)\),EST\.IDENT\_ESTADO,EST\.COD\_MUNICIPIO\),'YYYYMMDD'\) DATA\_VENCIMENTO,

       NULL                                                      DATA\_PAGAMENTO,

       FLX\.CONVENIO                                              CONVENIO,

       FLX\.DETALHE\_RECEITA                                       DETALHAMENTO\_RECEITA,

       FLX\.PRODUTO                                               PRODUTO,

       FLX\.INF\_COMPLEMENTAR                                      INF\_COMPLEMENTAR,

       null                                                      VALOR\_FECP,

       'REGRA\_FUNDO\_ICMS\_NORMAL\_4'                                 REGRA\_IMPOSTO

  FROM ITEM\_APURAC\_DISCR APU, ZGP\_VW\_UF\_CD\_RC\_GP\_IMP\_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD

 WHERE APU\.COD\_TIPO\_LIVRO = '108'

   AND APU\.COD\_OPER\_APUR  = '012'

   AND apu\.val\_item\_discrim    > 0

   AND APU\.COD\_EMPRESA    = FLX\.cod\_empresa

   AND APU\.COD\_ESTAB      = FLX\.cod\_estab

   AND UPPER\(FLX\.GRUPO\_IMPOSTO\)  = UPPER\('FUNDO\_ICMS\_NORMAL'\)

   \-\-AND UPPER\(DSC\_ITEM\_APURACAO\)  LIKE '%VLR\_PROTEGE\_15%'

   AND UPPER\(DSC\_ITEM\_APURACAO\)  LIKE '%INCENTIVO PRO GOIAS%'

   AND APU\.COD\_EMPRESA    = EST\.COD\_EMPRESA

   AND APU\.COD\_ESTAB      = EST\.COD\_ESTAB

   AND EST\.IDENT\_ESTADO   = STD\.IDENT\_ESTADO

   AND STD\.COD\_ESTADO     = FLX\.UF

   AND FLX\.REGRA\_IMPOSTO  = 'REGRA\_FUNDO\_ICMS\_NORMAL\_4'

UNION

SELECT GRUPO\_IMPOSTO,

       COD\_EMPRESA,

       GRUPO\_FISCAL,

       COD\_ESTAB,

       PERIODO,

       COD\_ARRECADACAO,

       COD\_RECEITA,

       NUM\_DOC\_ORIGEM,

       SERIE,

       CHAVE\_NFE,

       DATA\_EMISSAO,

       UF\_FAVORECIDA,

       SUM\(VALOR\_PRINCIPAL\) VALOR\_PRINCIPAL,

       DATA\_VENCIMENTO,

       DATA\_PAGAMENTO,

       CONVENIO,

       DETALHAMENTO\_RECEITA,

       PRODUTO,

       INF\_COMPLEMENTAR,

       VALOR\_FECP,

       REGRA\_IMPOSTO

  FROM \(

SELECT

       'FUNDO\_ICMS\_NORMAL'                                       GRUPO\_IMPOSTO,

       APU\.COD\_EMPRESA                                           COD\_EMPRESA,

       REPLACE\(FLX\.GRUPO\_FISCAL,'',''\)                           GRUPO\_FISCAL,

       APU\.COD\_ESTAB                                             COD\_ESTAB,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)                     PERIODO,

       FLX\.COD\_ARRECADACAO                                       COD\_ARRECADACAO,

       FLX\.COD\_RECEITA                                           COD\_RECEITA,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)||FLX\.COD\_RECEITA||1 NUM\_DOC\_ORIGEM,

       NULL                                                      SERIE,

       NULL                                                      CHAVE\_NFE,

       NULL                                                      DATA\_EMISSAO,

       STD\.COD\_ESTADO                                            UF\_FAVORECIDA,

       DECODE\(apu\.dsc\_item\_apuracao,'FEM \( Fundo de Erradica  o da Mis ria \)',apu\.val\_item\_discrim,apu\.val\_item\_discrim \* \-1\)  VALOR\_PRINCIPAL,

       TO\_CHAR\(GP\_DT\_GERA\_GUIAS\_CPROC\.calcula\_data\_vencimento\(FLX\.REGRA\_VENCTO,FLX\.DIA\_VENCTO,\(TO\_CHAR\(\(APU\.DAT\_APURACAO \+1\),'MMYYYY'\)\),EST\.IDENT\_ESTADO,EST\.COD\_MUNICIPIO\),'YYYYMMDD'\) DATA\_VENCIMENTO,

       NULL                                                      DATA\_PAGAMENTO,

       FLX\.CONVENIO                                              CONVENIO,

       FLX\.DETALHE\_RECEITA                                       DETALHAMENTO\_RECEITA,

       FLX\.PRODUTO                                               PRODUTO,

       FLX\.INF\_COMPLEMENTAR                                      INF\_COMPLEMENTAR,

       null                                                      VALOR\_FECP,

       'REGRA\_FUNDO\_ICMS\_NORMAL\_5'                                 REGRA\_IMPOSTO

  FROM ITEM\_APURAC\_DISCR APU, ZGP\_VW\_UF\_CD\_RC\_GP\_IMP\_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD

 WHERE APU\.COD\_TIPO\_LIVRO = '108'

   AND \(UPPER\(apu\.dsc\_item\_apuracao\) =  UPPER\('D BITO ESPECIAL \- FUNDO ERRADICA  O A MIS RIA \- ESTORNO FEM%'\)

    OR  UPPER\(apu\.dsc\_item\_apuracao\) =  UPPER\('%FEM \( Fundo de Erradica  o da Mis ria \)%'\)\)

   AND APU\.COD\_OPER\_APUR  IN \('003','007'\)

   AND apu\.val\_item\_discrim    > 0

   AND APU\.COD\_EMPRESA    = FLX\.cod\_empresa

   AND APU\.COD\_ESTAB      = FLX\.cod\_estab

   AND UPPER\(FLX\.GRUPO\_IMPOSTO\)  = UPPER\('FUNDO\_ICMS\_NORMAL'\)

   AND APU\.COD\_EMPRESA    = EST\.COD\_EMPRESA

   AND APU\.COD\_ESTAB      = EST\.COD\_ESTAB

   AND EST\.IDENT\_ESTADO   = STD\.IDENT\_ESTADO

   AND STD\.COD\_ESTADO     = FLX\.UF

   AND APU\.COD\_ESTAB      = 'K530'

   AND FLX\.REGRA\_IMPOSTO  = 'REGRA\_FUNDO\_ICMS\_NORMAL\_5' \)

   HAVING SUM\(VALOR\_PRINCIPAL\) > 0

   GROUP BY GRUPO\_IMPOSTO,

       COD\_EMPRESA,

       GRUPO\_FISCAL,

       COD\_ESTAB,

       PERIODO,

       COD\_ARRECADACAO,

       COD\_RECEITA,

       NUM\_DOC\_ORIGEM,

       SERIE,

       CHAVE\_NFE,

       DATA\_EMISSAO,

       UF\_FAVORECIDA,

       DATA\_VENCIMENTO,

       DATA\_PAGAMENTO,

       CONVENIO,

       DETALHAMENTO\_RECEITA,

       PRODUTO,

       INF\_COMPLEMENTAR,

       VALOR\_FECP,

       REGRA\_IMPOSTO

UNION

SELECT GRUPO\_IMPOSTO,

       COD\_EMPRESA,

       GRUPO\_FISCAL,

       COD\_ESTAB,

       PERIODO,

       COD\_ARRECADACAO,

       COD\_RECEITA,

       NUM\_DOC\_ORIGEM,

       SERIE,

       CHAVE\_NFE,

       DATA\_EMISSAO,

       UF\_FAVORECIDA,

       SUM\(VALOR\_PRINCIPAL\) VALOR\_PRINCIPAL,

       DATA\_VENCIMENTO,

       DATA\_PAGAMENTO,

       CONVENIO,

       DETALHAMENTO\_RECEITA,

       PRODUTO,

       INF\_COMPLEMENTAR,

       VALOR\_FECP,

       REGRA\_IMPOSTO

FROM \(

SELECT

       'FUNDO\_ICMS\_NORMAL'                                       GRUPO\_IMPOSTO,

       APU\.COD\_EMPRESA                                           COD\_EMPRESA,

       REPLACE\(FLX\.GRUPO\_FISCAL,'',''\)                           GRUPO\_FISCAL,

       APU\.COD\_ESTAB                                             COD\_ESTAB,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)                     PERIODO,

       FLX\.COD\_ARRECADACAO                                       COD\_ARRECADACAO,

       FLX\.COD\_RECEITA                                           COD\_RECEITA,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)||FLX\.COD\_RECEITA||1 NUM\_DOC\_ORIGEM,

       NULL                                                      SERIE,

       NULL                                                      CHAVE\_NFE,

       NULL                                                      DATA\_EMISSAO,

       STD\.COD\_ESTADO                                            UF\_FAVORECIDA,

       apu\.val\_item\_discrim                                      VALOR\_PRINCIPAL,

       TO\_CHAR\(GP\_DT\_GERA\_GUIAS\_CPROC\.calcula\_data\_vencimento\(FLX\.REGRA\_VENCTO,FLX\.DIA\_VENCTO,\(TO\_CHAR\(\(APU\.DAT\_APURACAO \+1\),'MMYYYY'\)\),EST\.IDENT\_ESTADO,EST\.COD\_MUNICIPIO\),'YYYYMMDD'\) DATA\_VENCIMENTO,

       NULL                                                      DATA\_PAGAMENTO,

       FLX\.CONVENIO                                              CONVENIO,

       FLX\.DETALHE\_RECEITA                                       DETALHAMENTO\_RECEITA,

       FLX\.PRODUTO                                               PRODUTO,

       FLX\.INF\_COMPLEMENTAR                                      INF\_COMPLEMENTAR,

       null                                                      VALOR\_FECP,

       'REGRA\_FUNDO\_ICMS\_NORMAL\_6'                                 REGRA\_IMPOSTO

  FROM ITEM\_APURAC\_DISCR APU, ZGP\_VW\_UF\_CD\_RC\_GP\_IMP\_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD

 WHERE APU\.COD\_TIPO\_LIVRO = '108'

   AND APU\.COD\_OPER\_APUR  = '012'

   AND apu\.val\_item\_discrim    > 0

   AND APU\.COD\_EMPRESA    = FLX\.cod\_empresa

   AND APU\.COD\_ESTAB      = FLX\.cod\_estab

   AND UPPER\(FLX\.GRUPO\_IMPOSTO\)  = UPPER\('FUNDO\_ICMS\_NORMAL'\)

   AND UPPER\(DSC\_ITEM\_APURACAO\)  = upper\('Fundo de Combate e Erradica  o da Pobreza\- FECEP'\)

   AND APU\.COD\_EMPRESA    = EST\.COD\_EMPRESA

   AND APU\.COD\_ESTAB      = EST\.COD\_ESTAB

   AND EST\.IDENT\_ESTADO   = STD\.IDENT\_ESTADO

   AND STD\.COD\_ESTADO     = FLX\.UF

   AND FLX\.REGRA\_IMPOSTO  = 'REGRA\_FUNDO\_ICMS\_NORMAL\_6'\)

   GROUP BY GRUPO\_IMPOSTO, COD\_EMPRESA, GRUPO\_FISCAL, COD\_ESTAB, PERIODO,

COD\_ARRECADACAO, COD\_RECEITA, NUM\_DOC\_ORIGEM, SERIE, CHAVE\_NFE,

UF\_FAVORECIDA, CONVENIO, DETALHAMENTO\_RECEITA, PRODUTO, INF\_COMPLEMENTAR,

DATA\_VENCIMENTO, DATA\_PAGAMENTO, REGRA\_IMPOSTO, VALOR\_FECP

UNION

SELECT

       'FUNDO\_ICMS\_NORMAL'                                       GRUPO\_IMPOSTO,

       APU\.COD\_EMPRESA                                           COD\_EMPRESA,

       REPLACE\(FLX\.GRUPO\_FISCAL,'',''\)                           GRUPO\_FISCAL,

       APU\.COD\_ESTAB                                             COD\_ESTAB,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)                     PERIODO,

       FLX\.COD\_ARRECADACAO                                       COD\_ARRECADACAO,

       FLX\.COD\_RECEITA                                           COD\_RECEITA,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)||FLX\.COD\_RECEITA||1 NUM\_DOC\_ORIGEM,

       NULL                                                      SERIE,

       NULL                                                      CHAVE\_NFE,

       NULL                                                      DATA\_EMISSAO,

       STD\.COD\_ESTADO                                            UF\_FAVORECIDA,

       ROUND\(\(apu\.val\_item\_discrim \* 0\.1\),2\)                     VALOR\_PRINCIPAL,

       TO\_CHAR\(GP\_DT\_GERA\_GUIAS\_CPROC\.calcula\_data\_vencimento\(FLX\.REGRA\_VENCTO,FLX\.DIA\_VENCTO,\(TO\_CHAR\(\(APU\.DAT\_APURACAO \+1\),'MMYYYY'\)\),EST\.IDENT\_ESTADO,EST\.COD\_MUNICIPIO\),'YYYYMMDD'\) DATA\_VENCIMENTO,

       NULL                                                      DATA\_PAGAMENTO,

       FLX\.CONVENIO                                              CONVENIO,

       FLX\.DETALHE\_RECEITA                                       DETALHAMENTO\_RECEITA,

       FLX\.PRODUTO                                               PRODUTO,

       FLX\.INF\_COMPLEMENTAR                                      INF\_COMPLEMENTAR,

       null                                                      VALOR\_FECP,

       'REGRA\_FUNDO\_ICMS\_NORMAL\_7'                                 REGRA\_IMPOSTO

  FROM ITEM\_APURAC\_DISCR APU, ZGP\_VW\_UF\_CD\_RC\_GP\_IMP\_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD

 WHERE APU\.COD\_TIPO\_LIVRO = '108'

   AND APU\.COD\_OPER\_APUR  = '012'

   AND apu\.val\_item\_discrim    > 0

   AND APU\.COD\_EMPRESA    = FLX\.cod\_empresa

   AND APU\.COD\_ESTAB      = FLX\.cod\_estab

   AND UPPER\(FLX\.GRUPO\_IMPOSTO\)  = UPPER\('FUNDO\_ICMS\_NORMAL'\)

   \-\-AND UPPER\(DSC\_ITEM\_APURACAO\)  LIKE '%VLR\_FEEF%'

   AND UPPER\(DSC\_ITEM\_APURACAO\)  LIKE UPPER\('%BENEFICIO INCENTIVO DESENVOLVE 90% \- CONF\. RESOLUCAO 72/2010%'\)

   AND APU\.COD\_EMPRESA    = EST\.COD\_EMPRESA

   AND APU\.COD\_ESTAB      = EST\.COD\_ESTAB

   AND EST\.IDENT\_ESTADO   = STD\.IDENT\_ESTADO

   AND STD\.COD\_ESTADO     = FLX\.UF

   AND FLX\.REGRA\_IMPOSTO  = 'REGRA\_FUNDO\_ICMS\_NORMAL\_7'

UNION

SELECT GRUPO\_IMPOSTO,

       COD\_EMPRESA,

       GRUPO\_FISCAL,

       COD\_ESTAB,

       PERIODO,

       COD\_ARRECADACAO,

       COD\_RECEITA,

       NUM\_DOC\_ORIGEM,

       SERIE,

       CHAVE\_NFE,

       DATA\_EMISSAO,

       UF\_FAVORECIDA,

       SUM\(VALOR\_PRINCIPAL\) VALOR\_PRINCIPAL,

       DATA\_VENCIMENTO,

       DATA\_PAGAMENTO,

       CONVENIO,

       DETALHAMENTO\_RECEITA,

       PRODUTO,

       INF\_COMPLEMENTAR,

       VALOR\_FECP,

       REGRA\_IMPOSTO

FROM \(

SELECT

       'FUNDO\_ICMS\_NORMAL'                                       GRUPO\_IMPOSTO,

       APU\.COD\_EMPRESA                                           COD\_EMPRESA,

       REPLACE\(FLX\.GRUPO\_FISCAL,'',''\)                           GRUPO\_FISCAL,

       APU\.COD\_ESTAB                                             COD\_ESTAB,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)                     PERIODO,

       FLX\.COD\_ARRECADACAO                                       COD\_ARRECADACAO,

       FLX\.COD\_RECEITA                                           COD\_RECEITA,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)||FLX\.COD\_RECEITA||1 NUM\_DOC\_ORIGEM,

       '001'                                                     SERIE,

       NULL                                                      CHAVE\_NFE,

       NULL                                                      DATA\_EMISSAO,

       STD\.COD\_ESTADO                                            UF\_FAVORECIDA,

       apu\.val\_item\_discrim                                      VALOR\_PRINCIPAL,

       TO\_CHAR\(GP\_DT\_GERA\_GUIAS\_CPROC\.calcula\_data\_vencimento\(FLX\.REGRA\_VENCTO,FLX\.DIA\_VENCTO,\(TO\_CHAR\(\(APU\.DAT\_APURACAO \+1\),'MMYYYY'\)\),EST\.IDENT\_ESTADO,EST\.COD\_MUNICIPIO\),'YYYYMMDD'\) DATA\_VENCIMENTO,

       NULL                                                      DATA\_PAGAMENTO,

       FLX\.CONVENIO                                              CONVENIO,

       FLX\.DETALHE\_RECEITA                                       DETALHAMENTO\_RECEITA,

       FLX\.PRODUTO                                               PRODUTO,

       FLX\.INF\_COMPLEMENTAR                                      INF\_COMPLEMENTAR,

       null                                                      VALOR\_FECP,

       'REGRA\_FUNDO\_ICMS\_NORMAL\_8'                                 REGRA\_IMPOSTO

  FROM ITEM\_APURAC\_DISCR APU, ZGP\_VW\_UF\_CD\_RC\_GP\_IMP\_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD

 WHERE APU\.COD\_TIPO\_LIVRO = '108'

   AND APU\.COD\_OPER\_APUR  = '012'

   AND apu\.val\_item\_discrim    > 0

   AND APU\.COD\_EMPRESA    = FLX\.cod\_empresa

   AND APU\.COD\_ESTAB      = FLX\.cod\_estab

   AND UPPER\(FLX\.GRUPO\_IMPOSTO\)  = UPPER\('FUNDO\_ICMS\_NORMAL'\)

   AND UPPER\(DSC\_ITEM\_APURACAO\)  like  '%FECEP 2% \(INCENTIVO B01%'

   AND APU\.COD\_EMPRESA    = EST\.COD\_EMPRESA

   AND APU\.COD\_ESTAB      = EST\.COD\_ESTAB

   AND EST\.IDENT\_ESTADO   = STD\.IDENT\_ESTADO

   AND STD\.COD\_ESTADO     = FLX\.UF

   AND FLX\.REGRA\_IMPOSTO  = 'REGRA\_FUNDO\_ICMS\_NORMAL\_8'\)

   GROUP BY GRUPO\_IMPOSTO, COD\_EMPRESA, GRUPO\_FISCAL, COD\_ESTAB, PERIODO,

COD\_ARRECADACAO, COD\_RECEITA, NUM\_DOC\_ORIGEM, SERIE, CHAVE\_NFE,

UF\_FAVORECIDA, CONVENIO, DETALHAMENTO\_RECEITA, PRODUTO, INF\_COMPLEMENTAR,

DATA\_VENCIMENTO, DATA\_PAGAMENTO, REGRA\_IMPOSTO, VALOR\_FECP

UNION

SELECT GRUPO\_IMPOSTO,

       COD\_EMPRESA,

       GRUPO\_FISCAL,

       COD\_ESTAB,

       PERIODO,

       COD\_ARRECADACAO,

       COD\_RECEITA,

       NUM\_DOC\_ORIGEM,

       SERIE,

       CHAVE\_NFE,

       DATA\_EMISSAO,

       UF\_FAVORECIDA,

       SUM\(VALOR\_PRINCIPAL\) VALOR\_PRINCIPAL,

       DATA\_VENCIMENTO,

       DATA\_PAGAMENTO,

       CONVENIO,

       DETALHAMENTO\_RECEITA,

       PRODUTO,

       INF\_COMPLEMENTAR,

       VALOR\_FECP,

       REGRA\_IMPOSTO

FROM \(

SELECT

       'FUNDO\_ICMS\_NORMAL'                                       GRUPO\_IMPOSTO,

       APU\.COD\_EMPRESA                                           COD\_EMPRESA,

       REPLACE\(FLX\.GRUPO\_FISCAL,'',''\)                           GRUPO\_FISCAL,

       APU\.COD\_ESTAB                                             COD\_ESTAB,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)                     PERIODO,

       FLX\.COD\_ARRECADACAO                                       COD\_ARRECADACAO,

       FLX\.COD\_RECEITA                                           COD\_RECEITA,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)||FLX\.COD\_RECEITA||1 NUM\_DOC\_ORIGEM,

       '002'                                                     SERIE,

       NULL                                                      CHAVE\_NFE,

       NULL                                                      DATA\_EMISSAO,

       STD\.COD\_ESTADO                                            UF\_FAVORECIDA,

       apu\.val\_item\_discrim                                      VALOR\_PRINCIPAL,

       TO\_CHAR\(GP\_DT\_GERA\_GUIAS\_CPROC\.calcula\_data\_vencimento\(FLX\.REGRA\_VENCTO,FLX\.DIA\_VENCTO,\(TO\_CHAR\(\(APU\.DAT\_APURACAO \+1\),'MMYYYY'\)\),EST\.IDENT\_ESTADO,EST\.COD\_MUNICIPIO\),'YYYYMMDD'\) DATA\_VENCIMENTO,

       NULL                                                      DATA\_PAGAMENTO,

       FLX\.CONVENIO                                              CONVENIO,

       FLX\.DETALHE\_RECEITA                                       DETALHAMENTO\_RECEITA,

       FLX\.PRODUTO                                               PRODUTO,

       FLX\.INF\_COMPLEMENTAR                                      INF\_COMPLEMENTAR,

       null                                                      VALOR\_FECP,

       'REGRA\_FUNDO\_ICMS\_NORMAL\_8'                                 REGRA\_IMPOSTO

  FROM ITEM\_APURAC\_DISCR APU, ZGP\_VW\_UF\_CD\_RC\_GP\_IMP\_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD

 WHERE APU\.COD\_TIPO\_LIVRO = '108'

   AND APU\.COD\_OPER\_APUR  = '012'

   AND apu\.val\_item\_discrim    > 0

   AND APU\.COD\_EMPRESA    = FLX\.cod\_empresa

   AND APU\.COD\_ESTAB      = FLX\.cod\_estab

   AND UPPER\(FLX\.GRUPO\_IMPOSTO\)  = UPPER\('FUNDO\_ICMS\_NORMAL'\)

   \-\-AND UPPER\(DSC\_ITEM\_APURACAO\)  LIKE '%FECEP 2%'

   AND UPPER\(DSC\_ITEM\_APURACAO\)  like  '%FECEP 2% \(INCENTIVO B02%'

   AND APU\.COD\_EMPRESA    = EST\.COD\_EMPRESA

   AND APU\.COD\_ESTAB      = EST\.COD\_ESTAB

   AND EST\.IDENT\_ESTADO   = STD\.IDENT\_ESTADO

   AND STD\.COD\_ESTADO     = FLX\.UF

   AND FLX\.REGRA\_IMPOSTO  = 'REGRA\_FUNDO\_ICMS\_NORMAL\_8'\)

   GROUP BY GRUPO\_IMPOSTO, COD\_EMPRESA, GRUPO\_FISCAL, COD\_ESTAB, PERIODO,

COD\_ARRECADACAO, COD\_RECEITA, NUM\_DOC\_ORIGEM, SERIE, CHAVE\_NFE,

UF\_FAVORECIDA, CONVENIO, DETALHAMENTO\_RECEITA, PRODUTO, INF\_COMPLEMENTAR,

DATA\_VENCIMENTO, DATA\_PAGAMENTO, REGRA\_IMPOSTO, VALOR\_FECP

UNION

SELECT

       'FUNDO\_ICMS\_NORMAL'                                       GRUPO\_IMPOSTO,

       APU\.COD\_EMPRESA                                           COD\_EMPRESA,

       REPLACE\(FLX\.GRUPO\_FISCAL,'',''\)                           GRUPO\_FISCAL,

       APU\.COD\_ESTAB                                             COD\_ESTAB,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)                     PERIODO,

       FLX\.COD\_ARRECADACAO                                       COD\_ARRECADACAO,

       FLX\.COD\_RECEITA                                           COD\_RECEITA,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)||FLX\.COD\_RECEITA||1 NUM\_DOC\_ORIGEM,

       NULL                                                      SERIE,

       NULL                                                      CHAVE\_NFE,

       NULL                                                      DATA\_EMISSAO,

       STD\.COD\_ESTADO                                            UF\_FAVORECIDA,

       ROUND\(\(apu\.val\_item\_discrim \* 0\.02\),2\)                    VALOR\_PRINCIPAL,

       TO\_CHAR\(GP\_DT\_GERA\_GUIAS\_CPROC\.calcula\_data\_vencimento\(FLX\.REGRA\_VENCTO,FLX\.DIA\_VENCTO,\(TO\_CHAR\(\(APU\.DAT\_APURACAO \+1\),'MMYYYY'\)\),EST\.IDENT\_ESTADO,EST\.COD\_MUNICIPIO\),'YYYYMMDD'\) DATA\_VENCIMENTO,

       NULL                                                      DATA\_PAGAMENTO,

       FLX\.CONVENIO                                              CONVENIO,

       FLX\.DETALHE\_RECEITA                                       DETALHAMENTO\_RECEITA,

       FLX\.PRODUTO                                               PRODUTO,

       FLX\.INF\_COMPLEMENTAR                                      INF\_COMPLEMENTAR,

       null                                                      VALOR\_FECP,

       'REGRA\_FUNDO\_ICMS\_NORMAL\_9'                                 REGRA\_IMPOSTO

  FROM ITEM\_APURAC\_DISCR APU, ZGP\_VW\_UF\_CD\_RC\_GP\_IMP\_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD

 WHERE APU\.COD\_TIPO\_LIVRO = '108'

   AND APU\.COD\_OPER\_APUR  = '012'

   AND apu\.val\_item\_discrim    > 0

   AND APU\.COD\_EMPRESA    = FLX\.cod\_empresa

   AND APU\.COD\_ESTAB      = FLX\.cod\_estab

   AND UPPER\(FLX\.GRUPO\_IMPOSTO\)  = UPPER\('FUNDO\_ICMS\_NORMAL'\)

   AND UPPER\(DSC\_ITEM\_APURACAO\)  like upper\('%INCENTIVO FISCAL%'\)

   AND APU\.COD\_EMPRESA    = EST\.COD\_EMPRESA

   AND APU\.COD\_ESTAB      = EST\.COD\_ESTAB

   AND EST\.IDENT\_ESTADO   = STD\.IDENT\_ESTADO

   AND STD\.COD\_ESTADO     = FLX\.UF

   AND FLX\.REGRA\_IMPOSTO  = 'REGRA\_FUNDO\_ICMS\_NORMAL\_9'

UNION

SELECT

       'FUNDO\_ICMS\_NORMAL'                                       GRUPO\_IMPOSTO,

       APU\.COD\_EMPRESA                                           COD\_EMPRESA,

       REPLACE\(FLX\.GRUPO\_FISCAL,'',''\)                           GRUPO\_FISCAL,

       APU\.COD\_ESTAB                                             COD\_ESTAB,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)                     PERIODO,

       FLX\.COD\_ARRECADACAO                                       COD\_ARRECADACAO,

       FLX\.COD\_RECEITA                                           COD\_RECEITA,

       TO\_CHAR\(APU\.DAT\_APURACAO, 'YYYYMMDD'\)||FLX\.COD\_RECEITA||1 NUM\_DOC\_ORIGEM,

       NULL                                                      SERIE,

       NULL                                                      CHAVE\_NFE,

       NULL                                                      DATA\_EMISSAO,

       STD\.COD\_ESTADO                                            UF\_FAVORECIDA,

       apu\.val\_item\_discrim                                      VALOR\_PRINCIPAL,

       TO\_CHAR\(GP\_DT\_GERA\_GUIAS\_CPROC\.calcula\_data\_vencimento\(FLX\.REGRA\_VENCTO,FLX\.DIA\_VENCTO,\(TO\_CHAR\(\(APU\.DAT\_APURACAO \+1\),'MMYYYY'\)\),EST\.IDENT\_ESTADO,EST\.COD\_MUNICIPIO\),'YYYYMMDD'\) DATA\_VENCIMENTO,

       NULL                                                      DATA\_PAGAMENTO,

       FLX\.CONVENIO                                              CONVENIO,

       FLX\.DETALHE\_RECEITA                                       DETALHAMENTO\_RECEITA,

       FLX\.PRODUTO                                               PRODUTO,

       FLX\.INF\_COMPLEMENTAR                                      INF\_COMPLEMENTAR,

       null                                                      VALOR\_FECP,

       'REGRA\_FUNDO\_ICMS\_NORMAL\_10'                                 REGRA\_IMPOSTO

  FROM ITEM\_APURAC\_DISCR APU, ZGP\_VW\_UF\_CD\_RC\_GP\_IMP\_CPROC FLX, ESTABELECIMENTO EST, ESTADO STD

 WHERE APU\.COD\_TIPO\_LIVRO = '108'

   AND APU\.COD\_OPER\_APUR  = '006'

   AND apu\.val\_item\_discrim    > 0

   AND APU\.COD\_EMPRESA    = FLX\.cod\_empresa

   AND APU\.COD\_ESTAB      = FLX\.cod\_estab

   AND UPPER\(FLX\.GRUPO\_IMPOSTO\)  = UPPER\('FUNDO\_ICMS\_NORMAL'\)

   AND UPPER\(apu\.dsc\_item\_apuracao\) =  'ART\. 56 DO RICMS/00 FECOEP'

   AND APU\.COD\_EMPRESA    = EST\.COD\_EMPRESA

   AND APU\.COD\_ESTAB      = EST\.COD\_ESTAB

   AND EST\.IDENT\_ESTADO   = STD\.IDENT\_ESTADO

   AND STD\.COD\_ESTADO     = FLX\.UF

   AND FLX\.REGRA\_IMPOSTO  = 'REGRA\_FUNDO\_ICMS\_NORMAL\_10'\) J, GP\_ESTAB\_TEMP\_CPROC TM

 where TM\.EMPRESA                             = J\.COD\_EMPRESA

   and TM\.ESTAB                               = J\.COD\_ESTAB

   and J\.COD\_EMPRESA                          = MCOD\_EMPRESA

   and to\_char\(last\_day\(tm\.dT\_PERIODO\), 'YYYYMMDD'\) = J\.PERIODO

   and upper\(TRIM\(TM\.GRP\_IMP\)\)                = upper\(J\.GRUPO\_IMPOSTO\)

   and J\.UF\_FAVORECIDA                LIKE DECODE\(tm\.uf\_estab, 'TD', '%', tm\.uf\_estab\)

   and J\.COD\_EMPRESA   = v\_cod\_empresa

   and tm\.saida        = v\_tipo\_saida

   and tm\.id\_proc      = v\_mcod\_id;

    REG geraJSON5%rowtype;

        v\_arquivo sys\.utl\_file\.file\_type;

        vs\_arquivo          varchar2\(32767\);

        mLinha              Varchar2\(2000\);

        v\_saida             varchar2\(1\);

    BEGIN

    loga\('GERA\_FUNDO\_ICMS\_NORMAL',FALSE\);

    FOR r\_pallet IN geraJSON5 LOOP

        vPalet\_Count := geraJSON5%ROWCOUNT;

        v\_saida      := r\_pallet\.p\_tipo\_saida;

    END LOOP;

    loga\('Qtde Registros:'||vPalet\_Count,FALSE\);

    IF vPalet\_Count = 0 then

         lib\_proc\.add\_log\('SEM DADOS PARA GERACAO DO ARQUIVO NO PERIODO E GRUPO SELECIONADO',1\);

         lib\_proc\.add\_log\('PERIODO: '||TO\_CHAR\(v\_periodo, 'MM/YYYY'\) ,1\);

         lib\_proc\.add\_log\('GRUPO DE IMPOSTO: '||v\_grupo\_imposto,1\);

     else

        FOR REG in geraJSON5 loop

        vCount := vCount\+1;

        If geraJSON5%ROWCOUNT = 1 Then

        if reg\.p\_tipo\_saida = 1 then

           v\_arquivo := SYS\.utl\_file\.fopen\(VS\_DIRETORIO,mproc\_id||'\_DOOTAX\_'|| REG\.GRUPO\_IMPOSTO||'\_'||to\_char\(trunc\(sysdate\), 'YYYYMMDD'\) ||'\.txt', 'W',32767\);

           SYS\.utl\_file\.put\_line\(v\_arquivo,\('\{"contas\_a\_pagar":\['\)||CHR\(10\)\);

           SYS\.utl\_file\.put\_line\(v\_arquivo, \('\{'\)||CHR\(10\)\);

           vs\_arquivo := '\{';

        elsif reg\.p\_tipo\_saida = 2 then

              LIB\_PROC\.ADD\_TIPO\(MPROC\_ID, 1, mproc\_id||'\_'|| REG\.GRUPO\_IMPOSTO||'\_'||to\_char\(trunc\(sysdate\), 'YYYYMMDD'\) ||'\.txt', 2\);

              vs\_arquivo := \('\{"contas\_a\_pagar":\['\);

              mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

              LIB\_PROC\.add\(mLinha, null, null, 1\);

              vs\_arquivo := \('\{'\);

              mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

              LIB\_PROC\.add\(mLinha, null, null, 1\);

        end if;

        lib\_proc\.add\_log\('  |Geracao arquivo JSON | NOME DO ARQUIVO: ''  |Geracao arquivo JSON | NOME DO ARQUIVO: '||mproc\_id||'\_'|| REG\.GRUPO\_IMPOSTO||'\_'||to\_char\(trunc\(sysdate\), 'YYYYMMDD'\) ||'\.txt   '||'DIRETORIO: '||VS\_DIRETORIO   ,1\);

        lib\_proc\.add\_log\('\{"contas\_a\_pagar":\[',1\);

        lib\_proc\.add\_log\('\{',1\);

        Else

            if reg\.p\_tipo\_saida = 1 then

               SYS\.utl\_file\.put\_line\(v\_arquivo, \('\{'\)||CHR\(10\)\);

               vs\_arquivo := \('\{'\);

            elsif reg\.p\_tipo\_saida = 2 then

                  vs\_arquivo := \('\{'\);

                  mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                  LIB\_PROC\.add\(mLinha, null, null, 1\);

            end if;

            lib\_proc\.add\_log\('\{',1\);

        End If;

        if reg\.p\_tipo\_saida = 1 then

        sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('cod\_empresa'    , reg\.cod\_empresa\)\)||CHR\(10\)\);

        sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('cod\_estab'      , reg\.cod\_estab\)\)||CHR\(10\)\);

        sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('periodo'        , reg\.periodo\)\)||CHR\(10\)\);

        sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('cod\_arrecadacao', reg\.cod\_arrecadacao\)\)||CHR\(10\)\);

        sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('cod\_receita'    , reg\.cod\_receita\)\)||CHR\(10\)\);

        sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('uf\_favorecida'  , reg\.uf\_favorecida\)\)||CHR\(10\)\);

        if reg\.num\_doc\_origem is not null then

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('num\_doc\_origem' , reg\.num\_doc\_origem\)\)||CHR\(10\)\);

        end if;

        IF REG\.SERIE IS NOT NULL THEN

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('serie' , reg\.serie\)\)||CHR\(10\)\);

        END IF;

        IF REG\.DETALHAMENTO\_RECEITA IS NOT NULL THEN

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('det\_receita' , reg\.detalhamento\_receita\)\)||CHR\(10\)\);

        END IF;

        IF REG\.PRODUTO IS NOT NULL THEN

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('cod\_produto' , reg\.produto\)\)||CHR\(10\)\);

        END IF;

        IF REG\.CONVENIO IS NOT NULL THEN

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('convenio' , reg\.convenio\)\)||CHR\(10\)\);

        END IF;

        IF REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' then

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('vlr\_principal' , replace\(trim\(to\_char\(reg\.valor\_principal,'999999990D99'\)\),',','\.'\),true\)\)||CHR\(10\)\);

        ELSE

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('vlr\_principal' , replace\(trim\(to\_char\(reg\.valor\_principal,'999999990D99'\)\),',','\.'\)\)\)||CHR\(10\)\);

        END IF;

        IF REG\.CHAVE\_NFE IS NOT NULL THEN

           sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('chave\_dfe' , reg\.chave\_nfe\)\)||CHR\(10\)\);

        END IF;

        \-\-\-\-\-

        CASE WHEN REG\.VALOR\_FECP IS NOT NULL AND REG\.VALOR\_FECP > 0 THEN

           CASE WHEN REG\.INF\_COMPLEMENTAR IS NOT NULL THEN

              CASE WHEN REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                 SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

              ELSE

                 sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_vencimento' , reg\.data\_vencimento\)\)||CHR\(10\)\);

              END CASE;

              CASE WHEN REG\.DATA\_PAGAMENTO IS NOT NULL THEN

                 sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_vencimento' , reg\.data\_vencimento\)\)||CHR\(10\)\);

              ELSE NULL;

              END CASE;

              sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('vlr\_fecp' , replace\(trim\(to\_char\(reg\.valor\_fecp,'999999990D99'\)\),',','\.'\),true\)\)||CHR\(10\)\);

           ELSE

              CASE WHEN REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                 SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)||CHR\(10\)\);

              ELSE

                 sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_vencimento' , reg\.data\_vencimento\)\)||CHR\(10\)\);

              END CASE;

              CASE WHEN REG\.DATA\_PAGAMENTO IS NOT NULL THEN

                 sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_pagamento' , reg\.data\_pagamento\)\)||CHR\(10\)\);

              ELSE NULL;

              END CASE;

             sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('vlr\_fecp' , replace\(trim\(to\_char\(reg\.valor\_fecp,'999999990D99'\)\),',','\.'\)\)\)||CHR\(10\)\);

             sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('inf\_complementar' , to\_char\(reg\.inf\_complementar\),true\)\)||CHR\(10\)\);

          END CASE;

       ELSE

           CASE WHEN REG\.INF\_COMPLEMENTAR IS NULL THEN

              CASE WHEN REG\.DATA\_PAGAMENTO IS NULL THEN

                 IF REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                    SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

                 ELSE

                    sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_vencimento' , to\_char\(reg\.data\_vencimento\),TRUE\)\)||CHR\(10\)\);

                 END IF;

              ELSE

                 IF REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' then

                    SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

                 ELSE

                    sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_vencimento' , to\_char\(reg\.data\_vencimento\)\)\)||CHR\(10\)\);

                 END IF;

                    sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_pagamento' , to\_char\(reg\.data\_pagamento\),TRUE\)\)||CHR\(10\)\);

              END CASE;

           ELSE

              CASE WHEN REG\.UF\_FAVORECIDA = 'AM'  AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                 SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

              ELSE

                    sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_vencimento' , to\_char\(reg\.data\_vencimento\)\)\)||CHR\(10\)\);

              END CASE;

              CASE WHEN REG\.DATA\_PAGAMENTO IS NOT NULL THEN

                        sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('data\_vencimento' , to\_char\(reg\.data\_pagamento\)\)\)||CHR\(10\)\);

              ELSE NULL;

              END CASE;

                    sys\.utl\_file\.put\_line\(v\_arquivo, \(json\('inf\_complementar' , to\_char\(reg\.inf\_complementar\),TRUE\)\)||CHR\(10\)\);

           END CASE;

       END CASE;

       \-\- SERVIDOR LOCAL

        elsif reg\.p\_tipo\_saida = 2 then

        vs\_arquivo := \(json\('cod\_empresa'    , reg\.cod\_empresa\)\);

        mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

        LIB\_PROC\.add\(mLinha, null, null, 1\);

        vs\_arquivo := \(json\('cod\_estab'      , reg\.cod\_estab\)\);

        mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

        LIB\_PROC\.add\(mLinha, null, null, 1\);

        IF REG\.REGRA\_IMPOSTO = 'REGRA\_DIFAL\_2' THEN

           vs\_arquivo := \(json\('periodo'        , reg\.data\_emissao\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        ELSE

           vs\_arquivo := \(json\('periodo'        , reg\.periodo\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        END IF;

        vs\_arquivo := \(json\('cod\_arrecadacao', reg\.cod\_arrecadacao\)\);

        mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

        LIB\_PROC\.add\(mLinha, null, null, 1\);

        vs\_arquivo := \(json\('cod\_receita'    , reg\.cod\_receita\)\);

        mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

        LIB\_PROC\.add\(mLinha, null, null, 1\);

        vs\_arquivo := \(json\('uf\_favorecida'  , reg\.uf\_favorecida\)\);

        mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

        LIB\_PROC\.add\(mLinha, null, null, 1\);

        if reg\.num\_doc\_origem is not null then

           vs\_arquivo := \(json\('num\_doc\_origem' , reg\.num\_doc\_origem\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        end if;

        IF REG\.SERIE IS NOT NULL THEN

           vs\_arquivo := \(json\('serie'  , reg\.serie\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        END IF;

        IF REG\.DETALHAMENTO\_RECEITA IS NOT NULL THEN

           vs\_arquivo := \(json\('det\_receita'  , reg\.detalhamento\_receita\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        END IF;

        IF REG\.PRODUTO IS NOT NULL THEN

           vs\_arquivo := \(json\('cod\_produto'  , reg\.produto\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        END IF;

        IF REG\.CONVENIO IS NOT NULL THEN

           vs\_arquivo := \(json\('convenio'  , reg\.convenio\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        END IF;

        IF REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' then

           vs\_arquivo := \(json\('vlr\_principal'  , replace\(trim\(to\_char\(reg\.valor\_principal,'999999990D99'\)\),',','\.'\),true\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        ELSE

           vs\_arquivo := \(json\('vlr\_principal'  , replace\(trim\(to\_char\(reg\.valor\_principal,'999999990D99'\)\),',','\.'\)\)\);

           mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

           LIB\_PROC\.add\(mLinha, null, null, 1\);

        END IF;

        IF REG\.CHAVE\_NFE IS NOT NULL THEN

              vs\_arquivo := \(json\('chave\_dfe'  , reg\.chave\_nfe\)\);

              mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

              LIB\_PROC\.add\(mLinha, null, null, 1\);

        END IF;

        CASE WHEN REG\.VALOR\_FECP IS NOT NULL AND REG\.VALOR\_FECP > 0 THEN

           CASE WHEN REG\.INF\_COMPLEMENTAR IS NOT NULL THEN

              CASE WHEN REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                 SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

              ELSE

                 vs\_arquivo := \(json\('data\_vencimento'  , to\_char\(reg\.data\_vencimento\)\)\);

                 mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                 LIB\_PROC\.add\(mLinha, null, null, 1\);

              END CASE;

              CASE WHEN REG\.DATA\_PAGAMENTO IS NOT NULL THEN

                 vs\_arquivo := \(json\('data\_vencimento'  , to\_char\(reg\.data\_pagamento\)\)\);

                 mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                 LIB\_PROC\.add\(mLinha, null, null, 1\);

              ELSE NULL;

              END CASE;

              vs\_arquivo := \(json\('vlr\_fecp'  , replace\(trim\(to\_char\(reg\.valor\_fecp,'999999990D99'\)\),',','\.'\),true\)\);

              mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

              LIB\_PROC\.add\(mLinha, null, null, 1\);

           ELSE

              CASE WHEN REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                 SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

              ELSE

                 vs\_arquivo := \(json\('data\_vencimento'  , to\_char\(reg\.data\_vencimento\)\)\);

                 mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                 LIB\_PROC\.add\(mLinha, null, null, 1\);

              END CASE;

              CASE WHEN REG\.DATA\_PAGAMENTO IS NOT NULL THEN

                 vs\_arquivo := \(json\('data\_pagamento'  , to\_char\(reg\.data\_pagamento\)\)\);

                 mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                 LIB\_PROC\.add\(mLinha, null, null, 1\);

              ELSE NULL;

              END CASE;

             vs\_arquivo := \(json\('vlr\_fecp'  , replace\(trim\(to\_char\(reg\.valor\_fecp,'999999990D99'\)\),',','\.'\)\)\);

             mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

             LIB\_PROC\.add\(mLinha, null, null, 1\);

             vs\_arquivo := \(json\('inf\_complementar'  , to\_char\(reg\.inf\_complementar\),true\)\);

             mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

             LIB\_PROC\.add\(mLinha, null, null, 1\);

          END CASE;

       ELSE

           CASE WHEN REG\.INF\_COMPLEMENTAR IS NULL THEN

              CASE WHEN REG\.DATA\_PAGAMENTO IS NULL THEN

                 CASE WHEN REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                    SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

                 ELSE

                    vs\_arquivo := \(json\('data\_vencimento'  , to\_char\(reg\.data\_vencimento\),TRUE\)\);

                    mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                    LIB\_PROC\.add\(mLinha, null, null, 1\);

                 END CASE;

              ELSE

                 CASE WHEN REG\.UF\_FAVORECIDA = 'AM' AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' then

                    SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

                 ELSE

                    vs\_arquivo := \(json\('data\_vencimento'  , to\_char\(reg\.data\_vencimento\)\)\);

                    mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                    LIB\_PROC\.add\(mLinha, null, null, 1\);

                 END CASE;

                    vs\_arquivo := \(json\('data\_pagamento'  , to\_char\(reg\.data\_pagamento\),TRUE\)\);

                    mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                    LIB\_PROC\.add\(mLinha, null, null, 1\);

              END CASE;

           ELSE

              CASE WHEN REG\.UF\_FAVORECIDA = 'AM'  AND REG\.GRUPO\_IMPOSTO = 'ICMS\_NORMAL' THEN

                 SYS\.DBMS\_OUTPUT\.PUT\_LINE\(json\('data\_vencimento', to\_char\(reg\.data\_vencimento\)\)\);

              ELSE

                    vs\_arquivo := \(json\('data\_vencimento'  , to\_char\(reg\.data\_vencimento\)\)\);

                    mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                    LIB\_PROC\.add\(mLinha, null, null, 1\);

              END CASE;

              CASE WHEN REG\.DATA\_PAGAMENTO IS NOT NULL THEN

                    vs\_arquivo := \(json\('data\_vencimento'  , to\_char\(reg\.data\_pagamento\)\)\);

                    mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                    LIB\_PROC\.add\(mLinha, null, null, 1\);

              ELSE NULL;

              END CASE;

                    vs\_arquivo := \(json\('inf\_complementar'  , to\_char\(reg\.inf\_complementar\),TRUE\)\);

                    mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                    LIB\_PROC\.add\(mLinha, null, null, 1\);

            END CASE;

       END CASE;

        end if;

        lib\_proc\.add\_log\(json\('cod\_empresa'    , reg\.cod\_empresa\),1\);

        lib\_proc\.add\_log\(json\('cod\_estab'      , reg\.cod\_estab\),1\);

        lib\_proc\.add\_log\(json\('periodo'        , reg\.periodo\),1\);

        lib\_proc\.add\_log\(json\('cod\_arrecadacao', reg\.cod\_arrecadacao\),1\);

        lib\_proc\.add\_log\(json\('cod\_receita'    , reg\.cod\_receita\),1\);

        lib\_proc\.add\_log\(json\('uf\_favorecida'  , reg\.uf\_favorecida\),1\);

        if reg\.num\_doc\_origem is not null then

           lib\_proc\.add\_log\(json\('num\_doc\_origem' , reg\.num\_doc\_origem\),1\);

        end if;

        if reg\.serie is not null then

           lib\_proc\.add\_log\(json\('serie' , reg\.serie\),1\);

        end if;

        if reg\.data\_vencimento is not null then

           lib\_proc\.add\_log\(json\('data\_vencimento' , reg\.data\_vencimento\),1\);

        end if;

        if reg\.data\_pagamento is not null then

           lib\_proc\.add\_log\(json\('data\_pagamento' , reg\.data\_pagamento\),1\);

        end if;

        if reg\.convenio is not null then

           lib\_proc\.add\_log\(json\('convenio' , reg\.convenio\),1\);

        end if;

        if reg\.produto is not null then

           lib\_proc\.add\_log\(json\('produto' , reg\.produto\),1\);

        end if;

        if reg\.detalhamento\_receita is not null then

           lib\_proc\.add\_log\(json\('det\_receita' , reg\.detalhamento\_receita\),1\);

        end if;

        if reg\.inf\_complementar is not null then

           lib\_proc\.add\_log\(json\('inf\_complementar' , reg\.inf\_complementar\),1\);

        end if;

        if reg\.chave\_nfe is null then

           if reg\.valor\_fecp is not null then

           lib\_proc\.add\_log\(json\('vlr\_principal'  , reg\.valor\_principal\),1\);

           lib\_proc\.add\_log\(json\('valor\_fecp' , reg\.valor\_fecp,true\),1\);

           else

           lib\_proc\.add\_log\(json\('vlr\_principal'  , reg\.valor\_principal,true\),1\);

           end if;

        else

           if reg\.valor\_fecp is not null then

           lib\_proc\.add\_log\(json\('vlr\_principal'  , reg\.valor\_principal\),1\);

           lib\_proc\.add\_log\(json\('valor\_fecp' , reg\.valor\_fecp\),1\);

           else

           lib\_proc\.add\_log\(json\('vlr\_principal'  , reg\.valor\_principal,true\),1\);

           end if;

           lib\_proc\.add\_log\(json\('vlr\_principal'  , reg\.valor\_principal\),1\);

           lib\_proc\.add\_log\(json\('chave\_dfe' , reg\.chave\_nfe,true\),1\);

        end if;

           if reg\.p\_tipo\_saida = 1 then

              \-\-Se houver mais de 1 bloco no json insere virgula ao final do bloco, exceto no ultimo registro\.

              if vCount < vPalet\_Count then

                 sys\.utl\_file\.put\_line\(v\_arquivo, \('\},'\)\);

              else

                 sys\.utl\_file\.put\_line\(v\_arquivo, \('\}'\)\);

              end if;

           elsif reg\.p\_tipo\_saida = 2 then

                 \-\-Se houver mais de 1 bloco no json insere virgula ao final do bloco, exceto no ultimo registro\.

                 if vCount < vPalet\_Count then

                    vs\_arquivo := \('\},'\);

                    mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                    LIB\_PROC\.add\(mLinha, null, null, 1\);

                    lib\_proc\.add\_log\('\},',1\);

                 else

                     vs\_arquivo := \('\}'\);

                     mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

                     LIB\_PROC\.add\(mLinha, null, null, 1\);

                     lib\_proc\.add\_log\('\}',1\);

                 end if;

            end if;

         insert into GP\_LOGS\_JSON\_DT\_CPROC  values \(mproc\_id,

                                                       musuario,

                                                       TO\_CHAR\(SYSDATE, 'DD/MM/YYYY HH24:MI:SS'\),

                                                       reg\.cod\_empresa,

                                                       reg\.cod\_estab,

                                                       reg\.periodo,

                                                       reg\.grupo\_imposto,

                                                       reg\.cod\_arrecadacao,

                                                       reg\.cod\_receita,

                                                       reg\.uf\_favorecida,

                                                       reg\.num\_doc\_origem,

                                                       reg\.serie,

                                                       reg\.chave\_nfe,

                                                       reg\.valor\_principal,

                                                       reg\.valor\_fecp,

                                                       reg\.data\_vencimento,

                                                       reg\.data\_pagamento,

                                                       reg\.inf\_complementar,

                                                       reg\.detalhamento\_receita,

                                                       reg\.convenio,

                                                       reg\.produto\);

        \-\-commit;

        end loop;

        if v\_saida = 1 then

           sys\.utl\_file\.put\_line\(v\_arquivo, \('\]\}'||CHR\(13\)\)\);

        elsif v\_saida = 2 then

              vs\_arquivo := \('\]\}'\);

              mLinha := LIB\_STR\.w\('', vs\_arquivo, 1\);

              LIB\_PROC\.add\(mLinha, null, null, 1\);

        end if;

        lib\_proc\.add\_log\('\]\}',1\);

        sys\.utl\_file\.fclose\(v\_arquivo\);

           end if;

           delete from GP\_ESTAB\_TEMP\_CPROC where id\_proc = mproc\_id;

           COMMIT;

       END;

END GERA\_FUNDO\_ICMS\_NORMAL;

  FUNCTION fn\_ret\_last\_ddl\_time

  RETURN VARCHAR2 IS

     VS\_LAST\_DDL\_TIME VARCHAR2\(30\);

  BEGIN

     SELECT TO\_CHAR\(MAX\(AO\.LAST\_DDL\_TIME\),'DD/MM/YYYY HH24:MI'\)

       INTO VS\_LAST\_DDL\_TIME

       FROM ALL\_OBJECTS AO

      WHERE OBJECT\_NAME = $$PLSQL\_UNIT;

  RETURN VS\_LAST\_DDL\_TIME;

  END;

  FUNCTION executar\(p\_periodo        date,

                    p\_grp\_imp       varchar2,

                    p\_uf\_estab      varchar2,

                    \-\-p\_saida         varchar2,

                    p\_cod\_estab      Lib\_Proc\.Vartab

                    \) return integer is

  cont\_estab NUMBER;

    V\_MODULO\_PRT   VARCHAR2\(100\);

BEGIN

    \-\- Cria Processo / Procedure

    \-\-mproc\_id := LIB\_PROC\.new\('GP\_DT\_GERA\_GUIAS\_CPROC', 47, 150\);

    mproc\_id := LIB\_PROC\.new\($$PLSQL\_UNIT, 47, 150\);

    LIB\_PROC\.add\_log\('V:'||V\_VERSAO||'\-'||fn\_ret\_last\_ddl\_time,1\);

    commit;

    mcod\_empresa := LIB\_PARAMETROS\.RECUPERAR\('EMPRESA'\);

    mcod\_estab   := LIB\_PARAMETROS\.recuperar\('ESTABELECIMENTO'\);

    musuario     := LIB\_PARAMETROS\.Recuperar\('USUARIO'\);

    loga\('Usu rio: '||musuario,false\);

    LIB\_PARAMETROS\.Salvar\('USUARIO',''\);

     SELECT MAX\(A\.VALOR\)

        INTO V\_MODULO\_PRT

        FROM FPAR\_PARAM\_DET  A,

             FPAR\_PARAMETROS B

       WHERE A\.ID\_PARAMETRO = B\.ID\_PARAMETROS

         AND B\.NOME\_FRAMEWORK = 'HNK\_ZFI412\_ARQUIVO\_CPAR'

         AND B\.DESCRICAO = 'DOOTAX'

         AND A\.NOME\_PARAM = 'MOD\_PRT\_DIR\_SERV';

        IF V\_MODULO\_PRT IS NULL THEN

          LOGA\('ATENCAO: MODULO NAO CADASTRADO NO PERFIL DOOTAX DOS PARAMETROS GERAIS GERACAO ARQUIVO', FALSE\);

          COMMIT;

        END IF;

  SELECT max\(DIRECTORY\_NAME\)

      into VS\_DIRETORIO

    FROM PRT\_DIRETORIOS\_SERVIDOR

   WHERE COD\_MODULO = V\_MODULO\_PRT;\-\-'JOB SERVIDOR';

\-\-   VS\_DIRETORIO := 'DOOTAX\_DIR';

   if VS\_DIRETORIO is null then

      loga\('ATENCAO: DIRETORIO NAO CADASTRADO',false\);

      commit;

   end if;

   \-\-FOR cont\_estab IN 1 \.\. p\_cod\_estab\.COUNT LOOP

   cont\_estab := 0;

   WHILE P\_COD\_ESTAB\.COUNT > cont\_estab

   LOOP

      cont\_estab := cont\_estab \+ 1;

      insert into GP\_ESTAB\_TEMP\_CPROC  values \(mproc\_id, mcod\_empresa, p\_cod\_estab\(cont\_estab\),p\_periodo,p\_grp\_imp,null,p\_uf\_estab,'1'\);

      \-\-commit;

   end loop;

   commit;

         begin

              IF UPPER\(p\_grp\_imp\) =  'ICMS\_NORMAL' THEN

              gera\_icms\_normal\(mproc\_id,mcod\_empresa, mcod\_estab, p\_periodo, p\_grp\_imp, p\_uf\_estab, '1'\);

              ELSIF UPPER\(p\_grp\_imp\) =  'DIFAL' THEN

              gera\_difal\(mproc\_id,mcod\_empresa, mcod\_estab, p\_periodo, p\_grp\_imp, p\_uf\_estab, '1'\);

              ELSIF UPPER\(p\_grp\_imp\) =  'ICMS\_ANTECIPADO' THEN

              gera\_icms\_antecipado\(mproc\_id,mcod\_empresa, mcod\_estab, p\_periodo, p\_grp\_imp, p\_uf\_estab, '1'\);

              ELSIF UPPER\(p\_grp\_imp\) =  'ICMS\_INCENTIVADO' THEN

              gera\_icms\_incentivado\(mproc\_id,mcod\_empresa, mcod\_estab, p\_periodo, p\_grp\_imp, p\_uf\_estab, '1'\);

              ELSIF UPPER\(p\_grp\_imp\) =  'FUNDO\_ICMS\_NORMAL' THEN

              gera\_fundo\_icms\_normal\(mproc\_id,mcod\_empresa, mcod\_estab, p\_periodo, p\_grp\_imp, p\_uf\_estab, '1'\);

              END IF;

         END;

# <a id="_Toc190696644"></a>10\. Campos Necessários para Requisição de Envio

Abaixo estão os campos obrigatórios e opcionais exigidos para a integração, com seus respectivos formatos e origens na base de dados da Tax One\.

 

# <a id="_Toc190696645"></a>10\.1 De/PARA integração DOOTAX – Campos para Requisição de Envio:  

__Campos DOOTAX__ 

__Dados do campo__ 

__Formato __ 

__Obrig\.__ 

__DE/PARA TAX ONE__ 

cod\_empresa 

 

Código da empresa conforme informado no cadastro da empresa no Dootax 

Alfanumérico 

 

Sim 

- SAFX 07\-Arquivo de Notas Fiscais 
- SAFX08 \-Itens Notas Fiscais Mercadorias e Produtos 
- SAFX 09\-Itens Notas Fiscais de Serviços 
- Tabelas de Apurações 

cod\_estab 

 

Código do estabelecimento conforme informado no cadastro da empresa no Dootax 

Alfanumérico 

 

- SAFX 07\-Arquivo de Notas Fiscais 
- SAFX08 \-Itens Notas Fiscais Mercadorias e Produtos 
- SAFX 09\-Itens Notas Fiscais de Serviços 
- Tabelas de Apurações 

periodo 

 

Data da ocorrência ou do encerramento do período 

Data 

 

 

Sim 

- SAFX07 \- Arquivo de Notas Fiscais 
- SAFX08 \- Itens Notas Fiscais Mercadorias e Produtos 
- SAFX09 \- Itens Notas Fiscais de Serviços 
- Tabelas de Apurações  
- SAFX 163 \-Guia de Recolhimento de Tributos Estaduais – GNRE\. 
- Tabela das Guias de Recolhimento da Apuração\. 

cod\_arrecadacao 

 

Tipo de documento utilizado na arrecadação, conforme cadastro no Dootax\. \(ex\.: DARF; GNRE\) 

Número 

Sim 

- SAFX 163 \-Guia de Recolhimento de Tributos Estaduais – GNRE\. 
- Tabela das Guias de Recolhimento da Apuração do ICMS 

cod\_receita 

Código da receita que está sendo paga, de acordo com o tipo de documento de arrecadação\. 

Número 

Sim 

- SAFX 163 \-Guia de Recolhimento de Tributos Estaduais – GNRE\. 
- Tabela das Guias de Recolhimento da Apuração do ICMS 

det\_receita 

 

Código do detalhamento da receita\. 

Alfanumérico 

Sim 

- SAFX 163 \-Guia de Recolhimento de Tributos Estaduais – GNRE\. 
- Tabela das Guias de Recolhimento da Apuração\. 

num\_doc\_origem 

Número do documento que deu origem ao pagamento\. 

Número 

 

- SAFX 07\-Arquivo de Notas Fiscais 
- SAFX08 \-Itens Notas Fiscais Mercadorias e Produtos 
- SAFX 09\-Itens Notas Fiscais de Serviços 
- Tabelas de Apurações 

Serie 

Série do documento 

Alfanumérico 

 

- SAFX 07\-Arquivo de Notas Fiscais 
- SAFX08 \-Itens Notas Fiscais Mercadorias e Produtos 
- SAFX 09\-Itens Notas Fiscais de Serviços 

uf\_favorecida 

 

Sigla da UF favorecida\. 

Texto 

Sim 

- SAFX 07\-Arquivo de Notas Fiscais 
- SAFX08 \-Itens Notas Fiscais Mercadorias e Produtos 

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

 

- SAFX 163 \-Guia de Recolhimento de Tributos Estaduais – GNRE\. 
- Tabela das Guias de Recolhimento da Apuração\. 

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

 

 

# <a id="_Toc190696646"></a>11\. Melhorias e Diferenciais na Jornada do Usuário

Para otimizar a experiência dos usuários, recomendamos implementar os seguintes itens:

# <a id="_Toc190696647"></a>11\.1\. Controle de Versão

- Registrar a versão da API e manter um histórico de atualizações\.
- Exemplo: Versão 1\.0 \- Lançamento inicial \- Versão 1\.1 \- Inclusão do campo "cod\_mun\_favorecido"

# <a id="_Toc190696648"></a>11\.2\. Segurança na Integração

- Utilizar __tokens de autenticação__ para garantir acesso seguro\.
- Aplicar __validação de dados__ para evitar ataques como SQL Injection\.
- Restringir acessos via __IP autorizado__ ou credenciais personalizadas\.

# <a id="_Toc190696649"></a>11\.3\. Detalhamento de Requisições e Respostas

- Indicar os métodos HTTP utilizados \(POST, GET, etc\.\)\.
- Exemplificar as respostas da API para sucesso e erro\.

# <a id="_Toc190696650"></a>11\.4\. Monitoramento e Suporte

- Possibilitar acompanhamento dos envios através de logs e dashboards\.

# <a id="_Toc190696651"></a>12\. Conclusão

A integração da API do Tax One com o Dootax oferece um fluxo automatizado e eficiente para a importação e processamento de guias de pagamento de tributos\. A padronização dos campos de requisição e a implementação de validações estruturadas garantem maior confiabilidade e segurança na transmissão dos dados, reduzindo erros operacionais\.

A funcionalidade __Executar__ desempenha um papel essencial ao permitir a automação do processamento das guias importadas, reduzindo a necessidade de intervenção manual e agilizando o cumprimento das obrigações fiscais\. 

Além disso, as melhorias sugeridas, como feedback em tempo real, logs detalhados e flexibilidade no envio de dados, aprimoram a experiência do usuário, tornando o sistema mais intuitivo e transparente\.

Com essas otimizações, espera\-se um ganho expressivo em produtividade, segurança e conformidade fiscal, proporcionando uma solução robusta e alinhada às necessidades das empresas\.

= = = = = =

