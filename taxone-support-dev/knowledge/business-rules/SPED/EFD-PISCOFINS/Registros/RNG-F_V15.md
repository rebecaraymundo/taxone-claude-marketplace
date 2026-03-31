# RNG-F_V15

- **Fonte:** RNG-F_V15.docx
- **Modificado:** 2025-11-09
- **Tamanho:** 108 KB

---

##### EFD\-Escrituração Fiscal Digital das Contribuições – Bloco F

##### DOCUMENTO DE REQUISITO

__DR__

__Nome__

__Descrição__

__Data__

MFS36163

Liiane Assaf

Considerar os Códigos Situação Tributária PIS e COFINS incluídos na SAFX147, na geração do registro F100, \(RN100\-07, RN100\-11\)

15/07/2020

MFS509499

Rogério Ohashi

O objetivo dessa demanda é incluir tratamento na geração do Campo 15 \- NAT\_BC\_CRED do Registro F100 para considerar o Campo Código de Produto na parametrização “Utilizar a parametrização da Conta Contábil/Centro de Custo X CST/Operação/Nat\. Base de Crédito”\.

14/03/2023

MFS59221

Rogério Ohashi

O objetivo dessa demanda é incluir tratamento na geração do Campo 02 \- IND\_OPER do Registro F100 para considerar a parametrização do Centralizador e das Centralizadas\.

13/02/2025

__Localização: Módulo SPED >> EFD\-Escrituração Fiscal Digital das Contribuições\. Menu:  Obrigações >> Geração dos Registros e Obrigações SCP >> Geração dos Registros__

Índice

