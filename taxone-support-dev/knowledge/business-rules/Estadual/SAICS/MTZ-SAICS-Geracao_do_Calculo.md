# MTZ-SAICS-Geracao_do_Calculo

- **Fonte:** MTZ-SAICS-Geracao_do_Calculo.docx
- **Modificado:** 2024-10-21
- **Tamanho:** 38 KB

---

# 53SAICS – Geração de Cálculo

__Localização:__

__Módulo:__ Estadual > SAICS

__Menu:__ Cálculo > Geração do Cálculo

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__CH1431\_2012__

Correção na geração de cálculo para frete

Correção na geração de cálculo para frete

__CH11025\_2012__

Criação de log de erro 

Criação de log de erro

__CH14565\_2012__

Correção na geração do cálculo médio do insumo 

Correção na geração do cálculo médio do insumo, que também usará a X16 e a X17

__CH14566\_2012__

Correção na geração de cálculo considerando a conversão de unidade de medida

Correção na geração de cálculo considerando a conversão de unidade de medida

__MFS78358__

Andréa Rocha

Alteração no cálculo da ficha 3A para os movimentos de estoque relativos a uma devolução\.  Como não havia a regra de como era feito o cálculo para a ficha 3A, o cálculo foi descrito na RN06, marcando o que foi alterado para a MFS78358\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Na __Geração do Cálculo das Fichas 6A e 6B__ __NÃO__ devem ser considerados os registros da tabela X131 que tenham o campo 08 – COD\_TP\_LANCTO = ‘317776’, ‘327776’ e ‘337776’, quando:

\- Campo 03 – DATA\_MOVTO pertinente ao período de geração \(SAFX131\)\.

__Obs\.:__ As notas nas condições acima devem compor normalmente a geração do SAICS\.

__OBS\* Para correta geração dos dados o campo de IND\_ATIVO\_SAICS da X2013\_PRODUTOS tem que estar preenchida com ‘S’\.__

__CH1431\_2012__

__RN01__

Na geração do cálculo inicial, devem ser criados os seguintes logs de erro:

1. Sempre que o produto acabado estiver sem a árvore do produto, ou seja, não possuir cadastro nas tabelas X16\_PRD\_ACABADO e X17\_PROD\_INSUMO, deve apresentar a seguinte mensagem de erro:

“Não foi encontrada árvore de produto para produto \_\_\_”\.

No espaço em branco deve ser preenchido com o código do produto\.

1. Sempre que o sistema não identificar a correlação do tipo de documento para o SAICS \(Módulo: SAICS > Menu: Parâmetros > Tipo Documento x Código Chave\) no qual o campo IND\_DOCTO\_FISCAL for igual a ‘S’ \( Documento Válido Fiscalmente\) apresentar a seguinte mensagem de erro:

“Código do Tipo de Documento não localizado”\.

A geração de cálculo do SAICS \(cálculo do Saldo Inicial\) deve ser interrompida sempre que ocorrer os logs de erro acima\.

__CH11025\_2012__

__RN02__

Na geração do cálculo inicial, devem ser criados os seguintes logs de erro:

1. Sempre que não houver documento fiscal suficiente para compor o total do estoque, apresentar a seguinte mensagem de erro:

“Não foi localizada movimentação suficiente para acobertar o total em estoque do produto\.”

1. Sempre que não houver cadastro de Conversão de Unidades de Medida \( Módulo: DW > Menu: Manutenção > Cadastros > Conversão de Unidades de Medida > Por Produto\), deve ser apresentada a seguinte mensagem:

“Conversão de unidade de medida não cadastrada para o produto \_\_\_\_\_\_”\. 

No espaço em branco deve ser preenchido com o código do produto\.

A geração de cálculo do SAICS \(cálculo do Saldo Inicial\) deve ser interrompida sempre que ocorrer os logs de erro acima\.

__CH11025\_2012__

__RN03__

__Regra para considerar as tabelas X16 e X17 na geração do cálculo do custo médio:__

Na geração do cálculo do custo o sistema deve considerar as tabelas X16 e X17, conforme fórmula abaixo:

Quantidade de insumo por unidade = Campo 09 – QTD\_USADA/ Campo 07 – QTD\_FABRICADA utilizada na X17\.

__CH14565\_2012 __

__RN04__

__Regra para considerar Conversão de Unidade de Medida no cálculo do custo médio:__

Na geração do cálculo do custo médio, o sistema deve considerar o cadastro de Conversão de Unidade de Medida \(DW > Manutenção > Cadastro > Conversão de Unidade de Medida \(tabela DWT\_CONV\_MEDIDA\)\.

__CH14566\_2012__

__RN05__

__Regra para cálculo com fator de conversão de medidas:__

Na geração do cálculo do custo médio, a tabela DWT\_CONV\_MEDIDA deve considerar a fórmula abaixo:

Campo COD\_MEDIDA\_ORIGEM __MULTIPLICADA__ pelo Campo VLR\_FATOR\_CONV __=__ COD\_MEDIDA\_DEST

__CH14566\_2012__

__RN06__

__Cálculo das Fichas 3A:__

O cálculo do custo será baseado na tabela SAFX52 \(Inventário do mês anterior\), SAFX10 \(Movimentos de estoque do mês  da geração\) e SAFX131 \(Rateio de Custos do mês  da geração\)\.

Critérios da recuperação dos produtos do Movimento de Estoque \(SAFX10\) para o cálculo:

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração do cálculo; 
- Data Movimento – data enquadrada no período informado em tela;
- Somente Produtos com Indicador de Ativo SAICS igual a “S” \(campo 49 da SAFX2013\); 
- Somente Movimento em que o campo Cód\. Tipo de Lançamento ” \(campo 56 da SAFX10\) esteja cadastrado na tabela  SAICS\_TP\_LANCTO\_REG \(TFIX81\), com código de layout igual a ‘CAC001’, indicador de movimento igual a ‘S’  e o código da ficha igual a ‘3A’ ; 
- Desconsiderar os movimentos em que o campo Cód\. Tipo de Lançamento ” \(campo 56 da SAFX10\) igual a ‘773178’ ou ‘773278’;

Devem ser recuperados os campos: Produto \(campo 12 da SAFX10\), Natureza de Estoque \(campo 17 da SAFX10\) e Quantidade \(campo 20 da SAFX10\)\.  A partir dos produtos recuperados do movimento de estoque, recuperar os dados do inventário por produto referente ao mês anterior e seus movimentos de estoque de entrada, saída e devolução, e seu Rateio de Custos:

 SAFX52 \(Inventário do mês anterior\)

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração do cálculo; 
- Data Movimento – data refererente ao período anterior informado em tela;
- Natureza de estoque \(campo 17 da SAFX10\) deve ser igual a Natureza de estoque do inventário \(campo 11 da SAFX52\);
- Natureza de estoque deve estar relacionada ao código da ficha igual a ‘3A’ na tabela de Relacionamento Natureza de Estoque x Ficha \(SAICS\_NAT\_ESTOQUE\_FICHA\);

      Devem ser recuperados os seguintes campos totalizados por produto: Quantidade \(campo 13 da SAFX52\), Valor do Custo SAICS \(campo 31 da SAFX52\) e Valor do ICMS \(campo 17 da SAFX52\)\.

SAFX10 \(Movimentos de estoque de entrada\)

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração do cálculo; 
- Data Movimento – data enquadrada no período informado em tela;
- Somente Movimento em que o campo Cód\. Tipo de Lançamento ” \(campo 56 da SAFX10\) esteja cadastrado na tabela  SAICS\_TP\_LANCTO\_REG \(TFIX81\), com código de layout igual a ‘CAC001’, indicador de movimento igual a ‘__E’__  e o código da ficha igual a ‘3A’ ; 
- Somente Movimento de estoque que estejam relacionados a uma saída no mês da geração, ou seja, em que o campo Cód\. Tipo de Lançamento \(campo 56 da SAFX10\) esteja cadastrado na tabela SAICS\_TP\_LANCTO\_REG \(TFIX81\), com código de layout igual a ‘CAC001’, indicador de movimento igual a ‘__S’__  e o código da ficha igual a ‘3A’  

__MFS78358__

__RN06__

__Cálculo das Fichas 3ª \(Continuação\):__

Devem ser recuperados os seguintes campos totalizados por produto: Quantidade \(campo 13 da SAFX10\), Valor do Custo SAICS \(campo 54 da SAFX10\) e Valor do ICMS SAICS \(campo 57 da SAFX10\)\.

SAFX131 \(Rateio de Custos – SAICS\)

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração do cálculo; 
- Data Movimento – data enquadrada no período informado em tela;
- Somente Movimento em que o campo Cód\. Tipo de Lançamento ” \(campo 08 da SAFX131\) esteja cadastrado na tabela  SAICS\_TP\_LANCTO\_REG \(TFIX81\), com código de layout igual a ‘CAC001’, indicador de movimento igual a ‘__E’__  e o código da ficha igual a ‘3A’ ; 

Devem ser recuperados os seguintes campos totalizados por produto: Quantidade \(campo 14 da SAFX131\), Valor do Custo SAICS \(campo 18 da SAFX131\) e Valor do ICMS SAICS \(campo 16 da SAFX131\)\.

SAFX10 \(Movimentos de estoque de devolução\)

- Empresa – código da empresa do login; 
- Estabelecimento – código do estabelecimento selecionado para geração do cálculo; 
- Data Movimento – data enquadrada no período informado em tela;
- Somente movimento em que o campo Cód\. Tipo de Lançamento ” \(campo 56 da SAFX10\) igual a ‘773178’ \(Devolução de produto acabado\);
- Somente Movimento de estoque que estejam relacionados a uma saída no mês da geração, ou seja, em que o campo Cód\. Tipo de Lançamento ” \(campo 56 da SAFX10\) esteja cadastrado na tabela  SAICS\_TP\_LANCTO\_REG \(TFIX81\), com código de layout igual a ‘CAC001’, indicador de movimento igual a ‘__S’__  e o código da ficha igual a ‘3A’; 

Devem ser recuperados os campos totalizados por produto: Quantidade \(campo 13 da SAFX10\), Valor do Custo SAICS \(campo 54 da SAFX10\) e Valor do ICMS SAICS \(campo 57 da SAFX10\), todos com o sinal negativo, ou seja, por se tratar de devolução a quantidade e os valores devem ser multiplicados por \-1\.

Devem ser recuperados os seguintes campos totalizados por produto: Quantidade \(campo 13 da SAFX10\), Valor do Custo SAICS \(campo 54 da SAFX10\) e Valor do ICMS SAICS \(campo 57 da SAFX10\)\.

Cálculo dos valores:

Valor do Custo Total: Valor do Custo SAICS \(Inventário do mês anterior\) \+ Valor do Custo SAICS \(Movimento de entrada\) 

                               \+ Valor do Custo SAICS \(Rateio do Custo\) \+ Valor do Custo SAICS \(Movimento de devolução\) /             

                                 Quantidade \(Inventário do mês anterior\) \+ Quantidade \(Movimento de entrada\) \+ Quantidade \(Rateio         

                                 do Custo\) \+ Quantidade \(Movimento de devolução\) \+ Quantidade \(Movimento p/ o cálculo\)

__MFS78358__

__RN06__

__Cálculo das Fichas 3A \(Continuação\):__

Valor do ICMS Total: Valor ICMS \(Inventário do mês anterior\) \+ Valor ICMS SAICS \(Movimento de entrada\) 

                               \+ Valor ICMS SAICS \(Rateio do Custo\) \+ Valor ICMS SAICS \(Movimento de devolução\) /             

                                 Quantidade \(Inventário do mês anterior\) \+ Quantidade \(Movimento de entrada\) \+ Quantidade \(Rateio         

                                 do Custo\) \+ Quantidade \(Movimento de devolução\) \+ Quantidade \(Movimento p/ o cálculo\)

__Obs__\.:  Os valores calculados devem truncados em 6 casas decimais\.

Após o cálculo dos valores do custo e do ICMS referentes ao SAICS, os valores serão atualizados para cada produto na tabela de movimento de estoque \(SAFX10\) e no item de mercadoria da nota fiscal \(SAFX08\), de acordo com o parâmetro informado em tela “Não atualizar valores informados pelo usuário”\.

Se \(o parâmetro “Não atualizar valores informados pelo usuário” estiver desmarcado\) OU \(se o parâmetro “Não atualizar 

    valores informados pelo usuário” estiver marcado e o indicador de gravação SAICS \(SAFX08 ou SAFX10\) igual a 0 ou 6\)

     Os valores de custo e ICMS serão atualizados

Senão \(parâmetro marcado\)

     Os valores de custo e ICMS não serão atualizados

__MFS78358__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

