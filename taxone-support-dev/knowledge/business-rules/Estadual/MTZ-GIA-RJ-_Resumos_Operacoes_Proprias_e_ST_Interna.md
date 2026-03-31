# MTZ-GIA-RJ- Resumos Operações Próprias e ST Interna

> Fonte: MTZ-GIA-RJ- Resumos Operações Próprias e ST Interna.docx






THOMSON REUTERS

Módulo GIA ICMS - RJ

Resumos das Operações Próprias e Substituição Tributária Interna


Localização: Menu Estadual, Módulo GIA-RJ, item Obrigações  Meio Magnético




DOCUMENTO DE REQUISITO


Sumário

1.	Regras Gerais	2
2.	Recuperação dos Dados	3
3.	Preenchimento dos Campos - Resumo Operações Próprias	5
4.	Preenchimento dos Campos – Resumo Substituição Tributária Interna	9

## Regras Gerais


O relatório foi criado contendo dois resumos:

- Resumo - Operações Próprias;
- Resumo - Substituição Tributária Interna;

O relatório está disponível na funcionalidade de Geração do Meio Magnético (vide MTZ_GIA_RJ_Geracao_do_Meio_Magnetico.docx).

Nesta opção, o sistema gera o arquivo magnético e o relatório dos resumos das Operações Próprias e de Substituição Tributária Interna.
Ao final da geração do meio magnético, o relatório é disponibilizado para visualização em tela, na aba “Resumo Operações Próprias / ST Interna”, e é gravado automaticamente em arquivo formato “psr”, no diretório informado na tela e com o nome informado no campo Arquivo Resumos da tela.

Como padrão do MasterSAF DW esse relatório também pode impresso e ser salvo em outros formatos.

Os resumos apresentam totalizações de valores contidos em registros gerados no arquivo magnético.
Não pode haver divergência entre os valores informados no arquivo magnético e os apresentados de forma totalizada nos resumos.

As informações destes resumos são geradas a partir dos valores apresentados em diversos registros da Apuração da GIA-RJ:
- 0120 - Movimentação de Entradas
- 0130 - Movimentação de Saídas
- 0140 - Movimentação de Outros débitos
- 0150 - Movimentação de Estornos Crédito 
- 0160 - Movimentação de Outros Créditos 
- 0170 - Movimentação de Estornos Débito 
- 0180 - Movimentação de Deduções
- 0110 - Registro de Identificação da Declaração

Devido a alta complexidade de gerar os resumos a partir da leitura direta das linhas do arquivo do meio magnético, decidimos gerá-los com base  nas tabelas que armazenam os registros mencionados. Mesmo assim temos como premissa que eles reflitam os valores contidos no arquivo magnético. Não pode haver divergência!

A tela de geração do meio magnético possibilita que mais de um estabelecimento possa ser selecionado. Nesse caso, vários arquivos do meio magnético são gravados, um para cada estabelecimento. No caso do relatório, apenas um arquivo é gerado, contendo os resumos de todos os estabelecimentos.

Os resumos acima citados apresentam os mesmos dados dos resumos gerados no programa da GIA ICMS do RJ.  O objetivo é auxiliar a conferência dos dados antes da transmissão do arquivo.





## Recuperação dos Dados



Recuperar os dados do Parâmetro da Apuração da GIA (vide menu Parâmetros >> Por Apuração da GIA) considerando os seguintes critérios:
Empresa de login
Estabelecimento informados na Tela de Geração do Meio Magnético.
Período (mês/ano) informados na Tela de Geração do Meio Magnético.

Com o Parâmetro da Apuração da Gia recuperado, fazer a recuperação os registros listados abaixo.
Tais registros são criados na Apuração Gia através da geração dos registros (vide de menu Obrigações >> Geração >> Geração dos Registros) ou digitados manualmente (vide de menu Obrigações >> Manutenção).

