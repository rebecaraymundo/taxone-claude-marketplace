# MTZ-OTF-SEFIP

- **Fonte:** MTZ-OTF-SEFIP.docx
- **Modificado:** 2020-08-31
- **Tamanho:** 33 KB

---

# Obrigações de Tributos Federais – Geração SEFIP

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS2495

Título do Requisito\.

O sistema irá gerar o registro tipo 12 \- Informações Adicionais do Recolhimento da Empresa, porém nesse registro possuirá regras de geração de valores apenas para os campos obrigatórios e o campo 26 que irá receber informações de valores pagos a cooperativas\.

CH85100

CH46422\-I

Ajustar relatório de conferência

Não demonstrar estabelecimentos sem movimento

CH46422\-K

Ajustar geração do Código de Ocorrência

Ajustar arredondamento da alíquota para cálculo da Ocorrência\.

OS3096\-F

Geração por Empresa

Inclusão de opção de geração por empresa\.

OS3447

Código de recolhimento SEFIP

Inclusão das opções 135 e 150 na tela e geração do arquivo SEFIP

CH4673\_2014

Geração do Indicador de CNAE Preponderante

O objetivo deste documento de requisito é permitir que o campo 14 – Indicador de Alteração CNAE do registro 10 – Informações da Empresa \(Header da empresa\) seja gerado com a opção “P” \(CNAE Preponderante\) para que o arquivo seja validado, uma vez que esse indicador é válido a partir de 12/2008\.

CH24869\_2014

Ajustar geração do SEFIP

Este documento tem como objetivo ajustar a geração do SEFIP para considerar os registros de acordo com o Período de Competência preenchido\.

CH122\_2015

Inclusão novo código no campo “Cód\. Outras Entidades” de Parâmetros SEFIP

Este documento tem como objetivo incluir o código 0071 na listagem do campo Cód\. Outras Entidades para parametrização da SEFIP\.

CH1831\_2016

Geração do Indicador de CNAE Preponderante

Este documento tem como objetivo alterar o preenchimento do campo 14 – Indicador de Alteração CNAE do registro 10 – Informações da Empresa \(Header da empresa\) em casos de geração por centralização pelo estabelecimento matriz\.

CH1831\_2016

\(MFS11407\)

Inclusão novo código no campo “Cód\. Outras Entidades” de Parâmetros SEFIP

Este documento tem como objetivo incluir o código 0131 na listagem do campo Cód\. Outras Entidades para parametrização da SEFIP\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

O sistema irá gerar o registro do tipo 12 apenas quando o usuário selecionar a opção Gerar pagamentos à cooperativas no momento da geração\.

__OS2495__

__RN01__

No campo Tipo do Registro o sistema irá gerar sempre com o valor “12” \.

__OS2495__

__RN02__

Para o campo de tipo de inscrição da empresa o sistema irá recuperar o mesmo valor do campo 2 do registro tipo 10\- Informações da empresa \(Esse campo inicia na posição 3 e termina na posição 3\), essa informação é obtida através da tabela ESTABELECIMENTO do campo CGC\.

__OS2495__

__RN03__

Para o campo de  Inscrição da empresa o sistema irá recuperar o mesmo valor do campo 3 do registro tipo 10\- Informações da empresa \(Esse campo inicia na posição 4 e termina na posição 17\)\.

__OS2495__

__RN04__

O sistema irá gerar o campo com “Zeros”  até completar as todas as posições do campo\.

__OS2495__

__RN05__

O sistema irá gerar com espaços em Branco até completar todas as posições do campo\.

__OS2495__

__RN06__

Para a geração do campo Valores pagos à Cooperativas \(Campo 26 do registro tipo 12\), o sistema irá considerar apenas os Documentos Fiscais que sejam de entrada e pessoa Física/Jurídica que possua o campo ind\_calsse\_PFJ igual a 02\- cooperativa ou 05\- Cooperativa de Transporte e os Documentos fiscais estejam dentro do período de geração\.

Após recuperar os Documentos fiscais  com tais características o sistema irá executar o somatório do campo Segunda Base de Cálculo para INSS \(Campo 151 da Safx07\)

__OS2495__

__RN07__

Será a quebra de linha

__OS2495__

__RN08__

O novo campo \(Gerar pagamentos à cooperativas\) será por default desmarcado\.

__OS2495__

__RN09__

Quando forem gerados mais de um estabelecimento na SEFIP, e não houver movimento para algum deles:

→ Não incluir a geração deste estabelecimento no meio magnético;

→ Exibir no log de processo a mensagem: *“O estabelecimento XXX foi desconsiderado do meio magnético neste período\. Não foram encontrados dados para geração do Registro 30”*\.

Onde XXX é o estabelecimento que foi desconsiderado\. 

Se todos os estabelecimentos tiverem movimento, desconsiderar esta regra\.

__CH85100__

__RN10__

Quando forem gerados mais de um estabelecimento na SEFIP, e não houver movimento para algum deles, considerar a seguinte regra para o relatório de conferência:

→ Não incluir o estabelecimento sem movimento no relatório de conferência;

→ Exibir no log de processo a mensagem: *“O estabelecimento XXX foi desconsiderado do relatório de conferência por não ter movimentação em nenhum registro”*\.

Onde XXX é o estabelecimento que foi desconsiderado\. 

Se todos os estabelecimentos tiverem movimento, desconsiderar esta regra\.

__CH46422\-I__

__RN11__

Quando for realizada a geração da SEFIP com o parâmetro “Regra de Retenção para o Campo Ocorrência” setado: 

