# MTZ_GIA-RS_Manutencao_Observacoes

- **Fonte:** MTZ_GIA-RS_Manutencao_Observacoes.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 28 KB

---

GIA–RS – Manutenção das Observações

__Localização__: menu Estadual, módulo GIA RS, menu Obrigações 🡪 IN DRP45/98 – GIA 🡪 Manutenção 🡪 Observações

DOCUMENTO DE REQUISITO

__DR__

__Nome__

__Descrição__

OS3900

Manutenção das Observações

Criar menu para permitir a manutenção das observações da GIA\-RS

REGRAS DE NEGÓCIO

#### Cód\.

### Descrição

### DR

__RN00__

__Regras Gerais__

Este item de menu foi criado na OS3900, para permitir a manutenção das observações a serem gravadas na GIA\-RS \(tabela EST\_RS\_GIA\_REG\_OBS\)\. Estas observações também são geradas de forma automática na primeira etapa da geração dos dados da GIA\-RS, no menu “Obrigações 🡪 IN DRP45/98 – GIA 🡪 Geração 🡪 Anexos e Quadros E e A/C \(parcial\)”\.

A tabela permite uma única linha de observação  por período, assim, existirá apenas um registro de observação para cada período \(mês/ano\), ou seja, apenas um campo texto de 4000 caracteres\.

Opções da barra de menu:

Novo – Esta opção permite a inclusão de um novo registro;

Abre – Esta opção abre a janela de seleção dos dados da tabela das observações da GIA\-RS para o usuário selecionar o registro desejado;

Exclui – Exclui o registro selecionado pelo usuário

Confirma – Salva a operação realizada

Relatório – Abre uma janela de seleção para o usuário informar os parâmetros de emissão do relatório 

Fecha – fecha a janela

__RN01__

__Campo: Estabelecimento__

Quando o usuário selecionar um registro na opção Abre, o campo exibirá o estabelecimento do registro escolhido\. 

Para a inclusão de um novo registro, este campo exibirá o estabelecimento do login, quando for o caso, ou, a lista dos estabelecimentos da UF do RS para seleção do usuário, caso o usuário não tenha informado estabelecimento no login\.

__RN02__

__Campo: Mês/ Ano Apuração__

Quando o usuário selecionar um registro na opção Abre, o campo exibirá o Mês/Ano do registro escolhido\. 

Para a inclusão de um novo registro, o usuário informará o mês e ano\.

 

__RN03__

__Campo: Observações__

Quando o usuário selecionar um registro na opção Abre, este campo exibirá o conteúdo da observação do registro escolhido\. O conteúdo do campo será exibido em 50 linhas de 80 caracteres, e o usuário poderá alterar seu conteúdo, ou inserir novas informações\.

Na inclusão de um novo registro, o usuário informará a observação\.

__RN04__

__Campo: Nº Processo__

Quando o usuário selecionar um registro na opção Abre, este campo exibirá o número do processo do registro selecionado\. Só existirá um número de processo caso a observação tenha sido gerada de forma automática na rotina de geração dos dados da GIA\-RS\. 

Na inclusão de um novo registro, o campo ficará sem informação\.

\(este campo *não* é habilitado para manutenção do usuário\)

