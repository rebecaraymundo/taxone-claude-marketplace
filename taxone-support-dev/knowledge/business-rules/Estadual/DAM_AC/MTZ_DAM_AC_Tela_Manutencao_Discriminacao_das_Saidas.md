# MTZ_DAM_AC_Tela_Manutencao_Discriminacao_das_Saidas

- **Fonte:** MTZ_DAM_AC_Tela_Manutencao_Discriminacao_das_Saidas.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 140 KB

---

THOMSON REUTERS

Manutenção da Discriminação das Saídas

DAM\-AC

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS1680

Julyana Perrucini

Este documento tem como objetivo criar o módulo DAM\-AC\.

Sumário

[1\.	Regras dos Campos	3](#_Toc452646112)

[2\.	Sugestão de Layout	12](#_Toc452646113)

# <a id="_Toc350763252"></a><a id="_Toc452646112"></a>Regras dos Campos 

__Localização da tela:__ Estadual\\ DAM\-AC\\ Obrigações\\ Manutenção\\ Discriminação das Saídas

__Título da tela: __Discriminação das Saídas

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

Os CFOP vem da tabela SAFX2012 na seleção pelo botão Novo e vinculado na NF de acordo com os registros geradass pelo botão Abrir\.

__Tratamento:__

- O campo será apresentado de forma desbloqueada se o usuário desejar selecionar um registro pelo botão Novo \(combinação entre os campos Estabelecimento, Mês/ Ano Referência e CFOP\)\.
- O campo será apresentado de forma desbloqueada se o usuário desejar selecionar um registro pelo botão Abrir\.

MFS1680

Para o Estado – Valor Contábil: 17%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor contábil das saídas, para o estado, geradas a 17% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para o Estado – Valor Contábil: 25%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor contábil das saídas, para o estado, geradas a 25% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para o Estado – Valor Contábil: Subst\. Tributária

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor contábil das saídas, para o estado, geradas por substituição tributária para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para o Estado – Valor Contábil: Outras

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor contábil das saídas, para o estado, geradas por outras operações para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para o Estado – Base de Cálculo: 17%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de cálculo das saídas, para o estado, geradas a 17% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para o Estado – Base de Cálculo: 25%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de cálculo das saídas, para o estado, geradas a 25% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para o Estado – Base de Cálculo: Subst\. Tributária

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de cálculo das saídas, para o estado, geradas por substituição tributária para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para o Estado – Base de Cálculo: Outras

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de cálculo das saídas, para o estado, geradas por outras operações para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para o Estado – Isentas ou Não Tributadas: 17%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de operações isentas ou não tributadas das saídas, para o estado, geradas a 17% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para o Estado – Isentas ou Não Tributadas: 25%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de operações isentas ou não tributadas das saídas, para o estado, geradas a 25% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para o Estado – Isentas ou Não Tributadas: Subst\. Tributária

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de operações isentas ou não tributadas das saídas, para o estado, geradas por substituição tributária para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para o Estado – Isentas ou Não Tributadas: Outras

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de operações isentas ou não tributadas das saídas, para o estado, geradas por outras operações para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para o Estado – Outras: 17%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base outras das saídas, para o estado, geradas a 17% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para o Estado – Outras: 25%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base outras das saídas, para o estado, geradas a 25% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para o Estado – Outras: Subst\. Tributária

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base outras das saídas, para o estado, geradas por substituição tributária para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para o Estado – Outras: Outras

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base outras das saídas, para o estado, geradas por outras operações para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para outros Estados – Valor Contábil: 17%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor contábil das saídas, para outros estados, geradas a 17% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para outros Estados – Valor Contábil: 25%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor contábil das saídas, para outros estados, geradas a 25% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para outros Estados – Valor Contábil: Subst\. Tributária

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor contábil das saídas, para outros estados, geradas por substituição tributária para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para outros Estados – Valor Contábil: Outras

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor contábil das saídas, para outros estados, geradas por outras operações para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para outros Estados – Base de Cálculo: 17%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de cálculo das saídas, para outros estados, geradas a 17% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para outros Estados – Base de Cálculo: 25%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de cálculo das saídas, para outros estados, geradas a 25% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para outros Estados – Base de Cálculo: Subst\. Tributária

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de cálculo das saídas para outros estados, geradas por substituição tributária para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para outros Estados – Base de Cálculo: Outras

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de cálculo das saídas, para outros estados, geradas por outras operações para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para outros Estados – Isentas ou Não Tributadas: 17%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de operações isentas ou não tributadas das saídas, para outros estados, geradas a 17% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para outros Estados – Isentas ou Não Tributadas: 25%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de operações isentas ou não tributadas das saídas, para outros estados, geradas a 25% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para outros Estados – Isentas ou Não Tributadas: Subst\. Tributária

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de operações isentas ou não tributadas das saídas, para outros estados, geradas por substituição tributária para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para outros Estados – Isentas ou Não Tributadas: Outras

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de operações isentas ou não tributadas das saídas, para outros estados, geradas por outras operações para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para outros Estados – Outras: 17%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base outras das saídas, para outros estados, geradas a 17% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para outros Estados – Outras: 25%

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base outras das saídas, para outros estados, geradas a 25% para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para outros Estados – Outras: Subst\. Tributária

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base outras das saídas, para outros estados, geradas por substituição tributária para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para outros Estados – Outras: Outras

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base outras das saídas, para outros estados, geradas por outras operações para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para o Exterior – Valor Contábil

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor contábil das saídas com operações para o exterior para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para o Exterior – Base de Cálculo

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de cálculo das saídas com operações para o exterior para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para o Exterior – Isentas ou Não Tributadas

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base de isentas ou não tributadas das saídas com operações para o exterior para o CFOP selecionado de acordo com o estabelecimento e período\.

MFS1680

Para o Exterior – Outras

Numérico

N

N

Formato: 

Text Input

Default: 

Não se aplica

Permite o usuário visualizar o valor da base outras das saídas com operações para o exterior para o CFOP selecionado de acordo com o estabelecimento e período\.

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

# <a id="_Toc452646113"></a>Sugestão de Layout

![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAucAAALfCAIAAABNTPtfAAAAAXNSR0IArs4c6QAA/VFJREFUeF7snQm8TfX6/3+myEzIkOkiQlHKVAkloZuQJEKZRYiQIWNKpFAqU1QqMkVJVChzESlDcU0pZDhCyND/zeO/7r77TPvsce1zPut1726dtb/D832vZX8/63me71qp/v777/+LZ+Orq666Kr5vEzh+5swZvs2QIYMfdamifn3kJs4+grJiuq58xKXrykdQuq6SBErXVZJw6fcqPlypk8RRhUVABERABERABEQgUgRSma+lXbt2U6dOjZQR6teTwA033JDCgaROHaiY9tvPl8LJJ6fh33nnnQEO5/Tp04G0cOHChUCqUzdz5syBtPDXX38FUl11AyeQMWPGABupVKlSIC34Fy3x7DFVqlSBGHDdddcFUp2611xzDY3YQM6dO3epNVQLW4UKFQJsWtVFQAREQAREQAREIOgE8uXLN2rUKJMrV3wtVapUWb9+fdB7ikiDSLNA+s2TJ08g1VUXAnfffXcgHBLItfKx2YMHD/pYMs5i1157bSDVqRugAQH2Hnj1HTt2BNhI4Df6u3btCtCGFF49W7ZsARII8CReuTMOwIgAb/RvvvnmADq/VDVAh9mmTZsCNEDVHQLPPfdc//79+fOKarnrrrtWr17N3//8848wiYAIiIAIiIAIiEDECdxyyy3ff/89Zrz22muksrBzJYGgSJEiETdOBoiACIiACIiACIiAQ+DVV1+1/Z9//tl2UlugKMC8MyEWAREQAREQAREQgdARMLmSmtRcNq25CB1otSwCIiACIiACIhAIgaNHj5pcuRIhypUrl1dzW7duvfXWW1mFS2YiWS8TJkzYt2+flTlw4MAjjzxy8uRJvy0gh6Zv376JVg+8I88uvvzyyy5dusycOZOHHY0dO5bGEzXAs8Aff/zRvHnzU6dOJamWZ2FE4nvvvffvf/+7aNGibdu2Xbhw4fnz5xNo7bPPPmvUqJFXme+++27AgAF+26CKIiACIiACIhAKAqQ/k0DtueXIkePjjz+O3ReTYIMGDfbs2eP11ZgxY/hq2rRpsascOXLEDl5RLSdOnPAqRAI/q4ratGnz/PPP165de9y4cSwc3759O8WyZMnSsmXLQFais/y6fv36iVILvCOni19++aVx48b0O3z4cKTYvHnzMmXKlKgBngX27t07ffr03377LUm1PAtPmjSpR48eNWvWHDhw4NVXX12vXr3evXtfvHgxzgbh//DDD5cuXTpt2rSeBTZv3uzE+fy2RBVFQAREQAREIIgEkCAbN270ajAmJqZbt26xe9m9ezezcPny5ZcvX+58+/jjj1OYr9hiV/n666+vHLRAESrE/mYNkW3c6PMn6sb+xLOCp6F69eroG6dMFO3gscC5gsHHjx8HkzMujvBVwgNBWIBow4YNANm2bZvfo77jjjteeuklp/qnn35KgywxjbPBY8eOTZ48GbeQ8y1r8DDVHgbIvt9mqKIIiIAIiIAIBJcAKoS5CZHg2awt9Fm2bJlXX61atXJ0yaBBg5ApDz74oHOEP53yzNfO00yu5LXEJ7XSpUvHV86CezwTxHTomwXov//+Ox0QZKIAU2+dOnWqVq36+uuvo6qsNb4aOnQoMgpfggVifvjhBzwHtHD99de/8cYbK1as6Ny5M8efeeYZFmGjh2rUqDH/8kZMhP1FixbxrdPRhx9+OHjw4NGjR9PmQw895LiVGNjixYsfe+wxHBjvv/++s7ae9lkiReEPPviAMjSVJk0a4mE8pgYfDwcPHz7MQeQInij8UWwYHOfDCVatWlWrVi3qPvnkk1bFxrhlyxZUYeXKlUeMGPHnn39yBEmBR4plWnQxe/bs2NGfBx54YPz48XPnzrXgGnE37HEeD+PVYPbs2X/88UeAW8vYXKZMmfz589MFR2xQcQ6fSBacixcvDgFbza5NBERABERABEJKwBwtTLuevcS3PJmIgVMS1UIxEz1s3JkXLlzYsxGvZ7DF++h0Uy2ez9hhaucIIRI2IlW4K3A83H///TxSrGnTpm+++SbhJMqfPXuW+RJp0rp1a6Z8vmLSRWd89NFHiCZCJLgcWMJkgaslS5YgF/LmzUv4icmejVm8bNmyTzzxBNLH6Yj5m4HheyAdhC4QEKYJUCpErwoUKIC+a9asGd1xkI54mDeP0sOeRx99dOXKlRzERUSBt99+u0mTJoihFi1aoD9QPCg+rO3Zsyf2kOzidVIRW7fffjtygbQee2STAUG6MYpDhw6htyZOnGj+D5ggSlBjPGiYZiHg1VqnTp3IB2rYsCFxHwJVMIEGUbD4GkR72VovRBtDxh9GRospJBNPcQ4fFYUAoiTPxUdN0khIr1Q1LgIiIAIiIAIW1vGSKSZN7Pbbc2M+5aCXxKEAvgAn8hMvUnO5MJtaCccts3TpUv5ENzhHzGvy1Vdfffvtt+wQ2vjmm2/YYb4ndfc///kPWsnu/jlI0ij7zOu0ww5OFKtirZHhgTphh7kfxcAcbPkiOGzY//XXX7066tevH0/vRW1QxaQJgJj1eU/HyJEjLXRCg6gH3BjFihVDSVhH9L5//352UCTQxE72zZGDuwWPEW4JeuSgxWtIf/F0ZD399NPVqlWzEBIJJRRAr4ALbxAayIJl2I88si7QK7RDBsy6devWrl0bp/8NCPhLbrvtNlrDgYTIi69BlBxt8m3BggXJLrLWyK2hIpGjOIdPATw6aCkEIgMEO8XiNEMHRUAEREAERCBYBPAdmEDxbDDOg1aA4IxnnMgUCEEGfDaeLTCXEaLhKyIq/xMhih3OMKcCgRVH7/z000/sE3qwG33yhFESODbwBJDfSmTHXnqHqsABYy82yp07N44KLLB2cubMaa3RgiXz4tFhjRJN2dJr3Dnsk6nKPtO50xEZqSTS4pLhuDmL8MR8/vnnNIL3hX5pHwcGwRHW+OzcuRMjrSPiNSyPoinEDQuISpUqxUGymvnEV4TMuummm+yh0ezw6bWwCD8NysaMt6xYxgJTxFDXrl3t3WbYb48/RysgX5BBhQoVIt82drbvO++8Qz4Rogp/DC4QJAXFGEV8DTIuuuPZ8KzewuVjI7KXSEEmzuHzFXE0hk/qMQNnmVJSk46tF20iIAIiIAIi4DsBBAeFYyfkxtkCCaYImtjvbEbKcJxvPWvhsOBP50WM/xMhMrlgm6kW5+27zPG8AuCpp54iHGNigq/effddfCqffPIJ3gWSS3DsEL9AmjCL26tk0BYlS5akjCkDJymExh3V4kgTCjBJO12jFZyO6Mt5N43tIHcQKDgh0qdPz58MkgfloU7QSSTQkDvCQbwsuCu++OILsnOY+J3YmL0jhr4oyUJo68V8S1jrCYs/CU6ZVbg3bAj2RD4LGKH2AGorsHC6oGDwshDWIT714osvep0tAjdICmsN8YGiQveQTBNfgxAAFB1RDFeWtWbJNzQS5/DJ4UWvEJVDupE+TF6LEyz0MkZ/ioAIiIAIiEACBAiksK6H2AKb53pmO9K9e3fPFUAW7vGacUzEeIWNTLI4+oZ9gickgZjuQbh4rZO1Gfa/d+DmciGrlKMstnY8M9ymc4QIBQkrJMzipaBpVAgFnBgN3gImVJI5SPsgknLfffehG+geZwauF55NQowKFwjqwVYkEbOw9qnCcXYYOV4QdkxbkRrCvi3LporTEbkv+G+s7po1a/iWWZyN3slKwUJ65+CwYcMoYOujsBx72EFDcPDll18GHCxwb9hJIikHdwU75iNhh9ccePnK7JSQU0xr5cqVYx8FhsgglYfG33rrLepyEMcSFVF15JFwmhkRDhUnpuO0abE9EpBnzJiBqaTvYLbprTgbpAukD9Uxm/jXK6+8QkTJHEUEwuIcPqeS2BNZOwSSMJuSjNFrUPpTBERABERABBIl4IukcxpxlisjPlALRH+cNc9eHTl6hUkZd4tnC1QxQeMcdIQRaaAmV/7P/mNTsqdqYVI0fcQnGawoA0dzYBxps0y3aBSkCfqDmZIp3FlOzGNdOnToQEW0mPkqcDPgA3DW8eL/wAKO9+nTZ8GCBezgtCBz1rJh8Gcw76JOnI7wnTgiAEcOURumbVMw+EuY/nv16oWrg1iVVcdaLEcKkGVig6c8ogQ7kQJ8e++99xIMoiQFkBps1MUl4wWXAognsCAaECX4MCxLBsOAi5LjxLAOCBcUBxk+WgQvCw9iQc95Llq2ZmkNHUreCWILEUa6Lq4R+yrOBmmNfFu+RdaQ8UPLnCYEHBrLUm3iHD4qjaiZJSNTwLJ2tImACIiACIhAkggkSbXQMhLE/CWeG/N17E7RJV75K/EZ5qiWjh07mly58s5noic4YUqUKOG8oIheaYXPAN8V7suwg16GBJchQ4YgTXgQbeCNM/GzeT3tLZBmAesHVZQKkTInZheIAaorAiIgAiIgAgkTSHieIiSEInHCF05TLAHhPtxiCzhOeMZHIJwJnlgL+DJYx3NJk1iaiOV4kgVi8Zdo30gcJt+YpFccJH7og2gfvuwXAREQAREQgQAJeKateDaFXrHMzjBsjmrhDQAkVyRb1cLA8I7ILRGGS0pdiIAIiIAIiECICKBaeM4Iz0Mhf9SemxrvU+ZCZEHYmpVkCRtqdSQCIiACIiACISJga1Cc7YpqufHGGy85Xi6vT9YmAiIgAiIgAiIgAm4gYM9JcZJur+S1sByGRUM8boS1P5G1MnYGclLtIac4qVWSWXmeqRPIiHhKXiDVVVcEgkIg9lvsg9Js2Bqxh0xoi2oC9s44bREkQGyoffv2ZoCl4f5PNm4ELVPXIuAQsHczBbLxwstAqttTmCO48VzjCPZO1/Z60chuvBMjEAMCFw2eCyoDsUR1/SbgPE7d7xZUMXkQ4FlxPLjE3ir4fzzNlo3XDdqj/rWJgAiIgAiIgAiIgBsI8Lx721hEbXIllb1DmKff2jN07RktgWw8jjeQ6j6+xSCQLhKuG/vtlKHrK86W41tsFjYzAj8FAV4DYRupOhIBNxMIMFwe+4W6YR5s4MF6XmMXZpuTWXc8FjXAEQX4Yx74i/B4G8/s2bMZBU+i56n67FyJEPFs2WCplgAZqboIiIAIiIAIiIAIQICMW96Qww4vtHn22WfZSbYrn3W+RUAEREAEREAEkhkBqZZkdkI1HBEQAREQARFItgSkWpLtqdXAREAEREAERCCZEZBqSWYnVMMRAREQAREQgWRLQKol2Z5aDUwEREAEREAEkhkBqZZkdkI1HBEQAREQARFItgSkWpLtqdXAREAEREAERCCZEZBqSWYnVMMRAREQAREQgWRLQKol2Z5aDUwEREAEREAEkhkBqZZkdkI1HBEQAREQARFItgT0RP9ke2pDPbC9e/fyhohQ96L2RSA+AlyBgiMC4SRQqFChcHYXlL4OHTp05swZ35vKkyfP3Xff7Xv5UJeM/UR/qZZQM0+27X/wwQdSLcn27GpgIiACKZVA3bp1y5Yt65LRS7W45EQkBzNMtXBxZ8uWLTmMR2OINgJ+X3hZs2aNtrHK3mAS+PPPP/1r7vjx4/5VjEitlStX0i8SxPcL/pdfflm/fn3BggWbNm0aEZtjdyrV4pITkRzMMNXyyCOPRKPXNDmcAI1BBERABOIn8NJLL/Flr169fIdE1PXDDz90uWpRNq7vJ1QlRUAEREAEREAEIklAqiWS9KO677Nnz0a1/TJeBERABEQg6ghcUS0FChSIOtNlcGQJkJqOAQoPRfYsqHcREAERiJOApbPYD3Uy2P744w8bRWR8LceOHWvQoMGNN95YvHjx/PnzX3vttTlz5ly0aJHfZInGNW/e3Mf1Xf379//yyy+T1NeBAwdI4Dh58mSSaqmwCIiACIiACESEgKWr+zgtmoXMxXy6fHFo6r8vb2Fm+uOPP86bN69FixbPPPPM4MGDhw8f/vLLL5cpUyY+MxBZXbt2TSB/e/fu3dOnTz98+LAvA0Eebd261ZeSTpksWbK0bNkyY8aMSaqVaGFsXrBgQaLFVEAEREAEREAE/CDgGcrH78Idvm1x+mDSp0/vRxdhq2JyJfVVl7ew9WodnTt3js/HHnusffv2bdu2bd269eOPP07ecnxm7Nq1a+zYsQmIknTp0lH34sWLvgwkbdq0PpZ0WsuUKVOdOnVSpw6ya2rhwoVr1671tPnChQu+DEFlREAEREAERCABAjwvjm891cnUqVNZImQb+ywyevPNN+fOnYsfISoWdZtcCfI07OM1lCZNmvhEBm6Vvn37Ejlq167d6tWrKUY4qXv37uw8+OCDv/32m3WxZcuWbt26Va5cecSIESy+twbxxxQtWrRPnz779++3YqgTGhkyZMiwYcPWrVv3zz//cBCJY+Igzm85fvTo0aFDh5YvX753797Ehjjy+++/0zvHP/roo06dOmHPrbfe+sorr3z77bfYWbFiRURVAm1yieBSGj16NG0+9NBDe/bsoc33L29jxoyhLn+eOnWqX79+KCpaxgeDqRyhU9xIPlJVMREQAREQAREwAhkyZEgUBbMnz2jh/jkqVIsNJzKqxdQD0zORFzJaSG1herbwGyoERTJgwAAcG1WrVl2xYgXBuXr16vFV586dKczOpk2b7rjjDiQkuSwTJ05EM6ZKlYrjMTEx6Izvv//+iSeeYMqnF4QFjfzwww+4NCpVqjRhwgQOmq8lvm/xpyFE3njjDTxAq1at4mE758+fRy19/PHHR44c2bZtG1/xZ7NmzZ5++mn0ysGDBzEPwYSCia9NlOygQYMmT56MYwlx8+STT9LmbbfdVrp0aVw41atXx3hMnTRpEsq3fv36jOuLL74gINWhQwfTy9pEQAREQAREwHcCltfi6WuJL6DB8WhaV2GBopEjRxoL5t0wbEuXLqUvOmUiZ0NMzJo1y5TEAw88wJy9fPly4kHz58/HLcFBpnDKow/Yx9oaNWogGk6cOMGfPXv2bNOmDYqBAps3b+bI9u3b2cfrhfphBx1Ay2w4MPhzw4YNtWrVouv4vl28eDHFvvvuO5rifGMqO9b+jh07XnzxxQoVKpgkqlatGoEtxBaNo41GjRoVX5s4UapUqYLDhlooIZrCg8I+2ouEHnbQQ2azwUfiIGiIo4XhXPjdBfqSze/qqigCIiACIhA6Asye/ETj0Xe6YCKz322vzaZO29z2w75z504TJ7gtruS1+C7cgljS0kpQJzhF2PBANGrUyPwlhFEIDzVu3DhXrly4rUgo4aBnGsrGjRtREvg2MmfOzFfkPCMmYM2+Zctef/31tLxmzRqcLvyJuwK3DRtChz85aB3F9y2q4v7770eaUCZ37tzkCNO4GUBFQlEsJ7OO6JqAFOlLHM+bN+9ff/0VX5t4d6677jrKUOuaa67hk2ATn/hdzBgEGZ8lSpQwyEgcBFAUueyCeG2oKREQAREQgVAQYN1u7HxbHC3ueeuQL6OOZIQotn2ksKBXCMogr3CKkJLCUiOKXX311TbH83n69Gk+zfdFnAUHBk4XdvjTYkwUI6+FWJIpHmTQzJkz0Zv4WvhEkeDDQMTE9y0VkUG2rgptUbJkSfwuplqohWrxTJh19rGKdJn42qSis1DLdix9GAVjliNoEGFfffWVDerTTz8l6mThMG0iIAIiIAIikFQCsSNESBZeS+TZTuwjSe0l/OUjo1pMBCAjpkyZQlbKO++8M23aNBYKMXPjlnj++eeJDc2YMYP8FYvDEXLjq3HjxvEiJVJJeI82vhbiSgRoECUUMClAcsz48ePJ0sUZw7mpWbMmJZcsWcK3tIMawGtCmgjihl7i+5YQFZ6PRx99FPPIyc2XLx+P4DNfDn4RZIpl/rKRzGyag41zjxiKr01Ui6NviC5R3vQNqTZEhWbPno3/5tlnnyUNmTxfnmRDfi77FPj888/9ftFX+C8m9SgCIiACIuASAqZavB5ijkffIgk2beEj8PstpJEaZmRUC0EcXFKkpNiaZx6F0qpVK5wreCDQCqDkK1I9iPKQg2KqZc6cOSwCIt+FvGhSYUqVKkX6KuKDbJLbb7+dUA5prQ0bNiRhBfVDSdon1ZdaqBA++Za3/VGe1oi/UD2+bwsXLky/NMjD6JAp+GlIFmYjSTZHjhxEr0hnsbOFfmIgtl+7dm3KxNcmxtCplSTyhbqyHNsuXbrcdddd2EweMWKLseBlYfi8q5NEGcQWucbOAwEjdYmoXxEQAREQgWRDgJt5piTmIKbdaFztkcq8FKy/5YFv7JhTITybZ1+W3pHwRvlEi8VXJuG6vrScmHXe3/vepu8lk2pDSMv78ULRkNqjxkVABERABDwJJPVXGscMYoAWkvSm6JAyJ8BSrFgxuiAb10IrkfG12CCRIM7my7ATlSzWZpxNJVzXl5Z9sdCzjO9t+l4yqTaEtLyJdJ6xGNJe1LgIiIAIiIAfBPx4wa2tC0ngia9+mBH0KpFULUEfjBoMJwGXP/s5nCjUlwiIgAi4jUBUSBA/oEm1+AFNVURABERABETA1QT88LW4ejz/37hI5rVEBSAZGR8Bspt5NSjLpgLM5/I7g93vijqnIiACIpDsCbCqg43EWx8fx8J6VSL+PMmdCBFri1zCJ3Zei1SLS05N9JnBmm1eYBF9dstiERABERCB+AkQ/efZIi4h5K5sXJdAkRn+EUC/I8mdjQvdv82/3lVLBERABEQgEAKeP+C2z9NceJKI15PoAukiFHXlawkFVbUpAiIgAiIgAiIQKAH5WgIlqPoiIAIiIAIiIAKRIqA1RJEir35FQAREQAREQASSRiA1L+Wxlw5qEwEREAEREAEREAF3EjC5Il+LO8+OrBIBERABERABEfAmoGxcXRN+Eti+fceBA4eoHMZXV/lpapzVYmKO2/GYmD8DaTdDhvRUz5s3j9fLJDhSsmTxQFpWXREQARFI4QT0vJYUfgEEc/iDB48KZnPJri3UTO/eXZLdsDQgERABEQgfAamW8LFO9j1NmzZj9+595cuXidJn1JqPxNwkgZws89ngsPH0tSxbtoqDAwf2DKRl1RUBERCBFE5AqiWFXwDBHL6pllatmhQuXDCY7SaLtswRJdWSLE6mBiECIhAxAnpeS8TQq2MREAEREAEREIEACWgNUYAAU251HC2Bh1dSLj6NXAREQAREIOkEXK1aeNH2kSNHkj6oZFLjwIEDFy9edPlgePeQyy2UeSIgAiIgAsmGQGRUyw8//FC7dm2vNwajUTp16jRv3jyDe+rUqXbt2t16661ffPGFL7j/+eef9957b8+ePXEW3rhxY82aNf/44w9fmkqgzKZNm/7973/fcMMNxYsX5xVTAwYM4L3eibY5ZcqUe+655+jRo4mWdAp89dVXvMgKILw93PdaVhKt0759+y1btiS1otvKc06//nr1oUOH3WaY7BEBERABEYgIgcioFtTD4sWLmVmPHTtmw2Z+GjNmzBtvvLF9+3Y7wv7vv//et2/fWrVq7d69O1E65Ow89thju3btirPk9OnTly5d+sknnyTaTsIFaGHfvn09evTo378/QmTt2rU33njjBx98kECtrVu3tm7dOlOmTGnSpPGxdwb+0EMPjRw58tdff3355Zd9rOUUS5UqVaNGjQoUKJDUim4rz/Ngli5deehQoFrTbeOSPSIgAiIgAv4RiIxqyZgxI+YiI/r163f+/Hn2cS307t2bHWdqb9CgwahRo6pUqbJhw4b8+fMnOrwvv/yySJEit912W+ySODnefPPNzJkzT5w48dy5c4k2ha8CFRVfMXpp06ZNq1atnn766c8++wxdNXz48ATK44zhDeCzZs3yfYXwNddcM3/+/OrVqz///PP0lajBXgVQLffee6/v3SW1fStfpMilpUN79lzKbgnR9tNP29KmTVu8+L9C1L6aFQEREAERiC4CkVEt6dKlA9Po0aNxqEyaNOnw4cPdunXr0qULGiV16ksm/fXXX++88065cuXwZDRv3twJEiFxxo0bd8stt9SvX3/27NmmeNjYmTp1Ks4bXBqxT8Dy5ctPnjyJZFm9evV3331nBT788MPBgwdjQ/ny5XFsOKGlVatWVa1aFd3QoUOHvXv3erWGeU6nfIW+IZJ1/fXXWzFiXjSIjlm0aBEBL44guXDM4J5p3LgxFXmHwscff4xWYxQ4h6xW9+7dBw0adP/991esWBEvi9V69tlniUNhG8LFPFIEpx599FHMJtR15513fv3111YdwYRiw7nC8QULFvDnhQsXEFU0YgUIFYG3cuXKI0aMsHgTjqIlS5bEBuWqI4xi48afypYt5TxYxVXmyRgREAEREIHwE4iMauEGmqHWqVPntdde69ixI1MsMzpTKWrG8k/Hjh3L9I+/AUcFqqVevXrLli3jOFP++PHjO3fuXKFCBWohegzZ5s2bUSTkysQmSIOklSBo0A133303WsfK0DJaYfLkyW3btmWCfPLJJ7EBmYJ6QCsQnUHHoCe8Xi2J5RynwQkTJvTp0wf1QAvoLdwbuI6QL1i4f/9+hkZdtBeOGbQI1pKjg5uHUBHDIc2WiBUSDYWEJZiEfipbtizaArWEDQ8//DB/IlNok4wcLPz77785TiiKfUaBS4l2iB9RHTcVsapcuXKhSx544IHPP/8cm6dNm2aSi0buuOOOQ4cOUR7dhrbjIMXKlCkT/qstST3ixTl16q8bbyyVpFoqLAIiIAIikJwJMB2yMUnbILlTD8PGTExfJHzQ9eOPP86+OQlq1KiBJcePH8+RIwczK+6Wd999lwm4VKlSzZo1owBqBgXw6aefMiWvW7eOtBKz9oUXXkAEIAtiG29JqU888QTuDTw0xIkQDRTD4UEVfBvsm3ogewYVVa1aNdwnHLQUmblz53q2SdDK62p45plnKHD69OnSpUsTzUExoJMYYJ48eZAIfIWzhLGwM2PGDOqiriiAJ4aKaBoGyyfuGQtLsaEtKAYHhk9+ca9evfiTwaLhbIcyltgLB/QW0JBxNEgLeJUOHjxoDhXymsHLt6A7ceIEtXr27ImFwTq/U6d+OGjQyN279warQa925s37bOTI15GSIWo/pM1Chv+FtAs1LgIiIALJnsDOnTttzmWaM7kSGV8LoDEC/wTOlZdeeonZF+cERyw8xEROTARNw1fM2XggcCpYagsOA+Zd5vhChQoNHDjQ4kEoBsJMLVu2NBeO18ZEzhGyaF9//XVzTli8icLXXXdd3rx52cfDwSdSAEA4WiztBjFRqVIlgjueDWIzWgcLmU3RB2gLNvQNsSHkEWZkyJCBUdAI7g08JdRlbTCigR1zF1kUjINURCdRkSokvtCydYSo4tMCWKTO4FtiMREmWcYP+3yi6vgkqRn1Ri9NmjS56qqraAG/Dq0ZXnpBPPFt165d0Wocufbaa3fs2BEbkQuPnD37908/bed1Ab6nMLtwFDJJBERABEQguAQio1osDGQahdAGS4idyYmpFyWBQwUnwffff//bb78hJpj1UTAUxlvA1Iu/4eeff86XL9+LL77IQVJVUBuUj40GVwTeGiJBKAxkECWZwtEWHKd3VJtVsR0kVMmSJZELtkCa2Aq+HHJrPJulFhZmzZoVg/GmEN4qVqwYquvqq6+mGI2TdUschwAQm7lJ+MpcI9mzZ0dt8C1Ol/fff58CxIaIBKGfPHNlrEfSh1EYmM3YGSwBHZM1WM6n5RRjMHKEDYVkRhK6wiQrg4XoOXYsLZcucCyZfnL/tnPnLsZ4ww1XEobcb7AsFAEREAERCAOBK6qlcOHCYejM6cKmVVMtnhsTFVM4kzE6g8QREjiYvF955RUiO8zflMTjQowGYUH6CE4U8lU5SOrrfffdZ04Irw2lQvSHdpzjpK3g88AJQe9mBhshIT7x3ODyYbJv2rQpggMZROoM7hbPNj1rWRXKID7+9a9/sQZq4cKFKB7kFK4RDMZbQxnECgII0dCiRQscIfSOo4VlyTxAj5Lss5l3xDasZQUQvRNCIjpGQgwyi+OOM4Z9Mmb4zJIlC5oPU/E/WUTp1Vdf9TQY1wutoaWASSSOVCHrYv369fE92CY2w4gc+fHHbTlzZsuf/5InTJsIiIAIiEAKJ2AagC0yvhbmbJbD4KvwOg08U86ECNoCtUHOKctemLlZHWMOA1JcccyQBsvcj5pheQ4HSekg4uU5qTvNIjKQIDTrHGH9EfM32ggnB8EaO87c/+CDD2IPgSc0EDu4T4hD0YXXs18xj+fHeJqN0EG74D0aNmwY1rJyh1zaIUOGIFNMlpHvgupCl5Cdw6AIBiG8yC/G8WMhLTSKp+RC8Xz00Uc0heRiXCi5m2++mWIoSxKKLdaDVSwaslqoFsQKWSwkwSB0eDAd9jBqOkIkkSxMvwyEvuj39ttvpwpj/Omnn9z8bwB6VatWjPOcutls2SYCIiACIhBSAqksOMKcx1zLjudNf0g79rFx7HH/1OVlpC82+1LGTodrh693PidwDeudzz7+A1cxERABEUiAgPPOZ27aSaugZGR8Lb6fJNfO2Z5D8DLSF5t9KUMXPhbznadKioAIiIAIiED0EriUkeokpUbvMGS5CIiACIiACIhAMiZwZeUzK2bZkvE4NTQREAEREAEREIFoJ2Byxe0RominLPtFQAREQAREQASCRUCqJVgk1Y4IiIAIiIAIiEBoCUi1hJavWk+BBOw92Hnz5k6BY9eQRUAERCCkBNy+8jmkg1fjgRCwlc+VK1coWbK4ZztFihT0r9kzZy69JZvtwIErj/r1r51I1fr/r2S4ZP+iRUvh0LJlk0gZo35FQAREIBkQiL3yWaolGZzWyAxhxIhxjs6IjAXu7lWqxd3nR9aJgAhEAQGplig4SdFi4vbtO9asWZ89e9Zjxy69YpotJuY4n8ePX/nT74EULuynt8bvHoNS0fG10FqGDOlLlSpRrlyZoLSsRkRABEQgZRKQakmZ512jFgEREAEREIHoIxB9z8aNPsayWAREQAREQAREIDQEtIYoNFzVqgiIgAiIgAiIQLAJSLUEm6jaEwEREAEREAERCA0BrSEKDdcU0CrZuLZE+Z9/wjRay/aNiUk825dk2Lx581DYyZDlT88V2uE33g9GGO8jWyPjI5yELQGdFfACaEcchlEB0A/mqhLtBJx/C3EOxJdfj2gn4PwTjj0Q+0cd3xbfr2VkgSgbN7L8k1XvgwePiqLx8C+5d+8ujsHRZbxLOHsyFECXnBSZIQJBJ+D1axn09pPUoFRLknCpcEIE7Clz5cuXyZYtW3hI2T1EwrcLZgn3W3ZTZXcPy5at4nPgwJ6OneE33g9EvvtavBwkfvTlVPFy2zi3X14MowJgIBxUN0oJJOBp8PHXI0oHHvufcOyBJOxqiu/XMrJApFoiyz9Z9W7zVqtWTdz/eBVzDMRWLVFhvEsuGi+GUXT2XQJQZohAVBCI/WsZWbOjZuXzP//8c/HixQsXLvDJvhc1DkaWo3oXAREQAREQAREIP4FIriE6c+bM1KlTH3744euvv75nz57btm2z8T/11FOpU6dOkyZN2rRp+WR/zJgx9tX69etbt25NSKJq1ao9evTYvHmzHf/uu+8ef/zx2rVrly9fnp1Fixb9/fffcdJ86623xo4d63z1448/9u7dm1p169Z95513zp698iocChw6dKhZs2bLly+Psx20VJcuXRybKbN79+7p06d7FR42bNj8+fM9D37yySeDBw+O3SZNNW/ePLbZdPTee+/t2bPHs8qcOXNuueWWokWL5s+f/6GHHpo7d+7x41fyMYN1DQ0dOhQgCbSGo4VvfYnXBMukILYT1cYHkYPfTQmg3+hUUQREIBACEVMtf/755yOPPMLE/69//atr164bNmyoWbMmnwwGzdGiRQumakQAn9OmTatevTrHV65ceeuttzKvv/766x06dDhw4MBNN93EQb5as2bNl19+WadOnaeffrpw4cItW7Z87bXXYnNBWCCP8uXLZ18tWLDgxhtv3Lhx4xNPPFGuXDlq9enT59y5c/btc889t3XrVlqLk+9ff/1FFxRwvp0wYQKmenmGsHbkyJE4jawYjQ8fPjxOX5GJnhMnTnh1h3/sscce27Vrl+fxH374gT+xduDAgcWLF0fJAROkgVwKXnWRRM888wyQE24zfforS06C2HXYmopq48NGKYGOBNANZ0E2iECKIpAahwdb+MfM5L1ly5Z169a9+OKLTz755Lx58+6+++5x48ZhybXXXouGwM/x6KOP8omC4U+MxLnSq1evt99+myNsU6ZM6d69O9P2+fPn0RA4bLp168bxQYMGvfnmmxT2mulpefLkycWKFcOtwv7PP/+MTDFfCN6dF1544fPPP3/11VdNELDVqFHj9ttv//3332OLDMRHqsuZS85XMTExdEqDdtzZatWqtWLFCkfc4CtavXr1gw8+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VomACIiACIiACLiBgMkVPWXODedCNoiACIiACIiACCROQKolcUYqIQIiIAIiIAIi4AYCUi1uOAuyQQREQAREQAREIHECUi2JM1IJERABERABERABNxCIAtVy6NCh9u3bN2jQ4MYbb3zwwQffeecdHgwSBnYXL17s27cvnV5//fWFChW69tprs2TJMmzYsGB1zcsTunTpsm3btmA1qHZEQAREQAREIHkTiIIn+q9cufKOO+7o169fiRIlYmJi3n777VKlSk2bNi19+vQhPTeHDx/OnTt39+7dS5YsmTp16lSpUvFZrly5ChUqxNkvKmfAgAHNmze/4YYbfDHs1KlTmTNnnjNnDoLMl/IqIwIiIAIiIAIpikAcz2tx//jPnDmDkZ07d27ZsmXXrl0/+uijGTNmLFmyJFiWX7hwIc6mzp8/z/H7778fT0/btm3btGnzxBNPxCdZKHny5Mnhw4fv2LHDF8POnTuHDKIkWsfKs6NXV/qCTmVEQAREQARSLIEoiBAxwXN60qRJYycJ/wcuimPHjjHHL168+LHHHqtZs+b777+P+CByVL9+/eeff56XQz766KPogC1btnTr1q1y5cojRoz480/v957g7cCFkzZt2ltvvXX69OleogHPiqeq8LxEEDTjxo275ZZb6G727Nmmb/r06cMn0urrr7+2wn/88QfG3H777Yit3bt328Fdu3ahgVh0fs899/CnaaZVq1ZVrVr1mmuu6dChw969e1Ps5aiBi4AIiIAIiEACBKJAtZheITA0derUMWPGIBRy5MhRrVo1lErt2rULFChQvXr1Zs2aMfET05k/f/7YsWObNm3aqlWrzZs3E1oiLYaozcSJE6nuBeKVV16ZNGnSm2++SZuU+eKLLzwLmIihZdJZcubMmT9/fsSNuVI+/vjj8ePH4/7B9UJHb7zxBgf//e9/84kiIQ+GnaNHjzZs2JCS6CqSV0hh4SARrsaNG6Nm6JeMGY4grZApeHTKly8/cuTIPXv2EJMy95I2ERABERABERCB/yFgj8hlsrejTNVu27788ksMy5cvH2Ll3nvvRbjgrmB2x+PCNI+vAldHnjx5ECU7d+6k5Lx58xgCg6pRowaa48SJE/zZs2dPQjyeQzty5AiF586dawcHDRpUunRp/DpOmd9//50CaIjJlzd0D8oJdw4FEEbolU8//RTBsW7durVr13Lwt99+o/zSpUuthaFDh5YtW5aYHPuzZs3iK1w7M2fOZIdaHDx79iz777333muvvYYI41sOMjRPq9x2LmSPCIiACIiACISNgE3rbIRQTK5EJhuXrNVEF+OYq4ONgMtdd93FTH/ddddZLggbGqJ///4///xztmzZ+BOBUq9evYceeqho0aKrV68mJPTtt98ySCTFbbfdRoFRo0YhMpAUjmTbunUrMuXHH38sU+bSK7kJNuG5wVtDmMbKHDhwAKn01Vdf0bhTy3aIT5Fbg5Nm06ZNderUQTzRyP79+7Fw2bJlWIu4YR9fDlKJ8jRy9913I2uQVgzns88+4yBeFtxIpBVv3LgR7YUas8YxHrFlvhk2Z8heNiTwJwP3vXCUlnQuj6Ta7yQSJbWiyruHwJ133umfMenSpfOvosWL/di4ufKjFlViR7T9a0e1PAlkzJjRPyA2j/ixZciQwY9aVPF7uQn38P71iF+AqIKTjOFfI0GvFTsb9/8i4mtJIKfVGbMj5VhDxEGcEJ7iDkFAI6dPn+YgYZdKlSohg3DAUHLFihUcXL58Ofvbt29nHw/K008/TXnPFojg8IOC18QKPPXUU+geS4m1zct34lmXtFzW/uAsQTaxT3SJb4n70CNhJvYJS7FPyovVImmGPxFeBIaKFCliDhucKxxEx6B+uM6owkEUDAcx3uku6BeBGhQBERABERCBOAmQiEl8I2yulEQ7couvhQSR9evXJ3zRODfT+EsQJSSUFCtWzKmCiLnppptIuSUllgQXHBiolhYtWvBglW+++YZ0FlJDSBbh1op1xRwhEINq+e677zw7ZcnPCy+8gDuExj/55BPkESmxTgHznfTo0YOVzMhPu9kiZwVfCL4i3CesLUJqoDkQLjzZBcXDLSDOnieffLJKlSrPPfccy506deqE+nnxxRdNtWAPjhDMw/VCcAr3z5QpU9inTRw/jAVZQ5INbTpCm7En439dlgzkx+b3Kz8PHjzoR3dU4YE9/lX0u0f/uvO7Fqnr/tX12ytALpp/PaaEWpb35sfm9+Os/F4HYA5vPzYy//yoRRXuVP2ryK+ufxVTVC2yLJiGXDJkt/hanJhLojrLfB5c3FymXoXXrFnz8MMPkzvSq1cv0lY+/PBD1h7zGDokiJVk2Q4LiHi4CwmzRIjwpni1gLcDfcBjYBo1aoRk8foWVwqteZ25Z555hmLkxCCSiB/hniElCIVkdXHtoJzojn1+O+j05ptvRjyRrnvffffZuidiUnZBkLfLiiEUFQeJNJFBjHAh2GTFtImACIiACIhA2AgwXdp8R/5D2DpNtCO3+FpI2iAFFTqOQ8Ulsi62GV4W+pJlQpVEixGY89tb4FpWMkwEREAERCBKCThejcGDBxMrcMko3PKUOR6R4hIiiZqB/vDcEi1PgUQlC2UkWXwhqTIiIAIiIAIi4EnAz8R4QRQBERABERABERCBMBNITU6GnmkWZujqTgREQAREQAREIEkETK7I15IkaCosAiIgAiIgAiIQMQKpeQaO34/BiZjV6lgEREAEREAERCAlETC5Il9LSjrnGqsIiIAIiIAIRDMBqZZoPnuyXQREQAREQARSEgGplpR0tjVWERABERABEYhmAlIt0Xz2ZLsIiIAIiIAIpCQCkVEtBQoUSEmQNVYREAEREAERiA4C9iZg126RUS2uxSHDREAEREAEREAEXEtAqsW1p0aGiYAIiIAIiIAI/A8BqRZdECIgAiIgAiIgAtFBQKolOs6TrBQBERABERABEZBq0TUgAiIgAiIgAiIQHQSuqJZff/01OuyVlSIgAiIgAiIgAimMwNatW23E8rWksDOv4YqACIiACIhA1BKQaonaUyfDXUDg9OnTffv23bFjhwtsSbYmTJw4cdGiRcl2eBqYWwn8c3lzq3Up167IqJbChQunXOQauVsJHDx4sHbt2lu2bEGF3Hrrrddee22WLFny589fsWLFb775Bqt/+eWXhx9+mOPt27f/66+/OPLRRx+98MILqVNH5t+RW0F624XmAOydd945Y8YMZxpgv2jRouDNmTMnnF999VWqHTt2rE+fPhCuUaPG3r17ObJp06Z27dqdO3cuWgbr2Pnzzz/36NGjTJkyDHzUqFE2nPi2L7/8kgspKGP8888/69ata1RTpUrFDjzhvGbNGqf9ixcvcg1zqWNV8+bNz5w543fXZ8+enTNnTkxMTOwWDhw48Mgjj5w8edLvxiNVESzPPffcv/71r9KlS3P5cQFDLFLGhL9ffgnD36nvPerX1ndWKpmcCRw/fnzMmDGLFy/+7rvvcufO3aJFi379+g0fPrxly5bffvsteoVfdvYvXLjAwa+//nrWrFn8KPfv33/kyJH8uiVnNIGNbfny5XXq1EH51axZkznM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kS1bNpMr8rWEGrjaFwEREAEREAERCA4BqZbgcFQrIiACIiACIiACoSYg1RJqwmpfBERABERABEQgOASkWoLDUa2IgAiIgAiIgAiEmoBUS6gJq/3kT2DixImLFi1K/uPUCEUgJRH45/KWkkYcHWONjGopXLhwdOCRlSmJwMGDB2vXrr1lyxYbNEKEP++8884ZM2Y4P17Hjh3r06fPtddeW6NGjb1791Js06ZN7dq1O3fuXHSh+vnnn3v06FGmTBkGOGrUKBtLfNuXX375wgsvBGWAf/75Z926dXPmzJklS5ZUqVKxA8z8+fOvWbPGaf/ixYvt27fnRGBV8+bNA3mg1NmzZ+fMmRMTExPb+AMHDjzyyCMnT54MyrgCaWTr1q233nrrDTfcAIq77rprwoQJ+/btC6RBp27//v05d743Bfl33323YsWKo0eP/uuvv55++ukdO3b4Xj3ZlOTCe+655/71r3+VLl2af938FEAm2Ywu0YHwS5homQgWiIxqieCA1bUIxEng+PHjY8aMWbx48XfffUeB5cuX16lTh5/vmjVrMrd98803VmvEiBGUGTx4cO7cuYcOHXr+/Pnnn3++fv369913XxSB5VcJm/fv39+3b98HHnhgwYIFt9122+bNm+Mbwk8//fTxxx/7OMD169cPHz48vsKZM2dGiKCThg0bRpnWrVujh1588cVixYo5VVAzjRo14gnau3fvnj59+uHDh33pOs5+OV8tW7Y8cuRI7BaQTXyVMWNGXxoPaZldu3ZhfJs2bbiWEMrjxo2rVKnS9u3bA++U6RZJ5Hs7e/bs6d2795NPPvn5558XL16cughK36snj5K//fZbw4YN+QV49tlnBwwYkCNHDn4Kxo8fn8DoeJhs165d+Q1JHgTcPoq/L28jR440Q80nFupt5syZ4ewu1MNR+9FOAMdDwYIF7ZrkThctUqJEiSFDhti47r77bmZW27///vv5LePenZ2ePXtaYOjbb7+NLgJffPEFZvPrbGafOnUK1YWCiW8U/GSXK1fOxzG+9dZbwEy0sHl3kIMJlFy1ahVlmEoTbY0Csfvllw318+mnn/pSPYJlPvvsM4aJtDIbcP8g7KpXr37ixImkWsWl61kF9YMW970RHoxx6NChZcuWvfHGG1zz6EXf6yabkjhTgX/06FEbEV6WadOmobZxgMU3xrVr13IG8UtF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/vz5Rx555Pvvvz927Fj37t058uCDD+KnmTFjxlNPPdW6deuiRYuuXLny7NmzU6ZMqVu3bpMmTfjT2sQ307dv3+LFiyOMVq9ezZFt27Y1atTo3LlzukREQAREQAREQATcScB1qoXH80GqbNmynrx4cGq6dOliYmL27du3ePHiv/76i2///vtvBArl+bZevXoc6dy5c86cOTdv3oy35syZM0SXyIzp3bs3waN7772XYvfddx96hZIjRozYsmULBVKnTl21atUVK1bkz5+/Y8eO9OLO8ySrREAEREAEREAEXKdaTp8+zVnJnDmz57k5ePAgDpXcuXPbt5kyZeIzTZo0fF64cAHlUalSJfZ559OlF0KmSlWtWrWJEyc+8cQTmzZtGjNmzNy5c7t164b/5uTJkxZm+uWXXwhC4Yx5/vnn58+fX6hQoaxZs95zzz26IERABERABERABFxLwHWqJW/evMDavXu3J7KlS5fmyZMHB4ytJCI2xKc9YNeOeK4wQs1ce+21GTNm5Pi7777bvHlzkyP2phvUD5+jR48mPNS4ceNcuXItXLjQZJA2ERABERABERABNxNwnWopVqxY9erVR40aZW4Vth9//LHP5Y3oT5EiRThCcIdPHDB8msfl6quv5hO/C5+4XggeWV00Sr58+WzfYkNkrnAQvdK0adOdO3du2LCBvBYyf918kmSbCIiACIiACIjApSnebRRQIS+88AIJK3fdddfUqVORL4R77rjjjg4dOmAqqqVLly6kqrz22msk0nIkbdq0fBLiIahEOgtpLqgWky9snTp1Gjly5NChQ3GukMZrBylJLYsN0RFRpIIFC546dYqnwuihdm67HmSPCIiACIhAeAgwe9KRy58h4jrVArLKlStv3LiRz6effprwzeuvvz558mTzprANHjwYZwwH69evTxIuuSmmWubMmbNu3Tqe8kIgqUqVKlaYB73MnDnzq6++mj17NlqHRUa4Xki5nT59Og/h7tmzJ0uW1qxZU6tWLdYlTZo0iQVH4bk41IsIiIAIiIAIiEBSCVwKpjjxlKRWDl35cuXK2fNXEByEchzJQo+siMZxsnXrVrwvCxYsKF++vJmB8liyZMnjjz+ONGFVsx3Ec0MwiLQY1jyzkoi03JtuuonjJUqUmDBhAsukSdolk5cUGSJTs2bNIpk3dINSyyIgAiIgAiIgAv4R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iYAIiIAIuINA6jOXN3cYIytEQAREQAREQAREIA4CJlfc5WshIYjlRX/++d8nW5w8efKRRx7ZuXNn7BH079//yy+/9O/cXrx4cfHixe3bty9evPhjjz3mdzuxez906NC8efNon6/27t3bvHnz2KLwrbfemjt3Lk/6Y7CU8W8IyaCWra85fjxpDzJJBgPXEERABERABPwjkDrD5c2/yv7VSqC7VKlSscJo9erVTsvLly+fMWNGnK8aWLRo0datW/2wAUkxZMiQ2rVr86yaHj16pE6d+p577nnnnXeS2tT06dMXLFjgWQsh0rZt2+HDh58/f57ju3fvpszhw4e9Wr7tttvKly9/9OhRBpuSVYtltDiLeJPKX+VFQAREQASCS2DPnj3BbTCIrZlccZevpUiRIg888MCnn35q4+SBLu+++26bNm04HnvkadOmNZeGbZ77CWOaP3/+4MGD8YhMmTKlY8eOfI4cObJly5bOaw5oypdnyfAc4bVr13r2xTu+UULvvffeVVddxfF06dLFadgtt9xStGhRJJqNMYgnVU2JgAiIgAiIQDIm4C7VwkTOI27efvvtI0eOAJ2AEY4WjrC/ZcuWbt26Va5cecSIERZCQhNcuHCBHdwVhFrwx9x///1r1qzhyA8//MCRvn37Xn/99W+88Ybn+UOREKDp169f/fr1TTdQsXv37jt27MiUKRN/rlq1qmrVqrzioEOHDuYI+fDDD1E5o0ePxkHy0EMPmRR9//I2ZsyYsWPHWvvnzp1buXIleqV3794WcjIXUdeuXdEoffr02b9/v5UcP348agwfD/sMYdu2bY0aNaJ6Mr7ONDQREAEREAERCJyAu1QL46lRowa5LCtWrGCfuT9fvnxVqlTZtGnTHXfcQcoIaSITJ06cOnUq35qv5ezZswRlcHKgda677rqmTZsiNRAWBF+ILhEAoqInpoMHDxJaqlWrludB5EWxYsVMACF9UCd4X2gENUNWyo8//jho0KDJkyfTESLjySefJABElKd06dK8ual69epUtKgT5t15550FCxYk5ERTpopiYmLQMd9///0TTzxh7pxvv/32p59+MtWCryV//vy4fMwxo00EREAEREAERCA+Aq5TLQUKFGjXrh0uFnwPFsEhjoV6qFu37oQJE3ixU4MGDTZv3sx4mOaZ8tevX09eLVKmVatWr7zySqlSpRznCqkq5NveeOONnoO3jJM4E2U4Tp4K5XGrtG7dmnbmzJmDxOE4ygkJhV7p1asXASy8JiVKlMiZMye+n5tuuokCeGiGDRtGjm3Pnj3t3ZCOauFNVLht+MTOJUuW8BU2IFmcCFHWrFlRObpGRUAEREAEREAEEibgOtWCuYSEPvjgA7JDyBpBrGzcuHHp0qXEWTJnzsy31157LdEcdmzWt7CLJb5cffXVuDpI0TVRgqqIPXhUEe4c3DCeX+HFadas2bFjx1ishKMlY8aM1malSpX27duHUwcvTt68eTlI5IhPEmn5xO9iNrDh2sHvQlIO+6gQK2M5K9YasSo8MRbAwjHjqVp0jYqACIiACIiACPhCwI2qBccGQRbiKeSXlCtX7vTp04zEXrCHl+L3338/ceIE+zhjmPspyb4tOyIWM2vWLESJiYk483OpwguvX375ZXPY2EZ+7meffcZOyZIlyWIh3sQ+YSlkEwZQxd6MzWY7Fs1BwZjnhu348eMoG+vXknIwz761lc9IHASWCSm+clKJ4/P6+HLyVEYEREAEREAEUhSBCKiWX3/9NWHEZMUSEqIMeSTM7hUrVrz77rvxtRAhevzxxwnfWHXUAN/efPPNZKIQ0CH3tmbNmigV8nAdF0icHZH7QlLtXXfdxRNf8OgMHDiQjoYOHZojRw78JcgIChAJQv0QdcLdgmqxtF82S0yxvF2+IiQ0e/ZsvqUkUaoBAwYQCbr33nutsEmcBx98kPRbUonxGOE64ghGYqG1SXe0SRxKi4lS1D88DVYEREAEXEjAv+eJhHMgEVAtvgyPJ8uxxsfmePJayIQlYYW0FWTKqFGjbr/9do7jkuEgz4NHLrAGh6AS4SFkBAm8hQsXJsxkEaXYG1Vo5NVXX92wYQN5M2Tdkr/CDiULFSqEgMiTJw/JK8ggeqRw2bJl6cvayZUrFyqEAux36dIF6UPeLj4ednDYkGbL4iCSaYg3EYrKnTs3Mqhhw4aU2bVr17p162iKimTD3HDDDZhXr149fEUHDhyYNGkSacW+kFEZERABERABEUixBFKZP4BgB2EXplieQRJqFmS5durUiV7c4F3AhoQdM4nS8KUFX8ok2lHyKzBt2gxeoNiqVZPChS+F+bQFTmDw4FE0MnBgz8CbUgsiIAIphwDPGbGFtFmyZPF8PH3ECTiGkdrB7T32uNTXEjZSAUoW7PSlBV/KhG3I6kgEREAEREAEopRASlctUXraZLYIiIAIiIAIpEACUi0p8KRryCIgAiIgAiIQlQSkWqLytMloEYhNYM+efRzMmze34IiACIhAciWQ0rNxk+t5jYpxWTZu5coVSpYs7mVwkSJByM89c+bKsqwDBw5FBRBPI+35hb6/W5PyDHPRoqWga9mySdSNVwaLgAhEkABJr9WqVbOntrphoYyDInY2rlRLBK+TlN71iBHjHGGR0lkEb/xSLcFjqZZEIKUQkGpJ6Ey7auVzSrkkXTnO7dt3rFmzPnv2rMeOXXqJN1tMzHHbOX78ypGgGB6NK6v98LXAKkOG9KVKlShXrkxQuKkRERCBFEJAqkWqJYVc6hqmCIiACIhA1BOIItWibNyov9o0ABEQAREQARFIIQQuvRfQeTVgChmzhikCIiACIiACIhBdBEyuKBs3us5asrKWvBZb3eP7SpmoG7+TqRMTk7RMnYTzWshfMRR58156JRablbcjsddkRR03GSwCIhBOAlEUIZJqCeeFob7+h4C9NEdbcAkgaHr37hLcNtWaCIhA8iaAamnatCmv+GWYWvnsfa61hih5X/2+j86e11K+fJls2bL5Xiu6SsZ2ivhof8K+ltguHCu/bNkqPvX2RB8hq5gIiIARkGpJ6EqQatG/EyOgdz4H/UrQO5+DjlQNikBKIBBFqkVriFLCBakxioAIiIAIiEByICDVkhzOYpSOgfAQljv5pFE6CpktAiIgAiIQNgJSLWFDrY7iJpA+/ZXlMAIkAiIgAiIgAgkTuKJaTpw4Qblbb71VvERABERABERABETAVQRMpbC5y9eyePHi8uXLFypU6MYbb2zduvWiRYtOnToVUnAs8erSpcu2bdt87OXixYsY2b59++LFiz/22GNffvll7Ioc3Llzpx3v379/nGUS6M6PKj4a77Zitr4muK8cctsYZY8IiIAIiEAQCbhLtRw6dGjTpk19+vRBSTDIOnXqDBkyJKRrx//666/XXntt69atvjBFsmBP7dq1eTxfjx49UqdOfc8997zzzjuedT/77DMObtmyxQ4ivHxs3GnEjyq+GO/CMpbR4izidaGFMkkEREAERMBVBNylWjJnzgydli1btmvXbvLkyR9//PFLL73022+/hQjZuXPnUl1+zAVyxJcu5s+fP3jw4Hnz5k2ZMqVjx458jhw5Ems9HUI//fTTCy+8ULduXWswbdq0PjbuGOBVJanVfRmIyoiACIiACIhANBJwl2pJkyYNEB3nCvM3f164cMEOEpohKFOzZs3333/fDv7xxx99+/YlWIPKWb16tZ0Apnn2cYoMGzaMJ/3F6arZtWtX27Ztr7rqKvwiThdnzpxBJ/Xr12/cuHEsXvc6nTT71ltv8W39+vVN62Bt9+7dd+zYkSlTJitMYOjgwYPImueff/7o0aMcSZcunWM/oaJGjRph/4IFC8yq119/nTat7rJly1BCnlX27t378MMP08v999+/Zs0aviKSRQuIrWi81GSzCIiACIiACARIwF2qxeZyvCxsTOdkeBAkKliwIAdRKoRmChQoUL169WbNmq1adekZoCNGjCAWM2DAAII1VatWXbFiBS288sor7P/www9r166tVKnShAkTvIRLTExM48aNUTyTJk0igcaEzunTp8mkad68+YEDB6ZPn16lShXrwtmQI8RuatWq5XkQSVGsWDE78vPPP995552ImBYtWnz00UcoEg46jpOvvvoKhZQrV67KlSs/8MADn3/+Od/Sxb59l1b/sqFR3nzzTSyxKmfPnkVXYeTbb7993XXX8axlCuTPnx9lgxIK8KyrugiIgAiIgAhEIwE3qpbhw4e3adOmQ4cO33///TfffLNhwwYmbP4kHMNXeDvy5MljvpBffvklS5YsRYsWxbdB+IY0XrwRPXv2ZPpHN3AE/UHFjRs3ep6bJUuWrF+/HocKMoVPvsIdgv8DYcRXSJmvv/6auA/a6M8///vGu/Pnz1PSvEGxN3TGs88+W7FiRcJGnTp1euSRR7777juKoTDQTHyLhZ07d6Y7dpYvX37LLbfwLf6YnDlzWmvWMiWtChbiW5o4cWKrVq3QYaVKleKZwlmzZjXnkDYREAEREAERSIEE3KVacJmYFsHTgEpgUkc9IFbwTGTMmBHfAwWY3UuXLo0TgpKjR48mPITjBB/GwoULidQgdDiOUqEkG8qDP+2gs+EOue+++8yF4wShCNDwJy4WavEEETrdvXs3lji1cPPUqFEDweHZFOnDdHHs2DFSbufMmdOtW7ccOXJQIHfu3NapxZJQXUuXLm3SpAkxKY4gbjJkyMBx1JIT7rGS6BXb2b9/P59FihTh8+qrr8aLk9Ss3hR4NWvIIiACIiACyZtABFRLAouZnZmb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78QQ0J7PHn8StOezx5HKoAgEAwE/Ui0+yMYNhidAfRQBERABERABEfA4AakWjyOVQREQAREQAREQgUIh4APVwgQiutKyZctC6ZCM+g8Bklpw1h8XrvUfxvJUBERABApAwLygnXz4QLVYwHH1+mGhoqqIgAiIgAiIgAgEDAGnq5bDhw//8Y9/vOWWWxo1ajRkyBBSiK9cuRIw9IO8I2Z+jWe3HApypOq+CIiACAQ2AUerlu+//75Xr14bNmwYP348K+BVqFCBteny30T7xIkTo0aNSkvL3IQvsG+ev/fOrJDmmsTr792R/yIgAiIgAoVNwNGqZdasWWXKlGE5PKIsjz766NSpU1mzDwVz5MiRvLh8++23M2fOTElJKWxwsi8CIiACIiACIuBlAs5VLSdPnkSmjB07lhCLgRISEvLQQw/xgZ2MkpOT77vvPs58zcjI+PWvf71r167Tp0+PGTOGKw8//DBxmmXLlo0cOXLw4ME333zzxo0bf/zxx3fffbd79+79+vXjq7FJbGbChAn16tVDGG3evJkr+/fv792796VLl7x8J9ScCIiACIiACIhA/gScq1pY9AbXmzRpkrUDLKJatGjR1NTU7777bs2aNRcuXOBXlvdFoFCeXx944AGuDB8+vGLFil9++SXRmvT0dEaXyIyJiYlh8Khr164U69atG3qFknFxcXv37qVAaGhou3btvvjii+rVqw8bNoxW9OiIgAiIgAiIgAg4ioBzVcvFixchVbp06ay8jh07RkClcuXK5tdSpUpxNttHX758GeXRunVrPvfs2TMsLIzYzJ133jl37txBgwbt2bPn9ddfj4+PHz16NPGbc+fOmWGmgwcPMghFMOZPf/rTX//619q1a7N077333uuomyRnREAEREAERKBQCbRq1Qr7zs8Kda5qCQ8Ph2BiYmLW+7Ru3boqVaoQgDEziRgb4ow64WyuZJ1hhJqpWrVqyZIluf7ee+8NGDDAyBGz6w3qh/OMGTMYHurbt2+lSpXYg9rIIB0iIAIiIAIiIAIOJOBc1XLrrbd26tRp+vTpJqzC8dVXXz17/WD0p27dulxhcIczARjOJuJSokQJzsRdOBN6MXtDGo1SrVo189mMDZG5wkX0Sv/+/Q8dOrRz507yWsxG2DpEQAREQAREQAQcSMC5qgUV8vLLL5Owctdddy1cuBD5wnBPhw4dhg4dCkdUy4gRI0hVmT17Nom0XClSpAhnhngYVCKdhTQXVIuRLxxPPvnktGnTpkyZQnCFNF5zkZLUMmNDNMQoUq1atc6fP8+qMFrUzoEPq1wSAREQAREIcgLOVS3cmDZt2uzevZvzU089xfDNG2+8MX/+fBNN4YiNjSUYw8UePXqQhEtuilEtH3744bZt21jlhYGktm3bmsIs9LJ8+fK1a9euWLECrcMkI0IvpNwuXry4ePHi48aNY8rSli1bunTpwrykefPmMeEoyJ8MdV8EREAEREAEnEYgxIyhFCtWjDNTaSZPnlzYLpo0lAK1RbYKgZN8HCM0YsyaI9vXwu6R7FsjsGjRMrYiio7up62IrAHMWSs2djoXJ00a5ymDsiMCIhAMBBidIFmCP/g7d+78+eefO6fLWR1jGATHHB1rcYHLX7JQLKtkyfnVOTdAnoiACIiACIiACFgm4B+qxXL3VFEEREAEREAEROCGBEx0wA9mPjNC5Jpoc8NeqYAIiIAIiIAIiIAIeJ+AkSuhZLSYpBYdIiACfk0gKek7/A8Pr+zXvZDzIiACIpArASNX/CMbV7cwIAmYbNw2baIaNKiXrYN169ay3+X09MyJYMnJx+1b87IFk1x+9aq7zVKebq5evQ50Awf2c7eayomACIjAL35B0utjjz3GRNqoqKjt27c7B0nObFypFufcnaDzJC6OXaI0w9zD912qxcNAZU4EgoCAVEt+N9nCzOcgeGaCsYsJCd9s2bKjfPmyp0+fMf1PTU0zH9LSMq94hIs/zqy2EGuBVVhY8cjIiGbNGnuEm4yIgAgECQEnqxZXEIj167kdirUEyTOpboqACIiACIhA7gT8SLVo5rMeYhEQAREQAREIdgJNmzb1CwRSLX5xm+SkCIiACIiACIiAn6yNqxslAiIgAiIgAiIgAoq16BkQAREQAREQARHwDwJSLf5xn+SlCIiACIiACIiAVIueAREQAREQAREQAf8gINXiH/dJXoqACIiACIiACPhAtbRq1QruZ8+eFX0REAEREAEREAEnEMjIyMCNAwcOOMGZfHzwwSpzkZGRCQkJ1apVGzJkiJfplC9f3lqLERER1ir6Ua0aNWpY87Z27drWKqpWMBNISkryl+7rTyxH3alz5845yp/AcObChQt9+/Y1fbnq/v5nhd/5rMvf+Xht3MLvrFoIWAJlypSx1rcuXbpYqxgeHm6touValSpVslzXQsWUlBQLtexU2bp1q7XqljWE8/+ItAbEt7UqVqzoWwfUugcJnDp1qnv37qtWrfKgTZumcqqWX/x0/TB2J06ciMgq7KNTp07169e32RNVFwEREAEREAER8AiBKlWqVL5+jBgxorA1QIHsHzp0qE2bNvSRzaiNXPHBCJF9xKmpqdaM7N6921pFy7XWr19vua61ihs2bLBW0XIty1Qt30fLrqqiCHiTgOUh6ebNm3vTT9qyPAjeuLG26szzXh09etTafbT8b2OpUqUst8i/5ImJiUuWLOnWrZs1I4VRyxEjRIXRMdkUAREQAREQAREIMAI5VUto+vUjwPqp7oiACIiACIiACAQSASNXfDDzOZAgqi8iIAIiIAIiIAJeIxAadv3wWntqSAREQAREQAREQAQKSsDIFcVaCspN5UVABERABERABHxDQKrFN9zVqgiIgAiIgAiIQEEJSLUUlJjKi4AIiIAIiIAI+IaAX67X4htUavXnBBISvklOPs41J63+7OGblJqaZiympp7xoOmwsOLGWnh4FfMhJCTTPFcaNKjnwbZkSgREQAT8l4DWa/Hfe+c4z2NjpzvOJ/93CEETEzPC//uhHoiACIiABwhItXgAokwYAosWLUtM/K5588blypULVCY5gyIe6WnOEI6Jtaxfv4nzpEnjPNKKjIiACIiAvxOQavH3O+gg/41qiY7uV6dOLQe55c+umPCVVIs/30P5LgIi4EkCuayN60nzsiUCIiACIiACIiAChUZAc4gKDa0Mi4AIiIAIiIAIeJSAVItHcQaTMYaH6K6Gh4LpnquvIiACIuBjAlItPr4Bal4EREAEREAERMBNAr5RLT/88EP37t3379/v8vL48eM9e/Y8efLklStXPv30U359++23f/rpp2zdeP/996Ojo9u3b9+mTZtx48bt2LHDzX6qmAiIgAiIgAiIgL8T8I1qSUhI+Pjjj5EdFy5cMASTk5NXrlx57Nixf/3rX127dq1Tp8748ePnzp2bje9f/vKX77//fsCAAcOGDTt79mzLli3Xr1/v7/fAT/2vW/fa1KGkpGvjRDpEQAREQAREwAsEfKNaMjIy6NuqVavmzJljOhny/4uDbt68uW3btq+99lqXLl127tyZDUFKSgqaBskycODAt95669lnnx09evTly5dzJUXYxgsEaSIvB7zTuloRAREQAREQgSAh4BvVEhp6rd24uDjCLVu3bnWxRrswNpSYmNi8efPly5f37ds32224ePFikSJFXEKnbt26hw8fZiBpzJgxL7zwwoMPPtiqVSuGn7j4yCOP3HTTTVzZsmWLKU+xBQsWdOzY8bHHHtuzZ4+5iLJBJ02ePPnFF1/ctm3b1eur0yOqZs2adfvtt/fo0WPFihVGY+V68fz588899xwuEfVZvHixqf78888zyBUkD5C6KQIiIAIiIAJeI+Ab1YKeoIf9+/f/3e9+N2rUqNOnT5v3ParltttuI1tl+PDhGzZs6NatWzYQ6AOGkObPnz9v3jwUjzlKlCiBtoiNjW3SpAmhl9KlSz/xxBMnTpxAo9SsWZNWEDHYmTlz5qBBgwjVoJnuvvvupKQkGn311VfbtWv3n//8B/HUunXrd955h4sfffTRm2++iQ9RUVGk0ZiAUK4XqY4nRH3QN4xbffbZZ5T81a9+1bhxY6/dQjUkAiIgAiIgAsFCgAiEK+l14sSJvLO9cKA84IuY4KhWrdpLL720e/durpCfm3/rqI0qVaqgSxo1ajRkyJBPPvkkPT2dKgRdJkyYQOCEzxs3bsTUwYMH+UzeDNKHgaQjR45wEbnDRaqQVUPYZu/evVxEc1CRg2AJXxmWQt+gVxjAwj0CMAgaauW8SO4w5ePj443PBHvw6tKlS14A6IQmFi5c+sIL0xITDzvBmcDwAZ78LzD6ol6IgAiIgH0Chw4dYvINr1peykau+DLWQjpIrVq1pk2bhuDYtOnaDiyu7Ja8NGNYWNjIkSPPnDnz9ddfM8mIwEnx4te2z+U6pkz1o0ePckbHcCYMw5DQvn37zJAQERHOVIEC8Z5du3bxdejQoURfOBg54isXiZo8/vjjeFW7du1JkyaVKlWK6zkvkjvM9YiICOMt6TjIoLS0zF2Cg0X2qp8iIAIiIAIi4C0CoVljLd5q9BcmN8Uksfbp04fsk2eeecYd1YIKIZiRU9xg0GSfcCBfOJOtwjk1NfWDDz4gQlO2bFm+mugIB6Jk4cKFRo7MmDGDHBrmVBNr4YwzjDpVrVqVKMuBAwcIBU2dOpViOS+Gh4cT9Vm7di2/0jqxmQceeKBixYpew6iGREAEREAERCBICGTGWopdP7zcZ5ONa+b4EPl45ZVXjAPuxFpc6iSrzxgxmTEcLVq0QHkMHjyYYEnnzp1phcxcsnTvueeeRx99lNnUJKOQBxMZGcmvXCRzFhZoHSxjhBGo6tWrT58+fenSpeSykF7TsGFDzOa8WKFCBaZn0wq5wCw2wxASn+kCeTkkzXgZqZoTAREQAREQgQAmYOSKb0aISJJFQFSuXNnwRRYw3ENExHUlL+6sL9e0adOcvzJU5BqpQcEgTXr37r1kyRKGh8g7IV5CV5ctW4a2YECKzBXyWvipTJkyH374IcmznO+//37KmyAQKoSpTGTDsBgMEmfs2LF5XST5F31DlIVGyachsZeSq1evZgArgB8ddU0EREAEREAEvEMg20s/xKTimnAL2bjMAfaOH05rhSjLDSM9TvPZt/4sWrSMrYiio/tpKyJP3YjY2OmYmjRpnKcMyo4IiIAI+DWB//73vyRpEIkgG9ckfvgm1uJAiJIsDrwpckkEREAEREAEshKQatHzIAIiIAIiIAIi4B8EpFr84z7JSxEQAREQAREQAakWPQMi4AgCZh/K8PDMFHVH+CQnREAERMBhBJSN67Ab4j/umGzcNm2iGjSol81rsx20zSM9/UdjITn5uE1Tzq/O+oh0c/XqdaAbOLCf8x2WhyIgAiLgBQI5s3GlWryAPTCbiIub5RIWgdlDX/RKqsUX1NWmCIiAQwlItTj0xvijWwkJ32zZsqN8+bKnT58x/qemZu5mkJaWecUj/QqGmdXX96JgY4rikZERzZpp602PPDgyIgIi4PcEpFr8/haqAyIgAiIgAiIQJAS0XkuQ3Gh1UwREQAREQAQCkIDmEAXgTVWXREAEREAERCAgCUi1BORtVadEQAREQAREIAAJSLUE4E1Vl0RABERABEQgIAlItQTkbVWnREAEREAERCAACUi1BOBNVZdEQAREQAREICAJSLUE5G1Vp0RABERABEQgAAmEpl8/ArBn6pIIiIAIiIAIiECgEDByJeTMmWvLmPbp02fNmjWB0jX/7kerVq38uwO2vb969apNG1euXLFpQdX9nUDHjh1tdqFo0aJ2LISG2o1kly5d2o4D5t92HT4kULJkSZut33HHHXYshIWF2alO3eLFi9uxUKVKFTvVqZuRkTF79uw5c+ZERUWtW7fumrWfrh98t2la1UVABERABERABETA4wTKlSsXERFh5Erm7olt27bdsWOHx1vyicEaNWrYaddmdTtNB0zdhx56yE5fihUrZqc6dY8dO2bHQtWqVe1Ut++AzdbtV9+7d69NI/b/0N+0aZNNH4K8etOmTW0SSEvL3FnMmp3Dhw9bq+iqxbvKjoVevXrZqU7d1NRUOxbi4+PtVFfdrARuu+227du3cyVTtRBN3bp1K9/tB+cFWgREQAREQAREQATsExg0aNCCBQuwExMTM2XKFD5kjrxWrlzZvnVZEAEREAEREAEREAFPEYiOjjamTpw4YT5kqpaUlBRPtSE7IiACIiACIiACIlAYBDJViyY/FwZc2RQBERABERABEbBPwJVjlKlaTp48ad+oLIiACIiACIiACIiAxwns27fP2MxULeHh4R5vQwZFQAREQAREQAREwD6BxMTEn6kW+xZlQQREQAREQAREQAQ8S8AsVXfx4kWpFs+ClTUREAEREAEREAEPE8i2wG7mCNGlS5c83I7MiYAIiIAIiIAIiIAnCHTu3FmxFk+AlA0REAEREAEREIFCI2D2QnItlJwZa7G/0VehOSzDIiACIiACIiACQUrgwIED9LxMmTI/i7VcvnyZ7+3btw9SKuq2CIiACIiACIiA8wicPXsWp1wr+GfGWoxq0SECIiACIiACIiACTiNw4cKFn8VakpKS+J6RkeE0R+WPCIiACIiACIhAkBM4f/78z1SLicDccsstQc5F3RcBERABERABEXAaAaNSODJHiJzmn/wRAREQAREQAREQgQYNGgDh8OHDUi16GERABERABERABBxNoGbNmln9C/3p+tGwYUOuulbMdXQP5JwIiIAIiIAIiEBwEChSpAgdZf6zkSsh/J/vERERJORWrVo1MjLStxwqVKhg04EWLVrYtODv1W3exKioKH8nIP8DgMDOnTv9uhenTp3ya//lPATOnDkjDr4lQBJubGys8cHIlUzVUqxYMd96ptZFwEXAtZqQZSZdunSxXJeKPt8CvVKlSnb8t183JSXFvhGbFrZu3WrHgit3z7IRs7aVDh8SqFixog9bV9POIcDfAE2aNMn8S8aEXDp06FC/fn3nuChPREAEREAEREAEgpwAC/mzvhxH27ZtfzZCVLRoUU+hMUu/WD7i4+Mt1/VIxZUrV3rEjmUje/bssVzXIxXT0tJs2rl69apNC6ouAiIQEhJiB4Jr3xY7RuzUtR+zNAmXOiwTOHLkiOW6pqLNmGWJEiXsO3D06NH09PTJkyfHxMRgLXOEKFe76BprI0c0gMGwsDBr7qpdN7mJs5ugTDE9V27i0nPlJig9VwUCpeeqQLj071VeuLReS4EeJBUWAREQAREQARHwGQGpFp+hV8MiIAIiIAIiIAIFIvB/n+hkSSzlreIAAAAASUVORK5CYII=)

