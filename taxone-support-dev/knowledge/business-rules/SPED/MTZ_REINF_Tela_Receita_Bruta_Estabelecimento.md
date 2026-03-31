# MTZ_REINF_Tela_Receita_Bruta_Estabelecimento

> Fonte: MTZ_REINF_Tela_Receita_Bruta_Estabelecimento.docx






THOMSON REUTERS

CPRB – Receita Bruta do Estabelecimento
EFD-REINF



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	4


## Regras dos Campos


Localização da tela: Módulo: SPED >> REINF
Menu: CPRB >> Receita Bruta do Estabelecimento

Título da tela: CPRB – Receita Bruta do Estabelecimento






| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS14998 | Lara Aline | Inclusão da Tela de Receita Bruta do Estabelecimento do EFD – Reinf |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Estabelecimento | TextBox | S | S |  | Campo será carregado com o estabelecimento logado no sistema. Caso nenhum estabelecimento tenha sido selecionado no log, serão listados todos os estabelecimentos da empresa logada e que usuário tenha permissão de acesso. | MFS14998 |
| Competência (Mês/Ano) | Data | S | S | MM/AAAAA | Caso não preenchido exibir a seguinte mensagem: “Competência (Mês/Ano) deve ser informado” | MFS14998 |
| Valor Receita Bruta - Total | TextBox | S | S | Default: Aplicativo do Contribuinte | Caso não preenchido exibir a seguinte mensagem: “Valor Receita Bruta - Total deve ser informado” | MFS14998 |
