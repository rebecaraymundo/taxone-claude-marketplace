---
source: "MTZ-Report_Fiscal-Diferencial_de_Aliquotas_por_Documento.doc"
category: Report_Fiscal
converted: auto
---

Report Fiscal - Relatório de Diferencial de Alíquota por Documento


                                         BÁSICOS ? REPORT FISCAL ? Obrigações Acessórias ? ICMS ? Diferencial de Alíquota p/ DataMart ? Documento
BÁSICOS ? REPORT FISCAL ? Obrigações Acessórias ? ICMS ? Diferencial de Alíquota p/ DataMart ? Documento - Formato EXCEL


DOCUMENTO DE REQUISITO

DR
Nome
Descrição
OS3196
Permitir a geração por Inscrição Estadual Única dos relatórios de Diferencial de Alíquota de ICMS 
Permitir a geração a partir dos estabelecimentos centralizadores. 
OS3819
Alteração da apuração do Dif. Alíquota
Alteração da apuração do diferencial de alíquota para considerar o parâmetro 67 (Parametrização por UF do Módulo ICMS). (ver RN05)
MFS-4142
Alteração para calcular o DIFAL
Alteração no calculo do DIFAL para demonstração no report, Dec. 46930/2015.
MFS-34957
Inclusão de colunas
Inclusão das colunas Chave da NF-Eletrônica e Base ICMS-ST no relatório e geração do relatório no formato EXCEL.
MFS76479
Alteração para calcular o DIFAL
Inclusão de Regra para considerar o Parâmetro 92 (Parâmetros p/ UF) Específico para as UF's RS, GO, MG e PR (Readequação a alteração dos Lançamentos Automáticos da Apuração. (MTZ_Calculo_Diferencial_Aliquota_Lancamento_Automatico).
MFS88013
Alteração para calcular o DIFAL
Inclusão de Regra para considerar o Parâmetro 92 (Parâmetros p/ UF) Específico para a UF de SP.
MFS94495
Alteração para calcular o DIFAL
Inclusão de Regra para considerar o Parâmetro 92 (Parâmetros p/ UF) Específico para as UF´s de ES, BA e SC.
MFS435431
Alteração para calcular o DIFAL
Inclusão de Regra para considerar o Parâmetro 92 (Parâmetros p/ UF) Específico para a UF de PA
MFS519100
Alteração para calcular o DIFAL
Inclusão de Regra para considerar o Parâmetro 92 (Parâmetros p/ UF) Específico para a UF de MA
MFS564128
Alteração para calcular o DIFAL
Inclusão de Regra para considerar o Parâmetro 92 (Parâmetros p/ UF) Específico para a UF de RO
MFS569514
Alteração para calcular o DIFAL
Inclusão de Regra para considerar o Parâmetro 92 (Parâmetros p/ UF) Específico para a UF de AC
MFS571687
Alteração para calcular o DIFAL
Inclusão de Regra para considerar o Parâmetro 92 (Parâmetros p/ UF) Específico para a UF de RJ
MFS571692
Alteração para calcular o DIFAL
Inclusão de Regra para considerar o Parâmetro 92 (Parâmetros p/ UF) Específico para a UF de SE
MFS572622
Alteração para calcular o DIFAL
Inclusão de Regra para considerar o Parâmetro 92 (Parâmetros p/ UF) Específico para a UF de RR.
MFS572711
Alteração para calcular o DIFAL
Inclusão de Regra para considerar o Parâmetro 92 (Parâmetros p/ UF) Específico para a UF de TO.
MFS573401
Alteração para calcular o DIFAL
Inclusão de Regra para considerar o Parâmetro 92 (Parâmetros p/ UF) Específico para a UF de AM.
MFS573416
Alteração para calcular o DIFAL
Inclusão de Regra para considerar o Parâmetro 92 (Parâmetros p/ UF) Específico para a UF de AP.
MFS573406
Alteração para calcular o DIFAL
Inclusão de Regra para considerar o Parâmetro 92 (Parâmetros p/ UF) Específico para a UF de PE.
MFS573412
Alteração para calcular o DIFAL
Inclusão de Regra para considerar o Parâmetro 92 (Parâmetros p/ UF) Específico para a UF de MS.
MFS576319
Alteração para calcular o DIFAL
Inclusão de Regra para considerar o Parâmetro 92 (Parâmetros p/ UF) Específico para a UF de PI.
MFS576330
Alteração para calcular o DIFAL
Inclusão de Regra para considerar o Parâmetro 92 (Parâmetros p/ UF) Específico para a UF de AL.
MFS589832
Andréa Rocha
Alteração da regra de validação do parâmetro "Somente documentos com diferencial" para tratar as regras específicas criadas para cada UF.
MFS593347
Alteração para calcular o DIFAL
Inclusão de Regra para considerar o Parâmetro 92 (Parâmetros p/ UF) Específico para a UF de PB.
MFS844874
Alteração para calcular o DIFAL
Inclusão de Regra para considerar o Parâmetro 92 (Parâmetros p/ UF) Específico para a UF de RN.
MFS859953
Alteração para calcular o DIFAL
Ajuste do Cálculo do DIFAL com Base Dupla p/ São Paulo em atendimento às operações de contribuintes do Simples Nacional - Base Dupla - RN06.d
MFS938348
Alteração para calcular o DIFAL
Ajuste do Cálculo do DIFAL com Base Dupla p/ São Paulo em atendimento às operações de contribuintes do Simples Nacional - Base Dupla - RN06.d


