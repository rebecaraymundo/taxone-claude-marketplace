# MTZ-Job-Servidor-Importacao_SAFX2064

- **Fonte:** MTZ-Job-Servidor-Importacao_SAFX2064.docx
- **Modificado:** 2025-06-09
- **Tamanho:** 114 KB

---

THOMSON REUTERS

Job Servidor \- Importação da SAFX2064

__Cadastro de Estabelecimento__

__           __

__Localização__: Menu Básicos, Módulo: Job Servidor, itens de menu:

	

\- Importação à Execução

\- Importação Batch à Programação à Execução

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

MFS59797

Criação da tabela SAFX2064 para carga das informações do Cadastro de Estabelecimento\. 

03/03/2021

MFS\-79885

Alessandra Cristina Navatta

Inclusão do campo Natureza Jurídica \(RN95\)

04/05/2022

MFS741454

Liliane Assaf

Inclusão da validação do CNPJ Alfanumérico “MTZ\-Regra de Validação do CNPJ\.docx”

08/01/2025

MFS772966

Andréa Rocha

Inclusão de um campo reservado\.

18/03/2025

MFS829924

Andréa Rocha

Inclusão de uma nova opção para o campo Natureza da Pessoa Jurídica, para utilizar as mesmas opções disponíveis na tela de manutenção do Estabelecimento\.

05/06/2025

REGRAS DE NEGÓCIO

__CÓD__

__DESCRIÇÃO__

__OS/CH__

__RN00__

__Estrutura da tabela SAFX2064__ à vide manual de layout

A manutenção desta tabela é feita na tela de Cadastro de Estabelecimento, no módulo Parâmetros: 

- Menu: Preliminares > Empresa/Estabelecimento

As informações importadas devem ser gravadas na tabela ESTABELECIMENTO\.

__Os campos que compõem a chave da tabela são:__

- Código da Empresa \+ Código do Estabelecimento	

__Processo de Importação Automática de SAFX__

Esse processo ocorre somente no TAX ONE e o mesmo já está habilitado para contemplar as novas SAFX’s\.

Para verificar as adequações necessárias, utilizar como exemplo, a SAFX04\.

__Campos internos__

Campos DAT\_OPERACAO, USUARIO, PST\_ID

Campos de controle interno\.

Campo NUM\_LOTE

Campo de controle interno, utilizado para o processo de importação automática de SAFX, no produto Tax One\.

MFS59797

__RN01__

__Campo Código da Empresa__

Campo COD\_EMPRESA

Campo de preenchimento __*obrigatório\.*__

*\(registros das tabelas SAFX sem a informação da Empresa são desconsiderados\)*

MFS59797

__RN02__

__Campo Código do Estabelecimento__

Campo COD\_ESTAB

Campo de preenchimento __*obrigatório\.*__

*\(registros das tabelas SAFX sem a informação do Estabelecimento são desconsiderados\)*

MFS59797

__RN03__

__Campo Matriz ou Filial__

Campo IND\_MATRIZ\_FILIAL

Campo de preenchimento __*não obrigatório*__\.

Quando preenchido, o conteúdo deve ser uma das seguintes opções: “M” ou “F”\. Gravado com a opção “F” como default\.

Se for preenchido e inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem: 

*Codigo 913117: “Campo Matriz ou Filial invalido”*

MFS59797

__RN04__

__Campo Classe do Estabelecimento__

Campo COD\_CLASSE

Campo de preenchimento __*não obrigatório\.*__

Quando preenchido, o conteúdo deve ser uma das seguintes opções: “1”, “2”, “3”, “4”, “5”, “10”, “11”, “12”, “13” ou “15”\.

Se for preenchido e inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Codigo 913118: “Campo Classe do Estabelecimento preenchido com informacao invalida”*

MFS59797

__RN05__

__Campo CNPJ__

Campo CGC

Campo de preenchimento __*não obrigatório\.*__

Se o campo for inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

Código 90082: *“Numero de CNPJ informado nao e valido, conforme regras da Secretaria de Fazenda”\.*

__\[MFS741454\]__

Validar o CNPJ podendo ser numérico ou alfanumérico de acordo com o Cálculo do Dígito Verificador, definido na matriz “MTZ\-Regra de Validação do CNPJ\.docx”

MFS59797

