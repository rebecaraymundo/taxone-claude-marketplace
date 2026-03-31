# MTZ-IPI-Geração da Apuração IPI

> Fonte: MTZ-IPI-Geração da Apuração IPI.doc

IPI – Geração da Apuração do IPI

Módulo: Federal ( IPI

Menu: Apuração IPI ( Geração da Apuração
Menu: Emissão Registro IPI ( Emissão P8
Menu: Emissão Registro IPI ( Emissão P8 p/ parâmetro de impressão
Menu: DATA MART ( Apuração do IPI
Menu: DATA MART ( Emissão Registro IPI ( Emissão P8
Menu: DATA MART ( Emissão Registro IPI ( Emissão P8 p/ parâmetro de impressão


DOCUMENTO DE REQUISITO

DR	Nome	Descrição		OS3227	Alterar o tratamento para Notas Fiscais extemporâneas	Não apurar notas fiscais extemporâneas de SAÍDA.		OS3526	Alterar o tratamento para Notas Fiscais especiais = “D”	Não apurar notas fiscais de faturamento simples.		4820	Alteração para exportação em planilha	Este documento tem como objetivo alterar o sistema quanto a geração dos relatórios de apuração de ICMS, ICMSST e IPI, pois, estes  quando salvos em Excel não trás o campo “Data da Apuração”.		
REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN01	Regra para notas fiscais extemporâneas de saída 

Desconsiderar as notas fiscais de saída Extemporâneas, já que os seus valores não serão considerados nos livros P2 e P2A, ou seja, se o campo MOVTO_E_S  (Item 03 da SAFX07) = ‘9’e o campo DAT_ESCR_EXTEMP (Item 77) > 0.
Desconsiderar a nota também em todos os resumos existentes para estes livros.
	OS3227		RN02	Regra para notas fiscais especiais D – Operação de Compra/Venda para entrega Futura

Desconsiderar as notas fiscais com situação especial “D – Operação de Compra/Venda para entrega Futura” (campo 125 da SAFX07 – IND_SITUACAO_ESP) e CFOP’s  “1922, 2922, 3922, 1117, 2117, 3117, 5922, 6922, 7922, 5116, 6116, 7116, 1923, 2923, 5923 ou 6923” (campos 14 da SAFX07, 22 da SAFX08 ou 17 da SAFX09 – COD_CFOP), já que os seus valores não serão considerados nos livros P1, P1A, P2, P2A, P8 e P9.
Desconsiderar a nota também em todos os resumos existentes para estes livros.
	OS3526		RN03	Relatório de Apuração do IPI

Incluir o campo “DAT_APURACAO” no relatório de apuração do IPI salvo em Excel. 
Formato: DD/MM/AAAA exemplo: 31/01/2015 00:00:00

Relatório IPI: 02 – RESUMO

Observação: Considerar também o menu: Emissão do Registro de IPI.
	OS4820		


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN