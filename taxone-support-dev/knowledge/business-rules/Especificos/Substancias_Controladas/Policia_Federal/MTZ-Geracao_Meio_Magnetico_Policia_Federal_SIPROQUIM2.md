# MTZ-Geracao_Meio_Magnetico_Policia_Federal_SIPROQUIM2

- **Fonte:** MTZ-Geracao_Meio_Magnetico_Policia_Federal_SIPROQUIM2.docx
- **Modificado:** 2025-02-25
- **Tamanho:** 158 KB

---

THOMSON REUTERS

Módulo Substâncias Controladas 

Geração do Meio Magnético – Polícia Federal – Portaria 240/19 – SIPROQUIM2

__Localização__: Menu Específico, módulo Substâncias Controladas, menu Atendimento 🡪 Polícia Federal 🡪 Portaria 240/19 🡪 Geração do Meio Magnético – SIPROQUIM2

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS30079__

Liliane Assaf 

Criação da geração do meio magnético da Portaria 240/19 – SIPROQUIM2\.

Estamos atendendo a Versão 17 do manual técnico \(mt17\.pdf\) divulgada em 16/09/2019\.

Escopo dos registros a serem gerados: EM, PR, MVN e filhos, UC e FB\.

21/10/2019

MFS31895

Liliane Assaf

Geração dos registros PR, MM, UC e FB com o Código Oficial da Polícia Federal \(COD\_OFICIAL\_PF\)

07/11/2019

MFS36502

Liliane Assaf

Inclusão do parâmetro Produto Controlado \(PR\)

04/05/2020

MFS88346

Rogério Ohashi

Alteração da regra de geração do Registro de Transporte \(MT\) para considerar todos os tipos de Frete\.

21/06/2022

MFS630251

Liliane Assaf

Inclusão da Movimentação Internacional de Produtos Químicos \(MVI e filhos\)

Manual técnico Versão 18 \(mt18\.pdf\)

10/04/2024

MFS761621

Liliane Assaf

Atualização do manual técnico para versão 1\.1 \(mt11\.pdf\)\.

11/02/2025

Sumário

