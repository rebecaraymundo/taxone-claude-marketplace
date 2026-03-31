# MTZ_Tela_Parametro_Geracao_Quadro_48_por_Tipo_de_AtividadexCFOP

- **Fonte:** MTZ_Tela_Parametro_Geracao_Quadro_48_por_Tipo_de_AtividadexCFOP.docx
- **Modificado:** 2021-12-13
- **Tamanho:** 74 KB

---

THOMSON REUTERS

Matriz da tela de Parâmetros para geração do Registro 48 

Por Código do Tipo de Atividade x CFOP

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS\_4502

Marcelo Souza

Criação da tela de parâmetros para geração do registro 48 do quadro 48 da DIME\- Santa Catarina\.

OS\_4581

Marcelo Silva

Incluir novo código para o parâmetro Tipo de Atividade\. 

MFS\-14715

Julyana Perrucini

Atendimento a Portaria SEF nº 399/2017\.

MFS76462

Liliane Assaf

Alteração no descritivo do Tipo de Atividade 506

Inclusão do Tipo de Atividade 507

Sumário

[1\.	Regras dos Campos	3](#_Toc499637168)

# <a id="regras_campos"></a><a id="_Toc350763252"></a><a id="_Toc499637168"></a>Regras dos Campos 

__\[ALTERADA – MFS\-14715\]__

__Localização da tela:__ 

Módulo: Estadual > DIME\-SC

		Menu: Parâmetros > Informações de ICMS > Quadro 47 e 48 > __Por Tipo de Atividade x CFOP__

	        __Título da tela: __Parâmetros p/Geração do Quadro 48 por Tipo de Atividade x CFOP\.

	        

Opções da barra de menu:

- 
	- 
		- __CONFIRMA__ – Salva os dados incluídos ou alterados\.
		- __RELATÓRIO__ – Para emitir o relatório o usuário poderá selecionar um estabelecimento, e serão listados todos os dados parametrizados para o estabelecimento selecionado\.
		- __FECHA__ – Fecha a janela da parametrização\.

	        

	        __Nesta tela estarão disponíveis os campos:__

                       

- 
	- 
		- Estabelecimento
		- Código de Atividade
		- CFOP
		- Replicar para os Estabelecimentos

	     	

__Funcionamento da tela:__ Nesta tela serão parametrizados os dados necessários para geração do registro 48 – Informações para Rateio do Valor Adicionado\. Neste item o usuário poderá identificar os códigos do tipo de atividade, e CFOP's que compõem as operações do quadro 48 da DIME\-SC, relacionado às notas fiscais de prestações de serviços e fornecimento de energia elétrica\. 

__Observações 1:__ A recuperação dos dados para a geração do Quadro 48, é feita através do documentos fiscais com operação de prestação de serviços e fornecedores de energia elétrica\. Estes documentos serão identificados através dos CFOPs parametrizados nesta opção\.

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a><a id="OLE_LINK4"></a>__Observações 2: __A partir de janeiro de 2014, será necessária essa parametrização para que seja feito um DE\-PARA com a tela __“Parâmetros p/Geração dos Quadros 47 e 48 por CFOP” __considerando o Código Tipo de Atividade selecionada\. Exemplo: O contribuinte já possui o CFOP 5251 na tela __“Parâmetros p/Geração dos Quadros 47 e 48 por CFOP” __para Operação de Energia Elétrica, ele precisa informar para esse mesmo CFOP o Código Tipo de Atividade na nova tela __“Parâmetros p/Geração do Quadro 48 por Tipo de Atividade x CFOP”__\.

__Observação 3: __Não poderá ser parametrizado para o mesmo estabelecimento código de CFOP iguais para código de atividade distinto\.  

	__ 	__

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Estabelecimento

Texto

S

S

Formato: 

Combo Box

Default: Habilitado/Desabilitado \(ver tratamento\)

Neste campo será exibido o Estabelecimento escolhido pelo usuário, na Tela de Login do Sistema, não tendo a opção de escolha de outro Estabelecimento, apenas será habilitado para seleção caso o usuário não entre com o Estabelecimento na Tela de Login\.

OS\_4502

Código Atividade

Texto

S

S

Formato: 

Combo Box

Default:

Habilitado

Neste campo será exibido o Código do tipo de atividade do estabelecimento, que deverá exibir as seguintes informações:

__\[ALTERADA – OS\_4581/ MFS\-14715\]__

- \(001\) for prestador de serviços de transportes;
- \(002\) for prestador de serviços de telecomunicações;
- \(003\) for fornecedor de energia elétrica por demanda contratada \(lançada no CFOP 5257\);
- \(004\) for distribuidor de energia elétrica a consumidor pessoa física ou jurídica;
- \(005\) for fornecedor de gás natural;  
- \(006\) for empresa que opere com o marketing direto;
- \(007\) for depósito ou centro de distribuição ou efetuar a entrega de mercadoria vendida por outro estabelecimento do mesmo titular;
- \(008\) for fornecedor de alimentos preparados;
- \(501\) for detentor de TTD de obrigação acessória autorizando a remessa de mercadorias ao varejo ou pronta entrega através de Central Integrada de Distribuição, na qualidade de inscrição única no Estado para tais operações;
- \(502\) for detentor de TTD de obrigação acessória autorizando que nas operações de venda utilize demonstrativo auxiliar especifico para escrituração do Livro de Saídas;
- \(503\) For detentor de TTD de obrigação acessória autorizando que o estabelecimento gerador de energia elétrica possua inscrição única englobando várias PCHs;
- \(504\) Para as saídas das partes e peças de um todo;
- \(505\) Para a transmissão da propriedade do produto final;

\[MFS76462\]

- \(506\) Autorizando que o estabelecimento trading registre as operações com importação por conta e ordem de terceiros nos CFOP 1949, 2949, 3949, 5949 ou 6949;
- 506\-Autoriza estabelecimento trading registrar operaçao de saída de mercadorias importadas por conta

\[MFS76462\]

- 507\-Autoriza estabelecimento trading registrar operaçao de entrada de mercadoria importada por conta 
- \(901\) informar percentual de rateio de VA \(__Valor Adicionado__\) por acordo entre municípios\.

A descrição do campo terá a quantidade máxima de 100 caracteres, cortando textos maiores que 100 caracteres\.

OS\_4502

OS\_4581

MFS\-14715

MFS76462

         CFOP’s

Texto

S

S

Formato:

Check Box

Default:

Habilitado

Preencher de acordo com a Tabela de Códigos Fiscais \(SAFX2012\) para seleção do usuário\.

Não mostrar CFOPs que já estejam marcados para o mesmo estabelecimento com códigos de atividade diferente\.              

OS\_4502

Replicar para os Estabelecimentos

Texto

N

S

Formato:

Check Box

Default:

Habilitado

Esta opção permite que a parametrização feita seja replicada para outros Estabelecimentos, que serão selecionados pelo usuário\. Serão disponibilizados apenas os estabelecimentos da Empresa do Login, que sejam de Santa Catarina\.

Para facilitar, o usuário poderá utilizar as opções “Selecionar Todos” e “Desmarcar Todos”\.

OS\_4502

*\* Descrição não disponível em tela*