Caso o valor total dos Documentos Fiscais for maior que o informado no parâmetro o sistema irá comparar o valor máximo de contribuição retida com o valor do imposto preenchido no Documento Fiscal se os valores forem iguais o sistema deverá gerar o campo de ocorrência em branco no arquivo magnético\.

Caso o valor total dos Documentos Fiscais for menor que o valor o sistema deverá verificar se o valor do INSS é confere com o percentual informado no parâmetro \(se a alíquota informada for 11%, considerar qualquer percentual a partir de 10,51%\)\. Se os valores forem iguais e o cadastro de Pessoa Física/ Jurídica forem iguais a 5, o arquivo magnético não deverá conter o campo ocorrência preenchido com o valor 5\. O campo de ocorrência deverá estar em branco\.

__OS2426 / CH46422\-K__

__RN10__

O parâmetro “Processar dados por” \(Empresa/Estabelecimento\) comporta\-se da seguinte maneira:

Processar dados por Estabelecimento \(Padrão\)

Nesta situação serão listadas todos os estabelecimentos pertencentes à empresa do login, considerando os estabelecimentos aos quais o usuário tenha acesso\.

Caso o parâmetro “Processar dados por” seja preenchido com a opção “Empresa”, a listagem de estabelecimentos será substituída pela lista de todas as empresas as quais o usuário tenha acesso\. Nesta situação todos os estabelecimentos pertencentes as empresas selecionadas serão processados, levando em consideração apenas os estabelecimentos aos quais o usuário em questão tenha acesso\.

__OS3096\-F__

__RN11__

__Campo \(Cod Recolhimento SEFIP\)__

Após a inclusão das opções 135 e 150 na tela de geração do meio magnético deve gravar

__Se selecionado a opção: __

__135__ \- Recolhimento ao FGTS e informações à previdência Social relat\. ao trabalhador avulso não portuário \(no prazo ou em atraso\)\.

Gravar 135 na posição 298 do arquivo gerado SEFIP

__Se selecionado a opção__: 

__150__ \- Recolhimento ao FGTS e informações à previdência Social de Empresa Prest\. de serviços de mão\-de\-obra e trabalho temporário \(Lei nº 6\.019/74\)

Gravar 150 na posição 298 do arquivo gerado SEFIP

Para as demais opções continuar gravando da mesma forma

__OS3447__

__RN12__

__\[ALTERADA \- CH4673\_2014/ CH1831\_2016\]__

Ao gerar a SEFIP, através do menu Outras Obrigações >> SEFIP >> Geração do Meio Magnético do módulo Obrigações de Tributos Federais:

Se o campo Período de Competência for menor igual a 05/2008:

- O sistema deverá gravar “N” no campo 14 – Indicador de Alteração CNAE do registro 10 – Informações da Empresa \(Header da empresa\)\.

Se o campo Período de Competência for maior igual a 06/2008:

- Quando a opção “Processar dados por:” for por Estabelecimento e existir parametrização de Centralização por Estabelecimento no item de menu Parâmetros do módulo Federal – OTF, o sistema deverá gravar “P” no campo 14 – Indicador de Alteração CNAE do registro 10 – Informações da Empresa \(Header da empresa\) para o estabelecimento centralizador e deverá gravar “N” aos estabelecimentos centralizados, caso contrário, ou seja, se não houver a parametrização de Centralização por Estabelecimento, gravar todos com “P”;
- Quando a opção “Processar dados por:” for por Empresa e existir parametrização de Centralização por Estabelecimento no item de menu Parâmetros do módulo Federal – OTF, o sistema deverá gravar “P” no campo 14 – Indicador de Alteração CNAE do registro 10 – Informações da Empresa \(Header da empresa\) para o estabelecimento centralizador e deverá gravar “N” aos estabelecimentos centralizados, caso contrário, ou seja, se não houver a parametrização de Centralização por Estabelecimento, gravar todos com “P”;
- Quando a opção “Processar dados por:” for por Empresa e for gerar por centralização pelo estabelecimento matriz, o sistema deverá gravar “P” no campo 14 – Indicador de Alteração CNAE do registro 10 – Informações da Empresa \(Header da empresa\)\.

__Observação:__ no momento não serão tratadas as opções “S” ou “A”\.

__CH4673\_2014__

__CH1831\_2016__

__RN13__

Para a geração do SEFIP, considerar os Documentos Fiscais que estejam dentro do Período de Competência preenchido na tela de geração \(verifica pela data fiscal da NF\) e ainda compreendendo a parametrização da Data de Vigência em Federal >> OTF >> Outras Obrigações >> SEFIP >> Parâmetros, ou seja, se estiver parametrizado dentro do Período de Competência considerar o parâmetro, caso contrário não gerar e emitir a mensagem no log: *“Status: Alerta \- Req 10 \- Inf\. Empresa: Não há informações de parâmetros da Sefip p/ o estabelecimento <<levar código do estabelecimento selecionado>>”\.*

__CH24869\_2014__

__RN14__

__Campo Cód\. Outras Entidades de Parâmetros SEFIP__

__\[ALTERADA – CH122\_2015 – CH5681\_2017\]__ – Inclusão de Código

__Conteúdo:__

- 0071 \- Salário educação \+ INCRA \+ SENAI \+ SEBRAE
- 0131 – Sem Convênio

__CH122\_2015__

__CH5681\_2017__

Considerações deste modelo:

__Quando uma Regra de Negócio for Excluída, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[EXCLUÍDA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

__Quando uma Regra de Negócio for Alterada, deverá ser indicada, em sua posição original, uma observação conforme exemplo abaixo descrito abaixo:__

__RN01__

__\[ALTERADA – OSXPTO\]__ Descrição da Regra de Negócio 01

OSNNNN

