# MTZ-Upload_Registros_M210_M610

> Fonte: MTZ-Upload_Registros_M210_M610.docx



Upload – Ajustes do Crédito de PIS/PASEP e COFINS – Registros M210/M610
(EFD- Escrituração Fiscal Digital das Contribuições)


DOCUMENTO DE REQUISITO


### REGRAS DE NEGÓCIO





| DR | Nome | Descrição | Data Alteração |
| --- | --- | --- | --- |
| OS3619 | Ajustes do crédito de PIS/PASEP e COFINS (Registros M210/M610) | Será criada a funcionalidade Upload para carregar as informações dos ajustes do crédito de PIS/PASEP e COFINS (Registros M210/M610) | 25/05/2012 |


| Cód. |  | DR |
| --- | --- | --- |
|  | REGISTRO PAI – M210/M610 |  |
| RN01 | Campo 01 - COD_REG Item: 01 Nome do Campo: A ser definido pelo A&D Descrição: Código do registro Tipo: A Tamanho: 010 Comentário: Campo destinado ao código do registro Valores Válidos: M210 M610 Chave Primária Obrigatório | OS3619 |
| RN02 | Campo 02 - COD_CONTRIB Item: 02 Nome do Campo: A ser definido pelo A&D Descrição: Código da contribuição social apurada no período, conforme a Tabela 4.3.5. Tipo: A Tamanho: 002 Comentário: Código da contribuição social apurada no período, conforme a Tabela 4.3.5. Valores válidos:    Chave Primária Obrigatório | OS3619 |
| RN03 | Campo 03 - VLR_ALIQ_PERC Item: 04 Nome do Campo: A ser definido pelo A&D Descrição: Alíquota (em percentual) Tipo: N Tamanho: 008 Sendo 4 inteiras e 4 decimais Comentário: Campo destinado a Alíquota (em percentual) Chave Primária Obrigatório |  |
| RN04 | Campo 04 - VLR_ALIQ_R Item: 04 Nome do Campo: A ser definido pelo A&D Descrição: Alíquota (em reais) Tipo: N Tamanho: 019 Sendo 15 inteiras e 4 decimais Comentário: Campo destinado a Alíquota (em reais) Chave Primária Obrigatório | OS3619 |
| RN05 | Validações  1 . Valores Válidos do campo COD_REG: M210, M610 2. Valores válidos do campo COD_CONTRIB:   3. Se o campo Vlr_Aliq_Perc estiver preenchido o campo Vlr_Aliq_R  não deve possuir informação. Neste caso exibir a seguinte msg ao usuário: Se o campo Vlr_Aliq_Perc estiver preenchido o campo Vlr_Aliq_R nao deve estar preenchido. 4. Se o campo Vlr_Aliq_R estiver preenchido o campo Vlr_Aliq_Perc não deve possuir informação. Neste caso exibir a seguinte msg ao usuário: Se o campo Vlr_Aliq_R estiver preenchido o campo Vlr_Aliq_Perc nao deve estar preenchido. 5.  Se o registro pai (M210), informado no arquivo lido, não existir na base, exibir a seguinte msg no log do processo: Nao foi encontrado registro pai com as seguintes informações chave (Cod_Contrib/Vlr_Aliq_Perc/Vlr_Aliq_R): 6.  Se o registro pai não for encontrado na base (conforme citado no item 2), automaticamente os seus filhos serão desconsiderados. 7.  Se algum dos campos obrigatórios (Registro Pai:Campo 01 - COD_REG, Campo 02 - COD_CONTRIB, Campo 03 – Vlr_Aliq_Perc  ou Campo 04 - Vlr_Aliq_R. não for enviado, exibir a seguinte msg no log do processo: O Campo <nome_campo_no_layout> e obrigatorio. |  |
|  | 8. Se  qualquer campo ultrapassar o tamanho definido no layout, só serão importada as primeiras posições até chegar ao tamanho definido no layout. 9 . Se o campo código da contribuição  não possuir um valor válido: Codigo de Contribuicao enviado nao esta de acordo com o Manual de Layout. Valor Informado:XXXX 10. Se o registro pai não pertence à funcionalidade chamadora(PIS/COFINS) ou filhos não pertencem ao pai respectivo, exibir a seguinte msg: Atencao o registro filho <valor_nivel2> nao pertence ao registro pai <valor_nivel1> ou nao pertence ao conjunto de informacoes do <funcionalidade chamadora>. O registro sera desconsiderado. |  |
