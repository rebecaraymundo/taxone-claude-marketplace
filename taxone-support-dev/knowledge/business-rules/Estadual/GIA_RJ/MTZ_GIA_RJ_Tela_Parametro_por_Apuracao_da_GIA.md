# MTZ_GIA_RJ_Tela_Parametro_por_Apuracao_da_GIA

- **Fonte:** MTZ_GIA_RJ_Tela_Parametro_por_Apuracao_da_GIA.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 62 KB

---

THOMSON REUTERS

Por Apuração da GIA

Tela de Parâmetro Por Apuração da GIA

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

CH10813\_2014

Julyana Perrucini

Alteração da recuperação do campo “Contabilista” da tela de parâmetro Por Apuração da GIA\.

CH9150\_2015

Julyana Perrucini

<a id="OLE_LINK17"></a><a id="OLE_LINK18"></a><a id="OLE_LINK19"></a>Inclusão de tratamento para recuperação de estabelecimentos da opção “Replicar p/ os Estabelecimentos”\.

Sumário

[1\.	Regras dos Campos	3](#_Toc393375277)

# <a id="_Toc350763252"></a><a id="_Toc393375277"></a>Regras dos Campos 

__Localização da tela:__ Estadual\\ GIA\-RJ\\ Parâmetros\\ Por Apuração da GIA\.

__Título da tela: __Parâmetro Por Apuração da GIA\.

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__OS/CH__

Contabilista

Combo Box

N

S

Default: Habilitado

Neste campo o usuário selecionará o contabilista responsável legal pela GIA, de acordo com a tela correspondente \(RESP\_INFORMACAO\), através do Módulo Parâmetros >> Requisitos Legais >> Responsável por Informações\.

__Tratamento:__

\- Disponibilizar na seleção desse campo todos os responsáveis que estiverem com a Categoria da tela Responsável por Informações igual a Contador, Técnico Contador e Empresa\.

__Atenção:__ Não alterar a regra existente, apenas acrescentar a Categoria Empresa\. 

CH10813\_2014

Replicar para os Estabelecimentos

Texto

N

S

Formato:

Check Box

Default:

Habilitado

Através desta opção o usuário poderá replicar a parametrização feita para outros estabelecimentos\.

__\[ALTERADA – CH9150\_2015\]__

Ao clicar na opção “Replicar”, serão disponibilizados para seleção do usuário os estabelecimentos com UF igual a ”RJ” da Empresa do login, com exceção do estabelecimento já informado no campo “Estabelecimento”\.

Ao salvar a operação com esta opção ativada, a parametrização feita será gravada para o estabelecimento informado, e também replicada para todos os estabelecimentos selecionados na opção da replicação\. 

Para facilitar, o usuário poderá utilizar as opções “Selecionar Todos” e “Desmarcar Todos”\.

CH9150\_2015

