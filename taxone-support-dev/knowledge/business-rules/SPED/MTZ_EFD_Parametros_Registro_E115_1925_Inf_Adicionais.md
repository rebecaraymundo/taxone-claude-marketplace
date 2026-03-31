# MTZ_EFD_Parametros_Registro_E115_1925_Inf_Adicionais

> Fonte: MTZ_EFD_Parametros_Registro_E115_1925_Inf_Adicionais.docx




THOMSON REUTERS

Módulo Sped Fiscal – Parametrização dos Códigos das Informações
Adicionais da Apuração p/os Registros E115 e 1925

MFS-13074: Essa demanda serve para reformular o item de menu que atende a parametrização do Registro E115, acrescentando o item de menu Registros E115/1925, em que haverá outras opções além da  Informações Adicionais da Apuração (Registro E115/1925).

Localização: Menu SPED, Módulo EFD – Escrituração Fiscal Digital, item Parâmetros  Registros E115/1925  Informações Adicionais da Apuração (Registro E115/1925)

DOCUMENTO DE REQUISITO






REGRAS DE NEGÓCIO



Esta parametrização foi criada pela OS2388-N2ge (Fev/2009).

Nesta tela são cadastrados os códigos da Tabela das Informações Adicionais da Apuração, utilizada nos registros E115 e 1925 (Valores Declaratórios) do arquivo do Sped Fiscal.

Os códigos são definidos por UF, assim como várias tabelas do Sped, como por exemplo:
- Códigos de Ajustes provenientes de NF’s (módulo DW – Manutenção – Cadastros)
- Código de Ajuste Sped Fiscal (módulo ICMS - Apuração – Apuração do ICMS – Lanctos Complementares)
- Códigos de Tipos de Utilização de Crédito (módulo Sped – Geração – Manutenção) (OS2388-Vge)



UF:

Este campo é uma lista das unidades da federação (tabela ESTADO), para seleção do usuário.

Default: (sem preenchimento)



Código da Informação Adicional

Tamanho: 8 posições
Tipo: alfanumérico

- Os dois primeiros caracteres do código são a própria sigla da UF, e na inserção de novos registros ficam sempre “fixos” com a sigla da
UF selecionada no campo “UF”;

- Os seis últimos caracteres são a parte “livre” do código, que são específicos de cada UF. Na inserção de novos registros esta parte
será informada pelo usuário, e terá obrigatoriamente um conteúdo numérico);

Ao salvar a operação, será verificada se a parte “livre” do código tem realmente um conteúdo numérico. Caso não, será exibida a seguinte mensagem de erro e a operação não será salva:

“A parte final do código da informação  adicional deve ser um número”

OS4593-B (correção de erro): A descrição do campo foi corrigida para o nome correto (“Código da Informação Adicional”), definido na criação da tela, ao invés do nome “Tipo de Utilização de Crédito ”que aparecia na tela.




Descrição

Tamanho: 250 posições
Tipo: alfanumérico

Campo de preenchimento obrigatório

Ao salvar a operação, será verificado o preenchimento do campo, e se não informado, será exibida a seguinte mensagem de erro e a operação não será salva:
“O campo Descrição deve ser informado”



[MFS693829] Inclusão do campo

Não Preencher Descrição Complementar do Ajuste

Tamanho: 1 posição
Tipo: checkbox

Campo de preenchimento não obrigatório.  Default desmarcado.




[MFS1019580] Inclusão do campo

Não Preencher Valor de Informação Adicional

Tamanho: 1 posição
Tipo: checkbox

Campo de preenchimento não obrigatório.  Default desmarcado.



= = = = =


| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| OS4593-A | Vânia Mattos | Correção de erro na chamada da geração do mapa das entradas | 17/09/2014 (criação do docto) |
| MFS-13074 | Julyana Perrucini | Alteração na estrutura do item de menu Parâmetros - Informações Adicionais da Apuração (Registro E115/1925). | 19/10/2017 |
| MFS693829 | Andréa Rocha | Criação de um campo para indicar se a descrição complementar do ajuste (campo 04- DESCR_COMPL_AJ) deve ser informada na geração do registro E115. | 10/10/2024 |
| MFS1019580 | Rogério Ohashi | Criação de um campo para indicar se o Valor de Informação Adicional (campo 3- VL_INF_ADIC) deve ser informada na geração do registro E115. | 13/01/2026 |


| RN00 | Regras Gerais |
| --- | --- |


| RN01 | Campo UF |
| --- | --- |


| RN02 | Campo Código da Informação Adicional |
| --- | --- |


| RN03 | Campo Descrição |
| --- | --- |


| RN04 | Campo Não Preencher Descrição Complementar do Ajuste |
| --- | --- |


| RN05 | Campo Não Preencher Valor de Informação Adicional |
| --- | --- |
