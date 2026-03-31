# MSAF_DWECF_Roteiro_Utilizacao

> Fonte: MSAF_DWECF_Roteiro_Utilizacao.docx





MASTERSAF
ECF - Escrituração Contábil Fiscal (DW)

ROTEIRO DE UTILIZAÇÃO

SUMÁRIO




## INTRODUÇÃO


Este documento tem como objetivo fornecer as orientações iniciais para a geração da Escrituração Contábil Fiscal no produto MastersafDW, módulo ECF - Escrituração Contábil Fiscal (DW).

O módulo ECF foi criado para possibilitar a entrega das informações da Escrituração Fiscal Digital do Imposto sobre a Renda e da Contribuição Social sobre o Lucro Líquido da Pessoa Jurídica, que foi instituída pela Instrução Normativa RFB nº 1.353/2013.

PRÉ-REQUISITOS
















































































-


–








-
















- –















ETAPAS REALIZADAS NO PRODUTO PARA A IMPLANTAÇÃO DO MÓDULO ECF - ESCRITURAÇÃO CONTÁBIL FISCAL (DW)

### PROCEDIMENTOS PARA REALIZAR O CÁLCULO DE ECF


#### ETAPAS NECESSÁRIAS PARA EMPRESAS DO LUCRO REAL PJ EM GERAL


TABELA DINÂMICA

A associação com base na Tabela Dinâmica citada no item 2 do tópico  PROCEDIMENTOS PARA REALIZAR O CÁLCULO DE ECF , deve ser realizada para os registros M300A, M350A e os demais registros quando aplicável L210, N500, N600, N610, N620, N630A, N660 e N670.

PLANO REFERENCIAL

A associação com base no Plano Referencial citada no item 3 do tópico PROCEDIMENTOS PARA REALIZAR O CÁLCULO DE ECF ,deve ser realizada para os registros correspondentes L100A e L300A.

#### ETAPAS NECESSÁRIAS PARA EMPRESAS DO SEGMENTO FINANCEIRO


TABELA DINÂMICA

A associação com base na Tabela Dinâmica citada no item 2 do tópico PROCEDIMENTOS PARA REALIZAR O CÁLCULO DE ECF, deve ser realizada para os registros M300B, M350B e os demais registros quando aplicável L210, N500, N600, N610, N620, N630B, N660 e N670.
PLANO REFERENCIAL

A associação com base no Plano Referencial citada no item 3 do tópico PROCEDIMENTOS PARA REALIZAR O CÁLCULO DE ECF,  deve ser realizada para os registros correspondentes L100B e L300B.

#### ETAPAS NECESSÁRIAS PARA SEGURADORAS


TABELA DINÂMICA

A associação com base na Tabela Dinâmica citada no item 2 do tópico PROCEDIMENTOS PARA REALIZAR O CÁLCULO DE ECF, deve ser realizada para os registros M300C, M350C e os demais registros quando aplicável L210, N500, N600, N610, N620, N660 e N670.

PLANO REFERENCIAL

A associação com base no Plano Referencial citada no item 2 do tópico PROCEDIMENTOS PARA REALIZAR O CÁLCULO DE ECF, devem ser realizadas para os registros correspondentes L100C e L300C.




PROCEDIMENTOS PARA REALIZAR O CÁLCULO DE ECF

- Realizar as importações obrigatórias das tabelas referenciadas no item PRE-REQUISITOS e avaliar a necessidade realizar importações opcionais;

- Associar o Plano da Empresa (Conta Contábil e Centro de Custo) com as linhas da Tabela Dinâmica e Estabelecimentos (de acordo com a forma de tributação escolhida pela empresa/estabelecimento). Esta associação é possível ser realizada através de importação. Além disso, permitimos indicar um percentual que será aplicado nas contas contábeis associadas à linha 2 dos Registros N500 e N650;

- Associar o Plano da Empresa (Conta Contábil e Centro de Custo) com o Plano Referencial disponibilizado pela RFB (de acordo com a forma de tributação escolhida pela empresa/estabelecimento). O Plano Referencial é utilizado em registros como K155, K355, L100, L300, P100, P100B, P150, P150B, U100 e U150. Para esta associação, é possível realizar importação;

- Associar subcontas correlatas com o Plano Empresa para a geração do registro J053.
- Associar Contas da Parte B com Contas da Parte A com as linhas da tabela dinâmica Estabelecimentos para a realização de ajustes automáticos nas contas da Parte B.

- Cadastrar Recuperação de Valores – Apuração IRPJ/CSLL e associar Estabelecimentos, os dados informados nessa tela são utilizados para a recuperação do Saldo das Contas Contábeis utilizados na apuração dos impostos IRPJ/CSLL para os Registros correspondes ao Bloco M;

- Cadastrar Informações ECF por Empresa e Exercício ou Situação Especial, os dados informados nesta tela são utilizados como base para a geração de cada arquivo;

- Cadastrar uma Abertura da Apuração para cada período mensal de apuração, , para garantir a execução do processo desde a transcrição dos valores empresa para referencias fisco até a realização dos cálculos; complementando com dados adicionais que podem variar de período a período tais como: Tipo de Receita, Método de Avaliação do Estoque, Cálculo das Contas Parte A e da Parte B, entre outros;


- Informar base de cálculo para Incentivos Fiscais correspondentes ao FINOR e FINAM quando aplicável;


