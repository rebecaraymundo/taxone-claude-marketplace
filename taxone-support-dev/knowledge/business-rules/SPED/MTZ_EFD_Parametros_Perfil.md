# MTZ_EFD_Parametros_Perfil

> Fonte: MTZ_EFD_Parametros_Perfil.doc

Parâmetros – Perfil – SPED FISCAL

Localização:  Menu Sped, Módulo EFD-Escrituração Fiscal Digital, item Parâmetros ( Perfil


DOCUMENTO DE REQUISITO

DR	Nome	Descrição		OS3576	Botão “Copiar perfil”
	Inserido botão para copiar perfil com intuito de automatizar o cadastro quando é criado um novo leiaute.
		CH23730_2012	D400 e D410	Alterada a regra do flag do D410 para quando o D400 for marcado.		OS3785	Atualização Legal	Ato Cotepe 50 Ago/2012		OS2931-H1	Geração dos Novos Registros de CF-e no Sped Fiscal	Geração dos Novos Registros de CF-e no Sped Fiscal: C116, C800, C850, C860 e C890 (ver RN00).		OS4342	Sped Fiscal – Bloco K	Inclusão do Bloco K nos perfis, e geração dos registros K200 e K220 (ver RN00).		OS4535	Alteração da tabela de layout do Sped 	Inclusão da nova versão 1.0.8 (Ato Cotepe 22/2014)		OS4609	Alteração da tabela de layout do Sped 	Inclusão da nova versão 1.0.9 (Ato Cotepe 49/2014)		MFS4992
(27/06/2016)	Ato Cotepe 7/2016	Criação dos novos registros do Bloco K, e da nova versão de layout 1.10. Ver RN00.		MFS-20986	Ato Cotepe n° 44/2018	Criação de novos registros em atendimento a nova versão de layout 1.12.		MFS31406	Andréa Rocha	Inclusão da nova versão 1.13		MFS45380	Criação de novo perfil	Criação da nova versão de layout 1.14 (Ato COTEPE 44/20, Jan/2021). Ver RN00.		MFS73692	Nova versão de layout	Atualização legal – Ato Cotepe 62/2021 – Nova versão de layout 1.15 (ver RN00).	13/10/2020		MFS85388	Nova versão de layout	Atualização legal – Ato Cotepe 21/2022– Nova versão de layout 1.16. 	09/05/2022		MFS85955	Tratativa para registros do Bloco K	Tratativa para os registros desobrigados de entrega do Bloco K	01/06/2022		MFS93255	Inclusão de novos registros	Inclusão dos registros C855, C857, C895 e C897	28/09/2022		MFS97666	Inclusão de novo registro	Inclusão do registro 0221.	05/12/2022		MFS433981	Cópia de Perfil	Correção de Bug	10/03/2023		MFS861835	Nova versão de layout	Atualização legal – Ato Cotepe 79/2025 Nova versão de layout 1.19 (RN00)	11/08/2025		

REGRAS DE NEGÓCIO

Cód.	Descrição	DR		RN00	Regra Geral

Alteração da OS2931-H1: Os registros C116, C800, C850, C860 e C890, específicos de Cupom Fiscal Eletrônico (CF-e), passarão a ser disponibilizados para seleção do usuário a partir do layout da versão 1.0.4.

Quando o perfil  = A ( serão habilitados os registros  C116, C800 e C850
Quando o perfil  = B ( serão habilitados os registros C116, C860 e C890

Alteração da OS4342: Os registros 0210 e todos os registros do Bloco K (K001, K100, K200, K220, K230, K235, K250, K255 e K990), passarão a ser disponibilizados para seleção do usuário a partir do layout da versão 1.0.7, para os dois perfis de geração (perfil A e perfil B).

Alteração da OS4535: 
Incluída a nova versão de layout “Escrituração Fiscal Digital – Ato Cotepe ICMS 22/2014 – Versão 1.0.8”

Os blocos de registros a serem disponibilizados nesta nova versão são os mesmos da versão 1.0.7, que já inclui o registro “0210-Consumo Específico Padronizado” e o Bloco K.

Obs: A princípio, o registro 0210 e o Bloco K continuarão a ser disponibilizados na versão 1.0.7, com objetivo de possibilitar a geração de arquivos de testes para dados anteriores à 2015.

Alteração da OS4609: 
Incluída a nova versão de layout “Escrituração Fiscal Digital – Ato Cotepe ICMS 49/2014 – Versão 1.0.9”

Os blocos de registros a serem disponibilizados nesta nova versão são os mesmos da versão 1.0.8, que já inclui o registro “0210-Consumo Específico Padronizado” e o Bloco K.

Obs: A princípio, o registro 0210 e o Bloco K continuarão a ser disponibilizados nas versões 1.0.7 e 1.0.8, com objetivo de possibilitar a geração de arquivos de testes para dados anteriores à 2016, já que o Bloco K foi prorrogado para 2016.

Alteração da MFS4992: 
Incluída a nova versão de layout “Escrituração Fiscal Digital – Ato Cotepe ICMS 07/2016 – Versão 1.10”.

Inclusão dos seguintes registros novos do Bloco K:  K210 / K215, K260 / K265, K270 / K275 e K280.

Estes novos registros serão habilitados para marcação apenas quando no campo “Leiaute” a versão escolhida pelo cliente for a nova versão (1.10). Caso contrário, ficarão desabilitados.

Alteração da MFS-15996: 
Incluída a nova versão de layout “Escrituração Fiscal Digital – Ato Cotepe ICMS 48/2017 – Versão 1.11”.

Alteração da MFS-20986: 
Incluída a nova versão de layout “Escrituração Fiscal Digital – Ato Cotepe ICMS 44/2018 – Versão 1.12”.

Inclusão dos seguintes registros novos do Bloco K:  K290 / K291 / K292 / K300 / K301 / K302.

Inclusão dos seguintes registros novos do Bloco B:  B001 / B020 / B025 / B030 / B035 / B350 / B420 / B440 / B460 / B470 / B500 / B510 / B990.

Para essa versão o nome do Registro C177 muda para “Complemento de Item – Outras Informações (Código 01, 55)”, sendo obrigatório nas entradas e nas saídas.

Inclusão de novo registro no Bloco C: C191.

Inclusão de novos registros no Bloco 1: 1960 / 1970 / 1975 / 1980, todos referentes ao GIAF.

Estes novos registros serão habilitados para marcação apenas quando no campo “Leiaute” a versão escolhida pelo cliente for a nova versão (1.10). Caso contrário, ficarão desabilitados.

Alteração da MFS-31406: 
Incluída a nova versão de layout “Escrituração Fiscal Digital – Ato Cotepe ICMS 65/2019 – Versão 1.13”.

Alteração da MFS45380: 
Incluída a nova versão de layout “Escrituração Fiscal Digital – Ato Cotepe ICMS 44/2020 – Versão 1.14”.

Inclusão dos seguintes registros novos do Bloco C:  C181 e C186.

Estes novos registros serão habilitados para marcação apenas quando no campo “Leiaute” a versão escolhida pelo cliente for a nova versão (1.14). Caso contrário, ficarão desabilitados.


Alteração da MFS73692: 
Incluída a nova versão de layout “Escrituração Fiscal Digital – Ato Cotepe ICMS 62/2021 – Versão 1.15”.

Inclusão do novo registro do Bloco 1: 1601.

Este novo registro será habilitado para marcação apenas quando no campo “Leiaute” a versão escolhida pelo cliente for a nova versão (1.15). Caso contrário, não será apresentado.

Alteração da MFS85388:
Incluída a nova versão de layout “Escrituração Fiscal Digital – Ato Cotepe ICMS 21/2022 – Versão 1.16”.

Alteração [MFS85955]
Inclusão do novo registro do Bloco K: K010.

Este novo registro será habilitado para marcação apenas quando no campo “Leiaute” a versão escolhida pelo cliente for a nova versão (1.16). Caso contrário, não será apresentado.

Alteração [MFS93255]
Inclusão dos novos registros do Bloco C: C855, C857, C895 e C897.

Estes novos registros serão habilitados para marcação apenas quando no campo “Leiaute” a versão escolhida pelo cliente for a nova versão (1.16). Caso contrário, não será apresentado.

Alteração [MFS97666]

Inclusão do novo registro do Bloco 0: 0221

Este novo registro será habilitado para marcação apenas quando no campo “Leiaute” a versão escolhida pelo cliente for a nova versão (1.16). Caso contrário, não será apresentado.

Alteração da MFS861835:
Incluída a nova versão de layout “Escrituração Fiscal Digital – Ato Cotepe ICMS 79/2025 – Versão 1.19”.
		RN01	Botão “Copiar perfil”

Se o usuário clicar no botão de copiar sem antes ter escolhido o novo “Leiaute” ou o “Perfil de apresentação” ou “Perfil”, emitir seguinte mensagem:

“Para realizar a cópia de perfil é necessário selecionar o novo “Leiaute” e “Perfil de apresentação” e “Perfil”.
[MFS433981]
São disponibilizados para cópia, apenas perfis de mesmo Tipo de Apresentação do perfil a ser criado. Por exemplo: se está sendo criado um perfil do tipo A, perfis do tipo B não são disponibilizados para serem copiados.
	OS3576		RN02	Botão “Gravar”

[MFS85955] Tratamento em atendimento ao layout  versão 1.16 (Janeiro/2023)

Se no campo Leiaute for selecionada a versão “Escrituração Fiscal Digital – Ato Cotepe ICMS 21/2022 – Versão 1.16”, ao clicar no botar “Gravar” deve ser feita a seguinte verificação:

Se na tela de Dados Iniciais, o campo Tipo de Leiaute estiver selecionado “Simplificado” E um ou mais registros do bloco K que são desobrigados de entrega estiverem marcados (registros K210, K215, K235, K255, K260, K265, K275, K292 ou K302) deve ser emitida a seguinte mensagem:

“Para a geração do Bloco K, no leiaute Simplificado foram marcados alguns registros que são desobrigados de entrega, para a versão 1.16. Deseja prosseguir com a gravação?”

Se o usuário clicar em “Sim”: a gravação dos registros marcados para geração deve ser concluída.
Se o usuário clicar em “Não”: a gravação dos registros marcados não deve prosseguir, para que o usuário desmarque os registros e prossiga posteriormente com a gravação..
	MFS85955		


Registros Bloco D


RND-400	Flag D400

Quando selecionado o Perfil B

Quando o flag D400 for marcado, então marcar automaticamente o flag D410.
	CH23730_2012/OS3785		RND411	Quando selecionado Perfil B:

O Registro D411 deverá ser alterado a coluna Obrig (Saída) para “OE” e (Entrada) não apresentar.
	OS3785		


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN