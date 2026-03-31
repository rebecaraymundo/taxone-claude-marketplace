# MTZ-GIA_MG-Anexos

- **Fonte:** MTZ-GIA_MG-Anexos.docx
- **Modificado:** 2023-02-01
- **Tamanho:** 37 KB

---

# Módulo – Manutenção Anexos

__Módulo:__ Estadual – GIA\-MG

__Menu__: Obrigações \-> DAPI \-> Manutenção \-> Anexos 

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__CH96365__

DW \- ESTADUAL \- DAPI\-MG \- Alterar geração da Linha 86 para que não constem valores de Devoluções\.

Ajustar o campo 86 da DAPI\-MG, pois segundo legislação, este campo deve contemplar os valores de entrada, excluindo os valores de devolução, pois o mesmo encontra\-se gerado no campo 80\.

__OS3706__

Atualização do Layout da DAPI – versão 7\.03\.00

Inclusão de itens no detalhamento Tipo 90 do campo “Estorno de Débitos” relativos à atividade de Comunicação e criação de campos do FEM\.

__OS4576__

Atualizaçãoes da Vrs 8\.00\.00

Inclusão do novo campo 104\.1 – Recolhimento Efetivo \(ver __RN05__ e __RN06__\)

__MFS7299__

Atualizações da Vrs 8\.02\.00

Atualizações da nova versão 8\.02: 

\(ver __RN01__ , __RN02__ , __RN03__ , __RN04__ e __RN05 __para alterações do Anexo VII\)

\(ver __RN11__ e __RN12 __para alterações do Anexo VI\)

\(ver __RN13 __para alterações do Anexo VIII\)

\(ver __RN07__ e __RN07\-A __para alterações do Anexo IX\)

__CH22608\_2016__

Alteração no preenchimento do campo “Imposto s/ aproveitamento de crédito” das Operações/ Prestações

Este documento tem como objetivo alterar o preenchimento do campo “Imposto s/ aproveitamento de crédito” das Operações/ Prestações dos Anexos\.

__MFS27892__

Atualizações da Vrs 9\.01\.00

Exclusão dos campos 71\.1\.e 74\.1 do Anexo VI\.

__MFS38330__

Atualização Legal – versão 9\.03\.00

Na vrs 9\.03\.00, a partir de 05/2020, os campos 115 e 116 foram retirados do layout \(ver __RN15__\)

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

A linha 86 – Valor Retido – Entradas da DAPI –MG deve ser gerada somente com os valores de entrada, devendo ser excluído os valores gerados na linha 80 – Devoluções\.

CH96365

__RN01__

###### Aba ICMS – Subst\. Tributário \(Anexo VII\), campo “77\.1 – Outros Débitos de ST”

Alteração da __MFS7299__ – Campo criado p/a versão 8\.02

Características: campo numérico \(tamanho 17,2\), *não* obrigatório\.

Obs: Na geração dos registros este campo é gerado a partir dos lançamentos complementares da apuração do ICMS\-ST de classe = 980, e como os demais campos da DAPI, ficará habilitado para manutenção do usuário\.

__MFS7299__

__RN02__

###### Aba ICMS – Subst\. Tributário \(Anexo VII\), campo “81 – Saldo Credor – ST Per\. Seguinte”

Alteração da __MFS7299__ \(alterada a totalização deste campo para incluir os novos campos 77\.1 e 82\.1\)

A cada inclusão/alteração deste quadro \(Anexo VII\), os campos 81 e 82 serão calculados da seguinte forma:

                         \[   \(campo 77 \+ campo 77\.1\)    –   \(campo 78 \+ campo 79 \+ campo 80 \+ campo 82\.1\)   \]

Dependendo do resultado obtido, o valor será carregado para o campo 81 ou 82, da seguinte forma:

Se resultado > 0

     O campo 81 será preenchido com zeros;

     O resultado será carregado p/o campo “82\-ICMS\-ST a Recolher”; 

Se resultado < 0

     O resultado será carregado p/o campo “81\-Saldo Credor \- ST Per\. Seguinte”;

     O campo 82 será preenchido com zeros;

