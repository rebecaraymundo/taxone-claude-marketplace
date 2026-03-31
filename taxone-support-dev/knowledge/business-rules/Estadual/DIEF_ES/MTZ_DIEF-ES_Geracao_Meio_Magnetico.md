# MTZ_DIEF-ES_Geracao_Meio_Magnetico

- **Fonte:** MTZ_DIEF-ES_Geracao_Meio_Magnetico.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 68 KB

---

THOMSON REUTERS

DIEF\-ES

Geração do Meio Magnético

##### DOCUMENTO DE REQUISITO

__MFS/CH__

__Nome__

__Descrição__

CH15409\_2016

Julyana Perrucini

Este documento tem como objetivo alterar a geração dos campos Descrição Outro ICMS e Valor Outro ICMS, para considerar o campo 25 da tela de Informações Complementares\.

MFS\-13823

Julyana Perrucini

Este documento tem como objetivo atender a nova versão 2017\.4 da DIEF\.

REGRAS DE NEGÓCIO

###### __CÓD__

###### __DESCRIÇÃO__

__MFS/CH__

RN01

Para o Registro Tipo 2, o sistema deve seguir os mesmos parâmetros de geração do arquivo magnético “DIA\-ES”\.

OS2203

RN01\.1

O DIEF será gerado, mesmo nos períodos de apuração em que não houverem sido realizadas quaisquer operações ou prestações\.

OS2203

RN01\.2

Cada documento DIEF deverá possuir um registro principal\.

OS2203

RN02

__Processamento dos dados:__

__Tipo de Registro:__ Grava a informação fixa = “2”, na posição 001 a 001\.

__Inscrição Estadual:__ Identifica a inscrição estadual do estabelecimento pelo campo “Inscrição Estadual” do cadastro “Inscrições Estaduais” em menu \(Básicos – Parâmetros – Preliminares – Inscrições Estaduais\), na posição 002 a 010\.

__Mês Referência__: O sistema identifica o mês de referência definido no parâmetro da tela de geração, campo “Mês/Ano Referência”, na posição 011 a 012\.

__Ano Referência:__ O sistema identifica o ano de referência definido no parâmetro da tela de geração, campo “Mês/Ano Referência”, na posição 013 a 016\.

__Tipo Documento:__ O sistema identifica o tipo de documento pelo campo “Tipo de Documento”, da tela de geração do meio magnético\. “O valor a ser gravado será um dos códigos selecionado pelo usuário, cuja opção da lista pode ser: 1\-Original no prazo, 2\-Retificadora no prazo, 3\-Original Fora do prazo, 4\-Retificadora fora do prazo”, na posição 017 a 017\.

__Débito do Período:__ O sistema transporta do Livro Registro de Apuração do ICMS, o total do ICMS debitado em decorrência das saídas tributadas realizadas no mês de referência do DIEF\-ES, na posição 018 a 028\.

__Outros Débitos:__ O sistema grava o valor de outros débitos, fazendo a somatória dos valores do código “002\-OUTROS DÉBITOS” do Livro de Apuração do ICMS, na posição 029 a 039\. Estes valores estão gravados no cadastro de Lançamentos Complementares, campo “Operação Apuração”\.

__Estorno de Créditos:__ O sistema grava o valor de Estorno de Créditos, fazendo a somatória dos valores do código “003\-ESTORNO DE CRÉDITOS” do Livro de Apuração do ICMS, na posição 040 a 050\. Estes valores estão gravados no cadastro de Lançamentos Complementares, campo “Operação Apuração”\.

__Desc Outros Débitos:__ O sistema grava Banco na posição 051 a 080\.

__Outros Débitos:__ O sistema zerado na posição 081 a 091

__*OBS:*__ O sistema não vai gravar os campos Desc Outros Débitos, na posição 051 a 080 e Outros Débitos, na posição 081 a 091, porque entendemos que estes valores devem estar escriturados no Resumo de Apuração do ICMS em “002\-OUTROS DÉBITOS” e não está de acordo com as instruções das normas de escrituração por processamento de dados regulamentado pela legislação\.

__Créditos do Período:__ O sistema transporta do Livro Registro de Apuração do ICMS, o total do ICMS creditado em decorrência das entradas tributadas realizadas no mês de referência do DIEF\-ES, na posição 092 a 102\.

