# MTZ_SAICS_Tela_Parametrização_IVA

> Fonte: MTZ_SAICS_Tela_Parametrização_IVA.docx






THOMSON REUTERS

Módulo SAICS – Sistema de Apuração do ICMS – Parametrização IVA



DOCUMENTO DE REQUISITO



Sumário

1.	Regras dos Campos	3
2.	Layout de Tela	4

## Regras dos Campos


Localização da tela: Menu: Estadual
Módulo: SAICS – Sistema de Apuração do ICMS – Custo
Item de Menu: Parâmetros >> Parametrização IVA

Título da tela: Parametrização IVA


Considerações Gerais:

Esta parametrização do IVA (Índice de Valor Agregado) é aplicável a Declaração Simplificada, conforme portaria CAT 207/20009, o usuário deverá informar nesse campo o índice de valor agregado obtido pela empresa conforme dispõe o artigo 30 das DDTT do Regulamento do ICMS.

Opções da barra de menu:

NOVO – Limpa todos os campos da tela, com exceção do estabelecimento, permitindo a inclusão de um novo registro;

ABRE – Ao clicar nesta opção, serão exibidos para seleção do usuário todos os dados já parametrizados. O usuário poderá selecionar um registro, e seus dados serão exibidos em tela para consulta / alteração / exclusão;

EXCLUI – Permite a exclusão dos dados.

CONFIRMA – Salva os dados incluídos ou alterados.

IMPRIME – Imprime todos os dados parametrizados para o estabelecimento selecionado.

RELATÓRIO – Para emitir o relatório o usuário poderá selecionar um estabelecimento, e serão listados todos os dados parametrizados para o estabelecimento selecionado.

FECHA – Fecha a janela da parametrização.























## Layout de Tela



| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS586454 | Rogério Ohashi | Alteração no campo de Índice de Valor Agregado (IVA) para 4 casas decimais. | 21/11/2023 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | N |  | Este campo é uma lista dos estabelecimentos da empresa para seleção do usuário, se o usuário selecionar um Estabelecimento na Tela de Login o Estabelecimento selecionado será listado não tendo a opção de escolha de outro Estabelecimento. | MFS586454 |
| Data de Validade | Date | S | S | Data (dd/mm/aaaa) | Este campo será informado a data inicial da validade da parametrização. Em caso de mudanças na legislação, uma nova data de validade poderá ser utilizada para recadastrar os itens alterados. | MFS586454 |
| Índice de Valor Agregado (IVA) | Numérico | S | S |  | Este campo será informado o índice de valor agregado obtido pela empresa conforme dispõe o artigo 30 das DDTT do Regulamento do ICMS.  [MFS586454]   Alteração para 4 casas decimais, conforme layout do registro 5325. | MFS586454 |