Recuperação dos Registros que compõe os resumos:
0120 - Movimentação de Entradas (vide Obrigações >> Manutenção >> Entradas e Saídas – Reg. 0120 e 0130)
0130 - Movimentação de Saídas (vide Obrigações >> Manutenção >> Entradas e Saídas – Reg. 0120 e 0130)
0140 - Movimentação de Outros débitos (vide Obrigações >> Manutenção >> Estorno e Outros Deb/Cred. Prazo Esp., Outros ICMS Dev – Reg. 0140 a 0200)
0150 - Movimentação de Estornos Crédito (vide Obrigações >> Manutenção >> Estorno e Outros Deb/Cred. Prazo Esp., Outros ICMS Dev – Reg. 0140 a 0200)
0160 - Movimentação de Outros Créditos (vide Obrigações >> Manutenção >> Estorno e Outros Deb/Cred. Prazo Esp., Outros ICMS Dev – Reg. 0140 a 0200)
0170 - Movimentação de Estornos Débito (vide Obrigações >> Manutenção >> Estorno e Outros Deb/Cred. Prazo Esp., Outros ICMS Dev – Reg. 0140 a 0200)
0180 - Movimentação de Deduções (vide Obrigações >> Manutenção >> Estorno e Outros Deb/Cred. Prazo Esp., Outros ICMS Dev – Reg. 0140 a 0200)
0110 - Registro de Identificação da Declaração





## Preenchimento dos Campos - Resumo Operações Próprias


Layout:



Preenchimento dos dados:























## Preenchimento dos Campos – Resumo Substituição Tributária Interna


Layout:



Preenchimento dos dados:





= = = = = =

| OS/CH | Nome | Descrição | Data |
| --- | --- | --- | --- |
| MFS15084 | Criação do Relatório | Inclusão de relatório contendo os resumos: “Operações Próprias” e “Substituição Tributária Interna”. | 28/01/2019 (criação do doc) |
| MFS26774 | Andréa Rocha | Alteração do cálculo do Saldo Credor a Transportar. | 13/05/2019 |
|  |  |  |  |


| Resumo – Operações Próprias   Totais das Entradas:      Valor Contábil             Base de Cálculo               Imposto               Operações Isentas     Outras Operações                                     999.999.999.999,99    999.999.999.999,99    999.999.999.999,99    999.999.999.999,99    999.999.999.999,99  Totais das Saídas:         Valor Contábil             Base de Cálculo               Imposto               Operações Isentas     Outras Operações                                     999.999.999.999,99    999.999.999.999,99    999.999.999.999,99    999.999.999.999,99    999.999.999.999,99                                 Débito do Imposto:                                                                     Crédito do Imposto:          001-Por saídas com débito: 999.999.999.999,99            006-Por entradas com crédito:              999.999.999.999,99         002-Outros débitos:             999.999.999.999,99            007-Outros Créditos:                             999.999.999.999,99         003-Estornos de créditos:    999.999.999.999,99            008-Estornos de débitos:                      999.999.999.999,99         005-Total:                             999.999.999.999,99            010-Subtotal:                                         999.999.999.999,99                                                                                                  011-Saldo Credor do período anterior: 999.999.999.999,99                                                                                                  012-Total:                                              999.999.999.999,99                                                                                   Apuração dos Saldos:                                                                013-Saldo Devedor:                     999.999.999.999,99                                                              014-Deduções:                             999.999.999.999,99                                                              015-Imposto a recolher:               999.999.999.999,99                                                              016-Saldo Credor a Transportar: 999.999.999.999,99 |
| --- |


| Total das entradas | Valor Contábil | Total do campo “Valor Contábil” dos registros Tipo 0120 (Entradas) |
| --- | --- | --- |
| Total das entradas | Base de Cálculo | Total do campo “Valor da Base de Cálculo” dos registros Tipo 0120 (Entradas) |
| Total das entradas | Imposto | Total do campo “Valor do Imposto” dos registros Tipo 0120 (Entradas) |
| Total das entradas | Operações Isentas | Total do campo “Valor de Operações Isentas” dos registros Tipo 0120 (Entradas) |
| Total das entradas | Outras Operações | Total do campo “Valor de Outras Operações” dos registros Tipo 0120 (Entradas) |
| Total das saídas | Valor Contábil | Total do campo “Valor Contábil” dos registros Tipo 0130 (Saídas) |
| Total das saídas | Base de Cálculo | Total do campo “Valor da Base de Cálculo” dos registros Tipo 0130 (Saídas) |
| Total das saídas | Imposto | Total do campo “Valor do Imposto” dos registros Tipo 0130 (Saídas) |
| Total das saídas | Operações Isentas | Total do campo “Valor de Operações Isentas” dos registros Tipo 0130 (Saídas) |
| Total das saídas | Outras Operações | Total do campo “Valor de Outras Operações” dos registros Tipo 0130 (Saídas) |
| Débito do Imposto | 001-Por saídas com débito | Total do campo “Valor do Imposto” dos registros Tipo 0130 (Saídas)  (Mesmo valor lançado no campo “Total das Saídas – Imposto”) |
| Débito do Imposto | 002-Outros débitos | Total do campo “Valor de Outro Débito” dos registros Tipo 0140 (Outros Débitos), considerando apenas as linhas cujo campo “Sequencial da Ocorrência” tenha um código que corresponda a um código de amparo legal iniciado por “N” (tabela Amparo/Texto/Ocorrência x Código GIA-RJ).  OBS.: No caso do estado do RJ, os lançamentos complementares têm o amparo legal preenchido conforme a tabela Amparo/Texto/Ocorrência x Código GIA-RJ. Mas o código do amparo legal não consta no layout do arquivo da GIA RJ, pois a informação que vai para o arquivo é um outro código desta tabela, que corresponde ao campo “Código Amparo da GIA”. A necessidade de verificar o código do amparo legal na tabela Amparo/Texto/Ocorrência x Código GIA-RJ, é para verificar se o código do amparo legal se refere à apuração do ICMS próprio ou do ICMS-ST. Os códigos iniciados por “N” são ajustes do ICMS próprio, e os iniciados por “S”, ajustes de ICMS-ST. É preciso filtrar corretamente as linhas do arquivo texto, para totalizar os valores que devem ir para o resumo das operações próprias, e os que devem ir para o resumo da substituição tributária interna. |
| Débito do Imposto | 003-Estornos de créditos | Total do campo “Valor de Estorno de Crédito” dos registros Tipo 0150 (Estorno de Crédito), considerando apenas as linhas cujo campo “Sequencial da Ocorrência” tenha um código que corresponda a um código de amparo legal iniciado por “N” (tabela Amparo/Texto/Ocorrência x Código GIA-RJ).  (Ver obs acima, campo 002-Outros débitos) |
| Débito do Imposto | 005-Total | Total dos campos: 001 + 002 + 003 |
| Crédito do Imposto | 006-Por entradas com crédito | Total do campo “Valor do Imposto” dos registros Tipo 0120 (Entradas)  (Mesmo valor lançado no campo “Total das Entradas – Imposto”) |
| Crédito do Imposto | 007-Outros Créditos | Total do campo “Valor de Outro Crédito” dos registros Tipo 0160 (Outros Créditos), considerando apenas as linhas cujo campo “Sequencial da Ocorrência” tenha um código que corresponda a um código de amparo legal iniciado por “N” (tabela Amparo/Texto/Ocorrência x Código GIA-RJ).  (Ver obs acima, campo 002-Outros débitos) |
| Crédito do Imposto | 008-Estornos de débitos | Total do campo “Valor de Estorno Débito” dos registros Tipo 0170 (Estorno de Débito), considerando apenas as linhas cujo campo “Sequencial da Ocorrência” tenha um código que corresponda a um código de amparo legal iniciado por “N” (tabela Amparo/Texto/Ocorrência x Código GIA-RJ).  (Ver obs acima, campo 002-Outros débitos) |
| Crédito do Imposto | 010-Subtotal | Total dos campos: 006 + 007 + 008 |
| Crédito do Imposto | 011-Saldo Credor do período anterior | Conteúdo do campo “Valor do Saldo Anterior” do registro Tipo 0110 (Registro de Identificação da Declaração). |
| Crédito do Imposto | 012-Total | Total dos campos: 010 + 011 |
| Apuração dos Saldos | 013-Saldo Devedor | Este campo será preenchido com o total dos débitos (campos 005) menos o total dos créditos (campo 012), mas apenas quando resultar um valor superior a zero.   Caso contrário, será preenchido com zeros. |
| Apuração dos Saldos | 014-Deduções | Total do campo “Valor de Dedução” dos registros Tipo 0180 (Deduções), considerando apenas as linhas cujo campo “Sequencial da Ocorrência” tenha um código que corresponda a um código de amparo legal iniciado por “N” (tabela Amparo/Texto/Ocorrência x Código GIA-RJ).  (Ver obs acima, campo 002-Outros débitos) |
| Apuração dos Saldos | 015-Imposto a recolher | Este campo será preenchido apenas quando o saldo devedor (campo 13) for > zeros.         Conteúdo = Saldo Devedor (campos 013) - Deduções (campo 014)  Quando este resultado for um valor negativo, não haverá imposto a recolher, e por isso, este campo será gerado com zeros. |
| Apuração dos Saldos | 016-Saldo Credor a Transportar | Este campo será preenchido com o total dos créditos (campos 012) menos o total dos débitos (campo 005), mas apenas quando resultar um valor superior a zero.   [MFS26774] Conteúdo = Total dos créditos (campo 012) - Total dos débitos (campo 005) +                         Deduções (campo 014)  Caso contrário, será preenchido com zeros. |