REGRAS DE NEGÓCIO

Cód.
Descrição
DR
RN00
Na tela de argumentos deste relatório, acrescentar um flag antes do campo UF:

[  ] Geração Centralizada por Inscrição Estadual Única

Este campo deve vir por default desmarcado.

[  ] Somente documentos com diferencial

Este campo deve vir por default marcado (vide RN07).

OS3196
MFS589832
RN01
Quando não for selecionado nenhuma opção no campo UF e o campo ¨Geração Centralizada por Inscrição Estadual Única¨ estiver marcado, apresentar somente a lista dos estabelecimentos centralizadores.
OS3196
RN02

Quando for selecionada uma UF no campo UF e o campo ¨Geração Centralizada por Inscrição Estadual Única¨ estiver marcado, apresentar somente a lista dos estabelecimentos centralizadores daquela UF.
OS3196
RN03
Quando não for selecionado nenhuma opção no campo UF e o campo ¨Geração Centralizada por Inscrição Estadual Única¨ não estiver marcado, apresentar a lista de todos os estabelecimentos.
OS3196
RN04
Quando for selecionada uma UF no campo UF e o campo ¨Geração Centralizada por Inscrição Estadual Única¨ não estiver marcado, apresentar a lista de todos os estabelecimentos daquela UF.
OS3196
RN05
Recuperação das NFs utilizando o parâmetro 67 (Parâmetros por UF do Módulo ICMS)


Alteração da OS3819:

A recuperação das notas para emissão do relatório foi alterada para utilizar o parâmetro 67 da parametrização por UF do Módulo ICMS (menu Manutenção --> Parâmetros por UF). Originalmente, este parâmetro não era utilizado no filtro dos documentos. A partir desta OS, tanto a apuração do DIFAL feita no livro P9, como os 4 relatórios do DIFAL do Report Fiscal foram atualizados para usar o parâmetro 67.

A partir de então, serão recuperadas apenas as notas em que e UF da pessoa fis/jur (ou a UF Origem da nota, dependendo do conteúdo do parâmetro 67) for diferente da UF do Estabelecimento.

A comparação das UF's a serem utilizadas será feita da seguinte forma:

Se parâmetro 67 marcado

      Neste caso, a comparação entre as Ufs é feita utilizando a UF Origem informada no documento fiscal (campo 117 
      da SAFX07), mas apenas nos casos em que ela estiver preenchida, ou seja:
        Se UF Origem da SAFX07 preenchida:
             [UF Origem da SAFX07 <> UF do cadastro do Estabelecimento] 
        Senão
             [UF do cadastro da SAFX04 <> UF do cadastro do Estabelecimento] 
Senão
       Neste caso, a comparação das Ufs é feita sempre a partir da UF da pessoa fis/jur:
                [UF do cadastro da SAFX04 <> UF do cadastro do Estabelecimento]

OS3819
RN06
 [MFS76479] Tratamento Regra Cálculo Diferencial de Alíquota - Débito (Considerando Parâmetro 92) 
Para cada item de nota (ou nota, se não existir itens) selecionado, o DIFAL será calculado utilizando a parametrização do módulo Ferramentas (*), da seguinte forma:
A regra para o cálculo do Valor de Diferencial de Alíquota dependerá do parâmetro 92 da parametrização por UF do Módulo ICMS (menu "Manutenção > Parâmetros por UF"), considerando a UF do estabelecimento, da seguinte forma:

Se (parâmetro 92 Desmarcado):
     Valor do DIFAL = Valor da Base de Cálculo (considerando a parametrização definida no RN01) multiplicado 
                              pelo Valor da Diferença Alíquota ICMS (valor deve ser dividido por 100) (campo 44 da SAFX08);
Sendo:

   Se parâmetro = 1 --> o DIFAL será = [ Base Tributada * DIF_ALIQ_TRIB_ICMS / 100 ]
   Se parâmetro = 2 --> o DIFAL será = [ (Base Tributada + Base Outras) * DIF_ALIQ_TRIB_ICMS / 100 ]
   Se parâmetro = 3 --> o DIFAL será = [ (Valor Contábil do Item - (Base Isenta + Base Redução) - Valor do ICMS-ST) 
                                                                                                                                          * DIF_ALIQ_TRIB_ICMS / 100 ]
   Se parâmetro = 4 --> o DIFAL será = valor carregado para o campo VLR_OUTROS1 (*Informado somente para Débito)

Para os parâmetros 1, 2 e 3 o que muda é o valor que será utilizado como base para aplicação da alíquota, e no caso do parâmetro 4, o valor não é calculado, pois já vem carregado no campo "Valor Outros 1" do item do documento fiscal.

(*) Módulo ferramentas, menu "Parâmetros do Sistema --> Parâmetros por Estabelecimento".
   Se parâmetro = 5 --> o DIFAL será = [((VLR_CONTAB_ITEM * (100 - VLR_ALIQ_ICMS) / 100) / ((100 - VLR_ALIQ_DESTINO) / 100) * (VLR_ALIQ_DESTINO / 100)) - (VLR_CONTAB_ITEM * VLR_ALIQ_ICMS /100)]
Senão
  Se (parâmetro 92 Marcado):
     Neste caso, a regra de cálculo a ser utilizada depende da UF:
     Se UF do Estabelecimento = "RS" --> Neste caso será utilizada a regra de cálculo descrita na RN06.a;
     Se UF do Estabelecimento = "GO" --> Neste caso será utilizada a regra de cálculo descrita na RN06.b;
     Se UF do Estabelecimento = "PR" ou "MG" --> Neste caso será utilizada a regra de cálculo descrita na RN06.c;
     Se UF do Estabelecimento = "SP" --> Neste caso será utilizada a regra de cálculo descrita na RN06.d;
     Se UF do Estabelecimento = "ES", "BA" ou "SC" --> Neste caso será utilizada a regra de cálculo descrita na RN06.e;
     Se UF do Estabelecimento = "PA" --> Neste caso será utilizada a regra de cálculo descrita na RN06.f;
     Se UF do Estabelecimento = "MA" --> Neste caso será utilizada a regra de cálculo descrita na RN06.g;
     Se UF do Estabelecimento = "RO" --> Neste caso será utilizada a regra de cálculo descrita na RN06.h;
     Se UF do Estabelecimento = "AC" --> Neste caso será utilizada a regra de cálculo descrita na RN06.i;
     Se UF do Estabelecimento = "RJ" --> Neste caso será utilizada a regra de cálculo descrita na RN06.j; 
     Se UF do Estabelecimento = "SE" --> Neste caso será utilizada a regra de cálculo descrita na RN06.k;
     Se UF do Estabelecimento = "RR" --> Neste caso será utilizada a regra de cálculo descrita na RN06.l;
     Se UF do Estabelecimento = "TO" --> Neste caso será utilizada a regra de cálculo descrita na RN06.m;
     Se UF do Estabelecimento = "AM" --> Neste caso será utilizada a regra de cálculo descrita na RN06.n; 
     Se UF do Estabelecimento = "AP" --> Neste caso será utilizada a regra de cálculo descrita na RN06.o;
     Se UF do Estabelecimento = "PE" --> Neste caso será utilizada a regra de cálculo descrita na RN06.p;
     Se UF do Estabelecimento = "MS" --> Neste caso será utilizada a regra de cálculo descrita na RN06.q;
     Se UF do Estabelecimento = "PI" --> Neste caso será utilizada a regra de cálculo descrita na RN06.r;
     Se UF do Estabelecimento = "AL" --> Neste caso será utilizada a regra de cálculo descrita na RN06.s;
     Se UF do Estabelecimento = "PB" --> Neste caso será utilizada a regra de cálculo descrita na RN06.t;
     Se UF do Estabelecimento = "RN" --> Neste caso será utilizada a regra de cálculo descrita na RN06.u;

     Se nenhuma das alternativas acima --> Neste caso o cálculo será feito pela mesma regra usada p/o parâmetro
                                                           desmarcado, conforme descrito acima; 


MFS-4142
MFS76479
RN06.a
Regra do cálculo para Diferencial de Alíquota- Débito e Débito (extras) (UF = RS): p/ Material de Consumo e Ativo Imobilizado

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado (menu "Manutenção > Parâmetros por UF");
  E a UF do Estabelecimento for igual à RS

Aplicar a fórmula abaixo:

[((Base de Cálculo - ICMS Origem * VLR_ALIQ_DESTINO) / (1 - VLR_ALIQ_DESTINO)] - ICMS Origem)

[Valor da Base de Cálculo - Valor do ICMS x Valor da Alíquota de Destino] - Valor do ICMS
       1 - Valor da Alíquota de Destino

Sendo:

- Base de Cálculo: o valor a ser utilizado depende da opção de valor escolhida pelo usuário no parâmetro 92
  (Parâmetros por UF), da seguinte forma:

   Se opção = 1 ("Valor Contábil do Item"), será utilizado o valor contábil do item (campo 64 da SAFX08);
   Se opção = 2 ("Valor parametrizado no Ferramentas"), será utilizado o valor parametrizado no módulo
                        Ferramentas, (Módulo ferramentas, menu "Parâmetros do Sistema --> Parâmetros por Estabelecimento").
- Valor do ICMS: Campo VLR_ICMS SAFX08 ou Campo VLR_ICMS_NDESTAC SAFX08.
- Alíquota de Destino: Campo VLR_ALIQ_DESTINO SAFX08 (valor deve ser dividido por 100).

Exemplo:

- Base de Cálculo: R$ 1.000,00
- ICMS Origem: 120,00
- Alíquota interna: 18
- Diferença de Alíquota: 6

Valor do DIFAL = [ ((1.000,00 - 120,00) x 0,18 ) /  (1 - 0,18)] - 120,00
                          [ (880,00 x 0,18) / 0,82] - 120,00
                          [ 158,40 / 0,82] - 120,00
                          193,17 - 120,00 = 73,17

Obs¹.: Para maiores informações consultar documento: MTZ_Calculo_Diferencial_Aliquota_Lancamento_Automatico.doc
Obs².: O cálculo do DIFAL para o tipo "Material de Consumo - Débito (extras)" é exatamente igual ao do tipo "Material de Consumo - Débito". A diferença é apenas na recuperação das notas, já que a parametrização de CFOP e Natureza de Operação é feita separadamente.

MFS76479
RN06.b
Regra do cálculo para Diferencial de Alíquota- Débito e Débito (extras) (UF = GO): p/ Material de Consumo e Ativo Imobilizado

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado (menu "Manutenção > Parâmetros por UF");
  E a UF do Estabelecimento for igual à GO;

Aplicar a fórmula abaixo:

[Base de Cálculo / (1 - VLR_ALIQ_DESTINO/100) * (DIF_ALIQ_ICMS/100)]


Valor do DIFAL =       Base de Cálculo 
                         ----------------------------      x    Diferença de Alíquota ICMS/100
                          1 - Alíquota Interna/100
 
Sendo:

- Base de Cálculo: o valor a ser utilizado depende da opção de valor escolhida pelo usuário no parâmetro 92
                            (Parâmetros por UF), da seguinte forma:
      Se opção = 1 ("Valor Contábil do Item"), será utilizado o valor contábil do item (campo 64 da SAFX08);
      Se opção = 2 ("Valor parametrizado no Ferramentas"), será utilizado o valor parametrizado no módulo
                          Ferramentas, (Módulo ferramentas, menu "Parâmetros do Sistema --> Parâmetros por Estabelecimento").
- Alíquota Interna: alíquota informada no campo "Valor da Alíquota de Destino" (campo 63 da SAFX08);
- Diferença de Alíquota ICMS: valor da diferença entre as alíquotas interna e interestadual (campo 44 da SAFX08);

Exemplo:

- Base de Cálculo: R$ 1.000,00
- Alíquota interna: 18
- Diferença de Alíquota: 6

Valor do DIFAL = [ 1.000,00 / (1 - 0,18) ] x 0,06 = [ 1.000,00 / 0,82 ] x 0,06 = 1.219,51 x 0,06 = 73,17

Obs¹.: Para maiores informações consultar documento: MTZ_Calculo_Diferencial_Aliquota_Lancamento_Automatico.doc
Obs².: O cálculo do DIFAL para o tipo "Material de Consumo - Débito (extras)" é exatamente igual ao do tipo "Material de Consumo - Débito". A diferença é apenas na recuperação das notas, já que a parametrização de CFOP e Natureza de Operação é feita separadamente.

