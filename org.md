# Observações
- testar outros possiveis bugs
- Colocar uma condicional para que o botão de editar só seja aberto caso existam notas na tabela (tabela.get)??



# Erros para resolver
- somente a  nota um está sendo salva em m1.notas quando o programa é fechado e apenas as notas 1 e 2 são mostrada na tabela quando o programa é reaberto


# Lógica
- O meu input.get() será armazenado diretamente no banco de dados (pois ficará salvo mesmo após o término da execucação do App), e o meu atributo m.notas recebrá o valor armazenado junto com a minha interface de tabela sempre que o aplicativo for executado
- As notas que ja deveriam estar na tabela quando o programa fosse fechado não estão sendo exibidas pois estão dentro da função submit