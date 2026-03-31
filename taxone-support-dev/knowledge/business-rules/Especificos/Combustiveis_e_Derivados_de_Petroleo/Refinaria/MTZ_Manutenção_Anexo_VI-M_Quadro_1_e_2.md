# MTZ_Manutenção_Anexo_VI-M_Quadro 1 e 2

- **Fonte:** MTZ_Manutenção_Anexo_VI-M_Quadro 1 e 2.docx
- **Modificado:** 2025-10-29
- **Tamanho:** 72 KB

---

THOMSON REUTERS

Manutenção Anexo VI\-M Quadros 1 e 2

Módulo Combustível e Derivados de Petróleo \(SCANC\)

Localização: Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadro 1 e 2

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

MFS535202

MFS783073

Liliane Assaf

Alteração do label dos campos referentes aos valores 1\.1\.5, 1\.1\.6, 1\.2\.4, 1\.2\.5 para inclusão do GLGNn\.

MFS917434

Liliane Assaf

Inclusão da linha __1\.1\.1\.2__: Somatório dos registros do quadro 3\.1\.

Inclusão da linha __1\.2\.0\.1__: Somatório dos registros do quadro 3\.2\.

Atualização da linha __1\.1\.7__: adicionar o valor da linha 1\.1\.1\.2 no somatório das linhas 1\.1\.1, 1\.1\.2, 1\.1\.3, 1\.1\.4, 1\.1\.5, 1\.1\.6\.

Atualização da linha __1\.2\.8__: adicionar o valor da linha 1\.2\.0\.1 no somatório das linhas 1\.2\.1, 1\.2\.2, 1\.2\.3, 1\.2\.4, 1\.2\.5, 1\.2\.6, 1\.2\.7\.

Sumário

