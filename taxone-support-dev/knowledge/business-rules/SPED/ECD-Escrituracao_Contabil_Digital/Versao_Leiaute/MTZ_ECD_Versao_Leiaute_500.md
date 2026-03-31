# MTZ_ECD_Versao_Leiaute_500

- **Fonte:** MTZ_ECD_Versao_Leiaute_500.docx
- **Modificado:** 2020-12-17
- **Tamanho:** 105 KB

---

THOMSON REUTERS

ECD

Atualização da Geração do Arquivo para atender ao Leiaute 5\.00

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS\-8216

Lara Aline

Atualização das Informações do arquivo da ECD para atender à versão 5\.00 do Leiaute da ECD\.

MFS\-8620

Lara Aline

Atualização das Informações do arquivo da ECD para atender à versão 5\.00 do Leiaute da ECD\.

CH21396/2016

Lara Aline

Ajuste na geração do campo 02 \- COD\_CTA\_RES do I015 para os livros auxiliares \(A e Z\)\.

MFS\-9689

Lara Aline

Atualização das Informações do arquivo da ECD para atender à versão 5\.00 do Leiaute da ECD\. De acordo com as orientação do PVA versão 4\.0\.0\.

MFS9809/

CH2989/2017

Andrea Rocha

Atualização das informações do bloco K

MFS10727

Lara Aline

Ajuste na regra do Campo 02 – COD\_PLAN\_REF do Registro I051\.

MFS\-10358

Lara Aline

Atualização das Informações do arquivo da ECD para atender o Bloco K na versão 5\.00 do Leiaute da ECD\.

CH8476\_2017 \(MFS\-10940\)

Julyana Perrucini

Alteração da regra de preenchimento do campo 03 do Registro J930\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral__

Este documento tem como objetivo demonstrar as alterações da versão 5\.00 do leiaute da ECD em relação à versão 4\.00\. Este novo leiaute será obrigatório a partir do ano\-calendário 2016\.

Todos os registros deverão ser mantidos conforme layout anterior, incluindo as alterações e criação dos novos registros que estarão definidos nas regras de negócios descritas neste documento, documento de requisito e documentos matriz relacionados na alteração da versão\.

MFS\-8216

__Alterações Registro 0000__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN0000\-14

__Registro 0000 – Campo 14 – IND\_FIN\_ESC__

Indicador de Finalidade de Escrituração

- Preencher com ‘0’ se na tela de geração o indicador de finalidade de escrituração estiver selecionado: ‘0 – Original’;
- Preencher com ‘1’ se na tela de geração o indicador de finalidade de escrituração estiver selecionado: ‘1 – Substituta’

Campo de preenchimento obrigatório\. 

MFS\-8216

RN0000\-16

__\[EXCLUÌDO\] Registro 0000 – Campo 16 – NIRE\_SUBST\.__

Este campo foi excluído a partir do layout da versão 5\.00\. 

Importante: Deverá ser reposicionada a numeração dos campos posteriores\.

MFS\-8216

RN0000\-20

__Registro 0000 – Campo 20 – IND\_ESC\_CONS__

Este campo existe a partir da versão 5\.00\. Inicialmente será gerado com conteúdo fixo: “N”

Será gerado conforme parâmetro “Escriturações Contábeis Consolidadas” da tela de Dados Iniciais \(menu Parâmetros\):

Se o referido parâmetro estiver desmarcado, será gerado com conteúdo “N”\.

Se o parâmetro estiver selecionado, será gerado com conteúdo “S”\.

MFS\-8216

MFS\-10358

__Alterações Registro I010__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNI010\-03

__Registro I010 – Campo 03 – COD\_VER\_LC__

Para a versão 5\.00, será gerado com o código “5\.00”\. 

MFS\-8216

__Alterações Registro I015__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNI015\-02

__Registro I015 – Campo 02 – COD\_CTA\_RES__

Para os livros auxiliares ‘A’ ou ‘Z’ nesse campo será gerada a informação da conta sintética \(campo COD\_CONTA\_SINT da SAFX2002\) associada à conta analítica movimentada encontrada, nesse caso será gerada sempre a primeira conta sintética encontrada\. Exemplo:

