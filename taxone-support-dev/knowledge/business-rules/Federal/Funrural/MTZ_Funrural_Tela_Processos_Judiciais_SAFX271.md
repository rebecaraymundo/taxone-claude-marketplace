# MTZ_Funrural_Tela_Processos_Judiciais_SAFX271

- **Fonte:** MTZ_Funrural_Tela_Processos_Judiciais_SAFX271.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 66 KB

---

THOMSON REUTERS

Informações de <a id="_Hlk509310579"></a>Processos Judiciais com decisão/sentença – Produtor Rural

Manutenção SAFX271

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

MFS22135

Lara Aline

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a>Definição das regras de manutenção para os campos da SAFX271\.

MFS22920

Lara Aline 

Inclusão do campo Tipo de Processo Judicial

CH31407\_2018

MFS23436

João Henrique

Alteração na manutenção da SAFX271 para que o sistema salve os dados se um dos campos: __“Valor da Contribuição Previdenciária Não Retida” __OU__ ”Valor da contribuição para o GILRAT Não Retido” __OU__ “Valor da contribuição para o SENAR Não Retido”__ estiver preenchido com valor maior que zero\.  

Sumário

[1\.	Regras dos Campos	3](#_Toc509319436)

# <a id="_Toc350763252"></a><a id="_Toc509319436"></a>Regras dos Campos 

__Localização da tela:__ Federal \\ Funrural \\ <a id="OLE_LINK54"></a><a id="OLE_LINK55"></a>Movimento \\ Manutenção dos Dados da NF \\ \(Botão:  Processos Judiciais – \(S\-1250\)\)

__Título da tela:__  Processos Judiciais – \(S\-1250\)

__Regra Geral Botões:__

__NOVO – __Permite inserir novo registro\.

__EXCLUI – __Permite excluir registro inserido\.

__CONFIRMA – __Permite salvar registro\.

__FECHA – __Permite sair da tela\.

__Regra Geral: __

- Podem existir até 10 Processos Judiciais por Produtor\. 
- O sistema deverá verificar se no campo 15 \- VLR\_CONT\_PREV\_N\_RET __ou__ 16 \- VLR\_GILRAT\_N\_RET __ou__ 17 VLR\_SENAR\_N\_RET existe valor __maior__ que zero\. Caso exista, o sistema deve permitir o cadastro na manutenção da SAFX271 com os dados\. Se os campos estiverem sem valor, zerados, uma mensagem no log deve ser exibida: *“Por favor informar um valor maior que zero em ao menos um dos impostos: Valor Contrib\. ou Valor Senar ou Valor Gilrat”*\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Tipo de Processo Judicial

DropDown

S

S

Default = Não selecionado

Deverá listar as seguintes opções:

1 – Processo Judicial do Produtor;

2 – Processo Judicial Coletivo\.

Caso não preenchido exibir a seguinte mensagem: “Tipo de Processo Judicial deve ser informado”

MFS22920

Número do Processo

Pasta

S

S

Default = Não selecionado

Deverão ser listados os processos conforme cadastro de processos na tela: \(MastersafDW >> Menu Manutenção >> Códigos >> Cadastro de Processo Admin/Judicial \(REINF/eSocial\) aba Informações do Processo \(SAFX2058\)\), filtrando APENAS pelos Processos que o Tipo do Processo = ‘Judicial’ ou ‘Processo FAP’ E que o campo Incide eSocial esteja selecionado\. 

Caso não preenchido exibir a seguinte mensagem: “Número de Processo deve ser informado”

Caso o número do processo não cadastrado na SAFX2058 exibir a seguinte mensagem: “Cadastro Processo Administrativo/Judicial não cadastrado”

MFS22135

Código da Suspensão 

Pasta

S

S

Default = Não selecionado

Deverão ser listados os códigos conforme cadastro de suspensão na tela: \(MastersafDW >> Menu Manutenção >> Códigos >> Cadastro de Processo Admin/Judicial \(REINF/eSocial\) aba Informações de Suspensão de Exigibilidade de Tributos \(SAFX2059\)\) filtrando APENAS pelos Processos que o Tipo do Processo = ‘Judicial’ ou ‘Processo FAP’ E que o campo Incide eSocial esteja selecionado\. 

Caso não preenchido exibir a seguinte mensagem: “Código da Suspensão deve ser informado”

Caso Código de Suspensão não cadastrado na SAFX2059 exibir a seguinte mensagem “Informação de Suspensão de Exibilidade de Tributos não cadastrada”

MFS22135

Valor da Contribuição Previdenciária não retida

Text Box

S

S

Informar o Valor da Contribuição Previdenciária não retida

Caso não preenchido exibir a seguinte mensagem: “Valor da Contribuição Previdenciária não retida deve ser informado”

MFS22135

Valor da contribuição para Gilrat não retida

Text Box

S

S

Informar o Valor da contribuição para Gilrat não retida\.

Caso não preenchido exibir a seguinte mensagem: “Valor da contribuição para Gilrat não retida deve ser informado”

MFS22135

Valor da contribuição para o Senar não retido

Text Box

S

S

Informar o Valor da contribuição para o Senar não retido

Caso não preenchido exibir a seguinte mensagem: “Valor da contribuição para o Senar não retido deve ser informado”

MFS22135