[1\.	Regras dos Campos	3](#_Toc494454507)

# <a id="_Toc350763252"></a><a id="_Toc494454507"></a>Regras dos Campos 

__Localização da tela:__ Específicos >> Combustível e Derivados de Petróleo

__                                   __Movimento de Refinaria 🡪 Manutenção Anexo VI\-M 🡪 Quadro 1 e 2

__Quadro 1:__

O Quadro 1 é uma totalização de quadros 3 ao 15\. A tela permite inclusão de registro e alteração dos valores\. As telas dos quadros 3 ao 15 atualizam automaticamente os valores do quadro 1, conforme regras abaixo\. 

Tabela: CBT\_ANEXO6M\_QUADR1

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

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF Destinatária do Anexo VI\-M recuperada dos quadros selecionados nos campos abaixo\.

Vlr 1\.1\.1 

ICMS SOBRE OPERAÇÕES POR TRIBUTAÇÃO MONOFÁSICA PRÓPRIAS E RETIDAS \(QUADRO 3\)

vlr\_icms\_st\_111      

Consultar o __Quadro 3__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração\.

Recuperar Vlr ICMS Total \(ICMS Cobrado \+ Retido\) totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS Total \(ICMS Cobrado \+ Retido\)\.

__\[MFS917434\]__

Vlr 1\.1\.1\.2 

ICMS SOBRE OPERAÇÕES COM GLGN DEVIDO A UF DE ORIGEM \(QUADRO 3\.1\)

vlr\_icms\_st\_1112      

Consultar o __Quadro 3\.1__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ31\.

Recuperar Vlr ICMS Total \(ICMS Cobrado \+ Retido\) totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS Total \(ICMS Cobrado \+ Retido\)\.

Vlr 1\.1\.2

REPASSE DE ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs \(QUADRO 4\.1\.1\)

vlr\_icms\_st\_112    

Consultar o __Quadro 4\.1\.1__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ41 e COD\_QUADRO = 1\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.1\.3

REPASSE DE ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS DE GÁS \(QUADRO 4\.1\.2\.\)

vlr\_icms\_st\_113

Consultar os __Quadros 4\.1\.2\.1__ e __4\.1\.2\.2 __com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ41 e COD\_QUADRO = 21 e 22\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.1\.4

REPASSE DE ICMS DECORRENTE DE RELATÓRIOS EXTEMPORÂNEOS \(QUADRO 4\.3\)

vlr\_icms\_st\_114    

Consultar o __Quadro 4\.3__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ43\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.1\.5

REPASSE DE ICMS SOBRE BIOCOMBUSTÍVEIS <a id="_Hlk193229402"></a>OU GLGNn DECORRENTE DE AJUSTES DE REPARTIÇÃO DE RECEITA \(QUADRO 6\.1\) MFS783073

vlr\_icms\_st\_115

Consultar o __Quadro 6\.1__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ61\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.1\.6

REPASSE DE ICMS SOBRE BIOCOMBUSTÍVEIS OU GLGNn DECORRENTE DE RELATÓRIOS EXTEMPORÂNEOS \(QUADRO 6\.2\) MFS783073

vlr\_icms\_st\_116

Consultar o __Quadro 6\.2__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ62\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

__\[MFS917434\]__

Vlr 1\.1\.7

SUB\-TOTAL \(1\.1\.1\+1\.1\.1\.2 \+ 1\.1\.2 \+ 1\.1\.3 \+ 1\.1\.4 \+ 1\.1\.5 \+ 1\.1\.6\)

vlr\_icms\_st\_117

Somatório dos campos Vlr 1\.1\.1, Vlr 1\.1\.1\.2, Vlr 1\.1\.2, Vlr 1\.1\.3, Vlr 1\.1\.4, Vlr 1\.1\.5 e Vlr 1\.1\.6\.

__\[MFS917434\]__

Vlr 1\.2\.0\.1 

DEDUÇÃO DE ICMS SOBRE OPERAÇÕES COM GLGN DEVIDO A UF DE ORIGEM \(QUADRO 3\.2\)

vlr\_icms\_st\_1201      

Consultar o __Quadro 3\.2__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ32\.

Recuperar Vlr ICMS Total \(ICMS Cobrado \+ Retido\) totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS Total \(ICMS Cobrado \+ Retido\)\.

Vlr 1\.2\.1

DEDUÇÃO DE ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs A SER REPASSADO A OUTRAS UFs \(QUADRO 7\.1\.1\)

vlr\_icms\_st\_121

Consultar o __Quadro 7\.1\.1__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ71 e COD\_QUADRO = 1\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.2\.2

DEDUÇÃO DE ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS DE GÁS \(QUADRO 7\.1\.2\)

vlr\_icms\_st\_122

Consultar os __Quadros 7\.1\.2\.1__ e 7__\.1\.2\.2 __com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ71 e COD\_QUADRO = 21 e 22\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.2\.3

DEDUÇÃO DE ICMS DECORRENTE DE RELATÓRIOS EXTEMPORÂNEOS \(QUADRO 7\.3\)

vlr\_icms\_st\_123

Consultar o __Quadro 7\.3__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ73\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.2\.4

DEDUÇÃO DE ICMS SOBRE BIOCOMBUSTÍVEIS OU GLGNn DECORRENTE DE AJUSTES DE REPARTIÇÃO DE RECEITA \(QUADRO 9\.1\) MFS783073

vlr\_icms\_st\_124

Consultar o __Quadro 9\.1__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ91\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.2\.5

DEDUÇÃO DE ICMS SOBRE BIOCOMBUSTÍVEIS OU GLGNn DECORRENTE DE RELATÓRIOS EXTEMPORÂNEOS \(QUADRO 9\.2\) MFS783073

vlr\_icms\_st\_125

Consultar o __Quadro 9\.2__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ92\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.2\.6

PROVISÃO PARA REPASSE POR OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs \(QUADRO 7\.2\)

vlr\_icms\_st\_126

Consultar o __Quadro 7\.2__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ72\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.2\.7

PROVISÃO PARA REPASSE POR OPERAÇÕES REALIZADAS POR IMPORTADORES \(QUADRO 8\)

vlr\_icms\_st\_127

Consultar o __Quadro 8__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ8\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

__\[MFS917434\]__

Vlr 1\.2\.8

SUB\-TOTAL DAS DEDUÇÕES \(1\.2\.0\.1\+1\.2\.1 \+ 1\.2\.2 \+ 1\.2\.3 \+ 1\.2\.4 \+ 1\.2\.5 \+ 1\.2\.6 \+ 1\.2\.7\)

vlr\_icms\_st\_128

Somatório dos campos Vlr1\.2\.0\.1, Vlr 1\.2\.1, Vlr 1\.2\.2, Vlr 1\.2\.3, Vlr 1\.2\.4, Vlr 1\.2\.5, Vlr 1\.2\.6 e Vlr 1\.2\.7\.

Vlr 1\.2\.9

ICMS RESSARCIDO A DISTRIBUIDORAS \(QUADRO 10\)

vlr\_icms\_st\_129

Consultar o __Quadro 10__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ10\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.2\.10

ICMS RESSARCIDO A TRRs \(QUADRO 11\)

vlr\_icms\_st\_1210

Consultar o __Quadro 11__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ11\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.2\.11

ICMS RESSARCIDO A IMPORTADORES \(QUADRO 12\)

vlr\_icms\_st\_1211

Consultar o __Quadro 12__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ12\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.2\.12

ICMS RESSARCIDO A OUTROS CONTRIBUINTES \(QUADRO 13\)

vlr\_icms\_st\_1212

Consultar o __Quadro 13__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ13\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.2\.13

__SUB\-TOTAL DOS RESSARCIMENTOS \(1\.2\.9 \+ 1\.2\.10 \+ 1\.2\.11 \+ 1\.2\.12\)__

vlr\_icms\_st\_1213

Somatório dos campos Vlr 1\.2\.9, Vlr 1\.2\.10, Vlr 1\.2\.11, Vlr 1\.2\.12

Vlr 1\.3

__ICMS DEVIDO \[1\.1\.7 \- \(1\.2\.8 \+ 1\.2\.13\)\]__

vlr\_icms\_st\_13

Preencher com Vlr 1\.1\.7 \- Vlr 1\.2\.8 \- Vlr 1\.2\.13

Vlr 1\.3\.1

DEDUÇÃO TRANSFERIDA DE OUTRO ESTABELECIMENTO DO SUJEITO PASSIVO POR TRIBUTAÇÃO MONOFÁSICA \(QUADRO 14\)

vlr\_icms\_st\_131

Consultar o __Quadro 14__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ14\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.3\.2

DEDUÇÃO TRANSFERIDA PARA OUTRO ESTABELECIMENTO DO SUJEITO PASSIVO POR TRIBUTAÇÃO MONOFÁSICA \(QUADRO 15\)

vlr\_icms\_st\_132

Consultar o __Quadro 15__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ15\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 1\.3\.3

__ICMS A RECOLHER \(1\.3 \+ 1\.3\.1\) ou \(1\.3 \- 1\.3\.2\)__

vlr\_icms\_st\_133

Preencher com: Vlr 1\.3 \+ Vlr 1\.3\.1 ou 

                          Vlr 1\.3 \- Vlr 1\.3\.2

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

1\-Inserido manualmente, 2\-calculado via Geração do Anexo VII\-M, 3\-calculado via Geração do Anexo VII\-M e atualizado via tela de manutenção\.

Usuário

Usuario

Usuário da aplicação

__Quadro 2:__

O Quadro 2 é uma totalização de quadros 4\.2 e 5\. A tela permite inclusão de registro e alteração dos valores\. As telas dos quadros 4\.2 e 5 atualizam automaticamente os valores do quadro 2, conforme regras abaixo\. 

Gravar os campos do Quadro 2 conforme regras abaixo\.

Tabela: CBT\_ANEXO6M\_QUADR2

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

Último dia do mês/ano da geração

UF Destinatária do Anexo VI\-M

Ident\_estado\_destino

UF Destinatária do Anexo VI\-M recuperada dos quadros selecionados nos campos abaixo\.

Vlr 2\.1

ICMS SOBRE OPERAÇÕES REALIZADAS POR DISTRIBUIDORAS/TRRs \(QUADRO 4\.2\)

vlr\_icms\_st\_21

Consultar o __Quadro 4\.2__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ42\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 2\.2

ICMS SOBRE OPERAÇÕES REALIZADAS POR IMPORTADORES \(QUADRO 5\)

vlr\_icms\_st\_22

Consultar o __Quadro 5__ com os critérios: empresa, estabelecimento e mês/ano referência informados para geração, COD\_TAG = A6MQ5\.

Recuperar Vlr ICMS totalizado por UF Destinatária do Anexo VI\-M\.

Gravar esse campo com o Vlr ICMS\.

Vlr 2\.3

ICMS PROVISIONADO \(2\.1 \+ 2\.2\)

vlr\_icms\_st\_23

Preencher com Vlr 2\.1 \+ Vlr 2\.2

No Processo

Num\_Processo

Número do processo da geração

Ind Dig Calc

Ind Dig Calc

1\-Inserido manualmente, 2\-calculado via Geração do Anexo VII\-M, 3\-calculado via Geração do Anexo VII\-M e atualizado via tela de manutenção\.

Usuário

Usuario

Usuário da aplicação

