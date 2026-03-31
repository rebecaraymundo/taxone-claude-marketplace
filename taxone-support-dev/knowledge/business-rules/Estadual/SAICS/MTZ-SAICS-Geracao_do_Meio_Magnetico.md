# MTZ-SAICS-Geracao_do_Meio_Magnetico

- **Fonte:** MTZ-SAICS-Geracao_do_Meio_Magnetico.docx
- **Modificado:** 2024-10-21
- **Tamanho:** 46 KB

---

# SAICS – Geração Meio Magnético

__Localização:__

__Módulo:__ Estadual > SAICS

__Menu:__ Obrigações > Geração Meio Magnético

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__CH1431\_2012\-A__

Correção na geração do meio magnético para frete

Correção na geração do meio magnético para frete

__CH12927\_2012__

Correção na geração para operação de exportação

Correção na geração para operação de exportação

__CH20390\_2013__

Vitor Canin de Souza

Correção na geração para operação de exportação e ZFM

__MFS28328__

Andréa Rocha

Alteração na geração do registro 5335 para a geração simplificada

__MFS29368__

Jorge Neto

Alteração na geração do registro 5335 para a geração quando não utilizada Operação de Exportação

__MFS93558__

Rogério Ohashi

Alteração na geração do registro 5325 – Operações Geradoras de Crédito Acumulado – Campo 04 \- PER\_MED\_ICMS \-PMC para considera o parâmetro para Recuperação dos valores\.

MFS619349

Liliane Assaf

Inclusão dos valores dos lançamentos complementares da Apuração do ICMS no Cálculo da Alíquota Média ICMS \(RN06\)\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Regra para geração – Apuração do custo e ICMS dos produtos vendidos/ saídos \- Módulo 3 para Módulo 6:__

Apuração do custo e ICMS dos produtos __saídos para a ficha 6A__, deve se levar em consideração o preenchimento do campo 08 – COD\_TP\_LANCTO \(SAFX131\), que deve ter os seguintes valores:

317771 \(Ficha 3A\)

327771 \(Ficha 3B\)

337771 \(Ficha 3C\)

__OBS\* Para correta geração dos dados o campo de IND\_ATIVO\_SAICS da X2013\_PRODUTOS tem que estar preenchida com ‘S’\.__

__CH1431\_2012\-A__

__RN01__

__Regra para geração – Apuração do custo e ICMS dos produtos vendidos/ saídos \- Módulo 3 para Módulo 6:__

Apuração do custo e ICMS dos produtos __saídos para a ficha 6B__, deve se levar em consideração o preenchimento do campo 08 – COD\_TP\_LANCTO \(SAFX131\), que deve ter os seguintes valores:

317772 \(Ficha 3A\)

327772 \(Ficha 3B\)

337772 \(Ficha 3C\)

__CH1431\_2012\-A__

__RN02__

__Regra para geração – Apuração do custo e ICMS dos produtos vendidos/ saídos \- Módulo 3 para Módulo 6:__

Apuração do custo e ICMS dos produtos __saídos para a ficha 6C__, deve se levar em consideração o preenchimento do campo 08 – COD\_TP\_LANCTO \(SAFX131\), que deve ter os seguintes valores:

317773 \(Ficha 3A\)

327773 \(Ficha 3B\)

337773 \(Ficha 3C\)

__CH1431\_2012\-A__

__RN03__

__Regra para preenchimento da coluna 17 – Registro 5315:__

Para o preenchimento da coluna 17 Valor do Crédito – Despesas Operacionais, no Registro 5315, deve ser recuperado os valores do campo 16 – VLR\_ICMS \(SAFX131\), quando:

\- Campo 03 \- DATA\_MOVTO \(SAFX131\) for pertinente ao período de geração\.

__CH1431\_2012\-A__

__RN04__

__Regra para Geração Meio Magnético:__

 No caso de operações de exportação, com não incidência de imposto e devida comprovação ou operações ZFM, com isenção e com a devida comprovação da Internação\. \(A comprovação é identificada quando o campo COMP\_OPER = 0 dos registros de exportação e ZFM\) 

