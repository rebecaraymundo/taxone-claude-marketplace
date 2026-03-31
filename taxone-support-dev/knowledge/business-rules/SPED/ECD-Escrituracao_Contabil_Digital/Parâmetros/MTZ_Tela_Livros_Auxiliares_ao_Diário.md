# MTZ_Tela_Livros_Auxiliares_ao_Diário

- **Fonte:** MTZ_Tela_Livros_Auxiliares_ao_Diário.docx
- **Modificado:** 2023-09-28
- **Tamanho:** 47 KB

---

ECD – Livros Auxiliares ao Diário

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS2328I

ECD – Livros Auxiliares R e A \(Matriz\)

Atualmente a Mastersaf gera somente o Livro G “Diário Geral” para atendimento do SPED, porém, existem os livros R “Diário Resumido” e A “Diário Auxiliar” que deverão ser atendidos pela Mastersaf, tanto para empresas normais como, instituições financeiras como é o caso da Yamaha, que gera as informações com base no plano de contas COSIF\.

Essa OS deve atender a geração dos os livros R – Diário Resumido e A – Diário Auxiliar para as instituições financeiras e empresas em geral\.

OS2328IB

ECD – Livros Auxiliares R e A \(Matriz\) 

Atualmente a Mastersaf gera somente o Livro G “Diário Geral” para atendimento do SPED, porém, existem os livros R “Diário Resumido” e A “Diário Auxiliar” que deverão ser atendidos pela Mastersaf, tanto para empresas normais como instituições financeiras como é o caso da Yamaha, que gera as informações com base no plano de contas COSIF\.

Essa OS deve atender a geração dos os livros R – Diário Resumido e A – Diário Auxiliar para as instituições financeiras e empresas em geral\.

CH64346

Registro I012

O sistema não está recuperando a informação correta do campo 03 \(NAT\_LIVR\) para o registro I012 do SPED Contábil, o objetivo do documento é criar regra de negócio direcionando para a informação correta\.

CH14409\_2012

Geração do 04 \- NAT\_LIVR do Registro I030 para Livros Auxiliares do Tipo A e Z

O objetivo deste requisito é definir a regra para geração do campo 04 \- NAT\_LIVR do Registro I030 quando a geração do arquivo da ECD for referente a um livro do Tipo A – Livro Diário Auxiliar e Tipo Z – Razão Auxiliar\.

CH15368\_2012

Livro Auxiliar

Considerar as contas parametrizadas na tela ‘Livros Auxiliares ao Diário’, localizada no módulo SPED / ECD – Escrituração Contábil Digital , menu: Parâmetros\.

CH25719\_2016

Ajuste na regra de parametrização do Controle da Obrigação

Alteração de regra para habilitar a aba Livro Auxiliares ao Diário também para o Livro Principal “G – Livro Diário”\.

__MFS564818__

Ajuste na regra de parametrização do Campo “Contas Empresas Selecionadas”

Alteração de regra na tela de “Livro Auxiliar ao Diário” no Campo “Contas Empresas Selecionadas”, que passa a permitir a parametrização da mesma conta contábil para os Livros A e Z\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Parâmetros – Livros Auxiliares ao Diário__

__RN01__

No campo “Livro \(Cód\./Desc\.\)” o usuário deverá informar uma codificação interna e a descrição para controle do tipo de Livro Auxiliar \(Ex\.: 001\)

__OS2328I\_2__

__RN02__

No campo “Tipo de Escrituração” o usuário deverá selecionar qual é o tipo de escrituração do livro, podendo ser: *0 \- Digital *\(incluídos no SPED\) ou *1 \- Outros*

__OS2328I\_2__

__RN03__

No campo “Tipo de Livro” o usuário poderá selecionar o livro tipo “A \- Livro Diário Auxiliar ao Diário com Escrituração Resumida" ou tipo “Z \- Razão Auxiliar”\. Obs: Essa OS trata apenas da Regra para o Livro “A” e “R”, sendo assim não falaremos do livro “Z” no momento\.

__OS2328I\_2__

