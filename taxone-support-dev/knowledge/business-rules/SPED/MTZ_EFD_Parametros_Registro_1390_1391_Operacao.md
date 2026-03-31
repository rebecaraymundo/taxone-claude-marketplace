# MTZ_EFD_Parametros_Registro_1390_1391_Operacao

> Fonte: MTZ_EFD_Parametros_Registro_1390_1391_Operacao.docx






THOMSON REUTERS

Parâmetros p/ Operação – Registro 1390/1391
SPED Fiscal – Parâmetro Registro 1390/1391



DOCUMENTO DE REQUISITO


Sumário

1.	Regras dos Campos	3

## Regras dos Campos


Localização da tela: SPED\ EFD-Escrituração Fiscal Digital\ Parâmetros\ Registro 1390/1391\ Operação

Título da tela: Parâmetros p/ Operação – Registro 1390/1391





| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| CH24790-C_2015 | Julyana Perrucini | Este documento tem como objetivo incluir a Obrigação Fiscal “QTD PRODUZIDA”. |
| MFS77290 | Liliane Assaf | Inclusão da Obrigação Fiscal “Entradas – Açúcar proveniente de mel” |


| Campo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- |
| Obrigação Fiscal | Texto | S | N | Formato:  Combo Box  Default:  Habilitado e Sem seleção | Neste campo exibe uma lista contendo as obrigações cadastradas numa tabela fixa para selecionar o tipo de obrigação que será atendida de acordo com o Registro 1390.  Conteúdo: CONSUMO ENTRADAS - PRODUÇÃO ENTRADAS - ÁLCOOL PROVENIENTE DE MEL [MFS77290] ENTRADAS - AÇÚCAR PROVENIENTE DE MEL ENTRADAS - REPROCESSO ENTRADAS - OUTRAS ENTRADAS OUTRAS - MEL SAÍDAS - EVAPORAÇÃO/PERDA SAÍDAS - REPROCESSO SAÍDAS - OUTRAS SAÍDAS OUTRAS - MEL QTD PRODUZIDA    O usuário lança no Movimento de Estoque a quantidade de movimentações de entrada/saída. De acordo com a operação informada na Movimentação de Estoque o sistema verifica nessa parametrização o equivalente da operação e informa isso no SPED FISCAL. | CH24790-C_2015 MFS77290 |