Quando o campo __Finalidade__ estiver com a opção __Remessa de arquivo com informações complementares relativas à comprovação de operações de exportações\-siscomex e ou ingresso de mercadoria – Suframa__ devidamente selecionada, a geração deverá somente gerar o arquivo do Meio Magnético com os seguintes registros que tiveram a sua comprovação, fora do período:

Registro 0000 – Abertura do Arquivo Digital e Identificação do Contribuinte \(Obrigatório\)

Registro 0001 – Abertura do Bloco 0 \(Obrigatório\)

Registro 0990 – Encerramento do Bloco 0 \(Obrigatório\)

Registro 5001 – Abertura do Bloco 5 \(Obrigatório\)

Registro 5310 – Abertura de Ficha 3A \(Informar se aplicável\)

Registro 5315 – Movimentação de Itens \(Em conjunto com o 5310\)

Registro 5325 – Operações Geradoras de Crédito Acumulado \(Em conjunto com o 5310\)

Registro 5335 – Operações Geradoras Apuradas na Ficha 6C ou 6D

Registro 5340 – Dados da Exportação Indireta Comprovada – Fichas 5H \(Informar se aplicável\)

Registro 5360 – Abertura da Ficha 3B \(Informar se aplicável\)

Registro 5365 – Movimentação de Itens \(Em conjunto com o 5360\)

Registro 5380 – Operações Geradoras de Crédito Acumulado \(Em conjunto com o 5365\)

Registro 5390 – Operações Geradoras Apuradas na Ficha 6C ou 6D \(Em conjunto com o 5380\)

Registro 5395 – Dados da Exportação Indireta Comprovada – Fichas 5H \(Informar se aplicável\)

Registro 5410 – Abertura de Ficha 3C \(Informar se aplicável\)

Registro 5415 – Movimentação de Itens \(Em conjunto com o 5410\)

Registro 5425 – Operações Geradoras de Crédito Acumulado \(Em conjunto com o 5415\)

Registro 5435 – Operações Geradoras Apuradas na Ficha 6C ou 6D \(Em conjunto com o 5425\)

Registro 5990 – Encerramento do Bloco 5 \(Obrigatório\)

Registro 9001 – Abertura do Bloco 9 \(Obrigatório\)

Registro 9900 – Registros do Arquivo \(Obrigatório\)

Registro 9990 – Encerramento do Bloco 9 \(Obrigatório\)

Para a geração desses registros, serão recuperados apenas os registros na tabela SAFX08 cujo campo tipo de lançamento seja '317773', '327773', '337773', '317774', '327774' ou '337774'\.

__CH12927\_2012__

__CH20390\_2013__

__RN05__

__Registro 5335 \- Operações Geradoras Apuradas na Ficha 6C ou 6D__

Origem dos dados:

\- SAFX48

\- SAFX103

    Primeiro verifica se há informações na SAFX48, a partir dos dados da nota fiscal de saída \(SAFX08\): empresa, estabelecimento, data fiscal, número do documento fiscal, série, pessoa física/jurídica e produto\.

    Se não houver informação na SAFX48, deve\-se recuperar os dados da SAFX103, a partir dos dados da nota fiscal de saída \(SAFX08\): empresa, estabelecimento, data fiscal, número do documento fiscal, série, pessoa física/jurídica e produto\.

Quando não houver dados nas tabelas acima e o registro estiver marcado para a geração simplificada \- Versão 1\.0\.0\.1 \(Verificar o leiaute selecionado para a geração\)

    O registro deve ser gerado com:

        \- Campo 2 – NUM\_DECL\_EXP = Nulo \(sem preenchimento\) , exceto quando de utilização da ficha 6C \(cod tipo do lançamento, campo 185 safx08,  317773, 327773 e 327773\) o campo 2 – NUM\_DECL\_EXP deverá ser preenchido como INDIRETA

        \- Campo 3 – COMP\_OPER = 1 \(Não\)

