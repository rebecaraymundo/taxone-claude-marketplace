# MTZ_Tela APURACAO_COFINS

- **Fonte:** MTZ_Tela APURACAO_COFINS.docx
- **Modificado:** 2024-04-17
- **Tamanho:** 41 KB

---

    

# \(EFD\-PIS/PASEP – COFINS\) – Apuração – COFINS

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

__Data Alteração__

OS3169\-GE28

Alteração na tela Apuração – COFINS

Incluir na tela de Apuração \(COFINS\) os campos Valor Limite da Contribuição Cumulativa e Não Cumulativa a Descontar e Criar a  Pasta de Retenção na Fonte\.

14/12/2011

OS4584

Upload do registro M605 

Inclusão na tela a funcionalidade upload para importação do XML compondo o registro M605\.

24/10/2014

MFS\-803

Alteração na tela Apuração – COFINS

Atualização da tela de apuração para o cenário de método de apropriação de créditos “Apropriação Direta”\.

20/09/2015

MFS\-4144

Alteração na tela Apuração – COFINS

Atualização da tela de apuração para o cenário de método de apropriação de créditos “Rateio Proporcional \(Receita Bruta\)”\.

10/10/2016

MFS\-628939

Alessandra Cristina Navatta

Inclusão de mensagem ao abrir a tela, sugerindo a utilização da tela única de Apuração PIS/COFINS, apenas no produto TAXONE\. \(RN13\)

17/04/2024

## REGRAS DE NEGÓCIO

#### Cód\.

### DR

__RN00__

Inclusão dos campos de visualização dos limites: 

\- Valor Limite da Contribuição Cumulativa a Descontar = Valor da Contribuição Cumulativa a Recolher/Pagar\.

\- Valor Limite da Contribuição Não Cumulativa a Descontar = Valor da Contribuição Não Cumulativa a Recolher/Pagar\.

OS3169\-GE28

__RN01__

Na Pasta de Ajustes do Crédito da COFINS Apurado – M500 → \(aba “Crédito da COFINS no Período – M500”\)

Se o parâmetro ‘’Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS’’ estiver marcado na tela de Dados Iniciais, na tela de manutenção do registro M500 o campo ‘’Valor do Crédito Disponível, descontado da contribuição apurada no próprio período’’ deve ficar habilitado para a manutenção \(alteração\)\. 

Para os demais campos o sistema não deve permitir alteração\.

OS3169\-GE28

__RN02__

Se o campo “Valor do Crédito disponível, descontado da contribuição apurada no próprio período” for alterado pelo usuário:

Se o “Valor do Crédito disponível, descontado da contribuição apurada no próprio período” for maior que o “Valor Total do Crédito Disponível Relativo ao Período”, dar a seguinte mensagem: 

Valor do Crédito descontado da contribuição superou o valor do Crédito Disponível\. 

Se o registro estiver consistente, então atualizar o saldo e o indicador, onde: 

\- “Saldo de Créditos a Utilizar e Períodos Futuros”:

“Saldo de Créditos a Utilizar e Períodos Futuros” = “Valor Total do Crédito Disponível Relativo ao Período”   –   “Valor do Crédito disponível, descontado da contribuição apurada no próprio período” 

\- “Utilização do Credito disponível”:

Se “Saldo de Créditos a Utilizar e Períodos Futuros” = 0 então: “Utilização do Credito disponível” = ‘0’

Senão “Utilização do Credito disponível” = ‘1’

OS3169\-GE28

__RN03__

Criar uma nova tela de manutenção das Retenções na Fonte Apuradas no Período

  
__Localização:__ Sped → EFD – Escrituração Fiscal Digital \- PIS/PASEP\-COFINS \- __Menu:__ Obrigações → Manutenção → Apuração COFINS → Pasta Retenção na Fonte COFINS Apurada no Período\.

OS3169\-GE28

__RN04__

__A tela terá os seguintes campos e definições:	  
__

__\- Natureza da Retenção na Fonte: __

Campo COD\_RET\_FONTE da tabela EPC\_REG\_TOT\_RET\_F600\.

Lista de possíveis códigos\. Apresentar códigos – descrições:

01 \- Retenção por Órgãos, Autarquias e Fundações Federais;

02 \- Retenção por outras Entidades da Administração Pública Federal;

03 \- Retenção por Pessoas Jurídicas de Direito Privado;

04 \- Recolhimento por Sociedade Cooperativa;

05 \- Retenção por Fabricante de Máquinas e Veículos; 

99 \- Outras Retenções

__\- Natureza da Receita:__

Campo IND\_NAT\_REC da tabela EPC\_REG\_TOT\_RET\_F600\.

Lista de possíveis códigos\. Apresentar códigos – descrições:

1. Receita de Natureza Não Cumulativa;

      1\- Receita de Natureza Cumulativa\.

