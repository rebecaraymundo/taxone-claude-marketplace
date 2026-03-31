# MTZ_Funrural_Tela_Geracao_a_partir_de_NF

- **Fonte:** MTZ_Funrural_Tela_Geracao_a_partir_de_NF.docx
- **Modificado:** 2025-01-31
- **Tamanho:** 69 KB

---

THOMSON REUTERS

Tela de Geração a partir de NF

Federal \- FUNRURAL

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

Tela de Geração a partir de NF

Tela de <a id="_Hlk529464055"></a>Geração a partir de NF

MFS22136

Lara Aline

Inclusão do campo Alíquota Gilrat

MFS\-70528

Rogério Ohashi

Inclusão do campo “Forma de Tributação do Produtor Rural: Sobre a folha de pagamento”

MFS755310

Andréa Rocha

Inclusão de um parâmetro para indicar se devem ser consideradas as notas fiscais de entrada de terceiros\.

Sumário

[1\.	Regras dos Campos	3](#_Toc496281226)

# <a id="_Toc350763252"></a><a id="_Toc496281226"></a>Regras dos Campos 

__Localização da tela:__ Módulo: Federal >> Funrural

__                                   __Menu: Movimento >> Geração a partir de NF

__Título da tela: __Geração a partir de NF

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Estabelecimento

TextBox

S

S

Campo será carregado com o estabelecimento logado no sistema\. Caso nenhum estabelecimento tenha sido selecionado no log, serão listados todos os estabelecimentos da empresa logada e que usuário tenha permissão de acesso\.

Período

Data

S

S

Formato: DD/MM/AAAA

Campo para informação do período de geração\.

Caso não preenchido será apresentada a mensagem:

‘Período deve ser preenchido’

Alíquota Contribuição

Pessoa Física

Numérico

S

S

Informar alíquota de contribuição para Pessoa Física\.

Caso não preenchido será apresentada a mensagem:

‘Alíquota de Contribuição de Pessoa Física deve ser preenchida’

Pessoa Jurídica

Numérico

S

S

Informar alíquota de contribuição para Pessoa Jurídica\.

Caso não preenchido será apresentada a mensagem:

‘Alíquota de Contribuição de Pessoa Jurídica deve ser preenchida’

Alíquota Gilrat

Pessoa Física

Numérico

N

S

Informar Alíquota Gilrat para Pessoa Física\.

MFS22136

Pessoa Jurídica

Numérico

N

S

Informar Alíquota Gilrat para Pessoa Jurídica\.

MFS22136

Alíquota Senar

Pessoa Física

Numérico

N

S

Informar Alíquota Senar para Pessoa Física\.

Pessoa Jurídica

Numérico

N

S

Informar Alíquota Senar para Pessoa Jurídica\.

Geração somente para Pessoa Física / Jurídica c/ retenção

Checkbox

N

S

Default: Não selecionado

Quando selecionado deverá gerar somente para Pessoa Física / Jurídica c/ retenção

Geração somente para Produto c/ retenção de INSS

Checkbox

N

S

Default: Não selecionado

Quando selecionado deverá gerar somente para Produto c/ retenção de INSS

Geração somente para CFOP/Natureza c/ retenção

Checkbox

N

S

Default: Não selecionado

Quando selecionado deverá gerar somente para CFOP/Natureza c/ retenção

Forma de Tributação do Produtor Rural: Sobre a folha de pagamento

Checkbox

N

S

Default: Não selecionado

Quando selecionado os Campos de Valores/Alíquota de Contribuição e Gilrat não deverão ser calculados \(Deverá ser preenchido com zero\)\.

MFS\-70528

Considerar NF Entrada de Terceiros

Checkbox

N

S

Default: Não selecionado

Quando selecionado, as notas fiscais de entrada de terceiros \(MOVTO\_E\_S = 1\) serão consideradas para a geração\.

MFS755310