__RN04__

No campo “Descritivo do Livro para o SPED” o usuário deverá digitar qual será a descrição do livro Auxiliar a ser apresentada no arquivo digital do SPED\. Esta descrição pode ser diferente da utilizada no campo "Livro \(Cód\./Desc\)”\. 

__OS2328I\_2__

__RN05__

No campo “Informar Conta para a Pesquisa” o usuário irá Informar o código da Conta Analítica para a pesquisa, isso fará com que essa conta seja apresentada no quadro “Contas da empresa a selecionar”\. O usuário também poderá clicar diretamente em "Pesquisar" e o sistema apresentará a lista de todas as contas analíticas para seleção\. 

__OS2328I\_2__

__RN06__

No quadro “Contas da Empresa a Selecionar” será apresentado as contas que foram encontradas a partir da pesquisa, efetuada na Regra acima \(RN10\)\. O usuário deverá selecionar a Conta Analítica que será associada ao Livro Auxiliar indicado e clicar no botão "Adicionar Contas"\. 

__\[ALTERAÇÃO\-MFS564818\] __Alteração da regra de parametrização da opção “Contas Empresas Selecionadas”

__Tratamento:__

Alteração para permitir ao usuário parametrizar a mesma Conta Contábil para os Livros A e Z, esta alteração deverá ser implementada na tela de “Livro Auxiliar ao Diário” no Campo “Contas Empresas Selecionadas”\.

__OS2328I\_2__

__MFS564818__

__RN07__

No Quadro “Contas da Empresa Selecionadas” será apresentado a lista de contas que foram adicionadas após a regra acima \(RN11\)\.

__OS2328I\_2__

__RN08__

