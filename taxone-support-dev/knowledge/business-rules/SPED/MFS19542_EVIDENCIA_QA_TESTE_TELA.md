# MFS19542_EVIDENCIA_QA_TESTE_TELA

> Fonte: MFS19542_EVIDENCIA_QA_TESTE_TELA.docx


Tela Bloco W




- O campo moeda está com o label errado Tax Identification Number (TIN) da Entidade Substituta – W100



- Ao selecionar o campo Moeda – W100



- Erro não tratado ao salvar o registro W100




- Campo 7 e 8 não estão respeitando as regras de desabilitar e calcular (w200)





- No registro w300, ao clicar no campo de jurisdição tributária



- Ao apagar um registro W100 que possui filhos, não estamos exibindo a mensagem (de exclusão de filhos) e inclusive os filhos permanecem sem o pai



- Ajustar o label para Entidade Substituta/Entidade Local



8 . Label com erro de digitação



9 . Não existe este campo na tela



10. não está sendo possível excluir registros w100. Não ocorre nenhuma msg de erro.



Ao confirmar (OK)



Ao consultar novamente o w100, o registro permanece na base.

11. Está abrindo o modal do registro w250, mesmo não existindo na base o w200.



O mesmo não acontece para o w200 se o w100 não for cadastrado.

12. não está sendo possível excluir registros w200. Não ocorre nenhuma msg de erro.


13. O campo modalidade  e idioma não é de preenchimento obrigatório e não está dando a possibilidade de alterar o campo, deixando-os sem preenchimento.





- 14. Registro W300 deixar os campos de lista para default não na tela. A tela está permitindo gravar o registro com o campo em branco.

15.A validação do campo 11 tin_substituta (no registro w100), no cenário abaixo não está sendo feita, pois a tela só aceita 13 posições:
-Se o campo 10 (Jurisdição de Residência da Entidade Substituta), estiver preenchido com 'BR', validar se a informação do campo 11 (Tax Identification Number (TIN) da Entidade Substituta ) é um CNPJ válido.



- ACEITE:

- 1.



- 2.




- 3.


- 4.



- 5.



- 6.






- 7.


- 8.


- 9.



- 10.








- 11.


- 12.








- 13.


- 14.

- 15.

| Data | MFS | Descrição | Autor |
| --- | --- | --- | --- |
| 17/07/2018 | MFS-19542 | Criação do documento | Alessandra Cristina Navatta |