__MFS741454__

__RN06__

__Campo Atividade Econômica__

Campo COD\_ATIVIDADE

Campo de preenchimento __*não obrigatório\.*__

Quando informado, deve ser um código existente na Tabela de Atividade Econômica \(TACES01\)

Quando o código informado não existir na TACES01, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

Código *90384*: “*O Campo Codigo de Atividade Economica nao esta cadastrado*”\.

MFS59797

__RN07__

__Campo Inscrição Municipal__

Campo INSC\_MUNICIPAL

Campo de preenchimento __*não obrigatório\.*__

MFS59797

__RN08__

__Campo Inscrição SUFRAMA__

Campo INSC\_SUFRAMA

Campo de preenchimento __*não obrigatório*__\.

MFS59797

__RN09__

__Campo Razão Social__

Campo RAZAO\_SOCIAL

Campo de preenchimento __*obrigatório\.*__

Quando não informado, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 90086: “A Razao Social deve ser preenchida*”\.

MFS59797

__RN10__

__Campo Nome Fantasia__

Campo NOME\_FANTASIA

Campo de preenchimento __*não obrigatório\.*__

MFS59797

__RN11__

__Campo Endereço__

Campo ENDERECO

Campo de preenchimento __*não obrigatório*__\.

MFS59797

__RN12__

__Campo Número do Endereço__

Campo NUM\_ENDERECO

Campo de preenchimento __*não obrigatório\.*__

MFS59797

__RN13__

<a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>

<a id="OLE_LINK32"></a><a id="OLE_LINK33"></a><a id="OLE_LINK34"></a>__Campo Complemento do Endereço__

Campo COMPL\_ENDERECO

Campo de preenchimento __*não obrigatório\.*__

MFS59797

__RN14__

__Campo Bairro__

Campo BAIRRO

Campo de preenchimento __*não obrigatório\.*__

MFS59797

__RN15__

__Campo Cidade__

Campo CIDADE

Campo de preenchimento __*não obrigatório\.*__\.

MFS59797

__RN16__

__Campo Distrito__

Campo DISTRITO

Campo de preenchimento __*não obrigatório\.*__

MFS59797

__RN17__

__Campo Subdistrito__

Campo SUB\_DISTRITO

Campo de preenchimento __*não obrigatório\.*__

MFS59797

__RN18__

__Campo UF__

Campo COD\_ESTADO

Campo de preenchimento __*não obrigatório\.*__

Quando informado, deve ser um código existente na Tabela de Unidades da Federação \(TFIX04\)\.

Quando o código informado não existir na TFIX04 , o registro não será importado, e no log de erros será gravada a seguinte mensagem:

Código 90027 – “*O Codigo da Unidade da Federacao e invalido”*\.

MFS59797

__RN19__

__Campo CEP__

Campo CEP

Campo de preenchimento __*não obrigatório\.*__

MFS59797

__RN20__

__Campo DDD__

Campo DDD

Campo de preenchimento __*não obrigatório\.*__

MFS59797

__RN21__

__Campo Telefone__

Campo TELEFONE

Campo de preenchimento __*não obrigatório\.*__

MFS59797

__RN22__

__Campo Fax__

Campo FAX\.

Campo de preenchimento __*não obrigatório\.*__

MFS59797

__RN23__

__Campo Município__

Campo COD\_MUNICIPIO

Campo de preenchimento __*não obrigatório\.*__

Quando informado, deve ser um código existente na Tabela de Municipios – IBGE \(TACES06\)\. 

Quando o código informado não existir na TACES06, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

Código 90664: “*Codigo do Municipio Invalido*\.”

MFS59797

__RN24__

__Campo Vendas sob Regime Especial __

Campo IND\_VENDA\_AMB

Campo de preenchimento __*não obrigatório\.*__

Campo para tratamento interno preenchido através do menu: Parâmetros do Sistema > Vendas sob Regime Especial > Parâmetros por Estabelecimento do Módulo Básicos > Ferramentas\.

Se o campo for inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

Código 913145: 

“*O Campo IND\_VENDA\_AMB da tabela ESTABELECIMENTO preenchido com informacao invalida\.  Deve ser <S> ou <N>*\.”

MFS59797

__RN25__

__Campo Centralizacao por Estabelecimento__