[1\.	Regras Gerais	1](#_Toc163682343)

[1\.1	Pré\-requisitos para Geração do Meio Magnético:	1](#_Toc163682344)

[2\.	Parâmetros de Tela	1](#_Toc163682345)

[3\.	Regra Geral de Geração dos Registros	1](#_Toc163682346)

[3\.1	– Regra de Recuperação dos Movimentos de Produtos \(SAFX70\)	1](#_Toc163682347)

[3\.2	– Críticas para Movimentos de Produtos	1](#_Toc163682348)

[4\.	Regras de Geração do Registro Identificação da Empresa/Mapa \(EM\)	1](#_Toc163682349)

[5\.	Regras de Geração do Registro Demonstrativo Geral \(DG\)	1](#_Toc163682350)

[6\.	Regras de Geração do Registro Produto Controlado \(PR\)	1](#_Toc163682351)

[7\.	Regras de Geração do Registro Movimentação Nacional de Produtos Químicos \(MVN\)	1](#_Toc163682352)

[8\.	Regras de Geração do Registro Movimentação \(MM\)	1](#_Toc163682353)

[9\.	Regras de Geração do Registro Transporte \(MT\)	1](#_Toc163682354)

[10\.	Regras de Geração do Registro Armazenagem \(MA\)	1](#_Toc163682355)

[11\.	Regras de Geração do Registro Utilização para Consumo \(UC\)	1](#_Toc163682356)

[12\.	Regras de Geração do Registro Fabricação \(FB\)	1](#_Toc163682357)

[13\.	Regras de Geração do Registro Movimentação Internacional de Produtos Químicos \(MVI\)	1](#_Toc163682358)

[14\.	Regras de Geração do Registro de Transporte Nacional \(TRA\)	1](#_Toc163682359)

[15\.	Regras de Geração do Registro de Transporte Internacional \(TRI\)	1](#_Toc163682360)

[16\.	Regras de Geração do Registro Armazenagem \(AMZ\)	1](#_Toc163682361)

[17\.	Regras de Geração do Registro Local de Entrega \(TER\)	1](#_Toc163682362)

[18\.	Regras de Geração do Registro de Adquirente \(ADQ\)	1](#_Toc163682363)

[19\.	Regras de Geração do Registro de Nota Fiscal \(NF\)	1](#_Toc163682364)

[20\.	Regras de Geração do Registro de Produto da Nota Fiscal	1](#_Toc163682365)

# <a id="_Toc163682343"></a>Regras Gerais

Este documento tem como objetivo descrever as regras de geração do arquivo magnético para atendimento a __Portaria nº240/2019__ e a __Portaria MJSP nº10/2019__ da Polícia Federal\. 

__Base Legal__:  

Portaria nº240/2019 e a Portaria MJSP nº10/2019 que estabelecem as normas referentes ao Sistema de Controle e Fiscalização de Produtos Químicos \(SIPROQUIM 2\)\. Esse sistema, mais especificamente os módulos Autoatendimento, Cadastro e Mapas, entra em vigor a partir do dia 01/09/2019\.

Portaria MJSP nº240/2019 – que regulamenta a sistemática do controle efetuado pela Polícia Federal a produtos identificados e a serem controlados através de arquivo ou preenchimento através do Sistema de Controle e Fiscalização de Produtos Químicos – SIPROQUIM\.

Portaria nº10/2019 – Disciplina sobre a nova versão do Sistema de Controle e Fiscalização de Produtos Químicos \(SIPROQUIM 2\): 

a\) O Pipoquem 2, especificamente os módulos autoatendimento, cadastro e mapas, entrará em funcionamento no dia 01 de setembro de 2019, data em que haverá mudança nos procedimentos referentes ao cadastro, licença, envio de mapas de controle e demais solicitações; 

b\) Todos os requerimentos/comunicados/informações de que tratam o artigo anterior deverão, a partir da data assinalada, ser realizados no pipoquem 2, seguindo as regras estabelecidas na Port\. MJSP 240/19; 

c\) A última versão do manual técnico \(mt11\.pdf\) do Siproquim encontra\-se disponível através do link abaixo:

 [https://www\.gov\.br/pf/pt\-br/assuntos/produtos\-quimicos/arquivos\-siproquim2/documentos/manual\-tecnico\-030125\-1\.pdf](https://www.gov.br/pf/pt-br/assuntos/produtos-quimicos/arquivos-siproquim2/documentos/manual-tecnico-030125-1.pdf)

O arquivo texto gerado nesta funcionalidade é importado no sistema __SIPROQUIM2__ da Polícia Federal\.

A geração do meio magnético segue os padrões de geração \(Framework\), com as seguintes abas:

__Parâmetros__

Aba dos parâmetros para a geração do arquivo\.

__Processos__

Esta aba mostra as gerações já efetuadas, e o usuário pode selecionar uma geração para consulta\. 

__Log__

Nesta aba é exibido o relatório do log de erros da geração\. 

__Arquivos__

Nesta aba o usuário pode salvar o arquivo referente às gerações já efetuadas\.

__Quantidade de Registros Gerados__

Nesta aba será mostrado um resumo com a quantidade total de registros gerados para cada tipo de registro no seguinte formato:

<a id="OLE_LINK17"></a><a id="OLE_LINK18"></a><a id="_Hlk5724864"></a>Registro EM \(Identificação da Empresa/Mapa\)

99999

Registro DG \(Demonstrativo Geral\)

99999

Registro PR \(Produto Controlado\)

99999

Registro PC \(Produto Compostos\)

99999

Registro SC \(Substância Controlada que compõe o produto composto\)

99999

Registro RC \(Resíduo Controlado\)

99999

Registro RS \(Resíduo Composto\)

99999

Registro RB \(Substância Controlada que compõe o Resíduo composto\)

99999

Registro MVN \(Movimentação Nacional de Produtos Químicos\)

99999

Registro MM \(Subseção Movimento\)

99999

Registro MT \(<a id="OLE_LINK21"></a>Subseção Transporte\)

99999

Registro MA \(Subseção Armazenagem\)

99999

Registro UP \(Produção\)

99999

Registro UF \(Subseção Produto Final Produzido – Produto Químico Controlado\)

99999

Registro UC \(Consumo\)

99999

Registro FB \(Fabricação\)

99999

## <a id="_Toc163682344"></a>Pré\-requisitos para Geração do Meio Magnético:

- Importar a TFIX28 \(Tipos de Operação\)\. Contém os tipos de operação que podem ser utilizados no Movimento de Produtos \(SAFX70\)\.
- Importar a TFIX38 \(Classificação dos Produtos\), que contém Produtos Controlados definidos nas listas de I a VII do Anexo I da Polícia Federal\.
- Pela Tela de Classificação de Produtos, adicionar as informações de Concentração, Densidade, Unidade de Medida, não presentes na TFIX38, pois são informações que variam de cliente para cliente\.

Na situação em que existam mais de uma Concentração ou Densidade para o mesmo produto controlado, adicionar novos registros preenchendo no campo Código Oficial da Polícia Federal o código oficial do produto controlado \(pertencente às Listas I a VII\)\. 

Exemplo:

Código Classif Produto

Descrição Classif Produto

Densidade

Concentração

Código Oficial da Polícia Federal

NCM

001

PERÓXIDO DE HIDROGÊNIO

4

2

TPN12471031

28470000

002

PERÓXIDO DE HIDROGÊNIO

5

2

TPN12471031

28470000

- Na tela de Parâmetros de Produtos por tipo de Obrigação, relacionar os produtos da SAFX2013 que são controlados pela Polícia Federal\. Obrigatoriamente deve ser informado o código de classificação do produto\.
- Parametrizar o DexPara dos Tipos de Operação x Tipos de Obrigação, para a Polícia Federal\. Os Tipos de Operação são as carregadas pela TFIX28 e referenciadas nos movimentos de produtos \(SAFX70\)\.
- Parametrizar as Conversões de Unidades de Medidas \(por Produto ou Padrão\), no módulo Básicos 🡪 Data Warehouse, menu: Manutenção 🡪 Cadastros 🡪 Conversão de Unidades de Medidas\. Considera\-se como unidade de medida origem a do movimento e como destino a unidade do Cadastro de Classificação de Produtos\.
- Carregar os Movimentos de Produtos, através da importação da SAFX70\.
- O módulo Substâncias Controladas também provê uma outra forma de carregar a tabela definitiva X70, que é através de uma geração disponível no menu: Movimento >> Geração\. Esta geração recupera documentos fiscais \(SAFX07, SAFX08\) e movimentos de estoque \(SAFX10\) e utilizando os parâmetros por CFOP e Operação \(vide menu Cadastro 3🡪 Parâmetros p/ Geração do Movimento\) gera os movimentos na tabela definitiva X70\.

__            MFS630251: Inclusão da Movimentação Internacional de Produtos Químicos \(MVI e filhos\)__

Exclusivamente para a geração dos registros MVI e filhos:

- Importação da TFIX120
- Parametrização do País x País Siproquim 2
- Carregar as Operações de Importação, através da SAFX49
- Carregar as Operações de Exportação, através da SAFX48

# <a id="_Toc163682345"></a>Parâmetros de Tela

Mês/Ano Referência: MM/AAAA

Gerar Registros:

\[ \] Produto Controlado \(PR\)

\[ \] Comercialização Nacional 

\[ \] Comercialização Internacional 

\[ \] Produção

\[ \] Transformação

\[ \] Consumo

\[ \] Fabricação

\[ \] Transporte

\[ \] Armazenamento

Recuperar Informações por: \(o\) Data Movimento

                                              \(  \) Data Emissão

Estabelecimentos:

\[ \] xxxxxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxx

\[ \] xxxxxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxx

\[ \] xxxxxx \- xxxxxxxxxxxxxxxxxxxxxxxxxxxx

Funcionamento dos campos:

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/__

__Default__

__Regra__

<a id="_Hlk517437550"></a>Mês/Ano Referência

Data

\(mês e ano\) 

S

S

MM/AAAA

Neste campo o usuário informa o período \(mês e ano\) para a geração do arquivo\.

Recuperar Informações por

Alfanumérico 

S

S

RadioButton

Default: Data Emissão

Desabilitado

Este campo é composto pelas seguintes opções:

🡪 Data Movimento

🡪 Data Emissão

Regra:

Caso o parâmetro Comercialização Nacional esteja marcado,

   Habilitar campo

Caso o parâmetro Comercialização Internacional esteja marcado,

  Habilitar o campo 

Caso contrário:

  Desabilitar o campo

Gerar Registros

Alfanumérico

S

Check\-box

Default: todos os itens desmarcados

Cada opção é um check\-box\. O usuário pode selecionar um ou mais itens\.

🡪 Produto Controlado \(PR\)

🡪 Comercialização Nacional 

🡪 Comercialização Internacional 

🡪 Produção

🡪 Transformação

🡪 Consumo

🡪 Fabricação

🡪 Transporte

🡪 Armazenamento

Habilitar apenas as opções cujos registros estão sendo considerados:

🡪 Produto Controlado \(PR\)

🡪 Comercialização Nacional

🡪 Comercialização Internacional

🡪 Consumo

🡪 Fabricação

Estabelecimentos

Alfanumérico 

S

S

Check\-box

Default: todos os itens desmarcados

Neste campo é exibida a lista de estabelecimentos da Empresa do login para seleção do usuário\.

Apresentar apenas os estabelecimentos que estejam cadastrados para o Tipo de Obrigação = “PF – Polícia Federal”, na  Tela de Estabelecimento x Tipo de Obrigação \(tabela SCT\_TP\_OBRIGACAO\)\.

Selecionar

Alfanumérico

N

N

Esta opção é um facilitador que permite ao usuário selecionar um ou mais estabelecimentos através de uma janela de seleção da tabela de estabelecimentos\.

O filtro dos estabelecimentos disponibilizados para seleção segue a mesma regra descrita para o campo “Estabelecimento”:

\- Somente Estabelecimentos da empresa do login;

\- Somente Estabelecimentos que cadastrados para o Tipo de Obrigação = “PF – Polícia Federal”, na  Tela de Estabelecimento x Tipo de Obrigação \(tabela SCT\_TP\_OBRIGACAO\)

Quando esta opção é utilizada, após escolher os estabelecimentos e clicar no botão <OK> da janela de seleção, os estabelecimentos selecionados pelo usuário serão demonstrados no campo “Estabelecimentos” já marcados\. 

   

Marcar todos

Alfanumérico

N

N

Através desta opção o usuário poderá marcar e desmarcar simultaneamente todos os estabelecimentos demonstrados no campo “Estabelecimentos”\.

# <a id="_Toc163682346"></a>Regra Geral de Geração dos Registros

Para cada estabelecimento selecionado em tela será gerado um arquivo txt, contendo a seguinte estrutura de registros:

__Registro__

__Descrição__

__Qtde regs \(min:max\)__

__Nível hierárquico__

__Observação__

__EM__

__Identificação da Empresa/Mapa__

1:1

1

__DG__

__Demonstrativo Geral__

1:1

1

__PR__

__Produto Controlado__

0:N

2

Filho do registro DG

PC

Produto Compostos

0:N

2

Filho do registro DG

SC

Substância Controlada que compõe o produto composto

0:N

3

Filho do registro PC

RC

Resíduo Controlado

0:N

2

Filho do registro DG

RS

Resíduo Composto

0:N

2

Filho do registro DG

RB

Substância Controlada que compõe o Resíduo composto

0:N

3

Filho do registro RS

__MVN__

__Movimentação Nacional de Produtos Químicos__

0:N

1

__MM__

__Subseção Movimento__

0:N

2

Filho do registro MVN

__MT__

__Subseção Transporte__

0:1

2

Filho do registro MVN

__MA__

__Subseção Armazenagem__

0:1

2

Filho do registro MVN

__MVI__

__MFS630251: Inclusão do MVI e filhos__

__Movimentação Internacional de Produtos Químicos__

__0:N__

__1__

TRA

Subseção Responsável pelo Transporte \(TRA\)

0:1

2

Filho do registro MVI

TRI

Subseção Responsável pelo Transporte \(TRI\)

0:1

2

Filho do registro MVI

AMZ

Subseção Responsável pela Armazenagem \(AMZ\)

0:1

2

Filho do registro MVI

TER

Subseção Local de Entrega \(TER\)

0:1

2

Filho do registro MVI

ADQ

Subseção Adquirente \(ADQ\)

0:1

2

Filho do registro MVI

NF

Subseção Nota Fiscal \(NF\)

0:N

2

Filho do registro MVI

Produtos

0:N

3

Filho do registro NF

UP

Utilização para Produção 

1

UT

Utilização para Transformação 

0:N

2

__UC__

__Utilização para consumo__

__0:N__

__1__

__FB__

__Fabricação__

__0:N__

__1__

__Obs:  A entrega da MFS\-30079, contempla o seguinte conjunto de registros: EM, DG, PR, MVN, MM, MT, MA, UC, FB\. __

__          Os demais registros devem ser entregues em futuras MFS’s\.__

Os registros devem seguir a ordem acima descrita\.

__Layout__: Ver layout e informações técnicas para geração do arquivo txt no manual técnico do SIPROQUIM2 \(mt11\.pdf\)\.

__Nome do arquivo__:  

O nome do arquivo deve seguir o seguinte formato: 

o M = Arquivo de Mapas;

o A = Ano;

o M = Mês;

o CNPJ = CNPJ da empresa declarante;

o Extensão = \.txt\.

Ex\.: M2017JUN98765432000199\.txt

__MFS761621__: Atualização Manual Técnico Versão 1\.1

O arquivo magnético deve ser gravado no formato UTF\-8, sem caracteres especiais do tipo acento gráfico \(ex: Ç, Á, À, Â, Ã, Ä\) e campos alfanuméricos preenchidos com letra Maiúscula\. Veja na planiha: Policia\_Federal\_Siproquim2\_DEPARA\.xls os campos indicados para serem preenchidos com letras maiúsculas\.

## <a id="_–_Regra_de"></a><a id="_Toc163682347"></a>– Regra de Recuperação dos Movimentos de Produtos \(SAFX70\)

Esta regra será utilizada na geração de praticamente todos os registros desse arquivo, exceto os registros EM, DG\.

__Origem dos dados__: 

Tabela de Movimentação de Produtos \(X70\_MOV\_SUBST\_CONT\)

Tabela de Parâmetros de Produto por Tipo de Obrigação \(X71\_PARAM\_SUBST\)

Tabela de Cadastro de Classificação de Produtos \(SCT\_CLASS\_PRD\)

Tabela de Cadastro do Tipo de Operação x Tipo de Obrigação \(SCT\_OPER\_OBRIG\)

Tabela de Cadastro do Tipo de Operação \(fdt\_sc\_tipo\_oper\)

__Critérios de recuperação__:

- Empresa do Movimento \(X70\_MOV\_SUBST\_CONT\)  =  código da Empresa de login;
- Estabelecimento do Movimento \(X70\_MOV\_SUBST\_CONT\) =  código do Estabelecimento informado em tela;
- Para os parâmetros __Comercialização Nacional e Comercialização Internacional__, aplicar o parâmetro “Recuperar Informações por” como filtro:

Se no parâmetro da tela “Recuperar Informações por” for selecionada a opção “Data Movimento” então:

- 
	- Data do Movimento \(X70\_MOV\_SUBST\_CONT\) deve pertencer ao Mês/Ano Referência;

Se no parâmetro da tela “Recuperar Informações por” for selecionada a opção “Data Emissão” então:

- 
	- Data da Emissão \(X70\_MOV\_SUBST\_CONT\) deve pertencer ao Mês/Ano Referência;

Para os demais parâmetros, considerar como filtro a Data do Movimento:

- 
	- Data do Movimento \(X70\_MOV\_SUBST\_CONT\) deve pertencer ao Mês/Ano Referência;
- Grupo, Indicador e Código do Produto do Movimento \(X70\_MOV\_SUBST\_CONT\) relacionado ao Tipo de Obrigação = ‘PF’, na Tabela de Parâmetros de Produto por Tipo de Obrigação \(X71\_PARAM\_SUBST\); 

Obs: não relacionar diretamente por ident\_produto\!

- Campo Classificação do Produto __preenchido__ na Tabela de Parâmetros de Produto por Tipo de Obrigação \(X71\_PARAM\_SUBST\);
- Tipo de Operação do Movimento \(X70\_MOV\_SUBST\_CONT\) __relacionada__ a um Tipo de Operação da Obrigação para o Tipo de Obrigação = ‘PF’, na Tabela de Cadastro do Tipo de Operação x Tipo de Obrigação \(SCT\_OPER\_OBRIG\)\.
- Filtrar os Tipos de Operação da Obrigação, de acordo com os registros parametrizados em “Gerar Registros” na tela para a geração do arquivo:

__Parâmetros__

__Tipos de Operação da Obrigação \(SCT\_OPER\_OBRIG – cod\_oper\_obrig\)\.__

Comercialização Nacional

1 \- Compra \(EC\)

2 \- Entrada por Transferência \(ET\)

3 \- Venda \(SV\)

4 \- Saída por Transferência \(ST\)

7 \- Recebimento de doação \(ED\)

8 \- Recebimento de produto armazenado \(EA\)

9 \- Recebimento de produto industrializado \(EP\)

10 \- Recebimento de produto para industrialização \(EI\)

11 \- Outros recebimentos \(ER\)

12 \- Outras remessas \(S0\)

13 \- Saídas para Devolução/Retorno de produto armazenado \(SA\) SD

14 \- Saídas para Devolução/Retorno de produto industrializado \(SI\)

15 \- Saídas para Doação \(SD\)

16 \- Saídas para Remessa de produto para armazenagem \(SR\)

17 \- Saídas para Remessa de produto para industrialização\(SP\)

Comercialização Internacional

5 \- Importação \(I\)

6 \- Exportação \(E\)

Produção

Não definido

Transformação

Não definido

Consumo

18 \- Consumo para Limpeza e Manutenção \(UC\-1\)

19 \- Consumo para Análises Laboratoriais \(UC\-2\)

20 \- Consumo para Outras finalidades \(UC\-3\)

21 \- Consumo para Processo Produtivo \(UC\-4\)

22 \- Consumo para Tratamento de Afluentes e Efluentes \(UC\-5\)

Fabricação

23 \- Fabricação \(FB\)

Recuperar cada registro de movimento de produtos individualmente, com o seguinte conjunto de informações:

Da tabela de Cadastro de Classificação de Produtos \(SCT\_CLASS\_PRD\):

- Código de Classificação de Produto \(COD\_CLASS\_PRD\);
- Descrição da Classificação de Produto \(DSC\_CLASS\_PRD\)
- Densidade \(DENSIDADE\)
- Concentração \(PERC\_CONCENT\)
- Unidade de Medida \(COD\_MEDIDA\)
- Código Oficial da Polícia Federal \(COD\_OFICIAL\_PF\)

Da tabela de Movimento de Produtos \(X70\_MOV\_SUBST\_CONT\):

- Código da Empresa
- Código do Estabelecimento
- Data do Movimento \(DATA\_MOVTO\) 
- Data de Emissão \(DATA\_EMISSAO\)
- Movimento de Entrada/Saída \(MOVTO\_E\_S\)
- Tipo de Operação \(TIPO\_OPERACAO\)
- Número do Documento Fiscal \(NUM\_DOCFIS\)
- Série do Documento Fiscal
- Subsérie do Documento Fiscal
- Produto \(identificador, grupo, indicador, código\) 
- Pessoa Física Jurídica \(identificador, grupo, indicador, código, CPF\-CGC, razão social\)
- Quantidade Movimentada \(QUANT\_MOVTO\)
- Unidade de Medida \(COD\_MEDIDA\)
- Pessoa Física/Jurídica Transportador \(identificador, grupo, indicador, código, CPF\-CGC, razão social\)
- Pessoa Física/Jurídica Armazém  \(identificador, grupo, indicador, código, CPF\-CGC, razão social\)
- Indicador do Tipo de Frete \(IND\_TP\_FRETE\)

__MFS630251: Inclusão da Movimentação Internacional de Produtos Químicos \(MVI e filhos\)  __

- Número do Registro de Exportação/Importação \(NUM\_REG\_EXP\_IMP\)
- Data Restrição Embarque \(DAT\_EMBARQUE\)
- Data Conhecimento Embarque \(DAT\_CONHEC\_EMBARQUE\)
- Pessoa Física/Jurídica da Entrega \(identificador, grupo, indicador, código, CPF\-CGC, razão social\)
- Pessoa Física/Jurídica Adquirente \(identificador, grupo, indicador, código, CPF\-CGC, razão social\)

   

      Da tabela de Cadastro do Tipo de Operação x Tipo de Obrigação \(SCT\_OPER\_OBRIG\):

- Código do Tipo de Operação Obrigação \(COD\_OPER\_OBRIG\)

  

   

Caso as Unidades de Medidas do Movimento de Produtos \(X70\_MOV\_SUBST\_CONT\) e da Classificação de Produtos \(SCT\_CLASS\_PRD\) sejam DIFERENTES, devemos recuperar o Fator de Conversão em uma das tabelas de Conversão de Unidades de Medidas por Produto ou Padrão\. 

Buscar primeiro a Conversão de Unidade de Medida por Produto\. Caso não encontre registro, utilizar a Conversão de Unidade de Medida Padrão\.

Da tabela de __Conversão de Unidade de Medidas por__ __Produto__ \(DWT\_CONV\_MEDIDA2\):

Recuperar o __Fator de Conversão__, considerando os critérios:

- Produto \(grupo, indicador e código = produto do Movimento de Produtos \(X70\_MOV\_SUBST\_CONT\)
- Unidade de Medida Origem = Unidade de Medida do Movimento de Produtos \(X70\_MOV\_SUBST\_CONT\)
- Unidade de Medida Destino = Unidade de Medida da Classificação de Produtos

Da tabela de __Conversão de Unidade de Medidas__ __Padrão__ \(DWT\_CONV\_MEDIDA\):

Recuperar o __Fator de Conversão__, considerando os critérios:

- Unidade de Medida Origem = Unidade de Medida do Movimento de Produtos \(X70\_MOV\_SUBST\_CONT\)
- Unidade de Medida Destino = Unidade de Medida da Classificação de Produtos

As Conversões de Unidades de Medidas por Produto ou Padrão, são encontradas no módulo Básicos 🡪 Data Ware House, menu: Manutenção 🡪 Cadastros 🡪 Conversão de Unidades de Medidas\.

__Observação:__

O relatório Relação Mensal dos Movimentos por Classificação de Produto também utiliza esta regra para recuperação dos movimentos \(vide MTZ\-Relatorios\_Policia\_Federal\_Siproquim2\)

*Ir para os tópicos:*

[*6 \- Regras de Geração do Registro Produto Controlado \(PR\)*](#_Regras_de_Geração)

[*7 \- Regras de Geração do Registro Movimentação Nacional de Produtos Químicos \(MVN\)*](#_Regras_de_Geração_1)

[*8 \- Regras de Geração do Registro Movimentação \(MM\)*](#_Regras_de_Geração_2)

[*9 \- Regras de Geração do Registro Transporte \(MT\)*](#_Regras_de_Geração_4)

[*10 \- Regras de Geração do Registro Armazenagem \(MA\)*](#_Regras_de_Geração_3)

[*11 \- Regras de Geração do Registro Utilização para Consumo \(UC\)*](#_Regras_de_Geração_5)

[*12 \- Regras de Geração do Registro Fabricação \(FB\)*](#_Regras_de_Geração_6)

[13 – Regras de Geração do Registro Movimentação Internacional \(MVI\)](#_Regras_de_Geração_7)

[14 – Regras de Geração do Registro de Transporte Nacional \(TRA\)](#_Regras_de_Geração_8)

[15 – Regras de Geração do Registro de Transporte Internacional \(TRI\)](#_Regras_de_Geração_9)

[16 – Regras de Geração do Registro de Armazém \(AMZ\)](#_Regras_de_Geração_10)

[17 – Regras de Geração do Registro de Local de Entrega \(TER\)](#_Regras_de_Geração_11)

[18 – Regras de Geração do Registro de Adquirente \(ADQ\)](#_Regras_de_Geração_13)

[19 – Regras de Geração do Registro de Nota Fiscal \(NF\)](#_Regras_de_Geração_14)

[20 – Regras de Geração do Registro de Produto da Nota Fiscal](#_Regras_de_Geração_12)

## <a id="_Toc163682348"></a>– Críticas para Movimentos de Produtos

__Mensagem de Erro \- Movimentos de Produtos \(SAFX70\) que não são gerados no arquivo magnético, nas seguintes situações:__

1. Campo Classificação do Produto da Tabela de Parâmetros de Produto por Tipo de Obrigação \(X71\_PARAM\_SUBST\) NÃO está preenchido\. Exibir a seguinte mensagem no log:

*“O Movimento do Produto será desconsiderado, pois produto está sem informação de Classificação do Produto em Parâmetros de Produto por Tipo de Obrigação\.”*

*Acrescentar os campos de identificação do registro: Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

1. Campo Código Oficial da Polícia Federal da Tabela de Cadastro da Classificação do Produto \(SCT\_CLASS\_PRD\) NÃO está preenchido\. Exibir a seguinte mensagem no log:

*“O Movimento do Produto será desconsiderado, pois a Classificação do Produto XXXXXX está sem Código Oficial da Polícia Federal\. Favor rever Cadastro de Classificação do Produto\.” *

*Onde XXXXXX é o código da classificação do produto \(COD\_CLASS\_PRD\)*

*Acrescentar os campos de identificação do registro: Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

1. Tipo de Operação do Movimento \(X70\_MOV\_SUBST\_CONT\) NÃO está relacionada a um Tipo de Operação da Obrigação, para o Tipo de Obrigação = ‘PF’\. Exibir a seguinte mensagem no log:

*“O Movimento do Produto será desconsiderado, pois o tipo de operação está sem relacionamento com o tipo de operação da obrigação, em Cadastro do Tipo de Operação x Tipo de Obrigação\.”*

*Acrescentar os campos de identificação do registro: Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

__Mensagem de Aviso \- Movimentos de Produtos \(X70\_MOV\_SUBST\_CONT\) que são gerados no arquivo magnético, nas seguintes situações:__

1. Crítica aplicada a todos os registros:

Se a Unidade de Medida do Movimentos de Produtos \(X70\_MOV\_SUBST\_CONT\) for diferente da Unidade de Medida da Classificação de Produtos \(SCT\_CLASS\_PRD\) e não tenha cadastro de conversão de unidade de medida\. Exibir a seguinte mensagem no log:

*“Movimento do Produto com Medida diferente da cadastrada para a Classificação do Produto e sem cadastro de fator de conversão de unidades de medidas\. Favor realizar o cadastro numa das opções de Conversão de Unidades de Medida, por Produto ou Padrão, no módulo Data Ware House\.*

*Unidade de Medida Movimento do Produto: xxx ;Unidade de Medida Classificação do Produto: yyy””*

*Acrescentar os campos de identificação do registro: Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

1. Crítica aplicada ao registro __MVN__ e filhos:

Se Parâmetro “Comercialização Nacional” estiver selecionado na tela de geração e Movimento de Produto \(X70\_MOV\_SUBST\_CONT\) atender ao critério da geração do registro MVN, gerar crítica para:

e\.1\) Campo Indicador do Tipo de Frete \(IND\_TP\_FRETE\) não preenchido\. 

*“Movimento de Produto sem Tipo de Frete preenchido, campo de preenchimento obrigatório do registro MVN\.”*

*Acrescentar os campos de identificação do registro: Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

e\.2\) Campo Pessoa Física/Jurídica Transportadora \(IND\_FIS\_JUR\_TRANSP / COD\_FIS\_JUR\_TRANSP\) não preenchido, quando o Indicador do Tipo de Frete \(IND\_TP\_FRETE\) = ‘3’ – Terceiros 

*“Movimento de Produto sem Transportadora preenchida, informação obrigatório para geração do registro MT\.”*

*Acrescentar os campos de identificação do registro: Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

e\.3\) Campo Pessoa Física/Jurídica Armazém  \(IND\_FIS\_JUR\_ARMAZEM / COD\_FIS\_JUR\_ARMAZEM\) não preenchido

*“Movimento de Produto sem Armazém preenchido, informação obrigatório para geração do registro MA\.”*

*Acrescentar os campos de identificação do registro: Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

__MFS630251: Inclusão da Movimentação Internacional de Produtos Químicos \(MVI e filhos\)__

1. Crítica aplicada ao registro __MVI__ e filhos:

Se parâmetro “Comercialização Internacional” estiver selecionado na tela de geração e Movimento de Produto \(X70\_MOV\_SUBST\_CONT\) atender ao critério da geração do registro MVI, gerar crítica para:

f\.1\) Se o movimento for de Importação \(Tipo de Operação Obrigação = 5\) e o campo 26\-Número do Registro de Exportação/Importação \(NUM\_REG\_EXP\_IMP\) não preenchido:

*“Movimento de Produto sem Número do Registro de Exportação/Importação preenchido, campo de preenchimento obrigatório do registro MVI nas operações de importação\.”*

*Acrescentar os campos de identificação do registro: Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

f\.2\) Se o movimento for de Importação \(Tipo de Operação Obrigação = 5\) e o campo 33\-Data Restrição Embarque \(DAT\_EMBARQUE\) não preenchido:

*“Movimento de Produto sem Data de Restrição de Embarque preenchido, campo de preenchimento obrigatório do registro MVI nas operações de importação\.”*

*Acrescentar os campos de identificação do registro: Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

f\.3\) Se o movimento for de Importação \(Tipo de Operação Obrigação = 5\) e o campo 34\-Data Conhecimento Embarque \(DAT\_CONHEC\_EMB\) não preenchido:

*“Movimento de Produto sem Data de Conhecimento de Embarque preenchido, campo de preenchimento obrigatório do registro MVI nas operações de importação\.”*

*Acrescentar os campos de identificação do registro: Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

f\.4\) Campo Pessoa Física/Jurídica Transportadora \(IND\_FIS\_JUR\_TRANSP / COD\_FIS\_JUR\_TRANSP\) não preenchido:

*“Movimento de Produto sem Transportadora preenchida, informação obrigatório para geração do registro MVI\.”*

*Acrescentar os campos de identificação do registro: Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

f\.5\) Se o movimento for de Importação por Conta e Ordem \(Tipo de Operação Obrigação = 5 e Tipo de Intermédio da SAFX49 = 2\) ou Exportação \(Tipo de Operação Obrigação = 6\) e Campo Pessoa Física/Jurídica Armazém \(IND\_FIS\_JUR\_ARMAZEM / COD\_FIS\_JUR\_ARMAZEM\) não preenchido

*“Movimento de Produto sem Armazém preenchido, informação obrigatório para geração do registro MVI nas operações de exportação e importação por conta e ordem\.”*

*Acrescentar os campos de identificação do registro: Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

f\.6\) Se o movimento for de Importação \(Tipo de Operação Obrigação = 5\) e Campo Pessoa Física/Jurídica Entrega \(IND\_FIS\_JUR\_ENTREGA / COD\_FIS\_JUR\_ENTREGA\) não preenchido:

*“Movimento de Produto sem Pessoa Fis/Jur de Entrega preenchido, informação obrigatório para geração do registro MVI nas operações de importação\.”*

*Acrescentar os campos de identificação do registro: Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

f\.7\) Se o movimento for de Importação por Conta e Ordem \(Tipo de Operação Obrigação = 5 e Tipo de Intermédio da SAFX49 = 2\) e Campo Pessoa Física/Jurídica Adquirente \(IND\_FIS\_JUR\_ADQ / COD\_FIS\_JUR\_ADQ\) não preenchido:

*“Movimento de Produto sem Pessoa Fis/Jur Adquirente preenchido, informação obrigatório para geração do registro MVI nas operações de importação por conta e ordem\.”*

*Acrescentar os campos de identificação do registro: Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

# <a id="_Toc163682349"></a>Regras de Geração do Registro Identificação da Empresa/Mapa \(EM\)

Este registro é o primeiro registro do arquivo e contém informação do estabelecimento e período de geração do arquivo\. 

Além disso informa quais movimentações o arquivo contém, como Comercialização Nacional, Internacional, Produção, Consumo, que serão apresentadas em registros próprios\.

Registro único no arquivo, gerado a partir das informações de cadastro do estabelecimento\.

Ver layout do registro e as regras de preenchimento de cada campo na planilha Policia\_Federal\_Siproquim2\_DEPARA\.xls, aba “Layout Siproquim 2 x Campo SAFX”\.

# <a id="_Toc163682350"></a>Regras de Geração do Registro Demonstrativo Geral \(DG\)

Registro único no arquivo\. 

Este registro é como se fosse um registro de abertura de bloco, pois não contém nenhuma informação além do campo identificador do registro, o tipo “DG”\.

Ver layout do registro e as regras de preenchimento de cada campo na planilha Policia\_Federal\_Siproquim2\_DEPARA\.xls, aba “Layout Siproquim 2 x Campo SAFX”\.

# <a id="_Regras_de_Geração"></a><a id="_Toc163682351"></a>Regras de Geração do Registro Produto Controlado \(PR\)

Este registro demonstra as informações cadastrais dos produtos controlados \(__simples__\) presentes em todos os registros de movimento do arquivo \(MM,MVI, UC, UF, FB,\.\.\.\)\.

O registro PR só é gerado caso o parâmetro “Produto Controlado \(PR\)” esteja marcado na tela de geração\.

Para gerar este registro, recuperar os movimentos de produtos conforme descrito no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”, considerando como critério:

- Tipos de Operação da Obrigação relacionados a TODOS os parâmetros que estejam selecionados em “Gerar Registros” na tela de geração\. São eles:

\[  \] Comercialização Nacional 

\[  \] Comercialização Internacional 

\[  \] Produção

\[  \] Transformação

\[  \] Consumo

\[  \] Fabricação

Gerar um registro para cada Código de Classificação de Produto \(COD\_CLASS\_PRD\) presente nos movimentos recuperados\.

Ver layout do registro e as regras de preenchimento de cada campo na planilha Policia\_Federal\_Siproquim2\_DEPARA\.xls, aba “Layout Siproquim 2 x Campo SAFX”\.

# <a id="_Regras_de_Geração_1"></a><a id="_Toc163682352"></a>Regras de Geração do Registro Movimentação Nacional de Produtos Químicos \(MVN\)

<a id="_Hlk9000681"></a>Este registro demonstra as informações de notas fiscais dos movimentos dos produtos controlados\.

Este registro deve ser gerado se na tela o parâmetro “Comercialização Nacional” estiver selecionado\.

Para gerar este registro, recuperar os movimentos de produtos conforme descrito no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”, considerando como critério:

- Tipos de Operação da Obrigação relacionados ao parâmetro “Comercialização Nacional”, quando este estiver selecionado em “Gerar Registros” na tela de geração\.  Ver tabela de relacionamento no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”\.

Os registros recuperados devem ser __consolidados__ pelos campos que identificam o documento fiscal e o tipo de operação da obrigação\. Veja:

- Código da Empresa
- Código do Estabelecimento
- Data do Movimento \(DATA\_MOVTO\) 
- Movimento de Entrada/Saída \(MOVTO\_E\_S\)
- Número do Documento Fiscal \(NUM\_DOCFIS\)
- Série do Documento Fiscal
- Subsérie do Documento Fiscal
- Pessoa Física Jurídica \(identificador, grupo, indicador, código, CPF\-CGC, razão social\)
- Tipo de Operação da Obrigação Tabela de Cadastro do Tipo de Operação x Tipo de Obrigação \(SCT\_OPER\_OBRIG – cod\_oper\_obrig\)\.

Ver layout do registro e as regras de preenchimento de cada campo na planilha Policia\_Federal\_Siproquim2\_DEPARA\.xls, aba “Layout Siproquim 2 x Campo SAFX”\.

Observação:

Uma nota fiscal com mais de um produto está carregada nem mais de um registro de Movimento de Produto na SAFX70\. Por isso é importante consolidar os movimentos para geração desse registro\.

# <a id="_Regras_de_Geração_2"></a><a id="_Toc163682353"></a>Regras de Geração do Registro Movimentação \(MM\)

Este registro é filho do registro MVN\.

Demonstra os produtos químicos controlados movimentados nos documentos fiscais, com suas respectivas quantidades\.

Para cada documento fiscal informado no registro MVN, podem existir um ou mais registros MM\. 

Este registro deve ser gerado se na tela o parâmetro “Comercialização Nacional” estiver selecionado\.

Para gerar este registro, recuperar os movimentos de produtos, conforme descrito no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”, considerando o seguinte critério:

- Tipos de Operação da Obrigação relacionados ao parâmetro “Comercialização Nacional”, quando este estiver selecionado em “Gerar Registros” na tela de geração\.

Os registros recuperados devem ser __consolidados__ pelos campos que identificam o documento fiscal, o tipo de operação da obrigação e a Classificação do Produto\. Veja:

- Código da Empresa
- Código do Estabelecimento
- Data do Movimento \(DATA\_MOVTO\) 
- Movimento de Entrada/Saída \(MOVTO\_E\_S\)
- Número do Documento Fiscal \(NUM\_DOCFIS\)
- Série do Documento Fiscal
- Subsérie do Documento Fiscal
- Pessoa Física Jurídica \(identificador, grupo, indicador, código, CPF\-CGC, razão social\)
- Tipo de Operação da Obrigação Tabela de Cadastro do Tipo de Operação x Tipo de Obrigação \(SCT\_OPER\_OBRIG – cod\_oper\_obrig\)\.
- Código de Classificação de Produto \(COD\_CLASS\_PRD\);

__Regra para Cálculo do campo Quantidade__:

Ao consolidar os registros de Movimento do Produto para calcular a Quantidade a ser gravada no registro MM, aplicar o seguinte tratamento:

Para cada registro de Movimento de Produto lido, tratar a Quantidade Movimentada \(campo QUANT\_MOVTO – X70\_MOV\_SUBST\_CONT\):

Passo 1: Aplicar a Conversão de unidade de Medida:

Se as Unidades de Medidas do Movimento de Produtos \(X70\_MOV\_SUBST\_CONT\) e da Classificação de Produtos \(SCT\_CLASS\_PRD\) forem DIFERENTES, então:

Aplicar o Fator de Conversão recuperado conforme descrito no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”\. 

Quantidade Movimenta = Quantidade Movimentada \(QUANT\_MOVTO\) \* Fator de Conversão

		Caso o Fator não seja encontrado, considerar Fator = 0, portanto:

		Quantidade Movimenta = 0

Se as Unidades de Medidas do Movimento de Produtos \(X70\_MOV\_SUBST\_CONT\) e da Classificação de Produtos \(SCT\_CLASS\_PRD\) forem iguais, então:

		Não há aplicação de fator de conversão de unidade de medida\.

Quantidade Movimenta = Quantidade Movimentada \(QUANT\_MOVTO\) 

Passo2: Somar ou subtrair a Quantidade Movimentada calculada no passo 1

Se o Movimento de Produto for de entrada \(MOVTO\_E\_S = ‘1’\) então: 

Somar a quantidade movimentada na consolidação\.

Quantidade Registro MM = Quantidade Registro MM  \+ Quantidade Movimentada resultante do passo 1

Se o Movimento de Produto for de saída \(MOVTO\_E\_S = ‘9’\), então: 

Subtrair a quantidade movimentada na consolidação\.

Quantidade Registro MM = Quantidade Registro MM  \- Quantidade Movimentada resultante do passo 1

Após a execução dos passos 1 e 2 para todos os Movimento de Produto, executar o passo final:

Passo 3: Analisar a Quantidade Registro MM, resultante dos passos 1 e 2\.

Após somar e subtrair quantidade dos movimentos, a Quantidade Registro MM pode ter sinal positivo ou negativo\.

Se  Quantidade Registro MM > 0 então:

Se Tipo de Operação da Obrigação \(SCT\_OPER\_OBRIG – cod\_oper\_obrig\) for de __Entrada__ então

		Resultado coerente, pois foram consolidados movimentos de entrada\.

Se Tipo de Operação da Obrigação \(SCT\_OPER\_OBRIG – cod\_oper\_obrig\) for de __Saída__ então

		Resultado incoerente, o que demonstra um problema no Cadastro do Tipo de Operação x Tipo de Obrigação \(SCT\_OPER\_OBRIG\)\.				Exibir mensagem de erro no relatório:

*“Tipo de Operação da Obrigação “XX  \- YYYYYYYYYY” foi relacionado à Tipos de Operações usados em movimentos de entrada\. Favor rever parametrização em Cadastro do Tipo de Operação x Tipo de Obrigação”*

*Onde XX e YYYYYYYYYY: são respectivamente o código e a descrição do Tipo de Operação da Obrigação\.*

*Acrescentar os campos do registro MM para sua identificação\. Número NF, Data Emissão NF, CNPJ Adquirente/Fornecedor, Código da Classificação do Produto, Código Oficial da Polícia Federal*

Se  Quantidade Registro MM < 0 então:

Se Tipo de Operação da Obrigação \(SCT\_OPER\_OBRIG – cod\_oper\_obrig\) for de __Saída__ então

		Resultado coerente, pois foi foram consolidados movimentos de saída; 

Se Tipo de Operação da Obrigação \(SCT\_OPER\_OBRIG – cod\_oper\_obrig\) for de __Entrada__ então

		Resultado incoerente, o que demonstra um problema no Cadastro do Tipo de Operação x Tipo de Obrigação \(SCT\_OPER\_OBRIG\)\.				Exibir mensagem de erro no relatório:

*“Tipo de Operação da Obrigação “XX  \- YYYYYYYYYY” foi relacionado à Tipos de Operações usados em movimentos de saída\. Favor rever parametrização em Cadastro do Tipo de Operação x Tipo de Obrigação”*

*Onde XX e YYYYYYYYYY: são respectivamente o código e a descrição do Tipo de Operação da Obrigação\.*

*Acrescentar os campos do registro MM para sua identificação\. Número NF, Data Emissão NF, CNPJ Adquirente/Fornecedor, Código da Classificação do Produto, Código Oficial da Polícia Federal*

__Tipos de Operação da Obrigação de Entrada __

__\(SCT\_OPER\_OBRIG – cod\_oper\_obrig\)\.__

1 \- Compra \(EC\)

2 \- Entrada por Transferência \(ET\)

7 \- Recebimento de doação \(ED\)

8 \- Recebimento de produto armazenado \(EA\)

9 \- Recebimento de produto industrializado \(EP\)

10 \- Recebimento de produto para industrialização \(EI\)

11 \- Outros recebimentos \(ER\)

__Tipos de Operação da Obrigação de Saída__

__\(SCT\_OPER\_OBRIG – cod\_oper\_obrig\)\.__

3 \- Venda \(SV\)

4 \- Saída por Transferência \(ST\)

12 \- Outras remessas \(S0\)

13 \- Saídas para Devolução/Retorno de produto armazenado \(SA\) SD

14 \- Saídas para Devolução/Retorno de produto industrializado \(SI\)

15 \- Saídas para Doação \(SD\)

16 \- Saídas para Remessa de produto para armazenagem \(SR\)

17 \- Saídas para Remessa de produto para industrialização \(SP\)

4º Passo: Analisar a Quantidade Registro MM 

Se  Quantidade Registro MM < 0 então:

		Gravar o valor absoluto da Quantidade Registro MM no registro MM\.

Ver layout do registro e as regras de preenchimento de cada campo na planilha Policia\_Federal\_Siproquim2\_DEPARA\.xls, aba “Layout Siproquim 2 x Campo SAFX”\.

# <a id="_Regras_de_Geração_4"></a><a id="_Toc163682354"></a>Regras de Geração do Registro Transporte \(MT\)

Este registro é filho do registro MVN\.

Demonstra informação da transportadora dos documentos fiscais\.

Para cada documento fiscal informado no registro MVN, podem existir zero ou um registro MT\. 

Este registro deve ser gerado se na tela o parâmetro “Comercialização Nacional” estiver selecionado\.

__\[MFS88346\] __Tratamento para considerar “TODOS” os Tipos de Fretes\.

Para gerar este registro, recuperar os movimentos de produtos, conforme descrito no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”, considerando os seguintes critérios:

- Tipos de Operação da Obrigação relacionados ao parâmetro “Comercialização Nacional”, quando este estiver selecionado em “Gerar Registros” na tela de geração\.
- Indicador de Tipo de Frete \(IND\_TP\_FRETE\) = ‘3’ – Terceiros\.

Os registros recuperados devem ser __consolidados__ pelos campos que identificam o documento fiscal e o tipo de operação da obrigação\. Veja:

- Código da Empresa
- Código do Estabelecimento
- Data do Movimento \(DATA\_MOVTO\) 
- Movimento de Entrada/Saída \(MOVTO\_E\_S\)
- Número do Documento Fiscal \(NUM\_DOCFIS\)
- Série do Documento Fiscal
- Subsérie do Documento Fiscal
- Pessoa Física Jurídica \(identificador, grupo, indicador, código, CPF\-CGC, razão social\)
- Tipo de Operação da Obrigação Tabela de Cadastro do Tipo de Operação x Tipo de Obrigação \(SCT\_OPER\_OBRIG – cod\_oper\_obrig\)\.

Ver layout do registro e as regras de preenchimento de cada campo na planilha Policia\_Federal\_Siproquim2\_DEPARA\.xls, aba “Layout Siproquim 2 x Campo SAFX”\.

# <a id="_Regras_de_Geração_3"></a><a id="_Toc163682355"></a>Regras de Geração do Registro Armazenagem \(MA\)

Este registro é filho do registro MVN\.

Demonstra informação de armazém dos documentos fiscais\.

Para cada documento fiscal informado no registro MVN, podem existir zero ou um registro MA\. 

Este registro deve ser gerado se na tela o parâmetro “Comercialização Nacional” estiver selecionado\.

Para gerar este registro, recuperar os movimentos de produtos, conforme descrito no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”, considerando os seguintes critérios:

- Tipos de Operação da Obrigação relacionados ao parâmetro “Comercialização Nacional”, quando este estiver selecionado em “Gerar Registros” na tela de geração\.
- Movimento de Entrada/Saída\(MOVTO\_E\_S\) = ‘9’ – Saída\.

Ou

Movimento de Entrada/Saída\(MOVTO\_E\_S\) = ‘1’ – Entrada e CNPJ da Pessoa Física/Jurídica Armazém <> CNPJ do Estabelecimento

Os registros recuperados devem ser __consolidados__ pelos campos que identificam o documento fiscal, o tipo de operação da obrigação\. Veja:

- Código da Empresa
- Código do Estabelecimento
- Data do Movimento \(DATA\_MOVTO\) 
- Movimento de Entrada/Saída \(MOVTO\_E\_S\)
- Número do Documento Fiscal \(NUM\_DOCFIS\)
- Série do Documento Fiscal
- Subsérie do Documento Fiscal
- Pessoa Física Jurídica \(identificador, grupo, indicador, código, CPF\-CGC, razão social\)
- Tipo de Operação da Obrigação Tabela de Cadastro do Tipo de Operação x Tipo de Obrigação \(SCT\_OPER\_OBRIG – cod\_oper\_obrig\)\.

Ver layout do registro e as regras de preenchimento de cada campo na planilha Policia\_Federal\_Siproquim2\_DEPARA\.xls, aba “Layout Siproquim 2 x Campo SAFX”\.

# <a id="_Regras_de_Geração_5"></a><a id="_Toc163682356"></a>Regras de Geração do Registro Utilização para Consumo \(UC\)

Este registro demonstra informações dos movimentos dos produtos controlados relacionadas a operações de consumo de um dia\.

Este registro deve ser gerado se na tela o parâmetro “Consumo” estiver selecionado\.

Para gerar este registro, recuperar os movimentos de produtos conforme descrito no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”, considerando como critério:

- Tipos de Operação da Obrigação relacionados ao parâmetro “Consumo”, quando este estiver selecionado em “Gerar Registros” na tela de geração\. 

Ver tabela de relacionamento no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”;

Os registros recuperados devem ser __consolidados__ pelos campos que identificam a data do consumo, o tipo de operação da obrigação e a Classificação do Produto\. Veja:

- Código da Empresa
- Código do Estabelecimento
- Data do Movimento \(DATA\_MOVTO\) 
- Tipo de Operação da Obrigação Tabela de Cadastro do Tipo de Operação x Tipo de Obrigação \(SCT\_OPER\_OBRIG – cod\_oper\_obrig\)\.
- Código de Classificação de Produto \(COD\_CLASS\_PRD\);

__Regra para Cálculo do campo Quantidade__:

Ao consolidar os registros de Movimento do Produto para calcular a Quantidade a ser gravada no registro UC, aplicar o seguinte tratamento:

Para cada registro de Movimento de Produto lido, tratar a Quantidade Movimentada \(campo QUANT\_MOVTO – X70\_MOV\_SUBST\_CONT\):

Passo 1: Aplicar a Conversão de unidade de Medida:

Se as Unidades de Medidas do Movimento de Produtos \(X70\_MOV\_SUBST\_CONT\) e da Classificação de Produtos \(SCT\_CLASS\_PRD\) forem DIFERENTES, então:

Aplicar o Fator de Conversão recuperado conforme descrito no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”\. 

Quantidade Movimenta = Quantidade Movimentada \(QUANT\_MOVTO\) \* Fator de Conversão

		Caso o Fator não seja encontrado, considerar Fator = 0, portanto:

		Quantidade Movimenta = 0

Se as Unidades de Medidas do Movimento de Produtos \(X70\_MOV\_SUBST\_CONT\) e da Classificação de Produtos \(SCT\_CLASS\_PRD\) forem iguais, então:

		Não há aplicação de fator de conversão de unidade de medida\.

Quantidade Movimenta = Quantidade Movimentada \(QUANT\_MOVTO\) 

Passo2: Somar ou subtrair a Quantidade Movimentada calculada no passo 1

Se o Movimento de Produto for de entrada \(MOVTO\_E\_S = ‘1’\) então: 

Somar a quantidade movimentada na consolidação\.

Quantidade Registro UC = Quantidade Registro UC  \+ Quantidade Movimentada resultante do passo 1

Se o Movimento de Produto for de saída \(MOVTO\_E\_S = ‘9’\), então: 

Subtrair a quantidade movimentada na consolidação\.

Quantidade Registro UC = Quantidade Registro UC  \- Quantidade Movimentada resultante do passo 1

Após a execução dos passos 1 e 2 para todos os Movimento de Produto, executar os dois passos finais:

Passo 3: Analisar a Quantidade Registro UC, resultante dos passos 1 e 2\.

Após somar e subtrair quantidade dos movimentos, a Quantidade Registro UC pode ter sinal positivo ou negativo\.

Se  Quantidade Registro UC > 0 então:

Como os Tipo de Operação da Obrigação \(SCT\_OPER\_OBRIG – cod\_oper\_obrig\) relacionados à Consumo representam __Saídas__ então:

		Resultado incoerente, o que demonstra um problema no Cadastro do Tipo de Operação x Tipo de Obrigação \(SCT\_OPER\_OBRIG\)\.				Exibir mensagem de erro no relatório:

*“Tipo de Operação da Obrigação “XX  \- YYYYYYYYYY” foi relacionado à Tipos de Operações usados em movimentos de entrada\. Favor rever parametrização em Cadastro do Tipo de Operação x Tipo de Obrigação”*

*Onde XX e YYYYYYYYYY: são respectivamente o código e a descrição do Tipo de Operação da Obrigação\.*

*Acrescentar os campos do registro UC para sua identificação\. Data Consumo, Código da Classificação do Produto*

*Chave: Classificação do Produto: xx \+ Data da Fabricação: xx/xx/xxxx \+ Código de Consumo \+ Código Oficial da Polícia Federal*

Se  Quantidade Registro UC < 0 então:

Como os Tipo de Operação da Obrigação \(SCT\_OPER\_OBRIG – cod\_oper\_obrig\) relacionados à Consumo representam __Saídas__ então:

		Resultado coerente, pois foi foram consolidados movimentos de saída; 

4º Passo: Analisar a Quantidade Registro UC

Se  Quantidade Registro UC < 0 então:

		Gravar o valor absoluto da Quantidade Registro UC no registro UC\.

__Tipos de Operação da Obrigação de Consumo__

__\(SCT\_OPER\_OBRIG – cod\_oper\_obrig\)\.__

18 \- Consumo para Limpeza e Manutenção \(UC\-1\)

19 \- Consumo para Análises Laboratoriais \(UC\-2\)

20 \- Consumo para Outras finalidades \(UC\-3\)

21 \- Consumo para Processo Produtivo \(UC\-4\)

22 \- Consumo para Tratamento de Afluentes e Efluentes \(UC\-5\)

Ver layout do registro e as regras de preenchimento de cada campo na planilha Policia\_Federal\_Siproquim2\_DEPARA\.xls, aba “Layout Siproquim 2 x Campo SAFX”\.

# <a id="_Regras_de_Geração_6"></a><a id="_Toc163682357"></a>Regras de Geração do Registro Fabricação \(FB\)

Este registro demonstra informações dos movimentos dos produtos controlados relacionadas a operações de consumo de um dia\.

Este registro deve ser gerado se na tela o parâmetro “Consumo” estiver selecionado\.

Para gerar este registro, recuperar os movimentos de produtos conforme descrito no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”, considerando como critério:

- Tipos de Operação da Obrigação relacionados ao parâmetro “Consumo”, quando este estiver selecionado em “Gerar Registros” na tela de geração\. 

Ver tabela de relacionamento no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”;

Os registros recuperados devem ser __consolidados__ pelos campos que identificam a data do consumo, o tipo de operação da obrigação e a Classificação do Produto\. Veja:

- Código da Empresa
- Código do Estabelecimento
- Data do Movimento \(DATA\_MOVTO\) 
- Tipo de Operação da Obrigação Tabela de Cadastro do Tipo de Operação x Tipo de Obrigação \(SCT\_OPER\_OBRIG – cod\_oper\_obrig\)\.
- Código de Classificação de Produto \(COD\_CLASS\_PRD\);

__Regra para Cálculo do campo Quantidade__:

Ao consolidar os registros de Movimento do Produto para calcular a Quantidade a ser gravada no registro FB, aplicar o seguinte tratamento:

Para cada registro de Movimento de Produto lido, tratar a Quantidade Movimentada \(campo QUANT\_MOVTO – X70\_MOV\_SUBST\_CONT\):

Passo 1: Aplicar a Conversão de unidade de Medida:

Se as Unidades de Medidas do Movimento de Produtos \(X70\_MOV\_SUBST\_CONT\) e da Classificação de Produtos \(SCT\_CLASS\_PRD\) forem DIFERENTES, então:

Aplicar o Fator de Conversão recuperado conforme descrito no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”\. 

Quantidade Movimenta = Quantidade Movimentada \(QUANT\_MOVTO\) \* Fator de Conversão

		Caso o Fator não seja encontrado, considerar Fator = 0, portanto:

		Quantidade Movimenta = 0

Se as Unidades de Medidas do Movimento de Produtos \(X70\_MOV\_SUBST\_CONT\) e da Classificação de Produtos \(SCT\_CLASS\_PRD\) forem iguais, então:

		Não há aplicação de fator de conversão de unidade de medida\.

Quantidade Movimenta = Quantidade Movimentada \(QUANT\_MOVTO\) 

Passo2: Somar ou subtrair a Quantidade Movimentada calculada no passo 1

Se o Movimento de Produto for de entrada \(MOVTO\_E\_S = ‘1’\) então: 

Somar a quantidade movimentada na consolidação\.

Quantidade Registro FB = Quantidade Registro FB  \+ Quantidade Movimentada resultante do passo 1

Se o Movimento de Produto for de saída \(MOVTO\_E\_S = ‘9’\), então: 

Subtrair a quantidade movimentada na consolidação\.

Quantidade Registro FB = Quantidade Registro FB  \- Quantidade Movimentada resultante do passo 1

Após a execução dos passos 1 e 2 para todos os Movimento de Produto, executar os dois passos finais:

Passo 3: Analisar a Quantidade Registro FB, resultante dos passos 1 e 2\.

Após somar e subtrair quantidade dos movimentos, a Quantidade Registro FB pode ter sinal positivo ou negativo\.

Se  Quantidade Registro FB > 0 então:

Como o Tipo de Operação da Obrigação \(SCT\_OPER\_OBRIG – cod\_oper\_obrig\) relacionado à Fabricação representa __Entrada__ então:

		Resultado coerente, pois foram consolidados movimentos de entrada\.

Se  Quantidade Registro FB < 0 então:

Como o Tipo de Operação da Obrigação \(SCT\_OPER\_OBRIG – cod\_oper\_obrig\) relacionado à Fabricação representa __Entrada__ então:

		Resultado incoerente, o que demonstra um problema no Cadastro do Tipo de Operação x Tipo de Obrigação \(SCT\_OPER\_OBRIG\)\.				Exibir mensagem de erro no relatório:

*“Tipo de Operação da Obrigação “XX  \- YYYYYYYYYY” relacionada à Tipos de Operações de movimentos de saída\. Favor rever parametrização em Cadastro do Tipo de Operação x Tipo de Obrigação”*

*Onde XX e YYYYYYYYYY: são respectivamente o código e a descrição do Tipo de Operação da Obrigação\.*

*Chave: Classificação do Produto: xx \+ Data da Fabricação: xx/xx/xxxx\+ Código Oficial da Polícia Federal*

__Tipos de Operação da Obrigação de Fabricação__

__\(SCT\_OPER\_OBRIG – cod\_oper\_obrig\)\.__

23 \- Fabricação

4º Passo: Analisar a Quantidade Registro FB 

Se  Quantidade Registro FB < 0 então:

		Gravar o valor absoluto da Quantidade Registro FB no registro FB\.

Ver layout do registro e as regras de preenchimento de cada campo na planilha Policia\_Federal\_Siproquim2\_DEPARA\.xls, aba “Layout Siproquim 2 x Campo SAFX”\.

# <a id="_Regras_de_Geração_7"></a><a id="_Toc163682358"></a>Regras de Geração do Registro Movimentação Internacional de Produtos Químicos \(MVI\)

__MFS630251: Inclusão da Movimentação Internacional de Produtos Químicos \(MVI e filhos\)  __

   

Este registro demonstra as informações das importações e exportações dos movimentos dos produtos controlados\.

Este registro deve ser gerado se na tela o parâmetro “Comercialização Internacional” estiver selecionado\.

Para gerar este registro, recuperar os movimentos de produtos conforme descrito no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”, considerando como critério:

- Tipos de Operação da Obrigação relacionados ao parâmetro “Comercialização Internacional”, quando este estiver selecionado em “Gerar Registros” na tela de geração\.  Ver tabela de relacionamento no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”\.

__Sobre Movimentos de Importação:__

Para os Movimentos de Produtos recuperados de __Importação__ \(SAFX70 – campo 06 \- MOVTO\_E\_S <> ‘9’ e Tipo de Operação Obrigação = 5 \- Importação\), recuperar os Registros de Importação na Tabela de Operações de Importação \(SAFX49\) através do relacionamento dos campos:

__SAFX70__

__SAFX49__

01 – COD\_EMPRESA

01 – COD\_EMPRESA

02 – COD\_ESTAB

02 – COD\_ESTAB

05 \- DATA\_MOVTO \(Data do Movimento\)

29 – DATA\_EMISSAO \(Data de Emissão\) \(\*\)

05 \- DAT\_NF \(Data da Nota Fiscal\) Data de Emissão

11 \- Indicador de Pessoa Física/Jurídica

06 \- Indicador de Pessoa Física/Jurídica

12 \- Código da Pessoa Física/Jurídica

07 \- Código da Pessoa Física/Jurídica

08 \- NUM\_DOCFIS

08 \- Número da Nota Fiscal \(NUM\_NF\)

09 \- SERIE\_DOCFIS

09 \- Série da Nota Fiscal \(SERIE\_NF\)

10 \- SUB\_SERIE\_DOCFIS

10 \- Subsérie da Nota Fiscal \(SUB\_SERIE\_NF\)

03 \- IND\_PRODUTO

11 \- Indicador do Produto

04 \- COD\_PRODUTO

12 \- Código do Produto

13 \- Número do Item da Nota Fiscal

Caso a consulta acima não retorne registro, exibir mensagem no log e não gravar registro MVI no arquivo:

*“O Movimento do Produto de Importação será desconsiderado, pois não foi encontrado o registro de Operação de Importação \(SAFX49\)\. Favor incluir informações de importação através da manutenção disponível no módulo Básicos >> Data Warehouse, opção Manutenção >> Exportação / Importação >> Operações de Importação”*

*Acrescentar os campos de identificação do registro da SAFX70: Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)*

Se for encontrado mais de um registro na SAFX49 para um registro da SAFX70, todos devem ser considerados\.  

Na SAFX70 só temos 1 registro para o produto/nota fiscal\. Na SAFX49 pode ter vários registros para o produto/nota fiscal, pois o número do item está na chave\.  Todos os registros devem ser recuperados e agrupados de acordo com o layout do registro MVI\.

__Sobre Movimentos de Exportação:__

Para os Movimentos de Produtos recuperados de __Exportação__ \(SAFX70 – campo 06 \- MOVTO\_E\_S = ‘9’ e Tipo de Operação Obrigação = 6 \- Exportação\), recuperar os Registros de Exportação na Tabela de Operações de Exportação \(SAFX48\) através do relacionamento dos campos:

__SAFX70__

__SAFX48__

01 – COD\_EMPRESA

01 – COD\_EMPRESA

02 – COD\_ESTAB

02 – COD\_ESTAB

05 \- DATA\_MOVTO \(Data do Movimento\)

29 – DATA\_EMISSAO \(Data de Emissão\) \(\*\)

05 \- DAT\_NF \(Data da Nota Fiscal\) Data de Emissão

11 \- Indicador de Pessoa Física/Jurídica

06 \- Indicador de Pessoa Física/Jurídica

12 \- Código da Pessoa Física/Jurídica

07 \- Código da Pessoa Física/Jurídica

08 \- NUM\_DOCFIS

08 \- Número da Nota Fiscal \(NUM\_NF\)

09 \- SERIE\_DOCFIS

09 \- Série da Nota Fiscal \(SERIE\_NF\)

10 \- SUB\_SERIE\_DOCFIS

10 \- Subsérie da Nota Fiscal \(SUB\_SERIE\_NF\)

03 \- IND\_PRODUTO

11 \-Indicador do Produto

04 \- COD\_PRODUTO

12 \- Código do Produto

13 \- Número do Item da Nota Fiscal

Se for encontrado mais de um registro na SAFX48 para um registro da SAFX70, todos devem ser considerados\.  

Na SAFX70 só temos 1 registro para o produto/nota fiscal\. Na SAFX48 pode ter vários registros para o produto/nota fiscal, pois o número do item está na chave\.  Todos os registros devem ser recuperados e agrupados de acordo com o layout do registro MVI,

Caso a consulta acima não retorne registro, exibir mensagem no log e não gravar registro MVI no arquivo:

*“O Movimento do Produto de Exportação será desconsiderado, pois não foi encontrado o registro de Operação de Exportação \(SAFX48\)\. Favor incluir informações de importação através da manutenção disponível no módulo Básicos >> Data Warehouse, opção Manutenção >> Exportação / Importação >> Operações de Exportação”*

*Acrescentar os campos de identificação do registro da SAFX70: Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)*

\(\*\) A DATA\_MOVTO na Geração dos Movimentos é gravada com a DATA\_FISCAL da SAFX07\. O campo 05 – DAT\_NF da SAFX49 é Data de Emissão e não Data Fiscal, e por ser um movimento de entrada essas datas de emissão e fiscal podem ser diferentes\. Por isso o relacionamento entre essas duas tabelas será pela DATA\_EMISSÃO da X70\.  Na saída como Data fiscal e emissão são iguais, o relacionamento entre a SAFX07 e SAFX48 pode ser feito pelo campo DATA\_MOVTO\.

__Regra do Campo ID País Adquirente/Fornecedor__

Para os Movimentos de Produtos recuperados \(SAFX70\) buscar o Código de País a ser gravado no campo Id País Adquirente/Fornec do registro MVI\.

Para isso consultar o Cadastro da Pessoa Física Jurídica \(SAFX04\) com a Pessoa Física/Jurídica do Movimento de Produtos \(campos 11\-IND\_FIS\_JUR e 12\-COD\_FIS\_JUR da SAFX70\)\. 

Caso o campo País não esteja preenchido no Cadastro da Pessoa Física Jurídica \(SAFX04\), exibir a seguinte mensagem no log e gravar registro MVI no arquivo:

*“Registro MVI foi gerado sem informação do País do Adquirente/Fornec, pois falta informação no Cadastro da Pessoa Fis/Jur relacionada ao Movimento de Produtos\. Pessoa Fis/Jur \(Gr\. Ind\. Cód\): gr\-id\-cod”*

*Acrescentar os campos de identificação do registro:*

*Para Importação: Num DI, Data DI, Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

*Para Exportação: Num DUE, Data DUE, Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

Caso o campo País esteja preenchido, mas falte a parametrização do País x País Siproquim 2 \(Polícia Federal\), exibir a seguinte mensagem no log e gravar registro MVI no arquivo:

*“Registro MVI foi gerado sem informação do País do Adquirente/Fornec, pois falta parametrização de País x País Siproquim 2 \(Polícia Federal\)\. Código do País: xxx”*

*Acrescentar os campos de identificação do registro:*

*Para Importação: Num DI, Data DI, Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

*            Para Exportação: Num DUE, Data DUE, Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

O campo ID País será preenchido com o Código do País Siproquim 2 que está relacionado ao Código do País da Pessoa Fisica/Jurídica\.

__Regra do campo Operação__:

Regra baseada no Tipo de Operação Obrigação \(COD\_OPER\_OBRIG\)\.

Se Tipo de Operação Obrigação = '5' \- Importação e o campo 75\- Tipo de Intermédio da SAFX49 = ‘2”, então:

       preencher com __'C’__ \- Importação por Conta e Ordem;

Se Tipo de Operação Obrigação = '5' – Importação e o campo 75\- Tipo de Intermédio da SAFX49 = ‘1” ou “3” ou não preenchido, então:

       preencher com __'I'__ \- Importação

Se Tipo de Operação Obrigação = '6' \- Exportação, então:

      preencher com __'E'__ \- Exportação\.

Caso o Tipo de Operação Obrigação seja igual a '5' \- Importação e o campo 75\-Tipo de Intermédio não esteja preenchido, exibir a seguinte mensagem no log e gravar registro MVI no arquivo:

*“Registro MVI foi gerado com Operação de Importação, mas faltou informação no campo Tipo de Intermédio na Operação de Importação \(SAFX49\), para identificação das Importações por Conta e Ordem\.*

*Acrescentar os campos de identificação do registro:*

*Para Importação: Num DI, Data DI, Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

__Regra do Campo Responsável pela Armazenagem__:

Definição segundo Manual Técnico:

• Exportação: Próprio \(E\)xportador, Empresa \(T\)erceirizada 

• Importação: deixar em branco 

• Importação por Conta e Ordem: Próprio \(I\)mportador, Próprio \(A\)dquirente, \(T\)erceirizada Nacional 

__Regra__:

O Responsável pela Armazenagem é carregado no campo Pessoa Fis/Jur Armazém do Movimento de Produtos \(SAFX70\)\.

Essa regra é feita comparando a Pessoa Fis/Jur Armazém com o Estabelecimento e a Pessoa Física/Jurídica Adquirente\.

Veja:

Se o campo Operação do Registro MVI = ‘__E__’ __– Exportação__:

	Se CNPJ da Pessoa Fis/Jur Armazém = CNPJ do Estabelecimento foco da geração, então:

		Preencher com “E” –Exportador;

	Senão:

		Preencher com “T” – Terceirizada\.

Se o campo Operação do Registro MVI = ‘__I__’ __– Importação__:

	Preencher com espaço\.

Se o campo Operação do Registro MVI = ‘__C’ – Importação por Conta e Ordem__:

	Se CNPJ da Pessoa Fis/Jur Armazém = CNPJ do Estabelecimento foco da geração, então:

		Preencher com “I” \- Importador;

	Se CNPJ da Pessoa Fis/Jur Armazém = CNPJ da Pessoa Física/Jurídica Adquirente do Movimento de Produto, então:

		Preencher com “A” \- Próprio Adquirente;

	Se nenhuma das duas opções acima forem verdadeiras, então:

		Se a UF da Pessoa Fis/Jur Armazém \(SAFX04 campo 19\) = ‘EX’, então:

			Preencher com espaço\.

		Se a UF da Pessoa Fis/Jur Armazém \(SAFX04 campo 19\) <> ‘EX’, então:

			Preencher com “T” \- Terceirizada Nacional

Onde:

- Pessoa Fis/Jur Armazém do Movimento de Produtos: campos 30\-IND\_FIS\_JUR\_ARMAZEM e 31\-COD\_FIS\_JUR\_ARMAZEM da SAFX70
- Pessoa Física/Jurídica Adquirente do Movimento de Produtos: campos 37\-IND\_FIS\_JUR\_ADQ e 38\-COD\_FIS\_JUR\_ADQ da SAFX70

__Regra do Campo Responsável pelo Transporte__:

Definição segundo Manual Técnico: 

• Exportação: Próprio \(E\)xportador, Empresa \(T\)erceirizada Nacional, \(A\)dquirente/Terceirizada Internacional 

• Importação: Próprio \(I\)mportador, \(T\)erceirizada Nacional, \(F\)ornecedor/Terceirizada Internacional 

• Importação por Conta e Ordem: Próprio \(I\)mportador, Próprio Adquirente \(Q\), \(T\)erceirizada Nacional, \(F\)ornecedor/Terceirizada Internacional 

__Regra__:

O Responsável pelo Transporte é carregado no campo Pessoa Fis/Jur Transportadora do Movimento de Produtos \(SAFX70\)\.

Essa regra é feita comparando a Pessoa Fis/Jur Transportadora com o Estabelecimento, a Pessoa Física/Jurídica do Movimento de Produtos \(SAFX70\)\.

Veja:

Se o campo Operação do Registro MVI = ‘__E__’ __– Exportação__:

	Se CNPJ da Pessoa Fis/Jur Transportadora = CNPJ do Estabelecimento foco da geração, então:

		Preencher com “E” – Próprio Exportador;

	Se CNPJ da Pessoa Fis/Jur Transportadora = CNPJ da Pessoa Física/Jurídica do Movimento de Produto, então:

		Preencher com “A” – Adquirente;

	Se nenhuma das duas opções acima forem verdadeiras, então:

		Se a UF da Pessoa Fis/Jur Transportadora \(SAFX04 campo 19\) = ‘EX’, então:

			Preencher com “A” \- Terceirizada Internacional

		Se a UF da Pessoa Fis/Jur Transportadora \(SAFX04 campo 19\) <> ‘EX’, então:

			Preencher com “T” \- Terceirizada Nacional

Se o campo Operação do Registro MVI = ‘__I__’ __– Importação__:

	Se CNPJ da Pessoa Fis/Jur Transportadora = CNPJ do Estabelecimento foco da geração, então:

		Preencher com “I” \- Importador;

	Se CNPJ da Pessoa Fis/Jur Transportadora = CNPJ da Pessoa Física/Jurídica do Movimento de Produto, então:

		Preencher com “F” \- Fornecedor;

	Se nenhuma das duas opções acima forem verdadeiras, então:

		Se a UF da Pessoa Fis/Jur Transportadora \(SAFX04 campo 19\) = ‘EX’, então:

			Preencher com “F” \- Terceirizada Internacional

		Se a UF da Pessoa Fis/Jur Transportadora \(SAFX04 campo 19\) <> ‘EX’, então:

			Preencher com “T” \- Terceirizada Nacional

Se o campo Operação do Registro MVI = ‘__C’ – Importação por Conta e Ordem__:

	Se CNPJ da Pessoa Fis/Jur Transportadora = CNPJ do Estabelecimento foco da geração, então:

		Preencher com “I” \- Importador;

	Se CNPJ da Pessoa Fis/Jur Transportadora = CNPJ da Pessoa Física/Jurídica do Movimento de Produto, então:

		Preencher com “F” \- Fornecedor;

	Se CNPJ da Pessoa Fis/Jur Transportadora = CNPJ da Pessoa Física/Jurídica Adquirente do Movimento de Produto, então:

		Preencher com “Q” \- Próprio Adquirente;

	Se nenhuma das três opções acima forem verdadeiras, então:

		Se a UF da Pessoa Fis/Jur Transportadora \(SAFX04 campo 19\) = ‘EX’, então:

			Preencher com “F” \- Terceirizada Internacional

		Se a UF da Pessoa Fis/Jur Transportadora \(SAFX04 campo 19\) <> ‘EX’, então:

			Preencher com “T” \- Terceirizada Nacional

Onde:

- Pessoa Fis/Jur Transportadora do Movimento de Produtos: campos 27\-IND\_FIS\_JUR\_TRANSP e 28\-COD\_FIS\_JUR\_TRANSP da SAFX70
- Pessoa Física/Jurídica do Movimento de Produtos:  campos 11\-IND\_FIS\_JUR e 12\-COD\_FIS\_JUR da SAFX70
- Pessoa Física/Jurídica Adquirente do Movimento de Produtos: campos 37\-IND\_FIS\_JUR\_ADQ e 38\-COD\_FIS\_JUR\_ADQ da SAFX70

__Regra do Campo Local de Entrega__:

Definição segundo Manual Técnico:

Local de Entrega: 

Próprio \(I\)mportador, 

Empresa \(T\)erceirizada\.

Se não for importação, deixar campo em branco

__Regra__:

O Local de Entrega é carregado no campo Pessoa Fis/Jur Entrega do Movimento de Produtos \(SAFX70\)\.

Essa regra é feita comparando a Pessoa Fis/Jur Entrega com o Estabelecimento\.

Veja:

Se o campo Operação do Registro MVI = ‘__E__’ __– Exportação__:

	Preencher com espaço\.

Se o campo Operação do Registro MVI = ‘__I__’ __– Importação__ ou ‘__C’ – Importação por Conta e Ordem__:

	Se CNPJ da Pessoa Fis/Jur Entrega = CNPJ do Estabelecimento foco da geração, então:

		Preencher com “I” \- Importador;

	Senão:

		Preencher com “T” \- Terceirizada

Onde:

- Pessoa Fis/Jur Entrega do Movimento de Produtos: campos 35\-IND\_FIS\_JUR\_ENTREGA e 36\-COD\_FIS\_JUR\_ENTREGA da SAFX70

__Sobre a Consolidação dos Movimentos para gravação do registro MVI:__

Os registros recuperados devem ser __consolidados__ por todos os campos que compõe o layout do registro MVI\.

Ver layout do registro e as regras de preenchimento de cada campo na planilha Policia\_Federal\_Siproquim2\_DEPARA\.xls, aba “Layout Siproquim 2 x Campo SAFX”\.

# <a id="_Regras_de_Geração_8"></a><a id="_Toc163682359"></a>Regras de Geração do Registro de Transporte Nacional \(TRA\)

__MFS630251: Inclusão da Movimentação Internacional de Produtos Químicos \(MVI e filhos\)__

Este registro é filho do registro MVI\.

Demonstra informação da transportadora dos documentos fiscais\.

O registro TRA somente deve ser gerado quando o Responsável Transporte for uma __Terceirizada__ __Nacional__ \(campo Responsável Transporte do MVI = “T” Terceirizada Nacional\)\.

Para cada registro MVI, podem existir zero ou vários registros TRA\. 

Este registro deve ser gerado se na tela o parâmetro “Comercialização Internacional” estiver selecionado\.

Para gerar este registro, recuperar os movimentos de produtos, conforme descrito no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”, considerando os seguintes critérios:

- Tipos de Operação da Obrigação relacionados ao parâmetro “Comercialização Internacional”, quando este estiver selecionado em “Gerar Registros” na tela de geração\.
- Campo Responsável Transporte do Registro MVI = “T” Terceirizada Nacional\.

__Sobre a Consolidação dos Movimentos para gravação do registro TRA:__

Os registros recuperados devem ser __consolidados__ por todos os campos que compõe o layout dos registros MVI\+TRA\.

Ver layout do registro e as regras de preenchimento de cada campo na planilha Policia\_Federal\_Siproquim2\_DEPARA\.xls, aba “Layout Siproquim 2 x Campo SAFX”\.

# <a id="_Regras_de_Geração_9"></a><a id="_Toc163682360"></a>Regras de Geração do Registro de Transporte Internacional \(TRI\)

__MFS630251: Inclusão da Movimentação Internacional de Produtos Químicos \(MVI e filhos\)__

Este registro é filho do registro MVI\.

Demonstra informação da transportadora dos documentos fiscais\.

O registro TRI somente deve ser gerado quando o Responsável Transporte for uma __Terceirizada__ __Internacional__\.

Para cada registro MVI, podem existir zero ou vários registros TRI\. 

Este registro deve ser gerado se na tela o parâmetro “Comercialização Internacional” estiver selecionado\.

Para gerar este registro, recuperar os movimentos de produtos, conforme descrito no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”, considerando os seguintes critérios:

- Tipos de Operação da Obrigação relacionados ao parâmetro “Comercialização Internacional”, quando este estiver selecionado em “Gerar Registros” na tela de geração\.
- Campo Responsável Transporte do Registro MVI = “F” \- Terceirizada Internacional e CNPJ da Pessoa Fis/Jur Transportadora <> CNPJ da Pessoa Física/Jurídica do Movimento de Produto

ou

- Campo Responsável Transporte do Registro MVI = “A” \- Terceirizada Internacional e CNPJ da Pessoa Fis/Jur Transportadora <> CNPJ da Pessoa Física/Jurídica do Movimento de Produto

__Sobre a Consolidação dos Movimentos para gravação do registro TRI:__

Os registros recuperados devem ser __consolidados__ por todos os campos que compõe o layout dos registros MVI\+TRI\.

Ver layout do registro e as regras de preenchimento de cada campo na planilha Policia\_Federal\_Siproquim2\_DEPARA\.xls, aba “Layout Siproquim 2 x Campo SAFX”\.

# <a id="_Regras_de_Geração_10"></a><a id="_Toc163682361"></a>Regras de Geração do Registro Armazenagem \(AMZ\)

__MFS630251: Inclusão da Movimentação Internacional de Produtos Químicos \(MVI e filhos\)__

Este registro é filho do registro MVI\.

Demonstra informação de armazém dos documentos fiscais\.

O registro AMZ somente deve ser gerado para Exportação ou para Importação por Conta e Ordem, sendo que o último apenas se o Responsável Transporte for o próprio importador ou uma terceirizada nacional\. \(campos do MVI Operação = “E” ou “C”, Responsável Transporte = “I” ou “T”\)\.

Para cada registro MVI, podem existir zero ou vários registros AMZ\. 

Este registro deve ser gerado se na tela o parâmetro “Comercialização Internacional” estiver selecionado\.

Para gerar este registro, recuperar os movimentos de produtos, conforme descrito no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”, considerando os seguintes critérios:

- Tipos de Operação da Obrigação relacionados ao parâmetro “Comercialização Internacional”, quando este estiver selecionado em “Gerar Registros” na tela de geração\.
- Campo Operação do Registro MVI = ‘E’ \- Exportação 

Ou

Campo Operação do Registro MVI = ‘C’ \- Importação por Conta e Ordem e Campo Responsável Transporte do Registro MVI = “I” – Importador, ou “T” \- Terceirizada Nacional

__Sobre a Consolidação dos Movimentos para gravação do registro AMZ:__

Os registros recuperados devem ser __consolidados__ por todos os campos que compõe o layout dos registros MVI\+AMZ\.

Ver layout do registro e as regras de preenchimento de cada campo na planilha Policia\_Federal\_Siproquim2\_DEPARA\.xls, aba “Layout Siproquim 2 x Campo SAFX”\.

# <a id="_Regras_de_Geração_11"></a><a id="_Toc163682362"></a>Regras de Geração do Registro Local de Entrega \(TER\)

__MFS630251: Inclusão da Movimentação Internacional de Produtos Químicos \(MVI e filhos\)__

Este registro é filho do registro MVI\.

Demonstra informação de Local de Entrega dos documentos fiscais\.

O registro TER somente deve ser gerado para Importação ou Importação por Conta e Ordem \(campo Operação do MVI = “I” ou “C”\)\.

Para cada registro MVI, podem existir zero ou vários registros TER\. 

Este registro deve ser gerado se na tela o parâmetro “Comercialização Internacional” estiver selecionado\.

Para gerar este registro, recuperar os movimentos de produtos, conforme descrito no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”, considerando os seguintes critérios:

- Tipos de Operação da Obrigação relacionados ao parâmetro “Comercialização Internacional”, quando este estiver selecionado em “Gerar Registros” na tela de geração\.
- Campo Operação do Registro MVI = ‘I’ – Importação, ou ‘C’ \- Importação por Conta e Ordem

__Sobre a Consolidação dos Movimentos para gravação do registro TER:__

Os registros recuperados devem ser __consolidados__ por todos os campos que compõe o layout dos registros MVI\+TER\.

Ver layout do registro e as regras de preenchimento de cada campo na planilha Policia\_Federal\_Siproquim2\_DEPARA\.xls, aba “Layout Siproquim 2 x Campo SAFX”\.

# <a id="_Regras_de_Geração_13"></a><a id="_Toc163682363"></a>Regras de Geração do Registro de Adquirente \(ADQ\)

__MFS630251: Inclusão da Movimentação Internacional de Produtos Químicos \(MVI e filhos\)__

Este registro é filho do registro MVI\.

Demonstra informação do Adquirente dos documentos fiscais\.

O registro ADQ somente deve ser gerado para Importação por Conta e Ordem \(campo Operação do MVI = “C”\)\.

Para cada registro MVI, podem existir zero ou vários registros ADQ\. 

Este registro deve ser gerado se na tela o parâmetro “Comercialização Internacional” estiver selecionado\.

Para gerar este registro, recuperar os movimentos de produtos, conforme descrito no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”, considerando os seguintes critérios:

- Tipos de Operação da Obrigação relacionados ao parâmetro “Comercialização Internacional”, quando este estiver selecionado em “Gerar Registros” na tela de geração\.
- Campo Operação do Registro MVI = ‘C’ \- Importação por Conta e Ordem

__Sobre a Consolidação dos Movimentos para gravação do registro TER:__

Os registros recuperados devem ser __consolidados__ por todos os campos que compõe o layout dos registros MVI\+ADQ\.

Ver layout do registro e as regras de preenchimento de cada campo na planilha Policia\_Federal\_Siproquim2\_DEPARA\.xls, aba “Layout Siproquim 2 x Campo SAFX”\.

# <a id="_Regras_de_Geração_14"></a><a id="_Toc163682364"></a>Regras de Geração do Registro de Nota Fiscal \(NF\)

__MFS630251: Inclusão da Movimentação Internacional de Produtos Químicos \(MVI e filhos\)__

Este registro é filho do registro MVI\.

Demonstra informação das notas fiscais dos movimentos dos produtos controlados\.

O registro NF deve ser gerado para todas as Operações \(Importação, Exportação e Importação por Conta e Ordem \(campo Operação do MVI = “I, “E”, “C”\)\.

Para cada registro MVI, podem existir 1 ou vários registros NF\. 

Este registro deve ser gerado se na tela o parâmetro “Comercialização Internacional” estiver selecionado\.

Para gerar este registro, recuperar os movimentos de produtos, conforme descrito no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”, considerando os seguintes critérios:

- Tipos de Operação da Obrigação relacionados ao parâmetro “Comercialização Internacional”, quando este estiver selecionado em “Gerar Registros” na tela de geração\.

__Sobre a Consolidação dos Movimentos para gravação do registro NF:__

Os registros recuperados devem ser __consolidados__ por todos os campos que compõe o layout dos registros MVI\+NF\.

Ver layout do registro e as regras de preenchimento de cada campo na planilha Policia\_Federal\_Siproquim2\_DEPARA\.xls, aba “Layout Siproquim 2 x Campo SAFX”\.

# <a id="_Regras_de_Geração_12"></a><a id="_Toc163682365"></a>Regras de Geração do Registro de Produto da Nota Fiscal

__MFS630251: Inclusão da Movimentação Internacional de Produtos Químicos \(MVI e filhos\)__

Este registro é filho do registro NF\.

Demonstra os produtos químicos controlados movimentados nos documentos fiscais, com suas respectivas quantidades\. 

A regra de geração desse registro é bastante semelhante a do registro MM\.

Para cada documento fiscal informado no registro NF, podem existir um ou mais registros de Produto\. 

Este registro deve ser gerado se na tela o parâmetro “Comercialização Internacional” estiver selecionado\.

Para gerar este registro, recuperar os movimentos de produtos, conforme descrito no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”, considerando o seguinte critério:

- Tipos de Operação da Obrigação relacionados ao parâmetro “Comercialização Internacional”, quando este estiver selecionado em “Gerar Registros” na tela de geração\.

__Sobre a Consolidação dos Movimentos para gravação do registro de Produto:__

Os registros recuperados devem ser __consolidados__ por todos os campos que compõe o layout dos registros MVI\+NF\+ o próprio registro de Produto, exceto o campo quantidade que será acumulada de acordo com a regra abaixo\.

__Regra para Cálculo do campo Quantidade__:

Ao consolidar os registros de Movimento do Produto totalizando a Quantidade, através do seguinte tratamento:

Para cada registro de Movimento de Produto lido, tratar a Quantidade Movimentada \(campo QUANT\_MOVTO – X70\_MOV\_SUBST\_CONT\):

Passo 1: Aplicar a Conversão de unidade de Medida:

Se as Unidades de Medidas do Movimento de Produtos \(X70\_MOV\_SUBST\_CONT\) e da Classificação de Produtos \(SCT\_CLASS\_PRD\) forem DIFERENTES, então:

Aplicar o Fator de Conversão recuperado conforme descrito no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”\. 

Quantidade Movimenta = Quantidade Movimentada \(QUANT\_MOVTO\) \* Fator de Conversão

		Caso o Fator não seja encontrado, considerar Fator = 0, portanto:

		Quantidade Movimenta = 0

Se as Unidades de Medidas do Movimento de Produtos \(X70\_MOV\_SUBST\_CONT\) e da Classificação de Produtos \(SCT\_CLASS\_PRD\) forem iguais, então:

		Não há aplicação de fator de conversão de unidade de medida\.

Quantidade Movimenta = Quantidade Movimentada \(QUANT\_MOVTO\) 

Passo2: Somar ou subtrair a Quantidade Movimentada calculada no passo 1

Se o Movimento de Produto for de entrada \(MOVTO\_E\_S = ‘1’\) então: 

Somar a quantidade movimentada na consolidação\.

Quantidade Registro = Quantidade Registro \+ Quantidade Movimentada resultante do passo 1

Se o Movimento de Produto for de saída \(MOVTO\_E\_S = ‘9’\), então: 

Subtrair a quantidade movimentada na consolidação\.

Quantidade Registro = Quantidade Registro \- Quantidade Movimentada resultante do passo 1

Após a execução dos passos 1 e 2 para todos os Movimento de Produto, executar o passo final:

Passo 3: Analisar a Quantidade Registro, resultante dos passos 1 e 2\.

Após somar e subtrair quantidade dos movimentos, a Quantidade Registro pode ter sinal positivo ou negativo\.

Se  Quantidade Registro > 0 então:

Se Tipo de Operação da Obrigação \(SCT\_OPER\_OBRIG – cod\_oper\_obrig\) for de __Entrada__ então

		Resultado coerente, pois foram consolidados movimentos de entrada\.

Se Tipo de Operação da Obrigação \(SCT\_OPER\_OBRIG – cod\_oper\_obrig\) for de __Saída__ então

		Resultado incoerente, o que demonstra um problema no Cadastro do Tipo de Operação x Tipo de Obrigação \(SCT\_OPER\_OBRIG\)\.				Exibir mensagem de erro no relatório:

*“Tipo de Operação da Obrigação “XX  \- YYYYYYYYYY” foi relacionado à Tipos de Operações usados em movimentos de entrada\. Favor rever parametrização em Cadastro do Tipo de Operação x Tipo de Obrigação”*

*Onde XX e YYYYYYYYYY: são respectivamente o código e a descrição do Tipo de Operação da Obrigação\.*

*Acrescentar os campos do registro MM para sua identificação\. Número NF, Data Emissão NF, CNPJ Adquirente/Fornecedor, Código da Classificação do Produto, Código Oficial da Polícia Federal*

Se  Quantidade Registro < 0 então:

Se Tipo de Operação da Obrigação \(SCT\_OPER\_OBRIG – cod\_oper\_obrig\) for de __Saída__ então

		Resultado coerente, pois foi foram consolidados movimentos de saída; 

Se Tipo de Operação da Obrigação \(SCT\_OPER\_OBRIG – cod\_oper\_obrig\) for de __Entrada__ então

		Resultado incoerente, o que demonstra um problema no Cadastro do Tipo de Operação x Tipo de Obrigação \(SCT\_OPER\_OBRIG\)\.				Exibir mensagem de erro no relatório:

*“Tipo de Operação da Obrigação “XX  \- YYYYYYYYYY” foi relacionado à Tipos de Operações usados em movimentos de saída\. Favor rever parametrização em Cadastro do Tipo de Operação x Tipo de Obrigação”*

*Onde XX e YYYYYYYYYY: são respectivamente o código e a descrição do Tipo de Operação da Obrigação\.*

*Acrescentar os campos do registro MM para sua identificação\. Número NF, Data Emissão NF, CNPJ Adquirente/Fornecedor, Código da Classificação do Produto, Código Oficial da Polícia Federal*

__Tipos de Operação da Obrigação de Entrada __

__\(SCT\_OPER\_OBRIG – cod\_oper\_obrig\)\.__

5 \- Importação \(I\)

__Tipos de Operação da Obrigação de Saída__

__\(SCT\_OPER\_OBRIG – cod\_oper\_obrig\)\.__

6 \- Exportação \(E\)

4º Passo: Analisar a Quantidade Registro

Se  Quantidade Registro MM < 0 então:

		Gravar o valor absoluto da Quantidade Registro no registro de Produto\.

Ver layout do registro e as regras de preenchimento de cada campo na planilha Policia\_Federal\_Siproquim2\_DEPARA\.xls, aba “Layout Siproquim 2 x Campo SAFX”\.

= = = = = =

 