[Regra para Geração de SCPs	1](#_Toc45807404)

[Registro F001 – Abertura do Bloco	1](#_Toc45807405)

[Registro F010 – Identificação do Estabelecimento	1](#_Toc45807406)

[Registro F100 – Demais documentos e Operações Geradoras de Contribuição e Créditos	1](#_Toc45807407)

[Registro F111 – Processo Referenciado	1](#_Toc45807408)

[Registro F120 – Bens Incorporados ao Ativo Imobilizado – Operações Geradoras de Crédito com Base nos Encargos de Depreciação e Amortização	1](#_Toc45807409)

[Registro F130 – Bens Incorporados ao Ativo Imobilizado – Operações Geradoras de Crédito com Base no Valor de Aquisição/Contribuição	1](#_Toc45807410)

[Registro F150 – Crédito Presumido sobre Estoque de Abertura	1](#_Toc45807411)

[Registro F500 – Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido – Incidência do PIS/Pasep e da Cofins pelo Regime de Caixa	1](#_Toc45807412)

[Registro F509 – Processo Referenciado	1](#_Toc45807413)

[Registro F510 – Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido – Incidência do PIS/Pasep e da Cofins pelo Regime de Caixa \(Apuração Da Contribuição por Unidade de Medida de Produto\)	1](#_Toc45807414)

[Registro F519 – Processo Referenciado	1](#_Toc45807415)

[Registro F525 – Composição da Receita Escriturada no Período – Detalhamento da Receita Recebida pelo  Regime de Caixa\.	1](#_Toc45807416)

[Registro F550 – Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido – Incidência do PIS/Pasep e da Cofins pelo Regime de Competência	1](#_Toc45807417)

[Registro F559 – Processo Referenciado	1](#_Toc45807418)

[Registro F560 – Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido – Incidência do PIS/Pasep e da Cofins pelo Regime de  Competência \(Apuração Da Contribuição por Unidade de Medida de Produto\)	1](#_Toc45807419)

[Registro F569 – Processo Referenciado	1](#_Toc45807420)

[Registro F600 – Contribuição Retida na Fonte	1](#_Toc45807421)

[Registro F700 – Deduções Diversas	1](#_Toc45807422)

[Registro F800 – Créditos Decorrentes de Eventos de Incorporação, Fusão e Cisão	1](#_Toc45807423)

__REGRAS DE NEGÓCIO__

# <a id="_Tratamento_para_Geração"></a><a id="_Toc45807404"></a>Regra para Geração de SCPs

__RNG\-001__

__\[OS4316\-A\] Tratamento para Geração de SCPs__

Quando a geração for realizada através da tela de "Geração dos Registros" do menu "Obrigações SCP", além da regra padrão de seleção, deve ser considerado:

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Centralizador, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento e os seus centralizados \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela como "Sócio Ostensivo", serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que não tenham o campo Código do SCP preenchido\.

Se for selecionado um Estabelecimento Descentralizado, que tenha identificação na tela de um código SCP, serão levados para o arquivo os registros pertencentes a este estabelecimento \(considerando a regra padrão de seleção\) e que tenham o campo Código do SCP preenchido com o código indicado na tela de geração\.

\[OS4316\-C\] Observar a parametrização de "Dados Iniciais" \(menu: Parâmetros >> Dados Iniciais\) para geração ou não do registro\. Se houver um cadastro de "Dados Iniciais" cujo campo Código da SCP esteja preenchido para a SCP que o arquivo está sendo gerado e que o registro se enquadre no critério de geração, respeitar o parametrizado para a SCP\. Se não houver, considerar o cadastro de Dados Iniciais do Sócio Ostensivo \(Código da SCP não informada\) como valido também para a SCP para o qual o arquivo está sendo gerado\.

Para a geração do arquivo do Sócio Ostensivo, permanece como válido o registro cujo campo código da SCP não está preenchido\.

Tratamento aplicados aos registros: [F100](#_Registro_F100_–) , [F120](#_Registro_F120_–) , [F130](#_Registro_F130_–) , [F500](#_Registro_F500_–) , [F510](#_Registro_F510_–) , [F525](#_Registro_F525_–), [F550](#_Registro_F550_–) , [F560](#_Registro_F560_–), [F600](#_Registro_F600_–) , [F700](#_Registro_F700_–)\.

Para maiores explicações veja o documento de regras gerais do módulo EFD\-Contribuições “RegraGeral\_v18\.doc”\.

# <a id="_Toc45807405"></a>Registro F001 – Abertura do Bloco

__RNG\-F001__

Deve ser gerado um registro por arquivo\.

__RNF001\-02__

Campo IND\_MOV:

Gravar "0" se existir movimentação a ser gerada no bloco F no período informado na tela de geração\. Senão, gravar ‘’1’’

# <a id="_Toc45807406"></a>Registro F010 – Identificação do Estabelecimento

__RNG\-F010__

CH27235/2013

Gerar um registro F010 para cada CNPJ de estabelecimento que possua movimentação nos registros do bloco F\.

As movimentações do bloco F devem ser geradas imediatamente abaixo do registro F010 do CNPJ do estabelecimento correspondente\.

\* *Foi incluída observação para gerar por CNPJ do estabelecimento por conta de situações onde a empresa tem mais de um estabelecimento com o mesmo CNPJ\. Neste caso, deve ser gerado apenas um A010 por CNPJ e as movimentações serão vinculadas abaixo do CNPJ\.*

# <a id="_Registro_F100_–"></a><a id="_Toc45807407"></a>Registro F100 – Demais documentos e Operações Geradoras de Contribuição e Créditos

__RNG\-F100__

__Regra Geral:__

A geração deste registro faz uso das seguintes informações:

- Tela de Dados Iniciais, parâmetros:

“Utilizar a parametrização do Tipo do DocumentoX CST/Operação/Nat\. Base de Crédito” ou 

“Utilizar a parametrização da Conta Contábil/Centro de Custo X CST/Operação/Nat\. Base de Crédito”\.

- Tela de Parâmetros F100 \- Tipo do DocumentoX CST/Operação/Nat\. Base de Crédito
- Tela de Parâmetros F100 \- Conta Contábil/Centro de Custo X CST/Operação/Nat\. Base de Crédito \(SAFX176\)
- Manuteção F100 – Demais Documentos e Operações Geradoras de Contribuição e Crédito \(SAFX147\)

Gerar um registro F100 para cada registro gravado na SAFX147 \(x147\_oper\_cred\)  no período:

Data da Operação: \(campo 08\)

	Entre a data inicial e final geração do arquivo

Aplicar o  [__Tratamento para Geração de SCPs__](#_Tratamento_para_Geração)

Obs\.: Os valores escriturados nos campos de bases de cálculo 08 \(VL\_BC\_PIS\) e 12 \(VL\_BC\_COFINS\), de itens com CST representativos de receitas tributadas \(CST 01, 02, 03 e 05\), são recuperados no Bloco M, para a demonstração das bases de cálculo do PIS/PASEP \(M210\) e da COFINS \(M610\), nos Campos “VL\_BC\_CONT”, respectivamente\.

Obs\.: Os valores escriturados nos campos de bases de cálculo 08 \(VL\_BC\_PIS\) e 12 \(VL\_BC\_COFINS\), de itens com CST representativos de operações com direito a crédito \(CST 50 a 56; 60 a 67\), são recuperados no Bloco M, para a demonstração das bases de cálculo dos créditos de PIS/PASEP \(M105\) e dos créditos de COFINS \(M505\) nos Campos “VL\_BC\_PIS\_TOT”, respectivamente\.

__RNF100\-02__

Campo IND\_OPER:

Para preenchimento desse campo deve seguir as seguintes regras: 

Se o parâmetro “Utilizar a parametrização do Tipo do DocumentoX CST/Operação/Nat\. Base de Crédito” estiver marcado \(nos dados iniciais\):

- Buscar o código do tipo de operação associado ao Tipo do documento \(campo da SAFX147\), através da parametrização no módulo: SPED à EFD – Escrituração Fiscal Digital – PIS/PASEP – COFINS, menu: Parâmetro à Registros F à Tipo de Documento X \(CST/Operação/ Nat\. Base de Crédito\.

Se o parâmetro ‘’Utilizar a parametrização da Conta Contábil/Centro de Custo X CST/Operação/Nat\. Base de Crédito’’ estiver marcado \(nos dados iniciais\):

- Buscar o código do tipo de operação associado à __Conta Contábil__ \(campo 17 da SAFX147\) ou ‘’__Conta Contábil e Centro de Custo’’ __\(campo 18 da SAFX147\), através da parametrização no módulo abaixo:

 SPED à EFD – Escrituração Fiscal Digital – PIS/PASEP – COFINS, menu: Parâmetro à Registros F à Conta Contábil/Centro Custo X CST/Operação/ Nat\. Base de Crédito \(SAFX176\)

Msg no LOG:

Na geração dos registros do SPED PIS/COFINS, emitir a seguinte msg no log , para os registros F100 que possuem o campo 02 \- Indicador do Tipo da Operação = 0 \( Operação Representativa de Aquisição, Custos, Despesa ou Encargos, Sujeita à Incidência de Crédito de PIS/Pasep ou Cofins \(CST 50 a 66\)\) e que não tenham a informação do campo 03 \-Código do Participante: ”Para os registros F100, quando o Indicador do Tipo da Operação = 0, o campo Código do Participante é obrigatório”\.

\[ALTERAÇÃO\-MFS59221\]

O sistema deverá recuperar o parâmetro conforme os estabelecimento Centralizador e as Centralizadas\.

__RNF100\-03__

Campo COD\_PART

\[OS4751\] Quando o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __estiver__ selecionado, este campo será gerado com o Código de identificação da pessoa fis/jur, concatenando o Indicador \(IND\_FIS\_JUR\) com o Código da PFJ \(COD\_FIS\_JUR\), considerando a formatação: Indicador \+ "\-" \+ Código\.

Se o parâmetro "Considerar o Indicador no Código do Participante" da tela de Dados Iniciais __NÃO estiver__ selecionado, este campo será gerado apenas com o Código da PFJ \(COD\_FIS\_JUR\)\.

Para o código aqui informado, será demonstrado o Cadastro no registro 0150\.

__RNF100\-07__

Campo CST\_PIS:

Se o parâmetro “Utilizar a parametrização do Tipo do Documento X CST/Operação/Nat\. Base de Crédito” estiver marcado \(nos dados iniciais\):

- Preencher com o Código Situação Tributária PIS informado no campo 26 da SAFX147\.
- Se não existir informação no campo 26 da SAFX147, buscar o Código da Situação Tributária PIS associado ao __Tipo do Documento__ \(campo 03 da SAFX147\) realizado do módulo: SPED à EFD – Escrituração Fiscal Digital – PIS/PASEP – COFINS, menu: Parâmetro à Tipo de Documento X \(CST/Operação/ Nat\. Base de Crédito\)\.

Se o parâmetro “Utilizar a parametrização da Conta Contábil/Centro de Custo X CST/Operação/Nat\. Base de Crédito” estiver marcado \(nos dados iniciais\):

- Preencher com o Código Situação Tributária PIS informado no campo 26 da SAFX147\.
- Se não existir informação no campo 26 da SAFX147, buscar o Código da Situação Tributária PIS associado à __Conta Contábil__ \(campo 17 da SAFX147\) ou ‘__’Conta Contábil e Centro de Custo’’__ \(campo 18 da SAFX147\) realizado do módulo: SPED à EFD – Escrituração Fiscal Digital – PIS/PASEP – COFINS, menu: Parâmetro à Conta Contábil/Centro Custo X CST/Operação/ Nat\. Base de Crédito\) \(SAFX176\)\.

__RNF100\-09__

Campo ALIQ\_PIS:

Se o parâmetro “Utilizar a parametrização do Tipo do Documento X CST/Operação/Nat\. Base de Crédito” estiver marcado \(nos dados iniciais\):

\- Preencher com a alíquota informada no campo 11 da SAFX147\.

Se o parâmetro “Utilizar a parametrização da Conta Contábil/Centro de Custo X CST/Operação/Nat\. Base de Crédito” estiver marcado \(nos dados iniciais\):

\-         Preencher com a alíquota PIS informada no campo 11 da SAFX147\.  

- Se não existir informação no campo 11 da SAFX147, buscar a alíquota PIS associada à __Conta Contábil__ \(campo 17 da SAFX147\) ou __Conta Contábil e Centro de Custo__ \(campo 18 da SAFX147\), realizado através do módulo: SPED à EFD – Escrituração Fiscal Digital – PIS/PASEP – COFINS, menu: Parâmetro à Conta Contábil/Centro Custo X CST/Operação/ Nat\. Base de Crédito\) \(SAFX176\)\.

__RNF100\-11__

Campo CST\_COFINS:

Para preenchimento desse campo deve seguir as seguintes regras: 

Se o parâmetro “Utilizar a parametrização do Tipo do Documento X CST/Operação/Nat\. Base de Crédito” estiver marcado \(nos dados iniciais\):

- Preencher com o Código Situação Tributária COFINS informado no campo 27 da SAFX147\.
- Se não existir informação no campo 27 da SAFX147, buscar o Código da Situação Tributária COFINS associado ao __Tipo do Documento__ \(03 campo da SAFX147\) realizado através do módulo: SPED à EFD – Escrituração Fiscal Digital – PIS/PASEP – COFINS, menu: Parâmetro à Tipo de Documento X \(Centro Custo/CST/Operação/ Nat\. Base de Crédito\)\.

Se o parâmetro “Utilizar a parametrização da Conta Contábil/Centro de Custo X CST/Operação/Nat\. Base de Crédito” estiver marcado \(nos dados iniciais\):

- Preencher com o Código Situação Tributária COFINS informado no campo 27 da SAFX147\.
- Se não existir informação no campo 27 da SAFX147, buscar o Código da Situação Tributária COFINS associado à __Conta Contábil__ \(campo 17 da SAFX147\) ou __Conta Contábil e Centro de Custo__ \(campo 18 da SAFX147\), realizado através do módulo: SPED à EFD – Escrituração Fiscal Digital – PIS/PASEP – COFINS, menu: Parâmetro à Conta Contábil/Centro Custo X CST/Operação/ Nat\. Base de Crédito\) \(SAFX176\)\.

__RNF100\-13__

Campo ALIQ\_COFINS:

Se o parâmetro “Utilizar a parametrização do Tipo do Documento X CST/Operação/Nat\. Base de Crédito” estiver marcado \(nos dados iniciais\):

\- Preencher com a alíquota COFINS informada no campo 14 da SAFX147\.

Se o parâmetro “Utilizar a parametrização da Conta Contábil/Centro de Custo X CST/Operação/Nat\. Base de Crédito” estiver marcado \(nos dados iniciais\):

\-         Preencher com a alíquota informada no campo 14 da SAFX147\.  

- Se não existir informação no campo 14 da SAFX147, buscar a alíquota COFINS associada à __Conta Contábil__ \(campo 17 da SAFX147\) ou __Conta Contábil e Centro de Custo__ \(campo 18 da SAFX147\), realizado através do módulo: SPED à EFD – Escrituração Fiscal Digital – PIS/PASEP – COFINS, menu: Parâmetro à Conta Contábil/Centro Custo X CST/Operação/ Nat\. Base de Crédito\) \(SAFX176\)\.

__RNF100\-15__

Campo NAT\_BC\_CRED:

Se o parâmetro “Utilizar a parametrização do Tipo do Documento X CST/Operação/Nat\. Base de Crédito” estiver marcado \(nos dados iniciais\):

- Buscar o código da natureza da base de crédito associado ao __Tipo do Documento__ \(03 campo da SAFX147\) realizado através do módulo: SPED à EFD – Escrituração Fiscal Digital – PIS/PASEP – COFINS, menu: Parâmetro à Tipo de Documento X \(CST/Operação/ Nat\. Base de Crédito\)\.

\[__ALTERADO\- MFS509499__\] Tratamento para incluir o campo de Código de Produto no critério de recuperação da Natureza Base de Crédito

Se o parâmetro “Utilizar a parametrização da Conta Contábil/Centro de Custo X CST/Operação/Nat\. Base de Crédito” estiver marcado \(nos dados iniciais\):

- Buscar o código da natureza da base de crédito associado à __Conta Contábil__ \(17 campo da SAFX147\) __ou__ __Conta Contábil e Centro de Custo __ \(17 campo da SAFX147\) __ou Conta Contábil e Código de Produto ou __ __Conta Contábil, Centro de Custo e Código de Produto __\(04/05 campos da SAFX147\) __ __realizado através do módulo: SPED à EFD – Escrituração Fiscal Digital – PIS/PASEP – COFINS, menu: Parâmetro à Conta Contábil/Centro Custo X CST/Operação/ Nat\. Base de Crédito\) \(SAFX176\)\.

# <a id="_Toc45807408"></a>Registro F111 – Processo Referenciado

__RNG\-F111__

Deverá ser gerado um registro F111 para cada registro informado na tela “Processo Referenciado \(F111\)” do menu Manutenção >> Registro do Bloco F >> Demais Documentos e Operações Geradoras de Contribuição e Créditos \(F100\)\. 

Poderao ser gerados N registros\.

__RNF111\-02__

Campo NUM\_PROC

Deverá ser recuperado do campo “Número Processo” da tela “Processo Referenciado \(F111\)”\.

__RNF111\-03__

Campo IND\_PROC

Deverá ser recuperado do campo “Indicador da Origem do Processo” da tela “Processo Referenciado \(F111\)”\.

- Gravar “1”, caso a opção selecionada seja “1 – Justiça Federal”
- Gravar “2”, caso a opção selecionada seja “2 – Secretaria da Receita Federal do Brasil”
- Gravar “9”, caso a opção selecionada seja “9 – Outros”

# <a id="_Registro_F120_–"></a><a id="_Toc45807409"></a>Registro F120 – Bens Incorporados ao Ativo Imobilizado – Operações Geradoras de Crédito com Base nos Encargos de Depreciação e Amortização

__RNG\-F120__

Gerar um registro F120 para cada bem ou grupo__\*__ de registros na SAFX148 no período que atendam ao critério abaixo:

Indicador de Operações Geradoras de Créditos: \(campo 03 da SAFX148\)

	Igual a “1 \- Crédito com Base nos Encargos de Depreciação” ou “2 \- Crédito com Base nos Encargos de Amortização”

Data de Lançamento do PIS/COFINS: \(campo 05 da SAFX148\):

	Entre a data inicial e final de geração do arquivo

      

Parâmetro “Indicador da geração dos bens incorporados ao Ativo Imobilizado” informado na tela de Dados Iniciais:

Se indicador = ‘’Geração de bens forma individualizada’’, gravar os registros informados da tabela SAFX148\.

     

Se indicador = “Geração por grupos de bens da mesma natureza ou destinação’’, deve\-se gerar o registro F120, agrupando, conforme os critérios abaixo\.  

__\*__O agrupamento dos registros da SAFX148 deve ser feito de acordo com a seguinte chave:

\- Código do Grupo \(campo 04\)

\- Origem do Crédito \(campo 07\)

\- Utilização do Bem \(campo 08\)

\- Código da Base de Cálculo do Crédito \(NAT\_BC\_CRED\)

\- CST PIS \(campo 17\)

\- Alíquota PIS \(campo 19\)

\- CST COFINS \(campo 21\)

\- Alíquota COFINS \(campo 23\)

\- Conta Contábil \(campo 25\)

\- Centro de Custo \(campo 26\)

Aplicar o  [__Tratamento para Geração de SCPs__](#_Tratamento_para_Geração)

__RNF120\-02__

Campo NAT\_BC\_CRED:

A partir do conteúdo do Indicador de Operações Geradoras de Créditos \(campo 03 da SAFX148\), verificar:

Se Indicador de Operações Geradoras de Créditos igual a “1” à gravar “__09__“\.

Se Indicador de Operações Geradoras de Créditos igual a “2” à gravar “__11__”\.

# <a id="_Registro_F130_–"></a><a id="_Toc45807410"></a>X’Registro F130 – Bens Incorporados ao Ativo Imobilizado – Operações Geradoras de Crédito com Base no Valor de Aquisição/Contribuição

__RNG\-F130__

Gerar um registro F130 para cada grupo__\*__ de registros na SAFX148 no período que atendam ao critério abaixo:

Indicador de Operações Geradoras de Créditos: \(campo 03 da SAFX148\)

	Igual a “3 \- Crédito com Base no Valor de Aquisição/Contribuição”

Data de Lançamento do PIS/COFINS: \(campo 05\):

	Entre a data inicial e final de geração do arquivo

Parâmetro “Indicador da geração dos bens incorporados ao Ativo Imobilizado” informado na tela de Dados Iniciais:

Se indicador = ‘’Geração de bens forma individualizada’’, gravar os registros informados da tabela SAFX148\.

     

Se indicador = “Geração por grupos de bens da mesma natureza ou destinação’’, deve\-se gerar o registro F130, agrupando, conforme os critérios abaixo\.  

__\*__O agrupamento dos registros da SAFX148 deve ser feito de acordo com a seguinte chave:

\- Código do Grupo \(campo 04\)

\- Origem do Crédito \(campo 07\)

\- Utilização do Bem \(campo 08\)

\- Mês/Ano de Aquisição \(campo 11\)

\- Nº de Parcelas \(campo 15\)

\- CST PIS \(campo 17\)

\- Alíquota PIS \(campo 19\)

\- CST COFINS \(campo 21\)

\- Alíquota COFINS \(campo 23\)

\- Conta Contábil \(campo 25\)

\- Centro de Custo \(campo 26\)

Aplicar o  [__Tratamento para Geração de SCPs__](#_Tratamento_para_Geração)

# <a id="_Toc45807411"></a>Registro F150 – Crédito Presumido sobre Estoque de Abertura

__RNG\-F150__

Gerar um registro F150 para cada registro informado através do módulo: EFD\-PIS/COFINS, menu: Manutenção → Crédito Presumido sobre Estoque de Abertura, que atenda ao critério abaixo:

Incidência Tributária no período: \(parâmetro nos dados iniciais da obrigação\)

Diferente ‘‘2 \- Escrituração de operações com incidência exclusivamente no regime cumulativo”\.

Período Inicial de utilização do crédito:

Igual ou até 11 meses anteriores ao período de geração do arquivo\.

__Regime Caixa __

# <a id="_Registro_F500_–"></a><a id="_Toc45807412"></a>Registro F500 – Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido – Incidência do PIS/Pasep e da Cofins pelo Regime de Caixa

__RNGF500__

Neste registro deverão ser gravadas as informações Consolidadas das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido – Incidência do PIS/Pasep e da Cofins pelo Regime de Caixa

\[MFS10591\]

__Se o parâmetro: “Geração com base nas informações da SAFX183 e SAFX187” estiver marcado__ \(em dados iniciais\):

Este registro será gerado somente com base nas informações registradas na tela ‘Demais Receitas – Lucro Presumido \(F500/F510/F550/F560\)’, localizada no Módulo: SPED / EFD – Escrituração Fiscal Digital \-  PIS/PASEP – COFINS, Menu: Manutenção / Registro do Bloco F \(SAFX183/SAFX187\)

__Se o parâmetro: “Geração com base nas informações da SAFX183 e SAFX187” estiver desmarcado__ \(em dados iniciais\):

Este registro deverá ser gerado para as empresas do Lucro Presumido e com Regime de Caixa\. A recuperação dos dados utilizará os mesmos critérios que os utilizados na geração dos registros A100/A110/A111/A170, C100/C111/C170/C175/C180/C181/C185/C188/C380/C381/C385/C400/C405/C481/C485/C489/C490/C491/C495/C499/C600/C601/C605/C609/ D200/D201/ D205/D209/D300/D309/D350/D359/D600/D601/D605/D609, porem deverão ser filtrados apenas os documentos de Saída\.

Além de considerarmos as informações registradas na tela ‘Demais Receitas – Lucro Presumido \(F500/F510/F550/F560\)’, localizada no Módulo: SPED / EFD – Escrituração Fiscal Digital \-  PIS/PASEP – COFINS, Menu: Manutenção / Registro do Bloco F \(SAFX183\) e da SAFX 501\.

O agrupamento do registro será por CST, Alíquota, Código do modelo, CFOP, código da conta e Informações complementares\.

Obs\. Este registro será gerado com base no recebimento, ou seja, se o valor do documento for recebido em 3 prestações, será exibido o valor da parcela recebida no período\. 

Exemplo: documento do mês de julho \(R$1\.500,00\) recebido em 3 parcelas \(julho, agosto, setembro\), será gerado um F500 para os meses de  julho, agosto, setembro no valor de R$500,00 cada\.

IMPORTANTE: Se a Origem for SAFX07 e com o tipo de Faturamento __diferente de__ “1 – A Vista”

\[CH2935/2017 – MFS\-10098\]

1\. Devem ser recuperados os registros da SAFX501 das parcelas com vencimento Data do Pagamento \(campo 18 da SAFX501\) no período da geração do arquivo;

2\. A partir destas parcelas devemos recuperar aos dados da nota fiscal lendo a SAFX05 ou a SAFX500 associada a estas parcelas;

3\. A partir do item 2, \(após termos as informações da nota recuperada\) buscamos os dados na SAFX07\.

Caso o tipo de Faturamento __for igual__ a “1 – A Vista”, o registro será gerado com base nas informações do documento fiscal \(SAFX07\)\.

__ATENÇÃO: Os documentos cancelados NÃO devem ser considerados na geração deste Registro\.__

Aplicar o  [__Tratamento para Geração de SCPs__](#_Tratamento_para_Geração)

__RNF500 \- 01__

__Campo: REG__

Gravar o Texto Fixo ”F500”

__RNF500 – 02__

__Campo: VL\_REC\_CAIXA	__

__Origem SAFX07,08 e 09__

Se o tipo de faturamento \(campo 99 da safx07\) for igual a  01 – A vista e 

 

__Notas Fiscais de Mercadoria,  Mista e Serviço:__

Somatório do campo “23\-Valor Total da Nota” da SAFX07\.

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor da parcela  \(14 \- VLR\_PARCELA\) informado na SAFX501\.

Origem SAFX994

Somatório do campo “19\-Valor do Item ” da SAFX994\.

Origem SAFX42

Somatório do campo “17 \- VLR\_TOT\_NOTA da SAFX42\.

Origem SAFX161

Somatório do campo “12\- VLR\_DOC da SAFX161\.

Origem SAFX183/187:

Considerar o valor do campo 28 \- Valor da Receita Recebida da SAFX187\.

Origem SAFX 190 

Valor do campo 12 \- VLR\_TOTAL

__RNF500 \- 03__

__Campo: CST\_PIS	__

__Origem SAFX07,08 e 09__

Se o tipo de faturamento \(campo 99 da safx07\) for igual a  01 – A vista e 

Para as notas sem Itens: Preencher com a informação do campo 249 \- COD\_SIT\_PIS da SAFX07

Notas Fiscais de Serviço 

Para as notas com Itens:__ __Preencher com a informação do campo 68 – COD\_SITUACAO\_PIS da SAFX09 

Notas Fiscais de Mercadoria

Para as notas com Itens:__ __Preencher com a informação do campo 175 – COD\_SITUACAO\_PIS da SAFX08

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor do campo 22  \- Código Situação Tributária PIS da SAFX 501\.

Origem SAFX994

Preencher com a informação do campo 32 \- COD\_SIT\_TRIB\_PIS da SAFX994\.

Origem SAFX43

Valor do campo 93 \- COD\_SIT\_PIS da SAFX43\.

Origem SAFX162

Valor do campo “13\- COD\_SIT\_PIS da SAFX162\.

Origem SAFX183/187:

Considerar as informações do campo 21\- Código Situação Tributária do PIS da SAFX187\.

Origem SAFX 191

Informação do campo 11\- COD\_SIT\_PIS

__RNF500 \- 04__

__Campo: VL\_DESC\_PIS__

__Origem SAFX07,08 e 09__

Se o tipo de faturamento \(campo 99 da safx07\) for igual a  01 – A vista e 

Para as notas *sem* itens à o campo deve ser preenchido com o valor desconto da SAFX07 \(campo 28\-Valor Descontos\);

Notas Fiscais de Serviço 

Para as notas *com *itens à deve\-se totalizar o valor do desconto de todos os itens da nota, considerando o campo “21\-Valor do Desconto” da SAFX09\.

Notas Fiscais de Mercadoria e Mista

Para as notas *com *itens à neste caso deve\-se totalizar o valor do desconto de todos os itens de mercadoria e serviço da nota, considerando o campo “29\-Valor do Desconto” da SAFX08, e “21\-Valor do Desconto” da SAFX09\.

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor do campo 23 \- Valor do Desconto PIS da SAFX 501\.

Origem SAFX43

\[Alteração OS\-3812\-A\]

Este campo deve ser preenchido com o “Valor acumulado dos descontos/exclusões PIS”

Origem SAFX994

Preencher com o somatório do campo 20 \- VLR\_DESC  da SAFX994\.

Origem SAFX162

Somatório do campo “12 \- VLR\_DESC da SAFX162\.

Origem SAFX183/187:

Considerar as informações do campo 31 \-  Valor do Desconto PIS do Valor Recebido da SAFX187\.

Origem SAFX 190

Somatório do campo 13 \- VLR\_DESCONTO

__RNF500 \- 05__

__Campo: VL\_BC\_PIS	__

__Origem SAFX07,08 e 09__

Se o tipo de faturamento \(campo 99 da safx07\) for igual a  01 – A vista e 

Para as notas *sem* itens à o campo deve ser preenchido com o valor da base de cálculo PIS da SAFX07 \(campo 102\-Base PIS\);

Notas Fiscais de Serviço 

Para as notas *com *itens à deve\-se totalizar o valor da base de cálculo PIS de todos os itens da nota, considerando o campo “46\-Base PIS” da SAFX09\.

Notas Fiscais de Mercadoria e Mista

Para as notas *com *itens à deve\-se totalizar o valor da base de cálculo COFINS de todos os itens da nota, considerando o campo “86\- VLR\_BASE\_PIS” da SAFX08 e campo “46\-Base PIS” da SAFX09\.

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor do campo 24 \- Valor Base PIS da SAFX 501\.

Origem SAFX43

Somatório do campo 78\- VLR\_BASE\_PIS da SAFX43

Origem SAFX994

Preencher com o somatório do campo 33\- VLR\_BASE\_PIS da SAFX994\.

Origem SAFX162

Somatório do campo “14 \- VLR\_BASE\_PIS da SAFX162\.

Origem SAFX183/187

Considerar as informações do campo 29 \- Valor da Base de cálculo do PIS do Valor Recebido da SAFX187\.

Origem SAFX 191

Somatório do campo 12\- VLR\_BASE\_PIS

__RNF500 \- 06__

__Campo: ALIQ\_PIS__

__Origem SAFX07,08 e 09__

Se o tipo de faturamento \(campo 99 da safx07\) for igual a  01 – A vista e 

Notas Fiscais Sem Itens 

Preencher com o valor do campo 164\-VLR\_ALIQ\_PIS da SAFX07

Notas Fiscais de Serviço 

Preencher com o valor do campo 47\-VLR\_ALIQ\_PIS da SAFX09

Notas Fiscais de Mercadoria 

Preencher com o valor do campo 129 \- VLR\_ALIQ\_PIS da SAFX08

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor do campo 26\- Valor Alíquota PIS da SAFX 501\.

Origem SAFX43

Valor do campo 79\- VLR\_ALIQ\_PIS da SAFX43

Origem SAFX994

Preencher com o valor do campo 34 \- VLR\_ALIQ\_PIS da SAFX994\.

Origem SAFX162

Preencher com o valor  do campo “15\- VLR\_ALIQ\_PIS da SAFX162\.

Origem SAFX183/187

Considerar as informações do campo 22\-  Alíquota do PIS do Valor Recebido  da SAFX187\.

Origem SAFX 191

Valor do campo 13 \- VLR\_ALIQ\_PIS

__RNF500 \- 07__

__Campo: VL\_PIS	__

__Origem SAFX07,08 e 09__

Se o tipo de faturamento \(campo 99 da safx07\) for igual a 01 – A vista e 

Para as notas *sem* itens 

O campo deve ser preenchido com o valor do PIS da SAFX07 \(campo 103\-Valor PIS\);

Notas Fiscais de Serviço 

Para as notas *com *itens à deve\-se totalizar o valor do PIS de todos os itens da nota, considerando o campo “48\-Valor PIS” da SAFX09\.

Notas Fiscais de Mercadoria e Mista 

Para as notas *com *itens à deve\-se totalizar o valor do PIS de todos os itens da nota, considerando o campo “87\-VLR\_PIS” da SAFX08 e campo “48\-Valor PIS” da SAFX09\.

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor do campo 28\- Valor PIS da SAFX 501\.

Origem SAFX43

Somatório do Valor do campo 77\- VLR\_PIS da SAFX43

Origem SAFX994

Somatório do valor do campo 26 \- VLR\_PIS da SAFX994\.

Origem SAFX162

Somatório do valor do campo “16 – VLR\_PIS da SAFX162\.

Origem SAFX183/187

Considerar as informações do campo 32 \-  Valor do PIS do Valor Recebido da SAFX187\.

Origem SAFX 191

Somatório do campo 14 \- VLR\_PIS

__RNF500 \- 08__

__Campo: CST\_COFINS__

__Origem SAFX07,08 e 09__

Se o tipo de faturamento \(campo 99 da safx07\) for igual a 01 – A vista e 

Para as notas sem Itens: Preencher com a informação do campo 250 \- COD\_SIT\_COFINS da SAFX07

Notas Fiscais de Serviço 

Para as notas com Itens: Preencher com a informação do campo 69 – COD\_SITUACAO\_COFINS da SAFX09 

Notas Fiscais de Mercadoria

Para as notas com Itens:__ __Preencher com a informação do campo 178 – COD\_SITUACAO\_COFINS da SAFX08

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor do campo 29 \- Código Situação Tributária COFINS da SAFX 501\.

Origem SAFX43

Preencher com a informação do campo 94 \- COD\_SIT\_COFINS da SAFX43

Origem SAFX994

Preencher com a informação do campo 35 \- COD\_SIT\_TRIB\_COFINS da SAFX994\.	

Origem SAFX162

Preencher com a informação do campo “17 – COD\_SIT\_COFINS da SAFX162\.

Origem SAFX183/187

Considerar as informações do campo 24 \-  Código Situação Tributária da COFINS do Valor Recebido da SAFX187\.

Origem SAFX 191

Valor do campo 15 \-COD\_SIT\_COFINS

__RNF500 \- 09__

__Campo: VL\_DESC\_COFINS	__

__Origem SAFX07,08 e 09__

Se o tipo de faturamento \(campo 99 da safx07\) for igual a 01 – A vista e 

Para as notas *sem* itens à o campo deve ser preenchido com o valor desconto da SAFX07 \(campo 28\-Valor Descontos\);

Notas Fiscais de Serviço 

Para as notas *com *itens à deve\-se totalizar o valor do desconto de todos os itens da nota, considerando o campo “21\-Valor do Desconto” da SAFX09\.

Notas Fiscais de Mercadoria e Mista

Para as notas *com *itens à neste caso deve\-se totalizar o valor do desconto de todos os itens de mercadoria e serviço da nota, considerando o campo “29\-Valor do Desconto” da SAFX08, e “21\-Valor do Desconto” da SAFX09\.

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor do campo 30 \- Valor de Desconto do COFINS da SAFX 501\.

Origem SAFX43

\[Alteração OS\-3812\-A\]

Este campo deve ser preenchido com o “Valor acumulado dos descontos/exclusões COFINS”

Origem SAFX994

Somatório do campo 20 – VLR\_DESC da SAFX994\.

Origem SAFX162

Somatório do campo “12 \- VLR\_DESC da SAFX162\.

Origem SAFX183/187:

Considerar as informações do campo 35 \-  Valor do Desconto COFINS do Valor Recebido da SAFX187\.

Origem SAFX 190

Somatório do campo 13 \- VLR\_DESCONTO 

__RNF500 \- 10__

__Campo: VL\_BC\_COFINS__

__Origem SAFX07,08 e 09__

Se o tipo de faturamento \(campo 99 da safx07\) for igual a 01 – A vista e 

Para as notas *sem* itens à o campo deve ser preenchido com o valor da base de cálculo COFINS da SAFX07 \(campo 104\-Base COFINS\);

Notas Fiscais de Serviço 

Para as notas *com *itens à deve\-se totalizar o valor da base de cálculo COFINS de todos os itens da nota, considerando o campo “49\-Base COFINS” da SAFX09\.

Notas Fiscais de Mercadoria e Mista

Para as notas *com *itens à deve\-se totalizar o valor da base de cálculo COFINS de todos os itens da nota, considerando o campo “88\- VLR\_BASE\_COFINS” da SAFX08 e o campo “49\-Base COFINS” da SAFX09\.

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor do campo 31 \- Base COFINS da SAFX 501\.

Origem SAFX43

Somatório do campo 81\- VLR\_BASE\_COFINS da SAFX43\.

Origem SAFX994

Preencher com a informação do campo 36 \-  VLR\_BASE\_COFINS da SAFX994\.

Origem SAFX162

Somatório do campo “18 \- VLR\_BASE\_COFINS da SAFX162\.

Origem SAFX183/187:

Considerar as informações do campo 33 \-  Valor da Base de Cálculo da COFINS do Valor Recebido  da SAFX187\.

Origem SAFX 191

Somatório do campo 16\- VLR\_BASE\_COFINS

__RNF500 \- 11__

__Campo: ALIQ\_COFINS__

__Origem SAFX07,08 e 09__

Se o tipo de faturamento \(campo 99 da safx07\) for igual a 01 – A vista e 

Notas Fiscais Sem Itens 

Preencher com o valor do campo 165\-VLR\_ALIQ\_COFINS da SAFX07

Notas Fiscais de Serviço 

Preencher com o valor do campo 50\-VLR\_ALIQ\_COFINS da SAFX09

Notas Fiscais de Mercadoria 

Preencher com o valor do campo 130 \- VLR\_ALIQ\_COFINS da SAFX08 

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor do campo 33 \- Valor Alíquota COFINS da SAFX 501\.

Origem SAFX43

Preencher com a informação do campo 82\- VLR\_ALIQ\_COFINS da SAFX43\.

Origem SAFX994

Preencher com a informação do campo 37 \- VLR\_ALIQ\_COFINS  da SAFX994\.

Origem SAFX162

Preencher com a informação do campo “19 \- VLR\_ALIQ\_COFINS da SAFX162\.

Origem SAFX183/187

Considerar as informações do campo 25\- Alíquota da COFINS do Valor Recebido da SAFX187\.

Origem SAFX 191

Valor do campo 17 \- VLR\_ALIQ\_COFINS

__RNF500 \- 12__

__Campo: VL\_COFINS__

__Origem SAFX07,08 e 09__

Se o tipo de faturamento \(campo 99 da safx07\) for igual a 01 – A vista e 

Para as notas *sem* itens à o campo deve ser preenchido com o valor da COFINS da SAFX07 \(campo 105\-Valor COFINS\);

Notas Fiscais de Serviço 

Para as notas *com *itens à deve\-se totalizar o valor da COFINS de todos os itens da nota, considerando o campo “51\-Valor COFINS” da SAFX09\.

Notas Fiscais de Mercadoria e Mista 

Para as notas *com *itens à deve\-se totalizar o valor do PIS de todos os itens da nota, considerando o campo “89\-VLR\_COFINS” da SAFX08 e campo “51\-Valor COFINS” da SAFX09\.

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor do campo 35 \- Valor COFINS da SAFX 501\.

Origem SAFX43

Preencher com o somatório do campo 80\- VLR\_COFINS da SAFX43\.

Origem SAFX994

Preencher com  o somatório do campo 27 \- VLR\_COFINS da SAFX994\.

Origem SAFX162

Somatório do campo “20 \- VLR\_COFINS da SAFX162\.

Origem SAFX183/187

Considerar as informações do campo 36 \- Valor da COFINS do Valor Recebido da SAFX187\.

Origem SAFX 191

Valor do campo 18 \- VLR\_COFINS

__RNF500 \- 13 __

__Campo: COD\_MOD__

__\[ALTERADA – CH32179\_2012\]__

__Origem SAFX07__

Preencher com a informação do campo 229 \- COD\_MODELO\_COTEPE, SAFX07	

Origem SAFX42

Preencher com a informação do campo 13 \- COD\_MODELO  da SAFX42\.

Origem SAFX994

Preencher com a informação do campo 03 \- COD\_MODELO  da SAFX994\.	

Origem SAFX162

Preencher com a informação do campo 03 \- COD\_MODELO  da SAFX162\.

Origem SAFX183/187

Considerar as informações do campo 11 \- Código do Modelo  da SAFX187\.

Origem SAFX191

Preencher com a informação do campo 03 \- COD\_MODELO  da SAFX191

__RNF500 \- 14__

__Campo: CFOP	__

__Origem SAFX07/08/09:__

Para as notas sem itens ou notas com o tipo de faturamento \(campo 99 da safx07\) for diferente de ‘ 01 – A vista’

Preencher com a informação do campo 14\-COD\_CFO da SAFX07 

Notas Fiscais de Serviço e com o tipo de faturamento \(campo 99 da safx07\) igual a  ‘ 01 – A vista’

Preencher com a informação do campo 17\-COD\_CFO da SAFX09

Notas Fiscais de Mercadoria  e com o tipo de faturamento \(campo 99 da safx07\) igual a  ‘ 01 – A vista’

Preencher com a informação do campo 22\-COD\_CFO da SAFX08

Origem SAFX43

Preencher com a informação do campo 13 \- COD\_CFO da SAFX43\.

Origem SAFX994

Preencher com a informação do campo 14 \- COD\_CFO da SAFX994\.

Origem SAFX162

Não preencher este campo\.

Origem SAFX183/187

Considerar as informações do campo 12 –Código Fiscal da SAFX187\.

Origem SAFX191

Não preencher este campo\.

__RNF500 \- 15__

__Campo: COD\_CTA__

__Origem SAFX07/08/09__

__\[ALTERADA – CH24956\_2015\]__

Para as notas sem itens ou notas com o tipo de faturamento \(campo 99 da safx07\) for diferente de ‘ 01 – A vista’

Preencher com a informação do campo 33\-COD\_CONTA da SAFX07

Notas Fiscais de Serviço e com o tipo de faturamento \(campo 99 da safx07\) igual a ‘ 01 – A vista’

Preencher com a informação do campo 52\-COD\_CONTA da SAFX09

Notas Fiscais de Serviço e com o tipo de faturamento \(campo 99 da safx07\) diferente de ‘ 01 – A vista’

Preencher com a informação do campo 33\-COD\_CONTA da SAFX07, se não estiver informado, preencher com a informação do campo 52\-COD\_CONTA da SAFX09

Notas Fiscais de Mercadoria e com o tipo de faturamento \(campo 99 da safx07\) igual a ‘ 01 – A vista’

Preencher com a informação do campo 105\-COD\_CONTA da SAFX08

Notas Fiscais de Mercadoria e com o tipo de faturamento \(campo 99 da safx07\) diferente de ‘ 01 – A vista’

Preencher com a informação do campo 33\-COD\_CONTA da SAFX07, se não estiver informado, preencher com a informação do campo 105\-COD\_CONTA da SAFX08

Origem SAFX43

Preencher com a informação do campo 53 \- COD\_CONTA da SAFX43\.

Origem SAFX994

Preencher com a informação do campo 40\- COD\_CONTA da SAFX994\.

Origem SAFX162

Preencher com a informação do campo 21\- COD\_CONTA da SAFX162\.

Origem SAFX183/187

__RNF500 \- 16__

__Campo: INFO\_COMPL__

__Não preencher este campo, quando a origem dos dados for documento fiscal, SAFX43,994,162,191\.__

__Origem SAFX183/187:__

Considerar as informações do campo 19 – Descrição complementar do Documento/Operação

da SAFX187\.

# <a id="_Toc45807413"></a>Registro F509 – Processo Referenciado

__RNGF509__

__Origem  \(Demais Receitas – Lucro Presumido \(F500/F510/F550/F560\)\)__

Deverá ser gerado um registro F509  para cada registro informado na tela “Processo Referenciado \(F509/519/559/569\)” do menu Manutenção >> Registro do Bloco F >> ‘Demais Receitas – Lucro Presumido \(F500/F510/F550/F560\)

__Origem Documentos Fiscais de Serviço e Mercadoria – Saída__

Nesse registro devem ser gravados os registros da SAFX114 relacionados aos documentos gerado no registro F500 que atendam ao critério abaixo:

Vinculação: \(campo ‘’15 – Vinculação da SAFX112\)

             Igual a ‘’2 – EFD PIS/COFINS

Origem do Processo: \(campo “14 – Origem do Processo” da SAFX114\)

	Igual a “1 – Justiça Federal”, “3 – Secex/RFB” ou “9 – Outros”

__Origem Documentos Utilities – SAFX42/43__

Deve ser gerado um registro F509 para cada registro existente na tela Registro C609 \-Processo Referenciado  que foi considerado no registro F500\. \(Módulo: MastersafDW / Básicos /  Manutenção / Documento Fiscal / Novo Documento Fiscal / Documento Fiscal Utilities / Registro C609 \-Processo Referenciado \)

__Origem Documentos Utilities – SAFX190/191__

Deverá ser gerado um registro F509  para cada registro informado na tela “Registro 609 \-Processo Referenciado ” do menu Manutenção >> Notas de Fornecimento de Energia Elétrica Água Canalizada e Gás \(C600\)’, localizada no Módulo: SPED / EFD – Escrituração Fiscal Digital \-  PIS/PASEP – COFINS\. 

Poderão ser gerados N registros\.

__RNF509\-01__

__Campo: REG__

Gravar o texto fixo “F509”	

__RNF509\-02__

__Campo: NUM\_PROC__ 

__Origem F500/F510/F550/F560__

Deverá ser recuperado do campo “Número Processo” da tela “Processo Referenciado \(F1509/519/559/569\)”\.

__Origem SAFX114__

Deverá ser recuperado do campo “Número Processo”

__SAFX42/43__

Deverá ser recuperado do campo “Número Processo”

__SAFX190/191__

Deverá ser recuperado do campo “Número Processo”

__RNF509\-03__

__Campo: IND\_PROC__

__Origem F500/F510/F550/F560__

Deverá ser recuperado do campo “Indicador da Origem do Processo” da tela “Processo Referenciado \(F509/519/559/569\)”\.

- Gravar “1”, caso a opção selecionada seja “1 – Justiça Federal”
- Gravar “2”, caso a opção selecionada seja “2 – Secretaria da Receita Federal do Brasil”

Gravar “9”, caso a opção selecionada seja “9 – Outros”

__Origem SAFX114__

 Campo “Indicador da Origem do Processo”

- Gravar “1”, caso a opção selecionada seja “1 – Justiça Federal”
- Gravar “2”, caso a opção selecionada seja “2 – Secretaria da Receita Federal do Brasil”

Gravar “9”, caso a opção selecionada seja “9 – Outros”

__SAFX42/43__

Campo “Indicador da Origem do Processo”

- Gravar “1”, caso a opção selecionada seja “1 – Justiça Federal”
- Gravar “2”, caso a opção selecionada seja “2 – Secretaria da Receita Federal do Brasil”

Gravar “9”, caso a opção selecionada seja “9 – Outros”

__SAFX190/191__

Campo “Indicador da Origem do Processo”

- Gravar “1”, caso a opção selecionada seja “1 – Justiça Federal”
- Gravar “2”, caso a opção selecionada seja “2 – Secretaria da Receita Federal do Brasil”

Gravar “9”, caso a opção selecionada seja “9 – Outros”

# <a id="_Registro_F510_–"></a><a id="_Toc45807414"></a>Registro F510 – Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido – Incidência do PIS/Pasep e da Cofins pelo Regime de Caixa \(Apuração Da Contribuição por Unidade de Medida de Produto\)

__RNGF510__

Neste registro deverão ser gravadas as informações Consolidadas das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido – Incidência do PIS/Pasep e da Cofins pelo Regime de Caixa \(Apuração por Unidade de Medida de Produto\)\.

\[MFS10591\]

__Se o parâmetro: “Geração com base nas informações da SAFX183 e SAFX187” estiver marcado__ \(em dados iniciais\):

Este registro será gerado somente com base nas informações registradas na tela ‘Demais Receitas – Lucro Presumido \(F500/F510/F550/F560\)’, localizada no Módulo: SPED / EFD – Escrituração Fiscal Digital \-  PIS/PASEP – COFINS, Menu: Manutenção / Registro do Bloco F \(SAFX183/SAFX187\)

__Se o parâmetro: “Geração com base nas informações da SAFX183 e SAFX187” estiver desmarcado__ \(em dados iniciais\):

Este registro deverá ser gerado para as empresas do Lucro Presumido e com Regime de Caixa \. A recuperação dos dados utilizará os mesmos critérios que os utilizados na geração dos registros C100/C111/C170/C180/C181/C185/C188/C380/C381/C385/C400/C405/C481/C485/C489/C490/C491/C495/C499/D200/D201/ D205/D209/D300/D309/D350/D359 ,porem deverão ser filtrados apenas os documentos de Saída\.

Além de considerarmos as informações registradas na tela ‘Demais Receitas – Lucro Presumido \(F500/F510/F550/F560\)’, localizada no Módulo: SPED / EFD – Escrituração Fiscal Digital \-  PIS/PASEP – COFINS, Menu: Manutenção / Registro do Bloco F \(SAFX183\) e da SAFX05,500 e 501\.

O agrupamento do registro será por CST, Alíquota, Código do modelo, CFOP, código da conta e Informações complementares\.

Obs\. Este registro será gerado com base no recebimento, ou seja, se o valor do documento for recebido em 3 prestações, será exibido o valor da parcela recebida no período\. 

Exemplo: documento do mês de julho \(R$1\.500,00\) recebido em 3 parcelas \(julho, agosto, setembro\), será gerado um F500 para os meses de  julho, agosto, setembro no valor de R$500,00 cada\.

IMPORTANTE: Se a Origem for SAFX07 e com o tipo de Faturamento  diferente de “1 – A Vista”

1\. Devem ser recuperados os registros da SAFX501 das parcelas com vencimento no período da geração do arquivo

2\. A partir destas parcelas devemos recuperar aos dados da nota fiscal lendo a SAFX05 ou a SAFX500 associada a estas parcelas;

3\. A partir do item 2,  \(após termos as informações da nota recuperada\) buscamos os dados na SAFX07\.

Caso o tipo de Faturamento for igual a  “1 – A Vista”, o registro será gerado com base nas informações do documento fiscal \(SAFX07\)\.

__ATENÇÃO: Os documentos cancelados NÃO devem ser considerados na geração deste Registro\.__

Aplicar o  [__Tratamento para Geração de SCPs__](#_Tratamento_para_Geração)

__RNF510 \- 01__

__Campo: REG__

Gravar o Texto Fixo ”F510”

__RNF510 – 02__

__Campo: VL\_REC\_CAIXA	__

__Origem SAFX07,08__

Se o tipo de faturamento \(campo 99 da safx07\) for igual a  01 – A vista e 

 

__Notas Fiscais de Mercadoria__

Somatório do campo “23\-Valor Total da Nota” da SAFX07\.

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor da parcela  \(14 \- VLR\_PARCELA\) informado na SAFX501\.

Origem SAFX994

Somatório do campo “19\-Valor do Item ” da SAFX994\.

__Origem SAFX183/187:__

Considerar o valor do campo 28 \- Valor da Receita Recebida da SAFX187\.

__RNF510 \- 03__

__Campo: CST\_PIS	__

__Origem SAFX07,08__

Se o tipo de faturamento \(campo 99 da safx07\) for igual a  01 – A vista e 

Para as notas sem Itens: Preencher com a informação do campo 249 \- COD\_SIT\_PIS da SAFX07

Notas Fiscais de Mercadoria

Para as notas com Itens:__ __Preencher com a informação do campo 175 – COD\_SITUACAO\_PIS da SAFX08

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor do campo 22  \- Código Situação Tributária PIS da SAFX 501\.

Origem SAFX994

Preencher com a informação do campo 32 \- COD\_SIT\_TRIB\_PIS da SAFX994\.

__Origem SAFX183/187:__

Considerar as informações do campo 21\- Código Situação Tributária do PIS da SAFX187\.

__RNF510 \- 04__

__Campo: VL\_DESC\_PIS__

__Origem SAFX07,08 __

Se o tipo de faturamento \(campo 99 da safx07\) for igual a 01 – A vista e 

Para as notas *sem* itens à o campo deve ser preenchido com o valor desconto da SAFX07 \(campo 28\-Valor Descontos\);

Notas Fiscais de Mercadoria

Para as notas *com *itens à neste caso deve\-se totalizar o valor do desconto de todos os itens de mercadoria da nota, considerando o campo “29\-Valor do Desconto” da SAFX08\.

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor do campo 23 \- Valor do Desconto PIS da SAFX 501\.

Origem SAFX994

Preencher com o somatório do campo 20 \- VLR\_DESC  da SAFX994\.

__Origem SAFX183/187:__

Considerar as informações do campo 31 \-  Valor do Desconto PIS do Valor Recebido da SAFX187\.

__RNF510 \- 05__

Campo: QUANT\_BC\_PIS

Se o tipo de faturamento \(campo 99 da safx07\) for igual a 01 – A vista e 

Notas Fiscais de Mercadoria

Para as notas com itens à neste caso deve\-se totalizar o valor do desconto de todos os itens de mercadoria da nota, considerando o campo “176\-QTD\_BASE\_PIS”  da SAFX08\.

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor do campo 25\- Quantidade \- Base de Cálculo PIS da SAFX 501\.

Origem SAFX994

Preencher com o somatório do campo 38\- QTD\_BASE\_PIS  da SAFX994\.

__Origem SAFX183/187:__

Considerar as informações do campo 30 \- Quantidade Base PIS do Valor Recebido da SAFX187\.

__RNF510 \- 06__

__Campo: ALIQ\_PIS\_QUANT__

Se o tipo de faturamento \(campo 99 da safx07\) for igual a 01 – A vista e 

Notas Fiscais de Mercadoria

Para as notas *com *itens à neste caso deve\-se totalizar o valor do desconto de todos os itens de mercadoria da nota, considerando o campo “177\-VLR\_ALIQ\_PIS\_R”  da SAFX08\.

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor do campo 27\- Alíquota do PIS \- em reais da SAFX 501\.

Origem SAFX994

Preencher com o somatório do campo 39 \-VLR\_ALIQ\_ESPEC\_PIS  da SAFX994\.

__Origem SAFX183/187:__

Considerar as informações do campo 23 \- Alíquota do PIS em Reais da SAFX187\.

__RNF510 \- 07__

__Campo: VL\_PIS	__

__Origem SAFX07,08__

Se o tipo de faturamento \(campo 99 da safx07\) for igual a 01 – A vista e 

Para as notas *sem* itens 

O campo deve ser preenchido com o valor do PIS da SAFX07 \(campo 103\-Valor PIS\);

Notas Fiscais de Mercadoria 

Para as notas *com *itens à deve\-se totalizar o valor do PIS de todos os itens da nota, considerando o campo “87\-VLR\_PIS” da SAFX08 

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor do campo 28\- Valor PIS \- em reais da SAFX 501\.

Origem SAFX994

Preencher com o valor do campo 26 \- VLR\_PIS da SAFX994\.

__Origem SAFX183/187:__

Considerar as informações do campo 32 \-  Valor do PIS do Valor Recebido da SAFX187\.

__RNF510 \- 08__

__Campo: CST\_COFINS__

__Origem SAFX07,08__

Se o tipo de faturamento \(campo 99 da safx07\) for igual a 01 – A vista e 

Para as notas sem Itens: Preencher com a informação do campo 250 \- COD\_SIT\_COFINS da SAFX07

Notas Fiscais de Mercadoria

Para as notas com Itens:__ __Preencher com a informação do campo 178 – COD\_SITUACAO\_COFINS da SAFX08

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor do campo 29 \- Código Situação Tributária COFINS da SAFX 501\.

Origem SAFX994

Preencher com a informação do campo 35 \- COD\_SIT\_TRIB\_COFINS da SAFX994\.

__Origem SAFX183/187:__

Considerar as informações do campo 24 \-  Código Situação Tributária da COFINS do Valor Recebido da SAFX187\.

__RNF510 \- 09__

__Campo: VL\_DESC\_COFINS	__

__Origem SAFX07,08 __

Se o tipo de faturamento \(campo 99 da safx07\) for igual a 01 – A vista e 

Para as notas *sem* itens à o campo deve ser preenchido com o valor desconto da SAFX07 \(campo 28\-Valor Descontos\);

Notas Fiscais de Mercadoria 

Para as notas *com *itens à neste caso deve\-se totalizar o valor do desconto de todos os itens de mercadoria da nota, considerando o campo “29\-Valor do Desconto” da SAFX08

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor do campo 30 \- Valor de Desconto do COFINS da SAFX 501\.

Origem SAFX994

Preencher com a informação do campo 20 – VLR\_DESC da SAFX994\.

__Origem SAFX183/187:__

Considerar as informações do campo 35 \-  Valor do Desconto COFINS do Valor Recebido da SAFX187\.

__RNF510 \- 10__

__Campo: QUANT\_BC\_COFINS__

Se o tipo de faturamento \(campo 99 da safx07\) for igual a 01 – A vista e 

Notas Fiscais de Mercadoria

Para as notas *com *itens à neste caso deve\-se totalizar o valor do desconto de todos os itens de mercadoria da nota, considerando o campo “179\-QTD\_BASE\_COFINS”  da SAFX08\.

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor do campo 32 \- Quantidade \- Base de Cálculo COFINS da SAFX 501\.

Origem SAFX994

Preencher com a informação do campo 41 \- QTD\_BASE\_COFINS da SAFX994\.

__Origem SAFX183/187:__

Considerar as informações do campo 34 \- Quantidade Base COFINS do Valor Recebido da SAFX187\.

__RNF510 \- 11__

__Campo: ALIQ\_COFINS\_QUANT__

Se o tipo de faturamento \(campo 99 da safx07\) for igual a 01 – A vista e 

Notas Fiscais de Mercadoria

Para as notas *com *itens à neste caso deve\-se totalizar o valor do desconto de todos os itens de mercadoria da nota, considerando o campo “180\-VLR\_ALIQ\_COFINS\_R”  da SAFX08\.

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor do campo 34 \- Alíquota do COFINS \- em reais da SAFX 501\.

Origem SAFX994

Preencher com a informação do campo 42 \- VLR\_ALIQ\_ESPEC\_COFINSda SAFX994\.

__Origem SAFX183/187:__

Considerar as informações do campo 26 \- Alíquota do COFINS em Reais da SAFX187\.

__RNF510 \- 12__

__Campo: VL\_COFINS__

__Origem SAFX07,08__

Se o tipo de faturamento \(campo 99 da safx07\) for igual a 01 – A vista e 

Para as notas *sem* itens à o campo deve ser preenchido com o valor da COFINS da SAFX07 \(campo 105\-Valor COFINS\);

Notas Fiscais de Mercadoria 

Para as notas *com *itens à deve\-se totalizar o valor do PIS de todos os itens da nota, considerando o campo “89\-VLR\_COFINS” da SAFX08 

Senão \(quando o tipo de Faturamento for diferente de “1 – A Vista”\):

Considerar o valor do campo 35 \- Valor COFINS da SAFX 501\.

Origem SAFX994

Preencher com a informação do campo 27 \- VLR\_COFINS da SAFX994\.

__Origem SAFX183/187:__

Considerar as informações do campo 36 \- Valor da COFINS do Valor Recebido da SAFX187\.

__RNF510 \- 13 __

__Campo: COD\_MOD__

__\[ALTERADA – CH32179\_2012\]__

__Origem SAFX07__

Preencher com a informação do campo 229 \- COD\_MODELO\_COTEPE, SAFX07	

Origem SAFX994

Preencher com a informação do campo 03 \- COD\_MODELO  da SAFX994\.

__Origem SAFX183/187:__

Considerar as informações do campo 11 \- Código do Modelo  da SAFX187\.

__RNF510 \- 14__

__Campo: CFOP	__

__Origem SAFX07/08__

Para as notas sem itens ou notas com o tipo de faturamento \(campo 99 da safx07\) for diferente de ‘ 01 – A vista’

Preencher com a informação do campo 14\-COD\_CFO da SAFX07

Notas Fiscais de Mercadoria e notas com o tipo de faturamento \(campo 99 da safx07\) igual a  ‘ 01 – A vista’

Preencher com a informação do campo 22\-COD\_CFO da SAFX08

Origem SAFX994

Preencher com a informação do campo 14 \- COD\_CFO da SAFX994\.

__Origem SAFX183/187:__

Considerar as informações do campo 12 –Código Fiscal da SAFX187\.

__RNF510 \- 15__

__Campo: COD\_CTA__

__Origem SAFX07/08__

Para as notas sem itens ou notas com o tipo de faturamento \(campo 99 da safx07\) for diferente de ‘ 01 – A vista’

Preencher com a informação do campo 33\-COD\_CONTA da SAFX07

Notas Fiscais de Mercadoria e notas com o tipo de faturamento \(campo 99 da safx07\) igual a  ‘ 01 – A vista’

Preencher com a informação do campo 105\-COD\_CONTA da SAFX08

Origem SAFX994

Preencher com a informação do campo 40\- COD\_CONTA da SAFX994\.

__Origem SAFX183/187:__

Considerar as informações do campo 17 – Código da conta analítica debitada/creditada da SAFX187\.

__RNF510 \- 16__

__Campo: INFO\_COMPL__

__Não preencher este campo, quando a origem dos dados for documento fiscal, SAFX994 \.__

__Origem SAFX183/187:__

Considerar as informações do campo 19 – Descrição complementar do Documento/Operação

da SAFX187\.

# <a id="_Toc45807415"></a>Registro F519 – Processo Referenciado

__RNGF519__

__Origem  \(Demais Receitas – Lucro Presumido \(F500/F510/F550/F560\)\)__

Deverá ser gerado um registro F519  para cada registro informado na tela “Processo Referenciado \(F509/519/559/569\)” do menu Manutenção >> Registro do Bloco F >> ‘Demais Receitas – Lucro Presumido \(F500/F510/F550/F560\)

__Origem Documentos Fiscais de Serviço e Mercadoria – Saída__

Nesse registro devem ser gravados os registros da SAFX114 relacionados aos documentos gerado no registro F510 que atendam ao critério abaixo:

Vinculação: \(campo ‘’15 – Vinculação da SAFX112\)

             Igual a ‘’2 – EFD PIS/COFINS

Origem do Processo: \(campo “14 – Origem do Processo” da SAFX114\)

	Igual a “1 – Justiça Federal”, “3 – Secex/RFB” ou “9 – Outros”

Poderão ser gerados N registros\.

__RNF519\-01__

__Campo: REG__

Gravar o texto fixo “F519”

__RNF519\-02__

__Campo: NUM\_PROC__ 

__Origem F500/F510/F550/F560__

Deverá ser recuperado do campo “Número Processo” da tela “Processo Referenciado \(F1509/519/559/569\)”\.

__Origem SAFX114__

Deverá ser recuperado do campo “Número Processo”

__RNF519\-03__

__Campo: IND\_PROC__

__Origem F500/F510/F550/F560__

Deverá ser recuperado do campo “Indicador da Origem do Processo” da tela “Processo Referenciado \(F509/519/559/569\)”\.

- Gravar “1”, caso a opção selecionada seja “1 – Justiça Federal”
- Gravar “2”, caso a opção selecionada seja “2 – Secretaria da Receita Federal do Brasil”

Gravar “9”, caso a opção selecionada seja “9 – Outros”

__Origem SAFX114__

 Campo “Indicador da Origem do Processo”

- Gravar “1”, caso a opção selecionada seja “1 – Justiça Federal”
- Gravar “2”, caso a opção selecionada seja “2 – Secretaria da Receita Federal do Brasil”

Gravar “9”, caso a opção selecionada seja “9 – Outros”

# <a id="_Registro_F525_–"></a><a id="_Toc45807416"></a>Registro F525 – Composição da Receita Escriturada no Período – Detalhamento da Receita Recebida pelo  Regime de Caixa\.

__RNGF525__

Registro Obrigatório para a Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido – optante pela apuração das contribuições sociais pelo Regime de Caixa\. Tem por objetivo relacionar a composição de todas as receitas recebidas pela pJ no período da escrituração, sujeitas ou não ao pagamento da contribuição social\.

Consolidar os registros pela composição das receitas\.

\[MFS10591\]

__Se o parâmetro: “Geração com base nas informações da SAFX183 e SAFX187” estiver marcado__ \(em dados iniciais\):

Este registro será gerado somente com base nas informações registradas na tela ‘Demais Receitas – Lucro Presumido \(F500/F510/F550/F560\)’, localizada no Módulo: SPED / EFD – Escrituração Fiscal Digital \-  PIS/PASEP – COFINS, Menu: Manutenção / Registro do Bloco F \(SAFX183/SAFX187\)

__Se o parâmetro: “Geração com base nas informações da SAFX183 e SAFX187” estiver desmarcado__ \(em dados iniciais\):

Este registro deverá ser gerado para as empresas do Lucro Presumido e com Regime de Caixa\. A recuperação dos dados utilizará os mesmos critérios que os utilizados na geração dos registros:

 A100/A110/A111/A170, C100/C111/C170/C180/C181/C185/C188/C380/C381/C385/C400/C405/C481/C485/C489/C490/C491/C495/C499/C600/C601/C605/C609/ D200/D201/ D205/D209/D300/D309/D350/D359/D600/D601/D605/D609,porem deverão ser filtrados apenas os documentos de Saída\.

Além de considerarmos as informações registradas na tela ‘Demais Receitas – Lucro Presumido \(F500/F510/F550/F560\)’, localizada no Módulo: SPED / EFD – Escrituração Fiscal Digital \-  PIS/PASEP – COFINS, Menu: Manutenção / Registro do Bloco F \(SAFX183\) e da SAFX 501\.

Aplicar o  [__Tratamento para Geração de SCPs__](#_Tratamento_para_Geração)

__RNF525 \- 01__

Campo: REG

Gravar o Texto Fixo ”F525”

__RNF525 – 02__

__Campo: VL\_REC__

Considerar o valor do campo 02 do registro F500

__Veja a situação abaixo:__

Documento

Cliente \- CNPJ

Item

Valor

01

Cliente01 \- 00000000000001

Merc01

1000,00

02

Cliente02 \- 00000000000002

Merc01

2000,00

03

Cliente01 \- 00000000000001

Merc02

3000,00

04

Cliente03 \- 00000000000003

Merc01

5000,00

1\-

|F500|11000,00|01||11000,00|1,65|181,50|1,65|181,50|||||

|F525|11000,00|01|00000000000001|||4000,00|01|01|||

|F525|11000,00|01|00000000000002|||2000,00|01|01|||

|F525|11000,00|01|00000000000003|||5000,00|01|01|||

2\-

|F500|6000,00|01||6000,00|1|60|1|60|||||

|F500|5000,00|01||5000,00|2|50|2|50|||||

|F525|11000,00|04||01||1000,00|01|01|||

|F525|11000,00|04||02||2000,00|01|01|||

|F525|11000,00|04||03||3000,00|01|01|||

|F525|11000,00|04||04||5000,00|01|01|||

3\-

|F500|10000,00|01||10000,00|1|100|1|100|||||

|F500|1000,00|01||1000,00|2|10|2|10|||||

|F525|11000,00|05|||Merc01|8000,00|01|01|||

|F525|11000,00|05|||Merc02|3000,00|01|01|||

__RNF525 \- 03__

__Campo: IND\_REC__

__Origem SAFX183/187:__

Considerar a informação do campo 04\- Indicador da Composição da Receita da SAFX183\.

Valores Válidos:

01\- Clientes

02\- Administradora de cartão de débito/crédito

03\- Título de crédito \- Duplicata, nota promissória, cheque, etc\.

04\- Documento fiscal

05\- Item vendido \(produtos e serviços\)

99\- Outros \(Detalhar no campo 10 – Informação Complementar\)

__As demais Origens \(SAFX07,08,09,42,43,161,162,191,192,992,993 e 994\)__

Considerar a informação do parâmetro ‘Critério do Detalhamento do Registro F525’ na tela de Dados Iniciais\.

Valores válidos:

01 – Clientes

04 \- Documento Fiscal

05 \- Item Vendido

Mensagem no Log:

Se o parâmetro ‘Critério do Detalhamento do Registro F525’ na tela de Dados Iniciais, for Clientes e existir na base cupom fiscal \(origem safx994\), exibir a seguinte msg:

'Consolidacao de cupons fiscais para empresas submetidas ao Regime de Caixa \(Lucro Precumido\)',

 'O indicador da composicao da receita para consolidacao dos documentos fiscais nos registros F525 foi definido atraves dos parametros de dados iniciais com a opcao de "Clientes"\. Para a consolidacao de cupons fiscais esta opcao nao sera valida devido a ausencia do CNPJ/CPF do cliente, o validador ira criticar esta informacao\.'

__RNF525 \- 04__

__Campo: CNPJ\_CPF__

Se o campo 03 do registro F525 for ‘01’ ou ‘02’, deve ser informado o CNPJ ou CPF do cliente informado no registro F500, caso contrário gerar ‘||”

Origem SAFX07: Considerar o CNPJ da Pessoa Física/Jurídica que consta no documento fiscal 

Origem SAFX42:  Considerar o CNPJ da Pessoa Física/Jurídica que consta no documento de utilities

Origem SAFX161: Gerar ‘||’

Origem SAFX191: Gerar ‘||’

Origem SAFX993: Considerar o CNPJ do cliente envolvido\.

Origem SAFX183: Considerar o CNPJ da Pessoa Física/Jurídica

__RNF525 \- 05__

__Campo: NUM\_DOC__

Se o campo 03 do registro F525 for ‘03’ ou ‘04’, deve ser informado o número do título de crédito ou do documento fiscal que foram considerados na geração do registro F500\. Caso contrário, deve ser gerado ‘||’\.

Origem SAFX07: Considerar o numero do documento \(campo 08\) que consta no documento fiscal 

Origem SAFX42:  Considerar o número do documento \(campo 06\) que consta no documento de utilities

Origem SAFX161: Gerar ‘||’

Origem SAFX191: Gerar ‘||’

Origem SAFX994: Considerar o  número do documento \(campo 05\) que consta no detalhe do cupom fiscal

Origem SAFX183: Considerar o  número do documento \(campo 06\) que consta na receita

__RNF525 \- 06__

__Campo: COD\_ITEM__

Se o campo 03 do registro F525 for ‘05’, deve ser informado o código do produto/serviço informado no documento que foi considerado no registro F500\. 

Se não existir nenhuma informação de produto, nos documentos que foram recuperados, não informar nada, ou seja ‘||’\.

__RNF525 \- 07__

__Campo: VL\_REC\_DET__

Informar o valor da receita detalhada, correspondente ao conteúdo informado no campo 04,05 ou 06 do registro F525\.

Neste campo será exibido o valor recebido com base no detalhamento feito pelo indicador da Receita \(campo 3 do F525\)\.

Exemplo: Uma empresa teve uma receita de R$100\.000,00 que irá detalhar por documento fiscal \(ind\_rec=04\)

No campo 02 temos a informação da receita total de 100\.000,00  e no campo 07 , deve indicar o valor da receita de cada documento\. 

Receita recebida                        indicador                   numero                                 receita detalhada

100\.000,00		                04		           1		                       30\.000,00

100\.000,00	                              04		          6		                      50\.000,00

100\.000,00		               04		          55		        20\.000,00

__RNF525 \- 08__

__Campo: CST\_PIS__

Informar o valor do campo CST PIS de cada documento recuperado para a geração do registro F500, considerando o indicador da composição da receita\.

__RNF525 \- 09__

__Campo: CST\_COFINS__

Informar o valor do campo CST PIS de cada documento recuperado para a geração do registro F500, , considerando o indicador da composição da receita\.	

__RNF525 \- 10__

__Campo: INFO\_COMPL__

__Origem SAFX07:__

Não preencher este campo\.

__Origem SAFX183:__

Preencher com a informação do Campo 05 – Informação Complementar da Composição da Receita da SAFX183

__RNF525 \- 11__

__Campo: COD\_CTA__

Informar a conta de cada documento recuperado para a geração do registro F500\.	

__	__

# <a id="_Registro_F550_–"></a><a id="_Toc45807417"></a>Registro F550 – Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido – Incidência do PIS/Pasep e da Cofins pelo Regime de Competência

__RNGF550__

Neste registro deverão ser gravadas as informações Consolidadas das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido – Incidência do PIS/Pasep e da Cofins pelo Regime de Competência\.

\[MFS10591\]

Se o parâmetro: “Geração com base nas informações da SAFX183 e SAFX187” estiver marcado \(em dados iniciais\):

Este registro será gerado somente com base nas informações registradas na tela ‘Demais Receitas – Lucro Presumido \(F500/F510/F550/F560\)’, localizada no Módulo: SPED / EFD – Escrituração Fiscal Digital \-  PIS/PASEP – COFINS, Menu: Manutenção / Registro do Bloco F \(SAFX183/SAFX187\)

Se o parâmetro: “Geração com base nas informações da SAFX183 e SAFX187” estiver desmarcado \(em dados iniciais\):

Este registro deverá ser gerado para as empresas do Lucro Presumido e com Regime de Competência Consolidada\. A recuperação dos dados utilizará os mesmos critérios que os utilizados na geração dos blocos A100/A110/A111/A170, C100/C111/C170/C180/C181/C185/C188/C380/C381/C385/C400/C405/C481/C485/C489/C490/C491/C495/C499/C600/C601/C605/C609/ D200/D201/ D205/D209/D300/D309/D350/D359/D600/D601/D605/D609, porém deverão ser filtrados apenas os documentos de Saída\.

Além de considerarmos as informações registradas na tela ‘Demais Receitas – Lucro Presumido \(F500/F510/F550/F560\)’, localizada no Módulo: SPED / EFD – Escrituração Fiscal Digital \-  PIS/PASEP – COFINS, Menu: Manutenção / Registro do Bloco F \(SAFX183\)

OBS\. Caso os registros tenham fontes de dados tabelas distintas, exemplo C600/C601/C605 e D600/D601/D605, a recuperação das informações deve considerar esta origem \(conforme informado na tela de Dados Iniciais\)\.

A data dos documentos que serão recuperados, devem considerar a opção informada no parâmetro: “Registro A100, C100,C180 e C190 – Seleção das Operações Geradoras de Receita”  disponível na tela de Dados Iniciais,  para definir se as notas devem ser recuperadas pela Data Fiscal ou pela Data Lancamento PIS/COFINS

O agrupamento do registro será por CST\_PIS,  CST\_COFINS, Alíquota PIS, Alíquota COFINS, Código do modelo, CFOP, código da conta e Informações complementares\.

Verifique RNG3 – EFD e RNG4 – EFD\.

ATENÇÃO: Os documentos cancelados NÃO devem ser considerados na geração deste Registro\.

Aplicar o  [Tratamento para Geração de SCPs](#_Tratamento_para_Geração)

__RNF550 \- 01__

__Campo: REG__

Gravar o Texto Fixo ”F550”

RNF550 – 02

Campo: VL\_REC\_COMP	

Notas Fiscais de Mercadoria, Mista e Serviço

Somatório do campo “23\-Valor Total da Nota” da SAFX07\.

Origem SAFX994

Somatório do campo “19\-Valor do Item ” da SAFX994\.

Origem SAFX42

Somatório do campo “17 \- VLR\_TOT\_NOTA da SAFX42\.

Origem SAFX161

Somatório do campo “12\- VLR\_DOC da SAFX161\.

Origem SAFX 183

Somatório do campo 20 – da SAFX183	

Origem SAFX 190 

Valor do campo 12 \- VLR\_TOTAL

__RNF550 \- 03__

__Campo: CST\_PIS__

Para as notas sem Itens: Preencher com a informação do campo 249 \- COD\_SIT\_PIS da SAFX07

Notas Fiscais de Serviço 

Para as notas com Itens:__ __Preencher com a informação do campo 68 – COD\_SITUACAO\_PIS da SAFX09 

Notas Fiscais de Mercadoria

Para as notas com Itens:__ __Preencher com a informação do campo 175 – COD\_SITUACAO\_PIS da SAFX08

Origem SAFX994

Preencher com a informação do campo 32 \- COD\_SIT\_TRIB\_PIS da SAFX994\.

Origem SAFX43

Valor do campo 93 \- COD\_SIT\_PIS da SAFX43\.

Origem SAFX162

Valor do campo “13\- COD\_SIT\_PIS da SAFX162\.

Origem SAFX 183

Preencher com a informação do campo 21 da SAFX183

Origem SAFX 191

Informação do campo 11\- COD\_SIT\_PIS

__RNF550 \- 04__

__Campo: VL\_DESC\_PIS__

Para as notas *sem* itens à o campo deve ser preenchido com o valor desconto da SAFX07 \(campo 28\-Valor Descontos\);

Notas Fiscais de Serviço 

Para as notas *com *itens à deve\-se totalizar o valor do desconto de todos os itens da nota, considerando o campo “21\-Valor do Desconto” da SAFX09\.

Notas Fiscais de Mercadoria e Mista

Para as notas *com *itens à neste caso deve\-se totalizar o valor do desconto de todos os itens de mercadoria e serviço da nota, considerando o campo “29\-Valor do Desconto” da SAFX08, e “21\-Valor do Desconto” da SAFX09\.

Origem SAFX43

\[Alteração OS\-3812\-A\]

Este campo deve ser preenchido com o “Valor acumulado dos descontos/exclusões PIS”

Origem SAFX994

Preencher com o somatório do campo 20 \- VLR\_DESC  da SAFX994\.

Origem SAFX162

Somatório do campo “12 \- VLR\_DESC da SAFX162\.

Origem SAFX 183

Preencher com o somatório do campo 26 da SAFX183

Origem SAFX 190

Somatório do campo 13 \- VLR\_DESCONTO

__RNF550 \- 05__

__Campo: VL\_BC\_PIS__

Para as notas *sem* itens à o campo deve ser preenchido com o valor da base de cálculo PIS da SAFX07 \(campo 102\-Base PIS\);

Notas Fiscais de Serviço 

Para as notas *com *itens à deve\-se totalizar o valor da base de cálculo PIS de todos os itens da nota, considerando o campo “46\-Base PIS” da SAFX09\.

Notas Fiscais de Mercadoria e Mista

Para as notas *com *itens à deve\-se totalizar o valor da base de cálculo COFINS de todos os itens da nota, considerando o campo “86\- VLR\_BASE\_PIS” da SAFX08 e campo “46\-Base PIS” da SAFX09\.

Origem SAFX994

Preencher com o somatório do campo 33\- VLR\_BASE\_PIS da SAFX994\.	

Origem SAFX43

Valor do campo 78\-VLR\_BASE\_PIS da SAFX43\.

Origem SAFX162

Somatório do campo “14 \- VLR\_BASE\_PIS da SAFX162\.

Origem SAFX 183

Preencher com o somatório do campo 23 da SAFX183

Origem SAFX 191

Somatório do campo 12\- VLR\_BASE\_PIS

__RNF550 \- 06__

__Campo: ALIQ\_PIS__

Notas Fiscais Sem Itens 

Preencher com o valor do campo 164\-VLR\_ALIQ\_PIS da SAFX07

Notas Fiscais de Serviço 

Preencher com o valor do campo 47\-VLR\_ALIQ\_PIS da SAFX09

Notas Fiscais de Mercadoria 

Preencher com o valor do campo 129 \- VLR\_ALIQ\_PIS da SAFX08

Origem SAFX43

Valor do campo 79\- VLR\_ALIQ\_PIS da SAFX43

Origem SAFX994

Preencher com o valor do campo 34 \- VLR\_ALIQ\_PIS da SAFX994\.

Origem SAFX162

Preencher com o valor  do campo “15\- VLR\_ALIQ\_PIS da SAFX162\.

Origem SAFX 183

Preencher com a informação do campo 22 da SAFX183

Origem SAFX 191

Valor do campo 13 \- VLR\_ALIQ\_PIS

__RNF550 \- 07__

__Campo: VL\_PIS	__

Para as notas *sem* itens 

O campo deve ser preenchido com o valor do PIS da SAFX07 \(campo 103\-Valor PIS\);

Notas Fiscais de Serviço 

Para as notas *com *itens à deve\-se totalizar o valor do PIS de todos os itens da nota, considerando o campo “48\-Valor PIS” da SAFX09\.

Notas Fiscais de Mercadoria e Mista 

Para as notas *com *itens à deve\-se totalizar o valor do PIS de todos os itens da nota, considerando o campo “87\-VLR\_PIS” da SAFX08 e campo “48\-Valor PIS” da SAFX09\.

Origem SAFX43

Somatório do Valor do campo 77\- VLR\_PIS da SAFX43

Origem SAFX994

Somatório do valor do campo 26 \- VLR\_PIS da SAFX994\.

Origem SAFX162

Somatório do valor do campo “16 – VLR\_PIS da SAFX162\.

Origem SAFX 183

Preencher com o somatório do campo 27 da SAFX183

Origem SAFX 191

Somatório do campo 14 \- VLR\_PIS

__RNF550 \- 08__

__Campo: CST\_COFINS__

Para as notas sem Itens: Preencher com a informação do campo 250 \- COD\_SIT\_COFINS da SAFX07

Notas Fiscais de Serviço 

Para as notas com Itens: Preencher com a informação do campo 69 – COD\_SITUACAO\_COFINS da SAFX09 

Notas Fiscais de Mercadoria

Para as notas com Itens:__ __Preencher com a informação do campo 178 – COD\_SITUACAO\_COFINS da SAFX08

Origem SAFX43

Preencher com a informação do campo 94 \- COD\_SIT\_COFINS da SAFX43

Origem SAFX994

Preencher com a informação do campo 35 \- COD\_SIT\_TRIB\_COFINS da SAFX994\.	

Origem SAFX162

Preencher com a informação do campo “17 – COD\_SIT\_COFINS da SAFX162\.

Origem SAFX 183

Preencher com a informação do campo 28 da SAFX183

Origem SAFX 191

Valor do campo 15 \-COD\_SIT\_COFINS

__RNF550 \- 09__

__Campo: VL\_DESC\_COFINS__

Para as notas *sem* itens à o campo deve ser preenchido com o valor desconto da SAFX07 \(campo 28\-Valor Descontos\);

Notas Fiscais de Serviço 

Para as notas *com *itens à deve\-se totalizar o valor do desconto de todos os itens da nota, considerando o campo “21\-Valor do Desconto” da SAFX09\.

Notas Fiscais de Mercadoria e Mista

Para as notas *com *itens à neste caso deve\-se totalizar o valor do desconto de todos os itens de mercadoria e serviço da nota, considerando o campo “29\-Valor do Desconto” da SAFX08, e “21\-Valor do Desconto” da SAFX09\.

Origem SAFX43

\[Alteração OS\-3812\-A\]

Este campo deve ser preenchido com o “Valor acumulado dos descontos/exclusões COFINS”

Origem SAFX994

Somatório do campo 20 – VLR\_DESC da SAFX994\.

Origem SAFX162

Somatório do campo “12 \- VLR\_DESC da SAFX162\.

Origem SAFX 183

Preencher com o somatório do campo 33 da SAFX183

Origem SAFX 190

Somatório do campo 13 \- VLR\_DESCONTO

__RNF550 \- 10__

__Campo: VL\_BC\_COFINS__

Para as notas *sem* itens à o campo deve ser preenchido com o valor da base de cálculo COFINS da SAFX07 \(campo 104\-Base COFINS\);

Notas Fiscais de Serviço 

Para as notas *com *itens à deve\-se totalizar o valor da base de cálculo COFINS de todos os itens da nota, considerando o campo “49\-Base COFINS” da SAFX09\.

Notas Fiscais de Mercadoria e Mista

Para as notas *com *itens à deve\-se totalizar o valor da base de cálculo COFINS de todos os itens da nota, considerando o campo “88\- VLR\_BASE\_COFINS” da SAFX08 e o campo “49\-Base COFINS” da SAFX09\.

Origem SAFX43

Somatório do campo 81\- VLR\_BASE\_COFINS da SAFX43\.

Origem SAFX994

Preencher com a informação do campo 36 \-  VLR\_BASE\_COFINS da SAFX994\.

Origem SAFX162

Somatório do campo “18 \- VLR\_BASE\_COFINS da SAFX162\.

Origem SAFX 183

Preencher com o somatório do campo 30 da SAFX183

Origem SAFX 191

Somatório do campo 16\- VLR\_BASE\_COFINS

__RNF550 \- 11__

__Campo: ALIQ\_COFINS__

Notas Fiscais Sem Itens 

Preencher com o valor do campo 165\-VLR\_ALIQ\_COFINS da SAFX07

Notas Fiscais de Serviço 

Preencher com o valor do campo 50\-VLR\_ALIQ\_COFINS da SAFX09

Notas Fiscais de Mercadoria 

Preencher com o valor do campo 130 \- VLR\_ALIQ\_COFINS da SAFX08

Origem SAFX43

Preencher com a informação do campo 82\- VLR\_ALIQ\_COFINS da SAFX43\.

Origem SAFX994

Preencher com a informação do campo 37 \- VLR\_ALIQ\_COFINS  da SAFX994\.

Origem SAFX162

Preencher com a informação do campo “19 \- VLR\_ALIQ\_COFINS da SAFX162\.

Origem SAFX 183

Preencher com a informação do campo 29 da SAFX183

Origem SAFX 191

Valor do campo 17 \- VLR\_ALIQ\_COFINS

__RNF550 \- 12__

__Campo: VL\_COFINS__

Para as notas *sem* itens à o campo deve ser preenchido com o valor da COFINS da SAFX07 \(campo 105\-Valor COFINS\);

Notas Fiscais de Serviço 

Para as notas *com *itens à deve\-se totalizar o valor da COFINS de todos os itens da nota, considerando o campo “51\-Valor COFINS” da SAFX09\.

Notas Fiscais de Mercadoria e Mista 

Para as notas *com *itens à deve\-se totalizar o valor do PIS de todos os itens da nota, considerando o campo “89\-VLR\_COFINS” da SAFX08 e campo “51\-Valor COFINS” da SAFX09\.

Origem SAFX43

Preencher com o somatório do campo 80\- VLR\_COFINS da SAFX43\.

Origem SAFX994

Preencher com  o somatório do campo 27 \- VLR\_COFINS da SAFX994\.

Origem SAFX162

Somatório do campo “20 \- VLR\_COFINS da SAFX162\.

Origem SAFX 183

Preencher com o somatório do campo 34 da SAFX183

Origem SAFX 191

Valor do campo 18 \- VLR\_COFINS

__RNF550 \- 13 __

__Campo: COD\_MOD__

__\[ALTERADA – CH32179\_2012\]__

Preencher com a informação do campo 229 \- COD\_MODELO\_COTEPE, SAFX07	

Origem SAFX42

Preencher com a informação do campo 13 \- COD\_MODELO  da SAFX42\.

Origem SAFX994

Preencher com a informação do campo 03 \- COD\_MODELO  da SAFX994\.	

Origem SAFX162

Preencher com a informação do campo 03 \- COD\_MODELO  da SAFX162\.

Origem SAFX 183

Preencher com a informação do campo 11 da SAFX183

Origem SAFX191

Preencher com a informação do campo 03 \- COD\_MODELO  da SAFX191

__RNF550 \- 14__

__Campo: CFOP	__

Para as notas sem itens

Preencher com a informação do campo 14\-COD\_CFO da SAFX07

Notas Fiscais de Serviço 

Preencher com a informação do campo 17\-COD\_CFO da SAFX09

Notas Fiscais de Mercadoria

Preencher com a informação do campo 22\-COD\_CFO da SAFX08

Origem SAFX43

Preencher com a informação do campo 13 \- COD\_CFO da SAFX43\.

Origem SAFX994

Preencher com a informação do campo 14 \- COD\_CFO da SAFX994\.

Origem SAFX162

Não preencher este campo\.

Origem SAFX 183

Preencher com a informação do campo 12 da SAFX183

Origem SAFX191

Não preencher este campo\.

__RNF550 \- 15__

__Campo: COD\_CTA__

Para as notas sem itens

Preencher com a informação do campo 33\-COD\_CONTA da SAFX07

Notas Fiscais de Serviço 

Preencher com a informação do campo 52\-COD\_CONTA da SAFX09

Notas Fiscais de Mercadoria 

Preencher com a informação do campo 105\-COD\_CONTA da SAFX08

Origem SAFX43

Preencher com a informação do campo 53 \- COD\_CONTA da SAFX43\.

Origem SAFX994

Preencher com a informação do campo 40\- COD\_CONTA da SAFX994\.

Origem SAFX162

Preencher com a informação do campo 21\- COD\_CONTA da SAFX162\.

Origem SAFX 183

Preencher com a informação do campo 17 da SAFX183

Origem SAFX 191

Preencher com a informação do campo 19\- COD\_CONTA  da SAFX191

__RNF550 \- 16__

__Campo: INFO\_COMPL__

__Não preencher este campo, quando a origem dos dados for documento fiscal, SAFX43,994,162,191\.__

Origem SAFX 183

Preencher com a informação do campo 19 da SAFX183

# <a id="_Toc45807418"></a>Registro F559 – Processo Referenciado

__RNGF559__

__Origem Documentos Fiscais de Serviço e Mercadoria – Saída__

Nesse registro devem ser gravados os registros da SAFX114 relacionados aos documentos gerado no registro F550 que atendam ao critério abaixo:

Vinculação: \(campo ‘’15 – Vinculação da SAFX112\)

             Igual a ‘’2 – EFD PIS/COFINS

Origem do Processo: \(campo “14 – Origem do Processo” da SAFX114\)

	Igual a “1 – Justiça Federal”, “3 – Secex/RFB” ou “9 – Outros”

__Origem Documentos Utilities – SAFX42/43__

Deve ser gerado um registro F559 para cada registro existente na tela Registro C609 \-Processo Referenciado  que foi considerado no registro F550\. \(Módulo: MastersafDW / Básicos /  Manutenção / Documento Fiscal / Novo Documento Fiscal / Documento Fiscal Utilities / Registro C609 \-Processo Referenciado \)

__Origem Documentos Utilities – SAFX190/191__

Deverá ser gerado um registro F559  para cada registro informado na tela “Registro 609 \-Processo Referenciado ” do menu Manutenção >> Notas de Fornecimento de Energia Elétrica Água Canalizada e Gás \(C600\)’, localizada no Módulo: SPED / EFD – Escrituração Fiscal Digital \-  PIS/PASEP – COFINS\. 

__Origem F500/F510/F550/F560__

Deverá ser gerado um registro F559  para cada registro informado na tela “Processo Referenciado \(F509/519/559/569\)” do menu Manutenção >> Registro do Bloco F >> Demais Receitas– Lucro Presumido \(F500/F510/F550/F560\)’, localizada no Módulo: SPED / EFD – Escrituração Fiscal Digital \-  PIS/PASEP – COFINS

Poderão ser gerados N registros\.

__RNF559\-01__

__Campo: REG__

Gravar o texto fixo “F559”

__RNF559\-02__

__Campo: NUM\_PROC__ 

__Origem F500/F510/F550/F560__

Deverá ser recuperado do campo “Número Processo” da tela “Processo Referenciado \(F1509/519/559/569\)”\.

__Origem SAFX114__

Deverá ser recuperado do campo “Número Processo”

__SAFX42/43__

Deverá ser recuperado do campo “Número Processo”

__SAFX190/191__

Deverá ser recuperado do campo “Número Processo”

__RNF559\-03__

__Campo: IND\_PROC__

__Origem F500/F510/F550/F560__

Deverá ser recuperado do campo “Indicador da Origem do Processo” da tela “Processo Referenciado \(F509/519/559/569\)”\.

- Gravar “1”, caso a opção selecionada seja “1 – Justiça Federal”
- Gravar “2”, caso a opção selecionada seja “2 – Secretaria da Receita Federal do Brasil”

Gravar “9”, caso a opção selecionada seja “9 – Outros”

__Origem SAFX114__

 Campo “Indicador da Origem do Processo”

- Gravar “1”, caso a opção selecionada seja “1 – Justiça Federal”
- Gravar “2”, caso a opção selecionada seja “2 – Secretaria da Receita Federal do Brasil”

Gravar “9”, caso a opção selecionada seja “9 – Outros”

__SAFX42/43__

Campo “Indicador da Origem do Processo”

- Gravar “1”, caso a opção selecionada seja “1 – Justiça Federal”
- Gravar “2”, caso a opção selecionada seja “2 – Secretaria da Receita Federal do Brasil”

Gravar “9”, caso a opção selecionada seja “9 – Outros”

__SAFX190/191__

Campo “Indicador da Origem do Processo”

- Gravar “1”, caso a opção selecionada seja “1 – Justiça Federal”
- Gravar “2”, caso a opção selecionada seja “2 – Secretaria da Receita Federal do Brasil”

Gravar “9”, caso a opção selecionada seja “9 – Outros”

# <a id="_Registro_F560_–"></a><a id="_Toc45807419"></a>Registro F560 – Consolidação das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido – Incidência do PIS/Pasep e da Cofins pelo Regime de Competência \(Apuração Da Contribuição por Unidade de Medida de Produto\)

__RNGF560__

Neste registro deverão ser gravadas as informações Consolidadas das Operações da Pessoa Jurídica Submetida ao Regime de Tributação com Base no Lucro Presumido – Incidência do PIS/Pasep e da Cofins pelo Regime de Competência 

\[MFS10591\]

__Se o parâmetro: “Geração com base nas informações da SAFX183 e SAFX187” estiver marcado__ \(em dados iniciais\):

Este registro será gerado somente com base nas informações registradas na tela ‘Demais Receitas – Lucro Presumido \(F500/F510/F550/F560\)’, localizada no Módulo: SPED / EFD – Escrituração Fiscal Digital \-  PIS/PASEP – COFINS, Menu: Manutenção / Registro do Bloco F \(SAFX183/SAFX187\)

__Se o parâmetro: “Geração com base nas informações da SAFX183 e SAFX187” estiver desmarcado__ \(em dados iniciais\):

Este registro deverá ser gerado para as empresas do Lucro Presumido e com Regime de Competência Consolidada\. A recuperação dos dados utilizará os mesmos critérios que os utilizados na geração dos blocos C100/C111/C170/C180/C181/C185/C188/C380/C381/C385/C400/C405/C481/C485/C489/C490/C491/C495/C499/D200/D201/ D205/D209/D300/D309/D350/D359, porém deverão ser filtrados apenas os documentos de Saída\.

Além de considerarmos as informações registradas na tela ‘Demais Receitas – Lucro Presumido \(F500/F510/F550/F560\)’, localizada no Módulo: SPED / EFD – Escrituração Fiscal Digital \-  PIS/PASEP – COFINS, Menu: Manutenção / Registro do Bloco F \(SAFX183\)

OBS\. Caso os registros tenham fontes de dados tabelas distintas, a recuperação das informações deve considerar esta origem \(conforme informado na tela de Dados Iniciais\)\.

A data dos documentos que serão recuperados, devem considerar a opção informada no parâmetro: “Registro A100, C100,C180 e C190 – Seleção das Operações Geradoras de Receita”  disponível na tela de Dados Iniciais,  para definir se as notas devem ser recuperadas pela Data Fiscal ou pela Data Lancamento PIS/COFINS

O agrupamento do registro será por CST, Alíquota, Código do modelo, CFOP, código da conta e Informações complementares\.

\(Só iremos considerar neste registro, os documentos cuja apuração seja por unidade de Medida de Produto\)

__Verifique RNG3 – EFD e RNG4 – EFD\.__

__ATENÇÃO: Os documentos cancelados NÃO devem ser considerados na geração deste Registro\.__

Aplicar o  [__Tratamento para Geração de SCPs__](#_Tratamento_para_Geração)

__RNF560 \- 01__

__Campo: REG__

Gravar o Texto Fixo ”F560”

__RNF560 – 02__

__Campo: VL\_REC\_COMP	__

Notas Fiscais de Mercadoria 

Somatório do campo “23\-Valor Total da Nota” da SAFX07\.

Origem SAFX994

Somatório do campo “19\-Valor do Item ” da SAFX994\.

Origem SAFX 183

Preencher com o somatório do campo 20 da SAFX183

__RNF560 \- 03__

__Campo: CST\_PIS__

Para as notas sem Itens: Preencher com a informação do campo 249 \- COD\_SIT\_PIS da SAFX07

Notas Fiscais de Mercadoria

Para as notas com Itens:__ __Preencher com a informação do campo 175 – COD\_SITUACAO\_PIS da SAFX08

Origem SAFX994

Preencher com a informação do campo 32 \- COD\_SIT\_TRIB\_PIS da SAFX994\.

Origem SAFX 183

Preencher com a informação do campo 21 da SAFX183

__RNF560 \- 04__

__Campo: VL\_DESC\_PIS__

Para as notas *sem* itens à o campo deve ser preenchido com o valor desconto da SAFX07 \(campo 28\-Valor Descontos\);

Notas Fiscais de Mercadoria 

Para as notas *com *itens à neste caso deve\-se totalizar o valor do desconto de todos os itens de mercadoria considerando o campo “29\-Valor do Desconto” da SAFX08

Origem SAFX994

Preencher com o somatório do campo 20 \- VLR\_DESC  da SAFX994\.

Origem SAFX 183

Preencher com o somatório do campo 26 da SAFX183

__RNF560 \- 05__

__Campo: QUANT\_BC\_PIS__

Notas Fiscais de Mercadoria

Para as notas *com *itens à neste caso deve\-se totalizar o valor do desconto de todos os itens de mercadoria da nota, considerando o campo “176\-QTD\_BASE\_PIS”  da SAFX08\.

Origem SAFX994

Preencher com o somatório do campo 38\- QTD\_BASE\_PIS  da SAFX994\.

Origem SAFX 183

Preencher com o somatório do campo 25 da SAFX183

__RNF560 \- 06__

__Campo: ALIQ\_PIS\_QUANT__

Notas Fiscais de Mercadoria

Para as notas *com *itens à neste caso deve\-se totalizar o valor do desconto de todos os itens de mercadoria da nota, considerando o campo “177\-VLR\_ALIQ\_PIS\_R”  da SAFX08\.

Origem SAFX994

Preencher com o somatório do campo 39 \-VLR\_ALIQ\_ESPEC\_PIS  da SAFX994\.

Origem SAFX 183

Preencher com a informação do campo 24 da SAFX183

__RNF560 \- 07__

__Campo: VL\_PIS	__

Para as notas *sem* itens 

O campo deve ser preenchido com o valor do PIS da SAFX07 \(campo 103\-Valor PIS\);

Notas Fiscais de Mercadoria 

Para as notas *com *itens à deve\-se totalizar o valor do PIS de todos os itens da nota, considerando o campo “87\-VLR\_PIS” da SAFX08

Origem SAFX994

Preencher com o valor do campo 26 \- VLR\_PIS da SAFX994\.

Origem SAFX 183

Preencher com o somatório do campo 27 da SAFX183

__RNF560 \- 08__

__Campo: CST\_COFINS__

Para as notas sem Itens: Preencher com a informação do campo 250 \- COD\_SIT\_COFINS da SAFX07

Notas Fiscais de Mercadoria

Para as notas com Itens:__ __Preencher com a informação do campo 178 – COD\_SITUACAO\_COFINS da SAFX08

Origem SAFX994

Preencher com a informação do campo 35 \- COD\_SIT\_TRIB\_COFINS da SAFX994\.

Origem SAFX 183

Preencher com a informação do campo 28 da SAFX183

__RNF560 \- 09__

__Campo: VL\_DESC\_COFINS__

Para as notas *sem* itens à o campo deve ser preenchido com o valor desconto da SAFX07 \(campo 28\-Valor Descontos\);

Notas Fiscais de Mercadoria 

Para as notas *com *itens à neste caso deve\-se totalizar o valor do desconto de todos os itens de mercadoria da nota, considerando o campo “29\-Valor do Desconto” da SAFX08

Origem SAFX994

Preencher com a informação do campo 20 – VLR\_DESC da SAFX994\.

Origem SAFX 183

Preencher com o somatório do campo 33 da SAFX183

__RNF560 \- 10__

__Campo: QUANT\_BC\_COFINS__

Notas Fiscais de Mercadoria

Para as notas *com *itens à neste caso deve\-se totalizar o valor do desconto de todos os itens de mercadoria da nota, considerando o campo “179\-QTD\_BASE\_COFINS”  da SAFX08\. 

Origem SAFX994

Preencher com a informação do campo 41 \- QTD\_BASE\_COFINS da SAFX994\.

Origem SAFX 183

Preencher com o somatório do campo 32 da SAFX183

__RNF560 \- 11__

__Campo: ALIQ\_COFINS\_QUANT__

Notas Fiscais de Mercadoria

Para as notas *com *itens à neste caso deve\-se totalizar o valor do desconto de todos os itens de mercadoria da nota, considerando o campo “180\-VLR\_ALIQ\_COFINS\_R”  da SAFX08\.

Origem SAFX994

Preencher com a informação do campo 42 \- VLR\_ALIQ\_ESPEC\_COFINSda SAFX994\.

Origem SAFX 183

Preencher com o somatório do campo 31 da SAFX183

__RNF560 \- 12__

__Campo: VL\_COFINS__

Para as notas *sem* itens à o campo deve ser preenchido com o valor da COFINS da SAFX07 \(campo 105\-Valor COFINS\);

Notas Fiscais de Mercadoria 

Para as notas *com *itens à deve\-se totalizar o valor do PIS de todos os itens da nota, considerando o campo “89\-VLR\_COFINS” da SAFX08 

Origem SAFX994

Preencher com a informação do campo 27 \- VLR\_COFINS da SAFX994\.

Origem SAFX 183

Preencher com o somatório do campo 34 da SAFX183

__RNF560 \- 13 __

__Campo: COD\_MOD__

__\[ALTERADA – CH32179\_2012\]__

Preencher com a informação do campo 229 \- COD\_MODELO\_COTEPE, SAFX07

Origem SAFX994

Preencher com a informação do campo 03 \- COD\_MODELO  da SAFX994\.

Origem SAFX 183

Preencher com a informação do campo 11 da SAFX183	

__RNF560 \- 14__

__Campo: CFOP	__

Para as notas sem itens

Preencher com a informação do campo 14\-COD\_CFO da SAFX07

Notas Fiscais de Mercadoria

Preencher com a informação do campo 22\-COD\_CFO da SAFX08

Origem SAFX994

Preencher com a informação do campo 14 \- COD\_CFO da SAFX994\.	

Origem SAFX 183

Preencher com a informação do campo 12 da SAFX183

__RNF560 \- 15__

__Campo: COD\_CTA__

Para as notas sem itens

Preencher com a informação do campo 33\-COD\_CONTA da SAFX07

Notas Fiscais de Mercadoria 

Preencher com a informação do campo 105\-COD\_CONTA da SAFX08

Origem SAFX994

Preencher com a informação do campo 40\- COD\_CONTA da SAFX994\.

Origem SAFX 183

Preencher com a informação do campo 17 da SAFX183

__RNF560 \- 16__

__Campo: INFO\_COMPL__

__Não preencher este campo, quando a origem dos dados for documento fiscal, SAFX994\.__

Origem SAFX 183

Preencher com a informação do campo 19 da SAFX183

# <a id="_Toc45807420"></a>Registro F569 – Processo Referenciado

__RNGF569__

__Origem Documentos Fiscais de Serviço e Mercadoria – Saída__

Nesse registro devem ser gravados os registros da SAFX114 relacionados ao documento gerado no registro F560 que atendam ao critério abaixo:

Vinculação: \(campo ‘’15 – Vinculação da SAFX112\)

             Igual a ‘’2 – EFD PIS/COFINS

Origem do Processo: \(campo “14 – Origem do Processo” da SAFX114\)

	Igual a “1 – Justiça Federal”, “3 – Secex/RFB” ou “9 – Outros”

__Origem F500/F510/F550/F560__

Deverá ser gerado um registro F569  para cada registro informado na tela “Processo Referenciado \(F509/519/559/569\)” do menu Manutenção >> Registro do Bloco F >> Demais Receitas– Lucro Presumido \(F500/F510/F550/F560\)’, localizada no Módulo: SPED / EFD – Escrituração Fiscal Digital \-  PIS/PASEP – COFINS

Poderão ser gerados N registros\.

__RNF569\-01__

__Campo: REG__

Gravar o texto fixo “F569”

__RNF569\-02__

__Campo: NUM\_PROC__ 

__Origem F500/F510/F550/F560__

Deverá ser recuperado do campo “Número Processo” da tela “Processo Referenciado \(F1509/519/559/569\)”\.

__Origem SAFX114__

Deverá ser recuperado do campo “Número Processo”

__RNF569\-03__

__Campo: IND\_PROC__

__Origem F500/F510/F550/F560__

Deverá ser recuperado do campo “Indicador da Origem do Processo” da tela “Processo Referenciado \(F509/519/559/569\)”\.

- Gravar “1”, caso a opção selecionada seja “1 – Justiça Federal”
- Gravar “2”, caso a opção selecionada seja “2 – Secretaria da Receita Federal do Brasil”

Gravar “9”, caso a opção selecionada seja “9 – Outros”

__Origem SAFX114__

 Campo “Indicador da Origem do Processo”

- Gravar “1”, caso a opção selecionada seja “1 – Justiça Federal”
- Gravar “2”, caso a opção selecionada seja “2 – Secretaria da Receita Federal do Brasil”

Gravar “9”, caso a opção selecionada seja “9 – Outros”

# <a id="_Registro_F600_–"></a><a id="_Toc45807421"></a>Registro F600 – Contribuição Retida na Fonte

__RNG\-F600__

Gerar um registro F600 para cada registro informado através do módulo: EFD\-PIS/COFINS, menu: Manutenção → Contribuição Retida na Fonte, que atenda ao critério abaixo:

Data de Pagamento: 

Entre a Data Inicial e Data Final de geração do arquivo ou anterior\.

O agrupamento dos registros deve ser feito de acordo com os campos chaves deste registro:

Indicador de Natureza da Retenção na Fonte \(Campo 02\)

Data da Pagamentódigo da Receita \(o \(Campo 14\)

C Campo 04\)

Indicador da Natureza da Receita \(Campo 07\)

CNPJ \(Campo 08\)

OBS: a partir da OS3590 o agrupamento será a partir da Data de Pagamento e não mais da Data de Retenção\. A Data de Pagamento deverá sempre ser igual ou menor que a DT\_FIM do arquivo, gerado no registro 0000\.

Aplicar o  [__Tratamento para Geração de SCPs__](#_Tratamento_para_Geração)

__RNF600\-03__

A data gerada nesse campo será a “Data de Pagamento” da SAFX145\.

__RNF600\-06__

Ao gerar o campo 06 – COD\_REC do registro F600, a informação deverá ser recuperada do campo “Código da Receita” \(12/SAFX145\) da tela de manutenção do registro F600 através do <a id="OLE_LINK1"></a><a id="OLE_LINK2"></a><a id="OLE_LINK3"></a><a id="OLE_LINK4"></a>menu Manutenção >> Registro do Bloco F >> Contribuição Retida na Fonte \(F600\)\.

__\[ALTERADA – CH11364\_2016\]__

__Tratamento:__

- Deverão ser recuperados e gravados no arquivo os 4 \(quatro\) primeiros dígitos do Código de Receita;
- Se o campo não estiver preenchido será gravado em branco \(“||” pipe\-pipe\) no arquivo\.

__RNF600\-07__

__MFS\-2273__

07 – IND\_NAT\_REC, a informação deverá ser recuperada do campo “Natureza Receita” caminho: menu Manutenção >> Registro do Bloco F >> Contribuição Retida na Fonte \(F600\)\.

Obs: Se não preenchido, no campo IND\_NAT\_RET da tabela X145\_CONTRIB\_RET\_FONTE será gravado “9”, para este caso gerar branco \(“||”\)\.

# <a id="_Registro_F700_–"></a><a id="_Toc45807422"></a>Registro F700 – Deduções Diversas

__RNG\-F700__

Gerar um registro F700 para cada registro informado através do módulo: EFD\-PIS/COFINS, menu: Manutenção → Deduções Diversas, que atenda ao critério abaixo:

Competência:

Igual a competência \(mês/ano\) da geração do arquivo\.

Aplicar o  [__Tratamento para Geração de SCPs__](#_Tratamento_para_Geração)

# <a id="_Toc45807423"></a>Registro F800 – Créditos Decorrentes de Eventos de Incorporação, Fusão e Cisão

__RNG\-F800__

Gerar um registro F800 para cada registro informado através do módulo: EFD\-PIS/COFINS, menu: Manutenção → Créditos Decorrentes de Eventos de Incorporação, Fusão e Cisão, que atenda ao critério abaixo:

MFS\-22180

Se a “Data Apropriação Credito” for menor ou igual a DT\_FIN \(data fim da geração do arquivo magnético da EFD Contribuições\)\.

Senão manter a geração através da:

Data do Evento \+ 1 dia: \(dia seguinte à data do evento\)

Entre a Data Inicial e Data Final de geração do arquivo\.