Campo IND\_DIRF\_CENTRAL

Campo de preenchimento __*não obrigatório\.*__

Campo para tratamento interno preenchido através do menu: Parâmetros > Centralização por Estabelecimento  

Módulo Federal > Obrigações do Tributos Federais\.

Se o campo for inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

Código 913146: 

“*O Campo IND\_DIRF\_CENTRAL da tabela ESTABELECIMENTO preenchido com informacao invalida\.  Deve ser <S> ou <N>*\.”

MFS59797

__RN26__

__Campo Tipo Logradouro__

Campo TP\_LOGRADOURO

Campo de preenchimento __*não obrigatório\.*__

MFS59797

__RN27__

__Campo Quant\. Itens Nota__

Campo ITENS\_NOTA

Campo para tratamento interno,__ não obrigatório\.__

Referenciada no módulo Escrita Fiscal, que já foi descontinuado\.

MFS59797

__RN28__

__Campo Imprime__

Campo IMPRIME

Campo para tratamento interno,__ não obrigatório\.__

Se o campo for inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

Código 913147: 

“*O Campo IMPRIME da tabela ESTABELECIMENTO preenchido com informacao invalida\.  Deve ser <S> ou <N>*\.”

MFS59797

__RN29__

__Campo Mult\. Série__

Campo 'MULT\_SERIE\_S'

Campo para tratamento interno,__ não obrigatório\.__

Se o campo for inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

Código 913148:

“*O Campo 'MULT\_SERIE\_S' da tabela ESTABELECIMENTO preenchido com informacao invalida\. Deve ser <S> ou <N>\.”*

MFS59797

__RN30__

__Campo Número PPVI__

Campo NUM\_PPVI\_SN

Campo para tratamento interno,__ não obrigatório\.__

Se o campo for inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

Código 913149:

“*O Campo ‘NUM\_PPVI\_SN' da tabela ESTABELECIMENTO preenchido com informacao invalida\. Deve ser <S> ou <N>\.”*

MFS59797

__RN31__

__Campo Seq Unico__

Campo SEQ\_UNICO

Campo para tratamento interno,__ não obrigatório\.__

Se o campo for inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

Código 913150:

“*O Campo ‘SEQ\_UNICO' da tabela ESTABELECIMENTO preenchido com informacao invalida\. Deve ser <S> ou <N>\.”*

MFS59797

__RN32__

__Campo Codigo Contábil__

Campo CODIGO\_CONTABIL

Campo para tratamento interno,__ não obrigatório\.__

Referenciado no modulo Escrita Fiscal, que já foi descontinuado\.

MFS59797

__RN33__

__Campo Codigo Produto__

Campo COD\_PRODUTO

Campo para tratamento interno,__ não obrigatório\.__

Se for preenchido e inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 92446: O produto informado nao existe na Tabela de Produtos \(SAFX2013\)\.*

Se não for preenchido, e o campo IND\_PRODUTO da tabela ESTABELECIMENTO estiver preenchido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 92445: O codigo do produto e de preenchimento obrigatorio e nao foi informado   \.*

MFS59797

__RN34__

__Campo Indicador Produto__

Campo IND\_PRODUTO

Campo para tratamento interno, __*não obrigatório*__

Quando preenchido, o conteúdo deve ser uma das seguintes opções: “1”, “2”, “3”, “4”, “5”, “6”, “7” ou “8”\.

Se for preenchido e inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913154: *

*O Campo IND\_PRODUTO da tabela ESTABELECIMENTO preenchido com a informacao invalida\. *

*Deve ser <1>, <2>, <3>, <4>, <5>, <6>, <7> ou <8>\.*

MFS59797

__RN35__

__Campo Indicador ST Nao Contr__

Campo IND\_ST\_NCONTRIB

Campo para tratamento interno, __*não obrigatório\.*__

MFS59797

__RN36__

__Campo Margem ST Nao Contri__

Campo MARGEM\_ST\_NCONTRIB

Campo para tratamento interno, __*não obrigatório\.*__

MFS59797

__RN37__

__Campo Município ISS__

Campo COD\_MUNIC\_ISS

Campo de preenchimento __*não obrigatório\.*__

Quando informado, deve ser um código existente na SAFX2097\.

Quando o código informado não existir na SAFX2097, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 90971: “O Campo Codigo do Municipio de ISS nao esta cadastrado\.”*

