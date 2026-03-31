# MTZ_Report_Fiscal_Tela_Relatorio_Analitico_Detalhamento_de_Produto_Grandes_Volumes

- **Fonte:** MTZ_Report_Fiscal_Tela_Relatorio_Analitico_Detalhamento_de_Produto_Grandes_Volumes.docx
- **Modificado:** 2023-11-09
- **Tamanho:** 72 KB

---

THOMSON REUTERS

Report Fiscal – Relatório Analítico – Detalhamento de Produto \(Grandes Volumes\) 

*Localização:* Report Fiscal\\ Gerenciais\\ Documentos Fiscais\\ Analíticos\\ Detalhamento por Produto \(Grandes Volumes\) 

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS\_4603

Marcelo Silva

Criação da tela Relatório Analítico – Detalhamento de Produto \(Grandes Volumes\), esse Grandes volumes ira salvar relatório em um arquivo Excel quebrando o por quantidade de registro\.   

Sumário

[1\.	Regras dos Campos	3](#_Toc388620863)

# <a id="regras_campos"></a><a id="_Toc350763252"></a><a id="_Toc388620863"></a>Regras dos Campos 

__Localização da tela:__ 

__Modulo: __Básicos >> REPORT FISCAL

__Menu: __Gerenciais >> Documentos Fiscais >> Analíticos >> __“Detalhamento por Produto \(Grandes Volumes\)”__

	        __Título da tela: __Relatório Analítico – Detalhamento por Produto \(Grandes Volumes\)

	       __Aba Serviços:__

- __Botão Relatório:__ Para geração do Relatório o usuário deverá preencher todos os campos de preenchimento obrigatório, o sistema deve informar os campos onde falta informação, após preencher todos os campo preenchidos o sistema deverá gerar o arquivos em diretório escolhido pelo usuário criando o arquivo com nome padrão __“detalhamentoProduto\_numero do processo\_sequencial\.xsl”__ onde:

__detalhamentoProduto: __O nome padrão dado a todo arquivo;

__numero do processo:__ O número de processo da geração de cada relatório;

__sequencial:__  Será o sequencial atribuído a cada quebra de arquivo;

  __\.xsl:__ Será a extensão do arquivo indicando o programa do qual o relatório será gravado\. 

Exemplo: detalhamentoProduto\_123456\_1\.xsl

	    detalhamentoProduto\_123456\_2\.xsl

	    detalhamentoProduto\_123456\_3\.xsl

	     

- __Botão Sair:__ Para o usuário finalizar a tela\.               	

	       

	        __Nesta tela estarão disponíveis os campos: __

                       

- 
	- 
		- Período 
		- Diretório 
		- Quebrar Arquivos por Quantidade de Registro
		- Seleção de CFOP’s
		- UF
		- Estabelecimentos

	     	

__Funcionamento da tela:__ Nessa tela o usuário poderá emitir o relatório Analítico por Produto, considerando para sua geração os parâmetros de empresa filial, período e CFOP\. 

Devido à grande quantidade de registros, esse relatório será gerado em arquivos Execel, o mesmo deverá ser quebrado por quantidade de registro parametrizado pelo usuário, o sistema trama como default para quebra a cada 500\.000 mil registros\.      

__Campos do Relatório:__ Serão demonstrados todos os campos como é demonstrado no relatório padrão, verificar documento matriz: MTZ\_Report\_Fiscal\_Relatorio\_Analitico\_Detalhamento\_de\_Produto\.docx

   

	__ 	__

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

__Período __

TextField 

S

S

\-

O usuário deverá informar a data inicial e a data final do Período desejado para a extração das informações\.

OS\_4603

__Diretório__

TextField

S

S

\-

Neste campo o usuário deverá informar o diretório aonde será gravado o arquivo gerado\.

OS\_4603

__Quebrar Arquivo por Quantidade de Registros__

TextField 

S

S

\-

Nesse campo o usuário deverá informar a quantidade de registro que o sistema deverá realizar a quebra de arquivos\.

O sistema deverá trazer como Default o campo preenchido com 250\.000, para quebra de arquivos a cada 250 Mil registros\.  

   

OS\_4603

__Seleção de CFOP's__

Seleção de RadioButton

S

S

\-

Esse campo irá lista todos os CFOP's cadastrados, para que o usuário selecione quais os CFOP's que deseja emitir o relatório\.

Incluir botão __“Marcar Todos”__ permitindo ao usuário selecionar todos os códigos CFOP's, e __“Desmarcar Todos” __para o usuário__ __desmarcar os códigos CFOP’s selecionados\. 

Incluir botão __“Marcar Entradas”__ permitindo ao usuário selecionar todos os códigos CFOP's de entrada e __“Desmarcar Entradas”__ para o usuário desmarcar todos os códigos CFOP’s de entrada\.  

Incluir botão __“Marcar Saídas”__ permitindo ao usuário selecionar todos os códigos CFOP's de saída e __“Desmarcar Saídas”__ para o usuário desmarcar todos os códigos CFOP’s de saída\.

OS\_4603

__UF__

DropDown

S

S

\-

O usuário deverá informar qual Estado ele deseja selecionar, para das informações\.

OS\_4603

__Estabelecimentos__

Seleção de RadioButton

S

S

\-

Nesse campo o usuário terá a possibilidade de informar os estabelecimentos para gerar o relatório, tendo a opção do botão __“Marcar Todos”__ e __“Desmarcar Todos”__\.   

OS\_4603

*\* Descrição não disponível em tela*

 

