# MTZ_REINF_Tela_Geracao_Ajustes_CPRB

- **Fonte:** MTZ_REINF_Tela_Geracao_Ajustes_CPRB.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 66 KB

---

THOMSON REUTERS

Geração dos Ajustes da CPRB – EFD\- Reinf

SPED – Reinf

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS15093

Lara Aline

Inclusão da Tela de Geração dos Ajustes da CPRB do EFD – Reinf

Sumário

[1\.	Regras dos Campos	3](#_Toc498439367)

# <a id="_Toc350763252"></a><a id="_Toc498439367"></a>Regras dos Campos 

__Localização da tela:__ Módulo: SPED >> EFD – Reinf

__                                   __Menu: Cálculo da CPRB >> Geração dos Ajustes da CPRB

__Título da tela: __Geração dos Ajustes da CPRB

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Tipo de Execução

Radio Button

N

S

Default Selecionado: Imediata

Este Campo permite ao usuário programar a importação do arquivo de retorno\. Programação que pode ser:

Imediata \- Processo de importação realizado naquele exato momento\. 

Programada – Processo de importação automático programado para a data e hora desejada pelo usuário\.

MFS15093

Data/Hora de Execução

Texto

N

S

Default: Desabilitado

Este campo permite ao usuário informar a data e hora desejada para importação do arquivo \(Processo automático\)\.

Campo será habilitado apenas quanto o campo Tipo de Execução na opção “Programada” for selecionado\.

MFS15093

Executar

Botão

N

N

Quando acionado o sistema irá iniciar o processo de pré geração dos ajustes\.

MFS15093

Data Inicial

Data

S

S

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a><a id="OLE_LINK4"></a>Formato: DD/MM/AAAA

Caso não preenchido exibir a seguinte mensagem: “O campo Data Inicial deve ser informado”\.

MFS15093

Data Final

Data

S

S

Formato: DD/MM/AAAA

Caso não preenchido exibir a seguinte mensagem: “O campo Data Final deve ser informado”\.

MFS15093

Ajustes

Checkbox

S

S

Default: Não selecionado

Listar os valores:

6 \- Vendas canceladas e os descontos incondicionais concedidos

Ao menos um ajuste deverá ser selecionado, caso contrário exibir a seguinte mensagem: “Ao menos um ajuste deve ser selecionado”\.

MFS15093

Geração Multiempresa

Checkbox

N

S

Default: Não selecionado

Quando selecionado pelo usuário, a geração será multiempresa\.

Este campo interfere na montagem da lista dos estabelecimentos para seleção do usuário, conforme especificado no campo abaixo “Empresa/ Estabelecimento”\.

MFS15093

Selecionar

Pasta de Seleção

N

S

Pasta padrão que permite seleção de um estabelecimento específico\.

MFS15093

Marcar Todos

Checkbox

N

S

Default: não selecionado

Quando selecionado, deve mudar o status dos estabelecimentos para “selecionado”\.

MFS15093

Empresa/Estabelecimento

Checkbox

S

S

Default: não selecionado

Nesse campo deverá apresentar todos os estabelecimentos da empresa do login que possuam o cadastro na tabela SAFX185 para o período selecionado em tela e devido à inclusão do campo Geração Multiempresa, seguir a seguinte regra:

__Se parâmetro “Geração Multiempresa” estiver marcado__

Na lista será demonstrado o código da empresa, código e a razão social de cada estabelecimento, mas neste caso serão demonstradas todas as empresas:

XXX / XXX\-XXXXXXXXXXXXXXXXX

*\(cód\.empresa \+ cód\. e razão social do estabelecimento\)*

__Se parâmetro “Geração Multiempresa” estiver desmarcado__

Na lista será demonstrado apenas o código e a razão social de cada estabelecimento, somente da empresa que acessou o módulo\.

XXX\-XXXXXXXXXXXXXXXXX

*\(cód\. e razão social do estabelecimento\)*

Ao menos uma Empresa/Estabelecimento deverá ser selecionada, caso contrário exibir a seguinte mensagem: Ao menos uma Empresa/Estabelecimento deve ser selecionada\.

MFS15093

