# MTZ_REINF_Relatorio_Validacao_Retencoes_Previdenciarias_Formato_XLS

- **Fonte:** MTZ_REINF_Relatorio_Validacao_Retencoes_Previdenciarias_Formato_XLS.docx
- **Modificado:** 2025-11-24
- **Tamanho:** 103 KB

---

<a id="OLE_LINK5"></a><a id="OLE_LINK6"></a><a id="OLE_LINK7"></a><a id="OLE_LINK8"></a>

THOMSON REUTERS

Módulo EFD Reinf 

Relatório Previdenciário

__Localização__: Menu SPED, Módulo: EFD – REINF / Validação de Retenções Previdenciárias à Formato\_XLS

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS901529

Rogério Ohashi

Criação Relatório de Validação de Retenções Previdenciárias em Formato XLS

Sumário

[1\.	REGRAS DOS CAMPOS	3](#_Toc519169829)

[2\.	REGRAS DE GERAÇÃO DO RELATÓRIO	8](#_Toc519169830)

[2\.1\.	Layout do Relatório	14](#_Toc519169831)

# <a id="_Toc350763252"></a><a id="_Toc427766285"></a><a id="_Toc453687761"></a><a id="_Toc519169829"></a>REGRAS DOS CAMPOS 

__Localização da tela:__ Menu: SPED, Módulo: EFD\-REINF, item de menu Relatórios > Previdenciário > Validação de Retenção Previdenciária

__Título da tela: __Retenções Previdenciárias

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Período

Data

S

S

Formato: MM/AAAA 

Default: Habilitado

Local para digitação do período inicial e final de referencia da geração do relatório, no formato de DD/MM/AAAA\. 

Este campo servirá para parametrização da Data que o sistema deverá considerar para seleção das informações para a criação do relatório\.

__Obs:__ No campo do Período final, o usuário deverá informar um período maior ou igual ao período inicial\. Caso informe um período menor do que o período inicial retornar a mensagem: 

*“O período final informado deve ser maior ou igual ao período inicial”\.*

MFS18748

Tipo do Relatório

ComboBox

S

S

Default: Habilitado

Permitir que o usuário informe qual o tipo de relatório será emitido entre as opções: 

- Listagem de Serviços Sujeitos à Retenção Previdenciária;
- Listagem de Serviços com Retenção destacada, mas sem vinculação com um Tipo de Serviço; 
- Serviços com Valor de Retenção Previdenciária e com Processo indicado;
- Serviços sem Valor de Retenção Previdenciária e sem Processo indicado; 
- Listagem com Base de INSS maior que o Valor Total Bruto
- Cálculo da Base de INSS pela Alíquota diferente do Valor de INSS informado
- Listagem de Alíquota de INSS não válida de acordo com a Legislação

MFS18748

MFS14863

Origem

Checkbox

S

S

Default: Entrada de Serviço

Permitir que o usuário informe qual origem que será emitido o relatório, Serão listadas as seguintes opções:

- <a id="_Hlk519171169"></a>Entrada de Serviço
- Saída de Serviço

O usuário só poderá escolher uma das opções\.

MFS18748

Multiempresas

Checkbox

N

S

Default: Desmarcado

Na abertura da tela esta opção aparecerá sempre desmarcada\.

MFS18748

Estabelecimentos

CheckBox

S

S

Default: não selecionado

Este campo exibe todos os estabelecimentos da empresa que acessou o módulo do EFD\-Reinf\. 

A partir da inclusão do parâmetro “*Geração Multiempresa*”, a lista passou a funcionar da seguinte forma:

\- Caso o parâmetro “*Geração Multiempresa*” estiver __desmarcado__:

Na lista será demonstrado apenas o código da empresa, código e a razão social de cada estabelecimento, somente da empresa que acessou o módulo\.

XXXXX / XXXXX\-XXXXXXXXXXXXXXXXX

\(cód\. empresa \+ cód\. e razão social do estabelecimento\)\.

    

\- Caso o parâmetro “*Geração Multiempresa*” estiver __marcado__:

Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento, mas neste caso serão mostradas todas as empresas:

XXXXX / XXXXX\-XXXXXXXXXXXXXXXXX

\(cód\. empresa \+ cód\. e razão social do estabelecimento\)

       

__Obs: __No caso da geração multiempresa, as regras da geração do relatório não se modificam\. A diferença é apenas na chamada, já que na lista de estabelecimentos para geração do relatório existirão estabelecimentos de empresas distintas\.

O usuário deverá escolher obrigatoriamente ao menos um estabelecimento para a geração do relatório\.  Por ser um campo obrigatório, quando não informado, retornar a mensagem: “Estabelecimento deve ser Selecionado”\.

Como facilitador, poderão ser utilizadas as opções “Selecionar todos” e “Desmarcar todos”\.

MFS18748

Selecionar Todos

Botão

N

S

Default: desabilitado

Neste campo é possível selecionar todos os estabelecimentos demostrados no campo Estabelecimento\.

Quando acionado, muda o status dos códigos de estabelecimento que não estão selecionados para selecionado\.

MFS18748

Desmarcar Todos

Botão

N

S

Default: desabilitado

Neste campo é possível desmarcar todos os estabelecimentos que estão selecionados no campo Estabelecimento\.

Quando acionado, muda o status dos códigos de estabelecimento que estão selecionados para não selecionado\.

MFS18748

# <a id="_Toc427766287"></a><a id="_Toc453687763"></a><a id="_Toc519169830"></a>REGRAS DE GERAÇÃO DO RELATÓRIO 

__Regra Geral: __ 

Todos os campos e colunas do relatório deverão refletir na opção Salvar Como, ou seja, todos os dados contidos no relatório devem compor a todas as opções disponíveis para salvar o relatório\. 

 

__Origem das informações para geração:__  

Para geração deste relatório, serão consideradas informações das seguintes origens: 

 

- __SAFX07 __\- Tabela dos Documentos Fiscais \(Capa\);  
- __SAFX08 __\- Tabela dos Documentos Fiscais de Mercadorias e Produtos \(Itens\); 
- __SAFX09 __\- Tabela dos Documentos Fiscais de Serviços \(Itens\); 

 

A recuperação das notas do relatório irá obedecer ao campo ‘Origem’ informado na tela de emissão do relatório, ou seja: 

 

- Caso o usuário informar a opção = Entrada de Serviço, nós iremos considerar os documentos que possuam o campo MOVTO\_E\_S <> 9 e o campo COD\_CLASS\_DOC\_FIS = "1" ou "2" ou “3”; 
- Caso o usuário informar a opção = Saída de Serviço, nós iremos considerar os documentos que possuam o campo MOVTO\_E\_S = 9 e o campo COD\_CLASS\_DOC\_FIS = "2” ou “3”; 

 

__Regra de apresentação de serviços/repasse parametrizados em múltiplos estabelecimentos:__ 

  

Caso um mesmo serviço e/ou tipo de repasse esteja parametrizado em mais de um estabelecimento, como por exemplo no estabelecimento Centralizador e em um ou mais estabelecimentos Centralizados, o relatório deverá apresentar a nota fiscal correspondente multiplicada conforme o número de parametrizações existentes para o serviço/repasse nos estabelecimentos envolvidos\.  

Ou seja, se o serviço 0001 estiver parametrizado tanto no estabelecimento Centralizador quanto em um estabelecimento Centralizado, a mesma nota fiscal será exibida duas vezes no relatório, uma para cada estabelecimento, considerando as respectivas parametrizações\.

__\- OBS\.: Para a geração de todos os relatórios, não serão considerados documentos Cancelados\.__

__Regra de seleção dos Relatórios: __

Deve existir na tela de geração de relatório, quatro opções para o relatório previdenciário, conforme critérios de geração de cada um deles como descrito

abaixo\. O usuário poderá escolher uma das seguintes opções de geração possíveis do relatório: 

\-  “Listagem de Serviços Sujeitos à Retenção Previdenciária”;

\-  “Listagem de Serviços com Retenção destacada, mas sem vinculação com um Tipo de Serviço”;

\-  “Serviços com Valor de Retenção Previdenciária e com Processo indicado”;

\-  “Serviços sem Valor de Retenção Previdenciária e sem Processo indicado”\.

\-  “Listagem com Base de INSS maior que o Valor Total Bruto”;

\-  “Cálculo da Base de INSS pela Alíquota diferente do Valor de INSS informado”;

\-  “Listagem de Alíquota de INSS não válida de acordo com a Legislação”\.

__1 \- Nome do relatório:  Listagem de Serviços Sujeitos à Retenção Previdenciária__

\- Este relatório servirá para listar os registros da SAFX07 que tenham itens de Serviço/Produto associados \(SAFX08/SAFX09\) cujo código de serviço tenha sido indicado na parametrização de Identificação do Tipo de Serviço ou Identificação do Tipo de Repasse; No caso de Produto \(SAFX08\) serão recuperadas APENAS as notas fiscais cujo COD\_MODELO seja igual a ‘07’ ou ‘67’

\- Devem ser considerados os registros de NFs de Entrada da SAFX07/SAFX08/SAFX09 \(inclusive notas mistas\), cuja Data de Emissão compreenda o período parametrizado na tela de emissão do relatório e que sejam do estabelecimento indicado pelo usuário, além dos critérios indicador no item anterior;

__Obs\.: Ao final do relatório deve ser realizada uma totalização dos valores por Tipo de Serviço, conforme indicado na parametrização de__

__Identi ficação do Tipo de Serviço ou Identificação do Tipo de Repasse \+ Alíquota \(o campo Alíquota não deve ser totalizado\);__

__2 \- Nome do relatório: Listagem de Serviços com Retenção destacada, mas sem vinculação com um Tipo de Serviço__

\- Este relatório servirá para listar os registros da SAFX07 que tenham itens de Serviço/Produto associados \(SAFX09/SAFX08\) cujo código de serviço __não tenha__ sido indicado na parametrização de Identificação do Tipo de Serviço <a id="_Hlk533148357"></a>ou Identificação do Tipo de Repasse, mas que tenha Valor de INSS Retido maior que zero; No caso de Produto \(SAFX08\) as notas fiscais deverão ser COD\_MODELO seja igual a ‘07’ ou ‘67’ além do Valor de INSS Retido maior que zero\.

\- Devem ser considerados os registros de NFs de Entrada da SAFX07/ SAFX08/SAFX09 \(inclusive notas mistas\), cuja Data de Emissão compreenda o período

parametrizado na tela de emissão do relatório e que sejam do estabelecimento indicado pelo usuário, além dos critérios indicador no item anterior;

__3 \- Nome do relatório: Serviços com Valor de Retenção Previdenciária e com Processo indicado__

\- Este relatório servirá para listar os registros da SAFX07 que tenham itens de Serviço/Produto associados \(SAFX08/SAFX09\) cujo código de serviço tenha sido indicado na parametrização de Identificação do Tipo de Serviço ou Identificação do Tipo de Repasse, que tenha o campo Valor do INSS maior que zero E que tenha o campo Número do Processo preenchido; No caso de Produto \(SAFX08\) as notas fiscais também deverão ser COD\_MODELO seja igual a ‘07’ ou ‘67’\.

\- Devem ser considerados os registros de NFs de Entrada da SAFX07/SAFX08/SAFX09 \(inclusive notas mistas\), cuja Data de Emissão compreenda o período parametrizado na tela de emissão do relatório e que sejam do estabelecimento indicado pelo usuário, além dos critérios indicador no item anterior;

__4 \- Nome do relatório: Serviços sem Valor de Retenção Previdenciária e sem Processo indicado__

\- Este relatório servirá para listar os registros da SAFX07 que tenham itens de Serviço/Produto associados \(SAFX08/SAFX09\) cujo código de serviço tenha sido indicado na parametrização de Identificação do Tipo de Serviço ou Identificação do Tipo de Repasse, que tenha o campo Valor do INSS __igual a zero__ e que o campo Número do Processo __não tem sido__ preenchido; No caso de Produto \(SAFX08\) as notas fiscais também deverão ser COD\_MODELO seja igual a ‘07’ ou ‘67’\.

\- Devem ser considerados os registros de NFs de Entrada da SAFX07/SAFX08/SAFX09 \(inclusive notas mistas\), cuja Data de Emissão compreenda o período parametrizado na tela de emissão do relatório e que sejam do estabelecimento indicado pelo usuário, além dos critérios indicador no item anterior;

__ 	\[MFS14863\]__

__5 \- Nome do relatório: Listagem com Base de INSS maior que o Valor Total Bruto__

\- Este relatório servirá para listar os registros da SAFX07 que tenham itens de Serviço/Produto associados \(SAFX08/SAFX09\) cujo código de serviço tenha sido indicado na parametrização de Identificação do Tipo de Serviço ou Identificação do Tipo de Repasse, que tenha o campo Base de INSS \(VLR\_BASE\_INSS SAFX08/09\) __maior __que o campo Valor Total Bruto \(VLR\_TOT\_NOTASAFX07\)\. No caso de Produto \(SAFX08\) as notas fiscais também deverão ser COD\_MODELO seja igual a ‘07’ ou ‘67’\. 

\- Devem ser considerados os registros de NFs de Entrada da SAFX07/SAFX08/SAFX09 \(inclusive notas mistas\), cuja Data de Emissão compreenda o período parametrizado na tela de emissão do relatório e que sejam do estabelecimento indicado pelo usuário, além dos critérios indicador no item anterior;

__6 \- Nome do relatório: Cálculo da Base de INSS pela Alíquota diferente do Valor de INSS informado__

\- Este relatório servirá para listar os registros da SAFX07 que tenham itens de Serviço/Produto associados \(SAFX08/SAFX09\) cujo código de serviço tenha sido indicado na parametrização de Identificação do Tipo de Serviço ou Identificação do Tipo de Repasse, que o resultado do cálculo da Base de INSS \* Alíquota \(VLR\_BASE\_INSS \* VLR\_ALIQ\_INSS SAFX08/09\) seja __diferente__ do valor encontrado no campo Valor do INSS \(VLR\_INSS\_RETIDO SAFX08/09\)__ __informado; No caso de Produto \(SAFX08\) as notas fiscais também deverão ser COD\_MODELO seja igual a ‘07’ ou ‘67’\.

\- Devem ser considerados os registros de NFs de Entrada da SAFX07/SAFX08/SAFX09 \(inclusive notas mistas\), cuja Data de Emissão compreenda o período parametrizado na tela de emissão do relatório e que sejam do estabelecimento indicado pelo usuário, além dos critérios indicador no item anterior;

__7 \- Nome do relatório: Listagem de Alíquota de INSS não válida de acordo com a Legislação __

\- Este relatório servirá para listar os registros da SAFX07 que tenham itens de Serviço/Produto associados \(SAFX08/SAFX09\) cujo código de serviço tenha sido indicado na parametrização de Identificação do Tipo de Serviço ou Identificação do Tipo de Repasse, que o valor da Alíquota de INSS \(VLR\_ALIQ\_INSS SAFX08/09\) não seja uma alíquota válida de acordo com a legislação \(Alíquotas válidas: 3,5 % ou 11%\); No caso de Produto \(SAFX08\) as notas fiscais também deverão ser COD\_MODELO seja igual a ‘07’ ou ‘67’\.

\- Devem ser considerados os registros de NFs de Entrada da SAFX07/SAFX08/SAFX09 \(inclusive notas mistas\), cuja Data de Emissão compreenda o período parametrizado na tela de emissão do relatório e que sejam do estabelecimento indicado pelo usuário, além dos critérios indicador no item anterior;

\- Para todas as possibilidades de geração do relatório previdenciário, devem ser exibidos os seguintes campos no relatório:

__\[MFS21682\]__

- 
	- 
		- 
			- Estabelecimento
			- Tipo do Documento
			- Indicador \+ Código PFJ
			- CNPJ da PFJ
			- Número do Documento Fiscal
			- Série / Subsérie do Documento Fiscal
			- Data de Emissão
			- Data Fiscal
			- Classificação do Documento Fiscal
			- Código Serviço/Produto
			- Valor Total do Documento Fiscal
			- Valor Total Serviços
			- Valor Base INSS
			- Valor Alíquota INSS
			- Valor INSS Retido
			- Tipo do Processo Principal
			- Número do Processo Principal
			- Tipo do Processo Adicional
			- Número do Processo Adicional

\- Se de acordo com os critérios informados, caso não existam informações recuperadas, o relatório será gerado com sua estrutura, porém será exibida a 

mensagem __“NÃO EXISTEM INFORMAÇÕES PARA OS DADOS INFORMADOS”__ no relatório\.

\- A partir dos dados recuperados, conforme descrito na Origem das informações para geração e Regra de Seleção, será gerado o relatório conforme layout anexo\. Ver layout do relatório na planilha anexa\.

__Campo/Coluna__

__Tipo__

__Formato/Default__

__Regra__

__MFS/CH__

__Dados do Cabeçalho__

Data

Data

DD/MM/AAAA às HH:MM:SS hs

Data de emissão e hora do relatório

MFS7084

Empresa

Texto

Razão social da empresa\.

MFS7084

Página

Numérico

Número da página sequencial do relatório

MFS7084

Filial

Texto

Código e a razão social do estabelecimento em questão \(estabelecimento informado em tela\)\.

MFS7084

CNPJ

Alfanumérico

Deve exibir o CNPJ do Estabelecimento\.

MFS7084

Título

Texto

Título do relatório

MFS7084

Período 

Numérico

Formato: DD/MM/AAAA

Período de Referência da geração do relatório\. Essa informação será recuperada de acordo com o campo “Período” da tela de Geração\.

MFS7084

__Corpo do Relatório __

Estabelecimento

Alfanumérico

Nesta coluna deve exibir o estabelecimentos selecionado na tela de geração\.

MFS7084

Tipo do Documento

Alfanumérico

Deve exibir o Tipo de Documento do campo COD\_DOCTO da SAFX08/SAFX09\.

MFS7084

MFS16773

                                                       Indicador \+ Cod\. Pessoa Jurídica

Alfanumérico

Deve exibir o Indicador \+ Cod\. Pessoa Jurídica, campo IND\_FIS\_JUR da SAFX07\.

Serão considerados apenas as Pessoas Jurídicas ou seja, código Pessoa Física/ Jurídica com 14 posições\.

MFS7084

MFS17891

                                                       CNPJ da Pessoa Jurídica

Alfanumérico

Deve exibir o CNPJ Pessoa Jurídica, campo CPF\_CGC da SAFX04 que corresponde ao Indicador \+ Cod\. Pessoa Jurídica da SAFX07 do campo Indicador \+ Cod\. Pessoa Jurídica\.

Serão considerados apenas as Pessoas Jurídicas, ou seja, CPF\-CGC Pessoa Física/ Jurídica com 14 posições\.

MFS21682

Número Documento

Alfanumérico

Deve exibir o número de documento do campo NUM\_DOCFIS da tabela SAFX07

MFS7084

MFS12751

Série/SubSérie

Numérico 

Alfanumérico

 Deve exibir a série  e subSérie do campo SERIE\_DOCFIS e SUB\_SERIE\_DOCFIS da tabela SAFX07

MFS7084

MFS12751

Data Emissão

Data

Formato: DD/MM/AAAA

Nesta coluna deve exibir a data de Emissão, referente ao campo DATA\_EMISSAO da tabela SAFX07\.

MFS7084

Data Fiscal

Data

Formato: DD/MM/AAAA

Nesta coluna deve exibir a data de Emissão, referente ao campo DATA\_FISCAL da tabela SAFX08/SAFX09\.

MFS7084

MFS12751

MFS16773

Classificação do Documento Fiscal 

Numérico 

Alfanumérico

Deve exibir a classificação do documento fiscal, campo COD\_CLASS\_DOC\_FIS da tabela SAFX07\.

MFS7084

                                                       Código Serviço/Produto

Alfanumérico

Deve exibir o Código do Serviço ou Produto \+ Descrição respectiva, campo COD\_SERVICO da SAFX09 ou COD\_PRODUTO da SAFX08\.

Caso Serviço, a descrição correspondente ao código será recuperada da tabela SAFX2018\.

Caso Produto, a descrição correspondente ao código será recuperada da tabela SAFX2013\.

MFS15748

Valor Total do Documento Fiscal

Numérico 

Alfanumérico

Deve exibir o valor total do documento fiscal, campo VLR\_TOT\_NOTA da tabela SAFX07\.

MFS7084

Valor Serviços

Numérico

Este campo deve informar o valor do serviço destacados na nota\. Campo VLR\_ITEM/VLR\_SERVICO da tabela SAFX08/SAFX09\.

MFS7084

MFS12751

MFS16773

Valor Base INSS

Numérico

Este campo deve informar o valor Base do INSS, campo VLR\_BASE\_INSS da tabela SAFX08/SAFX09\.

MFS7084

MFS12751

MFS16773

Valor Alíquota INSS

Numérico

Este campo deve informar o valor da alíquota do INSS, campo VLR\_ALIQ\_INSS da tabela SAFX08/SAFX09\.

MFS7084

MFS12751

MFS16773

Valor INSS Retido

Numérico

Este campo deve informar o valor do INSS retido, campo VLR\_INSS\_RETIDO da tabela SAFX08/SAFX09\.

MFS7084

MFS12751

MFS16773

Tipo do Processo Principal

Numérico 

Alfanumérico

Este campo deve informar o tipo de processo referente ao campo IND\_TP\_PROC\_ADJ\_PRINC da tabela SAFX08/SAFX09\.

MFS7084

MFS12751

MFS16773

MFS17634

Número do Processo Principal

Numérico 

Alfanumérico

Este campo deve informar o número do processo do campo NUM\_PROC\_ADJ\_PRINC da tabela SAFX08/SAFX09\.

MFS7084

MFS12751

MFS16773

MFS17634

Tipo do Processo Adicional

Numérico 

Alfanumérico

Este campo deve informar o tipo de processo referente ao campo IND\_TP\_PROC\_ADJ\_ADIC da tabela SAFX08/SAFX09\.

MFS17634

Número do Processo Adicional

Numérico 

Alfanumérico

Este campo deve informar o número do processo do campo NUM\_PROC\_ADJ\_ADIC da tabela SAFX08/SAFX09\.

MFS17634

## <a id="_Toc427766288"></a><a id="_Toc453687764"></a><a id="_Toc519169831"></a>Layout do Relatório

__Exemplo do Relatório:__

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABLwAAAE2CAIAAADkrhx0AAAAAXNSR0IArs4c6QAAXV5JREFUeF7tnT123TqWqKnqLo1Eai/3ag3gqEYg1Q0cOXRnR2FLgUNH7uwGUoVW9m6oyIGfNILWGYB6PS+3NJBWSav08EOCIAmS4D9IfgxsHRI/e38ASGzuDXDv+fn5T3/6U1Q43t7eiifFmbLzzsSchAAEIAABCEAAAhCAAAQgAIHxCezt7TkrLTtfJuE//vGPvZeXl3/+538eXwdqhAAEIAABCEAAAhCAAAQgAIHACby+vjp8jIELjXgQgAAEIAABCEAAAhCAAAQgMBoBjMbRUFMRBCAAAQhAAAIQgAAEIACB+RHAaJxfmyExBCAAAQhAAAIQgAAEIACB0QhgNI6GmoogAAEIQAACEIAABCAAAQjMjwBG4/zaDIkhAAEIQAACEIAABCAAAQiMRgCjcTTUVAQBCEAAAhCAAAQgAAEIQGB+BP7Edxfn12hIDAEIQAACEIAABCAAAQhAYCwCeBrHIk09EIAABCAAAQhAAAIQgAAEZkgAo3GGjYbIEIAABCAAAQhAAAIQgAAExiKw9/e///3Pf/5zRXV7e3tjCUM9EIAABCAAAQhAAAIQgAAEINA/gdbLEl9fX/E09t8elAgBCEAAAhCAAAQgAAEIQGAxBHw9ja0N08WQQhEIQAACEIAABCAAAQhAAAKzI6BDR1sbdHgaZ9fiCAwBCEAAAhCAAAQgAAEIQGBUAnxyY1TcVAYBCEAAAhCAAAQgAAEIQGBeBFjTOK/2QloIQAACEIAABCAAAQhAAAKjEsBobI776ep4b+/srnlGckAAAhCAAAQgAIGVE7g729s7vnpaOQXUh8DMCDQ0GpW9ZI4qw0mkbGJXmYIzmXLmmfipbjLFxPL+o470JpQkNpeMnedVl8lW1OLg/P52e/3V73anKsvfGp0nZ9ZzEBcCEIAABCAAAQiUEUjnX/n52dfr7e39+UE5uj7ezhcne32dkXL3ISFdBwIzI/D8/Cw20qk4tD5xgsfLTRRtb+Uv9efm8tGZ1UpXXbq+KpOrom63aZmqDHHo6uQhroofxcQyV3LFiKQTJ5e0uLIon7pMYpPdR4tyEnlMlexaV0VGCEAAAhCAAAQgEAYBa0o3/rSnONnr60wyA85MUMMgjhQQ8DXompN6eXlp6Gm0LOKD8y/baHfzQ4YXpG+TpE9NvH45vNhF0fWpdrFlr8a/bQfe04+bXXT0TrxzOny/iXY/H9UrHFWGfTz9eti8P3QkPvkmdP92otOqckQBKnGUuRQ9/HryqUul2X4QBWaz6wry6lieT/Euze1evfkUe0Lty7mTqlx5Xb++Okudp1c5P2ptAlNUiWy2w7iJP3hmL0QQFwIQgAAEIACB6QkcvDuK9PSuahKlZz7pRCiZER2fncVhbsmUpcXEsjj9a3fGOUGdnjASQGB4Au2NxtTCuzs7fVAeR/FSSVqRInwzcdWJ6IP8VYdOjz8z5qEw7WSixE+YZBCjO/r424E7sboPHV4c3cbGY5zYVKZuDZvS7Pm6hL/z4au283JGVVGdp6tPFzvtSxQAnGGru6Mv8Zsp67LzpBH4OvoQZ9ld3LyXhQumu4vfzVLK2gTKdHbJ5iHw8B2PGiAAAQhAAAIQWAcB8SJfTKzEq/ziJEpO3nY6puxDdO3EsYs+3OtAMT2JajWxLM4e251xTVDX0YhouXoCXYzGBJ5wx/0RSVfaqRjt+kWSdRSvutx3+YYQhmfiOkwuidEdexHdrSaKfXwvLD1l5WUTq1vS5vIPdwB9oS55H9lFH4WlJm5R16eZFYlFdQ5++yjcoxeHAsB3Yei5ovTljTKK1Iu29MifzGJRjs44i6V2bFCLS1UJTFFO2TwEXv24AAAEIAABCEAAAl0J6NnRnrIL5fyoMIlS5qSe0UQnH+Rqo+LhmC/lpp0+E8uuqiT5HRPUvoqmHAgETaCL0ShtKxkvKqIpD2+kiaVWAOaO6qs6sQxKtQ63aXj3/VrdVaoSK7NM2lVJYlmqkEBYs8maa5+6VBolhRVQoQV0qSPuH9rLKANyB9hXVd8tK46KBE7ZhhY46B6PcBCAAAQgAAEIjEMg3dNBeQJ85oS1gvkUUpzs9XWmVjwSQGCpBDoYjcIwSwM+pYmlXhflD+X9z161Vtzp1Mr1df1deAhjO9RBO16j6Eqc7kUqRZKVmcQ6aFUGjyZ+S5+6VBrl07PfgCmhHOrE1R/KhZXSckydgc06TQFLs+x26uzyyOOrrGx9CdxePnJCAAIQgAAEILA6AsVJlHo5r2aAYsYmJ3H1R7uJZXH61+5MvXykgMBSCbTYPdWgiPc1TbY5jbZbs/lp7HQU1lrxqmtL0jSV2Ss1tsHi3VP1Zqj6KCQ2J+K9U03i9IISWr/xqq1L1mG8punmrbm6U2XtWqo2SjUbidnbiJmTxY1eYzHiItNM9t60zs3JLMJO2aoEbr6fEjkgAAEIQAACEIBAloC9IX5yxTVjzJ4zG92nf8TToOwkSs7qzLTTb2JZnP61O2NmibkZIh0AAiET0OZbawnF7ql7wmjc39+vMIlFwKWuY6lmM3pBAAIQgAAEIAABCExMQMRJyZ0VKz/hOLGIVA+BuRLoaNC9vr52CE+dKzTkhgAEIAABCEAAAhAIgID9EbDT69I9CwOQFBEgsHICeBpX3gFQHwIQgAAEIAABCEAAAhBYMgE8jUtuXXSDAAQgAAEIQAACEIAABCAwOQHCUydvAgSAAAQgAAEIQAACEIAABCAQLgGMxnDbBskgAAEIQAACEIAABCAAAQhMTgCjcfImQAAIQAACEIAABCAAAQhAAALhEsBoDLdtkAwCEIAABCAAAQhAAAIQgMDkBDAaJ28CBIAABCAAAQhAAAIQgAAEIBAugYZGo/05nb29s7twFUMyCEAAAhCAAAQgAAEIQAACEOhOoKHRqCrc3r7p49tJdwEoAQIQgAAEIAABCEAAAhCAAATCJdDGaMxoI32PZ1fiH3Wc3d2dJX/JZOLX8dWVfUpePzuTZ6SfMvVcHl89xRl0fu3GTEoTv3UClcH2cKoT+ppMLP7iDDTm0hPCvTEgGQQgAAEIQAACEIAABAyB5+fn2G9Y8p9OGV98vNyYnJvLR3FWn5HOR/2XOnu7tf5Qp9RF+Ye8lDgr5d/abRlnkKl0sblDZTeVGFenSqVK3N6aOjkDjaQXhd83qgcfVyEAAQhAAAIQgAAEINCVQMaga17Yy8tL1MJozNhsxpyzTEVtIspkqSUXT9+tM7GVmTFCtUmZGo62kZqGxbosytQUNZasMU45oyGbhjNYOTN532g+bMkBAQhAAAIQgAAEIACBBgS6G42dw1O7Om1TC/T+/CA6+aY8lruLQx1o+ulipxJkjMfSKh9+qRBX6+AMNDSB8HtC15FEfghAAAIQgAAEIAABCAxEYHhPYxqemvU9mjDS1Ep+vNyamFcRppp6MRM/ZerDTDNpb+atCZNN/JucsUN/oREmjQaviEgKAQhAAAIQgAAEIACBFgS6exrbhKca8zW3yDCNRc2Gp270Oki9WNFaehj/SopL10XKM+kUX2cWhTjXNKaGZbK6kjOpb3Z7C42QabQY82SBAAQgAAEIQAACEIBAIwLdjcY94Wnc39+vcGOKjUvFVSFWG1en2ND09OHyUUaeckAAAhCAAAQgAAEIQAACEIDAyAQ6GXRR9Pr6OvmaxpGJUR0EIAABCEAAAhCAAAQgAAEINCAwsKexgSQkhQAEIAABCEAAAhCAAAQgAIGeCeBp7BkoxUEAAhCAAAQgAAEIQAACEICATYDwVPoDBCAAAQhAAAIQgAAEIAABCJQSwGikc0AAAhCAAAQgAAEIQAACEIAARiN9AAIQgAAEIAABCEAAAhCAAASaE8DT2JwZOSAAAQhAAAIQgAAEIAABCKyGQGejUXyJce/46skCVjyzGpooCgEIQAACEIAABCAAAQhAYGEEmhqN0iJMjqyt+HR1vLd3dlfJxyfNwgCjDgQgAAEIQAACEIAABCAAgTkTaGo0Sl03l49v8rg/P4iik2/xH4ZC8cycASE7BCAAAQhAAAIQgAAEIACBNRNoYzRmeBWdh+kZyy2Z9UpGhVzqhE4Uh7e2O1Pdlu3KJFf3dumL4ZrHKrpDAAIQgAAEIAABCEBgGgLPz8/KbVh6aLGSy7fb1NOozj1ebqJoe+v6wxTpk+ZNliwKsipod6Zam3Zlkqt7u/TFsLp9uQoBCEAAAhCAAAQgAAEIZAhkDbrGcF5eXqIWRmNi3UpTsdJoVMaindpYjy5RTWpVrjFIZf5GZ6ox9FUL5TRtl76INe7mZIAABCAAAQhAAAIQgMCKCXQ3GtuEpyZrGr+dVDpHn64+XexSw9Lfkfrwy96MVeZrccaExpbtzdOizHaSkCvX9H2R9+9RpIQABCAAAQhAAAIQgAAE2hNo4WlMjMbUG+gMT03dinFkYmUIqwpP3VzeKuek9iy2O1P9DqFdmeTq3i59MVzxOyJUhwAEIAABCEAAAhCAQHMC3T2NbcJTPY1GbfWpY7PZ1Kx7TC1MHcW4vW13xiM21XJ+tq2lnWzkMvHMA7Vv8xFEDghAAAIQgAAEIAABCCycQHejcU94Gvf39ys8leKrjOKqANnem0lOCEAAAhCAAAQgAAEIQAACEJiCQEeD7vX1tc2axik0pU4IQAACEIAABCAAAQhAAAIQmIAARuME0KkSAhCAAAQgAAEIQAACEIDAXAhgNM6lpZATAhCAAAQgAAEIQAACEIDABAQwGieATpUQgAAEIAABCEAAAhCAAATmQgCjcS4thZwQgAAEIAABCEAAAhCAAAQmIIDROAF0qoQABCAAAQhAAAIQgAAEIDAXAhiNc2kp5IQABCAAAQhAAAIQgAAEIDABAYzGCaBTJQQgAAEIQAACEIAABCAAgbkQaGE0Pl0di+9D6uP46klpqs+d3cm/786S8/Kv9EjSajQqh85QdZgiTNK0UHXKlsYIZFds1aHSKjGqcxlJc3XZ1ZliTVEVZxwKFxQr1lXHhusQgAAEIAABCEAAAhCAAAQGJ9DUaBQm0uFFdPn4Jo/Hy+ji0LIFr78XjcCNTvt4udldfIpNTF+tRGWn16qA2+31qaro7uz0OtreqgKvT4WddnB+r2SRJ6Jo8/G3A2ES/nqIVCJ5fDuJq3u6+nSxi/925EpKTiWVZ+LaI1WXsDU/aeWNPD5ntK15aCpXP0+vpYC327jkgl6+jEgHAQhAAAIQgAAEIAABCEBgSAINjca73y92m8s/zoVlJg5let3HP4TFtnlwWI1a+oN3R1G0+/no0EW52Jw+x8efwsg7eicqO/mwjXY3P56ik2+2HfjwSzs6tTlnJJP5th8SY9EkuDnaCrvSPuxcmZJVpZlj8/4wevpxs9PyHL7fKG18zuQtRiGsLEcJaCot02vItqdsCEAAAhCAAAQgAAEIQAACtQSaGY3KhVd6HH38WGo1qpzS8GpySNMsUoZhoWJld2m/ojykMRttv2j7VSW+PrXjZ6V1ePTl8/ts7ZlccUFnhxdHt9o9KQy526OLw72904fLR2kbKyM2PYRkPmdkBuFVFE5F+9g8fNWRu1lzOadXE1qkhQAEIAABCEAAAhCAAAQg0D+BZkZjTf3vzr9EX69+ZVLtpNW1tyeCM7e3qVPSTpJ1stlXhCfzdqsKOLyJbCfhnTDtLI9ndPf9Otpcfo59i9KSU2GlSaSpjiFNLpsasrn0aSHM43thzklTTrhApbkoyvl4c+ix/rKMjlDDxMiqNFLAXfRRSxjH3aoLeb36b29KhAAEIAABCEAAAhCAAAQg0IhAM6OxIsg0trk+HN3cZLyR8ZpGO6i0iYDKohTHl6M4MDReECh8d6kJKq0/HTaaGH46aPbgt48yivSH9EpK21MtKxR/6GWYuVxGKqWk8CKm15MzyvOZHqJGnzNFdVUuJa8NVC10zOjVBBRpIQABCEAAAhCAAAQgAAEIDEGgmdEYnXwW281cf7X3TM1uinry4WiXieHMCp3uX6rcgSpctXxNY3pJOQXj1MrJ+Gj57vS+N2YNo7VHqophff9bdq8cHWoa75bjyJUYi2lwbHJGGaFqt59Eep8zxWZTudKwWyV67GS09RqivSkTAhCAAAQgAAEIQAACEIBAMwLPz8/al1d26OKsq2qb0vhI/IjqnN6vVK3d0+fln6mn0drkVOVOrqgMyV6nOSnSunQCu+5MNZkCrFSZcvUGq/HWr4Vq01xG5nQdYlKOSWQK9jljuKTimKLVKade1e3CVQhAAAIQgAAEIAABCEAAArUECgZdbY5MgpeXlz1hNO7v71cYmmJBojYamxmjpIYABCAAAQhAAAIQgAAEIACBqQl0NOheX18bhqdOrTD1QwACEIAABCAAAQhAAAIQgMCYBDAax6RNXRCAAAQgAAEIQAACEIAABGZGAKNxZg2GuBCAAAQgAAEIQAACEIAABMYkgNE4Jm3qggAEIAABCEAAAhCAAAQgMDMCGI0zazDEhQAEIAABCEAAAhCAAAQgMCYBjMYxaVMXBCAAAQhAAAIQgAAEIACBmRHAaJxZgyEuBCAAAQhAAAIQgAAEIACBMQlgNI5Jm7ogAAEIQAACEIAABCAAAQjMjABG48waDHEhAAEIQAACEIAABCAAAQiMSQCjcUza1AUBCEAAAhCAAAQgAAEIQGBmBDAaZ9ZgiAsBCEAAAhCAAAQgAAEIQGBMAhiNY9KmLghAAAIQgAAEIAABCEAAAjMjgNE4swZDXAhAAAIQgAAEIAABCEAAAmMSwGgckzZ1QQACEIAABCAAAQhAAAIQmBkBjMaZNRjiQgACEIAABCAAAQhAAAIQGJMARuOYtKkLAhCAAAQgAAEIQAACEIDAzAhgNM6swRAXAhCAAAQgAAEIQAACEIDAmAQwGsekTV0QgAAEIAABCEAAAhCAAARmRgCjcWYNhrgQgAAEIAABCEAAAhCAAATGJIDROCZt6oIABCAAAQhAAAIQgAAEIDAzAhiNM2swxIUABCAAAQhAAAIQgAAEIDAmAYzGMWlTFwQgAAEIQAACEIAABCAAgZkRwGicWYMhLgQgAAEIQAACEIAABCAAgTEJYDSOSZu6IAABCEAAAhCAAAQgAAEIzIwARuPMGgxxIdAfgbuzPfdxdudRydPVscztlVbUVEznVYBXIg9pY129pE2Kq8zTRDCn+h5Cj5ukDaIcKt2dGkH207EJbb8SPVJlxoe3UrGox1dPlVUUNBqik2gNKkXpdhNQKg4heZadzVTUVsfWAb5ETe9W9eguKkl1R+0yxHwkcNXuNXS8EvlIQBoIQGDJBDAal9y66AaBdgSuT3uc+Mv5yOl1QZCnq08Xu83l49u3k3ZCziRXifozkd5HzIKGvXYfHwkGSDOuUkN1kpNvb4+Xm93FpxoL1gXQrxWHkjwj0dOPm9329u3t/t3ve+Jesvn420FPTe6nZE+VTVHMWm6zU7ClTgisjwBG4/raHI0hkCUgp2PWcbuVl6+/tphnNiF7cH4vZoHndbM/lewtQMsyWMGaNEIfaeWMXpQj7X95DNN9xqbdQalY1LquPZZGnuNsmpuAZ/+TOqh3S8IIFkcd2opSbTWFOd3/nW6sZnXrWKzds/mnFduzG5AMAhCYmgBG49QtQP0QCIzAyQdlNVpHHLukQg8rIsMyEWBxOpH18ELaFJF4p58GLtolZopM4umudOTs8dVdIQi2NG+eo5XQEYXmqVRp4+QDurLxb3GFbvVdoOJ6UqlECYVgNrfMJnYvZpVwzpTl1mMARHH32f18NFWWoM639bEKd7Y7WAqgGD5nQ8x1yqoe4mym2hGYU6rQMPaJQnhqZauJZm46RoS0vlpU9LRqnf1uAm7JK5tbhDBY13MNV96mVYp43xByKh+cf1F3Ot1VC3ceFV3s1KUY9FvRUVsNMVNeQ1aFYVLCrf4227rn1I4lEkAAAjMm8Pz8nPEyFH5o3arTcBUCEJghAe0UirJOhvj9uzkbJ7JucrFPKU4Y5y4mUyUkpcXZVWJH0pLaRE3ZWirzZlogV3Eifqm0iaOs6HPN8UkSZARz1KYKdKhfAkoW21LmkmyZx1LOkaSUaFldoaNbGjmqKe0/ubYUvHTStCUsxNluUIY79XRmn8mJWFX5cmpVKlUYOPaJuJJYDY/h03SM+GpR0dMKgQXtbgJe3Tvrgi5MljzapkqRqptJzVhOpNcCZgtS50rbrktHte64vkPDMKtl5XVPdinrm3GGTzlEhgAEEgIdDbqXl5cIo5HuBIG1EnBNuOIJSjLTy9ls8TxKTV4yl3RRyaQmM6kuMfvyEyD9OxHJWB+OWtJ68gZu2pC5cszstii5qbRo8DiNapfR6DRp4vKc6jtBtZU5q5xBqJtwYESaRr4jpSgr+k+xreMz2b6XUSPTSbLWSHbq7+xdVc1UvAeUK5VInqpZZjT6Dp8mY8RXi4oh6bCmXG++PW4C2btA7lfSMbJDO29Eerapz5Dx6O1FPXPvkdx3ntxdIms16hYp76jJfdH/LpT0vaasfO/JPrdZJ/C1PirRGwKLIIDRuIhmRAkITEPAbTRmfG4ldqXlRHT7KS0XZu0k155xF+w0O3d+Cp6aK3mDr5jSUUl+/liwGr2NxpzVlCnIIbRs7YyTxjZlLfyeMmddW0nJuflmQbl+EKUdN+d1KnW0pT3DgdeejNtT8Yw1UkLUomorWw7R5X3NDUS3Uv5Go+/waTNGbOd91f2j2NMyqbvdBHJmYoW+XtAqm6R0yJQ1d71tXDLYnG9CMrxbdlTPEd2alXNoODpA5W3WYKvpOdM8tKgVAhBoTaC70ciaxhmHFiM6BHohkHvVnlmN9uvBs4p4DUy8gLE80+NPtcLRPg7fqw0pHn6ZbxRs3h+6SvDKqzIWU8aVyItP3kp56i426PisN9XQh1q+Wbb/bCmoWOajd2ZvoEFl7htRvJVGMt/dXfwuvtvigTrT1prj7ubHU6S3onFtlOnoBgn5mh7SoJl0iU6lvHuFj/ot+rmvFr5DUonQy03Ao7lL4FW0qVnBWby3+N8QkmpzVmlhS520N1br0rKj9jKiK1nZfOs6QMlttgK4f9cnJQQgsEQCGI1LbFV0gkALAiff4jfL16f53W4KC/7yn8m4O9Mf1chMPZ1zEmvalJvpW9ZSifT+eYt2aHGmVatUE4axdWF7Wpz7z1aA6lnmOpx9VZffFMZ0I/slQLyzqnk/WvqZlYPfPkqr8edjuc0YObpB0lR1PcS/mbIfnHQp5d89mva0XrTwH5K2Il1uAqacpvqKjBVtWj9kbAWKr17828mVskyXBh3VGgi93IUqWGVNRt97ck7vdj2nG2ZyQwACsyCA0TiLZkJICIxB4OD8D+0wMx9201Mj8Vu6jcRR8nHq+K385vKz+ubi3ffiZxkTR+LBuyOZ5Po02dD06eqrtjc/1H6v0T9vnNLInVSilPBUqgHxGMvx1aH6JIBrux49c6wCNbLMfVUX77OZmsjx1yoiabU2R61zXH//XXqkt19cn2RJukHyURhru9LqHuLRTHGjVyplTJzr73pUZHqX3W2aqh+bF31o4TMknT283U1AS95U31SA8jb1GDKtbiZ1w7tOF/+O2vddqKL/W0q17gCtM9YR5ToEIDB/AmyE0zo4mIwQmDkB15o9s46lfNNDx+6p7rVMuZA3cbss2ZQwv4WO9Xq/ZIsQ+9brXAiVW42WpC+KFF+p2D21eJuXiTOCuWpzANxcXuY/Z6IKz+6Zk9S32eiQ1zqZ3Wsa6/ex6ANRYXmmET5xLha7hmsDG+fyM6thnYv+Mg2T09d5raqZqlcz6uJMJ6lau5dtjlL1sxpZyWrHiJ8WlUPSUrbbTSDzgkRKXtfc1jat2ZpdWqk2rVbEddV1Q6hcn5y+6KlZ0J29S5i6G3VUjxFdvabRve+xvS66lpu9JFP1Bbs3+vacmT/9EB8C6yOgH2St9Ra7p+JpnL/djwYQ6JGACODTk4bE2yi+p23PIsS0yfFtbRPVFhs5OkfsOMmuwVJf6M7MEOVMrDReMaead16hh1XJ9jY7E/JSqgHVbG3avEgwZdT/LYkBdoHKlLK9vf+inLLJ0bfMcsFeL4hkzGcWr91JmoudfCOw3Pecr9HuQVU9pKqZcq1dp5Tdg/O9q0WrNRkjflpUDsmart3kJpCTvHlzx7KUtmm1It43hAaj2XfEeXXUXoZYTed03kFbd4DWGVsgJgsEIDArAnvC07i/v18hs1jaoQ3TWemFsBCAAATmTSD+dLrbTJ+3ar1IL6JNzaot35cOvVRcXUjcbMLbE5BQI+jdSxWBtmkvulEIBCAAgUkJdDToXl9f8TRO2oBUDgEIQCAmEC+5U1uwyEPvFunaPxRkkoBwMungxWRt4fRY5PLK2g2EpxczXAkCbNNwYSEZBCAAgXEJYDSOy5vaIAABCLgJ5CL7ZCK8jGWdJd79Rvoat7fBuPTM7pgByTSf4RZmm86HH5JCAAIQGJYA4anD8qV0CEAAAhCAAAQgAAEIQAACExIgPHVC+FQNAQhAAAIQgAAEIAABCEBg+QQIT11+G6MhBCAAAQhAAAIQgAAEIACB1gQwGlujIyMEIAABCEAAAhCAAAQgAIHlE8BoXH4boyEEIACBjgTUJiXHV08diyE7BCAAAQhAAAKzJIDROMtmQ2gIQAACzQnkv+rhbQU+/bjZbW/vzw/q61R1nN3VJ7RSJPtmFuxSfcEuTRSvfrbIYmmfltisnPhrKN7cSimk1eZN8cWq3KhHkBgCEIAABIIj8Pz8LL51VXFoiavTcBUCEIAABIInIL9qKD5RoeVUP8RHPXqWOlOHV9lpDvlXKpE6L49EYi20/NU8y+PlJinb+tO/HJVJCdIDN1WYKi39K22TRars1RNIBAEIQAACQxHoaNC9vLzgaQzOjEcgCEAAAiMQOPksTJfdzQ8VcupwuCnH3PGxdPUJb9iV5UB0eeeSc2ffbdGLKYuOyLvv18KA+nAi8p182CYSiXTiG4z54+nXw+b9YdQiy8H5/dubdpUevDuKot3Px6hBOdLVmgj5TTzRS52ulguxPJxXCfNmPi8pVRLHXFUeoa9SBQQgAAEITE4Ao3HyJkAACEAAApMSEIbO4UWkfI63293FoRUOujv6Il963p+/MxLenR1eiFhVcfbxMro4VKGaT1efLnbKR/ghSk09V8p6RZU5Jw5ZnHbEpcfjz93Ru2KMbLMswvIUpWtDLXuUlyMqjjYPX+Pw1NLoW8lBg5QOyd3F75VhusJKVNyNBTpHlesblBQQgAAEILAEAhiNS2hFdIAABCDQlMDd7xfCEPr424Hyosk/RAnS1xddfze2jvYAWsfT1ddrYc99lqcPfvuofZVWCaoAdThTRifST2d8bDKZNOGKx8k3hzMvdjS2yJJWoCzZaPtFOB39y1Epd9FHbVdH16clqxqlC/H+/FF6ZZWf9OFX1dZBksXt0cVhvGhznio37XakhwAEIACBeRLAaJxnuyE1BCAAgXYErk+1v0xYNdbeNsLBmJyts3XSatNAz/Tc4fusc1BfcaW0rvhpImzTSNq2qjC/I8kSpxY+VaG2cOgps9W/HJ1SOzmVWZz4JHNS6ODU0yhZdlkvZN5KzxcYvMr1KpICAhCAAASWQACjcQmtiA4QgAAEfAlY28pYHr/Mjjhe26SK+lyBnjKQs3iUh4QW0joDR1WqkuDUkljTYhblZBSKlqpXXrXbFM7Lrj2usUkqL7piaX3baR4qN9KGxBCAAAQgMF8CGI3zbTskhwAEINADARNlKs3Auu8x6sR6sZ6JSrVKUHvUqMOZUu72kvsih+Vrk5njOFm34RlbdS2ySM2Uk/EP67sh3uVoZXTYrrULjxO+dkJqDiXhqXqPIfXVy+rS4nhckc5b1DTLeCr30AkpAgIQgAAEQifAJzeG2tqWciEAAQiERaD8cxjm8xa5T3IYt6SdNd2eJvVPJue2W/uzHsWUThFcBSpymS9SxJ/b0EibZrEU1E/lWDO/crLfw6j4TklaXBZEvh9YO/xYnt9ZqhxWF0caCEAAAhBwEtDPvtZwxCc39oTRuL+/X2Haiheiuo7QzV/kgwAEIAABCEAAAhCAAAQgAIEsgY4G3evrK+Gp9CkIQAACEIAABCAAAQhAAAIQKCWA0UjngAAEIAABCEAAAhCAAAQgAIFSAr7hqSCEAAQgAAEIQAACEIAABCAAgZkSaL3ekPDUmbY4YkMAAhCAAAQgAAEIQAACEBiJgK+nsbVhOpIeVAMBCEAAAhCAAAQgAAEIQAACBQJshEOngAAEIAABCEAAAhCAAAQgAIEBCbARzoBwKRoCEIAABCAAAQhAAAIQgMDcCWA0zr0FkR8CEIAABCAAAQhAAAIQgMCABDAaB4RL0RCAAAQgAAEIQAACEIAABOZOwHcjnLnrifwQgAAEIAABCEAAAhCAAARWS6D1zqZ8cmO1fQbFIQABCEAAAhCAAAQgAAEIeBHw9TS2Nky9pCARBCAAAQhAAAIQgAAEIAABCAxAgE9uDACVIiEAAQhAAAIQgAAEIAABCEAgIcBGOPQFCEAAAhCAAAQgAAEIQAACECglgNFI54AABCAAAQhAAAIQgAAEIAABjEb6AAQgAAEIQAACEIAABCAAAQg0J4CnsTkzckAAAhCAAAQgAAEIQAACEFgNAYzG1TQ1ikIAAhCAAAQgAAEIQAACEGhOAKOxOTNyQAACEIAABCAAAQhAAAIQWA0BjMbVNDWKQgACEIAABCAAAQhAAAIQaE4Ao7E5M3JAAAIQgAAEIAABCEAAAhBYDQGMxtU0NYpCAAIQgAAEIAABCEAAAhBoTgCjsTkzckAAAhCAAAQgAAEIQAACEFgNAYzG1TR1X4o+XR3v7Z3d9VVcp3ISWe7Ojq+eOpUUaua7s729peoWKnPkggAEIAABCEAAAhDIEmhqNMo5bN5iqLUiRIKpjAyXvGV9QKWVR6dJei2N5l3QS7Bq68KWqmNzHJzf326vvxaMNFVFelS3eEcZEoaPP49u3z7/Oj59+PjbQT1YA7JzMztbuUlnKxU2U/LT1dfr7e39uVO3AXpaPUJSQAACEIAABCAAAQiskMDz8/Nb5aGZJElut+LH9rY6S/bq4+WmaZYmxVen9ZdXptxcPr4pceUfoRw9CzZYc9gF12AfTIaaNktQimRDNLN/ZwulbyEHBCAAAQhAAAIQgMDyCWQNusb6vry8NPU0usxqy+Nhe5uUq0mcOLzYRdH1qfbfpb6exJ1nspydWV5MyycUu6x0LSqN9gZelTsG0zK/WwIXy3RpIxxpb2+Jb8eRRXn0zs6UV+34OI3UTCg4aRi3m0uGAjT3u4tUMKuK1LllexrL6N3lm8Nqj9R/XC1PsQUd4h6+F5b3wy8VMZoXxkMGJUECOfVsp4IlPB3C+LVydPDuKIp2Px+1fEldqlyHwEaGqlY+q+5snkrlG9d2imZFrUq5wtdfqAwBCEAAAhCAAAQgMBiBHjyNxm9keW/yPh3tnBRntQ/PXLacM+pP5cXM+6xUHnVSOzn1n7okh9PKv8yMma3rt5yiTjGU6KknUv4yumWFNzoaLLZ3ywjphmZLViVYqmu2utgZ7DhpadVCnmILGkmdnkY3w7wMTmmttlZNXeRZFMapUcrS6WnMNqhT4JpWtnpAgw5copQRwIG6RNSKRmn8IokMEIAABCAAAQhAAAJLIxCGp9EYtAe/fdxEu4tD4Rz5/iF116UG78m3tz+iT+Ly6bV28zz9ehDT7A8nMsnJh9hqe/pxo32T8khSxgadSqq8RNHRO7PSK/Zp6TRNy0zEE8Ipw0RWLN2gFWKkdUuhr78L/9Td9+tEEUsMJWPiIlQFbr/oBWpKWyl3LbQoL1j1C4QqsbM528hTaMGcMKbVhEn07aSSoW6s8rbevD80bZ00a4anBJPrTk7CWRF1/9wT/m97sWDSmdzy1LRygw5cr5SRtgy11e/jtHWNUt1huAoBCEAAAhCAAAQgAIFqAn2Ep6Y1KPPIWF6FLTZlPN3hzcfYa1QtWGZVoTA/Coeefjc6astU9pmUf3fzQ2/G6c5i1R3bE8Jm3Fx+dohZL2ANNF1AQbCO9CqyV8lT24LGUWxVUIu9NoFb2lphnNnSyqxele1MRXlatHJLpYzMZdoV+307DvUdkxQQgAAEIAABCEAAAhBQBHo1GvWqravD2PJKFrUZ1I8/hQdROkqUM1AeymeoPHXaV6dPKoelNtta7BCpsjcuM10cmAjnKYa0Jx6+f3/Y5PbvtFSLlxtqweJtR6W2KksdtKJgmpLyrhqQaXf2FDvh3EyeYgs6xtHB+R+Xm93FJ+GtrRWmNoEpv8jT0Z2chJsM9TJ5Slu5VWerUKpisJTp4dUoTSCQFgIQgAAEIAABCEAAAhkCbdY0WgWY/Ub1sjS92lAfxtUSr8kTv83l7Tbeq9TKos4lO7Mm6/jSYtyr49y7YGbrKS/TuabRIXr+VHZz1exGnPn1ek4W8qTZg9YJzRItZWGYJqc2G7PQ01qvp9ddZiq2pEqbI/YKx0m95HG1YCxqZnVpYV1ppkckAqYLXB3SxpDz6xAttZzCWLQKu/zajAzgwskiPdO1TcO7WtmnA3sqlXHYpoMlK2p2LbHqUumwWlokPvpAAAIQgAAEIAABCLQloKfabXO/id1T94TRuL+/X2FJi/Vfuo7BrW3hUzt9uHws+Srd4NUPUEG8UagwAVwBtv1WuDx6RT5j8uy3dSgNAhCAAAQgAAEIQAACExHoaNC9vr72Gp7agoL9eYdTsSzwD/d3zFuUHEIWuTxQeIcy+/QMIpe0GONw10HKD6TQ0XgGoi9iQAACEIAABCAAAQhAIAACIXkaA8DRrwjalJMxpQvynvaLqFFp8GyEi8QQgAAEIAABCEAAAhAQBLp7Gn2NRnBDAAIQgAAEIAABCEAAAhCAwEwJtF5vGEB46kyRIzYEIAABCEAAAhCAAAQgAIF1EPD1NLY2TNeBUWop3L7robQqZUfuw2tgu2wdl6Rd+LqEL6HPDaRj1JBPFUGlWZu+eoYg/l38JAE1gxpo7YRZSSPm4KxB64464mlsN6DIBQEIQAACEIAABCAAAQhAYC0Ept49dS2c0RMCEIAABCAAAQhAAAIQgMAsCWA0zrLZEBoCEIAABCAAAQhAAAIQgMA4BDAax+FMLRCAAAQgAAEIQAACEIAABGZJAKNxls2G0BCAAAQgAAEIQAACEIAABMYhgNE4DmdqcRB4ujre2zu7i+7Ojq+eIDQcgbuzvb11IF6PpsP1FkqGAAQgAAEIQAACBQIYjZN3CmU6ZQ85wU8sqq7yyWm0tMyGOnLiN6np8efR7dvnX8enDx9/O/CTT2kjj2Y2UAVMxyVTSYua/NToPZVuBQ2/YDjdfb/e3t6feyLuXbZhCnT2hBpN/ceUSNmshw2gZHZkVQ0skbLJuBtAVqvImYo9LBRKhwAEIAABCMyeAEbj5E14cH4vPt309na7jaLN5aP8U07w1elvJ5OL5yXA9jZR4frUf/p68k3oJ/X0NWjuzk6vJaLHy83u4lMD72RzmHFLNK7JC9dQia6/O18OnHybTUfyJVPSE2o09e8Gjz93R+9CsLL1yBLd8Pq0zIp9uvp0sfMFN1K6mYo9Eh2qgQAEIAABCMyQAEZjqI1mvCL6j7PYxZbOHC1/WNFOM6/7z75bClZm6QHE4ftNFD38kqGmaVVa4oz/IVYinyaTrco7qib/iaXpUiqtTaOxXEyOSis0P3h3FEW7n48ySXVFljvX1jVtGlf2ZsLUtdBm85CxGvNaK1my3Ul4bK+KzluHqMp9eXamnOKqnKH7Up2y+npdT8iKbXsaq4fPr4fN+0M/EcZIdXD+ZRvtbn4UR5ZQ6VCajNen2vneb4/qqNtMxe6oNdkhAAEIQGBFBNa0LgajcR4d+zr6oL2Ru4tDOWcXc0XtdFMnxYwxYzfenYmJpH7Z/yG6jjWsztILBuGfiSLpoRGOoAclnHCf6rlu7E8VLpMo2n6RoZLFNLUSnnwQxV0cZu2zIgepfiSrLzpoipVWK/7060H4f4X9oGQzDtXY7aN8PLoVhKLXX2Pz2HnS0V5Nhalro6OPH7NWY2kG3Z1kY+wubt5L+ZVL9ffYqixqqkraPbz/Q/apbye1LVUnatfrJT0h30A5sU2tztZMZXr6cRN5R0x3VcUvv3wfI19e5PuMGFd6TN3Ktyh99yg/2SpSBSi2/UoneQXnH7dcoatVSFJHzyHOhaUG5WsP2miUW2lQtwqgIii6Te0OsqvSd2Blc+9tmy7w6HwnaFvA4FjaCladb3CxTQXlK1PcKzjaLfBpTOnpb3/Jr7r6y9/Eqit52j8YrbTaoVddFSsOdgXQ6CgwGhuPhkkybD+oQFU5V5auPDGr3cW2V3oynRJLS8fOIa9UZ+molLBa5aHsNxlSK8IE/4g+qTPGUSdl0EbWZ61LPo2HhCKPCuOV9amFny4OytBTwYUZP5RSsUSwovrKNt3bU8a3mI2rilS1tlIHv32UZpdM+V1YYdr36TrpVs1bGN/WeXf+Jfp69as+ue4cyo2qSelDOondmurrSVKPlqqXoVsKZ08oNFBW7HSAOFszFSiY4NQio+o+03uP6tZIae5QxFaOWfVCSb0oiS4O+7Pr0uBnPT7ESzvfuHtPzOr2b8WgiyW85kbvWURVspKFEu4sYwRFr0rfgZWNWzFdSBK/I+yh3wxaxDhYeldhbLGLK1OcKzhaL/BpDOjgP/7LrLo6vlI33P/6D7HqSp6ey6orh9LrWQFU3uIYjY1HAxmKBOSjSDk89CFfyhzefBR3CmnhmePud2ky/qF3ZClJU09XmgupB7M+vZ3Cv9LYi6v8akkJ6bnktJ5mJWZs/AbNedIhp78w/kqefDi6uRE2s//hDMMsaioLDCpiU8hT6AmNxHYnlnrK7XT0S5pwDunEF/yr+8wQPaobgsDEztyBHO+UZOMnb+LNXlvOaHPHydi9lg8Y7gYwmzt5aajP2jZjVViyT7R5tZT5EsYKil6VvmMrG9/OPTv8ZOsRxsbS03gdV+z8yhRLieKbc3HRebInzSuLMZ5G/Uey6ko6IeObmrn/OhySxn056qorS6FwVgCZB9D4KDAaxxgp3euIQx/VNEH4e5Q3Kz6n5g4bO5pOX9XL21QOeVRn6S6huA/9kexPY8JUldPP3A2E21FHpsqjmKZWwtQPn5TrzKIcaFr9fKS5UzAf3bX7UC8qS2Ov1F/HV4exGauXc7pOOuVsLUyVwMJq3GV2RdEyWe1Qo65b02ym2pbyQdolTUlPKDRQSR3VOgpYoZnHZoxX95lBelSndopvTYGIXT8MXDHzviHoMahswHAXeo68Kixb34b0oNZvNyrCkssjydNo82ohHSWMFhS9Kn3HUDYNlilfJFK2vMIZ/N9zBw+kz/eg1RitacR0rEwpruAQqZ0ne1C2ZRFm1dX9uV519be/nF7Hfknnqqvz+8Kqq8osLeUqzRbKCqCpFqBpMM/Pz8qLXHroZPHljONIBeCUHcLvVHY5WYNTXa+OH9KrdXyPpuk9y63QxSohpeRZbC6ZtXtqRnet1DZ22aX+EastioiM209nTINSkuHQgKpLnVTZDHMlkyg6W3284ak9EsWpYprYaRenc0lo6WxAuDikXk+dzAhZIli2rlxLJPqnFaWNYLlXk61vMz7X9KTtdI2rcxJ4e2vTkaxWUGKa5a4a5mYjvcCqWru9LEXV6UQvh6YFJpXdr3YEtNExU2h1T8h0jlxrFcZCxuWo+2Bvo6MWREUCu2+ZIezqMzGLsjHVRYYWvXF0sf37UqaT21jsQWHJnw4YNYqsXpEmSk+mhbR5DmWesxVNZgairMTqujmxExGyopjMyY3aWVF2rJeUkD1dUrvvvGIF+goV65t40MYtdnKzx3FmVuDo29kxnRsL+carV7PpHWlQLE2FSdLXqzmo2GYEJ816u91cXqY78Gsxk8dk5hnnPJnDUK+dJzdZWWwGqmnt1bG+kZo/EjFFosw5JbuVs5hDzTST8oy6dhZPGU2yKq2dnPPzLucUK35wmKdPyWjK3JNL7rqxpJmrmUm3eRyVTGJ97kKV1F5eXlp4Gl2Be7Y9IP8eY8FDvk7x239LfUfmslNj6SKD7aw1MDldPkhvljjSFCo4Tx/FGPFkecrbt28yWZygMksDJHbSjJyqgvg7GloyWb35gkjaG8WprIixXjUSWpcNCFcWU3ayzjD5fkmxUkefybVEom1aUdoIaUVW0zhP6mDKTHs5CbRrBksLVU8O5/29DKNVvcDW11I0E6/i0LTAZIi+1ED36p6Q6Ry51iqMhfzCs1C+UGJ3IzOEXX0mZlE2phpQ7SNpwGLbeyE7VXXF93YKQe8DaLaMxIEh100m8SXtwpL7cqe3q92XzKr0HU1ZFWuhJmrFhSRlyyvK4/l927JtutGwtBXQnW9csZ0rU5xrebos8OmX0BxLW9UKIGcDtTAaiwZi+nH6ZFN/j13gvzf7hkTNBw9yX1bQEYRJwLTvdwV0YGH8XQG9x1NhgUoYXxqY42BDZghAAAJTEjj5LNxzSVh/EkierKYRgjnCaL1D0N169bSPqFW4nor+/ntqM7rETjJ0jySvLWHgoOhV6TuWsmqrJvHWwLPD+6xZGHJcj4WlZx3GFTu7MqW4gkMo5zzZs9JNirv+T7WWUa2h+rd/OTj468fjKD6nTh5//Gv6sWR9Nb/qqjJLE1m80wawAmiaBWiGUIfw1NQVa746kMTLZL22ucvaO6v9qAUne3JS5THFOGPqMt5/VXM2vRWOF8vlDiDKlmPlyoU2xvLYkX92GJvQqak3fL7pV6XsyM20BrbL1nFJ2oWvS0MJ7eCgxHmSe3DIx5MM67ceAPED03hbHKU4ny7ekaq6Aq9bTRqOnCQ30hix80/MWP7kgVUavJR5/hppXLHoVUHRHlqvTV/B0kvl4Ro3FxWX69x1Hd5aXpGP5891Wi81vTq6lWg4LE0lSdJ7qTmc2K6ZszrnWrfjXNRU2Yxe2vmgqw5PlXdZeaQxpa5bjalHBaPKY7hVV6U34Xwk6sQrgLK3/AYL0Dq2rAhPbbGmMdfXHBHw+cWIVQse4qeXO8w3aSfnVceDqdTI9IsqNkHHsTWbNxqr44x9H/k+Iy34NKtSduTWWAPbZeu4JO3C1yV8CX1uIB2f5T5VBJVmbfr6Go1BNVIrYVbSsstWc3DtsosRW3W0/jMNrnX/IjcusaOO7dY0xu8sk/9qPjDQZMFDddB8l5D6Bt8VyKnHTwhAAAIQgAAEIAABCEAAAmsm0HlNo3PJh0W0bMGD6xsSpTvmO0PqK76sUNui7WL0a1d31NZLAghAYHoC+U+xTC/RQBIkS+ruzvr7iP1AolIsBCAAAQisgsDBf/yXawfHVeg+cyVbGI27i8M9fch5SPx1PnXq9Dr5dLs26E7lN+zU1gOne3uHP49E/LL6apw8tkc/ZR6Z5VHuZygclrdbXfThRaTPpYfz6sk3ES+qvjuUVuzbHNXVZUpJdXmycok6t7f5fRfdtdvfgdbb6wR1CPGCk6kEUJak7H7pym6ZxexSlM6QRRZrupz7xGKstzEhsuWH1VRr7UWONi32jobbjYg19lWDt2FpbUaztZ+WuH95jb9WUj3+PLp9+/zr+PTB/pBrG4kr8xQHZitpM3V0L6F3NSkQAhCAAAQgsGYCzTbCaRxAu6IMohe5tbWWQtqrJsNA47FlgUvQUmUH1aoorP1tm2RzhwxkcTL/ebXyzxUWdo/o+L2+djDcbJfVi3z7j7NNi1hb9uJ27VOfq167yo1I6isYMUW9LkKYIfh7l+kl4YjE2lWlJyHt8s4x19r0ZU3jHHtphczL7sDL1q6sWdegdUcde1nTuGaLu7HuB+df5H7pP5S71fX1jvSVfe4jIpntkvmgSBV5+5ODT78eWn6O7PC92OPXOMYbt/SQGVbYi9I2tRxQWTdzFBW+4mM7wFJvnmPcKV9z/K2dszvbxzXaJ3ZqvxJkSeXUy3kyFd/428fRyF/apGEcog45iCgbAhCYnsBqVgpMjxoJINAHgRbhqX1Uu94ypC2y+/kovxGmQnPlO4/brQiylXOnuzMVmqve3F+fVq9Cuo4+xK/4dxc372U5ItPu4ncZ/aoKj71ksvC0pF30QXzmXb7El4tKxVQ8eZ8vIm2dIoXXUiog2RXTp76KJAOcU/tAfI4qahmXZxbjhkcgilbTixxtWtoeekSI0SQ6gf7G6qeLnfncT7yIumJoPLz/Q+a3AuPLE/fRKUycf9pfqwa1qbJEL4eyd2enD+oWIxyb+lXVkGPcPTCd0hZvdEVROyLuJZx7FmG3vWhq9a70s8t6BUp4ccJeIeu1/Sc8vWpFdiQwb850N9D3kqwl5sTVD0NPibVs9oQmhv909dV7mU9tXaLM2kD/cHA1WgtjVHN22vzb01pSQyTIrrj4i/oA42KPrLIr2y8Ao3Gafq0+rrv9cq4+XSpnxtKpJdxiUXT0TpyznWUlAm4/yFWfasGlzqMP6RtThauFpGq9Z6SsVH1ot5vOlTucIk1Dp7LWJGQ0u+pVcfymP/wpNdfjWFh+Fhs/ZQy3eLWtX65JUq2gFxXbtJS0HhFmNEV6tyu1TPq7MCfVAuSKoWGPIl1HVeIe2ttsB5325IpBnVbo0suprBwQf0SfrJvAoGPcPTCdrVC80RVE7QFw8jFgj1dwVbWZGHXZg9SduXjr6UXaLoVoITtqagQIWmXxfkG9blUvST+p+3yrI9SmbKVMkin++LlVhhNXXwz9ZJW3nc1mk4RYWZlkG/Q0mtTbKT950lRT4zJv9sWkpdzgtVQLu9PGn1sUn9O4P//3ZZuN5oOYXW9DTbvs9OkxGkduA+nAahkwWSopHxRJ0UgjwzhW5IYn2pJocMj7ePHDoA0KGCHpunpRpk0b0C37GpD74z0lo7LLl34ayFpIWnGTcOrlOCnfSh/efBSuRuuLyV1kapW35ptMusxBRW0czl2hZ9hht31qaiDUqdyqV/SQKfNmtSbm/PhYuLriWXmij1MvM3OvXjziuXlVD1o2K2KzefhestOe80W0x9vpZgK4Ut/9LiI+Pn756LIabT+28b2p1lLNZbVRxp2Wbx2R7lCajGrzRfEawTPWPRRc9lqYatVcnfbsu0V9nNUH1Z3i4F/+LYru/5/wVEhp/nJ29hcTGuYcVn9T1+3osepk1uh7MnntITkmBOWBUW6Z7CIXgchnAVptMltZ5bDPB9qNqaxqd4zG7vfEJiUIMybaiIBJ59c7yj4iolbWKTek37HOD4qkD5UEVbKgUd1o1bMkNbYs1qmD1+CN9wTu8Brbr6VaplpNLyq2qSbmHBG5r/joCYfYvzl+jaAyNRoajRK3bMoW2Vx6OZUtfu5ogo8GOVtBba6tZrdxIF3Zl5la4HFl6RTOHVbYbQ2RTpqashuo3FMLNSimGLJeH3N+fy82E4jdSrKvZd4lFoOlnVHczkDrBnKPkfTo48e81eiM8G8S9t9V7vhpdSICP+LlM84SLbxfjipdho7WyS608Y51DwVXevsrLizKqmbQyU67047KD5GIJlPHkKsPGnSDp//57yg6/lcZ1CaO+//+1/+j130IC+/0OvZG2muyzqMruSbr6vj6VIa1qmTW6ioV6vr0t38/v9d5xSvQ6/9UfsySk45aGkjfMKmaPppXvDuzyMXZFiW3mvxSMv8VKJO0OLun9rWpl+hr7qKybqt0Q07r9b85maZNPBxJKhHeIWoo3/kzdo/lsxkvuvaemVWUmT9FwWbtVzJkqjcOLVW2L5rOcqp3T7X9KUqddOfUIlZ978kpmynf3ph1UK3yhbvZLqsXefcfq5FqR8Q2blDjHLSZpR7DtEhzLruZaWETXdVNMi7H6g5Rr13W9RcH2yXhlKpnxtWloza/fW7cd6uUNfpvJRpr7Md5fTYHrtclXlpt71Kc2U/V2Qr5EVkUtePuqZns8Y9skTHlqnqK19IzqQbZu3cBqqW/iWIoktdN0uZG04umpuKGKrcRWOVpr6/Kbh6LOk41N9FTeHM3cPlTnk/+N1v+VmmcVKXGjqPFG6nfUWV3XUbLRI3b7ebyMh3uOpeNy5TjPNlII2finJrpzcwGbf5O/rCnJ2nTWVkKiqaapa3jmEhl70v94eramtleq2/OJT05f+sXWmY6baKU8/7WrkGba5d9pKVxt+apJq3C9IdqY2EEZk9KYdWZzKFnvea0vR1+8aSzFk8I3lp7KCtvSkbS0mdNVYsrafJ7/2dPtmhxbx3dzMTuqRFGo2d/qk3W8pFfW26QCVal7MgtsAa2y9ZxSdqFr4tbwsKsSkzLejUas7Nx9XAvMT+SN1h6BlBipLZ/lveiqbnH1ZlQ1ss2n3cOpffO9vqmRdpTseI7neyboMRaFGft9zH5+bcqvHIqZuaLjdXvQ+UCz6ItJaxG+YK5HogxJxu8D/N4FmbVzE6vzSx4SKMxtT+LL377w9W1NbMELKOx2BqzMRpjL2J2hJqTTYzGQklxmc7Rlzk5mtFYaKfMDcfzWZN5V5IfXB7KukzT6jHasd/yyY3cGw1+QgACEIDAsgi0CueuQRBE2G1BxqaaNtpBtDwuunbTyh77UzFk3TOMXIZkPnz//iCXh9jyFFeFuKO4ner3qFhfRZ18ONql4Z3OCP+ysP++RDDlyN1RLfNVzoKLe8+o1HYjyl5sHbnFCLUx9s1i3SfHZa2F8ezJCa4YpcFVS6b39m1U4MFfPx4ngaWRFPr4418P1PrHdKmCCEVVye5v/q+OPxXLHdXdRf31l7+ZxSb//T8qZrV40llLIzl7Sey5AM3d4t4rUKZpcTyNHu/OvJKIruaVbhGJVqXsyC22BrbL1nFJ2oWvi1vCbNxP00UB8ZCvdLvZNTiChHMBZyZCeBhPo5noNNO03q9YF2lcok7tPVMLXJvMlcByXmUCzHWRJTHnxoOYbSqz62wM0FFgGiHmbHF/FTqoXF6JK2pTnXNp4orRbxJ376WrpWbBj2IkK3gaEwevzK3GSozdxNCmy3NEUqsLZEIAtd6mneywfCsyIOfwb4era2s6A0wzqhVaKxsskdUy6aUuMl7Nlk3UXLs43DRbTOGkS7w08NT4F9NkqcvRDlvNei/jsZsmbQvBW+t8FIPbae9U1sTSV927MoHK3sttspHYJa3uraM7v/A07gmjcX9/v8K2Fnv16Jt7L/b3ggsRoNZDaVXKjtxp18B22TouSbvwdQlfQp8byNqes2HpG+++KayJnj4A4WrysFT26ZSt0vSgpvCEqq1QBmyMVqrZmXpQs7MMwxWwbO3KuK1B6446vr6+snvqcOOOkiEAAQhAAAIQCJuA/PSE8AuoQEgOCEAAAhAoIYCnsbeusYwX3p44VqWsJ5O+kq2B7bJ1XJJ24esSvoQ+d4aOL4B9qggqTVD6Ks+Wimy8P8+sd+wVWVAq96pZpjDUHI7taCWvpBFzPNegdUcdhacRo7G3YbiMuYsnjlUp68mkr2RrYLtsHZekXfi6hC+hz52h47Pcp4qg0qxNXwF/JSqjZlADrZ0wK2lEjMam3aOB0di0aNJDAAIQgAAEIAABCEAAAhCAQCAEWm+/0sBobF1HIIxGEGMZL7w9Qa1KWU8mfSVbA9tl67gk7cLXJXwJfe4Ma3u1vzZ98TT6jIIZpVl2B162dmXdbA1ad9SRjXBmdI9CVAhAAAIQgAAEIAABCEAAAhMQYPfUCaBTJQQgAAEIQAACEIAABCAAgbkQwGicS0shJwQgAAEIQAACEIAABCAAgQkIYDROAJ0qIQABCEAAAhCAAAQgAAEIzIXAko1G8fElfZzdxc0x3JmK9i5WaiceTqThSp5L50ZOfwLD9Zbq/u8vYZeUS9IufF3Cl9CzLy1GEfQtI7CSJkbN3ieBnmOqx2QracQeic2lqJm17PPzs9gZteLQ3KvThHj1diu/1Ssle7zcqL+GO6P0d1MqVmrDGk6k4UpOlNV0Bdxoe+vUSV8ygvCzlobGOMFwG663lPT/UXVcknbh6xK+hJ6Pq3EVmf45uzZ9RTdYicqo2fskUD2mF/wUG1s7z3vywMmm0XpWw/Pl5SVaqtGYWIqp1TjcmYq5frFSu9sPJ9JwJRtlt9JYFP09azLKy/qkucRPfxrTGI3D9Zay/j/m43ZJ2oWvS/gSek48RlZkmvmKxWJt+lqvk0eaJEzVxCtp2WWrOXftxCzQ8uLIP0M7o9/Xjzkz0XffebWsMBoXG5568O5od/PjSfaBpx83O/HfcGcqnODFSu3Ew4k0XMlG/s+XD6d7pw+Xn0/y+p9kL/HTBlVNY5p4iuF6S3X/H0fbJWkXvi7hS+jZ6xajCPqWEVhJE6Nm75NAzzHVY7K5N+LJt7fbo4tPV093Z4cXR7f35wehnemxsRoVNb+WXaqnUTu81LHZbnV86oBnKqIKi2LkgjlHE7IvILGyMt40jgBOSo5iv6N1KX6XkqTkp4rojbk5aEwSnjrk0HD2/5Hf5/XV833KGTrA2EeGvtK006Wv2n3KaSehp7PRR4C+0kzykjvHoS9dfMoJQd9BpwRFCBOq7NMifaVBTc/bS9NkfTWQTznDNKKc+thzH728KZwzw2hd384+LdJXmo46Ljk8NWeY5WIoi1GV3c/UzoNNmGb8HqKwFHAEITWWXpSVhWxd0am6fOsSP/1pDDoJrr979dE3fPpY7WDxEbVFmu49PxztwtclfAk9u9AIinR8lnsq4plsbfr28kysvTOE0MQradllqzlX7ZSFmLERAzsz+QgNv2UXbTQa/GarluHOqMeFex5crNRpzo4gZF/qJ8oq760dj50oFp9LLvHTBlVNo6IjeU732iXrq2/4lDO+jj5S9ZVmaO36ktOnnHa6+JTcV5p2EnqOkb6E9ClnouU0GRI+cvaVJgR9bUtxhOfvhCr31Wo+5aCm5+2laTIf+H2lGaQRkzEmhEy3qFShaaGcmWZNY+rDmcNdaNFGYxpxl27VIjqnPoxPr68zFQ6iYhU5s3EgkfpSzSl/yjAd8Fot0/H1vUCEBie0+VlDQ2/2O8XuqcEMlqZPUs/0w42FstHhKViLZOHrEr6EntjHVGTyl9zahhrtYRSCvutReSUtu2w156ydcikm026pyPYysDPyEwBT3ZRm1LLCaNwTaxr39/fjZ4XrP/GdQ+1Dq0jDJUFAgFoPpVUpO3L3XgPbZeu4JO3C1yV8CX1uIGt7zq5NXz1DWMNUCjV9xnvgaVbSiLlWWIPWHXV8fX1d7O6pgY9JxIMABCAAAQhAAAIQgAAEIDALAhiNs2gmhIQABCAAAQhAAAIQgAAEIDANAd/w1Gmko1YIQAACEIAABCAAAQhAAAIQ6Eyg9Uo6EZ7qazS2rqOzdrMpYBlLazxxr0pZTyZ9JVsD22XruCTtwtclfAl97gwdl5r4VBFUmrXpK+CvRGXUDGqgtRNmJY2Yg7MGrTvqyJrGdgOKXBCAAAQgAAEIQAACEIAABNZCgDWNa2lp9IQABCAAAQhAAAIQgAAEINCCAEZjC2hkgQAEIAABCEAAAhCAAAQgsBYCGI1raWn0hAAEIAABCEAAAhCAAAQg0ILAko3GuzOx5lMeZ3cxmeHOVKAvVmonHk6k4Upu0c/IEjiB4XpLdf8fB8uStAtfl/Al9Ox1i1EEfcsIrKSJUbP3SaDnmOox2UoasUdicylqZi37/PwsdkatODT36jQhXr3dRpvLRynZ4+VG/TXcGaW/m1KxUhvWcCINV3KirKYr4EbbW6dO+pIRhJ+1NDTGCYbbcL2lpP+PquOStAtfl/Al9HxcjavI9M/ZtekrusFKVEbN3ieB6jG94KfY2Np53pMHTjaN1rMani8vL9FSjcbEUkytxuHOVMz1i5Xa3X44kYYr2Si7lcai6O9Zk1Fe1ifNJX7605jGaByut5T1/zEft0vSLnxdwpfQc+IxsiLTzFcsFmvT13qdPNIkYaomXknLLlvNuWsnZoGWF0f+GdoZ/b5+zJmJvvvOq2WF0bjY8NSDd0e7mx9Psg88/bjZif+GO1PhBC9WaiceTqThSjbyf758ON07fbj8fJLX/yR7iZ82qGoa08RTDNdbqvv/ONouSbvwdQlfQs9etxhF0LeMwEqaGDV7nwR6jqkek829EU++vd0eXXy6ero7O7w4ur0/PwjtTI+N1aio+bXsUj2N2uGljs12q+NTBzxTEVVYFCMXzDmakH0BiZWV8aZxBHBSchT7Ha1L8buUJCU/VURvzM1BY5Lw1CGHhrP/j/w+r6+e71PO0AHGPjL0laadLn3V7lNOOwk9nY0+AvSVZpKX3DkOfeniU04I+g46JShCmFBlnxbpKw1qet5emibrq4F8yhmmEeXUx5776OVN4ZwZRuv6dvZpkb7SdNRxyeGpOcMsF0NZjKrsfqZ2HmzCNOP3EIWlgCMIqbH0oqwsZOuKTtXlW5f46U9j0Elw/d2rj77h08dqB4uPqC3SdO/54WgXvi7hS+jZhUZQpOOz3FMRz2Rr07eXZ2LtnSGEJl5Jyy5bzblqpyzEjI0Y2JnJR2j4Lbtoo9HgN1u1DHdGPS7c8+BipU5zdgQh+1I/UVZ5b+147ESx+FxyiZ82qGoaFR3Jc7rXLllffcOnnPF19JGqrzRDa9eXnD7ltNPFp+S+0rST0HOM9CWkTzkTLafJkPCRs680IehrW4ojPH8nVLmvVvMpBzU9by9Nk/nA7yvNII2YjDEhZLpFpQpNC+XMNGsaUx/OHO5CizYa04i7dKsW0Tn1YXx6fZ2pcBAVq8iZjQOJ1JdqTvlThumA12qZjq/vBSI0OKHNzxoaerPfKXZPDWawNH2SeqYfbiyUjQ5PwVokC1+X8CX0xD6mIpO/5NY21GgPoxD0XY/KK2nZZas5Z+2USzGZdktFtpeBnZGfAJjqpjSjlhVG455Y07i/vx8/K1z/ie8cah9aRRouCQIC1HoorUrZkbv3GtguW8claRe+LuFL6HMDWdtzdm366hnCGqZSqOkz3gNPs5JGzLXCGrTuqOPr6+tid08NfEwiHgQgAAEIQAACEIAABCAAgVkQwGicRTMhJAQgAAEIQAACEIAABCAAgWkI+IanTiMdtUIAAhCAAAQgAAEIQAACEIBAZwKtV9KJ8FRfo7F1HZ21m00By1ha44l7Vcp6Mukr2RrYLlvHJWkXvi7hS+hzZ+i41MSniqDSrE1fAX8lKqNmUAOtnTAracQcnDVo3VFH1jS2G1DkggAEIAABCEAAAhCAAAQgsBYCrGlcS0ujJwQgAAEIQAACEIAABCAAgRYEMBpbQCMLBCAAAQhAAAIQgAAEIACBtRDAaFxLS6MnBCAAAQhAAAIQgAAEIACBFgSWbDTenYk1n/I4u4vJDHemAn2xUjvxcCINV3KLfkaWwAkM11uq+/84WJakXfi6hC+hZ69bjCLoW0ZgJU2Mmr1PAj3HVI/JVtKIPRKbS1Eza9nn52exM2rFoblXpwnx6u022lw+SskeLzfqr+HOKP3dlIqV2rCGE2m4khNlNV0BN9reOnXSl4wg/KyloTFOMNyG6y0l/X9UHZekXfi6hC+h5+NqXEWmf86uTV/RDVaiMmr2PglUj+kFP8XG1s7znjxwsmm0ntXwfHl5iZZqNCaWYmo1DnemYq5frNTu9sOJNFzJRtmtNBZFf8+ajPKyPmku8dOfxjRG43C9paz/j/m4XZJ24esSvoSeE4+RFZlmvmKxWJu+1uvkkSYJUzXxSlp22WrOXTsxC7S8OPLP0M7o9/Vjzkz03XdeLSuMxsWGpx68O9rd/HiSfeDpx81O/DfcmQoneLFSO/FwIg1XspH/8+XD6d7pw+Xnk7z+J9lL/LRBVdOYJp5iuN5S3f/H0XZJ2oWvS/gSeva6xSiCvmUEVtLEqNn7JNBzTPWYbO6NePLt7fbo4tPV093Z4cXR7f35QWhnemysRkXNr2WX6mnUDi91bLZbHZ864JmKqMKiGLlgztGE7AtIrKyMN40jgJOSo9jvaF2K36UkKfmpInpjbg4ak4SnDjk0nP1/5Pd5ffV8n3KGDjD2kaGvNO106at2n3LaSejpbPQRoK80k7zkznHoSxefckLQd9ApQRHChCr7tEhfaVDT8/bSNFlfDeRTzjCNKKc+9txHL28K58wwWte3s0+L9JWmo45LDk/NGWa5GMpiVGX3M7XzYBOmGb+HKCwFHEFIjaUXZWUhW1d0qi7fusRPfxqDToLr71599A2fPlY7WHxEbZGme88PR7vwdQlfQs8uNIIiHZ/lnop4Jlubvr08E2vvDCE08UpadtlqzlU7ZSFmbMTAzkw+QsNv2UUbjQa/2apluDPqceGeBxcrdZqzIwjZl/qJssp7a8djJ4rF55JL/LRBVdOo6Eie0712yfrqGz7ljK+jj1R9pRlau77k9CmnnS4+JfeVpp2EnmOkLyF9yploOU2GhI+cfaUJQV/bUhzh+Tuhyn21mk85qOl5e2mazAd+X2kGacRkjAkh0y0qVWhaKGemWdOY+nDmcBdatNGYRtylW7WIzqkP49Pr60yFg6hYRc5sHEikvlRzyp8yTAe8Vst0fH0vEKHBCW1+1tDQm/1OsXtqMIOl6ZPUM/1wY6FsdHgK1iJZ+LqEL6En9jEVmfwlt7ahRnsYhaDvelReScsuW805a6dcism0WyqyvQzsjPwEwFQ3pRm1rDAa98Saxv39/fhZ4fpPfOdQ+9Aq0nBJEBCg1kNpVcqO3L3XwHbZOi5Ju/B1CV9CnxvI2p6za9NXzxDWMJVCTZ/xHnialTRirhXWoHVHHV9fXxe7e2rgYxLxIAABCEAAAhCAAAQgAAEIzIIARuMsmgkhIQABCEAAAhCAAAQgAAEITEPANzx1GumoFQIQgAAEIAABCEAAAhCAAAQ6E2i9kk6Ep/oaja3r6KzdbApYxtIaT9yrUtaTSV/J1sB22TouSbvwdQlfQp87Q8elJj5VBJVmbfoK+CtRGTWDGmjthFlJI+bgrEHrjjqyprHdgCIXBCAAAQhAAAIQgAAEIACBtRBgTeNaWho9IQABCEAAAhCAAAQgAAEItCCA0dgCGlkgAAEIQAACEIAABCAAAQishQBG41paGj0hAAEIQAACEIAABCAAAQi0ILBko/HuTKz5lMfZXUxmuDMV6IuV2omHE2m4klv0M7IETmC43lLd/8fBsiTtwtclfAk9e91iFEHfMgIraWLU7H0S6Dmmeky2kkbskdhcippZyz4/P4udUSsOzb06TYhXb7fR5vJRSvZ4uVF/DXdG6e+mVKzUhjWcSMOVnCir6Qq40fbWqZO+ZAThZy0NjXGC4TZcbynp/6PquCTtwtclfAk9H1fjKjL9c3Zt+opusBKVUbP3SaB6TC/4KTa2dp735IGTTaP1rIbny8tLtFSjMbEUU6txuDMVc/1ipXa3H06k4Uo2ym6lsSj6e9ZklJf1SXOJn/40pjEah+stZf1/zMftkrQLX5fwJfSceIysyDTzFYvF2vS1XiePNEmYqolX0rLLVnPu2olZoOXFkX+Gdka/rx9zZqLvvvNqWWE0LjY89eDd0e7mx5PsA08/bnbiv+HOVDjBi5XaiYcTabiSjfyfLx9O904fLj+f5PU/yV7ipw2qmsY08RTD9Zbq/j+OtkvSLnxdwpfQs9ctRhH0LSOwkiZGzd4ngZ5jqsdkc2/Ek29vt0cXn66e7s4OL45u788PQjvTY2M1Kmp+LbtUT6N2eKljs93q+NQBz1REFRbFyAVzjiZkX0BiZWW8aRwBnJQcxX5H61L8LiVJyU8V0Rtzc9CYJDx1yKHh7P8jv8/rq+f7lDN0gLGPDH2laadLX7X7lNNOQk9no48AfaWZ5CV3jkNfuviUE4K+g04JihAmVNmnRfpKg5qet5emyfpqIJ9yhmlEOfWx5z56eVM4Z4bRur6dfVqkrzQddVxyeGrOMMvFUBajKrufqZ0HmzDN+D1EYSngCEJqLL0oKwvZuqJTdfnWJX760xh0Elx/9+qjb/j0sdrB4iNqizTde3442oWvS/gSenahERTp+Cz3VMQz2dr07eWZWHtnCKGJV9Kyy1ZzrtopCzFjIwZ2ZvIRGn7LLtpoNPjNVi3DnVGPC/c8uFip05wdQci+1E+UVd5bOx47USw+l1zipw2qmkZFR/Kc7rVL1lff8ClnfB19pOorzdDa9SWnTzntdPEpua807ST0HCN9CelTzkTLaTIkfOTsK00I+tqW4gjP3wlV7qvVfMpBTc/bS9NkPvD7SjNIIyZjTAiZblGpQtNCOTPNmsbUhzOHu9CijcY04i7dqkV0Tn0Yn15fZyocRMUqcmbjQCL1pZpT/pRhOuC1Wqbj63uBCA1OaPOzhobe7HeK3VODGSxNn6Se6YcbC2Wjw1OwFsnC1yV8CT2xj6nI5C+5tQ012sMoBH3Xo/JKWnbZas5ZO+VSTKbdUpHtZWBn5CcApropzahlhdG4J9Y07u/vx88K13/iO4fah1aRhkuCgAC1HkqrUnbk7r0GtsvWcUnaha9L+BL63EDW9pxdm756hrCGqRRq+oz3wNOspBFzrbAGrTvq+Pr6utjdUwMfk4gHAQhAAAIQgAAEIAABCEBgFgQwGmfRTAgJAQhAAAIQgAAEIAABCEBgGgK+4anTSEetEIAABCAAAQhAAAIQgAAEINCZQOuVdISndmZPARCAAAQgAAEIQAACEIAABBZNwNfT2NowXTQ9lIMABCAAAQhAAAIQgAAEIBA0ATbCCbp5EA4CEIAABCAAAQhAAAIQgMDcCbARztxbEPkhAAEIQAACEIAABCAAAQgMSACjcUC4FA0BCEAAAhCAAAQgAAEIQGDuBDAa596CyA8BCEAAAhCAAAQgAAEIQGBAAhiNA8KlaAhAAAIQgAAEIAABCEAAAnMngNE49xZEfghAAAIQgAAEIAABCEAAAgMSwGgcEC5FQwACEIAABCAAAQhAAAIQmDsB3+80zl1P5IcABCAAAQhAAAIQgAAEILBaAm9vb+10f319xdPYDh25IAABCEAAAhCAAAQgAAEIrIKAr6extWG6CoooCQEIQAACEIAABCAAAQhAIEgCe3t7Qq7WBh2exiBbFaEgAAEIQAACEIAABCAAAQgEQ4Dw1GCaAkEgAAEIQAACEIAABCAAAQiERwCjMbw2QSIIQAACEIAABCAAAQhAAALBEMBoDKYpEAQCEIAABCAAAQhAAAIQgEB4BDAaw2sTJIIABCAAAQhAAAIQgAAEIBAMAYzGYJoCQSAAAQhAAAIQgAAEIAABCIRHAKMxvDZBIghAAAIQgAAEIAABCEAAAsEQwGgMpikQBAIQgAAEIAABCEAAAhCAQHgEMBrDaxMkggAEIAABCEAAAhCAAAQgEAwBjMZgmgJBIAABCEAAAhCAAAQgAAEIhEcAozG8NkEiCEAAAhCAAAQgAAEIQAACwRDAaAymKRAEAhCAAAQgAAEIQAACEIBAeAT+tLe3F55USAQBCEAAAhCAAAQgAAEIQAACQRDA0xhEMyAEBCAAAQhAAAIQgAAEIACBMAlgNIbZLkgFAQhAAAIQgAAEIAABCEAgCAJ7f//73//85z9XyEL8ahANhRAQgAAEIAABCEAAAhCAAATaEnh7e2uX9fX1FU9jO3TkggAEIAABCEAAAhCAAAQgsAoC9Z7GVWBASQhAAAIQgAAEIAABCEAAAhAoEMDTSKeAAAQgAAEIQAACEIAABCAAgSoChKfSPyAAAQhAAAIQgAAEIAABCECglABGI50DAhCAAAQgAAEIQAACEIAABDAa6QMQgAAEIAABCEAAAhCAAAQg0JzAn/iiRnNo5IAABCAAAQhAAAIQgAAEILAWAnv/+7//+0//9E/2VzvM38U/NJXWn/hYC1T0hAAEIAABCEAAAhCAAAQgMB2BnGvQ/Kz4o0zYf/zjH/8fy59cfpkuxHEAAAAASUVORK5CYII=)

