# MTZ-Registro_I355-Detalhe_dos_Saldos_das_Contas_de_Resultado_Antes_do_Encerramento

> Fonte: MTZ-Registro_I355-Detalhe_dos_Saldos_das_Contas_de_Resultado_Antes_do_Encerramento.docx






THOMSON REUTERS

Matriz Registro I355 – Sped Contábil


DOCUMENTO DE REQUISITO



REGRAS DE NEGÓCIO










Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:



| OS/CH | Nome | Descrição |
| --- | --- | --- |
| OS4711 | Elenilson Coutinho | Registro I355 - Detalhes dos Saldos das Contas de Resultado Antes do Encerramento |


| CÓD | DESCRIÇÃO | OS/CH |
| --- | --- | --- |
| RNG-I355 | Registro I355 - Detalhes dos Saldos das Contas de Resultado Antes do Encerramento   Registro é obrigatório caso exista registro I350 Nível hierárquico: 4  Ocorrência: vários (por tipo de escrituração)   Regras de Validação do Registro:   REGRA_COD_CTA_DT_RES_DUPLICIDADE: Verificar se, para uma mesma data de apuração do resultado “DT_RES” (Campo 02 do registro I350), o registro I355 não é duplicado considerando a chave “COD_CTA + COD_CCUS”.   REGRA_REGISTRO_OBRIGATORIO_I350: Verifica se existe lançamento de encerramento (nas escriturações G e R) no “IND_LCTO” (Campo 05 do registro I200), ou seja, deve existir “IND_LCTO” igual a “E” (lançamento de encerramento).   REGRA_VALIDACAO_CONTA_RESULTADO: Verifica se, na data de encerramento, a soma do saldo de cada conta de resultado “VL_SLD_FIN” (Campo 08 do registro I155) é igual a 0.   Regras de Validação dos Campos:  REGRA_CONTA_RESULTADO: Verifica se o “COD_NAT” (Campo 03 do registro I050) é de conta de resultado, ou seja, se a conta é uma conta de resultado (COD_NAT = 04).  REGRA_CONTA_PARA_LANCAMENTO: Verifica se a “REGRA_CONTA_ANALITICA” e a “REGRA_CONTA_NO_PLANO_CONTAS” foram atendidas.   REGRA_CONTA_ANALITICA: Localiza “COD_CTA” (Campo 02) no plano de contas (Registro I050) e verifica se “IND_CTA” é igual a ”A” (conta analítica).     REGRA_CONTA_NO_PLANO_CONTAS: Verifica se “COD_CTA” (Campo 02) existe no plano de contas (registro I050).   REGRA _CCUS_NO_CENTRO_CUSTOS: Verifica se o código do centro de custos “COD_CCUS” (Campo 03) existe no registro I100 (Centro de Custos).  REGRA_VALIDACAO_SALDO_CONTA: Verifica se a soma de todos os lançamentos do tipo encerramento de conta de resultado (“IND_LCTO” – Campo 05 do registro I200) para cada data (“DT_RES” – Campo 02 do registro I350) e conta (considerando se é crédito ou débito) é igual ao valor do saldo final antes do lançamento de encerramento (“VL_CTA” – Campo 04 do registro I355) para escriturações do tipo G ou R (com o indicador de débito ou crédito invertido).  Regara de Geração do Registro:  Quando selecionado o checkbox “Saldo Antes do Encerramento” (SAFX169) – No caminho: Módulo  SPED  ECD- Escrituração Contábil Digital Menu  Parâmetros  Dados Iniciais   Os campos, Empresa, Estabelecimento, Data Saldo e Código da Conta da SAFX169, deverá ser igual a Empresa campo -01, Estabelecimento campo-02,  Data da Operação campo -03 e Conta campo-04 do Lançamento de Encerramento da SAFX01.   O sistema deverá recuperar as informações da tabela SAFX169 – Saldo Antes do Encerramento para compor o registro, ou seja, considerando cada conta e centro de custo para o qual houve movimento.   Ex: I355 - 0001 - 0001A - 1.500,00 - D       I355 - 0001 - 0001B - 3.000,00 - D       I355 - 0001 - 0001C - 4.500,00 – D   Obs: Caso o checkbox “Saldo Antes do Encerramento” (SAFX169) não selecionado, seguir com a forma de geração hoje existente no sistema. | OS4711 |


| RN01 | [EXCLUÍDA – OSXPTO] Descrição da Regra de Negócio 01 | OSNNNN |
| --- | --- | --- |
