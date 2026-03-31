# MTZ-Manutencao_do_registro_67_da_DAC_AL

- **Fonte:** MTZ-Manutencao_do_registro_67_da_DAC_AL.docx
- **Modificado:** 2020-03-11
- **Tamanho:** 28 KB

---

__DAC\-AL – Manutenção Registro 67 – Dados de Consumo de Energia__

__Módulo:__ Estadual → DAC\-AL

__Menu: __Manutenção → Registros 65, 66, 67 e 68

__DOCUMENTO DE REQUISITO__

__DR__

__Nome__

__Descrição__

OS3480

Inclusão do Registro 67 – Dados de Consumo de Energia

Inclusão do Registro 67 – Dados de Consumo de Energia

__REGRAS DE NEGÓCIO__

__Cód\.__

__Descrição__

__DR__

__RN00__

__Regras Gerais__

Cada linha que é apresentada no arquivo é um registro da nova tabela\. 

Quando tiver a necessidade de exclusão de registro que não foi recuperado do banco, ou seja, linha nova, emitir a mensagem: "Não há registros recuperados para serem excluidos\."

Deverá emitir o Relatório de Conferência dos campos do registro\.

OS3480

__RN01__

__Campo Estabelecimento:__

Utilizar para o critério de busca o estabelecimento que o usuário escolheu\.  Trará o estabelecimento que o usuário está logado\. Se o usuário não estiver logado em nenhum, trará a lista de estabelecimentos de Alagoas\.

Campo obrigatório\.

Campo chave\.

Este campo não deverá estar bloqueado\.

OS3480

__RN02__

__Campo Ano:__

Utilizar para o critério de busca a data inicial e final que o usuário preencheu\. Trazer no formato AAAA\.

Campo obrigatório\.

Campo chave\.

Este campo não deverá estar bloqueado\.

OS3480

__RN03__

__Campo Número do Medidor__

Trazer fixo o conteúdo gerado através da RN71 do documento matriz “MTZ \- DAC\_AL\_ANUAL\.doc”\.

Este campo deverá estar habilitado para digitação\. Se for digitado algum conteúdo, considerar este na geração do arquivo\.

OS3480

__RN04__

__Campo Consumo__

Trazer fixo o conteúdo gerado através da RN72 do documento matriz “MTZ \- DAC\_AL\_ANUAL\.doc”\.

Este campo deverá estar habilitado para digitação\. Se for digitado algum conteúdo, considerar este na geração do arquivo\.

OS3480

  


