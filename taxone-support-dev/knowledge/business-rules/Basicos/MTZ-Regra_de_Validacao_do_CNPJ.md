# MTZ-Regra de Validação do CNPJ

> Fonte: MTZ-Regra de Validação do CNPJ.docx






THOMSON REUTERS



Regra de Validação do CNPJ






DOCUMENTO DE REQUISITO


Sumário

1.	Introdução	1
2.	Base Legal	1
3.	Regra de Negócio	1
3.1 - Regra de Formação:	1
3.2 – Regra de Validação do CNPJ	1



## Introdução


Este documento tem como objetivo especificar a regra de formação e validação do CNPJ, Cadastro Nacional de Pessoa Jurídica, que a partir de Julho de 2026 adotará formato alfanumérico.


## Base Legal

Instrução Normativa n° 2.229, de 15/10/24, estabelece o formato alfanumérico para o número identificador do Cadastro Nacional da Pessoa Jurídica – CNPJ.

Documento de apoio: Perguntas e Respostas da Receita Federal (cnpj-alfanumerico.pdf)



## Regra de Negócio


O CNPJ alfanumérico é a forma de identificar empresas no Brasil, combinando letras e números. A identificação da pessoa jurídica (PJ) será composta por números de 0 a 9 e quaisquer uma das 26 letras de A até Z.
O CNPJ numérico e alfanumérico irá coexistir, ou seja, as tanto o formato numérico quanto o alfanumérico será válido em todos os processos que utilizam a identificação do CNPJ.

### 3.1 - Regra de Formação:





### 3.2 – Regra de Validação do CNPJ

Essa regra refere-se ao cálculo do Dígito Verificador que é executada para validar o CNPJ no momento do impute dessa informação via telas manutenção e importações de SAFX.

O Dígito Verificador é calculado pelo algoritmo do módulo 11. Como este algoritmo de validação é um cálculo numérico, todos os caracteres que compõe a identificação do CNPJ numéricos e alfanuméricos, são transformados pelo código
ASCII conforme tabela abaixo:





Exemplo de Cálculo de Dígito Verificador de um CNPJ alfanumérico:
Vamos tomar como exemplo o número do CNPJ 12.ABC.345/01DE-dv, onde dv é o dígito verificador.
Tomemos a letra “A” cujo decimal correspondente, no código ASCII, é 65. Subtraindo 48 temos o valor 17 para o cálculo do módulo 11.
Para o cálculo do dígito verificador pelo Módulo 11 do número CNPJ 12.ABC.345/01DE– dv temos:

CNPJ 				:	1  2.  A   B    C.    3    4    5 /  0  1  D   E
Valor Hexa subtraído de 48 	:	1  2  17  18  19    3    4    5    0  1  20  21
Peso 				:           5  4  3    2    9      8    7    6    5  4  3    2
Multiplicar Valor x Peso 	:	5  8  51  36  171  24  28  30  0  4  60  42  => Soma = 459
Mod (459/11) = 8
Primeiro dv = 11- 8 = 3

Repete-se o processo acrescentando o primeiro Dígito Verificador no CNPJ
CNPJ				: 	1   2.  A    B    C.  3    4    5 /  0  1  D   E - 3
Valor Hexa subtraído de 48	:	1   2   17  18  19  3    4    5    0  1  20  21  3
Peso 				:	6   5   4    3    2    9    8    7    6  5  4    3    2
Multiplicar Valor x Peso:		6  10  68  54  38  27  32  35  0  5  80  63  6 => Soma = 424
Mod (424/11) = 6
Segundo dv = 11- 6 = 5

Concluindo:
Ao final do cálculo do Dígito Verificador pelo Módulo 11 temos o número do CNPJ:
CNPJ 1 2. A B C. 3 4 5 / 0 1 D E - 3 5

= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS741454 | Liliane V. Assaf | Infolegis nº 2242/24 - CNPJ Alfanumérico | 08/01/2025 |
|  |  |  |  |
|  |  |  |  |