Obs: Regra definida a partir das orientações de preenchimento do programa DAPI vrs\. 8\.02 \(menu Ajuda > Sistema > Instruções de Preenchimento > Modelo 1 > Fichas > ICMS Subst\. Tributária\)\.

__MFS7299__

__RN03__

###### Aba ICMS – Subst\. Tributário \(Anexo VII\), campo “82 – ICMS\-ST a Recolher”:

Alteração da __MFS7299__ \(alterada a totalização deste campo para incluir os novos campos 77\.1 e 82\.1\)

\(ver __RN02__\)

__MFS7299__

__RN04__

###### Aba ICMS – Subst\. Tributário \(Anexo VII\), campo “82\.1 – Estorno Devido ao FEM”

Alteração da __MFS7299__ – Campo criado na MFS7299 p/a versão 8\.02

Características: campo numérico \(tamanho 17,2\), *não* obrigatório\.

Obs: Este campo não é tratado na geração dos registros\. Portanto, será sempre inserido via manutenção, quando for o caso\.

__MFS7299__

__RN05__

###### Aba ICMS – Subst\. Tributário \(Anexo VII\), campo “82\.1 – Fundo de Erradicação da Miséria – FEM”

__Aba ICMS – Subst\. Tributário \(Anexo VII\), campo “82\.2 – Fundo de Errad\. da Miséria a recolher”__

Alteração da __MFS7299__ \- Este campo foi renumerado para 82\.2 na versão 8\.02 \(originalmente, era o campo 82\.1\), e sua descrição foi alterada conforme conteúdo acima\.

Obs: Este campo não é tratado na geração dos registros\. Portanto, será sempre inserido via manutenção, quando for o caso\.

Ao salvar a operação, sempre que existir informação neste campo, o valor digitado será carregado também para o campo “*105\.1\-Total do FEM Subst\. Tributário*” da aba “*Obrigações*” \(Anexo IX\-Obrigações do Período\)\.

__OS3706__

__RN06__

###### Geração do Anexo VIII – Apuração \- Campo 090\.1 – Estorno FEM

Trazer fixo o valor gerado através da RN03 do documento matriz “MTZ \- DAPI\-MG \- Geração dos Registros\.doc”\.

Este campo deverá estar habilitado para digitação\. Se for algum valor, considerar este na geração do arquivo\.

__OS3706__

__RN07__

###### Anexo IX – Obrigações \- Campo 105\.1 – Total do FEM Subst\. Tributário

Alteração da __MFS7299__ \- Este campo foi renomeado de “105\.1\-Total do FEM” p/ “105\.1\-Total do FEM Subst\. Tributário”;

Quando o período de referência for anterior à 09/2016:      Alteração da __MFS7299__     

     Deverá trazer o somatório do __Campo 082\.1 \(RN04\) 082\.2 \(RN05\) __\+ __Campo 090\.1 \(RN06\)\. __Este campo deverá estar

     bloqueado para digitação\.

Para períodos a partir de 09/2016:

     Este campo será preenchido com a informação do campo “82\.2\-Fundo de Erradicação da Miséria” da aba “ICMS Subst\.

     Tributario” \(Anexo VII\), e permanecerá bloqueado para manutenção do usuário, já que seu preenchimento é automático\.

__OS3706__

__MFS7299__

__RN07\-A__

###### Anexo IX – Obrigações \- Campo 105\.2 – Total do FEM Op\. Própria        \(campo incluído pela MFS7299\)

Campo “105\.2\-Total do FEM Op\. Própria” 

Características: campo numérico \(tamanho 17,2\)

Este campo será preenchido com a informação do campo “98\.1\-Fundo de Errad\. da Miséria a Recolher” da aba “Apuração” \(Anexo VIII\), e permanecerá sempre desabilitado para manutenção do usuário, já que seu preenchimento é automático\.

 

__MFS7299__

__RN08__

###### Geração do Anexo IX – Obrigações \- Campo 110\.1 – Total do FEM Antecipado

Trazer fixo o valor gerado através da RN05 do documento matriz “MTZ \- DAPI\-MG \- Geração dos Registros\.doc”\.

Este campo deverá estar habilitado para digitação\. Se for algum valor, considerar este na geração do arquivo\.

__OS3706__

__RN09__

