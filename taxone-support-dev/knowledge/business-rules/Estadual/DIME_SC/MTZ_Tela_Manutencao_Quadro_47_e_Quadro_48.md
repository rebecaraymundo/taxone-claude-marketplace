# MTZ_Tela_Manutencao_Quadro_47_e_Quadro_48

- **Fonte:** MTZ_Tela_Manutencao_Quadro_47_e_Quadro_48.docx
- **Modificado:** 2025-12-16
- **Tamanho:** 76 KB

---

 

THOMSON REUTERS

Tela de Manutenção Quadro 47 e Quadro 48 da DIME\-SC

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS\_4502

Marcelo Silva

Alteração da tela de manutenção para geração do quadro 47 e quadro 48 da DIME\- Santa Catarina\.

OS\_4581

Marcelo Silva

Incluir novo código para o parâmetro Tipo de Atividade\. 

CH5119\_2017

\(MFS\-11372\)

João Henrique

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a>Essa alteração consiste em alterar a tela de manutenção para considerar informação manual no quadro 47, como feito pelo quadro 48\.

MFS\-14715

Julyana Perrucini

Atendimento a Portaria SEF nº 399/2017\.

MFS35840

\(CH 6981/20\)

Vânia Mattos

Inclusão de novos tipos de atividade para o quadro 48 \(códigos 011, 012 e 013\)\.

Ato DIAT 36/2019: Códigos 14, 15 e 16 do Anexo III \(Tabela de Itens para Cálculo do Índice de Participação dos Municípios – IPM, códigos\)\. Estes códigos na DIME\-SC correspondem aos códigos 011, 012 e 013\.

MFS76462

Liliane Assaf

Alteração no descritivo do Tipo de Atividade 506

Inclusão do Tipo de Atividade 507

 Sumário

