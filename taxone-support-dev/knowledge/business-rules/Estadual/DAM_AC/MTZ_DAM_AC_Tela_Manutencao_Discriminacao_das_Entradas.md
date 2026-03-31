# MTZ_DAM_AC_Tela_Manutencao_Discriminacao_das_Entradas

- **Fonte:** MTZ_DAM_AC_Tela_Manutencao_Discriminacao_das_Entradas.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 144 KB

---

THOMSON REUTERS

Manutenção da Discriminação das Entradas

DAM\-AC

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS1680

Julyana Perrucini

Este documento tem como objetivo criar o módulo DAM\-AC\.

Sumário

[1\.	Regras dos Campos	3](#_Toc452646146)

[2\.	Sugestão de Layout	13](#_Toc452646147)

# <a id="_Toc350763252"></a><a id="_Toc452646146"></a>Regras dos Campos 

__Localização da tela:__ Estadual\\ DAM\-AC\\ Obrigações\\ Manutenção\\ Discriminação das Entradas

__Título da tela: __Discriminação das Entradas

__Regra Geral Botões \(procedimento padrão Mastersaf DW\):__

__Novo – __Permite voltar à tela inicial\.

__Abre – __Permite abrir uma lista de seleção dos registros inseridos\.

__Exclui – __Permite excluir registros\.

__Confirma –__ Permite salvar os registros depois de preenchidos\.

__Imprime –__ Permite imprimir o conteúdo gravado\.

__Relatório –__ Permite gerar relatório de conferência dos registros inseridos, sendo possível filtrar por todos os campos da tabela\.

__FECHA – __Permite sair da tela\.

Essa tela servirá para receber as informações do resumo de alíquota para conferência por CFOP antes da geração do demonstrativo, deverá ser bloqueada e não irá permitir a manutenção, será possível localizar os registros através de seleção \(pelo botão Abrir\) ou por dados inseridos no seu cabeçalho \(pelo botão Novo\), nesse último caso não haverá a possibilidade de inclusão\. 

__Campo__

__Tipo__

__Obrig__

__Ed__

__Formato/Default__

__Regra__

__MFS/CH__

Estabelecimentos

Texto

S

N

Formato:

Combo Box

Default:

Não se aplica

Permite o usuário selecionar ou visualizar o estabelecimento para conferir os registros de entradas processados pela geração dos registros\.

__Tratamento:__

- O campo será apresentado de forma desbloqueada se o usuário desejar selecionar um registro pelo botão Novo\. Nesse caso se não for selecionado um estabelecimento na tela de Login, deverá apresentar a lista dos estabelecimentos de UF igual a AC, caso contrário, apresentar o estabelecimento que foi selecionado na tela de Login;
- O campo será apresentado de forma bloqueada se o usuário desejar selecionar um registro pelo botão Abrir\. Nesse caso se não for selecionado um estabelecimento na tela de Login, deverá apresentar todos os registros dos estabelecimentos de UF igual a AC, caso contrário, apresentar os registros do estabelecimento que foi selecionado na tela de Login;

MFS1680

Mês/ Ano Referência

Texto

S

N

Formato: 

MM/AAAA

Default: 

Não se aplica

Permite o usuário selecionar ou visualizar o mês e o ano de referência para conferir os registros de entradas processados pela geração dos registros\.

__Tratamento:__

- O campo será apresentado de forma desbloqueada se o usuário desejar selecionar um registro pelo botão Novo \(combinação entre os campos Estabelecimento, Mês/ Ano Referência e CFOP\)\.
- O campo será apresentado de forma bloqueada se o usuário desejar selecionar um registro pelo botão Abrir\.

MFS1680

CFOP

Numérico

N

N

Formato: 

Icon/ Text Input

Default: 

Não se aplica

Permite o usuário selecionar ou visualizar o CFOP para conferir os registros de entradas processados pela geração dos registros\.

Os CFOP vem da tabela SAFX2012 na seleção pelo botão Novo e vinculado na NF de acordo com os registros geradas pelo botão Abrir\.

__Tratamento:__

- O campo será apresentado de forma desbloqueada se o usuário desejar selecionar um registro pelo botão Novo \(combinação entre os campos Estabelecimento, Mês/ Ano Referência e CFOP\)\.
- O campo será apresentado de forma desbloqueada se o usuário desejar selecionar um registro pelo botão Abrir\.

MFS1680

Do Estado – Valor Contábil: 17%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor contábil das entradas do estado geradas a 17% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Do Estado – Valor Contábil: 25%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor contábil das entradas do estado geradas a 25% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Do Estado – Valor Contábil: Subst\. Tributária

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor contábil das entradas do estado geradas por substituição tributária para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Do Estado – Valor Contábil: Outras

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor contábil das entradas do estado geradas por outras operações para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Do Estado – Base de Cálculo: 17%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de cálculo das entradas do estado geradas a 17% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Do Estado – Base de Cálculo: 25%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de cálculo das entradas do estado geradas a 25% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Do Estado – Base de Cálculo: Subst\. Tributária

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de cálculo das entradas do estado geradas por substituição tributária para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Do Estado – Base de Cálculo: Outras

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de cálculo das entradas do estado geradas por outras operações para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Do Estado – Isentas ou Não Tributadas: 17%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de operações isentas ou não tributadas das entradas do estado geradas a 17% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Do Estado – Isentas ou Não Tributadas: 25%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de operações isentas ou não tributadas das entradas do estado geradas a 25% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Do Estado – Isentas ou Não Tributadas: Subst\. Tributária

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de operações isentas ou não tributadas das entradas do estado geradas por substituição tributária para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Do Estado – Isentas ou Não Tributadas: Outras

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de operações isentas ou não tributadas das entradas do estado geradas por outras operações para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Do Estado – Outras: 17%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base outras das entradas do estado geradas a 17% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Do Estado – Outras: 25%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base outras das entradas do estado geradas a 25% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Do Estado – Outras: Subst\. Tributária

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base outras das entradas do estado geradas por substituição tributária para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Do Estado – Outras: Outras

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base outras das entradas do estado geradas por outras operações para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

De outros Estados – Valor Contábil: 7%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor contábil das entradas de outros estados geradas a 7% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

De outros Estados – Valor Contábil: 12%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor contábil das entradas de outros estados geradas a 12% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

De outros Estados – Valor Contábil: Subst\. Tributária a 7%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor contábil das entradas de outros estados geradas por substituição tributária a 7% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

De outros Estados – Valor Contábil: Subst\. Tributária a 12%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor contábil das entradas de outros estados geradas por substituição tributária a 12% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

De outros Estados – Valor Contábil: Outras

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor contábil das entradas de outros estados geradas por outras operações para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

De outros Estados – Base de Cálculo: 7%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de cálculo das entradas de outros estados geradas a 7% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

De outros Estados – Base de Cálculo: 12%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de cálculo das entradas de outros estados geradas a 12% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

De outros Estados – Base de Cálculo: Subst\. Tributária a 7%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de cálculo das entradas de outros estados geradas por substituição tributária a 7% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

De outros Estados – Base de Cálculo: Subst\. Tributária a 12%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de cálculo das entradas de outros estados geradas por substituição tributária a 12% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

De outros Estados – Base de Cálculo: Outras

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de cálculo das entradas de outros estados geradas por outras operações para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

De outros Estados – Isentas ou Não Tributadas: 7%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de operações isentas ou não tributadas das entradas de outros estados geradas a 7% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

De outros Estados – Isentas ou Não Tributadas: 12%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de operações isentas ou não tributadas das entradas de outros estados geradas a 12% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

De outros Estados – Isentas ou Não Tributadas: Subst\. Tributária a 7%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de operações isentas ou não tributadas das entradas de outros estados geradas por substituição tributária a 7% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

De outros Estados – Isentas ou Não Tributadas: Subst\. Tributária a 12%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de operações isentas ou não tributadas das entradas de outros estados geradas por substituição tributária a 12% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

De outros Estados – Isentas ou Não Tributadas: Outras

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de operações isentas ou não tributadas das entradas de outros estados geradas por outras operações para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

De outros Estados – Outras: 7%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base outras das entradas de outros estados geradas a 7% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

De outros Estados – Outras: 12%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base outras das entradas de outros estados geradas a 12% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

De outros Estados – Outras: Subst\. Tributária a 7%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base outras das entradas de outros estados geradas por substituição tributária a 7% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

De outros Estados – Outras: Subst\. Tributária a 12%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base outras das entradas de outros estados geradas por substituição tributária a 12% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

De outros Estados – Outras: Outras

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base outras das entradas de outros estados geradas por outras operações para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Do Exterior – Valor Contábil

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor contábil das entradas com operações do exterior para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Do Exterior – Base de Cálculo

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de cálculo das entradas com operações do exterior para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Do Exterior – Isentas ou Não Tributadas

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de isentas ou não tributadas das entradas com operações do exterior para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Do Exterior – Outras

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base outras das entradas com operações do exterior para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Nº Processo

Numérico

S

N

Formato: 

Text Input

Default: 

Bloqueado

Permite gravar o número do processo de geração dos registros\.

MFS1680

# <a id="_Toc452646147"></a>Sugestão de Layout

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA2YAAALlCAIAAAAg5GJrAAAAAXNSR0IArs4c6QAA/8pJREFUeF7snQm8TVX7x19TZCZ0yZgxQ5QyVciQqVIkCREyRShThowNIoWiTFFJZIoyVug1h8hc/E0N5nuvWab/V6u285477XvGfc797U+dz77rrPWstb57O+d3nmc9ayf766+//hP3wbu33HJLPBXieuvixYu8lSZNGg/a0kT92uQmzjZBmWq6r2zi0n1lE5Tuq0SB0n2VKFz6vLKJS/eVTVDef14lT1RPqiwCIiACIiACIiACIpAECSSzvIxt27adMmVKEkQQllO+6667wnJefppU8uQ+++3ksWfdT1OT2bAh8NBDD/lwLhcuXPCVtatXr/rKVPr06X1l6vz5874yJTvBIpA2bVofdl2+fHlfWfMs+hpr78mSJfPVqHLnzu0rU7fddhvWzDQvX75szN7w5iIZzVG2bFlfdSY7IiACIiACIiACIiACoUsgZ86cI0aMsFTi6dOnb3oZK1asuGnTptCdm/2RI5/tV06wZo4cORKsowr+IFC9enVfmY1/RW+iejl69Gii6sdT+fbbb/eVKR+OyldD8rmdvXv3+sqmDx1U+/fv99WoZCdRBDJlypSo+vFU9uH9QC+Wz8b74fnQQXXPPfd4Px5jwYde561bt/pqVLLjGYHXXnutX79+pi1expuSsUqVKmvXrqX0+vXrnplWKxEQAREQAREQAREQgZAmcO+99/70009M4f3332fVoiUZby7hyp8/f0jPUIMXAREQAREQAREQARHwksB7771nLPzyyy+uppJbUWofrob2cqxqLgIiIAIiIAIiIAIiEHQClkokTzQ5GTHmUKZn0C+MBiACIiACIiACIiACDiFw6tQpSyVeu3btZmA6W7ZsbkPctWvXfffdx3YtLMNnpeP48eMPHz5s6hw5cuSZZ545e/asx7Ni3WSfPn0SbO59R65dfPfdd507d545cyarOEePHo3xBAfgWuH48ePNmjU7d+5colq5VqbrMmXKgLRAgQK5cuXKmjVrnTp1Ll265LHBuBqyIJWZ7t692+eWZVAEREAEREAERMAhBEhdIhHK9ciSJctXX30Vc3gIjyeffPLgwYNub40aNYq3pk6dGrPJyZMnXQtvpr+88MILpoGV/rJw4cJ69eqRYk3q2bFjx6ZP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iEWTQRGAw5KMPEBuxowZ4S8ZmaFZIxgAuOpCBERABERABERABMKDAJKRNAlSXNj6Zu3atZZkDGdFJb0YHveuZiECIiACIiACIhBIAmb/PrfjpmQ0zwtRDDeQl0R9iYAIiIAIiIAIiIDTCJhcadfklhsS0drskORfUqTZVpBMW6cNnfHETAjyeJCk+HjcNgk2ZIMkX82aHc59ZUp2RCAkCLAmPSTG6c0gzf5tOkTAEGBzEqEIdQKEpNu1a2dmYanEWNJfQn2eGr8IeECAR3570CrWJjVr1vSVKfOsIwcePE7JgaNiIyoHjspsFuuTw7fKzM154JMRykiACVgPdAhwv+ouiRDgUSzsS8gz8Mx8b0hG87AQDrYSZP9tfY4kkVtB0xQBERABERABERCBmASsZ5rwwGc2mbYq3JSMr732mnlcjOuugV6iNFuQ++Sw+QhFn/SVKCNu+7Mnqq3/KseVpe+/Hu1Y9u1F9OHdZWfwqiMCIuBvAj5cgGQepObAw4cro/g6d+AEk8KQeKKHr6bpwy8yt4f7eTNCHrDMY+ew0KxZs7Fjx96UjFaUmqen+FwyejNitRUBERABERABERABEQgwATJbChYsSKeDBg3iyXOmdwLT4bzJToARqzsREAEREAEREAERCFcCkozhemU1LxEQAREQAREQARHwGQFJRp+hlCEREAEREAEREAERCFcCkozhemU1LxEQAREQAREQARHwGQFJRp+hlCEREAEREAEREAERCFcCkozhemU1LxEQAREQAREQARHwGQFJRp+hlCEREAEREAEREAERCFcCkozhemU1LxEQAREQAREQARHwGQFJRp+hlCEREAEREAEREAERCFcCkozhemU1LxEQAREQAREQARHwGYFkemCgz1gmPUOHDh3iSZRJb96asVMIcAc6ZSgaR9IgkDdv3pCb6LFjx3jUm/1h58iRo3r16vbrq2b4EYjrgYGSjOF3rQM3o+nTp0syBg63ehIBERCBgBCoW7duyZIlA9KVOnEiAUlGJ16VUB+TkYx8smTKlCnU56LxhyIBj2+8jBkzhuJ8NWZfETh9+rRnpqKjoz1rGJRWq1evpl/0n/0b/tdff920aVOePHmaNGkSlDGrUycQkGR0wlUItzEYyfjMM8+EYrAm3C6G5iMCIiAC/0vg7bffpqBnz572wbDY44svvpBktE8sLGvG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nkyyF/HIkSPXrl1z+PR5rrTDR6jhiYAIiIAIiIAIeEkgaJLx559/rlWr1q+//uo6AQRix44d582bZwrPnTvXtm3b++6779tvv7Uzz+vXr3/22WcHDx6MtfKWLVuqVat2/PhxO6biqbN169bHHnvsrrvuKlSoEM9u79+///bt2xO0OXny5Bo1apw6dSrBmlaF77//nifEA+T06URvAYPQbNeu3c6dO+1358yaXNMfflh77NgJZw5PoxIBERABERCBJEIgaJIR6bZ06VJkTWRkpGGNOBg1atS4ceP27NljSjj/888/+/TpU7NmzQMHDiR4SViw2bx58/3798dac9q0acuXL//6668TtBN/BSwcPnz4lVde6devHypw/fr1pUqVmj59ejytdu3a1bp163Tp0qVIkcJm70z8qaeeGj58+G+//fbOO+/YbGVVS5YsWcOGDe+4447ENnRaffZ9XL589bFj3gp9p81L4xEBERABERCB0CIQNMmYNm1aSKHh+vbte+XKFc5xqvXq1YsTS1c9+eSTI0aMqFix4ubNm3PlypUg2e+++y5//vz3339/zJq49z788MP06dNPmDDh8uXLCZrCS4eEjasavbRp06Zly5Yvv/zyokWLELVvvPFGPPVxQ+bJk2fWrFn2N6O57bbb5s+fX7Vq1ddff52+EhywWwUk4yOPPGK/u8TaN/Xz57+RKH3w4I0VjX46duzYnTJlykKF7vSTfZkVAREQAREQARGwQyBokjFVqlSMb+TIkbgSJ06ceOLEia5du3bu3BmBmDz5jVGdP3/+k08+KV26ND68Zs2aWbFp9OWYMWPuvffe+vXrz54928hNDk6mTJmC2xJnXsyZr1y58uzZs+jFtWvXbty40VT44osvBg0axBjKlCmDS8+KaK9Zs6ZSpUqItvbt2x86dMjNGsOzOuUtxCUB9CJFiphqhNoxiIhcvHgxcXZK0Lu4JHFMNmrUiIY8rvGrr75CKDML3KKmVbdu3QYOHPjoo4+WK1cO/6Jp9eqrrxL+ZmyoRuOLJSb+7LPPMmwi7A899NAPP/xgmqNWkcu4FSlfsGABf169ehVFixFTgQg1eCtUqDBs2DAT5sZFumzZspigHFXCLLZs2VGyZDFrA0VHDU+DEQEREAEREIGkQyBokhHXEZTr1Knz/vvvd+jQAX2DnELHICVNwsfo0aPRXnja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6ZkzZ0ZERMyZMwfpjaMRzyJRYJx8xJ1ZR4iIdP1xQKAZVyJORBQ6B94+XIksfzx58uSdd96JE7FIkSJ4WIl9k4jNSkfO8RoiNEmsPnXq1N13380JxlnU+MMPPyAZyXHBqclGPK+++irykR12IiMjCWpT+Oabb7I+cu/evV9//fXq1atJyrEmmDt3bvv/DFg6ab+yaton8Nhjj9mvHFdNbkLvjeAy995IPHtF2Tfuk5HY787fNXfu3Ol9Fz5xZZl1zzp8S6BUqVLeG4yOjvbeSMxUSw9smviVl0eDBg28tEBzfCLeG2FVmPdGZCEeAvPmzUPkBACR47yMBHnNtO1IZkafP39+KvPauHFjRCGORqshac5NmjRBNbLoEPXmZpA0FJSlK2KM7Nixg2oEl1m2yErH1157DU1tGuK5HDduXOnSpY3TER1J9nTJkiXZ1rF79+4kvlCI3/GDDz4gnE21IUOGIBNZ6YjDkoFhrWHDhuhFO/NSHREQAREQAREQARGIhwCr5oyGIekiMKAc52VkuSGZK0Yy2pHMpprHKwJde7FjhPoJVkMmssTHJ6t87BBQHREQAREQAREQgaRGwPL5DRo0CA9XAKYfl5fRB4uaPRs90eFENUTAJajh4jFomts3YqcvpiC9mKiLqMoiIAIiIAIiIAIhSiBokjFEeWnYIiACIiACIiACIpAECSQna9ocSXDymrIIiIAIiIAIiIAIiEBcBFxVoryMuk9EQAREQAREQAREQAQSIJCcHS/NIVQiIAIiIAIiIAIiIAIiYBFwVYnyMurGEAEREAEREAEREAERSMjLKEIiIAIiIAIiIAIiIAIiED8BeRl1h4iACIiACIiACIiACMjLqHtABERABERABERABETAOwJB8zLqMcreXTi1FgEREAEREAERSEIEjh8/HtzZBk0yBnfa6l0EREAEREAEREAERMA+AUlG+6xUUwREQAREQAREQASSKAFJxiR64TVtERABERABERABEbBPQJLRPivVFAEREAEREAEREIEkSkCSMYleeE1bBERABERABERABOwTkGS0z0o1RUAEREAEREAERCCJErgpGX/77bckykDTFgEREAEREAEREAER+F8Cu3btci2Ql1E3iAh4ReDChQt9+vTZu3evV1bUOF4CEyZMWLx4sSCJQIAJXP/7CHCn6k4EHEsgaJIxX758joWi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wIHp06fXrl3be4MJWojLyxgmkjHB+auCCIiACIiACIiACIhAggTikoxBy5hOcMSqIAIiIAIiIAIiIAIi4BACkowOuRAahgiIgAiIgAiIgAg4l4Ako3OvjUYmAiIgAiIgAiIgAg4hIMnokAuhYYiACIiACIiACIiAcwlIMjr32mhkIiACIiACIiACIuAQApKMDrkQGoYIiIAIiIAIiIAIOJeAJKNzr41GJgIiIAIiIAIiIAIOISDJ6JALoWGIgAiIgAiIgAiIgHMJhIZk3LVr13333XfXXXfdfvvtVapUGT9+/OHDh50L9d+RXbt2rU+fPqVKleLRiHnz5mXwPJ546NChvho5T/Xh8UG7d+/2lUHZEQEREAEREAEREIFYCYSGZNy/f/+mTZvatGnz+uuv16pVa8yYMeXLl9+zZ4/PL+rx48e7dOkSHR3tE8s8RPzNN9+sWbPmK6+80r9/fwbPUxnr1KkTl3EkZt++fdHHNns/f/78+++/b7++TbOqJgIiIAIiIAIiIAJuBJJbD5x2MprkyW9I2+effx7ViN9u3bp11atXb9++/dmzZ+0PG0GWYGW06ejRo0+cOBFXzatXryZoxKpw5coVzh999NF27dq98MILDL5Vq1Zly5aNywLTeeONN/bu3Wuni8uXLydLloya1rw4we9op63qiIAIiIAIiIAIiECCBCyViBJLfsu/R4LNglghVapU9I5IMmPgOd8IxxUrVmzdupU/L168+NVXX+Gfw/vIgxFjjvPQoUNPP/10ihQpUG/ITSOzmjZtumbNGlP5vffe++STTyIjI7t168afTzzxxB9//PHzzz/Tio4IK48bN+7cuXN0kTJlSkLk06ZNM+IMryQVChUq1LZt27Vr17p1bZRurFIVNclo77333vr168+ePduIy969e/PaokWLH374wZjCPr7JBx54AN8njyQ3hehaBCjXrUaNGvxpVCxzqVSp0m233YaSZr6m5vbt2xGpBPTxccZKJiYrlYiACIiACIiACIiAIWCpRMRMaASmjWR09fAVKFCAEoTdhQsXWrdu3axZsyNHjqDkKlasaAlBM9tLly4hsNBeH3/8ce7cuZs0aYKiwp/3+eefnzx50tTZsWMHAjFTpkz16tXjz06dOmXNmvXgwYNffvnlypUrCSs/+OCD77777sSJEz/88ENEHt19++231Bw2bNjOnTsRZKhDFNuqVatcbzIjK9GmLGHEYK5cuZCbxomIxh07diwd4XRs2bIlkpTCxx57jFdGi0jlhLh2gwYNqNm8eXMWLLJskcKoqKhGjRoxHQbDKklKuIrMCDVcpkyZ4cOHM2yELzIajYtfM2PGjD169CCsX7t2bRDp34AIiIAIiIAIiIAIeELAcjmiNkx7hI7TjuXLlxuBaA3MqJ/vv/9+xowZnODhQzmhDpFH+fPnZzGiVXP16tVU+PXXXylh8R/KCWfe0aNHKcSsqdahQwfceJwYIci7nM+fP59zFB7nRlzOnTvX1B84cGDx4sXxej7++OPIR2QlsWzqI9dc0f3555+0QsBN+vuYMGECstWMjfA3YvGbb75B7W3YsGH9+vUUMkHXUQ0ZMqRkyZJ4B3lr1qxZvIUKnDlzJie0opD5cv7ZZ5+xorFy5cq8SyE+SDNUZGWWLFkY6saNG5kRoBDKTruyGo8IiIAIiIAIiICjCOzbt69cuXJoiWrVqlkq8fTp08n4wyhFMjPQW0YyeqI9E9kGz1yCucPWSL777juCsOieHDlymH4QiyxnRDmRX2JcdK4HIslaMoinkPgy8o6YMnVYLIhE++ijjyIiIpYtW2Ziu3j7cBMi4yh55JFHTEcLFy7E6YirD+FFigkakThviRIlqL906VKycJCJ+PxQbPgLjx07RkSYGREatkaCrs2ZMydDffjhh91GSBAcDYfPktg6CTHodSz//vvv+EEJuJMVjrLkHNcmnkJrvmjKKVOmELZetGgRhahkou1Tp07dsmULLliuoOmlQoUKuDbxSuJwpT5SlWG8/PLLXbt2NRA4zDrIBA9z0+hwJeCTfyB2VtYKuwg89NBD3kMwURpvDrPGxssjffr0XlqgOV9a3huRBT8RSJs2rfeW77//fu+NpEmTxnsjqVOn9t6IJVq8MYUIIVDJ1703RhLVFl8VIVnEEpJx8eLFpi3Ry/8Ey8sYTxaINTFLdC9ZsoRC3GamBK1GAPqll15CJ7366qvQnD59OgqMWDOxaZYGMjGrrVliiMyiBKF2zz33sHKRtYMMALlJIWoS9YkvkPP//ve/VDbuTCQj5/TFOcKRzzs0palP16hJXI9YI3H7zJkzmzdvLl26NMFi1x8Kbl5D17dYYjhnzhzchL/88gvnuCp5lwnSI55OztGgnDMX04p58ScSmS4sNypuRQoRhUhP7kuaUBP5SCGOT4LRxNOpg9kFCxZQ+OOPP1pjSNTdo8oiIAIiIAIiIAJBJEBWA+6zwDgjHedlZFUfmiZ++pY7B6da3bp1UWwsw0SHEZzFR4jkQiyyyA8VTIAYXx1/4rTDMoLSsowse+qppxB2vCKW8e5gDa8bKpOclQEDBvAWOqxnz54sTEST4e3DP4dvDzGHTSSjcRzinkRiUk6o+uuvvybezY8hLiHJJXgcWQpJc6QtTkqra+M1ZCkkdfh9YH6ps04RLyBOVryPZFKj8xB8qEbSaBgbTgWWab744otM4bXXXsNF2rFjR6b81ltvGcmIwwDPH1oQmUv0mdD25MmTOccmflDyaZgLqy2xSas777yzX79+9MjEicKT+sP2kGZ47FIUxFs/WF2b1aJeHtyEXlqguVka4eXBTp9eWvDVSLwfhq8ssLbYe1M+cWW5Lar2flSyAAGzgNvLwyfbqFlZht4MhgX03jQ3bVny7r0RImbeG+EryXsjshAPgXnz5vH9HgBEjvMyWrFaO5KZ0eNaAxOvjRs3Rg8Z5585WL1HRBgVhSPwueeew5XqZpM1haxfpC3eQbM00DgLWQJYsGBBRFX37t3JmDblBJ1RYOgwvntINLEclrjr6Ldw4cINGzZEL5rKyEqyVRCgSEkEmdnmxjpQqyRfu11dov9UwEPJmGmIt5JFkFYv6FemQEIMdfhcGzFiBI5MUlsIvrMKEy8p5cTHzU1D10TD8YxSiFbGjYxqJMZtqnEQ42ZXSMaM+uRHgxsW/SkCIiACIiACIuBwAiwqM0KCaGpghuo4LyOePBQbCJi/HclsqsW/Ao86Npfoxd+jr+yYXtwmaGeEdgbAigKfuLvswFcdERABERABERCBoBDA1YV7i64HDRqEAygAY4jLy+iDRc2ejd7Kw7DZHKWVoNhKsIL9vmzWtFPNjNw6bDZJsJr0YoKIVEEEREAEREAERMBXBIImGX01AdkRAREQAREQAREQARHwNwFJRn8Tln0REAEREAEREAERCHkCkowhfwk1AREQAREQAREQARHwNwFJRn8Tln0REAEREAEREAERCHkCkowhfwk1AREQAREQAREQARHwNwFJRn8Tln0REAEREAEREAERCHkCkowhfwk1AREQAREQAREQARHwNwFJRn8Tln0REIEkSoCnQ/G8UJ5ByoNAeZJT/I+Y4+mxPJLUJ6R44CFPWM2aNWuGDBnYEZYTni2ZK1cunlBl2edRVTywlGdcMSqecc8DqDzumsdc8fjWWJ84d+TIkWeeeebs2bMeG0+woSAHAHKCV0EVkgiBoEnGO+64I4kg1jRFQASSIAEeI86DPXnQPI+Pf/zxxxcsWMBT6bdt2xYXih07dnz11Vc2QW3atImn3sdVmUenogIRqTyVlDqtW7dGjPKcevMACXMgJXn2KZ/DBw4cmDZtGo9gtdN1rP0OGzasRYsWPAQ1pgU0K2+lTZvWjnEP6ggy0PwN2YProiZ+InD8+HE/WbZrlt+j5uDZxKZNYJ5gGODuAjMp9SICIiAChsC3337Lx+kff/xh/uQh9TwmHvkYF5+xY8eWLl3aJr2PPvooT548CVY2fk3zGPq4jjVr1lDn4MGDCVqjQsx+eXIp0vObb76x09zndQTZ50hl0IEEeOKzkWedOnUKzPBcnzFtqUROguZltCtpVU8EREAEQpBA8eLF8fa9/vrre/bs4VMeT1uPHj1q1KjBVFatWtW8eXMKOUfVPfroo5GRkTxDlY/pp59+ukCBAuPGjbOCudu3b2/VqtVdd93Vv39/HvxKk61btw4cOPDw4cNUvnr1ajxsrly5wrupUqUydbp160ZDuitXrtxvv/3WsmXLzZs3p0iRgre6dOlCv71798Ytyp/EOmvVqsUr5xghuPzTTz/F2i+KM2PGjDgaJ0+efPny5ejoaHyrzJounn32WXp54oknTp06ZZwRS5cuZeLVqlX7/PPP4x+5zQsuyAGAbPNaqFpSIJA8zb9HUpit5igCIiACgSGQM2fOZcuWrVy5slixYg0aNCDojIp6+OGH6X3Xrl2oRjMM4rm46I4dO0akGJmYLl26l19++d133yWObHyTbdq0QZMhNwkK46dExuXLlw87mEVKGsEX12FUKZZNhdmzZw8aNKhkyZJdu3ZFwk6dOhXBat5lJWKvXr3QhdikU/Qo8u78+fO8hR9xxowZqNWY/TKpqlWrZsqUiaWThL/x+RHgnj9//ujRo5s0aYIkJXBMHROzRiYiQwmF06Rp06bGu+nlIcgBgOzlNVLzUCfwPyqRjwNzBDhSHODuAuPLVS8iIAIi4EoA+bVkyZL27dvztVG+fPktW7bwLoqwZs2aphquO95iIeOkSZNy5MhBGgqFaDsKSexg6VKWLFlwDW7cuBH5hXRDVlIBr55lIR7gxitJ1oupkz9/fiLjJL5wToyJt+bNm/fjjz9ywiJLCnGIcj537lyULifIUwpNZgxdu/WLzGXAAwYMwA3JW2XLlkUpmggaZk2PxvjevXsJfONz5WMf5yL1aThlyhRf3SqCHADIvrpYsuMBgeAGpi2VqMB0qKt/jV8ERMChBP78889XX32VcPMjjzxCoBnNROp0hw4d+PxFtKFyzLiTJ7+xOohvEbQUnr/UqVPzJ3LQ6Mhs2bJ9/fXXBIvvu+++MmXK4BQ0FbAQv38xVih4C1gBadyK9Gh6NycmQ6VIkSLkzSAxsc+fJq5t6psS135J8UY1MiMzEtoiMc10SNA2AzCtsIBuposXXniBCtQnoOyThfyCHADIDv0HpmEFg4DWMgaDuvoUAREIdwK4Awkub9iwwUwUrUYomfRkJBonhGXNqkHziopCn/FqXHrGBUgmLGsNiRe/9957CKzx48cTnsZPyVvEr03UOP7DVR1SE/1qVCCHWUpo+uXE9Esh42FTHvyR/MkWPLzi3TQ13fplAKRg33rrrZQzWZZjstuOkYzWOkUjGSlEIkPA6F3WO164cIHKCQ0/4fcFGUb+hpzwZVCNcCRg/hWz7MR1cpKM4XipNScREIFgE0BOkWjy0ksvffLJJx9//PFzzz3Xs2dPQrfIpsqVK5MczZrFkSNH8moEGaKN8BO5I0SoCWTjhyOQTVSaVY9skbNo0aLp06ezdI+QLvULFy6MmsR5ifyilYluxzzcJCNdG5+i64HXkz9JUiFlmzWOy5cvZ2EikrFz586o1ffff79t27ZUQG669VunTh1UI9XQsiRNL168mApuPZruKGReRL1JsiHnmi2H1q9f75PrI8hg9Ddkn1wpGQkPApKM4XEdNYuAEsBHwpowVmgFtNck39mECROMLgmJA9ca8ghdheDjyJ49O55FpBWDZ1XfF198gXtv4cKFZDGTDsK7JCyzhWHu3Lm5tXDIMVOqUbhixQoE1pAhQwoVKoR8zJs3LxYIdrMuEPu//voraTFWMo0bmdtuu43MG2sTXFqhNU0d/JRkqNARXTNIqmFw//79uEXJj6ECiTIM7IMPPkDt1atXj5G49Yt+Zfy4uEaNGoXA7du3b9GiRfFQoj55y/TC/uE0R/jSnOQYkmzQoBUqVOjevTvT8f46CnIAIHt/mRK0YJb3JVhNFYJPIFjpLzNnzjST92ApqJqIgD8I8O3LEn68OHxV853Hxss//PADHZGF0KhRI8pxtxBfo4RUU25dvDv+GEbY22TFG9qFhXpmpvjP+PPBBx9ERZnMDA62ZcHFBXNUi9ky0ARkycYNOT5MyppXrIN3ezf+yq4W7Ne0Ay0eax6P0E6/PqkjyD7BGHgj/Otm9yi82qzWYKkrnwbEQwM/DIf3aKW/8E0UmKHSI9+GfOQ++eSTSn8JvlLXCBxIAHcL0UOcJTxXA38PyZ6ISMKFnPMpRiEKctasWSiefv364ZK58847HTgLhw+JQCpOKTZwIQWYoZKZi4uL3WfYq4/N/9h02oyfjGDq4OjiouBgwyHHVn/4q9hlxuETjDk8wrLWNjexDt7t3fgru1qwX9MOtHiseTxCO/36pI4g+wRjgI2w0T3ubT4ESBRDOOKN5tOABRLxDINFvSxv4GMkwENVd4aAAtO6E0TgHwKs82XlGQfLs8yKMR4NjFtx7dq17JeLu4s8AMJ5LDXjle3rBC6xBJDgpUqVMk9SJvsBIY5fYfDgwYhC1GH16tWtvfrwQaIOiZyyBiBz5swk53755ZcodWtX6sR2rfoiIAJOIzBmzBhyvNiSiQAOn7GkixHAQT6yA3xcQ2XtBAuCbT7f0mnzDYPxSDKGwUXUFHxMYPfu3SQl8GOXhV+sBnv77befeuoptjghfspOIggXVA5rtnzcaxIwR7ifbwUC/eZhdwQTWf1GsgVTR02iC81CPQ7yMFCWLOwjZwJZybOSuSImUKJDBEQgDAiwwTufBq+88grORTMdXMWPPfYYJ/yrj/X5Q2Tls/aXCqyXxUPJXqH8wmcPeVbKrl69ml+hPIKIz5PGjRvzp7GJV5LFwSycRZXy4z8MuAV3CpKMweWv3h1HACnDTsv4FIlHm8HxIUV6ATsPkxk6ceJEhCPZAJ999hmharP1sQ6bBFgkii8BIc6HO5xxGfJoEIQg2/u9+OKLLGcErDGFxxFHI8DRkTyShHOiUYSt0essDzC7iugQAREIXQJmn3mTa2UdhHr4WCBNKtbnD/Gu+YjgUcv8aGf/efyUrB0iqM0yIVY/8ynB5zPViFGYjT9Z4sJeUVQgU6pSpUpxJYqFLsYAj1ySMcDA1Z3TCfAxhFIhOGI2N+Zge5EHHniAXFdSpImJ8JuVffJ4VC6rHtlgGU3j9Ck5b3w8jNgMis9xdmNm+2jyXVDhrnuAkYRLYJq4Fc8+ee2113D9VqlShRWNvL7zzjvOm5NGJAIikAgCrDmhNj8jXduw+AdXIiuYzbssAeLV7AnKOhY+Lth5inNyMtiXHq8k+1WxkQLLhNhnikXSPLiIAAWeSzbsNNFtwhd8huCG5KOD5DkrjpGIgaqqCwFJRt0OIvA/BFhMwwN88TK6ceEDa8SIEQRE+FlMzJSwNR9GPOCVmKkIekyAj3WyXlCNbDrII4xj2uHBxKhJtCMhJx5MzONPPvzwQzY4pInHnaqhCIhA0AlEREQwBja3dx0J24KyjpzP2HieP2TVR0rynCHz2/7TTz/ll2eNGjU4N788kZ68svUpUWkSjXmQEntCGQ2qw2MCkoweo1PDMCTA5xcfMaS/3HLLLW7TY3s8ZA0r6vj9yoF/kU8igiO+zVoNQ6axTYlPcz7u2QiaPatxJxCetvYLdK3Ok0hIi8Gbi9cBFy86nkWQZpdBYU8it4qmGa4E2Iadf9H8DjcORY7t27f3/vuI5/lD5mlD5sEkOB3NRvRGIFq7gZqQNKEMChGL/OBkyxi2vmctI6k24cozMPMKmmTEqxyYGaoXEbBPYMGCBewQZn6quh58+pAEw69YItSENniqBzkZREDIg2FTYvv2VRMCZs9ewv2sMfrmm29IS2eRIs5dHIp8oONHtChRSFAJ5yLfDawEwLkIbbCjI62nGAupCIhAKBLgRyPhGlJYWGrCSnG0I1FmFjTzM5LpxPX8IT5+iWWzhJGlkHwsWI+m7NixIxufsfcCv/lr1aplgFCTzxkTkqYjgtf85gxFVtaY2cYyuOMPmmQM7rTVuwjESsDsv4hMcXuXnR3Y/4Un/PIhhX+LFY333nsveRgsv2MjMcFMLIE2bdqQK3333Xej/3iYHlqQp4xAlfxHa20oezESjEYdkrSOfZYr4f3lo99oR3kZE8tc9UXAaQR4DhBb9PNK9IaoMR8CbGFm/IgcsT5/CMk4Z84cnlHEbo7ErytWrGgq8znM80G+//772bNnkwdjHkFEJs20adN4TiY/NUnQXrduXc2aNZ0GIbTGk8zy67J0lG9ERm98AP4+cOfwpNGAdefv6ch+2BMgSGo9eC3sJ+uQCbJgEW8iMt0h4wmnYRANxCWDEPfJg/vCiYyf5kKWBi6uUNyL3k9AXM2ycjH+f+bIEtdfiW5/BmCEwe0ClypxfMbAUw989Xz2+GdEj08//TQPIyXTCAetqUxyuj6Lg3snqPeQISC9GPhLhZ9AejFR2FnxySpbdDaecp7vzBeMeaAOqVp8AVDerl07lpBSwtbohAWFN1F4qUxKL3FP1lSYhjwKnD9ZXMHXquVtYQkdC/KgTSKdWWhBSJR9Aa2NAhLbadjXT/A+dP7zh8L+GpkJSjImkQutaYqACIQ/AT300q/XOAk+7tKvPGU85AjcSDgyR8gNXQMWAREQARFwJaCHXvrvftDjLv3HVpadTMBSiTiDk7OZiDmcPGKNTQREQAREwD4BPfTSPiubNfW4S5ugVC3MCFgq8caS0zCbm6YjAiIgAkmcgB566Y8bQI+79AdV2QwtApKMoXW9NFoREAERSICAHnrp11tEj7v0K14ZdzKBoElG8/xHHSIgAiIgAr4loIde+pZnXNb0uMvAcFYvFoFdu3YFl0bQJGNwp63eRUAERCAsCeihl/6+rHrcpb8Jy75jCUgyOvbSaGAiIAIikGgCeuhlopElpoEed5kYWqobbgQkGcPtimo+IiACSZmAHnrp76uvx136m7DsO5ZA0B4YOG7cOJ4jDpfAPJ/QsRdAAxMBERCBwBDQQy8Dw9n0osddBpJ2ePdlPTCQpzqdPn06AJPVAwMDAFldiIAIiIBzCeihl4G8NnrcZSBpq6/AEFBgOjCc1YsIiIAIiIAIiIAIhDABScYQvngaugiIgAiIgAiIgAgEhoAkY2A4qxcREAEREAEREAERCGECkowhfPE0dBEQAREQAREQgbAnYBYinzlzJrgzlWQMLn/1LgIiIAIiIAIiIAIhQECb7ITARQrvIe7Zs/fIkWPM8fr1sJ1oVFS0mVtUVOL2R0iW7CYWzt2O1KlTm5KIiBzmxKpDSdGihSgRXo/vqjRpEsYrwh7jpaFNwoIsyN4QcG3r8Udx/AOwfyd7NhG2vKlcuTKbZP39RRmIb8q4NtmRZPTsCqqVzwgMGjTCZ7Zk6F8CfIT16tWZv4TXHzeFhVeE/YHXqElzA5tDt7E/OAuyP6i62XSD7FmPkoz/0Vbent064ddq6tQZBw4cLlOmRKZMmcJvdmZGMX+D2pxp/F7GyEh356XxMq5YsYbXAQO68yq8NlHHrBbTIRETrwh7jJeGNgkLsiB7Q8C1rccfxfEPwP6d7NlEJBklGT27c8KwldE0LVs2zpcvTxhOLxhTMi4ZV8kovD68Dq54LTUjwv4jLMg+ZGuZcruNBTkwkD3rxTmSMfnFfw/PZqJWIiACIiACIiACIiACYUnAVSUqYzosL7EmJQIiIAIiIAIiIAK+JJA8zb+HL63KlgjYJkBUmrqKStsGlriKwps4XomvLcKJZ5boFoKcaGSJbyDIiWeWJFq4qsSbXsazZ88midlrkiIgAiIgAiIgAiIQOgTMVt6BPH755Re6y5Ahg2unTgxMmw2BTp++uYMdcvaZZ57Zt29fTF79+vX77rvvPON47dq1pUuXtmvXrlChQs2bN/fYTszejx07Nm/ePOzz1qFDh5o1a8ZqALdqH3300dy5c8+dO8dkqePZFNRKBERABERABERABAJAwImSMVmyZF9++eXatWut+a9cuXLGjBkpUqSISWTx4sW7du3ygBR6bvDgwbVq1frrr79eeeWV5MmT16hR45NPPkmsqWnTpi1YsMC1FSrwhRdeeOONN65cuUL5gQMHqHPixAk3y/fff3+ZMmVOnTrFZJOyZMyf/0ai9MGDN8LTOnxOQHh9jtTNoAj7mzD2BVmQA0BAXSRIwImSMX/+/I8//vg333xjRs9e559++mmbNm0ojzmflClTGmeeOVzP45/8/PnzBw0ahC9w8uTJHTp04HX48OEtWrRA8Fmm7GyzvnDhwvXr17v2dfz4cWToZ599dsstt1CeKlWqWAd27733FihQAH1s5pjgpVIFERABERABERABEQgWASdKRlRUo0aNPv7445MnT8KFODUuRko437lzZ9euXStUqDBs2DATuUaQXb16lRMcdUR48UQ++uij69ato+Tnn3+mpE+fPkWKFGHncFfEKEviwn379q1fv74RbTTs1q3b3r1706VLx59r1qypVKnSbbfd1r59e+MC/OKLL5CYI0eOxDX41FNPHTx4kMLP/z5GjRo1evRoY//y5curV69GLPbq1ctEuo1ztEuXLgjE3r17m2f+cIwdOxYpjHeTc6awe/fuhg0b0jxYt4L6FQEREAEREAEREIG4CDhRMjLWhx9+mPWLq1at4hzhlTNnzooVK27duvXBBx9kmSBLAydMmDBlyhTeNV7GS5cuEQvGvYfQzJ07d5MmTdB5qDpivgS1iTvT0BXB0aNHiWjXrFnTtRBtV7BgQUpoi+5EGuJ3xAhSkpWI27dvHzhw4KRJk+gIhffiiy8Sdya4XLx48Tp16lStWpWGJtjN8B566KE8efIQ6caUkaRRUVGIyJ9++qlVq1bGkfnjjz/u2LHDSEa8jLly5cLZaVySOkRABERABERABETAUQQcKhlJDmrbti3ORbxuJnBMmjfSrW7duuPHj+/UqdOTTz65bds2UKKx0FubNm0ikQUd2bJly3fffbdYsWKWW5HliSS4lCpVypW7WWUY6+JIylmbSH0ciq1bt8bOnDlz0JeUI1vRr4jFnj17EjfHX1i4cOGsWbPi9bz77rupgG9y6NChJLV07969R48eRn0ayThmzBgclrwyzmXLllHCGNCLVmA6Y8aMSExH3RwajAiIgAiIgAiIgAgYAg6VjIyMSPT06dNZEchKQZTili1bli9fTng3ffr0vHv77bcTRObESC4T7TWLHW+99VacfOTEGEWIpIt5sZGkODJxQLq+hf+yadOmkZGRpGbjYkybNq2xWb58+cOHD+POxH8ZERFBIQFrXslc4RWPoxkDB05NPI4sxOQcCWjqmHWKxhohcnyQJm6OS9JVMuqOFAEREAEREAEREAHHEnCuZMSlR2yXMC5rCkuXLn3hwgUgZsqUiVf8c3/++eeZM2c4xw2J8KIm5ybJmhDwrFmzUIRGycWaEEOT55577p133jGuSnOQELNo0SJOihYtyspFwtycEw1HszIAmpDUYmqaExNERj4anyVHdHQ0stL0axZiMjzzrtlkB32JujUqlres3J24/J2OvW80MBEQAREQAREQgSRFwLmSkTQUItFcDNYOIq3KlStXvXp1vIwEpp9//nmixuY6IcV495577mH1IXFkkl2qVauGTCTxxXL+xXpFWe9IFkuVKlXY2RFf5oABA+hoyJAhWbJkwVOIhqMCAWikJ8FuHI1IRpNnw2EWI5pEGd4iEj179mzepSbB8f79+xOAfuSRR0xloy+feOIJ8l3I3cFXitOUEgbJCI1NusMm4W+lTiepf36arAiIgAiIgAiECgHnSkYIsn03Gc1GYLGWkdQTFimyVBGNOGLEiAceeIBynJEUpk6dGq1GxjGxbKLSaDgyZvLly0d02wSyYx40wch77723efNm1kqS5sKaRU6omTdvXtRbjhw5WLCIBqVHKpcsWZK+jJ1s2bIhAanAeefOndGdJMrg3eQEVyV5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eosNAeVlVGDas1tIrURABERABERABMKfgHMko9Jfwv9u0wxFQAREQAREQAREwEsCkoxeAlRzERABERABERABEQh/ApKM4X+NNUMREAEREAEREAER8JKAJKOXANVcBERABERABERABMKfgCRj+F9jzVAEREAEREAEREAEvCQgyeglQDUXAREQAREQAREQgfAnIMkY/tdYMxQBERABERABERABLwkETTKWK1eOoZ85c8bLCai5CIiACIiACIiACIQxgStXrjC7X375JbhzvPnAwEqVKvHswoA9Y7pYsWJ79uzJmTNn27Ztg4vA6j1z5szej6Rw4cLeGwkzC3fccYf3M8qbN6/3RmRBBAJG4ODBgwHry98d6be9vwkH3f7Zs2eDPgYNIC4C58+fb9SokXn3+vXrAQBlPWO6Q4cOo0aNMj3+zzOmAywZk5nn6egQgVAjkCFDBu+HXLNmTe+NREREeG/EJxayZcvmEzveGzlx4oT3RnxiYf369d7b8YlWC7pnwnsO4Woha9as4To1zcvnBE6dOlW3bt1vvvnG55ZjGoxLMv7n9L/HfffdRzO8jGjYABxVq1YtUqRIAGauLkRABERABERABEQgRAnkyJEj+99H586dAyDP6GLfvn2GFV5GSyVykoz/zRvVqlULZGDat1cuKirKe4Nbtmzx3ohPLKxYscIndrw3snLlSu+N+MSCT66OT+4Tn0xHRkQgqRHwycqfMmXKOISbT9YglShRwiHTCbNh/P77797PyCffF+nSpfPJSPgGPHDgwPTp02vXru29wQQtuHoZhw0bZtUP2lrGBEesCiIgAiIgAiIgAiIgAgEmEFdgOmgZ0wGev7oTAREQAREQAREQARHwmIAko8fo1FAEREAEREAEREAEkgoBScakcqU1TxEQAREQAREQARHwmIAko8fo1FAEREAEREAEREAEkgoBScakcqU1TxEQAREQAREQARHwmIAko8fo1FAEREAEREAEREAEkgoBScakcqU1TxEQAREQAREQARHwmEAISMZdu3bxZJq77rrr9ttvr1Klyvjx4w8fPmxzwj///HOFChXYLrVQoUK5cuXi6UzYsbY1t2kknmpr167t06eP93ZkQQREQAREQAREQAScTCAEJOP+/fs3bdrUpk2b119/vVatWmPGjClfvvyePXvsYOUxKjyk9aWXXurZs+fgwYOHDx/ev39/pGdcbenojTfesGPZ1MmdO3f9+vXt11dNERABERABERABEQhFAiEgGZMnvzHI559/HtWIS2/dunXVq1dv37792bNnDfFr167xSMRY6f/1118IxHbt2rVt25bmrVu3fvbZZ9OnTx+PZPzwww/tX8g8efKgX636V69etd9WNUVABERABERABEQgVAiEgGRMlSoVNC9fvmyY8sRGhCPuw61bt/LnmjVrKlWqdNtttyEiDx065MY9RYoUVkPXt3gYzpNPPmkC3J9//nnXrl05weDAgQMpfPrpp434+/XXX0eOHEl3ixcvvnTpEiVEunmXkiJFiowbN27VqlWdOnWi/Ny5c3379k2ZMiUx9GnTpiFho6OjcUDiGS1Xrhw6FV0bKveExikCIiACIiACIiACbgRCRjK6OvAKFCjANP744w804qOPPsqD6ok4Hzx4sFu3bhcvXnSdIUKNh3mzijFDhgy4G/PmzTt06FAqIDF54jhK8ZtvvmnatGnJkiUpzJcv38MPP1ysWLFWrVqhNZcvX44u/Oqrr3jAeZ06dTB+/vx5evnyyy9Xrlz5yiuvPPjgg7/88svUqVNp++67706cOBEPJTKxWbNm33777YkTJ+bPnz969OgmTZq0bNnS+Ep1iIAIiIAIiIAIiEBIEiB0aw7cY0zgkUcewUPmqAPpZgSiNaojR45Q8v3337///vuVK1fGw8dbLHmkcO7cua6DHzFiROHChSdMmDBp0iQkHakzeCVNhZ07d+bIkYMmnTt3xhNpCocNG1azZk1OLly4ULx4cWLZaFCjO6k8ZcoUVCBN9u7da+pjk/KTJ0+6do2rkrZmteW8efMcBVODEQEREAEREAEREIF4CFhZwh06dLBU4unTp5Pxh5G6hHc3btyIZFyyZIm/xS85KMbbF8/BZMy73333XY0aNY4ePWoUnhGLLGfExYhvD+/jqFGjTDnJ0bgMkYCWWSTjwoULqR+zIxo2btx49uzZs2bNatiwoanw1ltv4UFctGjRtm3b7r77brdWLVq0ICpdr169U6dOZcmShXcRo6TL0AUacfv27aRmU7h06VLSdDZv3nzvvfeSUs2o3OwkS5bM34R9Yp+Quk/shJMR67b0ZlJapeANvaTT9qGHHvJ+smZhj5eHT4Ik8Switz88vrTsV1bNABNImzat9z3ef//93htJkyaN90ZS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5MmTTIM4NS5GSjjfuXNn165dK1SoMGzYMBO5RpBdvXqVExx1RHjxRD766KPr1q2j5Oeff6akT58+RYoUGTdunCsRlCVx4b59+9avX9+INhp269Zt79696dKl4881a9bw+EQ2qmzfvr1xAX7xxRdIzJEjR+IafOqpp4zS//zvg2fpjB492ti/fPny6tWrEYu9evUykW7jHO3SpQsCsXfv3r///rupOXbsWKQw3k3OmcLu3bsbNmxIc/tXTjVFQAREQAREQAREIGAEHCcZmfnDDz/M+sVVq1ZxjvDKmTNnxYoVt27d+uCDD7JMkKWBEyZMmDJlCu8aL+OlS5eIBePeQ2jmzp27SZMm6DxUHTFfgtrEnWnoCvTo0aNEtGvWrOlaiLYzz3CkLboTaYjfESNISVYibt++feDAgZMmTaIjFN6LL75I3JngcvHixdn8vGrVqjQ0wW6G99BDD+XJk4dIN6aMJI2KikJE/vTTT61atTKOzB9//HHHjh1GMuJlzJUrF85O45LUIQIiIAIiIAIiIAJOI+BEyXjHHXe0bdsW5yJeNxM4JpSOdKtbt+748eN5LPeTTz65bds2UKKx0FubNm0ikQUd2bJly3fffbdYsWKWW5HliSS4lCpVypW7WWUY6+JIylmbSH0ciq1bt8bOnDlz0JeUI1vRr4jFnj17EjfHX1i4cOGsWbPi9bz77rupgG9y6NChJLV07969R48eRn0aychzxHFY8so4ly1bRgljQC9agemMGTMiMZ12c2g8IiACIiACIiACImAIOFEyMiwi0dOnT2dFICsFUYpbtmxZvnw54d306dPz7u23304QmRMjuUy01yx2vPXWW3HykRNjFCGSLuaVRpLiyMQB6foW/sumTZtGRkaSmo2LMW3atMZm+fLlDx8+jDsT/2VERASFBKx5JXOFVzyOZgwcODXxOLIQk3MkoKlj1ikaa4TI8UGauDkuSVfJqNtRBERABERABERABJxMwKGSEZcesV3CuKwpLF269IULF4CYKVMmXvHP/fnnnzwOm3PckAgvanJukqwJAc+aNQtFaJRcrAkxNOGxie+8845xVZqDhJhFixZxUrRoUVYuEubmnGg4mpUB0ISkFlPTnJggMvLR+Cw5oqOjkZWmX7MQk+GZd80mO+hL1K1Rsbxl5e7E5e908n2jsYmACIiACIiACCQpAsGRjL/9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0mTAgAEU7Jw+fdqPmDR1IREw1cT2vk66kFyVWREQAREQAREozgScKBl/+eWXXr16rVy5cvTo0Rz6U61aNQ79fvnll3O5T/v37x86dGhaWlpxvpeBuHZz7ox12HUgLkE+i4AIiIAIiEBxIOBEyTh16tRKlSpx4DjxxbvuuuuZZ57huHPk4+7du3O6JT///POUKVMOHDhQHO6Z1igCIiACIiACIiACPibgOMl48OBBNOKIESMILhoWQUFBN998M194M3VycvINN9zAJ39mZmbecccdGzduTElJGT58OD233norEcoFCxY8+OCD99577wUXXLBq1arjx4+//vrr3bp1i4qK4k9jk6jkmDFjGjVqhCpds2YNPT/++GPv3r1Pnjzp4xug6URABERABERABETA+QQcJxk5shJqzZo1c2XHq0FKly6dmpq6a9euTz/99OjRo/zKe2tQh4zn15tuuomewYMHV69e/bvvviNOmZGRQVKb3ZCjRo0iZ3399dczrGvXrohFRsbFxW3ZsoUBJUqU6NChw9dff12nTp1BgwYxi/PvmTwUAREQAREQAREQAR8TcJxkPHbsGAgqVqzoCmLv3r2EEmvWrGl+rVChAp8lS5bk89SpU8i+tm3b8r1nz57BwcFEJa+66qoZM2b0799/8+bNL7744uLFi4cNG0bk8rfffjPZ7e3bt5P7Jgz55JNPvv/++w0aNOCFNNddd52P6Ws6ERABERABERABEcidQJs2bRjg94INx0nG0NBQuCQmJrriW758eUhICKFHUzdNSppPpCGfpse1nhopWatWrfLly9P/xhtv9O3b12hB8xZjpCefkydPJivdp0+fGjVqfPTRR0aDqomACIiACIiACIiACGRLwHGS8aKLLurUqdOkSZNMQJH2/fffP/p7I+kcFhZGDzllPgk98mlijeXKleOTiCOfBB3JWZtrEYi1a9c2301Kmt2KdCIW77zzzh07dmzYsIG9jJTa6PkQAREQAREQAREQARHIiYDjJCMS8Omnn2aT4tVXXz1nzhy0I1nmK6+8cuDAgawByThkyBC2J06bNo3KFXpKlSrFJ5llctlsYWRrI5LRaEfaAw88MHHixAkTJhBWpG7GdDKSq0xKmolIXtevX//IkSOc/qiTw/V/FREQAREQAREQARHISsBxkhEX27Vrt2nTJj4feughssYvvfTSrFmzTByRFhsbSxiSzh49elD1wn5EIxnffffdb775htMcyV+3b9/eDOZAx4ULFy5btmzRokUITUqqCTpS4zJv3ryyZcuOHDmSAu34+PguXbpQhT1z5kzKq/WUiIAIiIAIiIAIiIAIuBEIsnK4ZcqU4TeKiMePH1/YmMw2xDznYociIcNcnCEoaEyZ5vZnYa9C9r0nMHfuAl4zHR0dpddMew/TWIiNncRnTMxIuwzKjgiIgAiIgB8JkD5lKx1Bsc6dO3/xxRc+8MR1RhKwZkYOonFilNHCkbteZJirXsz6pw+wagoREAEREAEREAERKA4EHC0Zi8MN0BpFQAREQAREQAREIBcCJoLm/0N2SEybprslAiIgAiIgAiIgAiIgAhYBSyUiW0uwhdE0ARIBEQh0AklJu1hCaGjNQF+I/BcBERABEXACAUslUl7i6PIXJ8CSD4VKwJS/tGsX2bhxI7eJwsLqez91Rsa5Evjk5H3eW/OxBVPZdebMuWldCr3O9Vg/mb8ZwDKXLl0Oun79onzsraYTAREQAREoDAIUo9x9992c7hIZGblu3brCmMLNZk7lL5KMPoCvKXIkEBfH28B1sJHNT4gko81AZU4EREAE/EdAktGjQ3b8d4M0s48IJCT8FB+/vmrVyikp6WbK1NQ08yUt7VyPLa4E4iE+BYgywio4uGxERHiLFk1t4SYjIiACIiAC/iUgySjJ6N8nULOLgAiIgAiIgAgEAAHnSEYdshMAj4tcFAEREAEREAERKLYEmjdv7oS1SzI64S7IBxEQAREQAREQARFwNAFJRkffHjknAiIgAiIgAiIgAk4gIMnohLsgH0RABERABERABETA0QQkGR19e+ScCIiACIiACIiACPiYQLavKJRk9PFd0HQiIAIiIAIiIAIiEHgEJBkD757JYxEQAREQAREQARHwMQH/SMY2bdqwzsOHD/t4tZpOBERABERABERABAKLQGZmJg5v27bNv27754WBERERCQkJtWvXHjBggH/Xb81etWpV7z0JDw/33kgRs1C3bl3vV9SgQQPvjciCCPiMQFJSks/m8sFE+s97H0D27xS//fabfx3Q7LkQOHr0aJ8+fcyAM2fO+ICV6+Hha9asMTNmZGT4RzIGmVehqYlAoBGoVKmS9y536dLFeyOhoaHeG7HFQo0aNWyx472RAwcOeG/EFgtr1671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ijLqwRABERABERABERABEcgryihCIiACIiACIiACIiACIpA7AUUZ9YSIgAiIgAiIgAiIgAgoyqhnQAREQAREQAREQAREwDsCQSdOnDAWunfv/umnn3pnTVc7hUCbNm2c4kog+HHmzBm73Dx9+rRdpmRHBFwJdOzY0UYgpUuXtstaiRK2ZasqVqxol1fp6el2mZIdfxEoX768jVNffvnldlmjIsQuU2XLlrXLVEhIiF2mMjMzp02bNn369MjIyDVr1hiznLbzFySjafxg12SyIwIiIAIiIAIiIAIiELgEqlSpEh4ebqlE/jPsfJSxffv269evD9y1ee553bp1PR+c50h7reU5nQZYBG6++Wa7aJQpU8YuU3v37rXLVK1atewyZaNXdrlku50tW7bYZdPGANXq1avt8kp28kWgefPm+Rqfy+C0tDS7TGFn586ddlnj3+h2merVq5ddplJTU+0ytXjxYrtMyU7BCFx66aXr1q0z1xJlPC8ZyXqsXbuWXhuTdAVzUVeJgAiIgAiIgAiIgAj4hUD//v1nz57N1KNGjZowYYIlGc/vQalZs6ZfPNOkIiACIiACIiACIiACDiEQHR1tPNm/f7+rS+cl44EDBxziq9wQAREQAREQAREQARFwFIHzkvFsLYyaCIiACIiACIiACIiACPzlL247U89LxoMHD4qPCIiACIiACIiACIiACEBg69atrhzOS8bQ0FABEgEREAEREAEREAEREAEIJCYmZi8ZRUcEREAEREAEREAEREAEzMHgx44dk2TUwyACIiACIiACIiACIpA9gWzfJXM+MX3y5EmREwEREAEREAEREAEREAEIdO7cWVFGPQkiIAIiIAIiIAIiIALZEzAvv3Z7w9D5KKONr5bXHRABERABERABERABEQhQAtu2bcPzSpUq/SnKaL1w+tSpU/xwxRVXBOjy5LYIiIAIiIAIiIAIiID3BA4fPowR3gtoqUQCiyXK/NGMZFQTAREQAREQAREQAREQgaNHj1oq8fTp0+cT00lJSdDJzMwUIxEQAREQAREQAREQgWJO4MiRI64EzktGE4S88MILizkgLV8EREAEREAEREAEijOBZs2asfzdu3dnLxmLMxqtXQREQAREQAREQAREwBAwBy+mpaVJMuqREAEREAEREAEREAERyJ5AvXr1sv5wPjF9ySWX8LPby2HEUgREQAREQAREQAREoFgRKFWqFOs1R+1YLYjyafNHeHg4FTC1atWKiIhwIJdq1arZ5VWrVq3sMlUc7Nj4PERGRhYHYlqjCFgENmzYUORpHDp0qMivUQv0nEB6errngzXSmQSoeomNjTW+WSoxIyPjvGSkjtqZrssrEShsAm6nlXozXZcuXby53PXa0NBQu0zZa6dGjRr2GrTF2oEDB2yxY6+RtWvX2mXQVCja1dyCB3aZlR1fEqhevbovp9NcxY0A/zVIEYz1371/koy8SXDfvn3650hxeya0XhEQAREQAREQARGwCPCeQBNGbNSo0cqVK03/nyRj6dKlbedlznq0pS1evNgWO7YbWbJkie02vTe4efNm743YbsGt9spL+2fOnPHSgi4XARFwFIGgoCC7/HF7N65dZr23Y2P2wFQgqPmegNvRM944YGP2oFy5ct544notXu3ZsweNOH78+FGjRpmf/iQZs52JHHbBEtaYxmBwcHDBFqB5PeQmzh6CMsP0XHmIS8+Vh6D0XOULlJ6rfOHSP688xKXnykNQ3v/z6nzFdL6m1GAREAEREAEREAEREIHiQ0CSsfjca61UBERABERABERABApI4P8BG7kIDsyparEAAAAASUVORK5CYII=)

