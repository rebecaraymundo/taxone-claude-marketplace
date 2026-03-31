# MTZ_EFD_Manutencao_Registro_1255

> Fonte: MTZ_EFD_Manutencao_Registro_1255.docx






THOMSON REUTERS

Módulo EFD- Escrituração Fiscal Digital – Manutenção da Tabela SAFX304

SAFX304 - Saldo Consolidado da Restituição/Complemento de ICMS


Localização: Menu SPED, Módulo: EFD – Escrituração Fiscal Digital, item Geração  Manutenção  Registro 1255





DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Layout da Tela	3
3.	Regras de Funcionamento dos Campos	4
























## Regras Gerais


Esta tabela será usada para gerar o registro 1255 do SPED-EFD, que é filho do registro 1250.

Estrutura das tabelas  vide manual de layout

Campos que compõe a chave das tabelas:

[Código da empresa + Código do estabelecimento + Data da apuração + Código do Motivo]



## Layout da Tela




Botões da barra de menu:



## Regras de Funcionamento dos Campos








= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS31410 | Andréa Rocha | Criação da tabela SAFX304 para geração do registro 1255, da nova versão do SPED - EFD- Escrituração Fiscal Digital (vigência Jan/2020). | 23/12/2019 |
|  |  |  |  |
|  |  |  |  |


| NOVO | Ao clicar nesta opção, as informações dos campos serão limpas e o usuário poderá incluir um novo registro. |
| --- | --- |
| ABRE | Ao clicar nesta opção, será aberta a janela para seleção dos registros já cadastrados para consulta ou manutenção. |
| EXCLUI | Esta opção permite a exclusão do registro. |
| CONFIRMA | Opção para salvar as informações do registro incluído ou alterado. |
| RELATÓRIO | Esta opção permite imprimir os dados da tabela. Trata-se de opção padrão das telas de manutenção do sistema. |
| FECHA | Fecha a tela da manutenção. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | Alfanumérico | S | S | Listbox | Neste campo será exibida a lista dos estabelecimentos da empresa para seleção do usuário.  Caso tenha sido informado um estabelecimento no login, este campo exibirá fixo o estabelecimento informado, e o usuário não poderá alterá-lo. | MFS31410 |
| Data Apuração | Data | S | S | (DD/MM/AAAA) | Neste campo será informada uma data válida. | MFS31410 |
| Código do Motivo | Alfanumérico | S | S |  | Este campo trabalha com janela de seleção da tabela dos códigos de motivo de restituição / complementação de ICMS (DWT_COD_MOTIVO_SPED).  Quando o Código do Motivo for digitado, será validado a sua existência na tabela.  Caso não exista, será exibida a mensagem “Código do Motivo não cadastrado”. | MFS31410 |
| Valor do ICMS | Numérico | N | S |  | Neste campo será informado o valor do ICMS. | MFS31410 |
| Valor do ICMS ST Restituição | Numérico | N | S |  | Neste campo será informado o valor total do ICMS/ST que o informante tem direito ao crédito, referente às hipóteses de restituição em que há previsão deste crédito. | MFS31410 |
| Valor do FCP ST Restituição | Numérico | N | S |  | Neste campo será informado o valor total do FCP_ST agregado ao valor do ICMS/ST. | MFS31410 |
| Valor do ICMS ST Complemento | Numérico | N | S |  | Neste campo será informado o valor total do débito referente ao complemento do imposto. | MFS31410 |
| Valor do FCP ST Complemento | Numérico | N | S |  | Neste campo será informado o valor total do FCP_ST ST agregado ao valor do ICMS/ST. | MFS31410 |
