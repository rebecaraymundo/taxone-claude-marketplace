# MTZ_Geracao_Anexos VII e VII-M

- **Fonte:** MTZ_Geracao_Anexos VII e VII-M.docx
- **Modificado:** 2023-06-02
- **Tamanho:** 67 KB

---

Combustíveis e Derivados de Petróleo

Geração dos Anexos VII e VII\-M para Refinarias

__Localização: Movimento de Refinaria > Geração Anexos VII, VII\-M__

Quadro de Revisões

__                         __

__Data__

__OS / Chamado__

__Descrição__

__Responsável__

29/05/2023

MFS535202

Geração do Anexo VII\-M para produtos com tributação monofásica\.

Liliane Assaf

[1\.	Introdução	1](#_Toc136460527)

[2\.	Parâmetros de Tela	1](#_Toc136460528)

[3\.	Regras de Negócio	1](#_Toc136460529)

[RN01 \- Geração do Anexo VII\-M \- Quadro 1	1](#_Toc136460530)

[RN02 \- Geração do Anexo VII\-M \- Quadro 2	1](#_Toc136460531)

[RN03 \- Geração do Anexo VII\-M \- Quadro 3	1](#_Toc136460532)

[RN04 \- Geração do Anexo VII\-M \- Quadro 4	1](#_Toc136460533)

[RN05 \- Geração do Anexo VI\-M \- Quadro 5	1](#_Toc136460534)

[RN06 \- Geração do Anexo VII\-M \- Quadro 6	1](#_Toc136460535)

[RN07 \- Geração do Anexo VI\-M \- Quadro 7	1](#_Toc136460536)

# <a id="_Toc136460527"></a>Introdução 

O Anexo VII\-M vem para substituir o Anexo VII para os combustíveis no regime de tributação monofásica do ICMS\. Segundo a legislação que regulamenta o regime monofásico sobre combustíveis, o Diesel, Biodiesel e GLP/GLGN entram para o monofásico em Maio/2023, portando, a partir desse mês devem ser apresentados no Anexo VII\-M e não mais no Anexo VII\. A Gasolina e EAC aderem ao monofásico do ICMS a partir de Junho/2023\. Uma vez que o combustível é apresentado no Anexo VII\-M ele deixa de compor o Anexo VII\.

Anexo VII\-M é composto pelos quadro 1 ao 7, sendo que os quadros 2 ao 7 são digitados manualmente, através das telas disponíveis no menu “Movimento de Refinaria 🡪 Manutenção Anexo VII\-M”\. O quadro 1 é gerado por essa rotina a partir da totalização dos quadros 2 a 7 do Anexo VII\-M e do valor 2\.3 do quadro 2 do Anexo VI\-M\.

# <a id="_Toc136460528"></a>Parâmetros de Tela

Parâmetros demonstrados na tela:

- Mês/Ano Referência
- Estabelecimentos

# <a id="_Toc136460529"></a>Regras de Negócio

## <a id="_Toc136460530"></a>RN01 \- Geração do Anexo VII\-M \- Quadro 1

O Quadro 1 é uma totalização dos quadros 2 ao 7\.

Para cada UF que o estabelecimento tenha Inscrição Estadual, devem ser gerado o quadro 1, mesmo que zerado, ou seja para um período/UF SEM MOVIMENTO\. Esse procedimento já era adotado para o Anexo VII, e vale também para o VII\-M, com base em esclarecimento recebido por email do Sr Lino Silva Neto \([lino\.neto@fazenda\.mg\.gov\.br](mailto:lino.neto@fazenda.mg.gov.br)\) \.

Gravar os campos do Quadro 1 conforme regras abaixo\. O registro gerado está disponível para manutenção no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VII\-M 🡪 Quadro 1\.

Tabela: CBT\_ANEXO7M\_QUADR1

__Nome do Campo__

__Nome físico do campo__

__Regra de Preenchimento __

Empresa

Cod\_Empresa

Empresa de login

Estabelecimento:

Cod\_Estab

Estabelecimento selecionado na Geração

Mês/Ano Referência:

Dat\_apuracao

Último dia do mês/ano informado na tela de geração

UF Destinatária do Anexo VII\-M

Ident\_estado\_destino

UF Destinatária do Anexo VII\-M recuperada dos quadros selecionados nos campos abaixo\.

Vlr 1\.1

VALOR PROVISIONADO CONFORME LINHA 2\.3 DO QUADRO 2 DO ANEXO VI\-A

vlr\_icms\_st\_11     

Consultar o __Quadro 2 do Anexo VI\-M __com os critérios: empresa, estabelecimento e mês/ano referência informados para geração\.

Recuperar Vlr 2\.3 por UF Destinatária do Anexo VII\-M\.

Gravar esse campo com o Vlr 2\.3\.

Vlr 1\.2

REPASSE GLOSADO REFERENTE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs \(QUADRO 2\)

vlr\_icms\_st\_12    

Consultar o __Quadro 2 do Anexo VII\-M__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = “A7MQ2”\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VII\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.3

REPASSE GLOSADO REFERENTE OPERAÇÕES REALIZADAS POR IMPORTADORES \(QUADRO 3\)

vlr\_icms\_st\_13

Consultar o __Quadro 3 do Anexo VII\-M__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = “A7MQ3”\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VII\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.4

REPASSE GLOSADO REFERENTE A BIOCOMBUSTÍVEIS \(QUADRO 4\)

vlr\_icms\_st\_14    

Consultar o __Quadro 4 do Anexo VII\-M__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = “A7MQ4”\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VII\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.5

VALOR DA PROVISÃO A SER REPASSADA \(1\.1 \- 1\.2 \- 1\.3 \- 1\.4\)

vlr\_icms\_st\_15

Somatório dos campos Vlr 1\.1, Vlr 1\.2, Vlr 1\.3, Vlr 1\.4\.

Vlr 1\.6

DEDUÇÃO GLOSADA REFERENTE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs \(QUADRO 5\)

vlr\_icms\_st\_16

Consultar o __Quadro 5 do Anexo VII\-M__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = “A7MQ5”\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VII\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.7

DEDUÇÃO GLOSADA REFERENTE OPERAÇÕES REALIZADAS POR IMPORTADORES \(QUADRO 6\)

vlr\_icms\_st\_17

Consultar o __Quadro 6 do Anexo VII\-M__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = “A7MQ6”\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VII\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.8

DEDUÇÃO GLOSADA REFERENTE A BIOCOMBUSTÍVEIS \(QUADRO 7\)

vlr\_icms\_st\_18

Consultar o __Quadro 7 do Anexo VII\-M__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = “A7MQ7”\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VII\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.9

VALOR DA PROVISÃO PARA DEDUÇÃO GLOSADA \(1\.6 \+ 1\.7 \+ 1\.8\)

vlr\_icms\_st\_19

Somatório dos campos Vlr 1\.6, Vlr 1\.7, Vlr 1\.8\.

Vlr 1\.10

ICMS A RECOLHER \(1\.5 \+ 1\.9\)

vlr\_icms\_st\_110

Somatório dos campos Vlr 1\.5, Vlr 1\.9

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

2

Usuário

Usuario

Usuário da aplicação

## <a id="_Toc136460531"></a>RN02 \- Geração do Anexo VII\-M \- Quadro 2

O Quadro 2 não é gerado e sim apenas digitado manualmente no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VII\-M 🡪 Quadro 2 a 7\.

Tabela: CBT\_ ANEXO7M\_QUADR2A7

## <a id="_Toc136460532"></a>RN03 \- Geração do Anexo VII\-M \- Quadro 3

O Quadro 3 não é gerado e sim e apenas digitado manualmente no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VII\-M 🡪 Quadro 2 a 7\.

Tabela: CBT\_ ANEXO7M\_QUADR2A7

## <a id="_Toc136460533"></a>RN04 \- Geração do Anexo VII\-M \- Quadro 4

O Quadro 4 não é gerado e sim apenas digitado manualmente no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VII\-M 🡪 Quadro 2 a 7\.

Tabela: CBT\_ ANEXO7M\_QUADR2A7

## <a id="_Toc136460534"></a>RN05 \- Geração do Anexo VI\-M \- Quadro 5

O Quadro 5 não é gerado e sim apenas digitado manualmente no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VII\-M 🡪 Quadro 2 a 7\.

Tabela: CBT\_ ANEXO7M\_QUADR2A7

## <a id="_Toc136460535"></a>RN06 \- Geração do Anexo VII\-M \- Quadro 6

O Quadro 6 não é gerado e sim apenas digitado manualmente no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VII\-M 🡪 Quadro 2 a 7\.

Tabela: CBT\_ ANEXO7M\_QUADR2A7

## <a id="_Toc136460536"></a>RN07 \- Geração do Anexo VI\-M \- Quadro 7

O Quadro 7 não é gerado e sim apenas digitado manualmente no item de Menu Movimento de Refinaria 🡪 Manutenção Anexo VII\-M 🡪 Quadro 2 a 7\.

Tabela: CBT\_ ANEXO7M\_QUADR2A7