- Executar o Processamento em Lote (Transcrição dos Valores Empresa para Referenciais do Fisco/Manter Ajustes Manuais Realizados), com base nas associações; ou (Transcrição dos Valores Empresa para Referenciais do Fisco/Manter Ajustes Manuais Realizados / Os saldos, movimentos são atualizados nas contas referenciais e/ou linhas das tabelas dinâmicas para atender os padrões definidos pela RFB.

- Realizar o rateio do Bloco K, quando uma conta contábil está associada em mais de uma conta referencial, através da Tela Balanço/DRE (Balanço K).

- Ajustar o percentual de rateio quando se tratar de Empresas que possuem Atividades Mistas, quando aplicável, através da Tela Percentuais de Rateio das Atividades Mistas;

- Utilizar a tela Entrada Manual de Valores quando houver a necessidade de inserir um valor em uma linha da Tabela Dinâmica que não possui uma conta contábil atrelada ou mesmo deve ser realizado um ajuste também é possível atribuir valor em percentual na linha 2 dos Registros N500 e N650.

- Cadastrar contas da Parte B

- Realizar os ajustes manuais e associações necessárias nos Lançamentos da Parte A;

- Executar o Processamento em Lote (Execução das Fórmulas/Cálculo) para atualização das linhas que possuem fórmulas;

- Parametrizar o tipo de receita escolhido com base nos valores exibidos na tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução;

- Telas de Demonstração do Resultado (Lucro Real): Visualizar as informações a serem apresentadas no arquivo;

- Cadastrar Informações Econômicas - Bloco X e Informações Gerais - Bloco Y: nessa tela, os registros são inseridos manualmente ou por meio da funcionalidade de Importação.

- Cadastrar Declaração País a País (Bloco W) nessa tela, os registros são inseridos manualmente ou por meio da funcionalidade de Importação;

- Cadastrar Declaração DEREX (Bloco V) nessa tela, os registros são inseridos manualmente ou por meio da funcionalidade de Importação;


- Cadastrar na tela Perfil de Geração, os registros que devem conter no arquivo da ECF que será enviado para o Fisco são parametrizados. Este perfil, deverá ser associado na tela Informações ECF.
- Gerar relatórios para realizar conferências;

- Gerar Arquivo da ECF.

#### ETAPAS REALIZADAS NO PRODUTO ECF - PROCESSAMENTO PERIÓDICO DOS DADOS (MENSALE/OU SITUAÇÃO ESPECIAL)


- Avaliar a necessidade de realizar alguma importação obrigatória, por exemplo, Importação dos Saldos Contábeis e/ou realizar alguma importação opcional;

- Avaliar possíveis ajustes ou criação de parametrização na tela Informações ECF. Caso exista o cenário de Situação Especial, é possível realizar a cópia parametrização existente para uma nova parametrização em Informações ECF;
- Cadastrar para cada período de apuração, Trimestral ou Mensal, uma Abertura da Apuração, complementando com dados adicionais que podem variar de período a período tais como:  Tipo de Receita, Método de Avaliação do Estoque , Cálculo das Contas Parte A e da Parte B, entre outros, para garantir a execução do processo desde a transcrição dos valores empresa para referencias fisco até a realização dos cálculos ou criar Cópia de Abertura a partir de uma abertura da apuração existente por meio da funcionalidade Cópia de Abertura em Lote.
- Atualizar as associações parametrizadas quando aplicável;

- Realizar cadastro na tela PAT – Períodos Anteriores ao DW para informar os valores que ainda faltam ser compensados que foram apurados/controlados em períodos anteriores.

- Executar o Processamento em Lote (Transcrição dos Valores Empresa para Referenciais do Fisco/Manter Ajustes Manuais Realizados), com base nas associações ou (Transcrição dos Valores Empresa para Referenciais do Fisco/Manter Ajustes Manuais Realizados. Os saldos, movimentos são atualizados nas contas referencias e/ou linhas das tabelas dinâmicas para atender os padrões definidos pela RFB.

- Realizar o rateio do Bloco K, quando uma conta contábil está associada em mais de uma conta referencial.
- Ajustar o percentual de rateio quando se tratar de Empresas que possuem Atividades Mistas quando aplicável;

- Utilizar a tela de Entrada Manual de Valores quando houver a necessidade de inserir um valor em uma linha da Tabela Dinâmica que não possui uma conta contábil atrelada ou mesmo deve ser realizado um ajuste também é possível atribuir valor em percentual na linha 2 dos Registros N500 e N650;


- Realizar ajustes nas contas da parte B;

- Realizar os ajustes manuais e associações necessárias nos Lançamentos da Parte A;


- Informar base de cálculo para Incentivos Fiscais correspondentes ao FINOR e FINAM quando aplicável;


- Executar o Processamento em Lote (Execução das Fórmulas/Cálculo) para atualização das linhas que possuem fórmulas;

- Parametrizar o tipo de receita escolhido com base nos valores exibidos na tela Comparativo entre Receita Bruta X Balanço de Suspensão/Redução;

- Telas de Demonstração do Resultado: Visualizar as informações que a serem apresentadas no arquivo;

- Gerar relatórios para realizar conferências;


SUPORTE TÉCNICO

Para dúvidas ou problemas, abra um chamado no Contact Center ou entre em contato com nossa equipe de Suporte Técnico pelo Telefone:
 (11) 2159-0600 opção 01 (Atendimento das Soluções Fiscais).
Nosso horário de atendimento é de segunda à sexta-feira de 9h às 18h.