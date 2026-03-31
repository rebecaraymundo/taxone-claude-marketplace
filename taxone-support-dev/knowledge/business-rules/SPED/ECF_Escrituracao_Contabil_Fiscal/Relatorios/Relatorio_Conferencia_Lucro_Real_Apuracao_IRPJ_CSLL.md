# Relatorio_Conferencia_Lucro_Real_Apuracao_IRPJ_CSLL

- **Fonte:** Relatorio_Conferencia_Lucro_Real_Apuracao_IRPJ_CSLL.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 236 KB

---

	

THOMSON REUTERS

Relatório de Conferência do Lucro Real – Apuração IRPJ/CSLL

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

[1\.	INTRODUÇÃO	3](#_Toc525907102)

[2\.	DOCUMENTOS DE REFERÊNCIA	3](#_Toc525907103)

[3\.	Tela de Parâmetros	3](#_Toc525907104)

[4\.	LEIAUTE	9](#_Toc525907105)

[4\.1\.	Regras dos campos do Relatório \(Leiaute\)	10](#_Toc525907106)

[4\.2\.	Exemplos do Relatório	21](#_Toc525907107)

# <a id="_Toc525907102"></a><a id="_Toc361822343"></a>INTRODUÇÃO

Objetivo desta especificação é criar uma *tela para permitir ao usuário parametrizar dados e gerar o relatório de Conferência dos registros exibidos na tela Lucro Real – Demonstração, dos registros do bloco N*\.

# <a id="_Toc525907103"></a>DOCUMENTOS DE REFERÊNCIA

- Layout\_ECF\.xlsx
- Tela\_Lucro\_Real\-Registros\_de\_Tabela\_Dinamica\.doc

# <a id="_Toc522613784"></a><a id="_Toc522722809"></a><a id="_Toc525907104"></a><a id="_Toc396377211"></a>Tela de Parâmetros

<a id="_Toc359395873"></a>__Localização da tela:__  ECF \- Escrituração Contábil Fiscal >>Relatórios >> Conferência do Lucro Real >> Apuração IRPJ/CSLL

__Título da tela:__ Conferência do Lucro Real \- Apuração IRPJ/CSLL

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

Permite ao usuário selecionar um ou mais registros do Lucro Real, do bloco N, da Tela Demonstração,\) para gerar o relatório\.

Tratamentos:

- Só deve ser exibido os registros, quando o campo versão estiver preenchido\.
- Recuperar os registros do bloco N, compatível com a versão que foi indicada na tela de parâmetros do relatório\.

Lista de Registros Válidos:

N500

N600

N610

N615

N620

N630

N650

N660

N670

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

# <a id="_Toc525907105"></a><a id="Leiaute"></a>LEIAUTE

__Origem das informações para geração do relatório:__

- Tela Lucro Real, registros oriundos de Tabela Dinâmica <a id="_Hlk525897425"></a>\(todos os registros processados da tabela dinâmica do bloco N\)\. 
- Registros N500, N600, N610, N620, N630, N650, N660 e N670
- Tela Lucro Real, demais registros  
- RegistroN615

__Tipos de Relatórios:__

- Sintético
- Analítico 

O registro N615  não considera esse parâmetro \(será gerado com o mesmo leiaute, independentemente do tipo de relatório escolhido\) \.

__Regra de agrupamento: __

- Agrupar por Informação do ECF, por registro e período de apuração\. 

__Ordenação: __

- Ordenar por código do estabelecimento, data inicial Informação ECF, período de apuração, código do registro \(seguindo a hierarquia dos registros de acordo com o arquivo Layout\_ECF\.xlsx\) e 

Se registro oriundo de Tabelas Dinâmicas:

- 
	- Código da linha da tabela dinâmica\. Todos de forma crescente\.

Se registro oriundo do Plano Referencial:

- 
	- Código da conta referencial\. Todos de forma crescente\.
- Nos relatórios analíticos, ordenar os campos Conta Contábil e Centro de Custo, se houver, de forma crescente\.

__Busca de Registros: __

- Considerar as informações que foram processadas e exibidas na tela do Lucro Real, de acordo com as informações de filtro indicadas na tela de geração do relatório\. Não será possível selecionar a apuração anual nos períodos Inicial e Final, na tela de geração do relatório, se existir dados referente a apuração Anual \(A00\), a mesma deve ser exibida no relatório\.
- Para os demais registros \(N615\), não será considerado o tipo de relatório, ou seja, se marcados esses registros serão gerados sempre em um único leiaute\.

### <a id="_Toc525907106"></a>Regras dos campos do Relatório \(Leiaute\)

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

__Relatório de Conferência do Lucro Real – Apuração IRPJ/CSLL \- Sintético __

__Título 2:__ \(\*\)

__Relatório de Conferência do Lucro Real – Apuração IRPJ/CSLL \- Analítico__

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

Registros Atendidos: N500, N600, N610, N620, N630, N650, N660 e N670 \(\*\)

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

__Para as linhas 8 do N620 e 9 do N630:__

__Valores Válidos:__

Fórmula

‘nulo’

- Exibir com o texto ‘Fórmula’, se o tipo da linha igual a ‘CA’ e não existir associação ou se tipo da linha igual a ‘CNA’, nos demais casos, deixar o campo nulo\.

MFS\-20624

Relatório Analítico –  Registros de Origem de Tabela Dinâmica\(\*\)

Cód\. Registro \- Descrição do Registro

Para os registros N500, N600, N610, N620, N630, N650, N660 e N670 \(\*\)

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

__Detalhamento para os registros N500 e N650, linha 2 com percentual de receita bruta e sem entrada manual nos percentuais \(\*\)__

__Subtítulo: \(\*\)__

__DEMONSTRAÇÃO DO CÁLCULO DA ESTIMATIVA DA RECEITA BRUTA__

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

XX,XXC ou

X,XXD

Exibir o valor da conta contábil e centro de custo \(este último, se existir\), referente a linha da tabela dinâmica, antes da aplicação do percentual de receita\.

__Tratamento:__

Concatenar o valor com o indicador\.

MFS\-20624

PERCENTUAL DA RECEITA BRUTA 

Texto

XX,XXXX

Exibe o valor do percentual de receita bruta que foi utilizado\. 

MFS\-20624

__Detalhamento para os registros N500, linha 2 com percentual de receita bruta e com entrada manual nos percentuais \(\*\)__

VALOR DA RECEITA BRUTA SUJEITA A 1,6%

Texto

XX,XX

Exibe o valor da receita sujeita ao percentual referido\.

MFS\-20624

VALOR CALCULADO

Texto

XX,XX

Exibe o valor calculado da receita com o percentual aplicado\.

MFS\-20624

VALOR DARECEITA BRUTA SUJEITA A 8%

Texto

XX,XX

Exibe o valor da receita sujeita ao percentual referido\.

MFS\-20624

VALOR CALCULADO

Texto

XX,XX

Exibe o valor calculado da receita com o percentual aplicado\.

MFS\-20624

VALOR DARECEITA BRUTA SUJEITA A 16%

Texto

XX,XX

Exibe o valor da receita sujeita ao percentual referido\.

MFS\-20624

VALOR CALCULADO

Texto

XX,XX

Exibe o valor calculado da receita com o percentual aplicado\.

MFS\-20624

VALOR DARECEITA BRUTA SUJEITA A 32%

Texto

XX,XX

Exibe o valor da receita sujeita ao percentual referido\.

MFS\-20624

VALOR CALCULADO

Texto

XX,XX

Exibe o valor calculado da receita com o percentual aplicado\.

MFS\-20624

VALOR DARECEITA BRUTA SUJEITA A 100%

Texto

XX,XX

Exibe o valor da receita sujeita ao percentual referido\.

MFS\-20624

VALOR CALCULADO

Texto

XX,XX

Exibe o valor calculado da receita com o percentual aplicado\.

MFS\-20624

VALOR TOTAL DA RECEITA BRUTA

Texto

XX,XX

Exibe o valor total das receitas\.

MFS\-20624

SOMATÓRIO DO VALOR CALCULADO

Texto

XX,XX

Exibe o valor total calculado da receita \(valor aplicado ao percentual\)\.

MFS\-20624

__Detalhamento para os registros N650, linha 2 com percentual de receita bruta e com entrada manual nos percentuais \(\*\)__

VALOR DA RECEITA BRUTA SUJEITA A 12%

Texto

XX,XX

Exibe o valor da receita sujeita ao percentual referido\.

MFS\-20624

VALOR CALCULADO

Texto

XX,XX

Exibe o valor calculado da receita com o percentual aplicado\.

MFS\-20624

VALOR DA RECEITA BRUTA SUJEITA A 32%

Texto

XX,XX

Exibe o valor da receita sujeita ao percentual referido\.

MFS\-20624

VALOR CALCULADO

Texto

XX,XX

Exibe o valor calculado da receita com o percentual aplicado\.

MFS\-20624

VALOR DARECEITA BRUTA SUJEITA A 100%

Texto

XX,XX

Exibe o valor da receita sujeita ao percentual referido\.

MFS\-20624

VALOR CALCULADO

Texto

XX,XX

Exibe o valor calculado da receita com o percentual aplicado\.

MFS\-20624

VALOR TOTAL DA RECEITA BRUTA

Texto

XX,XX

Exibe o valor total das receitas\.

MFS\-20624

SOMATÓRIO DO VALOR CALCULADO

Texto

XX,XX

Exibe o valor total calculado da receita \(valor aplicado ao percentual\)\.

MFS\-20624

__Detalhamento para as *linhas 9 do registro N620 e 8 do registro N630A, N630B ou N630C\.* \(\*\)__

Agrupamento \(\*\)

ANTES DA ATUALIZAÇÃO

Texto

Agrupar os campos VALOR DO PAT e LIMITE DE 15% SOBRE O PAT

MFS\-20624

VALOR DO PAT 

Texto

XX,XX

Exibe o valor da linha *9 do registro N620 ou 8 do registro N630A, N630B ou N630C antes de realizar o cálculo do PAT\.*

*Obs\.: Mesmo valor após o processamento da importação dos saldos\.*

MFS\-20624

LIMITE DE 15% SOBRE O PAT 

Texto

XX,XX

Exibe o limite de 15% calculado sobre o PAT antes da atualização\.

MFS\-20624

VALOR DO IMPOSTO DEVIDO

Texto

XX,XX

Exibe o valor do imposto, ou seja, valor da linha 3 do *registro N620 ou 8 do registro N630A, N630B ou N630C\.*

MFS\-20624

LIMITE DE 4% SOBRE O IMPOSTO DEVIDO

Texto

XX,XX

Exibe o limite de 4% calculado sobre o imposto devido\.

MFS\-20624

VALOR DO PDTI/PDTA

Texto

XX,XX

Exibe o valor do PDTI/PDTA, ou seja, valor da linha 10 do registro N620 e linha 9 do registro N630A, N630B ou N630C

MFS\-20624

LIMITE DE 4% COM PDTI/PDTA

Texto

XX,XX

Exibe o limite de 4% com a dedução do incentivo PDTI/PDTA\.

MFS\-20624

VALOR DO PAT DE PERÍODOS ANTERIORES

Texto

XX,XX

Exibe o valor de PAT que foi utilizado de períodos anteriores\.

MFS\-20624

VALOR DO PAT ATUALIZADO

Texto

XX,XX

Exibe o valor do PAT após o cálculo\. 

Obs\.: Mesmo valor da linha *9 do registro N620 ou 8 do registro N630A, N630B ou N630C após a realização do cálculo de registros e fórmulas\.*

MFS\-20624

DEMAIS REGISTROS \(\*\)

N615 \(\*\)

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

### <a id="_Toc438651774"></a><a id="_Toc522628480"></a><a id="_Toc523143863"></a><a id="_Toc525907107"></a>Exemplos do Relatório 

Registros de Tabela Dinâmica – Sintético

![](data:image/png;base64,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0QEKMKbgABudKu+HQIVbVftRcWqBAAIItEWgwolajCkgUtCW9qWcCCCAwD4LECnY59albnstUOECdK89qBwCCCCwcwIVTtTMPti5VqRACCCAAAIIIIAAAggggAACCGxXoM4xBdutCbkjgAACCCCAAAIIbEWAFUm3wk6mCCCAgIsAYwpclNgGAQQQQAABBBBAAAEEEEAAAQTyBOocU0A4mWMNAQQQQAABBBBAAAEEEEAAgd0RYEzB7rQFJUEAAQQQQAABBBBAAAEEEECgrQLfaGvBKTcCCCCAAAIIIIAAAggggAACCDQgQKSgAVSSRAABBBBAAAEEEEAAAQQQQKC1AkQKWtt0FBwBBBBAAAEEEEAAAQQQQACBBgSIFDSASpIIIIAAAggggAACCCCAAAIItFaASEFrm46CI4AAAggggAACCCCAAAIIINCAAJGCBlBJEgEEEEAAAQQQQAABBBBAAIHWChApaG3TUXAEEEAAAQQQQAABBBBAAAEEGhAgUtAAKkkigAACCCCAAAIIIIAAAggg0FoBIgWtbToKjgACCCCAAAIIIIAAAggggEADAkQKGkAlSQQQQAABBBBAAAEEEEAAAQRaK0CkoLVNR8ERQAABBBBAAAEEEEAAAQQQaECASEEDqCSJAAIIIIAAAggggAACCCCAQGsFiBS0tukoOAIIIIAAAggggAACCCCAAAINCBApaACVJBFAAAEEEEAAAQQQQAABBBBorQCRgtY2HQVHAAEEEEAAAQQQQAABBBBAoAEBIgUNoJIkAggggAACCCCAAAIIIIAAAq0VIFLQ2qaj4AgggAACCCCAAAIIIIAAAgg0IECkoAFUkkQAAQQQQAABBBBAAAEEEECgtQJEClrbdBQcAQQQQAABBBBAAAEEEEAAgQYEiBQ0gEqSCCCAAAIIIIAAAggggAACCLRWgEhBa5uOgiOAAAIIIIAAAggggAACCCDQgACRggZQSRIBBBBAAAEEEEAAAQQQQACB1goQKWht01FwBBBAAAEEEEAAAQQQQAABBBoQIFLQACpJIoAAAggggAACCCCAAAIIINBaASIFrW06Co4AAggggAACCCCAAAIIIIBAAwJEChpAJUkEEEAAAQQQQAABBBBAAAEEWitApKC1TUfBEUAAAQQQQAABBBBAAAEEEGhAgEhBA6gkiQACCCCAAAIIIIAAAggggEBr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)

Registros de Tabela Dinâmica – Analítico

![](data:image/png;base64,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hgABAgQIECBAgAABAgQWCpSPyHUVphvD3Vzjt8ghmLLO9MG3rExWf2wo/UO4qQxb0kh64wz1pyueIlFsKytThl3uXjoMhRorH2LMupDdL8duDnVkqGuTxmjhtLH7EwQOzOe8v79LPD1hjukjAQIECBAgQIAAAQIEricg/3K9MRPxKQWOTTx51O6Uk0JQBAgQIECAAAECBAgQeLbAjEfkng2m9wROKjB5xdNJ+yEsAgQIECBAgAABAgQIECBAgACBAYFDXp3UPWpnxZMpSYAAAQIECBAgQIAAAQIECBAgsInAhBVPm7SvUgIECBAgQIAAAQIECBAgQIAAgTsKWPF0x1HVJwIECBAgQIAAAQIECBAgQIDAOQQ8aneOcRAFAQIECBAgQIAAAQIECBAgQOB2AhJPtxtSHSJAgAABAgQIECBAgAABAgQInENA4ukc4yAKAgQIECBAgAABAgQIECBAgMDtBCSebjekOkSAAAECBAgQIECAAAECBAgQOIeAxNM5xkEUBAgQIECAAAECBAgQIECAAIHbCUg83W5IdYgAAQIECBAgQIAAAQIECBAgcA4BiadzjIMoCBAgQIAAAQIECBAgQIAAAQK3E5B4ut2Q6hABAgQIECBAgAABAgQIECBA4BwCEk/nGAdRECBAgAABAgQIECBAgAABAgRuJyDxdLsh1SECBAgQIECAAAECBAgQIECAwDkEJJ7OMQ6iIECAAAECBAgQIECAAAECBAjcTkDi6XZDqkMECBAgQIAAAQIECBAgQIAAgXMISDydYxxEQYAAAQIECBAgQIAAAQIECBC4nYDE0+2GVIcIECBAgAABAgQIECBAgAABAucQePm3f/u3n/9c+ukcoyEKAgQIECBAgAABAgQIECBAgMBdBP793//9/wc7/HWXB3IjOwAAAABJRU5ErkJggg==)

N500 – linha 2 \(com percentual de receita e entrada manual nos percentuais\) 

 ![](data:image/png;base64,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)

N650 – linha 2 \(com percentual de receita e entrada manual nos percentuais\)

![](data:image/png;base64,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r8uffWg5agbeRfX5oO0sRg/PtjNY82laQQIECBAg0CuQJRFimbg9bOl+jN+Ej9KN4fv0Kyscd8mqKkMqa05Dquzeu+PUjb3dzygykPTHqFRuzD6q7NX7URlDParY8VR+6iGwZN+Wtrp3UT12Kaqnp6ds9vT+GB96bCmsDAECBAgQINAs8OkPMtZf2dRc3buCl7ovydbsb1zOq85eBAgQIECAAAECZxTYOin08vLiQb8zTix9JkCAAIETCby+WrxbTNT7nrQTMegqAQIECBAgQIDAzgWkqHY+QMIjQIAAAQJLBMLfmPv6+6++++3ry618ESBAgAABAgQIENipgAf9djowwiJAgAABAgQIECBAgAABAgQI7ETAg347GQhhECBAgAABAgQIECBAgAABAgQIbCjgQb8NcVVNgAABAgQIECBAgAABAgQIECDQIiBF1aKkDAECBAgQIECAAAECBAgQIECAwIYCUlQb4qqaAAECBAgQIECAAAECBAgQIECgRUCKqkVJGQIECBAgQIAAAQIECBAgQIAAgQ0FpKg2xFU1AQIECBAgQIAAAQIECBAgQIBAi4AUVYuSMgQIECBAgAABAgQIECBAgAABAhsKSFFtiKtqAgQIECBAgAABAgQIECBAgACBFgEpqhYlZQgQIECAAAECBAgQIECAAAECBDYUkKLaEFfVBAgQIECAAAECBAgQIECAAAECLQJSVC1KyhAgQIAAAQIECBAgQIAAAQIECGwoIEW1Ia6qCRAgQIAAAQIECBAgQIAAAQIEWgSkqFqUlCFAgAABAgQIECBAgAABAgQIENhQQIpqQ1xVEyBAgAABAgQIECBAgAABAgQItAhIUbUoKUOAAAECBAgQIECAAAECBAgQILChgBRVK+7j42Nr0duV64I8RJy3E9IyAQIECBAgQIAAAQIECBAgsEeBTVJUIVHSni6pZFXqCZeN0jFl8N2Wjx8/ZgMYWp8dw1Sl3tbTjSGSMs49zjsxESBAgAABAgQIECBAgAABAgQSgU1SVCFREr5GEytLhmNqOqYlnRSyUeErlq80NDWGtL9lQ+0aZbu94O0VKkmAAAECBAgQIECAAAECBAgQuJXAVimqbAlV+mNcfJQmjMryldxWLJxWNVRDy/ah1FVMA412p4s2W3vVvogs7emQSdrlbPVW+VGocF4At5qI2iVAgAABAgQIECBAgAABAgTOLLBViipd0RPXJQXokPcplynFVUuhfJasyT7N1hDFOmP6JlsDla2HiiG1PByXFc66E/NBvV2upOHKaZd2PG2lF7BsNyXNYj7zFNd3AgQIECBAgAABAgQIECBAYP8CW6Wo0p6H/FG2Umlo4VLcsfdBtkmgSx7BiwmgSS3WCzc+iBfTbSVavf5R0hX7oioCBAgQIECAAAECBAgQIECAwIoCW6Wo0qfewvfZQqdynVRWJk24hMJxxdPoI2xp+SxZllVSps/ivmU8aReyfFDWYvyxniaLSmXNJVpvBqqUCf1tDGDFmaQqAgQIECBAgAABAgQIECBAgMBsgcfn5+enp6eW/VueiWup577LxMTWNbt5k0av2UFtESBAgAABAgQIECBAgAABAjcU2Dop9PLystUqqhuq3arpdN3TNWPwfN81tbVFgAABAgQIECBAgAABAgQIbCEgRbWaauOrplZr71NFt2p39Y6okAABAgQIECBAgAABAgQIEDitgBTVaYdexwkQIECAAAECBAgQIECAAAECexGQotrLSIiDAAECBAgQIECAAAECBAgQIHBagT2mqLxc6bTTUccJECBAgACBVGD0rxhXuA5xQbWkg6YKAQIECBAgcGcCm6SowtXGvGuO3j9O13iNVRabt+XOxlh3CNy3wOwTzrzzQ+9e2RmvN6SwY3ZijD8ObQ+7xBFcK+b7nhJ6R2CfAvVjuTfm9r+bU153VS6oGi+rypBmn29DVUNnsO6tmvscMlERIECAAAECVxbYJEXV9SG8w3vGNUfvLjPqubKj5ggQuKFAPOG0ZHAqcZanmsaTTxlAJaQbQmmaAIFjCTReSoVsVPiKp8HK6avxzNZrteTk1nuOXRLMsUZTtAQIECBAgMCowFYpqnRFQFw7EKKJF09ZmaxYKFnum+6edi9cn2W/opyxZZRMAQIEdi5QrkhKzydZ8OXJqjz5ZBWm57EZFPG8lK1xGNoem3CWm6FtFwL7Eeg9xkcvirILm6GroNjNmPEpz4Tlvtnaq/Jc16JXiTBexQ1dzlWCbGlaGQIECBAgQODOBLZKUaW/9wvXZOGaKbvFSjdmv0aLvxLMbs/iFV75a7f0IinsNW/LnY2x7hA4m0DvUoJsY2rSm8tOzzDlvlN/7Z9lo9pHJNtx3jmt3Ks9ACUJENhOYPSiKD35xOuicETXz0JZ4fKaKl6SpSmt8lw3mrRKu5C2krWYRpt+VOngduxqJkCAAAECBHYrsFWKqt7hqXd3o3zxcif7FWXvpU+lzGhDChAgsH+B3ozMkjTNkn17udLEfZks6z1DOsvtf+KJkMCoQO+xnx3y8bd3IYs0WmdWYMYulSbS3zjWi8Ws2aQAJhWeSqE8AQIECBAgcDiBrVJU4ddu4coj/Q1buDjLrkgaN8Zi6dXb4cQFTIDA6gLxhBNODumqqHTdZeO9UHlGypZZlfeNWQChQPhaPSO/up4KCRC4lUDv9U966ijPZvGskp7QYj3x0+ySqeVCK9tlyKT3fBuv98oAynrSYCodvNWgaJcAAQIECBC4ocDj8/Pz09NTSwTh+sPtVouVMgQIECBAgACBQwjcJJl+k0YPMRyCJECAAAECuxXYOin08vKy1Sqq3ZoKjAABAgQIECBAoBO41WLPxjWtxogAAQIECBA4m8DkVVRnA9JfAgQIECBAgAABAgQIECBAgACBTmC7R+usojLBCBAgQIAAAQIECBAgQIAAAQIEbi8weRXVdgmz22OIgAABAgQIECBAgAABAgQIECBAoBDwLiqTggABAgQIECBAgAABAgQIECBA4P4FvC69NsbhNaLXnwW3avf6PdUiAQIECBAgME/gVlcLt2p3npK9CBAgQIAAgQMJbJKiCtcu617B9KaK0oayAuHHJQmmxjVsCztbRtjY7oEmmVAJECBAgACBILDkyiQ1bLxacJVi4hEgQIAAAQIHEtgkRdX1v3tlVfja1CI2UbY12vToNWJ7/LGzo3WWGmWc7e1uaqtyAgQIECBAYLcC7VcLrlJ2O4gCI0CAAAECBDKBrVJU2RKq9Mf4ffmbvd6FV2VVlVFMKw/FsqbDlvhRViD9sd6F+kxKc1WVvmfBxJVfQ7ubvgQIECBAgMBxBbp/37uEUXodMnSVkl0sxS6Pbk8vLYagXKUcdwqJnAABAgQI3LfAVimq9Jd74YIsvSaLS4fCN/GjrFi4zCqrqi9WytYllXXGEY2txwDS5tIdsy7Ul2ilF6BphVlf0koa273vuah3BAgQIEDg7gWyaxhXKXc/4jpIgAABAgQItAtslaJqjyAt2fig3OhDfJNaH2q0MZihtmL+KyTa2kOaVLi9WiUJECBAgACBGwrEX0elv7QbjcdVyiiRAgQIECBAgMDdCFwjRRUuxcKVWR2uvGiL+4Ydsx9bhiFtOlvJFS77yo2V7aEL2fViaCJ2MA1yaHsWebpLbzyjdC0UyhAgQIAAAQK7Ehi6SolBukrZ1XgJhgABAgQIENhU4PH5+fnp6amljZi4aSl86DIt2bQtOnirdrfoizoJECBAgACBusC8f/fn7bV8LG7V7vLI1UCAAAECBAisIrB1Uujl5eUaq6hWsbhaJbd6zu5W7V4NVkMECBAgQIDAQoFbXS3cqt2FXHYnQIAAAQIEjiUweRXVsbonWgIECBAgQIAAAQIECBAgQIAAgVUEtnsNkVVUqwyQSggQIECAAAECBAgQIECAAAECBBYJTF5FtV3CbFE/7EyAAAECBAgQIECAAAECBAgQILCNgHdRbeOqVgIECBAgQIAAAQIECBAgQIAAgT0JeF36nkZDLAQIECBAgAABAgQIECBAgACBUwpIUZ1y2HWaAAECBAgQIECAAAECBAgQILAnASmqPY2GWAgQIECAAAECBAgQIECAAAECpxSQojrlsOs0AQIECBAgQIAAAQIECBAgQGBPAlJUexoNsRAgQIAAAQIECBAgQIAAAQIETikgRXXKYddpAgQIECBAgAABAgQIECBAgMCeBKSo9jQaYiFAgAABAgQIECBAgAABAgQInFJAiuqUw67TBAgQIECAAAECBAgQIECAAIE9CUhR7Wk0xEKAAAECBAgQIECAAAECBAgQOKXA4/Pz89PTU0vfHx8fu2IfP34sC4ePfBEgQIAAAQIECBAgQIAAAQIECNyrQG9SaJXOvry8WEW1iqRKCBAgQIAAAQIECBAgQIAAAQIE5gusuYpqu1za/P7ZkwABAgQIECBAgAABAgQIECBAYJlA5dG6ZRW/7W0V1SqMKiFAgAABAgQIECBAgAABAgQIEFgk4EG/RXx2JkCAAAECBAgQIECAAAECBAgQWC4gRbXcUA0ECBAgQIAAAQIECBAgQIAAAQKLBKSoFvHZmQABAgQIECBAgAABAgQIECBAYLmAFNVyQzUQIECAAAECBAgQIECAAAECBAgsEpCiWsRnZwIECBAgQIAAAQIECBAgQIAAgeUCUlQzDbu/thi/ZlZhNwIECBAgQIAAAQIECBAgQIAAgYvAJimqLHcTfgzgvR8NbWwZozRVlDbUsm+9TKW22J2uho8fP7a31Rjhkk41NtEes5IECBAgQIAAAQIECBAgQIAAga0FNklRDQUdMjshp5NlebqN6fayTB0i7D51r5Y6e8vE5iblp6aO5bxORYeyOdmrqUOgPAECBAgQIECAAAECBAgQIHAdgW1TVGkeKu1PlkbZKHVSPohXPp1XWcBVWfwVUmxZ2PVH/8o+1stX0nz1dnvDTgcifF9ZznadmacVAgQIECBAgAABAgQIECBAgEAU2DZF1QtdJmvWXf0UGi1XbMUtoyu2srVRvYu/skrSymPrsftpDVl4lb6nWaShJWZlzWWjWUIw7V1W7RYD4WAjQIAAAQIECBAgQIAAAQIECIwKbJiiGsp39KZFRgMNeZ+p662yxwljJVlzlYfj0pJpsamRtHSwN6qScWhtWrn7UH9nBGMXAgQIECBAgAABAgQIECBAgMB2AhumqFqCnpToSd/N1FJ5VybbZeh9VY1hxGKVtUuNgS0p1u6w+vu5loRtXwIECBAgQIAAAQIECBAgQIDAkMC2KarsibnyabWWLS2DVz4TF2uOa44qZUIya6ihepBhr6y5Ssdbyo9GEjs16TnB0XVtt029tQy0MgQIECBAgAABAgQIECBAgMBdCjw+Pz8/PT219K3ltUct9Ry0zM7TNzsP76CDLmwCBAgQIECAAAECBAgQIECgE9g67fDy8rLtKqq7GcXG1z9dv7/l0rDrx6BFAgQIECBAgAABAgQIECBAgMBCASmqJsD21z81VbdeoRhY5UHF9VpTEwECBAgQIECAAAECBAgQIEBgEwEpqk1YVUqAAAECBAgQIECAAAECBAgQINAuIEXVbqUkAQIECBAgQIAAAQIECBAgQIDAJgJSVJuwqpQAAQIECBAgQIAAAQIECBAgQKBdQIqq3UpJAgQIECBAgAABAgQIECBAgACBTQSkqDZhVSkBAgQIECBAgAABAgQIECBAgEC7wOPz8/PT01PLDo+Pj12x3r8cFz7yRYAAAQIECBAgQIAAAQIECBAgcK8CvUmhVTr78vJiFdUqkiohQIAAAQIECBAgQIAAAQIECBCYL7DmKqrtcmnz+2dPAgQIECBAgAABAgQKgcoTErTuScBA39No6guB2wpsfT6xiuq24zut9W42eKByGpnSBAgQIECAAAECBAgQIECAwEEEPOh3jIGKySlZqmMMmCgJECBAgAABAgQIECBAgACBKQKbPOiXrf6KP8b0SvdIYLYx3RLiL5eQpbunfcyyNunzhr3r0MosT9ylN/LYVihWNldppXz4sTfaOlEvSKbRa5tFOyozZeYoS4AAAQIECBAgcGCBoSv28jq8UjK9TA3fD10wH1jq4KHPuMEpe1y/XSo/rc+Z0RuZ9P6rvM0ZCi+9z/IKmoNPW+HvVMCDfp8HJrXoXUnUnYZ6/0XsPYXFc1bcqzIFemsOG2ef+9qjXTI3I1qjzJK27EuAAAECBAgQIHBCgcoF53WueE9ovrzL9Ruc9DZnyS3P7Djrt1q94bnxma1tRwK7ErjNg35ljinbEn8sU+ztZ8mykjr9UPlue5ksjBt765zadFnJKEjcpR5J+iuI7Pcb3Ue9yb5dTVDBECBAgAABAgQIXEEg/kZzaNGN68YrjMJtmxi9rWi8x1l+I9MbiRl42+mhdQLXEbhNiqrsW8typFstBar8kuE6g6QVAgQIECBAgAABAocT6P1F7+F6cZ6A25cC1E1a7uxGa1heyXkGTk8J3JPADVJUo6eb3lWa4V+49izV1KWeU8tXJsHyqjKioV9EdDGkTyzW52W8RFge3j0dAPpCgAABAgQIECAQBMoLy4XXjR70u6epNW8yVPZqv5FJJ+c9keoLAQKlwIYpqtGVopPGI01O9Sa5tvstTW/NYWOaPJrU3xnRzvi1xtCC7UnyChMgQIAAAQIECBDIBLKr2RkXt0hvKNB4g9MY4aT7oJY6y1ut0b3c+IwSKUDgEAKb/EW/Q/RckAQIECBAgAABAgROKxCXt5xW4CQdN9AnGWjdJHAFga3PJy8vLxuuoroCkCYIECBAgAABAgQIECBAgAABAgTuQGDNVVR3wKELBAgQIECAAAECBAgQIECAAAECvQKjrxef7WYV1Ww6OxIgQIAAAQIECBAgQIAAAQIECKwmsOYqqu1yaat1V0UECBAgQIAAAQIECDw8bP1KEcY7ETDQOxkIYRC4A4GtzydWUd3BJNEFAgQIECBAgAABAgQIECBAgMDhBe7kdemr/6HTww+sDhAgQIAAAQIECBAgQIAAAQIEjiOwVYqqkjMKH81OKoWlZenX1ovNjjOaIiVAgAABAgQIECAwRyC9xg7fl1tCve0l58Rhn40FFt6LZRMguynL5kZ549bSuXl7tdSsDAEC+xfYJEXVnVa691J1X0Pnl/BppUAFrnzjVahq/9YiJECAAAECBAgQILBPgXhlHq7kuyDLLSHy9pL77Kmo4r1YRiE3ZG4QIHBzgU1SVDMSRkMZ97jYKv0mqJUfZdtvjisAAgQIECBAgAABAkcRCLmn9Eq+3JJmqVpKHqXvp4ozfZwle7QlLqDLvinvs3qfielNaw41ly7Wm/2EzakGTmcJnEFgkxRVzB+Ff7dGzzjh38J4koqrouJqrPhvYRyS9KN0QdboAq4zDKo+EiBAgAABAgQIECBAoFcgewYlfbQlph3jSrre27Su2vZnYrKSvU/StNdmTAkQuG+BTVJUZWqpZV1VPA+GrFa7+6TC7dUqSYAAAQIECBAgQOA8AumvjUOvyy1D24dKnkfvLntauc+qvNElW4vXcrPWUuYuhXWKAIFMYJMUVfj3rLJ4Kn6aPuieriYtt2dxh+x72CVL/IftLUkxs4EAAQIECBAgQIAAgZiNSi+t4xV1uo6msSTSPQsM3amV65t677NC13oXQ/X2eqhkWfme0cRGgMB1BB6fn5+fnp5aGov5oLJw5aOWmmeXkYqaTWdHAgQIECBAgACBMwvMuIB37X3ECTNjoI/YTTETIHAFga3PJy8vL1utorqazhUa0gQBAgQIECBAgAABAh5TMAcIECBAYFOBNVdRbRqoygkQIECAAAECBAgQIECAAAECBG4osN2vK469iuqGQ6JpAgQIECBAgAABAgQIECBAgACBFQXWXEW1XS5txQ6risBsAe9fmE237o5bPwK9brRqI7C6gHPR6qTbVWiwtrNV8yoCpugqjPuvxEDvf4xuHqFJcvMhOEQAW9+IWUV1iGkgSAIECBAgQIAAAQIECBAgcJ8C4a9M3mff9GqiwIFflz6xp4oTIECAAAECBAgQIECAAAECOxLYemHOjroqlAaBHT3ol07NbJrWf+y6meZcw/OGWRY2ewix8unQEdK7y+jGoWCGksQxzrXC6A0gTozR5lLJtKry+1iy+6hkmd3fEGrltFVOm6581uu1HkGdvfz1mnO793DoZSxVh46jbLh7h6P3IB2aaWH77HFZ/Z+xaw6Qk082+qNHd3ZE7+3kk87kOLgbnYLiAZWei645e89wemm4cJpW5FaD5VRzZ6eaobPK8tPOraao88m0U8ni0jcZ6PL6v7wxKW8cyn9YR29YnPHaz3iVqZTd6WSnl/odd/0cNXRD2jsfhm7ke2/6yhuKoclQ3uakl1W9V5vlTWj73VN5E5Q1V94N9d5MpbdLO7lTW/1GLJuTd/KgX2TqneWVHE33UT2DUx7DvbuEjdmN01Aw6TyLe4Wjov2OvRJGeVSnR0hsorG5oXNByz+UKUs8CKcGUG8oPVAroXYflf9GtnTh5mVmzO3KLi2YMw6KSrVZbbNju/lADAUwY4CyY6F9Zjr5tE+Dq5180vP84U5BM2bv7EN49o5nPr2kfZ8xWE41Z7jO2c9pZ8YUnX1amL2j80n7P6NrXfb03umUIzj7hiiLc8ZF7NkurtrnQHl6WX7oNc6H8tY1u1puieQ69yBOfe0zalLJHT3oF6/1ezOIlczLpA633KVPbWsoA5JdHrUnSuJxOHT7Gqtqz2pVOl5pLg5K46VedkndePtd7+9oeGX+qzcjtuI8mVrVreZ2Omqjkyrt1NThnlT5VL0rlL/VAJW3oE4+6XVJ0Jg6G8NeVzj5dIGl/1qVcWaXYhvN5FvNXqeXGQN6q8Fyqhm9kNjzqWbSTFt42rnVFHU+mTTKywvfaqCnRr788nJeDXd8Z9c+BFPvAXvR5vm3B7lWyVsdEU59QyO4oxTVWpOsN0uySionvfNJK2y8g2os1uLQm/JfN29V3ii2BLYkzTG1/rJ8KZClO5c3sZ8aNhru/XTw6JGsPkC9FTaeVRqLtZg7+WRnuTSreDenoNVnb8vUUmaewOqD5VTTPhArnlrbGx0tubcrn9Wn6KiAAjcROOhAn/CM1z49YuKmfZd1Sx50UgWEQwe/7jjOqG1fKaqY94nfxH9o5x0kvXdTQ0wtbU2tsPE3+WlILWH0dmFSbLGGenPh6BrFH/ptQ8uMHA2gq6Sla1k9vfeNLfFsVOYmczuOy9RJNWlAp1a+kfDCam8yQI2HYSjWchSkFTr5jE6JJSef8hi54SnoJrPX6WV0gg39Sx2P6HgVO/UAT2ueemYYbWtqhU41ozNhyalmtPKsQByOSf+OZzPq+lPU+WTqQC8vf5N/OCaFvfzysqWGs53x2oeg8R4wO12kazha/OvxTBqd9q7t519np76hUdtXimrS3Mpyk9mPLVXN2KW32lBPPA67Mr01p8VawquUaYl8aMnipKbT5FT4vl5tdmKafYU0Kci0cDYWaTyz67z+ji3TaSiqqeNeb6tSW8vgZpVPje368o0tLhmg0ETLIdwSjJNPVLryyac8N6Yjm12WtQzl1cosmb1TD2Gnl4XDumSwnGoa8Q90nVMJNV6exTu6xu4vLLZkijqfLMS/5u5LBrqMc+rQlzUMXYK6uFpxVkw9N85uesZ8aNll03uQJUdES/Dlve3QPfi93qnt6C/6zZ7ZdiRwHYHufHTQnNd1fK7WSpoOvlqjGiKwHwHnov2MxWgkBmuUSIHbCpiit/W/WusG+mrUx23IJDnu2F0z8q1vxO7kL/pdc0i0RYAAAQIECBAgQIAAAQIECBAgsLrAmquoVg9OhQQIECBAgAABAgQIECBAgAABAjsR2O7RIquodjLEwiBAgAABAgQIECBAgAABAgQInFpgzVVU2+XSTj1EOr8Pga0fu91HL48RhbE4xjiJchsB838b101qNVibsKp0PQFTdD3LXddkoHc9PPsIziTZxzgcIIqtp4pVVAeYBEIkQIAAAQIECBAgQIAAAQIECNy9wI/uvoc6SIAAAQIECBAgQIAAAQIECBAgsHMBKaqdDlBYQRe+wvfllvTTlpI77aqw1hMwbdazPG9NZtGxxt54HWi8DNaBBuucoZqiJxl3A32SgV7STZNkiZ59FwpIUS0E3Gr37sVeMTMVXvJVbgltt5fcKlb17kagfTK0l9xN5wRyJYH2udFe8kqhn7KZ9lFoL3lKyGt0un0I2kteI25tnEagfeK1lzwN3pE62j587SWP1H+xNgi0D317yYZmFSHwKiBFtd95EA749CX05ZY0S9VScr+9FdlKAqbNSpCnrsYsOtbwG68DjZfBOtBgnTNUU/Qk426gTzLQS7ppkizRs+8SASmqJXr2JUCAAAECBAgQIECAAAECBAgQWEFAimoFxI2qCEuosieBsy2h6faSG4Wq2v0ItE+G9pL76Z1IriPQPjfaS14n8nO20j4K7SXPKXmFXrcPQXvJK4StifMItE+89pLn0TtQT9uHr73kgbov1BaB9qFvL9nSrjIEpKh2OgfiI37153tjfqr7plJyp50U1toCps3aomeszyw61qgbrwONl8E60GCdM1RT9CTjbqBPMtBLummSLNGz70KBx+fn56enp5ZawnKe9IVHca/KRy01KzNPIHtT1bxK7NUocDeT/A6mzd2MRePc22GxO5hFO1RtDGnG/DdejbarFzNYq5OqcF0BU3Rdz93WZqB3OzT7Ccwk2c9Y7DySGVNlUo9eXl6sopoktq/CvenCfYUomv0JmDb7G5PjRWQWHWvMjNeBxstgHWiwzhmqKXqScTfQJxnoJd00SZbo2bci8Pjhw4cvvviixWh0FVVLJcoQIECAAAECBAgQIECAAAECBAgcUWC7BKVVVEecD2ImQIAAAQIECBAgQIAAAQIECNybwDqrqO5NRX8IECBAgAABAgQIECBAgAABAgQ+CXgXlblAgAABAgQIECBAgAABAgQIEJgjELIq4b+bfl2hiU3j30nlXpe+k4EQBgECBAgQIECAAAECBAgQuLFAl2pJv0I09S2V7ExvbS09XCXjE/6ucctfNy472BJkLJM2kUVe5shKkxmdnbHLpB7dqvAmKaogno7WQr6swhRrtObRAr30W6Ras0nfHlh7yVtNI+0SIECAAAECBAgQIECAwH0IdGmd+BXyU+mWeH+aFRvqe2OxbPfwTu6F98KhktHXew91sD6aaWyVJno/ykxGI7yPedXSi01SVC0Nt6eZ4nQpZ2dLNrS9oTLsqRNl9PhJj/OplU9VVZ4AAQIECBAgQIAAAQIECKwrsPxONq7eCIGlS1Li9/HmOls+En9MC1SWyPQuoKnfuccO9saZtVV2oezRqH/Wl8aujVZ7xAJbpajCarowNtkAR6ZsIsahzcY4VhXTqL1zolc/tD40hxonU7b6aSjO+vbeY69+QI4mvI444cRMgAABAgQIECBAgAABAnsWyFIzQ6HOK5YuWYoZg/S2PUuBDWXE4vawECTNP2S1lZ9mWYJKMiGtvCtW/hj2rRcr6++la5FpiXzPU2s0tq1SVL0N906dOKJxdsbUTDrn0o1D0zfLj2Y5o3pD2YTO4g+RZDM7DSmLOc6tLM0UBNLKY8n04Cyn+OhAKkCAAAECBAgQIECAAAECBJYLhPvWodxQrL+3WHlXnhULt9XlgozR5ob6Va+t99PlRFkNU1vppRuVmdrK6t28QoUbpqiCbzrP0lkYtvcuFCqTOFl6aMglO4rSHGRLQ1O5Zx9CaUNDDpZQTR0O5QkQIECAAAECBAgQIEBga4H6vWp7biurZ94tcLrmI+14fQ1KnWhqJEMxzBiIbDVWqGFJX2bEcNtdNkxRlR1LVz+F/F+2Oqk3axg3ZoVnwMUAKunJlsRkffeYUMsydL0Blw5h/qVWM3pqFwIECBAgQIAAAQIECBAgMEMg3KXGW+N4/5vevbZXm9UWf0xv8IfunafewvdmD2LKKe1IuuKkt4NDhWPHK7EthOqVGcpCtA/EIUo+fvjw4YsvvmiJNaZOWgorQ4AAAQIECBAgQIAAAQIECBC4skDLYpErh3QfzW2dFHp5ebnqKqr7GBW9IECAAAECBAgQIECAAAECBHYoMPUxvR124cwhTV5FdWYsfSdAgAABAgQIECBAgAABAgQInFZglbdy9+pZRXXaSaXjBAgQIECAAAECBAgQIECAAIEdCUxYRbWjqIVCgAABAgQIECBAgAABAgQIECBwLwJWUd3LSOoHAQIECBAgQIAAAQIECBAgQODIAl6XfuTREzsBAgQIECBAgAABAgQIECBA4C4EpKjuYhh1ggABAgQIECBAgAABAgQIECBwZAEpqiOPntgJECBAgAABAgQIECBAgAABAnchIEV1F8OoEwQIECBAgAABAgQIECBAgACBIwtIUR159MROgAABAgQIECBAgAABAgQIELgLASmquxhGnSBAgAABAgQIECBAgAABAgQIHFlAiurIoyd2AgQIECBAgAABAgQIECBAgMBdCEhR3cUw6gQBAgQIECBAgAABAgQIECBA4MgCUlRHHj2xEyBAgAABAgQIECBAgAABAgTuQkCK6i6GUScIECBAgAABAgQIECBAgAABAkcWkKI68uiJnQABAgQIECBAgAABAgQIECBwFwJSVHcxjDpBgAABAgQIECBAgAABAgQIEDiywOM///nPH/1IourIYyh2AgQIECBAgAABAgQIECBAgMCRBf71r3/9f8Kei/cjsccsAAAAAElFTkSuQmCC)

N620 – linha 8 e N630 – linha 9 \(PAT\)

__![](data:image/png;base64,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OIfAxqdUZ/NzTBu9IECAAAEC+xfYIHtmFd7+p8G+IsyW4KW/xn+X73hXF+6VVTW6mlYeimVNh1fin7IC6a/tLrS507UDjb5nwcSVg0Ob72uMRUOAAAECBB4jEBJq6fl66GyeXVTEcEZfT0/BQ51wNn/M8KqVAAECBAgQeKyAFN5jfc9X++3KOy7ECxfi6bV4/FP4R/xTVixcXpdVpZfUJV22ALCsM24SW48BpM2lG2ZdaK8xTG880gqzvqSVdLZ7vnmiRwQIECBAoCqQneudzc0TAgQIECBAgECngBReJ5RiiwTaubks9baopWTjoUY7gxkKI+YHQyKyP9pJhfurVZIAAQIECBxCIL6tlb75Nxq5s/kokQIECBAgQIDARQSk8C4y0A/pZrgED1fk7QbKi/W4bdgw+7Un3LTpbCVguNwvX2y8HrqQ3SeEJmIH0yCHXs8iTzepxjNK10OhDAECBAgQOKjA0Nk8dsfZ/KAjK2wCBAgQIEBgdYHx5EvMeqzetgoJbCzQk218REjPavcRfVEnAQIECBBYS2De+XHeVstjfla7yyNXAwECBAgQILCBwAbZM6vwNhhHTexC4FnPsT6r3V2gC4IAAQIECKwq8Kyz6rPaXRVPZQQIECBAgMCxBXpX4R27l6InQIAAAQIECBAgQIAAAQIECBAg8EiBh35YllV4jxw6dRMgQIAAAQIECBAgQIAAAQIECBBYLNC7Cu+hecTFvVABAQIECBAgQIAAAQIECBAgQIAAgecI+Cy857hrlQABAgQIECBAgAABAgQIECBAgMB+BDxIu5+xEAkBAgQIECBAgAABAgQIECBAgACBioAUnmlBgAABAgQIECBAgAABAgQIECBAYNcCUni7Hh7BESBAgAABAgQIECBAgAABAgQIEJDCMwcIECBAgAABAgQIECBAgAABAgQI7FpACm/XwyM4AgQIECBAgAABAgQIECBAgAABAlJ45gABAgQIECBAgAABAgQIECBAgACBXQtI4e16eARHgAABAgQIECBAgAABAgQIECBAQArPHCBAgAABAgQIECBAgAABAgQIECCwawEpvF0Pj+AIECBAgAABAgQIECBAgAABAgQIfPj48WNb4cOHD7cCo8VQnlIgjL4fAgQIECBAgAABAgQIECBAgACBtsBDs2dW4Zl+BAgQIECAAAECBAgQIECAAAECBHYt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)__

__DEMAIS REGISTROS__

Registro N615 ![](data:image/png;base64,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EUAAAQQQQAABBBBAYGcFCBrubNOtqeCLMxHTFs8cPJis6YS9nGYYteiFhkwRcAsM48IZRi3opwgggAACCCCAAAIIIIDAugVYnrxucc6HAAIIIIAAAggggAACCCCAAAIIIICAj8AGlycHBw196kMaBBBAAAEEEEAAAQQQQAABBBBAAAEEEOhEYP1bjPBMw04ajkwQQAABBBBAAAEEEEAAAQQQQAABBBAYlEDwTMP1hzYH5U1lEEAAAQQQQAABBBBAAAEEEEAAAQQQ8BPY4PJkNkLxayJSIYAAAggggAACCCCAAAIIIIAAAgggMBoBgoajaWoqigACCCCAAAIIIIAAAggggAACCCCAgJ8AQUM/J1IhgAACCCCAAAIIIIAAAggggAACCCAwGgGChqNpaiqKAAIIIIAAAggggAACCCCAAAIIIICAnwBBQz8nUiGAAAIIIIAAAggggAACCCCAAAIIIDAaAYKGo2lqKooAAggggAACCCCAAAIIIIAAAggggICfAEFDPydSIYAAAggggAACCCCAAAIIIIAAAgggMBoBgoajaWoqigACCCCAAAIIIIAAAggggAACCCCAgJ8AQUM/J1IhgAACCCCAAAIIIIAAAggggAACCCAwGgGChqNpaiqKAAIIIIAAAggggAACCCCAAAIIIICAnwBBQz8nUiGAAAIIIIAAAggggAACCCCAAAIIIDAaAYKGo2lqKooAAggggAACCCCAAAIIIIAAAggggICfAEFDPydSIYAAAggggAACCCCAAAIIIIAAAgggMBoBgoajaWoqigACCCCAAAIIIIAAAggggAACCCCAgJ8AQUM/J1IhgAACCCCAAAIIIIAAAggggAACCCAwGgGChqNpaiqKAAIIIIAAAggggAACCCCAAAIIIICAnwBBQz8nUiGAAAIIIIAAAggggAACCCCAAAIIIDAaAYKGo2lqKooAAggggAACCCCAAAIIIIAAAggggICfwN6XL1+ePXvmk3hvb08ke3p68km8hWl0+XkhgAACCCCAAAIIIIAAAgggMEiB3b1hH2RzUCkEOhHYVDju8fGRmYadtCCZIIAAAggggAACCCCAAAIIIIAAAgggMByB0c005A8vw+m81AQBBBBAAAEEEEAAAQQQQEAJbGouEvwIINC3wKaubmYa9t2y5I8AAggggAACCCCAAAIIIIAAAggggMDu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)