MFS59797

__RN38__

__Campo Codigo Tipo Recolhimento__

Campo COD\_TP\_RECOLH

Campo para tratamento interno__, não obrigatório\.__

MFS59797

__RN39__

__Campo Indicador Forma Abat__

Campo IND\_FORMA\_ABAT

Campo para tratamento interno__, não obrigatório\.__

Referenciada nas queries de Relatórios\.

MFS59797

__RN40__

__Campo Indicador Numeração__

Campo IND\_NUMERACAO              

Campo para tratamento interno__, não obrigatório\.__

Referenciada no módulo Escrita Fiscal, que já foi descontinuado

MFS59797

__RN41__

__Campo Email__

Campo EMAIL

Campo de preenchimento __*não obrigatório\.*__

MFS59797

__RN42__

__Campo Utiliza mais de um NBM e/ou mais de uma Insc\. Estadual__

Campo IND\_NBM\_IEST

Campo de preenchimento __*não obrigatório\.*__

MFS59797

__RN43__

__Campo Contribuinte IPI__

Campo IND\_CONTRIB\_IPI

Campo de preenchimento __*não obrigatório\.*__

*      *

MFS59797

__RN44__

__Campo Contribuinte Substituto__

Campo IND\_CONTRIB\_SUB

Campo de preenchimento __*não obrigatório\.*__

MFS59797

__RN45__

__Campo Data Início Atividade__

Campo DAT\_INI\_ATIVIDADE

Campo de preenchimento __*não obrigatório\.*__

Se a data informada, não estiver em formato válido \(aaaammdd\), o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913134: “O Campo de Data Inicio Atividade com formato invalido”*

MFS59797

__RN46__

__Campo Indicador Aprovador__

Campo IND\_APROVADOR      

Campo de preenchimento __*não obrigatório\.*__

Se o campo for inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913151:*

“*O Campo ‘IND\_APROVADOR' da tabela ESTABELECIMENTO preenchido com informacao invalida\. Deve ser <S> ou <N>\.”*     

MFS59797

__RN47__

__Campo Inscrição DF__

Campo INSC\_DF

Campo de preenchimento __*não obrigatório\.*__

MFS59797

__RN48__

__Campo Indicador Imune__

Campo IND\_IMUNE      

Campo de preenchimento __*não obrigatório\.*__

Se o campo for inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913152:*

“*O Campo ‘IND\_IMUNE’ da tabela ESTABELECIMENTO preenchido com informacao invalida\. Deve ser <S> para o campo ISS igual ‘1\-Imune’ ou <N> para as demais opções\.”*                 

MFS59797

__RN49__

__Campo Indicador Isento__

Campo IND\_ISENTO

Campo de preenchimento __*não obrigatório\.*__

Se o campo for inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913153:*

“*O Campo ‘IND\_ISENTO’ da tabela ESTABELECIMENTO preenchido com informacao invalida\. Deve ser <S> para o campo ISS igual ‘4\-Isento’ ou <N> para as demais opções\.”*             

MFS59797

__RN50__

__Campo Escrita Contábil Regular__

Campo IND\_ESCR\_CONTAB

Campo de preenchimento __*não obrigatório\.*__

MFS59797

<a id="_Hlk25589382"></a>__RN51__

__Campo Data Jucemat__

Campo DATA\_JUCEMAT

Campo de preenchimento __*não obrigatório\.*__

Se a data informada, não estiver em formato válido \(aaaammdd\), o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913135: “O Campo de Data Jucemat com formato invalido”*

MFS59797

RN52

__Campo Data Cadastro Sefaz__

Campo DATA\_SEFAZ

Campo de preenchimento __*não obrigatório\.*__

Se a data informada, não estiver em formato válido \(aaaammdd\), o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913136: “O Campo de Data Cadastro Sefaz com formato invalido”*

MFS59797

__RN53__

__Campo Secundário \(CAT 95/03\)__

Campo IND\_SECUNDARIO

Campo de preenchimento __*não obrigatório\.*__

MFS59797

__RN54__

__Campo Estabelecimento sujeito a apuração de IPI com condições estabelecidas em liminares que determinam IPI Sub Judice__

Campo IND\_IPI\_SJ