| Resumo - Substituição Tributária Interna   Totais das Entradas:     Base de Cálculo              Imposto                                      999.999.999.999,99   999.999.999.999,99  Totais das Saídas:          Base de Cálculo               Imposto                                     999.999.999.999,99    999.999.999.999,99                                 Débito do Imposto:                                                                     Crédito do Imposto:          001-Por saídas com débito: 999.999.999.999,99            006-Por entradas com crédito:              999.999.999.999,99         002-Outros débitos:             999.999.999.999,99            007-Outros Créditos:                             999.999.999.999,99         003-Estornos de créditos:    999.999.999.999,99            008-Estornos de débitos:                      999.999.999.999,99         005-Totais:                           999.999.999.999,99            010-Subtotal:                                         999.999.999.999,99                                                                                                  011-Saldo Credor do período anterior: 999.999.999.999,99                                                                                                  012-Total:                                              999.999.999.999,99                                                                                  Apuração dos Saldos:                                                                013-Saldo Devedor:                     999.999.999.999,99                                                              014-Deduções:                             999.999.999.999,99                                                              015-Imposto a recolher:               999.999.999.999,99                                                              016-Saldo Credor a Transportar: 999.999.999.999,99 |
| --- |


| Total das entradas | Base de Cálculo | Total do campo “Valor da Base de Cálculo ST” de todos os registros Tipo 0120 (Entradas) que atendam a seguinte condição: o CFOP deve ser de operação interna (o conteúdo do campo Código Fiscal de Operação deve iniciar por “1”). |
| --- | --- | --- |
| Total das entradas | Imposto | Total do campo “Valor do Imposto Retido ST” de todos os registros Tipo 0120 (Entradas) que atendam a seguinte condição: o CFOP deve ser de operação interna (o conteúdo do campo Código Fiscal de Operação deve iniciar por “1”). |
| Total das saídas | Base de Cálculo | Total do campo “Valor da Base de Cálculo ST” de todos os registros Tipo 0130 (Saídas) que atendam a seguinte condição: o CFOP deve ser de operação interna (o conteúdo do campo Código Fiscal de Operação deve iniciar por “5”). |
| Total das saídas | Imposto | Total do campo “Valor do Imposto Retido ST” de todos os registros Tipo 0130 (Saídas) que atendam a seguinte condição: o CFOP deve ser de operação interna (o conteúdo do campo Código Fiscal de Operação deve iniciar por “5”). |
| Débito do Imposto | 001-Por saídas com débito | Total do campo “Valor do Imposto Retido ST” de todos os registros Tipo 0130 (Saídas) que atendam a seguinte condição: o CFOP deve ser de operação interna (o conteúdo do campo Código Fiscal de Operação deve iniciar por “5”).  (Mesmo valor lançado no campo “Total das Saídas – Imposto”) |
| Débito do Imposto | 002-Outros débitos | Total do campo “Valor de Outro Débito” dos registros Tipo 0140 (Outros Débitos), considerando apenas as linhas cujo campo “Sequencial da Ocorrência” tenha um código que corresponda a um código de amparo legal iniciado por “S” (tabela Amparo/Texto/Ocorrência x Código GIA-RJ).  OBS.: No caso do estado do RJ, os lançamentos complementares têm o amparo legal preenchido conforme a tabela Amparo/Texto/Ocorrência x Código GIA-RJ. Mas o código do amparo legal não consta no layout do arquivo da GIA RJ, pois a informação que vai para o arquivo é um outro código desta tabela, que corresponde ao campo “Código Amparo da GIA”. A necessidade de verificar o código do amparo legal na tabela Amparo/Texto/Ocorrência x Código GIA-RJ, é para verificar se o código do amparo legal se refere à apuração do ICMS próprio ou do ICMS-ST. Os códigos iniciados por “N” são ajustes do ICMS próprio, e os iniciados por “S”, ajustes de ICMS-ST. É preciso filtrar corretamente as linhas do arquivo texto, para totalizar os valores que devem ir para o resumo das operações próprias, e os que devem ir para o resumo da substituição tributária interna. |
| Débito do Imposto | 003-Estornos de créditos | Total do campo “Valor de Estorno de Crédito” dos registros Tipo 0150 (Estorno de Crédito), considerando apenas as linhas cujo campo “Sequencial da Ocorrência” tenha um código que corresponda a um código de amparo legal iniciado por “S” (tabela Amparo/Texto/Ocorrência x Código GIA-RJ).  (Ver obs acima, campo 002-Outros débitos) |
| Débito do Imposto | 005-Total | Total dos campos: 001 + 002 + 003 |
| Crédito do Imposto | 006-Por entradas com crédito | Total do campo “Valor do Imposto Retido ST” de todos os registros Tipo 0120 (Entradas) que atendam a seguinte condição: o CFOP deve ser de operação interna (o conteúdo do campo Código Fiscal de Operação deve iniciar por “1”).  (Mesmo valor lançado no campo “Total das Entradas – Imposto”) |
| Crédito do Imposto | 007-Outros Créditos | Total do campo “Valor de Outro Crédito” dos registros Tipo 0160 (Outros Créditos), considerando apenas as linhas cujo campo “Sequencial da Ocorrência” tenha um código que corresponda a um código de amparo legal iniciado por “S” (tabela Amparo/Texto/Ocorrência x Código GIA-RJ).  (Ver obs acima, campo 002-Outros débitos) |
| Crédito do Imposto | 008-Estornos de débitos | Total do campo “Valor de Estorno Débito” dos registros Tipo 0170 (Estorno de Débito), considerando apenas as linhas cujo campo “Sequencial da Ocorrência” tenha um código que corresponda a um código de amparo legal iniciado por “S” (tabela Amparo/Texto/Ocorrência x Código GIA-RJ).  (Ver obs acima, campo 002-Outros débitos) |
| Crédito do Imposto | 010-Subtotal | Total dos campos: 006 + 007 + 008 |
| Crédito do Imposto | 011-Saldo Credor do período anterior | Conteúdo do campo “Valor do Saldo Anterior ST” do registro Tipo 0110 (Registro de Identificação da Declaração). |
| Crédito do Imposto | 012-Total | Total dos campos: 010 + 011 |
| Apuração dos Saldos | 013-Saldo Devedor | Este campo será preenchido com o total dos débitos (campos 005) menos o total dos créditos (campo 012), mas apenas quando resultar um valor superior a zero.   Caso contrário, será preenchido com zeros. |
| Apuração dos Saldos | 014-Deduções | Total do campo “Valor de Dedução” dos registros Tipo 0180 (Deduções), considerando apenas as linhas cujo campo “Sequencial da Ocorrência” tenha um código que corresponda a um código de amparo legal iniciado por “S” (tabela Amparo/Texto/Ocorrência x Código GIA-RJ).  (Ver obs acima, campo 002-Outros débitos) |
| Apuração dos Saldos | 015-Imposto a recolher | Este campo será preenchido apenas quando o saldo devedor (campo 13) for > zeros.         Conteúdo = Saldo Devedor (campos 013) - Deduções (campo 014)  Quando este resultado for um valor negativo, não haverá imposto a recolher, e por isso, este campo será gerado com zeros. |
| Apuração dos Saldos | 016-Saldo Credor a Transportar | Este campo será preenchido com o total dos créditos (campos 012) menos o total dos débitos (campo 005), mas apenas quando resultar um valor superior a zero.   [MFS26774] Conteúdo = Total dos créditos (campo 012) - Total dos débitos (campo 005) +                         Deduções (campo 014)  Caso contrário, será preenchido com zeros. |