__Conta__

__Tipo__

__Conta Pai__

__Nível__

1\.1\.1

S

1

1\.1\.1\.01

S

1\.1\.1

2

__1\.1\.1\.01\.0001__

__A__

__1\.1\.1\.01__

__3__

1\.1\.1\.01\.0001\.01

A

1\.1\.1\.01\.0001

4

\-\-\-\-\-\-\\\\\-\-\-\-\-\-

Livros Auxiliares ao Diário

1\.1\.1\.01\.0001

__Auxiliar__

Como deve ser gerado:

__I015 \- 1\.1\.1\.01__

I050 \- 1\.1\.1

I050 \- 1\.1\.1\.01

I050 \- 1\.1\.1\.01\.0001

No caso do exemplo acima para a conta analítica 1\.1\.1\.01\.0001 está associada a conta sintética 1\.1\.1\.01, que será gerado no registro I015 para os livros ‘A’ ou ‘Z’\.

Obs\.: Para os outros Livros a geração desse campo continua conforme o padrão, ou seja, gerando a conta analítica movimentada encontrada\.

CH21396\_2016

__Alterações Registro I051__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNI051\-02

__Registro I051 – Campo 02 – COD\_PLAN\_REF__

A partir da versão 5\.00 nesse campo foi incluído um novo Código da Entidade “10\- Financeiras – Lucro Presumido” e foi alterado o tamanho do campo para 2 posições\.

A partir da versão 5\.00 este registro será gerado apenas quando o Código da Entidade for igual a “1 \- PJ em Geral”, ”2 \- PJ em Geral \- Lucro Presumido”, “3 – Financeiras”, “4 – Seguradoras”, “5 \- Imunes e Isentas em Geral”, “6 \- Financeiras \- Imunes e Isentas”, “7 \- Seguradoras \- Imunes e Isentas”, “8 \- Entidades Fechadas de Previdência Complementar”, “9 \- Partidos Políticos”\. ou “10\- Financeiras – Lucro Presumido/ Secretaria da Receita Federal”\.

Caso o usuário não tenha realizado parametrização para uma destas entidades indicadas acima em Dados Iniciais e/ou Plano de Contas Referencial X Plano de Contas Empresa e esteja gerando a versão 5\.00 do Leiaute, será demonstrada uma mensagem no log: “A partir da versão 5\.00 do leiaute não serão válidas as Contas Referenciais de entidade 00\-SUSEP ou 20\- Banco Central do Brasil \(COSIF\)”\.

MFS8620

MFS10727

__Alterações Registro I053__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNI053\-04

__Registro I053 – Campo 04 – NAT\_SUB\_CNT__

Será gerado com o conteúdo do campo Natureza da Subconta da tela de Subconta Correlata\.

Não deverão ser considerados os códigos de Natureza da Subconta que estejam fora do período de validade na TACES90\. 

MFS\-8216

__Alterações Registro J800__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNJ800\-02

__Registro J800 – Campo 02 – TIPO\_DOC__

Este campo existe a partir da versão 5\.00, porém ele deve ser gerado para todas as versões\.

Será gerado o código conforme opção selecionada pelo usuário no campo “Tipo de documento” na Aba Demonstrações Contábeis dos Dados Iniciais \(menu Parâmetros\) \- quadro ‘Outras Informações das Demonstrações Contábeis \(Balanço Patrimonial e Demonstração de Resultado\)’, conforme opções a seguir:

001: Demonstração do Resultado Abrangente do Período 

002: Demonstração dos Fluxos de Caixa 

003: Demonstração do Valor Adicionado 

010: Notas Explicativas 

011: Relatório da Administração 

012: Parecer dos Auditores 

099: Outros

MFS\-8620

MFS\-9689

RNJ800\-03

__Registro J800 – Campo 03 – DESC\_RTF__

Este campo existe a partir da versão 5\.00, porém ele deve ser gerado para todas as versões\.