Campo de preenchimento __*não obrigatório*__\.

MFS59797

__RN55__

__Campo Estabelecimento com IPI Sub Judice sujeito \_as regras de escrituração definidas para a região de Ribeirão Preto\.__

Campo IND\_IPISJ\_REGRA\_RB

Campo de preenchimento __*não obrigatório*__\.

MFS59797

__RN56__

__Campo Data Encerramento__

Campo DT\_ENCERRAMENTO

Campo de preenchimento __*não obrigatório*__\.

Se a data informada, não estiver em formato válido \(aaaammdd\), o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913137: “O Campo de Data Encerramento com formato invalido”*

MFS59797

__RN57__

__Campo Cadastro Específico INSS\-CEI__

Campo CEI\_PORT63

Campo de preenchimento __*não obrigatório\.*__

MFS59797

__RN58__

__Campo Inscrição\-PIS/PASEP/CI/SUS__

Campo INSC\_PORT63

Campo de preenchimento __*não obrigatório*__\.

MFS59797

__RN59__

__Campo Número Threads__

Campo NUM\_THREADS\_MMAG

Campo de preenchimento __*não obrigatório*__

MFS59797

__RN60__

__Campo Caixa Postal__

Campo CX\_POSTAL

Campo de preenchimento __*não obrigatório*__\.

MFS59797

__RN61__

__Campo Cep\-Caixa Postal__

Campo NUM\_CEP\_CX\_POSTAL

Campo de preenchimento __*não obrigatório*__\.

MFS59797

__RN62__

__Campo Benefício Fiscal do ICMS__

Campo COD\_BENEF\_ICMS

Campo de preenchimento __*não obrigatório*__\.

Quando preenchido, o conteúdo deve ser uma das seguintes opções:“DF001”, “PE001”, “PE002”, “PE003”, “SE001”, “TO001”, “TO002” ou “TO003”\.

Se for preenchido e inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913121: “Campo Beneficio Fiscal do ICMS preenchido com informacao invalida”\.*

MFS59797

__RN63__

__Campo Benefício Fiscal do ISSQN__

Campo COD\_BENEF\_ISS

Campo de preenchimento __*não obrigatório*__\.

Quando preenchido, o conteúdo deve a opção: “DF001”\.

Se for preenchido e inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Codigo 913122: “Campo Beneficio Fiscal do ISSQN preenchido com informacao invalida”\.*

MFS59797

__RN64__

__Campo Número Protocolo Encerramento__

Campo NUM\_PROTOCOLO

Campo de preenchimento __*não obrigatório*__\.

MFS59797

__RN65__

__Campo Data Protocolo__

Campo DATA\_PROTOCOLO

Campo de preenchimento__ não obrigatório\.__

Se a data informada, não estiver em formato válido \(aaaammdd\), o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913138: “O Campo de Data Protocolo com formato invalido”*

MFS59797

__RN66__

__Campo Data Cisão__

Campo DATA\_CISAO

Campo de preenchimento__ não obrigatório\.__

Se a data informada, não estiver em formato válido \(aaaammdd\), o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913139: “O Campo de Data Cisao com formato invalido”*

MFS59797

__RN67__

__Campo Data Fusão__

Campo DATA\_FUSAO

Campo de preenchimento__ não obrigatório\.__

Se a data informada, não estiver em formato válido \(aaaammdd\), o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913140: “O Campo de Data Fusao com formato invalido”*

MFS59797

__RN68__

__Campo Data Incorporação__

Campo DATA\_INCORPORACAO

Campo de preenchimento__ não obrigatório\.__

Se a data informada, não estiver em formato válido \(aaaammdd\), o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913141: “O Campo de Data Incorporacao com formato invalido”*

MFS59797

__RN69__

__Campo Data Validade Inicial Atividade __

Campo DAT\_VALIDADE\_INI\_ATIVIDADE

Campo de preenchimento __não obrigatório\.__

Se a data informada, for maior que a data de validade inicial do estabelecimento, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913144*: 

“*A data de validade do estabelecimento e anterior a data de inicio de vigencia do codigo de atividade economica informada*\.”

MFS59797

__RN70__

__Campo Tipo de Atividade__

Campo IND\_ATIVIDADE

Campo de preenchimento __obrigatório\.__

