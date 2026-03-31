# MTZ_DIME_SC_Parametros_Geracao_Quadro_01_Por_CFOP

- **Fonte:** MTZ_DIME_SC_Parametros_Geracao_Quadro_01_Por_CFOP.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 63 KB

---

THOMSON REUTERS

Parâmetros p/Geração do Quadro 01 por CFOP

Parâmetro Geração Quadro 01

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4443

Julyana Perrucini

Criação da tela Parâmetros p/Geração do Quadro 01\.

Sumário

[1\.	Regras dos Campos	3](#_Toc382488202)

# <a id="_Toc350763252"></a><a id="_Toc382488202"></a>Regras dos Campos 

__Localização da tela:__ Estadual\\ DIME\-SC\\ Parâmetros\\ Informações de ICMS\\ Quadro 01\\ Por CFOP

__Título da tela: __Parâmetros p/Geração do Quadro 01 por CFOP

__Considerações Gerais: __Parametrização de CFOP para identificar as operações de devolução com valor de ICMS\-ST que serão desconsideradas dos registros 22 e 24 da DIME\-SC\.

__Opções da barra de menu:__

- 
	- 
		- __CONFIRMA__ – Salva os dados incluídos ou alterados\.
		- __RELATÓRIO__ – Para emitir o relatório o usuário poderá selecionar um estabelecimento, e serão listados todos os dados parametrizados para o estabelecimento selecionado\.
		- __FECHA__ – Fecha a janela da parametrização\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Estabelecimento

ComboBox

S

N

\-

Neste campo será exibido o Estabelecimento escolhido pelo usuário, na Tela de Login do Sistema, não tendo a opção de escolha de outro Estabelecimento, apenas será habilitado para seleção caso o usuário não entre com o Estabelecimento na Tela de Login\.

__Tratamento:__

Se o Estabelecimento não for selecionado na Tela de Login e não for selecionado no parâmetro, ao salvar, emitir a mensagem: “Estabelecimento deve ser preenchido”\.

OS4443

Operação

ComboBox

S

N

\-

Permitir o usuário selecionar a operação disponível na lista\. No momento será incluída somente a operação __“Devolução”__, pois será feita uma análise para outras possíveis situações que não deve ser gerado no Quadro 01\.

__Conteúdo:__

- Devolução

__Tratamento:__

Se a Operação não for selecionada no parâmetro, ao salvar, emitir a mensagem: “Operação deve ser preenchida”\.

OS4443

CFOP’s

Checkbox

S

S

\-

Neste quadro serão exibidos todos os CFOP’s de entrada \(iniciados por 1, 2 ou 3\) da SAFX2012 para seleção do usuário\. Quando existir na tabela registros de mesmo CFOP e validades diferentes, será considerado para exibição o registro de maior data de validade \(ou seja, não aparecerão códigos repetidos\)\.

Para facilitar, o usuário poderá utilizar as opções “Selecionar Todos” e “Desmarcar Todos”\.

OS4443

Replicar para os Estabelecimentos

Checkbox

N

N

Através desta opção o usuário poderá replicar a parametrização feita para outros estabelecimentos\.

Ao clicar na opção “Replicar”, serão disponibilizados para seleção do usuário os estabelecimentos da Empresa do login, com exceção do estabelecimento já informado no campo “Estabelecimento”\.

Ao salvar a operação com esta opção ativada, a parametrização feita será gravada para o estabelecimento informado, e também replicada para todos os estabelecimentos selecionados na opção da replicação\. 

Para facilitar, o usuário poderá utilizar as opções “Selecionar Todos” e “Desmarcar Todos”\.

OS4443