###### Aba Obrigações \(Anexo IX – Obrigações do Período\), campo 104\.1 – Recolhimento Efetivo

\(campo incluído pela __OS4576__\)

Campo “104\.1 – Recolhimento Efetivo” 

Características: campo numérico \(tamanho 17,2\), *não* obrigatório\.

A informação deste campo compõe o total do campo 105\-Total\.

__   OS4576__

__RN10__

###### Aba Obrigações \(Anexo IX – Obrigações do Período\), campo 105 – Total 

Alteração da OS4576 \(incluído o campo 104\.1 na totalização do campo 105\)

Este é um campo calculado a partir da totalização dos campos 99 ao 104\.1\. 

__   OS4576__

__RN11__

###### Aba Outros Créditos/Débitos \(Anexo VI\), campo 71\.1\-Crédito Difal Origem \(EC 87/15\)

\(campo incluído pela __MFS7299__\)

Campo “71\.1 – Crédito Difal Origem \(EC 87/2015\)” 

Características: campo numérico \(tamanho 17,2\), *não* obrigatório\.

A informação deste campo compõe o total do campo 72\-Total\.

Este campo não será mais gerado a partir de 05/2019\.

__MFS7299__

__MFS27892__

__RN12__

###### Aba Outros Créditos/Débitos \(Anexo VI\), campo 74\.1\-Débito Difal Origem \(EC 87/15\)

\(campo incluído pela __MFS7299__\)

Campo “74\.1 – Débito Difal Origem \(EC 87/2015\)” 

Características: campo numérico \(tamanho 17,2\), *não* obrigatório\.

###### A informação deste campo compõe o total do campo 75\-Total\.

Este campo não será mais gerado a partir de 05/2019\.

__MFS7299__

__MFS27892__

__RN13__

###### Aba Apuração \(Anexo VIII\), campo “98\.1 – Fundo de Errad\. da Miséria a Recolher”

Alteração da __MFS7299__ – Campo criado p/a versão 8\.02

Campo: “98\.1 – Fundo de Errad\. da Miséria a Recolher”

Características: campo numérico \(tamanho 17,2\), *não* obrigatório\.

Ao salvar a operação, sempre que existir informação neste campo, o valor digitado será carregado também para o campo “*105\.2\-Total FEM Op\. Própria*” da aba “*Obrigações*” \(Anexo IX\-Obrigações do Período\)\.

__MFS7299__

__RN14__

###### Aba Operações/ Prestações \(Anexo IV\), campo “Imposto s/ aproveitamento de crédito”

__\[ALTERADA – CH22608\_2016\]__

Campo “Imposto s/ aproveitamento de crédito”

Características: campo numérico \(tamanho 17,2\), *não* obrigatório\.

###### A informação deste campo deverá ser fixo zero, pois a DAPI não está mais considerando o seu preenchimento em nenhuma das colunas da linha 10 é composta pela totalização do campo ICMS n/Escrit \(campo 80\) da nota fiscal de entrada \(SAFX08\) e permanecerá sempre desabilitado, já que seu preenchimento é era automático\.

__CH22608\_2016__

__RN15__

###### Anexo XI – Informações Econômicas \(Aba Inform\. Econômicas\)

Quando o período de referência \(Anexo I, aba Identificação\)  for igual ou superior à __05/2020__, os seguintes campos ficarão desabilitados:

\- Campo “115\-Número de Empregados no Último Dia do Período”

\- Campo “116\-Valor da Folha de Pagamento”

######  

__MFS38330__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

*CAMPO 80\- Devolução  
Valor do ICMS retido por substituição tributária em devolução ou retorno de mercadoria que não tenha sido entregue ao destinatário e que foram escrituradas nos termos do artigo 25 do RICMS\. Informar os valores acumulados no período de referência, que serão extraídos do livro Registrode Apuração do ICMS, nas folhas subseqüentes reservadas à informação de ST interna, no campo "Por Entradas com Crédito do Imposto"\.  
*

*CAMPO 86\- Valor Retido  
Valor do ICMS devido pelo contribuinte, na entrada da mercadoria ou serviço, na condição de substituto tributário\. Os valores serão extraídos da coluna "Observações" do livro Registro de Entradas\.*”\.

