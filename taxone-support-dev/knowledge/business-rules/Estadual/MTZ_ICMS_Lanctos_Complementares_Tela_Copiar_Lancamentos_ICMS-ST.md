# MTZ_ICMS_Lanctos_Complementares_Tela_Copiar_Lançamentos_ICMS-ST

> Fonte: MTZ_ICMS_Lanctos_Complementares_Tela_Copiar_Lançamentos_ICMS-ST.docx






THOMSON REUTERS

Módulo ICMS
Menu: Apuração >> Apuração do ICMS >> Lançamentos Complementares ICMS-ST
Tela botão Copiar Lançamentos




DOCUMENTO DE REQUISITO



Sumário

1.	Regras dos Campos	3
2.	Layout de Tela	5


## Regras dos Campos


Localização da tela: Menu: Apuração >> Apuração do ICMS >> Lançamentos Complementares >> Apuração ICMS Subst Tributária >> Botão Copiar Lançamentos

Título da tela: Copiar Lançamentos

Considerações Gerais:

Poderão ser parametrizado “N” (vários) códigos nessa parametrização.








## Layout de Tela





| MFS/CH | Nome | Descrição |
| --- | --- | --- |
| MFS1943 | Criação do documento | Tela botão Copiar Lançamentos |


| Campo | Tipo | Tipo | Obrig | Ed | Formato/Default | Regra | MFS/CH |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Período | Data | Data | S | S | Default: Habilitado | Este campo é de preenchimento obrigatório deverá ser informado o mês e ano para que o sistema possa recuperar os dados de acordo com o período informado. | MFS1943 |
| Caixa de seleção dos Lançamentos * | Caixa de seleção dos Lançamentos * | Caixa de seleção dos Lançamentos * | Caixa de seleção dos Lançamentos * | Caixa de seleção dos Lançamentos * | Caixa de seleção dos Lançamentos * | Caixa de seleção dos Lançamentos * | Caixa de seleção dos Lançamentos * |
| Checkbox para seleção dos Lançamentos * | Checkbox para seleção dos Lançamentos * | Checkbox | S | S | Default: todos selecionados | Nesse campo serão listados todos os lançamentos efetuados dentro do período informado no campo Período e que corresponda ao livro (Obrigação Fiscal) e Estabelecimento informado na abertura da tela para seleção do usuário. | MFS1943 |
| Cód. Operação | Cód. Operação | Texto | N | N | Default: desabilitado | Nessa coluna serão exibidos os códigos de Operação da Apuração do campo Operação Apuração da Aba Lançamento de Valores de acordo com os Lançamentos efetuados no período. | MFS1943 |
| Descrição | Descrição | Texto | N | N | Default: desabilitado | Nessa coluna serão exibidas as descrições efetuadas no campo Descrição da Aba Lançamento de Valores de acordo com os Lançamentos efetuados no período. | MFS1943 |
| UF | UF | Texto | N | N | Default: desabilitado | Nessa coluna serão exibidas as UFs do campo UF da Aba Lançamento de Valores de acordo com os Lançamentos efetuados no período. | MFS1943 |
| Classe Lançamento | Classe Lançamento | Texto | N | N | Default: desabilitado | Nessa coluna serão exibidas as Classes de Lançamentos do campo Classe Lançamento da Aba Lançamento de Valores de acordo com os Lançamentos efetuados no período. | MFS1943 |
| Amparo/Texto/Ocor. | Amparo/Texto/Ocor. | Texto | N | N | Default: desabilitado | Nessa coluna serão exibidos os Amparos/Texto/Ocorrência do campo Amparo/Texto/Ocorrência da Aba Lançamento de Valores de acordo com os Lançamentos efetuados no período. | MFS1943 |
| Subitem Amp. | Subitem Amp. | Texto | N | N | Default: desabilitado | Nessa coluna serão exibidos os Subitens dos Amparos/Texto/Ocorrência do campo Subitem Amp./Texto/Ocor. da Aba Lançamento de Valores de acordo com os Lançamentos efetuados no período. | MFS1943 |
| Código de Ajuste (Sped Fiscal – E111/E220) | Texto | Texto | N | N | Default: desabilitado | Nessa coluna serão exibidos os Códigos de Ajuste correspondente ao Sped Fiscal do campo Código de Ajuste (Sped Fiscal – E111/E220) da Aba Lançamento de Valores de acordo com os Lançamentos efetuados no período. | MFS1943 |
| Copiar | Botão | Botão | N | N | Default: desabilitado | Neste campo efetuará a cópia de todos os Lançamentos selecionados no Checkbox para seleção dos Lançamentos para os Lançamentos em questão, lançamento do período de apuração e livro (Obrigação Fiscal) informado na abertura da tela. | MFS1943 |
| Cancelar | Botão | Botão | N | N | Default: desabilitado | Neste campo é possível cancelar a cópia dos lançamentos selecionados.  Quando selecionado, cancela a operação e fecha a tela de parametrização. | MFS1943 |