[1\.	Regras dos Campos	3](#_Toc499637879)

# <a id="_Toc332809666"></a><a id="_Toc332888929"></a><a id="_Toc350763246"></a>

<a id="_Toc350763252"></a>

# <a id="regras_campos"></a><a id="_Toc499637879"></a>Regras dos Campos 

__Localização da tela:__ 

Módulo: Estadual > DIME\-SC

		Menu: Obrigações > Manutenção \- Quadro 47 e Quadro 48

	        __Título da tela: __Manutenção Quadro 47 e Quadro 48

	        

Opções da barra de menu:		

- 
	- 
		- __NOVO: \- __Para o usuário__ __realizar novo cadastro, se algum campo estiver preenchido, perguntar ao cliente se deseja gravar os dados, os dados só poderão ser gravados se todos os campos estiverem preenchidos\.  
		- __ABRE: __Para o usuário__ __abrir um cadastro existente, manter a tela de consulta padrão do Mastersaf DW com todos os campos existentes em tela\.
		- __EXLUI: __O usuário poderá excluir totalmente um cadastro aberto em tela\. __  __
		- __CONFIRMA__ – Salva os dados incluídos ou alterados\.
		- __RELATÓRIO__ – Para emitir o relatório o usuário poderá selecionar um estabelecimento, e serão listados todos os dados parametrizados para o estabelecimento selecionado\.
		- __FECHA__ – Fecha a janela da parametrização\.

	        

	        __Nesta tela estarão disponíveis os campos:__

                       

- 
	- 
		- Estabelecimento
		- Quadro
		- Data de Apuração
		- Estado
		- Município
		- Código de Atividade
		- Valor/Porcentagem

	     	

__Funcionamento da tela: __Nesta tela o usuário poderá fazer a manutenção do Quadro 47 \- Compras de Extratores, Produtores Agropecuários e Pescadores e Quadro 48 \- Receita de Prestação de Serviço e Fornecimento de Energia Elétrica, os valores aqui salvos serão considerados para geração dos Quadros 47 e 48\.      

__Observações 1: __Se não tem informação na tela de manutenção do quadro 47 OU 48, então a geração vai gerar a partir dos dados de NF \(incluindo telecom\)\.  Caso possua dados na tabela da manutenção do quadro 47 OU 48, só considera estes dados p/ geração do quadro\.   

Alteração da __MFS35840__: Inclusão de novos tipos de atividade \(011, 012 e 013\) para o quadro 48\. Estes novos códigos c correspondem aos códigos 14, 15 e 16 do Ato DIAT 36/2019 \(Anexo III \- Tabela de Itens para Cálculo do Índice de Participação dos Municípios \- IPM\)\. Para estas atividades, a príncipio, não haverá geração automática, e o usuário poderá inserir os valores manualmente quando for o caso\. Por isso, os novos códigos foram incluídos *apenas* na tela de manutenção, e não aparecem nas telas de parametrização por CFOP ou Natureza\.__ 	__

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

Default:

Habilitado

Neste campo será exibido o Estabelecimento escolhido pelo usuário, na Tela de Login do Sistema, não tendo a opção de escolha de outro Estabelecimento, apenas será habilitado para seleção caso o usuário não entre com o Estabelecimento na Tela de Login\. 

OS\_4502

Quadro

Texto

S

N

Formato:

Combo Box

Default:

Habilitado

Neste campo será exibido o respectivo quadro para a inserção dos valores, que deverá exibir as seguintes informações para seleção:

__Quadro 47 \-__ Compras de Extratores, Produtores Agropecuários e Pescadores\. 

  
__Quadro 48 \-__ Receita de Prestação de Serviço e Fornecimento de Energia Elétrica\.

OS\_4502

Data de Apuração

Data

S

N

Formato:

DD/MM/AAAA

Default:

Habilitado

Deverá permitir a gravação do dia/mês/ano\. Utilizar para o critério de busca o dia, mês, e ano que o usuário preencheu\.

OS\_4502

Estado

Texto

S

N

\-

Neste campo estará indicado o estado referente ao estabelecimento indicado, devendo estar bloqueado para manutenção do registro\.

OS\_4502

Município

Texto

S

N

Formato:

Combo Box

Default:

Habilitado

Neste campo deverá trazer os municípios indicado no estabelecimento\. 

OS\_4502

Tipo de Atividade

Texto

S

N

Formato:

Combo Box

Default:

Habilitado 

Neste campo será exibido o Código do tipo de atividade do estabelecimento, que deverá exibir as seguintes informações:

- \(001\) For prestador de serviços de transportes;
- \(002\) For prestador de serviços de telecomunicações;
- \(003\) For fornecedor de energia elétrica por demanda contratada \(lançada no 

CFOP 5257\);

- \(004\) For distribuidor de energia elétrica a consumidor pessoa física ou jurídica;
- \(005\) For fornecedor de gás natural;
- \(006\) For empresa que opere com o marketing direto;
- \(007\) For depósito ou centro de distribuição ou efetuar a entrega de mercadoria vendida por outro estabelecimento do mesmo titular;
- \(008\) For fornecedor de alimentos preparados;
- \(011\) Geração de Energia Elétrica por fonte Hidráulica;
- \(012\) Venda de energia elétrica adquirida de terceiros, realizada por estabelecimento gerador de energia elétrica por fonte hidráulica;
- \(013\) Entrada da energia elétrica em estabelecimento gerador de energia elétrica por fonte hidráulica adquirida de terceiros, para comercialização;
- \(501\) For detentor de TTD de obrigação acessória autorizando a remessa de mercadorias ao varejo ou pronta entrega através de Central Integrada de Distribuição, na qualidade de inscrição única no Estado para tais operações;
- \(502\) For detentor de TTD de obrigação acessória autorizando que nas operações de venda utilize demonstrativo auxiliar especifico para escrituração do Livro de Saídas;
- \(503\) For detentor de TTD de obrigação acessória autorizando que o estabelecimento gerador de energia elétrica possua inscrição única englobando várias PCHs;
- \(504\) Para as saídas das partes e peças de um todo;
- \(505\) Para a transmissão da propriedade do produto final;

\[MFS76462\] 

- \(506\) Autorizando que o estabelecimento trading registre as operações com importação por conta e ordem de terceiros nos CFOP 1949, 2949, 3949, 5949 ou 6949;
- \(506\) autorizando que o estabelecimento trading registre as operações de saída das mercadorias importadas por conta e ordem de terceiros nos CFOP 5949 ou 6949;

\[MFS76462\]

- \(507\) autorizando que o estabelecimento trading registre as operações de entrada das mercadorias importadas por conta e ordem de terceiros nos CFOP 1949, 2949 ou 3949
- \(901\) informar percentual de rateio de VA \(__Valor Adicionado__\) por acordo entre municípios\.

Caso o campo __quadro__ seja igual a QUADRO 48 este campo será desabilitado\. 

OS\_4502

OS\_4581

MFS\-14715

MFS35840

MFS76462

Valor/Percentual

Numérico

S

S

Formato:

0,00

Default:

Habilitado

Este campo receberá o valor ou percentual do ICMS relacionado ao município indicado\. Quando o campo __“Tipo de Atividade”__ for selecionado o __código \(901\)__, este campo deverá ser gravado com o valor em percentual\.

Validação para Percentual: <= 100 é Percentual  

OS\_4502

*\* Descrição não disponível em tela*