Será gerado com o conteúdo do campo Descrição \(\.rtf\) da tela de Dados iniciais/Aba Demonstrações Contábeis \- Quadro \(Outras Informações das Demonstrações Contábeis \(Balanço Patrimonial e Demonstração de Resultado\)\)\.

MFS\-8620

MFS\-9689

RNJ800\-04

__Registro J800 – Campo 04 – HASH\_RTF__

Este campo existe a partir da versão 5\.00, porém ele deve ser gerado para todas as versões\.

Será gerado sem informação \(em branco\)\. Pois essa informação será gerada pelo próprio PVA no momento da validação do arquivo\.

MFS\-8620

MFS\-9689

__Novo Registro J801 \- Termo de Verificação para Fins de Substituição da ECD__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNJ801\-00

__Registro J801 – Regra Geral__

Este registro existe a partir da versão 5\.00, porém ele deve ser gerado para todas as versões\.

__Origem das informações__: Tela de Dados Iniciais – Aba Demonstrações Contábeis \(Módulo ECD / Menu Parâmetros > Dados Iniciais\)

__Regra de Seleção__: Este registro será gerado sempre que no quadro ‘Termo de Verificação para Fins de Substituição da ECD \(Balanço Patrimonial e Demonstração de Resultado\)’ na aba Demonstrações Contábeis da tela de Dados Iniciais existir informação de um arquivo RTF\.

__Campo\-chave__: ARQ\_RTF

__Registro pai / Nível hierárquico__: J005 / Nível 3

__Ocorrência__: Um por arquivo

MFS\-8620

MFS\-9689

RNJ801\-01

__Registro J801 – Campo 01 – REG__

Informação fixa “J801”\.

MFS\-8620

RNJ801\-02

__Registro J801 – Campo 02 – TIPO\_DOC__

Nesse registro será gerado o tipo de documento que no caso será 001: Termo de Substituição da ECD\.

Valor fixo: 001\.

O quadro ‘Termo de Verificação para Fins de Substituição da ECD \(Balanço Patrimonial e Demonstração de Resultado\)’ foi criado justamente para o usuário informar o arquivo de formato RTF que corresponde apenas ao tipo de documento: Termo de Substituição da ECD\. 

MFS\-8620

RNJ801\-03

__Registro J801 – Campo 03 – DESC\_RTF__

Será gerado com o conteúdo do campo Descrição \(\.rtf\) da tela de Dados iniciais/Aba Demonstrações Contábeis \- Quadro \(Termo de Verificação para Fins de Substituição da ECD \(Balanço Patrimonial e Demonstração de Resultado\)\)\.

MFS\-8620

RNJ801\-04

__Registro J801 – Campo 04 – HASH\_RTF__

Será gerado sem informação \(em branco\)\. Pois essa informação será gerada pelo próprio PVA no momento da validação do arquivo\.

MFS\-8620

RNJ801\-05

__Registro J801 – Campo 05 – ARQ\_RTF__

Será gerada uma sequência de bytes que representem um único arquivo no formato RTF \(Rich Text Format\)\.

MFS\-8620

RNJ801\-06

__Registro J801 – Campo 06 – IND\_FIM\_RTF__

Informação fixa “J801FIM”\.

MFS\-8620

__Alterações Registro J930__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNJ930\-03

__Registro J930 – Campo 03 – IDENT\_CPF\_CNPJ__

Consultar DE\-PARA: DE\-PARA \_SPED Contábil\_Conf\.IN RFB nº 926\.09\.xls\.

__Tratamento:__

Se o campo NUM\_CPF da tabela RESP\_INFORMACAO não estiver preenchido, será verificada a existência do CNPJ no campo NUM\_CPF da tabela RESP\_CONTADOR, ambos localizados em Básicos > Parâmetros > Requisitos Legais > Responsável pelas informações\.

CH8476\_2017 \(MFS\-10940\)

RNJ930\-12

__Registro J930 – Campo 12 – IND\_RESP\_LEGAL__