__\- Condição da Pessoa Jurídica Declarante:__

Campo IND\_COND\_PJ\_DECL da tabela EPC\_REG\_TOT\_RET\_F600\.

Lista de possíveis códigos\. Apresentar códigos – descrições:

1. Beneficiária da Retenção / Recolhimento 

      1\- Responsável pela Retenção / Recolhimento

__\- Retenção Apurada__

Campo VLR\_RET\_APUR da tabela EPC\_REG\_TOT\_RET\_F600\.

__\- Retenção Deduzida da Contribuição__

Campo VLR\_RET\_UTIL\_DED da tabela EPC\_REG\_TOT\_RET\_F600\.

__\- Retenção Disponível__

Campo VLR\_RET\_DISP da tabela EPC\_REG\_TOT\_RET\_F600\.

OS3169\-GE28

__RN05__

Ao clicar 2 vezes no registro, a tela de manutenção do registro será disponibilizada\.

Tela nos mesmos moldes da manutenção do M500, M510\.\.\. 

OS3169\-GE28

__RN06__

Se o parâmetro ‘’Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS’’ estiver marcado na tela dados iniciais, habilitar campo “__Retenção Deduzida da Contribuição__”\.

OS3169\-GE28

__RN07__

Ao clicar no botão confirma, se houver valor na “Retenção Deduzida da Contribuição”, então criticar o valor digitado e atualizar os campos abaixo:

Se o campo “Condição da Pessoa Jurídica Declarante” \(campo IND\_COND\_PJ\_DECL\) estiver preenchido com ‘__1__’, o registro não poderá ser alterado\. 

Gerar a seguinte mensagem:

Retenção na Fonte não pode ser utilizada pois a Condição da Pessoa Jurídica Declarante é 1 \- Responsável pela Retenção/Recolhimento\.

Se o valor da “__Retenção Deduzida da Contribuição__” __>__  que o valor da “__Retenção Apurada__”, dar a seguinte mensagem: 

Valor da  Retenção Deduzida da Contribuição superou o valor da Retenção Apurada\.

Se o registro estiver consistente, então atualizar a “__Retenção Disponível__”\.

“__Retenção Disponível__”  = “__Retenção Apurada__” \- “__Retenção Deduzida da Contribuição__”

OS3169\-GE28

__RN08__

Ao clicar no botão salvar da janela principal, as retenções alteradas devem ser gravadas 

OS3169\-GE28

__RN09__

Manter as críticas do recálculo, incluindo os valores negativos de contribuição, caso o valor informado pelo usuário tenha superado o valor limite\.

OS3169\-GE28

__RN10__

Criação da funcionalidade \(botão\) “Upload”,  para importação do arquivo XML que irá compor o registro M605\.

OS4584

__RN11__

Atualizar a tela de “Detalhamento da Base de Cálculo do Crédito – M505” \(Localização: Sped → EFD – Escrituração Fiscal Digital \- PIS/PASEP\-COFINS \- Menu: Obrigações → Manutenção → Apuração COFINS → Pasta Crédito de COFINS no Período – M500, aba Detalhamento da Base de Cálculo do Crédito – M505\), considerando as seguintes condições:

__\[ALTERADA – MFS\-4144\]__

Se na parametrização da tela de Dados Iniciais \(Menu Parâmetros → Dados Iniciais\) do estabelecimento da apuração o campo Incidência Tributária no Período estiver preenchido com a opção “3 – Escrituração de operações com incidência no regime não cumulativo e cumulativo” __E__ o campo Método de Apropriação de Créditos Comuns Comuns estiver preenchido com a opção “1 – Metodo de Apropriação Direta” ou “2 – Metodo de Rateio Proporcional \(Receita Bruta\)” __E__ o parâmetro “Informar os Descontos/Deduções manualmente, nas telas de Apuração PIS/PASEP e COFINS” estiver selecionado \(as três regras devem ser verdadeiras\), na tela de detalhe “Detalhamento da Base de Cálculo do Crédito – M505”, devemos ter as seguintes alterações:

- Campo “Base de Cálculo – Cumulativa”: este campo deve ser habilitado para edição\. O usuário poderá indicar o valor da BC Cumulativa e este valor deve ser menor ou igual ao valor apurado pelo sistema para o campo “Valor Total da Base Cálculo”\. Caso o usuário informe um valor maior, retornar a mensagem: “Valor da Base de Cálculo Cumulativa não deve ser maior que o Valor Total da Base Cálculo” e não permitir a gravação da informação\.
- Campo “Base de Cálculo – Não\-Cumulativa”: este campo deve ser atualizado dinamicamente quando o valor do campo “Base de Cálculo – Cumulativa” for alterado\. Ele será resultado do cálculo: Valor Total da Base de Cálculo __menos__ Base de Cálculo – Cumulativa\.
- Campo “Valor da Base de Cálculo do Crédito, vinculada ao tipo de crédito escriturado”: este campo deve ser atualizado dinamicamente quando o valor do campo “Base de Cálculo – Não\-Cumulativa” for alterado, considerando a seguinte regra:

