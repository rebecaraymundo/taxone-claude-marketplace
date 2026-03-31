# Relatorio_Conferencia_Lucro_Real_LALUR_LACS

- **Fonte:** Relatorio_Conferencia_Lucro_Real_LALUR_LACS.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 246 KB

---

__Atenção:__ Para recuperar a versão, considerar a versão compatível com o período ‘01/01 do ano anterior’ até ‘01/01 do ano informado no exercício’\.

	

THOMSON REUTERS

Relatório de Conferência do Lucro Real – LALUR/LACS 

##### DOCUMENTO DE REQUISITO

__Data__

__MFS__

__Descrição__

__Autor__

27/08/2018

MFS\-20624

Criação do documento

Alessandra Cristina Navatta

Sumário

[1\.	INTRODUÇÃO	3](#_Toc525906928)

[2\.	DOCUMENTOS DE REFERÊNCIA	3](#_Toc525906929)

[3\.	Tela de Parâmetros	3](#_Toc525906930)

[4\.	LEIAUTE	9](#_Toc525906931)

[4\.1\.	Regras dos campos do Relatório \(Leiaute\)	11](#_Toc525906932)

[4\.2\.	Exemplos do Relatório	22](#_Toc525906933)

# <a id="_Toc525906928"></a><a id="_Toc361822343"></a>INTRODUÇÃO

Objetivo desta especificação é criar uma *tela para permitir ao usuário parametrizar dados e gerar o relatório de Conferência dos registros exibidos na tela Lucro Real – Demonstração, dos registros do bloco M*\.

# <a id="_Toc525906929"></a>DOCUMENTOS DE REFERÊNCIA

- Layout\_ECF\.xlsx
- Tela\_Lucro\_Real\-Registros\_de\_Tabela\_Dinamica\.doc

# <a id="_Toc522613784"></a><a id="_Toc522722809"></a><a id="_Toc525906930"></a><a id="_Toc396377211"></a>Tela de Parâmetros

<a id="_Toc359395873"></a>__Localização da tela:__  ECF \- Escrituração Contábil Fiscal >>Relatórios >> Conferência do Lucro Real >> LALUR/LACS 

__Título da tela:__ Conferência do Lucro Real – LALUR/LACS

As regras destacadas em amarelo \(e com fonte vermelha\), não serão implementadas neste momento\.

__Campo__

__Tipo__

__Formato/Default__

__Obrig\. __

__Editável__

__Regra__

__MFS__

Exercício

Texto

AAAA 

Sim

Sim

Informar o exercício que será utilizado para recuperar as Informações ECF\.

Tratamentos:

- Trazer o campo preenchido, com o ano atual\.
- Se o campo exercício, for alterado, os demais campos devem ser limpos \(inclusive os campos de opções definidas com default\), para serem novamente definidos\.

MFS\-20624

Versão

Lista

Código \- Descrição

Sim 

Sim

Permite ao usuário indicar a versão que será utilizada para recuperar as Informações ECF\.

Lista de Opções Válidas:

Exibir a lista de versões da RNG00004 – Versão de layout\.

__Atenção:__ Para recuperar a versão, considerar a versão compatível com o período ‘01/01 do ano anterior’ até ‘01/01 do ano informado no exercício’\.

__Tratamentos:__

Se este campo for alterado, os demais campos, exceto o campo exercício, devem ser limpos \(inclusive os campos de opções definidas com default\), para serem novamente definidos

MFS\-20624

Apuração

Lista

S

N

__Default:__

Anual

__Formato:__

Descrição

Permite que o usuário informe o tipo de Apuração\.

Valores válidos:

Anual

Trimestral

MFS\-20624

Data Inicial

Data

S

S

__DD/MM/AAAA__

Permite que o usuário escolha uma data inicial para gerar o relatório\.

 

MFS\-20624

Data Final

Data

S

S

__DD/MM/AAAA__

Permite que o usuário escolha uma data final para gerar o relatório\.

MFS\-20624

Tipo do Relatório:

Radiobutton

S

S

__Default:__

Sintético

Permite que o usuário selecione o tipo do relatório\.

__Conteúdos Válidos:__

Sintético 

Analítico 

MFS\-20624

Apenas Registros com Movimento

Check\-box

__Default:__

Marcado

Permite que o usuário escolha a forma de exibição das informações no relatório, se deseja visualizar apenas os registros que possuam movimento ou todos os registros\.

__Tratamentos:__

Quando o usuário selecionar a opção “Apenas Registros com Movimento”, apresentar no relatório apenas os registros cujo campo “Valor” seja diferente de zero\.

Atenção para o relatório Sintético: Devido à quebra do relatório em mais de uma página, a linha que possuir valor diferente de zero, em pelo menos um mês/trimestre \(dentro da escrituração\), a mesma deve sair em todas as páginas do relatório\.

Esta regra acima não se aplica ao relatório Analítico, que possui estrutura diferente de exibição de valor\.

Quando o usuário desmarcar a opção “Apenas Registros com Movimento”, apresentar no relatório todos os registros\.

MFS\-20624

Relatório Analítico – Exibir os lançamentos associados dos registros do Bloco M

Checkbox

S

S

Desabilitado

Permite que o usuário escolha se na geração do relatório analítico dos registros do Bloco M, seja exibido os lançamentos das associações das contas contábeis caso existam\.

Tratamento:

Habilitar esse campo apenas quando o “Tipo do Relatório” for igual a “Analítico” 

Ao habilitar, apresentar com marcação selecionada\.

Se o usuário desmarcar essa opção, não exibir nenhum lançamento associado às contas contábeis, caso existam, na geração do relatório analítico dos registros do Bloco M\.

MFS\-20624

Gravar Arquivos

Radio\-Button

Arquivo Único

Sim

Sim

Opções Válidas:

- Quebra por Informações ECF
- Arquivo Único

__Tratamentos:__

- Se selecionada a opção ‘Quebra por Estabelecimentos’, será gerado um relatório por Informações ECF, com todos os registros selecionados\.
- Se selecionada a opção ‘Arquivo Único’, será gerado em um único relatório, contendo todas as Informações ECF recuperadas, com os dados de todos os registros selecionados\.
- Se este campo for alterado, os demais campos não devem ser limpos\.

MFS\-20624

__Informações ECF dos Estabelecimentos__

Informações ECF\(\*\)

Check\-box

Código Estab \- CGC \- Exercício \-  Data Inicial da Escrituração   
\(076 \- XXXXXXXXXXXXXX \-  01/03/2017\)

\-

\-

Permite ao usuário selecionar um ou mais registros de Informações ECF\.

__Tratamentos:__

Recuperar apenas as Informações ECF que estão compatíveis com as opções de filtro preenchidas na tela de parametrização do relatório\. 

MFS\-20624

Marcar Todos

Check\-box

Desmarcado

\-

\-

Permite ao usuário selecionar todas ou desmarcar todas as Informações ECF\.

__Tratamentos:__

- Se selecionar o check\-box, todos os registros exibidos no componente de Informações serão marcados\. 
- Se desmarcar o check\-box, o sistema deve desmarcar todos os registros de Informações ECF selecionados\.

MFS\-20624

__Registros __

Registros \(\*\)

Check\-box

Cód\. \- Descrição

\-

\-

Permite ao usuário selecionar um ou mais registros do Lucro Real do Bloco M , da Tela Demonstraçãopara gerar o relatório\.

Tratamentos:

- Só deve ser exibido os registros, quando o campo versão estiver preenchido\.
- Recuperar os registros do bloco M, compatível com a versão que foi indicada na tela de parâmetros do relatório 

Lista de Registros Válidos:

M300 

M350 

M410

M500

MFS\-20624

Marcar Todos

Check\-box

Desmarcado

\-

\-

Permite ao usuário selecionar todos ou desmarcar todos os registros de tabela dinâmica\.

Tratamentos:

- Se selecionar o check\-box, todos os registros exibidos no componente de Registros serão marcados\. 
- Se desmarcar o check\-box, o sistema deve desmarcar todos os registros do componente de Registros\.

MFS\-20624

OK

Botão

\-

\-

Permite ao usuário gerar um relatório de conferência dos registros selecionados\.

Tratamentos:

- Se o usuário clicar em OK, sem ter selecionado pelo menos uma Informação ECF, exibir a mensagem DW00057\.
- Aplicar RNG00010 – Campo Obrigatório
- Se não houver dados para a composição do relatório, exibir a mensagem DW00274\.
- Se a “Data Inicial” for posterior ao “Data Final”, exibir a mensagem DW00212\.
- Aplicar a regra RNG00010 \- Campo Obrigatório\.

Gerar o relatório conforme tópico “[4\. LEIAUTE](#Leiaute)”\.

__Atenção: __Será recuperada e exibida nos relatórios as apurações que estão compreendidas integralmente entre as datas inicial e final indicadas na tela de geração do relatório\.

MFS\-20624

Cancelar

Botão

\-

\-

Permite ao usuário fechar a tela e não executar o relatório\.

MFS\-20624

<a id="_Toc398564359"></a>

# <a id="_Toc525906931"></a><a id="Leiaute"></a>LEIAUTE

__Origem das informações para geração do relatório:__

- Tela Lucro Real, registros oriundos de Tabela Dinâmica \(todos os registros processados da tabela dinâmica do bloco M\)\. 
- Registros M300, M350
- Tela Lucro Real, demais registros  
- Registros M410, M500

__Tipos de Relatórios:__

- Sintético 
- Analítico 

Os registros M410 e M500 não consideram esse parâmetro \(serão gerados com o mesmo leiaute, independentemente do tipo de relatório escolhido\) \.

__Regra de agrupamento: __

- Agrupar por Informação do ECF, por registro e período de apuração\. 

__Ordenação: __

- Ordenar por código do estabelecimento, data inicial Informação ECF, período de apuração, código do registro \(seguindo a hierarquia dos registros de acordo com o arquivo Layout\_ECF\.xlsx\) e 

Se registro oriundo de Tabelas Dinâmicas:

- 
	- Código da linha da tabela dinâmica\. Todos de forma crescente\.
- Nos relatórios analíticos, ordenar os campos Conta Contábil e Centro de Custo, se houver, de forma crescente\.

Para o registro M410:

- 
	- Ordenar por CNPJ da empresa, data inicial Informação ECF, período de apuração, código do registro, grupo da conta, conta da parte b, tributo, data do lançamento e
		- Apresentar inicialmente os registros que possuem o campo Conta da Parte B Origem da Contrapartida, sem preenchimento\. 

__Busca de Registros: __

- Considerar as informações que foram processadas e exibidas na tela do Lucro Real, de acordo com as informações de filtro indicadas na tela de geração do relatório\. Não será possível selecionar a apuração anual nos períodos Inicial e Final, na tela de geração do relatório, se existir dados referente a apuração Anual \(A00\), a mesma deve ser exibida no relatório\.
- Para os demais registros \(M410, M500\), não será considerado o tipo de relatório, ou seja, se marcados esses registros serão gerados sempre em um único leiaute\.

### <a id="_Toc525906932"></a>Regras dos campos do Relatório \(Leiaute\)

__Campo/Coluna__

__Tipo__

__Formato/Default__

__Regra__

__MFS__

Cabeçalho\(\*\)

Empresa\(\*\)

Texto

Código \- Descrição

Apresenta no lado superior esquerdo do cabeçalho, a empresa do estabelecimento, que está sendo gerado os dados do relatório\. 

MFS\-20624

Página X de Y

Texto

Página X de Y

Apresenta no lado superior direito do cabeçalho, o número da página atual \(X\) e a quantidade total de páginas do relatório \(Y\)\.

MFS\-20624

Data 

Data

DD/MM/AAAAA às HH:MM:SS hs

Apresenta no lado superior direito do cabeçalho, a data, hora, minuto e segundo em que o relatório foi gerado\.

MFS\-20624

__Corpo do Relatório \(\*\)__

__Título1:__ \(\*\)

__Relatório de Conferência do Lucro Real\- LALUR/LACS \- Sintético __

__Título 2:__ \(\*\)

__Relatório de Conferência do Lucro Real \- LALUR/LACS \- Analítico__

Exibir somente um dos títulos de acordo com o tipo de relatório parametrizado na tela de geração\.\(\*\)

Estabelecimento

Texto

Código \- Descrição

Exibe o estabelecimento de cada Informações ECF que foi recuperada\.

MFS\-20624

Exercício

Texto

AAAA

Exibe o exercício correspondente a cada Informações ECF, que foi recuperada\.

MFS\-20624

Data Inicial

Texto

DD/MM/AAAA

Exibe a data inicial correspondente a cada Informações ECF que foi recuperada\.

MFS\-20624

Versão 

Texto

\-

Exibe a versão correspondente a cada Informações ECF recuperada\.

MFS\-20624

Forma de Tributação

Texto

\-

Exibe a forma de tributação correspondente a cada Informações ECF que foi recuperada\.

MFS\-20624

Apuração

Texto

\-

Exibe a apuração correspondente a cada Informação ECF que foi recuperada\.

MFS\-20624

Relatório Sintético – Registros de Origem de Tabela Dinâmica \(\*\)

Registros Atendidos: M300, M350 \(\*\)

Cód\. Registro \- Descrição do Registro

<a id="RegraPeríodo"></a>Período \(\*\)

Texto

Descrição

Exibe a descrição de cada período informado, conforme as apurações que foram recuperadas, baseadas nos campos de data inicial e final na geração do relatório\. 

__Tratamento:__

Se existir mais de um período a ser exibido, os mesmos devem ser demonstrados em ordem crescente, um abaixo do outro, \(após a exibição de todos os códigos de linha do registro\)\.

Valores Válidos:

Se apuração = Anual:

Janeiro

Fevereiro

Março

Abril

Maio

Junho

Julho

Agosto

Setembro

Outubro

Novembro

Dezembro

Anual

Se apuração  =  Trimestral

1º Trimestre

2º Trimestre

3º Trimestre

4º Trimestre

[Registro M410](#VoltarM410)

MFS\-20624

LINHAS DA TABELA DINÂMICA

Texto

Código \- Descrição

Exibe o código e a descrição das linhas da tabela dinâmica de cada registro gerado\.

__Tratamentos:__

Exibir as linhas da tabela dinâmica, de acordo com a informação indicada no campo ‘Exibição dos Dados’ da tela de geração deste relatório\.

As linhas da tabela dinâmica, devem ser exibidas em ordem crescente\.

MFS\-20624

VALOR 

Texto

XX,XX ou 

\- XX,XX

Exibe o valor de cada linha da tabela dinâmica que foi recuperada\.

__Tratamento:__

Essa coluna irá exibir o saldo de cada linha e por período processado\.

MFS\-20624

DETALHAMENTO

Texto

Descrição

Exibe o tipo de detalhamento da linha da tabela dinâmica que foi recuperada\.

__Tratamento:__

__Valores Válidos:__

Conta Contábil

Entrada Manual

Fórmula

- Exibir com o texto ‘Fórmula’, se o tipo da linha igual a ‘CA’ e não existir associação ou se tipo da linha igual a ‘CNA’, 
- Exibir ‘Entrada Manual’, se o tipo da linha igual a ‘E’ e existir entrada manual na linha\.
- exibir ‘Conta Contábil’, se o tipo da linha igual a ‘E’, ou tipo da linha igual a ‘CA’ e existir associação\. 

__Para os registros do Bloco M:__

__Valores Válidos:__

Fórmula

‘nulo’

- Exibir com o texto ‘Fórmula’, se o tipo da linha igual a ‘CA’ e não existir associação ou se tipo da linha igual a ‘CNA’, nos demais casos, deixar o campo nulo\.

MFS\-20624

Relatório Analítico –  Registros de Origem de Tabela Dinâmica\(\*\)

Cód\. Registro \- Descrição do Registro

Para os registros M300, M350\(\*\)

LINHAS DA TABELA DINÂMICA

Texto

Cód \- Descrição

__Tratamentos:__

Exibir as linhas da tabela dinâmica, de acordo com a informação indicada no campo ‘Exibição dos Dados’ da tela de geração deste relatório\.

As linhas da tabela dinâmica, devem ser exibidas em ordem crescente\.

As linhas do tipo R, não terão detalhamento\. Os demais tipos, estão detalhados abaixo\. 

MFS\-20624

VALOR

Texto

X,XX ou \-XX,XX 

Exibe o valor da linha da tabela dinâmica recuperada\.

MFS\-20624

Detalhamento das linhas da tabela dinâmica com tipos E \(\*\)

CONTA CONTÁBIL

Texto

Cód \- Descrição

Exibir o código e a descrição da conta contábil associada à linha da tabela dinâmica\.

Tratamentos:

As contas devem ser apresentadas por ordem de código\.

MFS\-20624

CENTRO DE CUSTO

Texto

Cód \- Descrição

 Exibe o código e a descrição do centro de custo associado, caso exista\.

Tratamentos:

As contas devem ser apresentadas por ordem de código\.

MFS\-20624

VALOR

Texto

X,XXC ou

X,XXD

Exibir o valor da conta contábil e centro de custo \(este último, se existir\), referente a linha da tabela dinâmica\.

__Tratamento:__

Concatenar o valor com o indicador\.

MFS\-20624

Para os registros M300 e M350 \(\*\)

Detalhamento das linhas da tabela dinâmica com tipos E com informações de contas da parte B\(\*\)

Registros M305

CONTA DA PARTE B

Texto

Cód \- Descrição

Exibir o código e a descrição da conta da parte B\.

Tratamentos:

As contas devem ser apresentadas por ordem de código\.

MFS\-20624

VALOR

Texto

XX,XX

Exibir o valor da conta da parte B, referente a linha da tabela dinâmica\.

MFS\-20624

Detalhamento das linhas da tabela dinâmica com tipos E com informações de contas contábeis\(\*\)

Registros M310M360\(\*\)

Cód\. Registro \- Descrição do Registro

CONTA CONTÁBIL

Texto

Cód \- Descrição

Exibir o código e a descrição da conta contábil associada à linha da tabela dinâmica\.

__Tratamentos:__

As contas devem ser apresentadas por ordem de código\.

MFS\-20624

CENTRO DE CUSTO

Texto

Cód \- Descrição

 Exibe o código e a descrição do centro de custo associado, caso exista\.

__Tratamentos:__

As contas devem ser apresentadas por ordem de código\.

MFS\-20624

VALOR

Texto

X,XXC ou

X,XXD

Exibir o valor da conta contábil e centro de custo \(este último, se existir\), referente a linha da tabela dinâmica\.

__Tratamento:__

Concatenar o valor com o indicador\.

MFS\-20624

RECUPERAÇÃO DE VALORES

Texto

Cód\. \- Descrição

Exibe a informação utilizada para a recuperação dos valores \(de cada conta contábil\)\.

MFS\-20624

Detalhamento das linhas da tabela dinâmica com tipos E com informações de contas contábeis M312/M362\(\*\)

Cód\. Registro \- Descrição do Registro

LANÇAMENTO

Texto

Descrição

Exibe a informação de número de lançamento \(se existir\)

__Tratamento:__

Apresentar os lançamentos, ordenado pelo campo número, se existir lançamentos e o parâmetro ‘Relatório Analítico – Exibir os lançamentos associados dos registros do Bloco M’, estiver selecionado na tela de geração do relatório\.

MFS\-20624

VALOR

Texto

XX,XXC ou

XX,XXD

Exibe o valor do lançamento contábil\.

__Tratamento:__

Concatenar o valor com o indicador\.

MFS\-20624

DEMAIS REGISTROS \(\*\)

M410, M500 \(\*\)

 <a id="VoltarM410"></a>Relatório do Registro M410 \(independente se tipo do Relatório = Sintético ou Analítico\) \(\*\)

Cód\. Registro \- Descrição do Registro

PERÍODO \(\*\)

Texto

Descrição

Ver regra do campo [Período](#RegraPeríodo)

MFS\-20624

GRUPO DA CONTA

Texto

Cód\.

Exibe o código e a descrição do grupo da Conta da Parte B

Tratamentos:

Ordenar pelo campo código\.

MFS\-20624

CONTA DA PARTE B

Texto

Cód\. \- Descrição

Exibe o código e a descrição da Conta da Parte B

Tratamentos:

Ordenar as contas pelo campo código\.

MFS\-20624

TRIBUTO

Texto

Cód\. \- Descrição

Exibe o código e a descrição do tributo da conta da parte B

Tratamentos:

Ordenar pelo campo código\.

MFS\-20624

DATA LANÇAMENTO

Texto

DD/MM/AAAA

Exibe a data do Lançamento do ajuste da Conta da Parte B\.

Tratamentos:

Ordenar pelo campo data lançamento\.

MFS\-20624

VALOR

Texto

x\.xxx,xxCR, ou x\.xxx,xxDB

Exibe o valor do lançamento da Conta da Parte B e o indicador

MFS\-20624

CONTRAPARTIDA

Texto

Cód\. \- Descrição

Exibe a Conta da Parte B, que será gerado o lançamento de Contrapartida\.

MFS\-20624

CONTA DA PARTE B ORIGEM DA CONTRAPARTIDA

Texto

Cód\. \- Descrição

Exibe a Conta da Parte B, que originou o lançamento de Contrapartida\.

MFS\-20624

HISTÓRICO

Texto

Descrição

Exibe o valor do lançamento da Conta da Parte B\.

MFS\-20624

AJUSTE COM ORIGEM NA PARTE B

Texto

Cód\. \- Descrição

Exibe se o ajuste é incremental ou cumulativo\.

MFS\-20624

TRIBUTAÇÃO DIFERIDA

Texto

Descrição

Exibe se há ou não Tributação Diferida\.

MFS\-20624

Registro M415 – Processos \(\*\)

Cód\. Registro \- Descrição do Registro

TIPO 

Texto

Cód\. \- Descrição

Exibe o tipo de processo do ajuste\.

Tratamentos:

Ordenar pelo tipo de processo\.

MFS\-20624

NÚMERO 

Texto

Descrição

Exibe o número do processo\.

Tratamentos:

Ordenar pelo número de processo\.

MFS\-20624

Relatório do Registro M500 \(independente se tipo do Relatório = Sintético ou Analítico\) \(\*\)

Cód\. Registro \- Descrição do Registro

GRUPO DA CONTA

Texto

Cód\.

Exibe o código e a descrição do grupo da Conta da Parte B

Tratamentos:

Ordenar pelo campo código\.

MFS\-20624

CONTA DA PARTE B

Texto

Cód\. \- Descrição

Exibe o código e a descrição da Conta da Parte B

Tratamentos:

Ordenar as contas pelo campo código\.

MFS\-20624

TRIBUTO

Texto

Cód\. \- Descrição

Exibe o código e a descrição do tributo da conta da parte B

Tratamentos:

Ordenar pelo campo código\.

MFS\-20624

SALDO INICIAL

Texto

x\.xxx,xxC ou x\.xxx,xxD

Exibe o Saldo Inicial da Conta da Parte B\.

MFS\-20624

LANÇAMENTOS DA PARTE A

Texto

x\.xxx,xxC ou x\.xxx,xxD

Exibe o valor do Lançamento da parte A para a Conta da Parte B\.

MFS\-20624

LANÇAMENTOS DA PARTE B

Texto

x\.xxx,xxC ou x\.xxx,xxD

Exibe o valor do Lançamento da Parte B para a Conta da Parte B\.

MFS\-20624

LANÇAMENTOS DA PARTE B \- CONTRAPARTIDA

Texto

x\.xxx,xxC ou x\.xxx,xxD

Exibe o valor do Lançamento de Contrapartida da parte B para a Conta da Parte B\.

MFS\-20624

SALDO FINAL

Texto

x\.xxx,xxC ou x\.xxx,xxD

Exibe o Saldo Final da Conta da Parte B\.

MFS\-20624

Relatório do Registro N615 \(independente se tipo do Relatório = Sintético ou Analítico\) \(\*\)

Cód\. Registro \- Descrição do Registro

BASE DE CÁLCULO

Texto

x\.xxx,xx

Exibe o valor da base de cálculo do incentivo\.

MFS\-20624

PERCENTUAL FINOR

Texto

x,xxxx

Exibe o valor do percentual do incentivo\.

MFS\-20624

VALOR LÍQUIDO FINOR

Texto

x\.xxx,xx

Exibe o valor líquido do incentivo\.

MFS\-20624

PERCENTUAL FINAM

Texto

x,xxxx

Exibe o valor do percentual do incentivo\.

MFS\-20624

VALOR LÍQUIDO FINAM

Texto

x\.xxx,xx

Exibe o valor líquido do incentivo\.

MFS\-20624

VALOR TOTAL

Texto

x\.xxx,xx

Exibe o valor do incentivo\.

MFS\-20624

__Rodapé\(\*\)__

MasterSaf – Atendimento Fiscal

Texto

\-

Apresentar o texto do lado inferior esquerdo\.

MFS\-20624

ECF – Escrituração Contábil Fiscal

Texto

\-

Apresentar o texto do lado inferior direito\.

MFS\-20624

<a id="_Toc398564360"></a>

     \(\*\)Não exibir a descrição na tela/relatório\.<a id="_Toc412124419"></a>

### <a id="_Toc438651774"></a><a id="_Toc522628480"></a><a id="_Toc523143863"></a><a id="_Toc525906933"></a>Exemplos do Relatório 

Registros de Tabela Dinâmica – Sintético

![](data:image/png;base64,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)

Registros de Tabela Dinâmica – Analítico![](data:image/png;base64,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WYSdfe+LpGQp44znZj/qsyrHZaDOLLC0zr6zUr1Sphys1i4D/SFwOwFZrWOGvPLRXccEp1UCBAgQIECAAAECrQrEBy1ZttPqEOsXAQJ3EmhtB+Kdxk5fCRAgQIAAAQKbC9iBuDmxBggQIECAwMkE7EA82YAIhwABAgQIECBAgAABAgQIECBAoC2B1tZq+TixrfmpNwQIECBAgAABAgQIECBAgMCuAtZq7cqtMQIECBAgQIAAAQIECBAgQIAAgbsJeFr83UZcfwkQIECAAAECBAgQIECAAAECLQjIarUwivpAgAABAgQIECBAgAABAgQIELibgKzW3UZcfwkQIECAAAECBAgQIECAAAECLQjIarUwivpAgAABAgQIECBAgAABAgQIELibgKzW3UZcfwkQIECAAAECBAgQIECAAAECLQjIarUwivpAgAABAgQIECBAgAABAgQIELibgKzW3UZcfwkQIECAAAECBAgQIECAAAECLQjIarUwivpAgAABAgQIECBAgAABAgQIELibgKzW3UZcfwkQIECAAAECBAgQIECAAAECLQjIarUwivpAgAABAgQIECBAgAABAgQIELibgKzW3UZcfwkQIECAAAECBAgQIECAAAECLQh8PJ/Px+OxRVc+Pj7e1X5+fm5ReVlnaM4XAQIECBAgQCAT2O3dCHkCBAgQIECAQAMCO+dzZou9Xi9rtWbrOZEAAQIECBAgQIAAAQIECBAgQOAwgdbWavkw9rCppGECBAgQIHA+gat80ng+ORERIECAAAEC9xW4yjsoa7XuO0f1nAABAgQIECBAgAABAgQIECBwaQE7EC89fIInQIAAAQIECBAgQIAAAQIECNxUQFbrpgOv2wQIECBAgAABAgQIECBAgACBSwvIal16+ARPgAABAgQIECBAgAABAgQIELipgKzWTQdetwkQIECAAAECBAgQIECAAAEClxaQ1br08AmeAAECBAgQIECAAAECBAgQIHBTAVmtmw68bhMgQIAAAQIECBAgQIAAAQIELi0gq3Xp4RM8AQIECBAgQIAAAQIECBAgQOCmAs1mtT5+foWB7fvn+3gc+Vhm9ODoZEmrCt+PnrJ6gc7u1LRSGfAZ+ljTHWUIECBAgAABAgQIECBAgACBJgWazWoNjFbIMX1+/woJr/j/moP18yDUlrZSf+5wydHEU5pHCwFs9LWk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b1xBVxm4+l3tlQnKSR/YvJXSzyrKzx46a5u6rf4SYyFIAgQIECBAgACBcwrcJas1/HnyvFVCcUT7HluTDvk++3RGdyCmtz0zPmOv6cVUzIFbrPSGKuazptZ/zgtPVATOLFBe6TXX/pl71HBsyxOUy2tomFfXCBAgQIAAAQIETi7w8Xw+H4/HFlGmz+nYov6szp2b26FHmiBAYEDAJW96XFEgm7flAqu+hU7lOrvQ/c4K34WzmuORsp7hGrIPEmLhzsjTqmKBvshj8HEcN/rQwmvFFa8UMRMgQIAAAQLHClzlHdTr9ZLVOnaqaJ0AgZkCV3mdndk9pzUqYN7uP7DM9zfXIgECBAgQIHB1gau8g3pnte6yA/HqU0r8BAgQIECAAAECBAgQIECAAAECqYCslvlAgAABAgQIECBAgAABAgQIECBwPQFZreuNmYgJECBAgAABAgQIECBAgAABAgRktcwBAgQIECBAgAABAgQIECBAgACB6wnIal1vzERMgAABAgQIECBAgAABAgQIECAgq2UOECBAgAABAgQIECBAgAABAgQIXE9AVut6YyZiAgQIECBAgAABAgQIECBAgAABWS1zgAABAgQIECBAgAABAgQIECBA4HoCslrXGzMREyBAgAABAgQIECBAgAABAgQIyGqZAwQIECBAgAABAgQIECBAgAABAtcTkNW63piJmAABAgQIECBAgAABAgQIECBAQFbLHCBAgAABAgQIECBAgAABAgQIELiegKzW9cZMxAQIECBAgAABAgQIECBAgAABAh/P5/PxeGwB8fHx8a728/Nzi8rLOkNzvggQIECAAAECmcBu70bIEyBAgAABAgQaENg5nzNb7PV6Was1W8+JBAgQIECAAAECBAgQIECAAAEChwm0tlbrb//wh8MsNUyAwL4Cf/rb37rk9yXX2lKB96R9V2HeLnWccn4wt1ZripmyBAgQIECAwN0FrNW6+wzQfwIECBAgQIAAAQIECBAgQIAAgU0F7EDcijd8OBz+74sAAQIECBAgQIAAAQIECBAgQGBdgZazWu+MUl9SKfwo/rfEtLOJsDHK9qglsM4lQGAjgfRVq8y/lz8NYQyX3ChU1RIgQIAAAQIECBAgQGBAoNmsVsgohdRSZ//DT4fL1EydzsejhIOenFIDqAwBAgQIECBAgAABAgQIECBAYIZAs1mteRml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gAABAgQIECBAgEDzArJazQ/xMR2s3waY5qrC9+Gr5iFW8VnvaSdjDVkKbPQxXumJ8VnyWTD1/TrGXasElglMShyXl8yyxp1NgAABAgQIECBAgACBaQIfz+fz8XhMO6mudLg7qslN1NU3Umrn5laJWSWdApUpLXoETJXV5wDS1UmzCv2q2lpY/QQIECBAgAABAssFrvKu9fV6Wau1fLjVsKbApKUiazasLgIEdvwcAjYBAgQIECBAgAABAgSWC8hqLTdUw5oCnZsK12xAXQQIECBAgAABAgQIECBAgEATAq3tQGxiUHSCAAECBFoW2G1vfsuI+kaAAAECBAgQILCZgB2Im9GqmAABAgQIECBAgAABAgQIECBAgMD7D7g387R4o0mAAAECBAgQIECAAAECBAgQILBQwFqthYBOJ0CAAAECBAgQIECAAAECBAgQIDAk4Gnx5gcBAgQIECBAgAABAgQIECBAgMD1BGS1rjdmIiZAgAABAgQIECBAgAABAgQIEJDVMgcIECBAgAABAgQIECBAgAABAgSuJyCrdb0xEzEBAgQIECBAgAABAgQIECBAgICsljlAgAABAgQIECBAgAABAgQIECBwPQFZreuNmYgJECBAgAABAgQIECBAgAABAgRktcwBAgQIECBAgAABAgQIECBAgACB6wnIal1vzERMgAABAgQIECBAgAABAgQIECAgq2UOECBAgAABAgQIECBAgAABAgQIXE9AVut6YyZiAgQIECBAgAABAgQIECBAgAABWS1zgAABAgQIECBAgAABAgQIECBA4HoCslrXGzMREyBAgAABAgQIECBAgAABAgQIyGqZAwQIECBAgAABAgQIECBAgAABAtcTkNW63piJmAABAgQIECBAgAABAgQIECBAQFbLHCBAgAABAgQIECBAgAABAgQIELiegKzWnDH7+P6VnlkemVPv93NCVVn9WVvDlS8MJjQ9EMDsrsUTYx9jqDOam3HK8sjVQIAAAQIECBAgQKAZgfJteXo/Et9vdxbrQ5hUeAfJyrubNOwlUaVonfWkdzErWrk5WjJqzr20gKzWrsM3+lrzLvD586uzcCgwKejRRjtrm9rKpLzbu3DsZmhoSXOTNBQmQIAAAQIECBAgQCAKZG/L0/uR94/irURWbBhwUuGp9xGTxi50Z/Qeqq/Xk9oKCcGB+5rO+7LSf2qjyhO4uYCs1swJkL7EZy9e2VKpmIAPLWWfeMSD5WtcfEHMKhyOOL4iZx8ClA1lgYXYss8Wsk8Pyg8W0moHWhzNrGUsnUpZhDNHzmkECBAgQIAAAQIECNQJ7PzZc2hu9N6hLvZvpeZ9gl7f6yzU4RNrqq0pU999JQncQUBWa/1RDun28AKXZv1DS/GVOi2WvuCWyaas5IxX+YFGy1AzkdB6iLAsnH16k/4z634WdtnNkqvM0GUU6w+eGgkQIECAAAECBAjcSaDzbXkJUFksnNj38fnoJ9nlR+wxknh71VdJTbudZQZGO+tI+pF/FlhN6533cWUTnYajpHeas/pK4IuArNb8CRFSPCHzktYSDoYjsUzfL4byeFyD2rdeKW0ubSt9Ye3LfHWWn0ewsKrYzbT1Pq7Y5YWNzuupswgQIECAAAECBAi0KtD5tnzgJqW88Snfomd1xs+qs8/a40fm4b4puy/oA48ls/umtJX0dqzzs/m06b6GaipMIy/v48oj9bCpYWUkrU5R/SIwLCCrtfIMia84sd6+5UWdvz/KbFRZYfZynyW5YrWdr9SVv7RqUFasquxR5hA/mQmN1oSnDAECBAgQIECAAAECmwqktx4DDQ180r/kvX25fCm9BQvfD5RZXWbFtmrEVmxudQoVEthTQFZrkXaZZMlegOJrTXi9jpmmvtepeDwuARt4RasMfbTRUM+khoYLly2WK9o6g+/kWpGiUkwxAgQIECBAgAABAgRCVmgVh75P+ivrH/jsvzMvln0oPjV3VhlVKpOtR1uONiy2enPLA1YDgaMEPp7P5+Px2KL58Fow9RVki0jUSYAAAQIECBAgQIAAAQKZQJa+Cfdu6cF4pP62rqwz3Q8YAsiOxI+xO78JN5XhR+mH5Z1xhvpjtDVlspA6Ty8d+kKNAfQxZl3IYGM3+zrS17XKZQQuAQKVAlfJ57xeL1mtyjFVjAABAgQIECBAgAABAgROLSC5c+rhEdx1BC6U1bID8TrTSqQECBAgQIAAAQIECBAg0CMwY+cgSwIEri6w+VqtqwOJnwABAgQIECBAgAABAgQIECBwN4H6rcdHybx3IFqrdRS+dgkQIECAAAECBAgQIECAAAECBOYLbLhWa35QziRAgAABAgQIECBAgAABAgQIECDQL2CtltlBgAABAgQIECBAgAABAgQIECBwSQE7EC85bIImQIAAAQIECBAgQIAAAQIECNxcQFbr5hNA9wkQIECAAAECBAgQIECAAAEClxSQ1brksAmaAAECBAgQIECAAAECBAgQIHBzAVmtm08A3SdAgAABAgQIECBAgAABAgQIXFJAVuuSwyZoAgQIECBAgAABAgQIECBAgMDNBWS1bj4BdJ8AAQIECBAgQIAAAQIECBAgcEkBWa1LDpugCRAgQIAAAQIECBAgQIAAAQI3F5DVuvkE0H0CBAgQIECAAAECBAgQIECAwCUFZLUuOWyCJkCAAAECBAgQIECAAAECBAjcXEBW6+YTQPcJECBAgAABAgQIECBAgAABApcUkNW65LAJmgABAgQIECBAgAABAgQIECBwcwFZrZtPAN0nQIAAAQIECBAgQIAAAQIECFxSQFbrksMmaAIECBAgQIAAAQIECBAgQIDAzQVktW4+AXSfAAECBAgQIECAAAECBAgQIHBJAVmtSw6boAkQIECAAAECBAgQIECAAAECNxeQ1br5BNB9AgQIECBAgAABAgQIECBAgMAlBWS1LjlsgiZAgAABAgQIECBAgAABAgQI3FxAVuvmE0D3CRAgQIAAAQIECBAgQIAAAQKXFJDVuuSwCZoAAQIECBAgQIAAAQIECBAgcHMBWa2bTwDdJ0CAAAECBAgQIECAAAECBAhcUuDjH/7hH/7oj+S2Ljl4giZAgAABAgQIECBAgAABAgQI3FPgH//xH/9/ekTpVkNVEtAAAAAASUVORK5CYII=)

__DEMAIS REGISTROS__

Registro M410 – M415

![](data:image/png;base64,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)

Registro M500

![](data:image/png;base64,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AtMWCBu1e3x8ZFXytDuUT+3FLslH1zt6w5HxvrajFuP1p+QDFNiOi2I7ajHA7kGREEAAAQQQQAABBBBAYNoCRAyn3f71tb89EWFq8ZzBvVl92uGm2I5aDNeXko1QYDsuiu2oxQi7D0VGAAEEEEAAAQQQQACBbRdgVfK2tzD1QwABBBBAAAEEEEAAAQQQQAABBBDYaoHgq5IbRwy3mpfKIYAAAggggAACCCCAAAIIIIAAAgggMEqBULuP8BzDUTY/hUYAAQQQQAABBBBAAAEEEEAAAQQQQGB9Ao3nGIaKVq6vSuSMAAIIIIAAAggggAACCCCAAAIIIIDAdASCr0pm55PpdB5qigACCCCAAAIIIIAAAggggAACCCCAQL0AEcN6I1IggAACCCCAAAIIIIAAAggggAACCCAwHQEihtNpa2qKAAIIIIAAAggggAACCCCAAAIIIIBAvQARw3ojUiCAAAIIIIAAAggggAACCCCAAAIIIDAdASKG02lraooAAggggAACCCCAAAIIIIAAAggggEC9ABHDeiNSIIAAAggggAACCCCAAAIIIIAAAgggMB0BIobTaWtqigACCCCAAAIIIIAAAggggAACCCCAQL0AEcN6I1IggAACCCCAAAIIIIAAAggggAACCCAwHQEihtNpa2qKAAIIIIAAAggggAACCCCAAAIIIIBAvQARw3ojUiCAAAIIIIAAAggggAACCCCAAAIIIDAdASKG02lraooAAggggAACCCCAAAIIIIAAAggggEC9ABHDeiNSIIAAAggggAACCCCAAAIIIIAAAgggMB0BIobTaWtqigACCCCAAAIIIIAAAggggAACCCCAQL0AEcN6I1IggAACCCCAAAIIIIAAAggggAACCCAwHQEihtNpa2qKAAIIIIAAAggggAACCCCAAAIIIIBAvQARw3ojUiCAAAIIIIAAAggggAACCCCAAAIIIDAdASKG02lraooAAggggAACCCCAAAIIIIAAAggggEC9ABHDeiNSIIAAAggggAACCCCAAAIIIIAAAgggMB2BnS9fvjx79synwjs7OyLZ09OTT+IBptHl54UAAggggAACCCCAAAIIIIAAAggggMD2CYSK2j0+PjLHcPu6BzVCAAEEEEAAAQQQQAABBBBAAAEEEECgvcDk5hiGira2J+dIBBBAAAEEEEAAAQQQQAABBBBA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)

