# MTZ-Geracao_Meio_Magnetico_Policia_Federal_SIPROQUIM2

- **Fonte:** MTZ-Geracao_Meio_Magnetico_Policia_Federal_SIPROQUIM2.docx
- **Modificado:** 2022-06-21
- **Tamanho:** 122 KB

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

Sumário

[1\.	Regras Gerais	2](#_Toc23876123)

[1\.1	Pré\-requisitos para Geração do Meio Magnético:	4](#_Toc23876124)

[2\.	Parâmetros de Tela	5](#_Toc23876125)

[3\.	Regra Geral de Geração dos Registros	7](#_Toc23876126)

[3\.1	– Regra de Recuperação dos Movimentos de Produtos \(SAFX70\)	8](#_Toc23876127)

[3\.2	– Críticas para Movimentos de Produtos	11](#_Toc23876128)

[4\.	Regras de Geração do Registro Identificação da Empresa/Mapa \(EM\)	13](#_Toc23876129)

[5\.	Regras de Geração do Registro Demonstrativo Geral \(DG\)	13](#_Toc23876130)

[6\.	Regras de Geração do Registro Produto Controlado \(PR\)	13](#_Toc23876131)

[7\.	Regras de Geração do Registro Movimentação Nacional de Produtos Químicos \(MVN\)	14](#_Toc23876132)

[8\.	Regras de Geração do Registro Movimentação \(MM\)	15](#_Toc23876133)

[9\.	Regras de Geração do Registro Transporte \(MT\)	18](#_Toc23876134)

[10\.	Regras de Geração do Registro Armazenagem \(MA\)	19](#_Toc23876135)

[11\.	Regras de Geração do Registro Utilização para Consumo \(UC\)	20](#_Toc23876136)

[12\.	Regras de Geração do Registro Fabricação \(FB\)	22](#_Toc23876137)

# <a id="_Toc23876123"></a>Regras Gerais

Este documento tem como objetivo descrever as regras de geração do arquivo magnético para atendimento a __Portaria nº240/2019__ e a __Portaria MJSP nº10/2019__ da Polícia Federal\. 

__Base Legal__:  

Portaria nº240/2019 e a Portaria MJSP nº10/2019 que estabelecem as normas referentes ao Sistema de Controle e Fiscalização de Produtos Químicos \(SIPROQUIM 2\)\. Esse sistema, mais especificamente os módulos Autoatendimento, Cadastro e Mapas, entra em vigor a partir do dia 01/09/2019\.

Portaria MJSP nº240/2019 – que regulamenta a sistemática do controle efetuado pela Polícia Federal a produtos identificados e a serem controlados através de arquivo ou preenchimento através do Sistema de Controle e Fiscalização de Produtos Químicos – SIPROQUIM\.

Portaria nº10/2019 – Disciplina sobre a nova versão do Sistema de Controle e Fiscalização de Produtos Químicos \(SIPROQUIM 2\): 

a\) O Pipoquem 2, especificamente os módulos autoatendimento, cadastro e mapas, entrará em funcionamento no dia 01 de setembro de 2019, data em que haverá mudança nos procedimentos referentes ao cadastro, licença, envio de mapas de controle e demais solicitações; 

b\) Todos os requerimentos/comunicados/informações de que tratam o artigo anterior deverão, a partir da data assinalada, ser realizados no pipoquem 2, seguindo as regras estabelecidas na Port\. MJSP 240/19; 

c\) A última versão do manual técnico da nova versão do Siproquim encontra\-se disponível através do link abaixo:

[http://www\.pf\.gov\.br/servicos\-pf/produtos\-quimicos/arquivos\-siproquim2/arquivo\-txt](http://www.pf.gov.br/servicos-pf/produtos-quimicos/arquivos-siproquim2/arquivo-txt)

Estamos atendendo a Versão 17 do manual técnico \(mt17\.pdf\), disponível no site em 16/09/2019\.

O arquivo texto gerado nesta funcionalidade é  importado no sistema __SIPROQUIM2__ da Polícia Federal\.

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

## <a id="_Toc23876124"></a>Pré\-requisitos para Geração do Meio Magnético:

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

- Na tela de Parâmetros de Produtos por tipo de Obrigação, relacionar os produtos da SAFX2013 que são controlados pela Policia Federal\. Obrigatoriamente deve ser informado o código de classificação do produto\.
- Parametrizar o DexPara dos Tipos de Operação x Tipos de Obrigação, para a Polícia Federal\. Os Tipos de Operação são as carregadas pela TFIX28 e referenciadas nos movimentos de produtos \(SAFX70\)\.
- Parametrizar as Conversões de Unidades de Medidas \(por Produto ou Padrão\), no módulo Básicos 🡪 Data Warehouse, menu: Manutenção 🡪 Cadastros 🡪 Conversão de Unidades de Medidas\. Considera\-se como unidade de medida origem a do movimento e como destino a unidade do Cadastro de Classificação de Produtos\.
- Carregar os Movimentos de Produtos, através da importação da SAFX70\.
- O módulo Substâncias Controladas também provê uma outra forma de carregar a tabela definitiva X70, que é através de uma geração disponível no menu: Movimento >> Geração\. Esta geração recupera documentos fiscais \(SAFX07, SAFX08\) e movimentos de estoque \(SAFX10\) e utilizando os parâmetros por CFOP e Operação \(vide menu Cadastro 🡪 Parâmetros p/ Geração do Movimento\) gera os movimentos na tabela definitiva X70\.

# <a id="_Toc23876125"></a>Parâmetros de Tela

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

# <a id="_Toc23876126"></a>Regra Geral de Geração dos Registros

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

MVI

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

__Os demais registros devem ser entregues em futuras MFS’s\.__

Os registros devem seguir a ordem acima descrita\.

__Layout__: Ver layout e informações técnicas para geração do arquivo txt no manual técnico do SIPROQUIM2 \(mt17\.pdf\)\.

__Nome do arquivo__:  

O nome do arquivo deve seguir o seguinte formato: 

o M = Arquivo de Mapas;

o A = Ano;

o M = Mês;

o CNPJ = CNPJ da empresa declarante;

o Extensão = \.txt\.

Ex\.: M2017JUN98765432000199\.txt

## <a id="_–_Regra_de"></a><a id="_Toc23876127"></a>– Regra de Recuperação dos Movimentos de Produtos \(SAFX70\)

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

## <a id="_Toc23876128"></a>– Críticas para Movimentos de Produtos

__Criticar os Movimentos de Produtos \(SAFX70\) do período e estabelecimento, que não foram recuperados pela regra descrita no tópico __[__3\.1 \- “Regra de recuperação dos Movimentos de Produtos__](#_–_Regra_de)__”, nas seguintes situações:__

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

__Criticar os Movimentos de Produtos \(X70\_MOV\_SUBST\_CONT\) recuperados pela regra descrita no tópico __[__3\.1 \- “Regra de recuperação dos Movimentos de Produtos__](#_–_Regra_de)__”, nas seguintes situações:__

1. Unidade de Medida do Movimentos de Produtos \(X70\_MOV\_SUBST\_CONT\) seja diferente da Unidade de Medida da Classificação de Produtos \(SCT\_CLASS\_PRD\) e não tenha cadastro de conversão de unidade de medida\. Exibir a seguinte mensagem no log:

*“Movimento do Produto com Medida diferente da cadastrada para a Classificação do Produto e sem cadastro de fator de conversão de unidades de medidas\. Favor realizar o cadastro numa das opções de Conversão de Unidades de Medida, por Produto ou Padrão, no módulo Data Ware House\.*

*Unidade de Medida Movimento do Produto: xxx ;Unidade de Medida Classificação do Produto: yyy””*

*Acrescentar os campos de identificação do registro: Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

1. Parâmetro “Comercialização Nacional” selecionado e Movimento de Produto \(X70\_MOV\_SUBST\_CONT\) a ser gravado no registro MVN, gerar crítica para:

e\.1\) Campo Indicador do Tipo de Frete \(IND\_TP\_FRETE\) não preenchido\. 

*“Movimento de Produto sem Tipo de Frete preenchido, campo de preenchimento obrigatório do registro MVN\.”*

*Acrescentar os campos de identificação do registro: Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

e\.2\) Campo Pessoa Física/Jurídica Transportadora  \(IND\_FIS\_JUR\_TRANSP / COD\_FIS\_JUR\_TRANSP\) não preenchido, quando o Indicador do Tipo de Frete \(IND\_TP\_FRETE\) = ‘3’ – Terceiros 

*“Movimento de Produto sem Transportadora preenchida, informação obrigatório para geração do registro MT\.”*

*Acrescentar os campos de identificação do registro: Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

e\.3\)  Campo Pessoa Física/Jurídica Armazém  \(IND\_FIS\_JUR\_ARMAZEM / COD\_FIS\_JUR\_ARMAZEM\) não preenchido

*“Movimento de Produto sem Armazém preenchido, informação obrigatório para geração do registro MA\.”*

*Acrescentar os campos de identificação do registro: Número NF, Data do Movimento, Pessoa Fis/Jur \(Gr\. Ind\. Cód\), Produto \(Gr, Ind, Cód\)\.*

Obs: gravar registro MVN, quer dizer que o Tipo de Operação do movimento está relacionado à Tipo de Operação da Obrigação correspondente ao parâmetro “Comercialização Nacional”\.  Ver tabela de relacionamento no tópico [3\.1 \- “Regra de recuperação dos Movimentos de Produtos](#_–_Regra_de)”\.

# <a id="_Toc23876129"></a>Regras de Geração do Registro Identificação da Empresa/Mapa \(EM\)

Este registro é o primeiro registro do arquivo e contém informação do estabelecimento e período de geração do arquivo\. 

Além disso informa quais movimentações o arquivo contém, como Comercialização Nacional, Internacional, Produção, Consumo, que serão apresentadas em registros próprios\.

Registro único no arquivo, gerado a partir das informações de cadastro do estabelecimento\.

Ver layout do registro e as regras de preenchimento de cada campo na planilha Policia\_Federal\_Siproquim2\_DEPARA\.xls, aba “Layout Siproquim 2 x Campo SAFX”\.

# <a id="_Toc23876130"></a>Regras de Geração do Registro Demonstrativo Geral \(DG\)

Registro único no arquivo\. 

Este registro é como se fosse um registro de abertura de bloco, pois não contém nenhuma informação além do campo identificador do registro, o tipo “DG”\.

Ver layout do registro e as regras de preenchimento de cada campo na planilha Policia\_Federal\_Siproquim2\_DEPARA\.xls, aba “Layout Siproquim 2 x Campo SAFX”\.

# <a id="_Regras_de_Geração"></a><a id="_Toc23876131"></a>Regras de Geração do Registro Produto Controlado \(PR\)

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

# <a id="_Regras_de_Geração_1"></a><a id="_Toc23876132"></a>Regras de Geração do Registro Movimentação Nacional de Produtos Químicos \(MVN\)

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

# <a id="_Regras_de_Geração_2"></a><a id="_Toc23876133"></a>Regras de Geração do Registro Movimentação \(MM\)

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

# <a id="_Regras_de_Geração_4"></a><a id="_Toc23876134"></a>Regras de Geração do Registro Transporte \(MT\)

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

# <a id="_Regras_de_Geração_3"></a><a id="_Toc23876135"></a>Regras de Geração do Registro Armazenagem \(MA\)

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

# <a id="_Regras_de_Geração_5"></a><a id="_Toc23876136"></a>Regras de Geração do Registro Utilização para Consumo \(UC\)

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

# <a id="_Regras_de_Geração_6"></a><a id="_Toc23876137"></a>Regras de Geração do Registro Fabricação \(FB\)

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

= = = = = =

 

