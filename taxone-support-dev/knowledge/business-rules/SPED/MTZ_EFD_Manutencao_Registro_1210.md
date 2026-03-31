# MTZ_EFD_Manutencao_Registro_1210

> Fonte: MTZ_EFD_Manutencao_Registro_1210.docx






THOMSON REUTERS

Módulo EFD Escrituração Fiscal Digital
Manutenção da Utilização de Créditos Fiscais (Registro 1210)


Localização:  Menu Sped, Módulo EFD-Escrituração Fiscal Digital, item Geração  Manutenção  Registro 1200/1210 (Controle de Créditos)  Registro 1210




DOCUMENTO DE REQUISITO



Sumário

1.	Layout de Tela	3
2.	Regras dos Campos	3



## Layout de Tela






## Regras dos Campos



Alteração da MFS7082: Inclusão do campo “Chave NFe” para atendimento ao Ato Cotepe 07/2016, que inclui esta informação no registro 1210.
















| MFS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS7082 | Alterações do Ato Cotepe 07/2016 | Criação do campo “Chave-NFe” | 29/11/2016 (Criação do Docto) |
| MFS698484 | Andréa Rocha | Alteração da regra do campo Número do documento, que vai deixar de ser obrigatório.  Essa alteração está sendo feita para seguir a regra do guia prático do SPED-EFD, em que o campo 03 do registro 1210 não é obrigatório. | 11/11/2024 |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Tipo da Utilização de Credito |  |  |  |  |  |  |
| Número do Documento | Alfanumérico | N | S |  | Campo de preenchimento não obrigatório, onde será informado o número do documento.  Obs.: O Número do documento é um campo obrigatório na tabela, mas não vai ser obrigatório na tela.  Portanto, deve ser gravado com um espaço em branco na tabela. | MFS698484 |
| Chave NFe | Alfanumérico | N | S |  | Campo de preenchimento não obrigatório, onde será informada a chave do documento fiscal eletrônico. | MFS7082 |
| Valor do Crédito Utilizado |  |  |  |  |  |  |
| Usuário |  |  |  |  |  |  |
| Data Operação |  |  |  |  |  |  |
