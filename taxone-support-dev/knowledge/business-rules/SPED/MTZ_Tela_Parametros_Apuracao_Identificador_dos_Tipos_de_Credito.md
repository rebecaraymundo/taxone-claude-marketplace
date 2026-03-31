# MTZ_Tela_Parâmetros_Apuracao_Identificador_dos_Tipos_de_Credito

> Fonte: MTZ_Tela_Parâmetros_Apuracao_Identificador_dos_Tipos_de_Credito.docx



## Tela - Identificador dos Tipos de Créditos (EFD-PIS/PASEP – COFINS)



DOCUMENTO DE REQUISITO


### REGRAS DE NEGÓCIO






| DR | Nome | Descrição | Data Alteração |
| --- | --- | --- | --- |
| CH6590_2012 | Criação do Documento | Permitir a manutenção dos registros, mesmo quando a data Validade Final estiver preenchida. | 13/03/2012 |


| Cód. |  | DR |
| --- | --- | --- |
| RN00 | Regras gerais  Nessa tela, o usuário poderá modificar todos os campos, porém o sistema deverá verificar se existe registro com os mesmos campos chaves parametrizado nesta tela.    Caso exista, o sistema deve verificar se o registro apresenta a Validade Final preenchida. Se estiver preenchida, verificar se o novo registro não está intercalando a Validade inicial com a do registro anterior. | OS3169-DW12 |
| RN01 | O campo Código Tipo Crédito será alimentado pela TFIX93. | OS3169-DW12 |
| RN02 | O campo CST PIS/COFINS será alimentados pela TACES65. | OS3169-DW12 |
| RN03 | Os registros que estiverem com o campo Validade Final preenchido, não deve permitir alteração. Obs. Caso haja necessidade de manutenção em um registro, cujo campo Validade Final esteja preenchido, deve ser incluído um novo registro com a data de validade Inicial posterior a Data de Validade Final.   Permitir que o usuário efetue manutenção nos registros. Antes da gravação da alteração, exibir a seguinte msg ao usuário: Esta alteração poderá impactar nos registros que já foram gerados. Neste caso, é recomendável avaliar se o período deverá ser reprocessado.. Deseja Continuar? Se sim, grava as alterações. Se não, os dados serão mantidos. | OS3169-DW12/ CH6590_2012 |
| RN04 | No momento da gravação de um registro, o sistema deve fazer as verificações abaixo, exibindo ao usuário o motivo de NÃO ter gravado a informação na base:  1 – Tentar inserir na base um registro com os mesmos parâmetros preenchidos,  válidos para o mesmo período. Neste caso, a gravação do novo registro não deve ser efetuada, exibindo a seguinte msg ao usuário: "Registro já existe na base de dados".  2 – Tentar inserir na base um registro com uma data entre um período fechado. Neste caso, a gravação do novo registro não deve ser efetuada, exibindo a seguinte msg ao usuário: "Registro não pode compreender a faixa de registro já fechado".  3 – Tentar inserir um registro com data inicial inferior ao registro gravado e com uma data final superior a data inicial (considerando sempre os mesmos dados cadastrados). Neste caso, a gravação do novo registro não deve ser efetuada, exibindo a seguinte msg ao usuário: "A data final do registro deve ser inferior a DD/MM/AAAA, pois já existe um registro com esta data inicial" | CH6590_2012 |