__Outros Créditos:__ O sistema grava o valor de outros créditos, fazendo a somatória dos valores do código “006\-OUTROS CRÉDITOS” do Livro de Apuração do ICMS, na posição 103 a 113\. Estes valores estão gravados no cadastro de Lançamentos Complementares, campo “Operação Apuração”\.

__Estorno de Débitos:__ O sistema grava o valor de outros créditos, fazendo a somatória dos valores do código “007\-ESTORNOS DE DÉBITOS” do Livro de Apuração do ICMS, na posição 114 a 124\. Estes valores estão gravados no cadastro de Lançamentos Complementares, campo “Operação Apuração”\.

__Deduções:__ O sistema grava o valor de outros créditos, fazendo a somatória dos valores do código “012\-DEDUÇÕES” do Livro de Apuração do ICMS, na posição 125 a 135\. Estes valores estão gravados no cadastro de Lançamentos Complementares, campo “Operação Apuração”\.

__Desc Outros Créditos:__ O sistema grava Branco na posição 136 a 165\.

__Outros Créditos:__ O sistema grava zerado na posição 166 a 176\.

__*OBS:*__ O sistema não vai gravar os campos Desc Outros Créditos, na posição 136 a 165 e Outros Créditos, na posição 166 a 176, porque entendemos que estes valores devem estar escriturados no Resumo de Apuração do ICMS em “006\-OUTROS CRÉDITOS” e não está de acordo com as instruções das normas de escrituração por processamento de dados regulamentado pela legislação\.

__Sld Cred Mês Anterior:__ O sistema grava o valor do saldo credor do Livro de Apuração do ICMS, verificado no final do mês anterior ao mês de referência do DIEF\-ES, na posição 177 a 187\.

 

__ICMS a Recolher:__ o sistema grava o valor do ICMS a recolher do Livro Registro de Apuração do ICMS na posição 188 a 198\.

__Sld Credor Mês Seguinte:__ O sistema grava o valor do saldo credor do Livro de Apuração do ICMS, verificado no final do mês de referência do DIEF\-ES, na posição 199 a 209\.

__Diferencial de Alíquota:__ O sistema disponibiliza um campo para o usuário entrar com o valor do diferencial de alíquota \(em menu Estadual – DIEF\-ES – Obrigações – Informações Complementares\), denominado “19 – Diferencial de Alíquota”, no Quadro “B – ICMS a Recolher não incluído no Campo 17” e grava o conteúdo informado na posição 210 a 220\.

O estado do ES não lança o valor do diferencial em conta gráfica e sim na coluna de Observações do livro resumo de apuração \(artigo 715, parágrafo 3º, Item XII \- RICMS\)\. Sendo assim, não há possibilidade de usarmos a ferramenta por classe de lançamento\.

__Substituição Tributária:__ O sistema grava o valor do ICMS da substituição tributária do Livro de Apuração do ICMS, verificado no final do mês de referência do DIEF\-ES, na posição 221 a 231\.

FUNDAP: O sistema disponibiliza um campo para o usuário entrar com o valor do FUNDAP \(em menu Estadual – DIEF\-ES – Obrigações – Informações Complementares\), denominado “21 – FUNDAP”, no Quadro “B – ICMS a Recolher não incluído no Campo 17” e grava o conteúdo informado na posição 232 a 242\.

__\[ALTERADA – MFS\-13823\]__

__Estimativa Supermercados Dif\. de Alíquota – EC 87/15:__ O sistema grava o valor a recolher gerado na Apuração do ICMS Diferencial de Alíquota \- UF Origem/Destino \(EC 87/15\) referente a UF igual a “ES” \(em menu Estadual – ICMS – DATA MART – Apuração do ICMS – Ajuste SINIEF\. É importante que em Parâmetros p/ UF para “ES” esteja com a opção 91 selecionada, senão irá gerar zerado\) Estimativa \(em menu Estadual – DIEF\-ES – Obrigações – Informações Complementares\), denominado “22 – Estim\. Supermercados”, no Quadro “B – ICMS a Recolher não incluído no Campo 17” e grava o conteúdo informado na posição 243 a 253\.

__\[ALTERADA – MFS\-13823\]__

