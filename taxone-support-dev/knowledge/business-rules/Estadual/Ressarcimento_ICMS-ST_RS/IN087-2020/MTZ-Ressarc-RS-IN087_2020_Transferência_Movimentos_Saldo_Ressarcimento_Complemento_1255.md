# MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_Saldo Ressarcimento Complemento_1255

- **Fonte:** MTZ-Ressarc-RS-IN087_2020_Transferência_Movimentos_Saldo Ressarcimento Complemento_1255.docx
- **Modificado:** 2021-10-11
- **Tamanho:** 99 KB

---

THOMSON REUTERS

Módulo Ressarcimento / Complemento ICMS ST – RS 

\(IN\-RE 087/2020\) 

Geração do Saldo Consolidado de Ressarcimento e Complementação \(1255\) 

__Localização__: Menu Estadual, Módulo: Ressarcimento de ICMS\-ST \- RS \(IN\-RE 048/2018\),

 itens: Geração 🡪 IN\-RE 087/20 🡪 Transferência dos Movimentos para EFD Fiscal 

	

##### DOCUMENTO DE REQUISITO

__OS/CH__

__Nome__

__Descrição__

__Data__

__MFS48753__

Liliane Videira Assaf

Criação da funcionalidade\.

Não estamos considerando Cupom Fiscal nesta entrega\.

22/12/2020 

__MFS65137__

Liliane Videira Assaf

Os cupons fiscais gravados na tabela X297\_INF\_COMP\_ST\_CUPOM\_ECF para geração do registro C480, passam a ser considerados na geração do registro 1255 do Sped Fiscal\.

13/05/2021

__MFS72429__

Andréa Rocha

Inclusão do arredondamento dos valores calculados, ou seja, os valores calculados não serão mais truncados\.  Conforme informação passada pela SEFAZ/RS\.

11/10/2021

Sumário

