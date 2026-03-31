# MTZ_Tela_Parametros_Identificacao_Natureza_Rendimento

> Fonte: MTZ_Tela_Parametros_Identificacao_Natureza_Rendimento.docx






THOMSON REUTERS

Parâmetro
Identificação da Natureza de Rendimento



DOCUMENTO DE REQUISITO


Sumário

1.	TELA	3
2.	Regras dos Campos	3

## TELA




## Regras dos Campos


Localização da tela: Módulo: SPED>> SPED >> EFD – REINF
Menu: Parâmetros >> Identificação da Natureza de Rendimento

Título da tela: Identificação da Natureza de Rendimento


Campos de preenchimento obrigatório: Natureza de Rendimento e pelo menos um dos campos (Pessoa  Fís/Jur (Gr./Ind.Cód./Val.), Cód. Receita e ou) Serviço para Atribuição da Natureza de Rendimento




| MFS | Nome | Descrição |
| --- | --- | --- |
| MFS-97021 | Alessandra Cristina Navatta | Criação do Documento |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS |
| --- | --- | --- | --- | --- | --- | --- |
| Natureza de Rendimento | Combo | S | S | Default: Não selecionado | Recuperar as informações da Taces101, tabela DWT_COD_NAT_REND (campo COD_NAT_REND) | MFS-97021 |
| Pessoa Fís/Jur (Gr./Ind.Cód./Val.) | Pasta | N | S | (Gr./Ind.Cód./Val.) | Abrir a tela de grupo para seleção. Considerando o grupo selecionado, recuperar as informações da SAFX04. | MFS-97021 |
| Cód. Receita | Combo | N | S | Default: Não selecionado | Recuperar as informações da Taces14, tabela DWT_COD_RECEITA (campo COD_RECEITA) | MFS-97021 |
| Serviço para Atribuição da Natureza de Rendimento | Texto | N | S |  | Permite informar o serviço que será considerado na parametrização  Campo de Tamanho 10 e Alfanumérico. | MFS-97021 |
