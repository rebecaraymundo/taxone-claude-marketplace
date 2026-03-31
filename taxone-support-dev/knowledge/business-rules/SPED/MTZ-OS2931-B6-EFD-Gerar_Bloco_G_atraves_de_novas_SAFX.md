# MTZ-OS2931-B6-EFD-Gerar_Bloco_G_atraves_de_novas_SAFX

> Fonte: MTZ-OS2931-B6-EFD-Gerar_Bloco_G_atraves_de_novas_SAFX.doc

TITLE   \* MERGEFORMAT EFD - Geração do Bloco G com cálculos não apurados pelo módulo Ativo Permanente


DOCUMENTO DE REQUISITO

DR	Nome	Descrição		OS2931-B6
	 TITLE   \* MERGEFORMAT EFD - Geração do Bloco G com cálculos não apurados pelo módulo Ativo Permanente	Criação do parâmetro “Gerar os registros a partir de valores não calculados pelo módulo Ativo Permanente” na tela de parametrização de Dados Iniciais
Gerar as informações do Bloco G a partir das novas tabelas SAFX criadas na OS2931-B4. As tabelas são:
SAFX133 
SAFX134 
SAFX135 
SAFX136
Geração dos registros pertinentes ao Bloco G (G001, G110, G125, G126, G130 e G140) e Bloco 0 (0200, 0300, 0305, 0500 e 0600).		


Cód.	Descrição	DR		RN01	Criar o parâmetro “Gerar os registros a partir de valores não calculados pelo módulo Ativo Permanente” dentro do grupo “Bloco G - Controle do Crédito de ICMS do Ativo Permanente - CIAP”. Esse novo grupo e novo parâmetro serão disponibilizados no módulo SPED >> EFD – Escrituração Fiscal Digital, menu Parâmetros >> Dados Iniciais.

Esse novo parâmetro será disponibilizado antes da replicação para outros estabelecimentos – funcionalidade essa já existente na tela.	OS2931-B6		RN02	Por default, o parâmetro citado na RN01 ficará desmarcado.	OS2931-B6		RN03	O relatório de conferência dessa tela deverá ser alterado para contemplar o novo parâmetro criado. Deverá ser criada uma nova coluna para demonstrar se o parâmetro foi selecionado ou não. Caso o parâmetro esteja marcado deverá aparecer na coluna “Sim”, caso esteja desmarcado deverá aparecer “Não”.	OS2931-B6		RN04	Caso o parâmetro esteja selecionado, a geração será realizada através das novas tabelas do tipo SAFX criadas (vide tabelas SAFX133, SAFX134, SAFX135 e SAFX136 da OS2931-B4). As regras de geração estão contidas no documento SPED_Fiscal_Regras_BlocoG_OutrasOrigens.doc.

Caso o parâmetro esteja desmarcado, a geração será realizada através dos valores calculados pelo módulo Ativo Permanente – vide documento Sped_Fiscal_Regras.doc.	OS2931-B6		RN05	No processo de geração do meio magnético, caso a Conta Contábil informada no campo 06 do registro 0300 não esteja cadastrada na tabela SAFX2002, deverá ser exibida a seguinte mensagem:

“Conta Contábil <código da conta contábil> não cadastrada na tabela de Contas Contábeis do produto. (módulo: DW – menu: Manutenção >> Códigos >> Plano de Contas).	OS2931-B6		RN06	No processo de geração do meio magnético, caso o Centro de Custo informado no campo 02 do registro 0305 não esteja cadastrada na tabela SAFX2003, deverá ser exibida a seguinte mensagem:

“Centro de Custo <código do centro de custo> não cadastrado na tabela de Centro de Custos do produto. (módulo: DW – menu: Manutenção >> Códigos >> Centro de Custo).	OS2931-B6		RN07	Caso o campo “Índice de participação” da tabela SAFX133 não seja o resultado da divisão dos campos “Valor Total das saídas tributadas e para exportação” pelo campo “Valor total das saídas” da mesma tabela deverá ser exibido mensagem de erro informando tal ocorrência.	OS2931-B6		RN08	Caso o campo “Valor da parcela a ser apropriada” da tabela SAFX133 não seja o resultado da multiplicação dos campos “Somatório das parcelas passíveis de apropriação de cada bem” pelo “Índice de participação” da mesma deverá ser exibido mensagem de erro informando tal ocorrência.	OS2931-B6		RN09	Caso o campo “Índice de participação” da tabela SAFX136 não seja o resultado da divisão dos campos “Valor Total das saídas tributadas e para exportação” pelo campo “Valor total das saídas” da mesma tabela deverá ser exibido mensagem de erro informando tal ocorrência.	OS2931-B6		RN10	Caso o campo “Valor de outros créditos a ser apropriado” da tabela SAFX136 não seja o resultado da multiplicação dos campos “Valor do ICMS passível de apropriação” pelo “Índice de participação” da mesma deverá ser exibido mensagem de erro informando tal ocorrência.	OS2931-B6		RN11	Caso o campo “Chave do Documento Fiscal Eletrônico” da tabela SAFX135 seja informado e o campo “Indicador do Emitente” da mesma tabela seja diferente de 0, deverá ser exibido mensagem de erro informando tal ocorrência.	OS2931-B6		

Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN		
Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01	[ALTERADA – OSXPTO] Descrição da Regra de Negócio 01	OSNNNN