Este campo existe a partir da versão 5\.00, porém ele dever ser gerado para todas as versões\.

Será gerado conforme parâmetro “Indicação do Representante Legal Junto às Bases da RFB” na Aba Signatários dos Dados Iniciais \(menu Parâmetros\):

- Se o referido parâmetro estiver desmarcado, será gerado com conteúdo “N”\.
- Se o parâmetro estiver selecionado, será gerado com conteúdo “S”\.

MFS\-8216

MFS\-9689

__Inclusão do Bloco K \- Conglomerados Econômicos \(Facultativo para o ano\-calendário 2016\)__

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNK001

__Registro K001 – Abertura do Bloco K__

A princípio não atenderemos a geração do Bloco K \- Conglomerados Econômicos \(Facultativo para o ano\-calendário 2016\), porém deverão ser gerados pelo menos os registros de Abertura e Encerramento do Bloco K\.

Registro abertura: K001

MFS8216

MFS\-10358

RNK001\-01

__Registro K001 – Campo 1 – REG__

Informação fixa “K001”\.

MFS9809

RNK001\-02

__Registro K001 – Campo 2 – IND\_DAD__

Indicador de movimento: 

1. Bloco com dados informados; 
2. Bloco sem dados informados\.

Gravar a informação de acordo com os dados encontrados para esse bloco se houver dados informados gravar = 0 \- Bloco com dados informados, se não encontrar dados gravar = 1 \- Bloco sem dados informados\.

Informação fixa “1”\.

Obs\.: Como a princípio não atenderemos a geração do Bloco K, o conteúdo deste campo será fixo igual a “1” \(Bloco sem dados informados\)\. 

MFS9809

MFS\-10358

RNK030\-00

__Registro K030 – Regra geral__

__Origem da Informação__: SAFX240 \- Relação das Empresas Consolidadas\.

__Regra de geração__: Quando a empresa tem escriturações contábeis consolidadas \(Parâmetro “Escriturações Contábeis Consolidadas” __selecionado__ na tela de Dados Iniciais – menu Parâmetros\) __e__ a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5\.00”, a estrutura do registro K030 será gerada conforme definida neste documento\.

Como este registro é de geração facultativa, pode ocorrer do usuário não tê\-lo selecionado no Perfil \(menu Parâmetros >> Perfil\)\. Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K030 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K030 – Período da Escrituração Contábil Consolidada”\.

parâmetro “Escriturações Contábeis Consolidadas” da tela de Dados Iniciais \(menu Parâmetros\)

__Campo\-chave__: DT\_INI 

__Registro pai / Nível hierárquico__: K030 / Nível 2

__Ocorrência__: Um por arquivo\.

MFS\-10358

RNK030\-01

__Registro K030 – Campo 1 – REG__

Informação fixa “K030”\.

MFS\-10358

RNK030\-02

__Registro K030 – Campo 2 – DT\_INI__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Data Inicial do período consolidado\.

MFS\-10358

RNK030\-03

__Registro K030 – Campo 3 – DT\_FIN__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Data Final do período consolidado\.

MFS\-10358

RNK100\-00

__Registro K100 – Regra geral__

__Origem da Informação__: SAFX240 \- Relação das Empresas Consolidadas\.

__Regra de geração__: Quando a empresa tem escriturações contábeis consolidadas \(Parâmetro “Escriturações Contábeis Consolidadas” __selecionado__ na tela de Dados Iniciais – menu Parâmetros\) __e__ a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5\.00”, a estrutura do registro K100 será gerada conforme definida neste documento\. 

Como este registro é de geração facultativa, pode ocorrer do usuário não tê\-lo selecionado no Perfil \(menu Parâmetros >> Perfil\)\. Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K100 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K100 – Relação das Empresas Consolidadas”\.

__Campo\-chave__: EMP\_COD

__Registro pai / Nível hierárquico__: K100 / Nível 3

__Ocorrência__: Vários por arquivo\.

MFS\-10358

RNK100\-01

__Registro K100 – Campo 1 – REG__

Informação fixa “K100”\. 

MFS\-10358

RNK100\-02

__Registro K100 – Campo 2 – COD\_PAIS__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código do País\. 

MFS\-10358

RNK100\-03

__Registro K100 – Campo 3 – EMP\_COD__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da Empresa Participante\.

MFS\-10358

RNK100\-04

__Registro K100 – Campo 4 – CNPJ__

Considerando a Origem da Informação, demonstrar aqui APENAS os primeiros 8 dígitos do conteúdo informado no campo CNPJ da Empresa Participante\. 

MFS\-10358

RNK100\-05

__Registro K100 – Campo 5 – NOME__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Nome da Empresa Participante\.

MFS\-10358

RNK100\-06

__Registro K100 – Campo 6 – PER\_PART__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Percentual de Participação Total\.

MFS\-10358

RNK100\-07

__Registro K100 – Campo 7 – EVENTO__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Evento Ocorrido no Período\.

MFS\-10358

RNK100\-08

__Registro K100 – Campo 8 – PER\_CONS__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Percentual de Consolidação no Final Período\.

MFS\-10358

RNK100\-09

__Registro K100 – Campo 9 – DATA\_INI\_EMP__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Data Início da Consolidação\.

MFS\-10358

RNK100\-10

__Registro K100 – Campo 10 – DATA\_FIN\_EMP__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Data Final da Consolidação\.

MFS\-10358

RNK110\-00

__Registro K110 – Regra geral__

__Origem da Informação__: SAFX241 \- Relação dos Eventos Societários / Empresas Participantes do Evento\.

__Regra de geração__: Quando a empresa tem escriturações contábeis consolidadas \(Parâmetro “Escriturações Contábeis Consolidadas” __selecionado__ na tela de Dados Iniciais – menu Parâmetros\) __e__ a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5\.00”, a estrutura do registro K110 será gerada conforme definida neste documento\. Este registro é filho do K100\. 

Este registro é filho do K100\. Sempre que existir registro nas tabelas indicadas na Origem da Informação vinculada ao registro pai, este registro será gerado\. 

Como este registro é de geração facultativa, pode ocorrer do usuário não tê\-lo selecionado no Perfil \(menu Parâmetros >> Perfil\)\. Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K110 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K110 – Relação dos Eventos Societários”\. 

__Campo\-chave__: Nenhum 

__Registro pai / Nível hierárquico__: K110 / Nível 4

__Ocorrência__: Vários por arquivo\.

MFS\-10358

RNK110\-01

__Registro K110 – Campo 1 – REG__

Informação fixa “K110”\.

MFS\-10358

RNK110\-02

__Registro K110 – Campo 2 – EVENTO__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Evento Societário ocorrido no período\.

MFS\-10358

RNK110\-03

__Registro K110 – Campo 3 – DT\_EVENTO__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Data do Evento Societário\.

MFS\-10358

RNK115\-00

__Registro K115 – Regra geral__

__Origem da Informação__: SAFX241 \- Relação dos Eventos Societários / Empresas Participantes do Evento\.

__Regra de geração__: Quando a empresa tem escriturações contábeis consolidadas \(Parâmetro “Escriturações Contábeis Consolidadas” __selecionado__ na tela de Dados Iniciais – menu Parâmetros\) __e__ a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5\.00”, a estrutura do registro K115 será gerada conforme definida neste documento\.

__Campo\-chave__: Nenhum

__Registro pai / Nível hierárquico__: K115 / Nível 5

__Ocorrência__: Vários por arquivo\.

MFS\-10358

RNK115\-01

__Registro K115 – Campo 1 – REG__

Informação fixa “K115”\.

MFS\-10358

RNK115\-02

__Registro K115 – Campo 2 – EMP\_COD\_PART__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da Empresa envolvida na operação\.

MFS\-10358

RNK115\-03

__Registro K115 – Campo 3 – COND\_PART__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Condição da empresa relacionada à operação\.

MFS\-10358

RNK115\-04

__Registro K115 – Campo 4 – PER\_EVT__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Percentual da empresa participante envolvido na operação\.

MFS\-10358

RNK200\-00

__Registro K200 – Regra geral__

__Origem da Informação__: SAFX2002 – Tabela de Plano de Contas

__Regra de geração__: Quando a empresa tem escriturações contábeis consolidadas \(Parâmetro “Escriturações Contábeis Consolidadas” __selecionado__ na tela de Dados Iniciais – menu Parâmetros\) __e__ a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5\.00”, a estrutura do registro K200 será gerada conforme definida neste documento\. 

Serão consideradas as contas contábeis utilizadas nas escriturações contábeis consolidadas \(campo IND\_CONTA\_CONSOLID = S da SAFX2002\) que possuam movimento \(SAFX242\) no período de consolidação do K030 \(SAFX240\)\.

- Para a geração do Plano de Contas Consolidado, as informações serão recuperadas da tela de Plano de Contas \(menu: Manutenção >> Códigos >> Plano de Contas\) do módulo Mastersaf DW\.
- Para este cenário, deve ser gerado no arquivo as informações do cadastro das contas sintéticas \(campo COD\_CONTA\_SINT da SAFX2002\) associada à conta movimentada encontrada \(SAFX242\) e também o cadastro de todas as outras contas vinculadas, de nível superior, de forma que tenhamos o plano completo\. 

Exemplo:

No movimento \(SAFX242\) temos a conta: 0001\.0001\.0001\.0001, que no cadastro tem:

__Código de Conta__

__Código de Conta Sintética__

__Nível__

0001\.0001\.0001\.0001

0001\.0001\.0001

4

0001\.0001\.0001

0001\.0001

3

0001\.0001

0001

2

0001

1

- Neste exemplo, apenas a conta 0001\.0001\.0001\.0001 foi movimentada, porém, no arquivo gerado devem ser demonstradas informações das contas "0001\.0001\.0001\.0001", "0001\.0001\.0001", "0001\.0001" e "0001"\.

Como este registro é de geração facultativa, pode ocorrer do usuário não tê\-lo selecionado no Perfil \(menu Parâmetros >> Perfil\)\. Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K200 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K200 – Plano de Contas Consolidado”\.

__Campo\-chave__: COD\_CTA

__Registro pai / Nível hierárquico__: K200 / Nível 2

__Ocorrência__: Vários por arquivo\.

MFS\-10358

RNK200\-01

__Registro K200 – Campo 1 – REG__

Informação fixa “K200”\.  

MFS\-10358

RNK200\-02

__Registro K200 – Campo 2 – COD\_NAT__

Considerando a Origem da Informação, demonstrar aqui o conteúdo de acordo com campo Indicador de Natureza conforme abaixo:

Indicador de Natureza:

Se informado ‘0\. Compensação’, gravar ‘05’;

Se informado ‘1\. Ativo’, gravar ‘01’;

Se informado ‘2\. Passivo’, gravar ‘02’;

Se informado ‘3\. Despesa’, gravar ‘04’;

Se informado ‘4\. Receita’, gravar ‘04’;

Se informado ‘5\. Mutações Ativas \("Variações Patrimoniais" anuais\)’, gravar ‘09’;

Se informado ‘6\. Mutações Passivas \("Variações Patrimoniais" anuais\)’, gravar ‘09’;                                                                                                                                                                                                           Se informado ‘7\. Patrimônio Líquido’, gravar ‘03’;                                                                                                                                                                                      Se informado ‘8\. Custo’, gravar ‘04’;

Se informado ‘9\. Outros’, gravar ‘09’\. 

MFS\-10358

RNK200\-03

__Registro K200 – Campo 3 – IND\_CTA__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador de Conta\.

MFS\-10358

RNK200\-04

__Registro K200 – Campo 4 – NIVEL__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Nível\.

MFS\-10358

RNK200\-05

__Registro K200 – Campo 5 – COD\_CTA__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da Conta\.

MFS\-10358

RNK200\-06

__Registro K200 – Campo 6 – COD\_CTA\_SUP__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código de Conta Sintética\.

MFS\-10358

RNK200\-07

__Registro K200 – Campo 7 – CTA__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Descrição da Conta\.

MFS\-10358

RNK210\-00

__Registro K210 – Regra geral__

__Origem da Informação__: Manutenção \- Mapeamento para Planos de Contas das Empresas Consolidadas

__Localizaçao: __Menu SPED,  Módulo: ECD \- Escrituração Contábil Digital, item de menu Manutenção  Bloco K  Mapeamento para Planos de Contas das Empresas Consolidadas

__Regra de geração__: Quando a empresa tem escriturações contábeis consolidadas \(Parâmetro “Escriturações Contábeis Consolidadas” __selecionado__ na tela de Dados Iniciais – menu Parâmetros\) __e__ a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5\.00”, a estrutura do registro K210 será gerada conforme definida neste documento\. 

__Campo\-chave__: COD\_EMP, COD\_CTA\_EMP

__Registro pai / Nível hierárquico__: K210 / Nível 4

__Ocorrência__: Vários por arquivo\.

MFS\-10358

RNK210\-01

__Registro K210 – Campo 1 – REG__

Informação fixa “K210”\.

MFS\-10358

RNK210\-02

__Registro K210 – Campo 2 – COD\_EMP__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código/Nome da Empresa Participante\.

MFS\-10358

RNK210\-03

__Registro K210 – Campo 3 – COD\_CTA\_EMP__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da Conta da Empresa Participante\.

MFS\-10358

RNK300\-00

__Registro K300 – Regra geral__

__Origem da Informação__: SAFX242 \- Saldos das Contas Consolidadas\.

__Regra de geração__: Quando a empresa tem escriturações contábeis consolidadas \(Parâmetro “Escriturações Contábeis Consolidadas” __selecionado__ na tela de Dados Iniciais – menu Parâmetros\) __e__ a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5\.00”, a estrutura do registro K300 será gerada conforme definida neste documento\.

Serão considerados apenas os saldos das contas consolidadas que pertençam ao período de consolidação informado no K030 \(SAFX240\)\.

Como este registro é de geração facultativa, pode ocorrer do usuário não tê\-lo selecionado no Perfil \(menu Parâmetros >> Perfil\)\. Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K300 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K300 – Saldos das Contas Consolidadas”\. 

__Campo\-chave__: COD\_CTA

__Registro pai / Nível hierárquico__: K300 / Nível 3\.

__Ocorrência__: Vários por arquivo\.

MFS\-10358

RNK300\-01

__Registro K300 – Campo 1 – REG__

Informação fixa “K300”\.

MFS\-10358

RNK300\-02

__Registro K300 – Campo 2 – COD\_CTA__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da conta consolidada\.

MFS\-10358

RNK300\-03

__Registro K300 – Campo 3 – VAL\_AG__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Valor absoluto aglutinado\.

MFS\-10358

RNK300\-04

__Registro K300 – Campo 4 – IND\_VAL\_AG__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador da situação do valor aglutinado\.

MFS\-10358

RNK300\-05

__Registro K300 – Campo 5 – VAL\_EL__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Valor absoluto das eliminações\.

MFS\-10358

RNK300\-06

__Registro K300 – Campo 6 – IND\_VAL\_EL__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador da situação do valor eliminado\.

MFS\-10358

RNK300\-07

__Registro K300 – Campo 7 – VAL\_CS__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Valor absoluto consolidado\.

MFS\-10358

RNK300\-08

__Registro K300 – Campo 8 – IND\_VAL\_CS __

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador da situação do valor consolidado\.

MFS\-10358

RNK310\-00

__Registro K310 – Regra geral__

__Origem da Informação__: SAFX243 \- Empresas Detentoras das Parcelas do Valor Eliminado Total\.

__Regra de geração__: Quando a empresa tem escriturações contábeis consolidadas \(Parâmetro “Escriturações Contábeis Consolidadas” __selecionado__ na tela de Dados Iniciais – menu Parâmetros\) __e__ a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5\.00”, a estrutura do registro K310 será gerada conforme definida neste documento\.

