# MTZ-OTF-Gerar_Registros_20_e_21_da_SEFIP

- **Fonte:** MTZ-OTF-Gerar_Registros_20_e_21_da_SEFIP.docx
- **Modificado:** 2020-08-31
- **Tamanho:** 34 KB

---

# OTF \- Gerar Registros 20 e 21 da SEFIP Autônomos

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS2774

OTF \- Gerar Registros 20 e 21 da SEFIP Autônomos

- Incluir código __155 – Recolhimento ao FGTS e informações à Previdência Social de obra de construção civil – empreitada total ou obra própria \(no prazo ou em atraso\)__ no campo “Cód\. Recolhimento SEFIP” da tela de Geração do Meio Magnético SEFIP\-Autônomos\.
- Incluir campos “Salário Família” e “Retenção \(Lei 9711/98” na tela de parâmetros da SEFIP\.
- Gerar Registro 20 – Registro do Tomador de Serviço/Obra de Construção Civil\.
- Gerar Registro 21 – Registro de informações adicionais do Tomador de Serviço/Obra de Const\. Civil\.
- Alterar Registro 30 – Registro do Trabalhador para contemplar CNPJ e CEI\.

OS3447

Código de recolhimento SEFIP

- Inclusão das opções 135 e 150 na tela e geração do arquivo SEFIP
- Gerar Registro 20 – Registro do Tomador de Serviço/Obra de Construção Civil também para os códigos 135 e 150
- Gerar Registro 21 – Registro de informações adicionais do Tomador de Serviço/Obra de Const\. Civil, também para os códigos 135 e 150

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN01__

Incluir o código “155 \- Recolhimento ao FGTS e informações à Previdência Social de obra de construção civil – empreitada total ou obra própria \(no prazo ou em atraso\)” no conteúdo do campo no conteúdo do campo “Cód\. Recolhimento SEFIP” da tela de Geração do Meio Magnético SEFIP\-Autônomos\. 

Incluir o código “135 \- Recolhimento ao FGTS e informações à previdência Social relat\. ao trabalhador avulso não portuário \(no prazo ou em atraso\) no conteúdo do campo no conteúdo do campo “Cód\. Recolhimento SEFIP” da tela de Geração do Meio Magnético SEFIP\-Autônomos\. 

Incluir o código “150 \- Recolhimento ao FGTS e informações à previdência Social de Empresa Prest\. de serviços de mão\-de\-obra e trabalho temporário \(Lei nº 6\.019/74, no conteúdo do campo no conteúdo do campo “Cód\. Recolhimento SEFIP” da tela de Geração do Meio Magnético SEFIP\-Autônomos\.

__OS2774__

__OS3447__

__RN02__

Essa tela citada na regra RN01 encontra\-se no módulo Federal – Obrigações de Tributos Federais e na tela Outras Obrigações – SEFIP – Autônomos – Geração do Meio Magnético\.

__OS2774__

__RN03__

Para a correta geração do registro tipo 20 – Registro do Tomador de Serviço/Obra de Construção Civil e 21 – Registro de informações adicionais do Tomador de Serviço/Obra de Construção Civil, o código selecionado na tela de geração deve ser 130, 135, 150, 155 ou 608\.

__OS2774__

__OS3447__

__RN04__

Gravar no campo 1 – Tipo de Registro o texto fixo “20”\.

__OS2774__

__RN05__

Gravar no campo 2 – Tipo de Inscrição – Empresa o valor “1” \(CNPJ\)\.

__OS2774__

__RN06__

Gravar no campo 3 – Tipo de Inscrição\-Tomador/Obra Const\. Civil o CNPJ do estabelecimento\. Essa informação deverá ser recuperada do campo CGC da tabela ESTABELECIMENTO\.

__OS2774__

__RN07__

Gravar no campo 4 – Tipo de Inscrição\-Tomador/Obra Const\. Civil o valor “2” \(CEI\)\. 

__OS2774__

__RN08__

Gravar no campo 5 – Inscrição Tomador/Obra Const\. Civil o CEI do estabelecimento\. Essa informação deverá ser recuperada do campo CEI\_PORT63 da tabela ESTABELECIMENTO\.

__OS2774__

__RN09__

Ao gravar o campo 6 – Zeros, completar com 0’s \(zeros\)\.

__OS2774__

__RN10__

Gravar no campo 7 – Nome do Tomador/Obra de Const\. Civil o conteúdo do campo RAZAO\_SOCIAL da tabela ESTABELECIMENTO\.

__OS2774__

__RN11__

Gravar no campo 8 – Logradouro, rua, nº, andar, apartamento o conteúdo dos campos ENDERECO, NUM\_ENDERECO e COMPL\_ENDERECO de forma concatenada\. Essas informações deverão ser recuperadas da tabela ESTABELECIMENTO\.

__OS2774__

__RN12__

Gravar no campo 9 – Bairro o conteúdo do campo BAIRRO da tabela ESTABELECIMENTO\.

__OS2774__

__RN13__

Gravar no campo 10 – CEP o conteúdo do campo CEP da tabela ESTABELECIMENTO\.

__OS2774__

__RN14__

Gravar no campo 11 – Cidade a descrição do município que se encontra no conteúdo do campo COD\_MUNICIPIO da tabela ESTABELECIMENTO\.

__OS2774__

__RN15__

Gravar no campo 12 – Unidade da Federação a UF associada ao conteúdo do campo IDENT\_ESTADO da tabela ESTABELECIMENTO\.

__OS2774__

__RN16__

Gravar no campo 13 – Código de Pagamento GPS o conteúdo do campo “Cód\. Pagamento GPS” na tela Parâmetros SEFIP – Autônomos \(menu Outras Obrigações >> SEFIP – Autônomos >> Parâmetros\) no módulo Obrigações de Tributos Federais\.

__OS2774__

__RN17__

Gravar no campo 14 – Salário Família o conteúdo do campo “Salário Família” na tela de Geração do Meio Magnético da SEFIP – Autônomos \(menu Outras Obrigações >> SEFIP – Autônomos >> Geração do Meio Magnético\) no módulo Obrigações de Tributos Federais\.

__OS2774__

__RN18__

Ao gravar o campo 15 – Contrib\. Desc\. Empregado Referente à competência 13, completar com 0’s \(zeros\)\.

__OS2774__

__RN19__

Ao gravar o campo 16 – Indicador de valor negativo ou positivo, completar com 0’s \(zeros\)\.

__OS2774__

__RN20__

Ao gravar o campo 17 – Valor Devido à Previdência Social, Referente à competência 13, completar com 0’s \(zeros\)\.

__OS2774__

__RN21__

Gravar no campo 18 – Valor de Retenção \(Lei 9\.711/98\) o conteúdo do campo “Retenção \(Lei 9711/98\)” na tela de Geração do Meio Magnético da SEFIP – Autônomos \(menu Outras Obrigações >> SEFIP – Autônomos >> Geração do Meio Magnético\) no módulo Obrigações de Tributos Federais\.

__OS2774__

__RN22__

Ao gravar o campo 19 – Valor das faturas emitidas para o tomador, completar com 0’s \(zeros\)\.

__OS2774__

__RN23__

Ao gravar o campo 20 – Zeros, completar com 0’s \(zeros\)\.

__OS2774__

__RN24__

Ao gravar o campo 21 – Brancos, completar espaços em branco\.

__OS2774__

__RN25__

Ao gravar o campo 22 – Final de Linha, gravar “\*” para marcar o fim de linha\.

__OS2774__

__RN26__

Gravar no campo 1 – Tipo de Registro o texto fixo “21”\.

__OS2774__

__RN27__

Gravar no campo 2 – Tipo de Inscrição – Empresa o valor “1” \(CNPJ\)\.

__OS2774__

__RN28__

Gravar no campo 3 – Inscrição da Empresa o CNPJ do estabelecimento\. Essa informação deverá ser recuperada do campo CGC da tabela ESTABELECIMENTO\.

__OS2774__

__RN29__

Gravar no campo 4 – Tipo de Inscrição\-Tomador/Obra Const\. Civil o valor “2” \(CEI\)\. 

__OS2774__

__RN30__

Gravar no campo 5 – Inscrição Tomador/Obra Const\. Civil o CEI do estabelecimento\. Essa informação deverá ser recuperada do campo CEI\_PORT63 da tabela ESTABELECIMENTO\.

__OS2774__

__RN31__

Ao gravar o campo 6 – Zeros, completar com 0’s \(zeros\)\.

__OS2774__

__RN32__

Ao gravar o campo 7 – Compensação – Valor Corrigido, completar com 0’s \(zeros\)\.

__OS2774__

__RN33__

Ao gravar o campo 8 – Compensação – Período Inicio, completar com espaços em branco\.

__OS2774__

__RN34__

Ao gravar o campo 9 – Compensação – Período Fim, completar com espaços em branco\.

__OS2774__

__RN35__

Ao gravar o campo 10 – Recolhimento de Competências Anteriores – Valor do INSS sobre folha de pagamento, completar com 0’s \(zeros\)\.

__OS2774__

__RN36__

Ao gravar o campo 11 – Recolhimento de Competências Anteriores – Outras Entidades sobre folha de pagamento, completar com 0’s \(zeros\)\.

__OS2774__

__RN37__

Ao gravar o campo 12 – Parcelamento do FGTS – somatório das remunerações das categorias 01, 02, 03, 05 e 06, completar com 0’s \(zeros\)\.

__OS2774__

__RN38__

Ao gravar o campo 13 – Parcelamento do FGTS – somatório das remunerações das categorias 04 e 07, completar com 0’s \(zeros\)\.

__OS2774__

__RN39__

Ao gravar o campo 14 – Parcelamento do FGTS – valor recolhido, completar com 0’s \(zeros\)\.

__OS2774__

__RN40__

Ao gravar o campo 15 – Brancos, preencher com espaços em branco\.

__OS2774__

__RN41__

Ao gravar o campo 16 – Final de Linha, gravar “\*” para marcar o fim de linha\.

__OS2774__

__RN42__

Deverá ser criado na tela de Geração do Meio Magnético da SEFIP \(módulo Obrigações de Tributos Federais, menu Outras Obrigações >> SEFIP – Autônomos >> Geração do Meio Magnético\) os campos “Salário Família” e “Retenção \(Lei 9711/98\)”\. Esses campos deverão ser numéricos de 15 posições com 2 casas decimais\.

__OS2774__

__RN43__

Gravar no campo 2 – Tipo de Inscrição – Empresa o valor “1” \(CNPJ\)\.

__OS2774__

__RN44__

Gravar no campo 3 – Tipo de Inscrição\-Tomador/Obra Const\. Civil o CNPJ do estabelecimento\. Essa informação deverá ser recuperada do campo CGC da tabela ESTABELECIMENTO\.

__OS2774__

__RN45__

Gravar no campo 4 – Tipo de Inscrição\-Tomador/Obra Const\. Civil o valor “2” \(CEI\)\. 

__OS2774__

__RN46__

Gravar no campo 5 – Inscrição Tomador/Obra Const\. Civil o CEI do estabelecimento\. Essa informação deverá ser recuperada do campo CEI\_PORT63 da tabela ESTABELECIMENTO\.

__OS2774__

__RN47__

Gerar mensagem no log de processo quando o campo CEI\_PORT63 da tabela ESTABELECIMENTO não estiver preenchido\.

__OS2774__

__RN48__

Deve ser gerado no campo 22 – Salário\-Família do registro tipo 10 o total do Salário Família de todos os autônomos\.

__OS2774__

__RN49__

O campo 22 – Salário\-Família do registro tipo 10 deve ser gerado independente do Código de Recolhimento SEFIP mencionado\.

__OS2774__

__RN50__

O campo 5 – Inscrição Tomador/Obra de Construção Civil do registro tipo 30 deverá ser preenchido de acordo com a regra abaixo:

- Caso o campo 4 – Tipo de Inscrição – Tomador/Obra de Construção Civil = 2, deverá ser recuperado o campo “Cadastro Específico INSS\-CEI” da tabela ESTABELECIMENTO

Caso o campo “Cadastro Específico INSS\-CEI” da tabela ESTABELECIMENTO não esteja preenchido deverá ser recuperado o campo “CNPJ” da tabela ESTABELECIMENTO\. Nesse caso em específico de ser recuperado o campo “CNPJ” o campo 4 – Tipo de Inscrição deverá ser alterado de “2” para “1”\.

Essa regra vale para os códigos de recolhimento 135 e 150\. Essa regra não é válida para os códigos de recolhimento 130, 155 e 608\. As regras desses códigos devem ser mantidas conforme atualmente\.

__OS3447__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

