# MTZ-Registro_I355-Detalhe_dos_Saldos_das_Contas_de_Resultado_Antes_do_Encerramento

- **Fonte:** MTZ-Registro_I355-Detalhe_dos_Saldos_das_Contas_de_Resultado_Antes_do_Encerramento.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 63 KB

---

THOMSON REUTERS

Matriz Registro I355 – Sped Contábil

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4711

Elenilson Coutinho

Registro I355 \- Detalhes dos Saldos das Contas de Resultado Antes do Encerramento

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RNG\-I355

__Registro I355 \- Detalhes dos Saldos das Contas de Resultado Antes do Encerramento __

Registro é obrigatório caso exista registro I350

Nível hierárquico: 4 

Ocorrência: vários \(por tipo de escrituração\) 

__Regras de Validação do Registro:__

__ __

__REGRA\_COD\_CTA\_DT\_RES\_DUPLICIDADE:__ Verificar se, para uma mesma data de apuração do resultado “DT\_RES” \(Campo 02 do registro I350\), o registro I355 não é duplicado considerando a chave “COD\_CTA \+ COD\_CCUS”\. 

__REGRA\_REGISTRO\_OBRIGATORIO\_I350:__ Verifica se existe lançamento de encerramento \(nas escriturações G e R\) no “IND\_LCTO” \(Campo 05 do registro I200\), ou seja, deve existir “IND\_LCTO” igual a “E” \(lançamento de encerramento\)\. 

__REGRA\_VALIDACAO\_CONTA\_RESULTADO:__ Verifica se, na data de encerramento, a soma do saldo de cada conta de resultado “VL\_SLD\_FIN” \(Campo 08 do registro I155\) é igual a 0\. 

__Regras de Validação dos Campos:__

__REGRA\_CONTA\_RESULTADO:__ Verifica se o “COD\_NAT” \(Campo 03 do registro I050\) é de conta de resultado, ou seja, se a conta é uma conta de resultado \(COD\_NAT = 04\)\.

__REGRA\_CONTA\_PARA\_LANCAMENTO__: Verifica se a “REGRA\_CONTA\_ANALITICA” e a “REGRA\_CONTA\_NO\_PLANO\_CONTAS” foram atendidas\. 

__REGRA\_CONTA\_ANALITICA:__ Localiza “COD\_CTA” \(Campo 02\) no plano de contas \(Registro I050\) e verifica se “IND\_CTA” é igual a ”A” \(conta analítica\)\. 

 

__REGRA\_CONTA\_NO\_PLANO\_CONTAS:__ Verifica se “COD\_CTA” \(Campo 02\) existe no plano de contas \(registro I050\)\. 

__REGRA \_CCUS\_NO\_CENTRO\_CUSTOS__: Verifica se o código do centro de custos “COD\_CCUS” \(Campo 03\) existe no registro I100 \(Centro de Custos\)\.

__REGRA\_VALIDACAO\_SALDO\_CONTA:__ Verifica se a soma de todos os lançamentos do tipo encerramento de conta de resultado \(“IND\_LCTO” – Campo 05 do registro I200\) para cada data \(“DT\_RES” – Campo 02 do registro I350\) e conta \(considerando se é crédito ou débito\) é igual ao valor do saldo final antes do lançamento de encerramento \(“VL\_CTA” – Campo 04 do registro I355\) para escriturações do tipo G ou R \(com o indicador de débito ou crédito invertido\)\.

__Regara de Geração do Registro:__

Quando selecionado o checkbox “Saldo Antes do Encerramento” \(SAFX169\) – No caminho:

Módulo 🡪 SPED 🡪 ECD\- Escrituração Contábil Digital

Menu 🡪 Parâmetros 🡪 Dados Iniciais

Os campos, Empresa, Estabelecimento, Data Saldo e Código da Conta da SAFX169, deverá ser igual a Empresa campo \-01, Estabelecimento campo\-02,  Data da Operação campo \-03 e Conta campo\-04 do Lançamento de Encerramento da SAFX01\. 

O sistema deverá recuperar as informações da tabela SAFX169 – Saldo Antes do Encerramento para compor o registro, ou seja, considerando cada conta e centro de custo para o qual houve movimento\.

Ex: I355 \- 0001 \- 0001A \- 1\.500,00 \- D

      I355 \- 0001 \- 0001B \- 3\.000,00 \- D

      I355 \- 0001 \- 0001C \- 4\.500,00 – D

Obs: Caso o checkbox “Saldo Antes do Encerramento” \(SAFX169\) não selecionado, seguir com a forma de geração hoje existente no sistema\.

OS4711

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