Deve ser preenchido com: “0”, “1”, “2”, “3”, “4” ou “5”\.

Quando não preenchido, ou inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913123: “Campo Tipo de Atividade nao esta preenchido ou preenchido com informacao invalida”\.*

MFS59797

__RN71__

__Campo Tipo de Apuração do ICMS utilizada no Mastersaf__

Campo IND\_APUR\_ICMS

Campo de preenchimento__ não obrigatório\.__

Quando preenchido, o conteúdo deve ser uma das seguintes opções: “1”, “2”, “3” ou “4”\.

Se for preenchido e inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913124: “Campo Tipo de Apuracao do ICMS utilizada no Mastersaf preenchido com informacao invalida”\.*

MFS59797

__RN72__

__Campo Tipo de Apuração do IPI utilizada no Mastersaf__

Campo IND\_APUR\_IPI

Campo de preenchimento__ não obrigatório\.__

Quando preenchido, o conteúdo deve ser uma das seguintes opções: “1”, “2”, “3” ou “4”\.

Se for preenchido e inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Codigo 913125: “Campo Tipo de Apuracao do IPI no Mastersaf preenchido com informacao invalida”\.*

MFS59797

__RN73__

__Campo Estabelecimento obrigado a geração do arquivo do Convenio ICMS 115/03__

Campo IND\_CONV\_ICMS

Campo de preenchimento__ não obrigatório\.__

Quando preenchido, o conteúdo deve ser uma das seguintes opções: “S” ou “N”;

Se for preenchido e inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913126: *

*“Campo Estabelecimento obrigado a geracao do arquivo do Convenio ICMS 115/03 preenchido com informacao invalida”\.*

MFS59797

__RN74__

__Campo ISS__

Campo IND\_ISS

Campo de preenchimento__ não obrigatório\.__

Quando preenchido, o conteúdo deve ser uma das seguintes opções: “01”, “02”, “03”, “04”, “05”, “06”, “07”, “08”, “09”, “10”, “11”, “12”, “13” ou “14”\.

Se for preenchido e inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913127*: 

“*Campo ISS preenchido com informacao invalida”\.*

MFS59797

__RN75__

__Campo Atividade com Base de Cálculo Reduzida__

Campo IND\_ATIV\_BASE\_CALC\_REDUZ

Campo de preenchimento__ não obrigatório\.__

Quando preenchido, o conteúdo deve ser uma das seguintes opções: “01”, “02”, “03”, “04” ou “05”\.

Se for preenchido e inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Codigo 913128: *

*“Campo  Atividade com Base de Calculo Reduzida preenchido com informacao invalida”\.*

MFS59797

__RN76__

__Campo Tipo de Assinante__

Campo TIPO\_ASSINANTE

Campo de preenchimento__ não obrigatório\.__

Quando preenchido, o conteúdo deve ser uma das seguintes opções: “1”, “2”, “3”, “4”, “5” ou “6”\.

Se for preenchido e inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913129*: 

“*Campo Tipo de Assinante preenchido com informacao invalida”\.*

MFS59797

__RN77__

__Campo Natureza da Pessoa Jurídica__

__\[MFS829924\]__ Inclusão da opção 05 

Campo NAT\_PESSOA\_JUR

Campo de preenchimento__ não obrigatório\.__

Quando preenchido, o conteúdo deve ser uma das seguintes opções: “00”, “01”, “02”, “03”, “04” ou “05”\.

Se for preenchido e inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913130: *

“*Campo Natureza da Pessoa Juridica preenchido com informacao invalida”\.*

MFS59797

MFS829924

__RN78__

__Campo Codigo da Instituição Financeira__

Campo COD\_INST\_FINANC

Campo de preenchimento__ não obrigatório\.__

MFS59797

__RN79__

__Campo Contribuinte Equiparado a Const\. Civil__

Campo IND\_CONTRIB\_EQ\_CCIVIL

Campo de preenchimento__ não obrigatório\.__

MFS59797

__RN80__

__Campo Alvará__

Campo NUM\_ALVARA

Campo de preenchimento__ não obrigatório\.__

MFS59797

__RN81__

__Campo Tipo Instituição Financeira__

Campo IND\_INST\_FINANCEIRA

Campo de preenchimento não__ obrigatório\.__

Quando preenchido, o conteúdo deve ser uma das seguintes opções: “1”, ”3”, “5” ou “7”\.

Se for preenchido e inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem: 

*Código 913131: *

*“Campo Tipo Instituicao Financeira preenchido com informacao invalida”\.*

MFS59797

__RN82__

__Campo Código Indicador da Incidencia de Tributação da Contribuição Previdenciaria__

Campo IND\_REG\_APUR\_CONT\_PREV

Campo de preenchimento__ não obrigatório\.__

Quando preenchido, o conteúdo deve ser uma das seguintes opções: “0”, “1” ou “2”\.

Se for preenchido e inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913132: *

“*Campo Codigo Indicador da Incidencia de Tributacao da Contribuicao Previdenciaria preenchido com informacao invalida”\.*

MFS59797

__RN83__

__Campo Certificado Digital__

Campo CERTIFICADO\_DIGITAL

Campo de preenchimento__ não obrigatório\.__

MFS59797

__RN84__

__Campo Agente Regulado Informante__

Campo COD\_ARI\_ANP

Campo de preenchimento__ não obrigatório\.__

MFS59797

__RN85__

__Campo Código da Instalação 1__

Campo COD\_INSTAL\_ANP

Campo de preenchimento__ não obrigatório\.__

MFS59797

__RN86__

__Campo Complemento Endereço__

Campo COMPL\_ENDERECO\_EFD

Campo de preenchimento__ não obrigatório\.__

MFS59797

__RN87__

__Campo Tipo de Atividade Financeira__

Campo IND\_ATIV\_FINANCEIRA

Campo de preenchimento__ não obrigatório\.__

Quando preenchido, o conteúdo deve ser uma das seguintes opções: “0”, “1”, “2”, “3”, “4”, “5” ou “6”\.

Se for preenchido e inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913133: *

“*Campo Tipo de Atividade Financeira preenchido com informacao invalida”\.*

MFS59797

__RN88__

__Campo Informação Complementar__

Campo DSC\_INF\_COMPLEMENTAR

Campo de preenchimento__ não obrigatório\.__

MFS59797

__RN89__

__Campo Razão Social Complementar__

Campo RAZAO\_SOCIAL\_COMPL

Campo de preenchimento__ não obrigatório\.__

MFS59797

__RN90__

__Campo Bairro Complementar__

Campo BAIRRO\_COMPL 

Campo de preenchimento__ não obrigatório\.__

MFS59797

__RN91__

__Campo Código do Mobiliário__

Campo COD\_IMOBILIARIO

Campo de preenchimento__ não obrigatório\.__

MFS59797

__RN92__

__Campo Data Transf\. de Sede__

Campo DAT\_TRANSF\_SEDE

Campo de preenchimento__ não obrigatório\.__

Se a data informada, não estiver em formato válido \(aaaammdd\), o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913142: *

“*O Campo de Data Transf Sede com formato invalido”*

MFS59797

__RN93__

__Campo Data Transformação__

Campo DAT\_TRANSF

Campo de preenchimento__ não obrigatório\.__

Se a data informada, não estiver em formato válido \(aaaammdd\), o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913143:*

 “*O Campo de Data Transformacao com formato invalido”*

MFS59797

__RN94__

__Campo Classificação de Contribuintes do IPI \(EFD, registro 0002\)__

Campo IND\_CLAS\_ESTAB

Campo de preenchimento __*não obrigatório*__\.

Quando preenchido, o conteúdo deve ser uma das seguintes opções: “00”, “01”, “02”, “03”, “04”, “05”, “06”, “07”, “08” ou “09”\. 

Se for preenchido e inválido, o registro não será importado, e no log de erros será gravada a seguinte mensagem:

*Código 913120: *

*“Campo Classificacao de Contribuintes do IPI \(EFD, registro 0002\) preenchido com informacao invalida”\.*

MFS59797

__RN95__

__Campo Natureza Jurídica__

Campo COD\_ NAT\_JUR

Tamanho: 4 posições

Tipo: Alfanumérico

Campo de preenchimento __*não obrigatório*__\.

MFS\-79885

__RN96__

__Campo Reservado 1__

Campo DSC\_RESERVADO1

Tamanho: 50 posições

Tipo: Alfanumérico

Campo de preenchimento __*não obrigatório*__\.

MFS772966

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