MFS76479
RN06.c
Regra do cálculo para Diferencial de Alíquota- Débito e Débito (extras) (UF = MG e PR): p/ Material de Consumo e Ativo Imobilizado

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado (menu "Manutenção > Parâmetros por UF");
  E a UF do Estabelecimento for igual à MG ou PR;

Aplicar a fórmula abaixo:

[((Base de Cálculo - ICMS Origem) / (1 - VLR_ALIQ_DESTINO/100) * (VLR_ALIQ_DESTINO/100)] - ICMS Origem


Valor do DIFAL =           Base de Cálculo - ICMS Origem
                          [ (  --------------------------------------  )  x  Alíquota Interna/100 ] - ICMS Origem
                                       1 - Alíquota Interna/100

Sendo:

- Base de Cálculo: o valor a ser utilizado depende da opção de valor escolhida pelo usuário no parâmetro 92
                            (Parâmetros por UF), da seguinte forma:
      Se opção = 1 ("Valor Contábil do Item"), será utilizado o valor contábil do item (campo 64 da SAFX08);
      Se opção = 2 ("Valor parametrizado no Ferramentas"), será utilizado o valor parametrizado no módulo
                          Ferramentas, (Módulo ferramentas, menu "Parâmetros do Sistema --> Parâmetros por Estabelecimento").
- Alíquota Interna: alíquota informada no campo "Valor da Alíquota de Destino" (campo 63 da SAFX08);
- ICMS Origem: valor do ICMS do documento fiscal (campo 43 da SAFX08). Quando este valor não estiver preenchido, 
  será utilizado o valor do campo "80-ICMS Não Escriturado" (caso das aquisições em que o ICMS não será creditado,
  como por exemplo as aquisições de Bens cujo crédito será apropriado no controle do CIAP);

Exemplo:

- Base de Cálculo: R$ 1.000,00
- Alíquota interna: 18
- ICMS Origem: 120,00

Valor do DIFAL = [ [(1.000,00 - 120,00) / (1 - 0,18)] x 0,18 ] - 120,00
                         [ [ 880,00 / 0,82 ] x 0,18 ] - 120,00
                         [ 1.073,17 x 0,18 ] - 120
                          193,17 - 120 = 73,17

Obs¹.: Para maiores informações consultar documento: MTZ_Calculo_Diferencial_Aliquota_Lancamento_Automatico.doc
Obs².: O cálculo do DIFAL para o tipo "Material de Consumo - Débito (extras)" é exatamente igual ao do tipo "Material de Consumo - Débito". A diferença é apenas na recuperação das notas, já que a parametrização de CFOP e Natureza de Operação é feita separadamente.


RN06.d
Regra do cálculo para Diferencial de Alíquota- (UF = SP).

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado (menu "Manutenção > Parâmetros por UF");
  E a UF do Estabelecimento for igual à SP;

Aplicar a fórmula abaixo:

O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para SP.


Alteração [MFS859953]: Ajuste da Regra para SP nas Operações de contribuintes optantes pelo simples nacional:


Cálculo do Valor Diferencial Alíquota para estabelecimentos de SP para Contribuintes do Simples Nacional:
  

Cálculo dos Valores


* Base de Cálculo Crédito (Considerada para o cálculo do Valor de Crédito)
Valor Contábil do Item / (1 - Alíquota Interestadual)

* Valor do Crédito:
Base de Cálculo Crédito * Alíquota Interestadual


[MFS938348]

* Base de Cálculo Débito (Considerada para o cálculo do Valor de Débito)
Valor Contábil do Item / (1 - Alíquota Interna)

* Valor do Débito:
Base de Cálculo Débito * Alíquota Interna

* Valor Cálculado = Valor do Débito - Valor do Crédito

* Valor Diferencial Alíquota = Valor Calculado

   Observação: A mesma base de cálculo deve ser utilizada tanto para o débito quanto para o crédito.

A seguir os valores a serem recuperados para os cálculos do Valor de Crédito e do Valor de Débito:
 
 Definição das Alíquotas
* Alíquota Interestadual:
Buscar no Campo 42 da tabela SAFX08 (alíquota do ICMS do item de mercadoria).
* Alíquota Interna:
Buscar no Campo 63 da tabela SAFX08 (alíquota de destino do item de mercadoria).

      Regra de Recuperação da Alíquota Interestadual para a fórmula da Base de Cálculo de Crédito:

	Primeiro verificar se a Alíquota ICMS está preenchida no item de Mercadoria. Se não estiver preenchido, utilizar a Parametrização da Alíquota por CFOP e Produto. Caso a parametrização não seja encontrada, verificar a Parametrização da Alíquota Padrão.
	Critérios para recuperação da Parametrização da Alíquota por CFOP e Produto :
	- Tributo = ICMS
	- UF Origem = 
        Se CST for iniciado por 1, 2, 6 ou 7 (estrangeira), então considerar UF Origem = "EX".
        Se CST for iniciado por 0, 3, 4, ,5 8 (nacional), então considerar UF Origem = UF do fornecedor.
	- UF Destino = UF do Estabelecimento = SP
	- CFOP do Item de Mercadoria
	- Produto do Item de Mercadoria
	Critérios para recuperação da Parametrização Padrão:
	- Tributo = ICMS
	- UF Origem = 
        Se CST for iniciado por 1, 2, 6 ou 7 (estrangeira), então considerar UF Origem = "EX".
        Se CST for iniciado por 0, 3, 4, ,5 8 (nacional), então considerar UF Origem = UF do fornecedor.
	- UF Destino = UF do Estabelecimento = SP

      Regra de Recuperação da Alíquota Interna para a fórmula da Base de Cálculo de Débito:

	Primeiro verificar se a Alíquota Destino está preenchida no item de Mercadoria. Se não estiver preenchido, utilizar a Parametrização da Alíquota por CFOP e Produto. Caso a parametrização não seja encontrada, verificar a Parametrização da Alíquota Padrão. 

     Critérios para recuperação da Parametrização da Alíquota por CFOP e Produto :
	- Tributo = ICMS
	- UF Origem  = UF do Estabelecimento = SP 
	- UF Destino = UF do Estabelecimento = SP
	- CFOP do Item de Mercadoria
	- Produto do Item de Mercadoria
	Critérios para recuperação da Parametrização Padrão:
	- Tributo = ICMS
        - UF Origem  = UF do Estabelecimento = SP
	- UF Destino = UF do Estabelecimento = SP
	
OBS: Em caso de não encontrar as alíquotas parametrizadas (Necessárias para o cálculo dos valores a débito e a crédito) informar os valores zerados e emitir mensagem de Log.

Mensagem de Log: Caso não sejam encontrados os parâmetros da Alíquota por CFOP e Produto ou Alíquota Padrão emitir a seguinte mensagem de Erro:

"Para clientes optantes pelo Simples Nacional os parâmetros de Alíquota por CFOP e Produto ou Alíquota Padrão devem estar preenchidos para cálculo do DIFAL SP."


MFS88013
MFS859953
MFS938348
RN06.e
Regra do cálculo para Diferencial de Alíquota- (UF = ES, BA e SC).

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado (menu "Manutenção > Parâmetros por UF");
  E a UF do Estabelecimento for igual à ES ou BA ou SC;

Aplicar a fórmula abaixo:


O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para ES:


O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para BA:


O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para SC:


RN06.f
Regra do cálculo para Diferencial de Alíquota- (UF = PA).

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado (menu "Manutenção > Parâmetros por UF");
  E a UF do Estabelecimento for igual à PA;

Aplicar a fórmula abaixo:


O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para PA.

Valor do DIFAL =    [Valor da Base de Cálculo - Valor do ICMS x Valor da Alíquota de Destino] - Valor do ICMS
                                  1 - Valor da Alíquota de Destino


MFS435431
RN06.g
Regra do cálculo para Diferencial de Alíquota- (UF = MA).

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado (menu "Manutenção > Parâmetros por UF");
  E a UF do Estabelecimento for igual à MA;

Aplicar a fórmula abaixo:


O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para MA.

Valor do DIFAL =         Base de Cálculo - Valor do ICMS
                                   ( -----------------------------------------------)  x  Dif. de Alíquota ICMS/100
                                           1 - Alíquota Interna/100

Quando estiver sujeito ao adicional relativo ao FUMACOP:
	
	Será identificado através do campo 263 (VLR_FECP_ALIQ_ICMS) descrição: Alíquota FECEP ICMS da tabela SAFX08

Neste caso o Valor da alíquota do FUMACOP será incorporado ao cálculo da fórmula:

Valor do DIFAL =         Base de Cálculo - Valor do ICMS
                               ( ----------------------------------------------------- )  x  Dif. ALiq.(FUMACOP) /100
                                   1 - Alíquota Interna + FUMACOP/100


MFS519100
RN06.h
Regra do cálculo para Diferencial de Alíquota- (UF = RO).

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado (menu "Manutenção > Parâmetros por UF");
  E a UF do Estabelecimento for igual à RO;

Aplicar a fórmula abaixo:


O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para RO.

Valor do DIFAL =      Base de Cálculo - Valor do ICMS
                             [ ( -------------------------------------------------) x Alíquota Interna/100 ] - Valor do ICMS
                                         1 - Alíquota Interna/100

Vigência a partir de: 01/04/2022


MFS564128
RN06.i
Regra do cálculo para Diferencial de Alíquota- (UF = AC).

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado (menu "Manutenção > Parâmetros por UF");
  E a UF do Estabelecimento for igual à AC;

Aplicar a fórmula abaixo:


O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para AC.

Valor do DIFAL =      Base de Cálculo - Valor do ICMS
                             [ ( -------------------------------------------------) x Alíquota de Destino] - Valor do ICMS
                                         1 - Alíquota de Destino

Vigência a partir de: 17/03/2023


MFS569514
RN06.j
Regra do cálculo para Diferencial de Alíquota- (UF = RJ).

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado (menu "Manutenção > Parâmetros por UF");
  E a UF do Estabelecimento for igual à RJ;

Aplicar a fórmula abaixo:


O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para RJ.

Valor do DIFAL =      Base de Cálculo - Valor do ICMS
                             [ ( -------------------------------------------------) x Alíquota de Destino] - Valor do ICMS
                                         1 - Alíquota de Destino


MFS571687
RN06.k
Regra do cálculo para Diferencial de Alíquota- (UF = SE).

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado (menu "Manutenção > Parâmetros por UF");
  E a UF do Estabelecimento for igual à SE;

Aplicar a fórmula abaixo:


O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para SE.

Valor do DIFAL =      Base de Cálculo - Valor do ICMS
                             [ ( -------------------------------------------------) x Alíquota de Destino] - Valor do ICMS
                                         1 - Alíquota de Destino

Vigência a partir de: 01/04/2022


MFS571692
RN06.l
Regra do cálculo para Diferencial de Alíquota- (UF = RR).

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado (menu "Manutenção > Parâmetros por UF");
  E a UF do Estabelecimento for igual à RR;

Aplicar a fórmula abaixo:


O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para RR.

Valor do DIFAL =      Base de Cálculo - Valor do ICMS
                             [ ( -------------------------------------------------) x Alíquota de Destino] - Valor do ICMS
                                         1 - Alíquota de Destino

Vigência a partir de: 01/04/2022

MFS572622
RN06.m
Regra do cálculo para Diferencial de Alíquota- (UF = TO).

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado (menu "Manutenção > Parâmetros por UF");
  E a UF do Estabelecimento for igual à TO;

Aplicar a fórmula abaixo:


O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para TO.

Valor do DIFAL =      Base de Cálculo - Valor do ICMS
                             [ ( -------------------------------------------------) x Alíquota de Destino] - Valor do ICMS
                                         1 - Alíquota de Destino

Vigência a partir de: 29/08/2022

MFS572711
RN06.n
Regra do cálculo para Diferencial de Alíquota- (UF = AM).

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado (menu "Manutenção > Parâmetros por UF");
  E a UF do Estabelecimento for igual à AM;

Aplicar a fórmula abaixo:


O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para AM.

Valor do DIFAL =      Base de Cálculo - Valor do ICMS
                             [ ( -------------------------------------------------) x Alíquota de Destino] - Valor do ICMS
                                         1 - Alíquota de Destino

Vigência a partir de: 01/04/2023

MFS573401
RN06.o
Regra do cálculo para Diferencial de Alíquota- (UF = AP).

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado (menu "Manutenção > Parâmetros por UF");
  E a UF do Estabelecimento for igual à AP;

Aplicar a fórmula abaixo:


O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para AP.

Valor do DIFAL =      Base de Cálculo - Valor do ICMS
                             [ ( -------------------------------------------------) x Alíquota de Destino] - Valor do ICMS
                                         1 - Alíquota de Destino

Vigência a partir de: 30/08/2022

MFS573416
RN06.p
Regra do cálculo para Diferencial de Alíquota- (UF = PE).

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado (menu "Manutenção > Parâmetros por UF");
  E a UF do Estabelecimento for igual à PE;

Aplicar a fórmula abaixo:


O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para AP.

Valor do DIFAL =      Base de Cálculo - Valor do ICMS
                              ( ---------------------------------------------) x Dif. de Alíquota ICMS
                                         1 - Alíquota de Destino

Vigência a partir de: 01/04/2017

MFS573406
RN06.q
Regra do cálculo para Diferencial de Alíquota- (UF = MS).

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado (menu "Manutenção > Parâmetros por UF");
  E a UF do Estabelecimento for igual à MS;

Aplicar a fórmula abaixo:


Valor Calculado =      Base de Cálculo - Valor do ICMS
                             [ ( -------------------------------------------------) x Alíquota de Destino] - Valor do ICMS
                                         1 - Alíquota de Destino

       Valor Diferencial Alíquota = Valor Calculado 

     Em caso de FECOMP de MS:

       Valor com FECOMP = [Base de Cálculo - Valor do ICMS  _]  *  Alíquota FECEP ICMS 
                                             1 - Valor da Alíquota de Destino

       Valor Diferencial Alíquota  = Valor Calculado - Valor com FECOMP

Vigência a partir de: 01/04/2023

MFS573412
RN06.r
Regra do cálculo para Diferencial de Alíquota- (UF = PI).

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado (menu "Manutenção > Parâmetros por UF");
  E a UF do Estabelecimento for igual à PI;

Aplicar a fórmula abaixo:


O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para PI.

Valor do DIFAL =      Base de Cálculo - Valor do ICMS
                             [ ( -------------------------------------------------) x Alíquota de Destino] - Valor do ICMS
                                         1 - Alíquota de Destino

Vigência a partir de: 08/03/2023

MFS576319
RN06.s
Regra do cálculo para Diferencial de Alíquota- (UF = AL).

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado (menu "Manutenção > Parâmetros por UF");
  E a UF do Estabelecimento for igual à AL;

Aplicar a fórmula abaixo:


O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para AL.

Valor do DIFAL =      Base de Cálculo - Valor do ICMS
                             [ ( -------------------------------------------------) x Alíquota de Destino] - Valor do ICMS
                                         1 - Alíquota de Destino

Vigência a partir de: 01/01/2016

MFS576330
RN06.t
Regra do cálculo para Diferencial de Alíquota- (UF = PB).

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado (menu "Manutenção > Parâmetros por UF");
  E a UF do Estabelecimento for igual à PB;

Aplicar a fórmula abaixo:


O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para PB.

Valor do DIFAL =      Base de Cálculo - Valor do ICMS
                              ( ---------------------------------------------) x Dif. de Alíquota ICMS
                                         1 - Alíquota de Destino

Vigência a partir de: 01/04/2020

MFS593347
RN06.u
Regra do cálculo para Diferencial de Alíquota- (UF = RN).

Regra para obtenção do valor a débito:

Se o parâmetro 92 estiver marcado (menu "Manutenção > Parâmetros por UF");
  E a UF do Estabelecimento for igual à RN;

Aplicar a fórmula abaixo:


O cálculo do DIFAL passará a considerar regra de cálculo com base dupla disponibilizada para AL.

Valor do DIFAL =      Base de Cálculo - Valor do ICMS
                             [ ( -------------------------------------------------) x Alíquota de Destino] - Valor do ICMS
                                         1 - Alíquota de Destino

Vigência a partir de: 22/03/2024

MFS844874
RN07
Tratamento do parâmetro "Somente documentos com diferencial":

Se o parâmetro "Somente documentos com diferencial" estiver desmarcado
     Todas as notas fiscais devem ser consideradas para o relatório, de acordo com os parâmetros de tela
Senão
      Serão consideradas somente as notas fiscais em que a coluna Valor Diferença da Alíquota do relatório for maior  
      que zero.

As notas fiscais que devem ser consideradas para calcular a coluna do Valor Diferença da Alíquota, devem ter o campo Valor da Alíquota de Destino (campo 63 da SAFX08) ou o campo Diferença Alíquota ICMS (campo 44 da SAFX08)  preenchido no item de mercadoria, se o parâmetro Base de Cálculo p/ Dif. Aliquota** for igual a 1, 2 ou 3.
Se o parâmetro Base de Cálculo p/ Dif. Aliquota for igual a 4, o campo Valor Diferença Alíquotas ICMS - Ativo / Material Consumo (campo 69 da SAFX08) deve estar preenchido no item de mercadoria.

Alteração [MFS859953]

Regra para Pessoa Física e Jurídia optante do Simples Nacional para UF SP:

Considerar na seleção das Notas os clientes optantes pelo Simples Nacional para UF de São Paulo:

No cadastro da tabela SAFX04 o campo 43 (IND_SIMPLES_NAC) de Enquadramento do Simples Nacional deve estar marcado.


** A parametrização da Base de Cálculo do Diferencial de Alíquota deve ser realizada no seguinte caminho: Módulo Ferramentas, item de menu Parâmetros do Sistema > Parâmetros por Estabelecimento.

MFS589832
MFS859953


Considerações deste modelo:

Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[EXCLUÍDA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:

RN01
[ALTERADA - OSXPTO] Descrição da Regra de Negócio 01
OSNNNN