__Estimativa Atacadista Estabilização Fiscal 10\.630/17:__ O sistema disponibiliza um campo para o usuário entrar com o valor da Estimativa estabilização fiscal de acordo com a Lei 10\.630/17 \(em menu Estadual – DIEF\-ES – Obrigações – Informações Complementares\), denominado “23 – Estim\. Atacadista Estab\. Fiscal 10\.630/17”, no Quadro “B – ICMS a Recolher não incluído no Campo 17” e grava o conteúdo informado na posição 254 a 264\.

__Descrição Outro ICMS:__ O sistema disponibiliza um campo para o usuário entrar com a descrição de Outro ICMS \(em menu Estadual – DIEF\-ES – Obrigações – Informações Complementares\), denominado “24 – Desc\. Outro ICMS”, no Quadro “B – ICMS a Recolher não incluído no Campo 17” e grava o conteúdo informado na posição 265 a 394\.

__Valor Outro ICMS:__ O sistema disponibiliza um campo para o usuário entrar com o valor de outra operação do ICMS, no Quadro “B – ICMS a Recolher não incluído no Campo 17” e grava o conteúdo informado na posição 295 a 305\.

__\[ALTERADA – CH15409\_2016\]__

O sistema grava os campos Descrição Outro ICMS, posição 306 a 335 e 347 a 376 preenchendo com brancos\. O sistema já contempla o campo 24 nas “Informações Complementares do DIEF”\.

__Descrição Outro ICMS:__ O sistema disponibiliza um campo para o usuário entrar com a descrição de Outro ICMS \(em menu Estadual – DIEF\-ES – Obrigações – Informações Complementares\), denominado “25 – Desc\. Outro ICMS”, no Quadro “B – ICMS a Recolher não incluído no Campo 17” e grava o conteúdo informado na posição 306 a 335\.

__Valor Outro ICMS:__ O sistema disponibiliza um campo para o usuário entrar com o valor de outra operação do ICMS, no Quadro “B – ICMS a Recolher não incluído no Campo 17” e grava o conteúdo informado na posição 336 a 346\.

__\[ALTERADA – MFS\-13823\]__

__Descrição Outro ICMS:__ O sistema disponibiliza um campo para o usuário entrar com a descrição de Outro ICMS \(em menu Estadual – DIEF\-ES – Obrigações – Informações Complementares\), denominado “26 – Desc\. Outro ICMS”, no Quadro “B – ICMS a Recolher não incluído no Campo 17” e grava o conteúdo informado na posição 347 a 376\.

__Valor Outro ICMS:__ O sistema disponibiliza um campo para o usuário entrar com o valor de outra operação do ICMS, no Quadro “B – ICMS a Recolher não incluído no Campo 17” e grava o conteúdo informado na posição 377 a 387\.

O sistema grava os campos Valor Outro ICMS, posição \(336 a 346 e\) 377 a 387 preenchendo com zeros\. O sistema já contempla os campos 24 e 25 nas Informações Complementares do DIEF\.

Quando o usuário selecionar no campo “Tipo Documento”, igual a Orig\. fora do prazo ou Retif\. fora do prazo, na Figura01, o campo Descrição Outro ICMS, posição 347 a 376 e Valor Outro ICMS, posição 377 a 387, devem ser deixados em branco\.

Gravar na posição “388 a 388” a informação fixa igual a “0”, que significa estar entregando a declaração no Regime Normal\. Não vamos gerar declarações no regime de Estimativa por não possuirmos clientes nesta condição de apuração\.

Excluir da geração o campo de informação do tipo de DIA, denominado “DIATIPO”\.

__*OBS:*__ Observar que as posições do layout de 136 a 195, que foi publicada pela secretaria da fazenda, está errado, o correto é 136 a 165\.

O sistema deve gravar na apuração dos campos, no período de referência, considerando os valores dos estabelecimentos relacionados no cadastro \(Estadual – Controle de Obrigações Estaduais – Obrigações – Empresas/Estabelecimento c/Insc\. Estadual Única\), quando o campo “Geração para Empresas c/Insc\. Estadual Única” estiver selecionado “Sim”, na tela de geração do meio magnético\.

OS2203

MFS\-13823

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

MFSNNNN