Se o conteúdo do campo “CST” for igual a “50”, “51”, “52”, “60”, “61” ou “62” o conteúdo deste campo será igual ao valor apurado para o campo “Base de Cálculo – Não\-Cumulativa” e __não deve__ ser permitida a sua edição\.

Se o conteúdo do campo “CST” for igual a “53”, “54”, “55”, “56”, “63”, “64”, “65” ou “66” o conteúdo deste campo será igual ao valor apurado para o campo “Base de Cálculo – Não\-Cumulativa” e __deve__ ser permitida a sua edição, sendo que o valor aqui informado deve ser menor ou igual ao valor apurado para o campo “Base de Cálculo – Não\-Cumulativa”\. Se for maior, retornar a mensagem: “Valor da Base de Cálculo do Crédito, vinculada ao tipo de crédito escriturado não deve ser maior que o valor da Base de Cálculo – Não\-Cumulativa” e não permitir a gravação da informação\.

MFS\-803

MFS\-4144

__RN12__

Atualizar os valores da tela de “Crédito de PIS/PASEP no Período – M500” \(Localização: Sped → EFD – Escrituração Fiscal Digital \- PIS/PASEP\-COFINS \- Menu: Obrigações → Manutenção → Apuração COFINS → Pasta Crédito de COFINS no Período – M500\), considerando as alterações realizadas na aba “Detalhamento da Base de Cálculo do Crédito – M505”, conforme definições descritas na RN11\.

No momento que o usuário clicar no botão “Confirmar” da aba “Detalhamento da Base de Cálculo do Crédito – M505” e tendo alterado valores na referida tela, estas alterações irão refletir nos valores apurados para a tela “Crédito da COFINS no Período – M500” que é pai dos registros M505\. Este reflexo se dá no conteúdo dos campos:

- Campo “Valor da Base de Cálculo do Crédito”: este campo deve ser atualizado com o resultado da somatória do valor do campo “Valor da Base de Cálculo do Crédito, vinculada ao tipo de crédito escriturado” de todos os registros da aba “Detalhamento da Base de Cálculo do Crédito – M505” associados ao registro M500\. Observar que este recálculo é necessário porque os valores foram alterados na tela de “Detalhamento da Base de Cálculo do Crédito – M505” e esta coluna é o total informado nestes registros filhos\.
- Campo “Valor Total do Crédito Apurado no Período”: uma vez que o conteúdo do campo “Valor da Base de Cálculo do Crédito” foi atualizado, o valor demonstrado neste campo também é impactado, de modo que ele deve ser recalculado para refletir o resultado do cálculo: Valor da Base de Cálculo do Crédito __vezes__ \(Alíquota do COFINS __dividido__ por 100\)\.
- Campo “Valor Total do Crédito Disponível Relativo ao Período”: uma vez que o conteúdo do campo “Valor Total do Crédito Apurado no Período” foi atualizado, o valor demonstrado neste campo também é impactado, de modo que ele deve ser recalculado para refletir o resultado do cálculo: Valor Total do Crédito Apurado no Período __mais__ Valor Total dos Ajustes de Acréscimo __menos__ Valor Total dos Ajustes de Redução __menos__ Valor Total do Crédito Diferido no Período\.

Observar que existem mensagens padrão para os casos em que os ajustes lançados \(campos Valor Total dos Ajustes de Acréscimo,__ __Valor Total dos Ajustes de Redução e__ __Valor Total do Crédito Diferido no Período\) repercutem em um resultado negativo no campo Valor Total do Crédito Disponível Relativo ao Período\. Estas mensagens devem ser mantidas, bem como o tratamento que bloqueia a gravação de valores negativos para esta coluna\.

- Campo “Saldo de Créditos a Utilizar em Períodos Futuros”: uma vez que o conteúdo do campo “Valor Total do Crédito Disponível Relativo ao Período” foi atualizado, o valor demonstrado neste campo também é impactado\. Deve ser verificada na RN02 a regra de cálculo deste campo e seus tratamentos, para manter a coerência dos valores\.

MFS\-803

__RN13__

Ao clicar na tela,apenas no produto TAXONE,  exibir a mensagem orientativa para o usuário:

“Liberamos uma tela única, para a realização da apuração e dos respectivos ajustes de PIS/PASEP e COFINS\. Utilize\-a para agilizar suas atividades e conferências\! A nova tela, está disponível no Menu: Obrigações > Manutenção> Apuração Geral PIS/COFINS\.”

MFS\-628939