[1\.	Introdução	1](#_Toc61547900)

[2\.	Limpeza da tabela de Saldo Consolidado da Restituição/Complemento \- X304\_SALDO\_CONS\_RES\_COMP\_ICMS	1](#_Toc61547901)

[3\.	Recuperação dos Dados e Processamento	1](#_Toc61547902)

[3\.1 – Recuperação da Movimentação de Saída por Nota \(C185, C380\)	1](#_Toc61547903)

[3\.2 – Recuperação da Movimentação de Saída por Cupons Fiscais \(C480\)	1](#_Toc61547904)

[3\.3 – Recuperação da Movimentação de Saída por Cupons Fiscais Eletrônicos \(C815\)	1](#_Toc61547905)

[3\.4 – Recuperação da Movimentação de Saída Venda a Consumidor \(C330\)	1](#_Toc61547906)

[3\.5 – Recuperação da Movimentação do Equipamento ECF \(C430\)	1](#_Toc61547907)

[3\.6 – Recuperação da Movimentação do Equipamento SAT\-CF\-E \(C880\)	1](#_Toc61547908)

[3\.7– Recuperação a Movimentação de Devolução de Saída \(C181\)	1](#_Toc61547909)

[4\.	Gravação dos Dados na Tabela de Saldo Consolidado da Restituição/Complemento \- X304\_SALDO\_CONS\_RES\_COMP\_ICMS	1](#_Toc61547910)

[5\.	RELATORIO DE CONFERÊNCIA	1](#_Toc61547911)

# <a id="_Toc61547900"></a>Introdução 

Esse documento tem como objetivo definir a geração do registro 1255 – __Saldo Consolidado do Ressarcimento Complementação por Motivo __que consiste em:

- Recuperar os valores de ressarcimento e complementação das movimentaçoes do período, oriundos das seguintes tabelas:
- x296\_info\_compl\_st\_itens\_merc – Movimentos de Saídas \(C185, C380\);
- x297\_inf\_comp\_st\_cupom\_ecf – Movimento de Cupons Fiscais \(C480\) \[__MFS65137\]__
- x298\_info\_comp\_st\_it\_cupom\_cfe \(C815\)
- X299\_INF\_COMP\_ST\_RES\_MOD\_02 \(C330\)
- x302\_inf\_comp\_st\_res\_it\_ecf \(C430\)
- x303\_inf\_comp\_st\_res\_cupom\_cfe \(C880\)
- X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV – Movimentos de Devolução de Saídas \(C181\);
- Totalizar os valores por Código de Motivo da Restituição/Complemento
- Gravar o registro resultante da consolidação por Código de Motivo da Restituição/Complementação, na tabela de __Saldo Consolidado da Restituição/Complemento \- __X304\_SALDO\_CONS\_RES\_COMP\_ICMS, base para geração do registro 1255 no Sped Fiscal\.

__Sobre os registros C330, C430, C815 e C880:__

Hoje a funcionalidade de Geração dos Movimentos do Ressarcimento RS não gera os registros C330, C430, C815 e C880 pois as instruções normativas 087/20 e 096/20 não estabelecem regras para utilização dos mesmos\.

Mesmo assim, nada impede do cliente gerar tais registros no Sped Fiscal, através da importação das SAFX298, SAFX299, SAFX302, SAFX303\.  Por isso é necessário considerá\-los na geração do registro 1255, para obtermos um arquivo do Sped Fiscal consistente\.

O Guia Prático esclarece que os valores de ressarcimento e complemento são totalizações dos valores oriundos os registros C181, C185, C330, C380, C430, C480, C815 e C880\.Veja:

__“Campo 04 __\(VL\_ICMS\_ST\_REST\_MOT\) – __Validação: __o valor informado no campo deve corresponder à soma dos campos VL\_UNIT\_ICMS\_ST\_CONV\_REST multiplicados pelo campo QUANT\_CONV dos registros C181, C185, C330, C380, C430, C480, C815 e C880 para cada código informado no campo COD\_MOT\_REST\_COMPL”

# <a id="_Toc61547901"></a>Limpeza da tabela de Saldo Consolidado da Restituição/Complemento \- X304\_SALDO\_CONS\_RES\_COMP\_ICMS

No início do processamento é necessário excluir os registros da tabela __x304\_saldo\_cons\_res\_comp\_icms__ com os seguintes critérios:

\- Empresa = de login do Manager

\- Estab = selecionado na tela de geração;

\- Data Apuração compreendida no período informado na tela de geração

\- Ind\_gravação = '0', '6','7','8'\.

# <a id="_Toc350763252"></a><a id="_Toc61547902"></a>Recuperação dos Dados e Processamento

## <a id="_2.1_–_Recuperação"></a><a id="_Toc61547903"></a>3\.1 – Recuperação da Movimentação de Saída por Nota \(C185, C380\)

__Origem dos dados__: \- Tabela Informações Complementares das Operações Sujeitas ao ST \(C180, C185 e C380\) \- x296\_info\_compl\_st\_itens\_merc

__Critérios da recuperação: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data Fiscal – data enquadrada no período informado em tela;

\- Nota de saída \(MOVTO\_E\_S = “9”\);

 Recuperar os campos:

- 24\-Código Motivo \(Saídas\) \(COD\_MOTIVO\_SAI\)
- 16\-Quantidade Convertida \(QTD\_CONV\)
- 29\- Valor Unitário ICMS\-ST Conv\. Rest\. \(Saídas\) \(VLR\_UNIT\_ICMSS\_REST\_SAI\)
- 30\- Valor Unitário FCP\-ST Conv\. Rest\. \(Saídas\)  \(VLR\_UNIT\_FCP\_REST\_SAI\)
- 31\-Valor Unitário ICMS\-ST Conv\. Compl\. \(Saídas\) \(VLR\_UNIT\_ICMSS\_COMPL\_SAI\)
- 32\-Valor Unitário FCP\-ST Conv\. Compl\. \(Saídas\) \(VLR\_UNIT\_FCP\_COMPL\_SAI\)

Calcular os valores de ICMS\-ST e FECEP\-ST de Ressarcimento e Complemento, através da multiplicação dos valores unitários pela quantidade\. Veja:

- Valor do ICMS\-ST Restituição \(VLR\_ICMS\_ST\_REST\) = VLR\_UNIT\_ICMSS\_REST\_SAI x QTD\_CONV
- Valor do FCP\-ST  Restituição \(VLR\_FCP\_ST\_REST\) =  VLR\_UNIT\_FCP\_REST\_SAI x QTD\_CONV
- Valor do ICMS\-ST Complemento \(VLR\_ICMS\_ST\_COMP\) = VLR\_UNIT\_ICMSS\_COMPL\_SAI x QTD\_CONV
- Valor do FCP\-ST Complemento \(VLR\_FCP\_ST\_COMP\) = VLR\_UNIT\_FCP\_COMPL\_SAI x QTD\_CONV

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

__      Obs\.: Todos os valores calculados devem ser arredondados, não devem ser truncados\.__

\[__MFS65137\]__

## <a id="_2.2_–_Recuperação"></a><a id="_Toc61547904"></a>3\.2 – Recuperação da Movimentação de Saída por Cupons Fiscais \(C480\) 

__Origem dos dados__: \- Tabela Informações Complementares das Operações Sujeitas ao ST \(C480\) \- x297\_inf\_comp\_st\_cupom\_ecf

__Critérios da recuperação: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data Emissão – data enquadrada no período informado em tela;

 Recuperar os campos:

- 9\-Código do Motivo \(COD\_MOTIVO\)
- 10\-Quantidade Convertida \(QTD\_CONV\)
- 18\- Valor Unitário ICMS\-ST Conv\. Rest\. \(VLR\_UNIT\_ICMSS\_REST\_CONV\)
- 19\- Valor Unitário FCP\-ST Conv\. Rest\.  \(VLR\_UNIT\_FCPS\_REST\_CONV\)
- 20\-Valor Unitário ICMS\-ST Conv\. Compl\. \(VLR\_UNIT\_ICMSS\_COMPL\_CONV\)
- 21\-Valor Unitário FCP\-ST Conv\. Compl\. \(VLR\_UNIT\_FCPS\_COMPL\_CONV\)

Calcular os valores de ICMS\-ST e FECEP\-ST de Ressarcimento e Complemento, através da multiplicação dos valores unitários pela quantidade\. Veja:

- Valor do ICMS\-ST Restituição \(VLR\_ICMS\_ST\_REST\)      = VLR\_UNIT\_ICMSS\_REST\_CONV x QTD\_CONV
- Valor do FCP\-ST Restituição \(VLR\_FCP\_ST\_REST\)         =  VLR\_UNIT\_FCPS\_REST\_CONV x QTD\_CONV
- Valor do ICMS\-ST Complemento \(VLR\_ICMS\_ST\_COMP\) = VLR\_UNIT\_ICMSS\_COMPL\_CONV x QTD\_CONV
- Valor do FCP\-ST Complemento \(VLR\_FCP\_ST\_COMP\)     = VLR\_UNIT\_FCPS\_COMPL\_CONV x QTD\_CONV

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

__      Obs\.: Todos os valores calculados devem ser arredondados, não devem ser truncados\.__

## <a id="_Toc61547905"></a>3\.3 – Recuperação da Movimentação de Saída por Cupons Fiscais Eletrônicos \(C815\) 

__Origem dos dados__: \- Tabela Informações Complementares das Operações Sujeitas ao ST \(C815\) \- x298\_info\_comp\_st\_it\_cupom\_cfe

__Critérios da recuperação: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data Emissão – data enquadrada no período informado em tela;

 Recuperar os campos:

- 7\-Código do Motivo \(COD\_MOTIVO\_SAI\)
- 8\-Quantidade Convertida \(QTD\_CONV\)
- 16\- Valor Unitário ICMS\-ST Conv\. Rest\. \(VLR\_UNIT\_ICMSS\_REST\_CONV\)
- 17\- Valor Unitário FCP\-ST Conv\. Rest\.  \(VLR\_UNIT\_FCPS\_REST\_CONV\)
- 18\-Valor Unitário ICMS\-ST Conv\. Compl\. \(VLR\_UNIT\_ICMSS\_COMPL\_CONV\)
- 19\-Valor Unitário FCP\-ST Conv\. Compl\. \(VLR\_UNIT\_FCPS\_COMPL\_CONV\)

Calcular os valores de ICMS\-ST e FECEP\-ST de Ressarcimento e Complemento, através da multiplicação dos valores unitários pela quantidade\. Veja:

- Valor do ICMS\-ST Restituição \(VLR\_ICMS\_ST\_REST\)      = VLR\_UNIT\_ICMSS\_REST\_CONV x QTD\_CONV
- Valor do FCP\-ST  Restituição \(VLR\_FCP\_ST\_REST\)         =  VLR\_UNIT\_FCPS\_REST\_CONV x QTD\_CONV
- Valor do ICMS\-ST Complemento \(VLR\_ICMS\_ST\_COMP\) = VLR\_UNIT\_ICMSS\_COMPL\_CONV x QTD\_CONV
- Valor do FCP\-ST Complemento \(VLR\_FCP\_ST\_COMP\)     = VLR\_UNIT\_FCPS\_COMPL\_CONV x QTD\_CONV

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

__      Obs\.: Todos os valores calculados devem ser arredondados, não devem ser truncados\.__

## <a id="_Toc61547906"></a>3\.4 – Recuperação da Movimentação de Saída Venda a Consumidor \(C330\) 

__Origem dos dados__: \- Tabela Informações Complementares das Operações Sujeitas ao ST \(C330\) \- X299\_INF\_COMP\_ST\_RES\_MOD\_02

__Critérios da recuperação: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data Emissão – data enquadrada no período informado em tela;

 Recuperar os campos:

- 14\-Código do Motivo \(COD\_MOTIVO\)
- 15\-Quantidade Convertida \(QTD\_CONV\)
- 23\- Valor Unitário ICMS\-ST Conv\. Rest\. \(VLR\_UNIT\_ICMSS\_REST\_CONV\)
- 24\- Valor Unitário FCP\-ST Conv\. Rest\.  \(VLR\_UNIT\_FCPS\_REST\_CONV\)
- 25\-Valor Unitário ICMS\-ST Conv\. Compl\. \(VLR\_UNIT\_ICMSS\_COMPL\_CONV\)
- 26\-Valor Unitário FCP\-ST Conv\. Compl\. \(VLR\_UNIT\_FCPS\_COMPL\_CONV\)

Calcular os valores de ICMS\-ST e FECEP\-ST de Ressarcimento e Complemento, através da multiplicação dos valores unitários pela quantidade\. Veja:

- Valor do ICMS\-ST Restituição \(VLR\_ICMS\_ST\_REST\)      = VLR\_UNIT\_ICMSS\_REST\_CONV x QTD\_CONV
- Valor do FCP\-ST  Restituição \(VLR\_FCP\_ST\_REST\)         =  VLR\_UNIT\_FCPS\_REST\_CONV x QTD\_CONV
- Valor do ICMS\-ST Complemento \(VLR\_ICMS\_ST\_COMP\) = VLR\_UNIT\_ICMSS\_COMPL\_CONV x QTD\_CONV
- Valor do FCP\-ST Complemento \(VLR\_FCP\_ST\_COMP\)     = VLR\_UNIT\_FCPS\_COMPL\_CONV x QTD\_CONV

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

__      Obs\.: Todos os valores calculados devem ser arredondados, não devem ser truncados\.__

## <a id="_Toc61547907"></a>3\.5 – Recuperação da Movimentação do Equipamento ECF \(C430\) 

__Origem dos dados__: \- Tabela Informações Complementares das Operações Sujeitas ao ST \(C430\) \- x302\_inf\_comp\_st\_res\_it\_ecf

__Critérios da recuperação: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data do Movimento \(DATA\_FISCAL\) – data enquadrada no período informado em tela;

 Recuperar os campos:

- 10\-Código do Motivo \(COD\_MOTIVO\)
- 11\-Quantidade Convertida \(QTD\_CONV\)
- 19\- Valor Unitário ICMS\-ST Conv\. Rest\. \(VLR\_UNIT\_ICMSS\_REST\_CONV\)
- 20\- Valor Unitário FCP\-ST Conv\. Rest\.  \(VLR\_UNIT\_FCPS\_REST\_CONV\)
- 21\-Valor Unitário ICMS\-ST Conv\. Compl\. \(VLR\_UNIT\_ICMSS\_COMPL\_CONV\)
- 22\-Valor Unitário FCP\-ST Conv\. Compl\. \(VLR\_UNIT\_FCPS\_COMPL\_CONV\)

Calcular os valores de ICMS\-ST e FECEP\-ST de Ressarcimento e Complemento, através da multiplicação dos valores unitários pela quantidade\. Veja:

- Valor do ICMS\-ST Restituição \(VLR\_ICMS\_ST\_REST\)      = VLR\_UNIT\_ICMSS\_REST\_CONV x QTD\_CONV
- Valor do FCP\-ST  Restituição \(VLR\_FCP\_ST\_REST\)         =  VLR\_UNIT\_FCPS\_REST\_CONV x QTD\_CONV
- Valor do ICMS\-ST Complemento \(VLR\_ICMS\_ST\_COMP\) = VLR\_UNIT\_ICMSS\_COMPL\_CONV x QTD\_CONV
- Valor do FCP\-ST Complemento \(VLR\_FCP\_ST\_COMP\)     = VLR\_UNIT\_FCPS\_COMPL\_CONV x QTD\_CONV

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

__      Obs\.: Todos os valores calculados devem ser arredondados, não devem ser truncados\.__

## <a id="_Toc61547908"></a>3\.6 – Recuperação da Movimentação do Equipamento SAT\-CF\-E \(C880\) 

__Origem dos dados__: \- Tabela Informações Complementares das Operações Sujeitas ao ST \(C430\) \- x303\_inf\_comp\_st\_res\_cupom\_cfe

__Critérios da recuperação: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data da Emissão \(DATA\_EMISSAO\) – data enquadrada no período informado em tela;

 Recuperar os campos:

- 11\-Código do Motivo \(COD\_MOTIVO\)
- 12\-Quantidade Convertida \(QTD\_CONV\)
- 20\- Valor Unitário ICMS\-ST Conv\. Rest\. \(VLR\_UNIT\_ICMSS\_REST\_CONV\)
- 21\- Valor Unitário FCP\-ST Conv\. Rest\.  \(VLR\_UNIT\_FCPS\_REST\_CONV\)
- 22\-Valor Unitário ICMS\-ST Conv\. Compl\. \(VLR\_UNIT\_ICMSS\_COMPL\_CONV\)
- 23\-Valor Unitário FCP\-ST Conv\. Compl\. \(VLR\_UNIT\_FCPS\_COMPL\_CONV\)

Calcular os valores de ICMS\-ST e FECEP\-ST de Ressarcimento e Complemento, através da multiplicação dos valores unitários pela quantidade\. Veja:

- Valor do ICMS\-ST Restituição \(VLR\_ICMS\_ST\_REST\)      = VLR\_UNIT\_ICMSS\_REST\_CONV x QTD\_CONV
- Valor do FCP\-ST  Restituição \(VLR\_FCP\_ST\_REST\)         =  VLR\_UNIT\_FCPS\_REST\_CONV x QTD\_CONV
- Valor do ICMS\-ST Complemento \(VLR\_ICMS\_ST\_COMP\) = VLR\_UNIT\_ICMSS\_COMPL\_CONV x QTD\_CONV
- Valor do FCP\-ST Complemento \(VLR\_FCP\_ST\_COMP\)     = VLR\_UNIT\_FCPS\_COMPL\_CONV x QTD\_CONV

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

__      Obs\.: Todos os valores calculados devem ser arredondados, não devem ser truncados\.__

## <a id="_Toc61547909"></a>3\.7– Recuperação a Movimentação de Devolução de Saída \(C181\)

__Origem dos dados__: \- Tabela de Informações Complementares das Operações de Devolução Sujeitas ao ST \(C181 e C186\) \- X308\_INFO\_COMPL\_ST\_IT\_MERC\_DEV;

__Critérios da recuperação: __

\- Empresa – código da empresa do login;

\- Estabelecimento – código do estabelecimento selecionado para geração;

\- Data Fiscal – data enquadrada no período informado em tela;

\- Nota de entrada \(MOVTO\_E\_S <> “9”\);

 Recuperar os campos:

- 31\-Código do Motivo \(COD\_MOTIVO\)
- 32\-Quantidade Convertida \(QTD\_CONV\)
- 43\- Valor Unitário ICMS\-ST Conv\. Rest\. \(VLR\_UNIT\_ICMSS\_REST\_CONV\)
- 44\- Valor Unitário FCP\-ST Conv\. Rest\.  \(VLR\_UNIT\_FCPS\_REST\_CONV\)
- 45\-Valor Unitário ICMS\-ST Conv\. Compl\. \(VLR\_UNIT\_ICMSS\_COMPL\_CONV\)
- 46\-Valor Unitário FCP\-ST Conv\. Compl\. \(VLR\_UNIT\_FCPS\_COMPL\_CONV\)

Calcular os valores de ICMS\-ST e FECEP\-ST de Ressarcimento e Complemento, através da multiplicação dos valores unitários pela quantidade\. Veja:

- Valor do ICMS\-ST Restituição \(VLR\_ICMS\_ST\_REST\)      = VLR\_UNIT\_ICMSS\_REST\_CONV x QTD\_CONV
- Valor do FCP\-ST Restituição \(VLR\_FCP\_ST\_REST\)         =  VLR\_UNIT\_FCPS\_REST\_CONV x QTD\_CONV
- Valor do ICMS\-ST Complemento \(VLR\_ICMS\_ST\_COMP\) = VLR\_UNIT\_ICMSS\_COMPL\_CONV x QTD\_CONV
- Valor do FCP\-ST Complemento \(VLR\_FCP\_ST\_COMP\)     = VLR\_UNIT\_FCPS\_COMPL\_CONV x QTD\_CONV

__\[MFS72429\]__ Substituição do truncamento pelo arredondamento dos campos

__      Obs\.: Todos os valores calculados devem ser arredondados, não devem ser truncados\.__

# <a id="_Toc61547910"></a>Gravação dos Dados na Tabela de Saldo Consolidado da Restituição/Complemento \- X304\_SALDO\_CONS\_RES\_COMP\_ICMS

Os valores recuperados nas consultas acima, devem ser consolidados pelo Código de Motivo, gerando um registro para cada código\.

Caso registro já exista na tabela __x304\_saldo\_cons\_res\_comp\_icms__ \(caso que foi incluído via digitação ou importação\), então:

Gravar a seguinte mensagem de aviso no log:

*“Registro 1255: Registro de Saldo incluído via importação/manutenção da SAFX304, foi atualizado pelo processamento da geração\. Os dados originalmente inseridos foram desprezados”*

 Exibir dados para identificação do registro \(dados da chave\);

Contabilizar o número de registros inseridos e atualizados a ser demonstrado para o 1255 no relatório de “Resumo Registros Gerados”, especificado no “*MTZ\-Ressarc\-RS\-IN087\_2020\_Transferência\_Movimentos\_EFD Fiscal\.docx*”\.

PK

Item

SAFX304

Campo

Regra de Preenchimento

Campos para relatório

__*Campos do layout da SAFX304*__

\(\*\)

01

Código da Empresa 

COD\_EMPRESA

Código da empresa de login\.

Cod Empresa

\(\*\)

02

Código do Estabelecimento

COD\_ESTAB

Código do estabelecimento SELECIONADO na tela de geração\.

Cod Estab

\(\*\)

03

Data da Apuração

DATA\_APURACAO

Último dia do Mês da geração, informado na tela de geração\.

Dt Apuração

\(\*\)

04

Código do Motivo 

COD\_MOTIVO

Código do Motivo recuperado nas consultas descritas no tópico 3\.

Cod Motivo

05

Valor do ICMS

VLR\_ICMS

Preencher com Zero\.

OBS: em conversa com o CAN identificamos que não seria possível calcular esse valor\. Caso seja necessário preenche\-lo isso ser fará através da tela de manutenção, disponível no módulo Sped Fiscal\.

Vlr ICMS

06

Valor do ICMS\-ST Restituição

VLR\_ICMS\_ST\_REST

Valor do ICMS\-ST Restituição \(VLR\_ICMS\_ST\_REST\) calculado nas consultas descritas no tópico 3\.

Vlr ICMS\-ST Rest\.

07

Valor do FCP\-ST Restituição

VLR\_FCP\_ST\_REST

Valor do FCP\-ST Restituição \(VLR\_FCP\_ST\_REST\) calculado nas consultas descritas no tópico 3\.

Vlr FECEP\-ST Rest\.

08

Valor do ICMS\-ST Complemento

VLR\_ICMS\_ST\_COMP

Valor do ICMS\-ST Complemento \(VLR\_ICMS\_ST\_COMP\) calculado nas consultas descritas no tópico 3\.

Vlr ICMS\-ST Compl\.

 

09

Valor do FCP\-ST Complemento

VLR\_FCP\_ST\_COMP

Valor do FCP\-ST Complemento \(VLR\_FCP\_ST\_COMP\) calculado nas consultas descritas no tópico 3\.

Vlr FECEP\-ST Compl\.

Indicador de Gravação

IND\_GRAVACAO

‘6’

__Sobre o campo IND\_GRAVAÇÃO__:

O ind\_gravação informa a origem do registro nas tabelas definitivas \(X\) que possuem importação por SAFX\. 

IND\_GRAVACAO:

Valores padrão do campo \( tabelas de importação \):

1\.  Incluído por Importação

2\.  Atualizado por Importação

3\.  Incluído por Importação / Atualizado por Digitação

4\.  Incluído por Digitação

5\.  Incluído por Digitação / Atualizado por Digitação

6\.  Gerado pelo Sistema

7\.  Gerado pelo Sistema  / Atualizado por Digitação

8\. Gerado pelo Sistema  / Atualizado por Importação

O valor 8 foi criado na OS2388\-AA, A4, e somente é considerado nas importações das SAFX112 e SAFX113\.

9\. Atualizado pelo Sistema

# <a id="_Toc61547911"></a>RELATORIO DE CONFERÊNCIA

Gerar arquivos excel a partir da leitura da tabela x304\_saldo\_cons\_res\_comp\_icms

Nome do arquivo: Relatório\_Conferência\_1255\_mm\_aaaa\_cod\_estab\.xlsx

= = = = = =

 