Este registro é filho do K300\. Sempre que existir registro nas tabelas indicadas na Origem da Informação vinculada ao registro pai, este registro será gerado\.

Como este registro é de geração facultativa, pode ocorrer do usuário não tê\-lo selecionado no Perfil \(menu Parâmetros >> Perfil\)\. Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K310 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K310 – Empresas Detentoras das Parcelas do Valor Eliminado Total”\.

__Campo\-chave__: EMP\_COD\_PARTE 

__Registro pai / Nível hierárquico__: K310 / Nível 4\.

__Ocorrência__: Vários por arquivo\.

MFS\-10358

RNK310\-01

__Registro K310 – Campo 1 – REG__

Informação fixa “K310”\.

MFS\-10358

RNK310\-02

__Registro K310 – Campo 2 – EMP\_COD\_PARTE__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da empresa detentora do valor aglutinado que foi eliminado\.

MFS\-10358

RNK310\-03

__Registro K310 – Campo 3 – VALOR__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Parcela do valor eliminado total\.

MFS\-10358

RNK310\-04

__Registro K310 – Campo 4 – IND\_VALOR__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador da situação do valor eliminado\.

MFS\-10358

RNK315\-00

__Registro K315 – Regra geral__

__Origem da Informação__: SAFX244 \- Empresas Contrapartes das Parcelas do Valor Eliminado Total\.

__Regra de geração__: Quando a empresa tem escriturações contábeis consolidadas \(Parâmetro “Escriturações Contábeis Consolidadas” __selecionado__ na tela de Dados Iniciais – menu Parâmetros\) __e__ a versão do Leiaute indicada na tela de geração do Meio Magnético for maior ou igual a “5\.00”, a estrutura do registro K315 será gerada conforme definida neste documento\.

Como este registro é de geração facultativa, pode ocorrer do usuário não tê\-lo selecionado no Perfil \(menu Parâmetros >> Perfil\)\. Neste caso, se o usuário selecionar na geração do Meio Magnético um Perfil ao qual o registro K315 não tenha sido selecionado, retornar a mensagem no log: “Empresa com Escriturações Contábeis Consolidadas, conforme parametrizado na tela de Dados Iniciais, porém, não houve seleção do Registro K315 – Empresas Contrapartes das Parcelas do Valor Eliminado Total”\. 

__Campo\-chave__: EMP\_COD\_CONTRA, COD\_CONTRA

__Registro pai / Nível hierárquico__: K315 / Nível 5\.

__Ocorrência__: Vários por arquivo\.

MFS\-10358

RNK315\-01

__Registro K315 – Campo 1 – REG__

Informação fixa “K315”\.

MFS\-10358

RNK315\-02

__Registro K315 – Campo 2 – EMP\_COD\_CONTRA__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da empresa da contrapartida\.

MFS\-10358

RNK315\-03

__Registro K315 – Campo 3 – COD\_CONTRA__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Código da conta consolidada da contrapartida\. 

MFS\-10358

RNK315\-04

__Registro K315 – Campo 4 – VALOR__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Parcela da contrapartida do valor eliminado total\.

MFS\-10358

RNK315\-05

__Registro K315 – Campo 5 – IND\_VALOR__

Considerando a Origem da Informação, demonstrar aqui o conteúdo informado no campo Indicador da situação do valor eliminado\.

MFS\-10358

RNK990

__Registro K990 – Encerramento do Bloco K__

A princípio não atenderemos a geração do Bloco K \- Conglomerados Econômicos \(Facultativo para o ano\-calendário 2016\), porém deverão ser gerados pelo menos os registros de Abertura e Encerramento do Bloco K\.

Registro encerramento: K990 

MFS8216

MFS\-10358

RNK990\-01

__Registro K990 – Campo 1 – REG__

Informação fixa “K990”\. 

MFS9809

RNK990\-02

__Registro K990 – Campo 2 –QTD\_LIN\_K __

Será preenchido com o total de linhas do bloco K\.

MFS9809

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