Após ter adicionado a conta selecionada conforme regras \(RN10, RN11 e RN12\) o usuário deverá confirmar a inclusão, acionando o botão “![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAARCAIAAABIGvtnAAAAAXNSR0IArs4c6QAAAAlwSFlzAAAOxAAADsIBw3GpnQAAAMZJREFUOE9jfPPyBgM1ABM1DAGZwUiki0TENeBWYtWCxSCIHmTVIJGGBoTbGxowzcLutf//GeBOQHYL3CwsgkCzIQg5sIAGARHCXcjOAYqCuXCNEAbCa8JiiFCAG8rICGaiGrRGQzIkIh3NbgKxBnEXMYCAQVAXEWESwiCgHjiCaARyiUwcQMUIg9BCnSRTUAxCdj6yKSBHoQY2ZkgTm7LRUs2aFTMdHO3Rwo3YLHJg/0G4TkxTiHUREZGGFNjEqMajhmrFCAB0MWRmMtNYQwAAAABJRU5ErkJggg==)” \(Confirma\)\.

__OS2328I\_2__

__RN09__

Se durante a geração do livro perfil “R” o sistema verificar que o campo 3 \(NAT\_LIVR\) do registro I012 não estiver preenchido, o mesmo deverá apresentar no Log a seguinte mensagem:

“Tipo I012 – Registro não será gerado\. Favor informar o Descritivo do Livro para o SPED\. \(Livro Auxiliar\) de escrituração\. Localização: SPED \-\-> ECD Escrituração Contábil Digital \-\-> Parâmetros \-\-> Livros Auxiliares ao Diário”

__\[ALTERADA – MFS46921\]__ A regra acima também é válida para o livro perfil “B”\.

__OS2328IB__

__MFS46921__

__RN10__

Se durante a geração do livro perfil “R” o sistema verificar que o campo 4 \(TIPO\) do registro I012 não estiver preenchido, o mesmo deverá apresentar no Log a seguinte mensagem:

“Tipo I012 – Registro não será gerado\. Favor informar Tipo de escrituração do Livro associado para o SPED\. \(Livro Auxiliar\) de escrituração\. Localização: SPED \-\-> ECD Escrituração Contábil Digital \-\-> Parâmetros \-\-> Livros Auxiliares ao Diário”

__\[ALTERADA – MFS46921\]__ A regra acima também é válida para o livro perfil “B”\.

__OS2328IB__

__MFS46921__

__RN11__

Se durante a geração do livro perfil “R” o sistema verificar que o campo 2 \(COD\_CTA\_RES\) do registro I015 não estiver preenchido, o mesmo deverá apresentar no Log a seguinte mensagem:

“Tipo I015 – Registro não será gerado\. Favor informar o Código da conta analítica do Livro Diário com Escrituração Resumida \(Livro “R”\) que recebe os lançamentos globais\. Localização: Módulo SPED \-> ECD Escrituração Contábil Digital \-> Parâmetros \-> Livros Auxiliares ao Diário”

__\[ALTERADA – MFS46921\]__ A regra acima também é válida para o livro perfil “B”\.

__OS2328IB MFS46921__

__RN12__

__\[ALTERADA – OS2848\]__ Se durante a geração do livro perfil “A” o sistema verificar que o campo 2 \(NUM\_ORD\) do registro I012 não estiver preenchido, o mesmo deverá apresentar no Log a seguinte mensagem:

Tipo I012 – Registro não será gerado\. Favor informar o Número de ordem da geração\. \(Livro Auxiliar\) de escrituração\. 

Localização: SPED \-\-> ECD Escrituração Contábil Digital \-\-> Parâmetros \-\-> Controle da Obrigação na opção \[Livros Auxiliares\]

__OS2328IB__

__RN13__

Se durante a geração do livro perfil “A” o sistema verificar que o campo 3 \(NAT\_LIVR\) do registro I012 não estiver preenchido, o mesmo deverá apresentar no Log a seguinte mensagem:

Tipo I012 – Registro não será gerado\. Favor informar o Descritivo do Livro para o SPED\. \(Livro Auxiliar\) de escrituração\.

Localização: SPED \-\-> ECD Escrituração Contábil Digital \-\-> Parâmetros \-\-> Livros Auxiliares ao Diário

__OS2328IB__

__RN14__

Se durante a geração do livro perfil “A” o sistema verificar que o campo 4 \(TIPO\) do registro I012 não estiver preenchido, o mesmo deverá apresentar no Log a seguinte mensagem:

Tipo I012 – Registro não será gerado\. Favor informar Tipo de escrituração do Livro associado para o SPED\. \(Livro Auxiliar\) de escrituração\.

Localização: SPED \-\-> ECD Escrituração Contábil Digital \-\-> Parâmetros \-\-> Livros Auxiliares ao Diário

__OS2328IB__

__RN15__

Se durante a geração do livro perfil “R” o sistema verificar que o campo 2 \(COD\_CTA\_RES\) do registro I015 não estiver preenchido, o mesmo deverá apresentar no Log a seguinte mensagem:

“Tipo I015 – Registro não será gerado\. Favor informar o Código da conta analítica do Livro Diário com Escrituração Resumida \(Livro “R”\) que recebe os lançamentos globais\. Localização: Módulo SPED \-\-> ECD Escrituração Contábil Digital \-\-> Parâmetros \-\-> Livros Auxiliares ao Diário

__OS2328IB__

__RN16__

O relatório disponível no botão “![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAAUCAIAAADgN5EjAAAAAXNSR0IArs4c6QAAAAlwSFlzAAAOwQAADsUB3P2u6QAAAK5JREFUOE+tk1EOhCAMRLd7BhOvsPc/jVcw8Q5aMjgUWjBL7Bci0zctVI59+0zFd0qVROKZy/pDurGdlqmy8w6mCH295BZAEkSEa++8qtMqVTbOUtw2wKY2Fs/9uE4L1DUi3YQUj1npgTztacAWpk3M0z1gVhKoAttP/d0DVkyWzpYOgJXyL2BW6i2zSDTQfjYtLe+k96zxaOHcXsazEiegD7MHUxZOht+cn5V55QUNRIfgoQO1KAAAAABJRU5ErkJggg==)” da tela de “Livros Auxiliares ao diário” deverá ser atualizado com a retirada do campo __“Cód\. Hash do Arquivo correspondente ao Arquivo auxiliar”, na apresentação do relatório\.__

__OS2328IB__

__RN17__

Geração do livro “R” \(Registro I012 campo 03\) – Quando o campo 02 do registro I010 for igual a “R” \(somente se existirem livros auxiliares\), preencher com os dados dos livros auxiliares \(“A” ou “Z”\) coluna TERMO\_ABERTURA da tabela SPED\_TERMOS\_LIVRO\.

\[ALTERADA CH28131\_2012\]

Geração do livro “R” \(Registro I012 campo 03\) – Quando o campo 02 do registro I010 for igual a “R” ou “B" \(somente se existirem livros auxiliares\), preencher com os dados dos livros auxiliares \(“A” ou “Z”\) conforme parâmetro do campo Descritivo do Livro para o SPED\. Esta informação está disponível na tela “Livros Auxiliares ao Diário” \(Módulo ECD >> Parâmetros >> Livros Auxiliares ao Diário\)\.

__CH64346__

__CH28131\_2012__

__RN18__

__\[ALTERADA CH25719\_2016\]__

A guia “Livros Auxiliares ao Diário” será habilitada para o usuário, quando este selecionar no campo “Livro” da guia “Livros Principais” o Tipo “R \- Livro Diário com escrituração Resumida” ou “G – Livro Diário”\.

Quando selecionado o Tipo “G – Livro Diário”, na guia “Livros Auxiliares ao Diário” deverá ser apresentado no campo Tipo de Livro apenas o Tipo “Z – Razão Auxiliar \(Livro Contábil Auxiliar conforme Leiaute definido nos Registros I500 a I555\)”\.

__OS2328I\_2__

__CH25719\_2016__

__RN19__

Só deve ser considerado para a geração do Livro Auxiliar as informações das contas que estão parametrizadas na tela ‘Livros Auxiliares ao Diário’, localizada no módulo SPED / ECD – Escrituração Contábil Digital , menu: Parâmetros\.

__CH15368\_2012__

__RN20__

Na geração do arquivo da ECD para os Livros do Tipo A – Livro Diário Auxiliar e Tipo Z – Razão Auxiliar, gerar no campo 04 \- NAT\_LIVR do Registro I030 do livro gerado a informação parametrizada no campo Descritivo do Livro para o SPED do cadastro correspondente ao livro que está sendo gerado\. Esta informação está disponível na tela “Livros Auxiliares ao Diário” \(Módulo ECD >> Parâmetros >> Livros Auxiliares ao Diário\)\.

Para geração da ECD para os Livros do Tipo G – Diário Geral, Tipo R – Diário Resumido e Tipo B – Balancete Diário a informação para geração do campo 04 \- NAT\_LIVR do Registro I030 do livro gerado deve ser recuperada do campo Natureza do Livro referente ao Termo de Abertura, disponível na tela “Termo de Abertura/Encerramento” \(Módulo ECD >> Parâmetros >> Termo de Abertura/Encerramento\)\.

__CH14409\_2012__

__CH28131\_2012__

__RN21__

Na geração do arquivo da ECD para os Livros do Tipo A – Livro Diário Auxiliar e Tipo Z – Razão Auxiliar, gerar no campo 04 \- NAT\_LIVRO do Registro J900 do livro gerado a informação parametrizada no campo Descritivo do Livro para o SPED do cadastro correspondente ao livro que está sendo gerado\. Esta informação está disponível na tela “Livros Auxiliares ao Diário” \(Módulo ECD >> Parâmetros >> Livros Auxiliares ao Diário\)\.

Para geração da ECD para os Livros do Tipo G – Diário Geral, Tipo R – Diário Resumido e Tipo B – Balancete Diário a informação para geração do campo 04 \- NAT\_LIVRO do Registro J900 do livro gerado deve ser recuperada do campo Natureza do Livro referente ao Termo de Encerramento, disponível na tela “Termo de Abertura/Encerramento” \(Módulo ECD >> Parâmetros >> Termo de Abertura/Encerramento\)\.

__CH14409\_2012__

