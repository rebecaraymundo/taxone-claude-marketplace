# MTZ_EFD_Tela_Geracao_Meio_Magnetico_SPED_Fiscal

> Fonte: MTZ_EFD_Tela_Geracao_Meio_Magnetico_SPED_Fiscal.docx






THOMSON REUTERS

SPED FISCAL
Tela de Geração do SPED Fiscal



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3
2.	Sugestão de Layout	4

## Regras dos Campos


Localização da tela: SPED\ EFD-Escrituração Fiscal Digital\ Geração\ Meio Magnético

Título da tela: Geraçao do Meio Magnetico - EFD


## Sugestão de Layout





| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4812 | Julyana Perrucini | Este documento tem como objetivo criar um parâmetro para limite de quantidade de logs de erro no intuito de melhorar a performance de geração da obrigação acessória SPED Fiscal. |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | OS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Qtd. Max. de logs (0 = todos) | Texto | N | S | Formato:  Text Input  Default:  Habilitado e preenchido com 0 | Permitir ao usuário limitar a quantidade de geração de log de erro emitidos na geração do arquivo magnético.   Tratamento: O campo deverá receber até 4 posições; Quando o campo não for preenchido, converter para default para trazer todos logs. | OS4812 |
