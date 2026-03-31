# MTZ-Tela_Impressao_do_Livro_Auxiliar

- **Fonte:** MTZ-Tela_Impressao_do_Livro_Auxiliar.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 32 KB

---

##### DOCUMENTO DE REQUISITO

###### DR

###### Nome

__Descrição__

OS3853

<a id="OLE_LINK1"></a><a id="OLE_LINK2"></a>ECD– Tela ‘Impressão do Livro Auxiliar’\.

Inclusão do campo Livro \(Cód\./Desc\.\)\.

MFS\-2926

ECD – Tela ‘Impressão do Livro Auxiliar’

Atualização da regra do campo Livro \(Cód\./Desc\.\)\.

## REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

Inclusão do campo Livro \(Cód\./Desc\.\), logo abaixo do campo Estabelecimento, na tela “Impressão do Livro Auxiliar”, localizada no Módulo: SPED / ECD – Escrituração Contábil Digital, Menu: Parâmetros\.

OS3853

__RN01__

O novo campo Livro \(Cód\./Desc\.\) deve compor a chave da tabela que armazena o layout do Livro Razão Auxiliar, de modo a permitir que o usuário tenha layouts diferentes para cada livro\.

Na implementação da OS3853, como se trata de inclusão de um campo chave e que tem relacionamento com outra tabela, assumir o primeiro código de livro encontrado da tela “Livros Auxiliares ao Diário”, localizada no Módulo: SPED >> ECD – Escrituração Contábil Digital / Menu: Parâmetros, cujo tipo de livro esteja preenchido com a opção “Z – Razão Auxiliar \(Livro Contábil Auxiliar conforme leiaute definido nos registros I500 a I555\)”\.

OS3853

__RN02__

O campo Livro \(Cód\./Desc\.\) será recuperado da Tela “Livros Auxiliares ao Diário”, localizada no Módulo: SPED >> ECD – Escrituração Contábil Digital / Menu: Parâmetros\.

Recuperação dos Dados:

Apenas os registros, cujo tipo de livro esteja preenchido com a opção “Z – Razão Auxiliar \(Livro Contábil Auxiliar conforme leiaute definido nos registros I500 a I555\)” __E__ que __não tenha__ sido parametrizado na tela “Critérios de Consolidação – Razão Auxiliar das Subcontas” \(Módulo: SPED >> ECD – Escrituração Contábil Digital / Menu: Parâmetros\), devem ficar disponíveis para seleção\.

OS3853

MFS\-2926

__RN03__

Incluir o ícone Abrir na barra de ação\.

OS3853

__RN04__

Ícone Excluir, na barra de ação

A exclusão do layout só será permitida se o layout não estiver vinculado a nenhum processo de importação do arquivo do Livro Razão\. Caso esteja vinculado a um processo, emitir a seguinte msg ao usuário: ‘O layout ‘XXX’, não será excluído, pois está vinculado em importações do Livro Razão’\.

OS3853

__RN05__

No relatório da tela, incluir o campo Livro \(Cód\./Desc\.\), logo abaixo do campo Estabelecimento\.

OS3853

__RN06__

Botão Incluir Detalhe e Excluir Detalhe

Deverão ser incluídos dois novos botões para incluir e excluir detalhes do lado direito da caixa de definição de layout\. Eles impactarão diretamente na definição do layout, incluindo ou excluindo linhas para que o usuário defina a estrutura do livro auxiliar\.

OS3853

__RN07__

Alteração dos dados da tela

A partir do momento que um livro associado a um layout for importado através da tela “Livro Razão Auxiliar” \(Módulo: SPED >> ECD – Escrituração Contábil Digital / Menu: Manutenção\) todos os campos desta tela devem ser bloqueados para edição\.

OS3853

__RN08__

Opção de “Replicar para os Estabelecimentos”

Serão demonstrados os estabelecimentos Centralizadores, conforme parametrização realizada no módulo Parâmetros / Menu: Preliminares >> Centralização da Escrituração de Obrigações Federais e os Descentralizados \(os que não foram associados a nenhuma centralização\)\.

Não deve ser demonstrado na relação de estabelecimentos que podem receber a replicação os estabelecimentos que tenham o mesmo código de livro que será replicado e que já tenha importações de arquivo vinculadas\.

OS3853