__Obs\.: __O campo COMP\_OPER será preenchido com “1” quando ocorrer a saída do estabelecimento, mas ainda não foi emitido o Comprovante de Exportação, ou seja, os dados ainda não foram carregados para as tabelas SAFX48 e SAFX103\.

__MFS28328__

__MFS29368__

__RN06__

__Registro 5325 – Operações Geradoras de Crédito Acumulado – Campo 04 \- PER\_MED\_ICMS \-PMC__

MFS93558: Criação da opção “Recuperação dos valores” na Parametrização do CFOP p/ Cálculo da Alíquota Média ICMS \(Base Cálculo\)

MFS619349: Inclusão dos valores dos lançamentos complementares da Apuração do ICMS no Cálculo da Alíquota Média ICMS\.

Cálculo para Método Simplificado \(CAT207/09\)

O Cálculo da Alíquota Média para preenchimento do Registro 5325 para o Campo 04 \- PER\_MED\_ICMS, segue a fórmula:

Alíquota Média ICMS = Somatório do Vlr do Imposto / Somatório do Valor das Bases \* 100

Onde:

- Vlr do Imposto = Valor do ICMS das Entradas das notas fiscais 

                                  \(–\) Valor do ICMS das Saídas das notas fiscais

                            \(\+\) Valor dos Lançamentos da Apuração ICMS à Crédito 

                            \(\-\) Valor dos Lançamentos da Apuração ICMS à Débito

Critérios de Recuperação das Notas Fiscais \(DWT\_DOCTO\_FISCAL/DWT\_ITENS\_MERC\): 

- 
	- estabelecimento selecionado na tela
	- data fiscal compreendida no período formado pela Data Inicial e Final
	- CFOP pertencente à Parametrização do CFOP p/ Cálculo da Alíquota Média ICMS \(Imposto\)

Critérios de Recuperação dos Lançamentos Complementares da Apuração do ICMS \(ITEM\_APURAC\_DISCR\):

- 
	- estabelecimento selecionado na tela
	- Data da Apuração compreendido no Mês/Ano Competência informado na tela
	- Código de Ajuste \(Sped Fiscal\) pertencente à Parametrização do Ajuste da Apuração p/ Cálculo da Alíquota Média ICMS
	- Operação da Apuração = 002 \(Outros Débitos\), 003 \(Estorno de Créditos\), 

                                      006 \(Outros Créditos\), 007 \(Estorno de Débitos\),

                                      012 \(Deduções\)

Sendo que o valor dos Lançamentos das operações 006, 007 e 012, compõe o Valor dos Lançamentos da Apuração ICMS à Crédito, na fórmula do Vlr do Imposto\. E os Lançamentos das operações 002 e 003 compõe o Valor dos Lançamentos da Apuração ICMS à Débito\.

Os Lançamentos Complementares da Apuração do ICMS estão disponíveis no módulo Estadual >> ICMS, menu Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS >> Ajuste SINIEF

- Vlr das Bases = Valor da Base ICMS das Entradas das notas fiscais 

                       \(\-\) Valor da Base ICMS das Saídas das notas fiscais

Critérios de Recuperação das Notas Fiscais \(DWT\_DOCTO\_FISCAL/DWT\_ITENS\_MERC\): 

- 
	- estabelecimento selecionado na tela
	- data fiscal compreendida no período formado pela Data Inicial e Final
	- CFOP pertencente à Parametrização do CFOP p/ Cálculo da Alíquota Média ICMS \(Base Cálculo\)
		- Na parametrização do CFOP, verificar a opção selecionada para Recuperação dos valores, onde:

1 – Base de Cálculo ICMS: Recuperar a informação do Campo VLR\_BASE\_ICMS\_1 da Tabela DWT\_ITENS\_MERC, para considerar na fórmula como Valor da Base ICMS das Entradas e Saídas\.

2 – Valor Contábil: Recuperar a informação do Campo VLR\_CONTAB\_ITEM da Tabela DWT\_ITENS\_MERC, para considerar na fórmula como Valor da Base ICMS das Entradas e Saídas;

__MFS93558__

__MFS619349__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

