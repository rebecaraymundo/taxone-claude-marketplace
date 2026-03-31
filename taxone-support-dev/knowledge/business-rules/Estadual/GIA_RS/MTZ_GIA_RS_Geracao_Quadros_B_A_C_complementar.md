# MTZ_GIA_RS_Geracao_Quadros_B_A_C_complementar

- **Fonte:** MTZ_GIA_RS_Geracao_Quadros_B_A_C_complementar.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 66 KB

---

THOMSON REUTERS

GIA\-RS

Geração – Quadros B e A/C \(complementar\)

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

OS4636

Julyana Perrucini

<a id="OLE_LINK65"></a><a id="OLE_LINK66"></a><a id="OLE_LINK67"></a><a id="OLE_LINK118"></a><a id="OLE_LINK119"></a><a id="OLE_LINK120"></a>Alteração da rotina para geração automática do Quadro B\.

CH7408\_2016

Eric Celestrino

Alteração da regra para gerar o campo SALDO CREDOR do Quadro B

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__OS/CH__

RN00

__Regra Geral:__

Quadro B

Origem: tabela est\_res\_cfo\_uf\_01 \(Resumo das Operações por UF/CFOP – Entradas e Resumo das Operações por UF/CFOP – Saídas do Módulo Estadual >> Obrigações Acessórias >> Relatórios >> Resumo das Operações\)\.

OS4636

RN01

__Apuração ICMS no Mês de Referência – Campo ICMS Próprio:__

Permite calcular o valor o ICMS próprio para período de apuração preenchido na tela de geração\.

__ALTERADA – OS4636\]__

__Tratamento:__

O sistema faz a seguinte operação para o lançamento do ICMS próprio via rotina:

1. Valor do campo "Valor Total \(saídas\)" do quadro A \( \- \) Valor total do campo "Valor ICMS vencido" do Anexo IX \( \- \) Valor do campo " Valor Total \(entradas\) " do quadro A \( \- \) Valor total do campo "Valor Pagto\. ICMS" do Anexo VIII \( \- \) Valor do campo "Valor Saldo Credor Anterior" do quadro B \( \- \) Valor do campo "Valor Atualização Monetária" do quadro B \+ Valor do campo "Valor Crédito não Compensável" do quadro B = Resultado da operação;
2. Se a operação resultar em débito a recolher \(valor positivo\), este resultado será o valor deste campo;
3. Se a operação resultar em saldo credor \(valor negativo\), informar neste campo zero, devendo o resultado da operação ser registrado no campo "Valor Saldo ICMS transportar", desconsiderando\-se o sinal negativo;
4. Se cair na condição do item 2, somar ainda ao campo ICMS próprio o valor de outros débitos do Anexo XV quando o campo código de outros débitos \(Amparo/Texto/Ocorrência da manutenção do Anexo XV\) for igual a “8006”;
5. Se cair na condição do item 3, mesmo se houver valor para o Anexo XV com código de outros débitos igual a “8006”, não somar o valor\.

OS4636

RN02

__Transporte de valores de períodos anteriores – Campo Saldo Credor:__

__\[ALTERADA – CH7408\_2016\]__

O sistema preenche o campo __Saldo Credor__ das seguintes formas:

1. Manualmente preenchido diretamente no campo __Saldo Credor\.__
2. Existindo geração do Quadro b – Apuração de ICMS no período anterior, deve carregar o somatório dos campos __Créditos não Compensáveis, Saldo Credor de Substituição Tributaria e Saldo Credor a transportar \(Tela de Manutenção do Quadro B\-  APURACAO DO ICMS\);__
3. Automaticamente somando os itens 014 da apuração de ICMS \(Ajuste Sinief ou Empresas c/ Inscricao Estadual Única\) e 014 da apuração de ICMS por substituição tributária \(Ajuste Sinief ou Empresas c/ Inscricao Estadual Única\), desconsiderando o procedimento 2;

CH7408\_2016

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

