# Segurança no Ambiente Web

A segurança do site requer vigilância em todos os aspectos do design e uso do site. Este artigo introdutório não fará de você um guru da segurança de sites, mas ajudará a entender de onde vem as ameaças e o que você pode fazer para proteger sua aplicação web contra os ataques mais comuns.

A Internet é um lugar perigoso! Com grande regularidade, ouvimos sobre a indisponibilidade de sites devido a ataques de negação de serviço ou a exibição de informações modificadas (e muitas vezes prejudiciais) em suas páginas iniciais. Em outros casos de alto perfil, milhões de senhas, endereços de email e detalhes de cartão de crédito foram vazados para o domínio público, expondo os usuários do site a vergonha pessoal e risco financeiro.

O objetivo da segurança do site é impedir esse (ou qualquer) tipo de ataque. A definição mais formal de segurança do site é o ato ou prática de proteger sites contra acesso, uso, modificação, destruição ou interrupção não autorizados.

A segurança efetiva do site requer um esforço de design em todo o site: em sua aplicação web, na configuração do servidor da web, em suas políticas para criar e renovar senhas e no código do cliente. Embora tudo isso pareça muito ameaçador, a boa notícia é que, se você estiver usando framework (uma estrutura da web) no servidor, é provável que ele habilitará "por padrão" mecanismos de defesa robustos e bem pensados contra vários ataques mais comuns. Outros ataques podem ser mitigados através da configuração do servidor da web, por exemplo, ativando o HTTPS. Por fim, existem ferramentas de scanner de vulnerabilidades disponíveis publicamente que podem ajudá-lo a descobrir se você cometeu algum erro óbvio.

O restante deste artigo fornece mais detalhes sobre algumas ameaças comuns e algumas das etapas simples que você pode executar para proteger seu site.

----

## [x] | Ameaças à segurança do site

| Ataque | Descrição |
| ---- | ---- |
| Cross-Site Scripting (XSS) | XSS é um termo usado para descrever uma classe de ataques que permitem que um invasor injete scripts do lado do cliente através do site nos navegadores de outros usuários. Como o código injetado chega ao navegador a partir do site, o código é confiável e pode fazer coisas como enviar o cookie de autorização do site do usuário ao invasor. Quando o invasor possui o cookie, ele pode fazer login em um site como se fosse o usuário e fazer tudo que o usário pode, como acessar os detalhes do cartão de crédito, ver detalhes do contato ou alterar senhas. |
| Injeção de SQL | As vulnerabilidades de injeção de SQL permitem que usuários mal-intencionados executem código SQL arbitrário em um banco de dados, permitindo que os dados sejam acessados, modificados ou excluídos, independentemente das permissões do usuário. Um ataque de injeção bem-sucedido pode falsificar identidades, criar novas identidades com direitos de administração, acessar todos os dados no servidor ou destruir/modificar os dados para torná-los inutilizáveis. |
| Cross-Site Request Forgery (CSRF) | Os ataques de CSRF permitem que um usuário mal-intencionado execute ações usando as credenciais de outro usuário sem o conhecimento ou consentimento desse usuário. |

### Cross-Site Scripting (XSS)

As vulnerabilidades do XSS são divididas em refletidas e persistentes, de acordo como o site retorna os scripts injetados para um navegador.

- Uma vulnerabilidade XSS refletida ocorre quando o conteúdo do usuário passado para o servidor é retornado imediatamente e não é modificado para exibição no navegador. Quaisquer scripts no conteúdo original do usuário serão executados quando a nova página for carregada. Por exemplo, considere uma função de pesquisa no site em que os termos de pesquisa são codificados como parâmetros de URL e esses termos são exibidos junto com os resultados. Um invasor pode construir um link de pesquisa que contenha um script malicioso como parâmetro (por exemplo, `https://developer.mozilla.org?q=beer<script%20src="http://example.com/tricky.js"></script>`) e enviar por e-mail para outro usuário. Se o usuário alvo clicar nesse "link interessante", o script será executado quando os resultados da pesquisa forem exibidos. Conforme discutido anteriormente, isso fornece ao invasor todas as informações necessárias para entrar no site como usuário alvo, potencialmente fazendo compras como o usuário ou compartilhando suas informações de contato.

- Uma vulnerabilidade persistente do XSS ocorre quando o script mal-intencionado é armazenado no site e posteriormente exibido novamente sem modificação para que outros usuários executem sem querer. Por exemplo, um quadro de discussão que aceita comentários que contêm HTML não modificado pode armazenar um script mal-intencionado de um invasor. Quando os comentários são exibidos, o script é executado e pode enviar ao invasor as informações necessárias para acessar a conta do usuário. Esse tipo de ataque é extremamente popular e poderoso, porque o invasor pode até não ter nenhum envolvimento direto com as vítimas.

Embora os dados das solicitações `POST` ou `GET` sejam a fonte mais comum de vulnerabilidades XSS, qualquer dado do navegador é potencialmente vulnerável, como dados de cookies renderizados pelo navegador ou arquivos de usuário que são carregados e exibidos.

A melhor defesa contra as vulnerabilidades do XSS é remover ou desativar qualquer marcação que possa conter instruções para executar o código. Para HTML, isso inclui elementos, como `<script>`, `<object>`, `<embed>` e `<link>`.

O processo de modificação de dados do usuário para que não possa ser usado para executar scripts ou afetar a execução do código do servidor é conhecido como limpeza de entrada. Muitas estruturas da Web limpam automaticamente a entrada do usuário de formulários HTML por padrão.

### Injeção de SQL

As vulnerabilidades de injeção de SQL permitem que usuários mal-intencionados executem código SQL arbitrário em um banco de dados, permitindo que os dados sejam acessados, modificados ou excluídos, independentemente das permissões do usuário. Um ataque de injeção bem-sucedido pode falsificar identidades, criar novas identidades com direitos de administração, acessar todos os dados no servidor ou destruir/modificar os dados para torná-los inutilizáveis.

Os tipos de injeção SQL incluem injeção SQL baseada em erro, injeção SQL baseada em erros booleanos e injeção SQL baseada em tempo.

Esta vulnerabilidade está presente se a entrada do usuário que é passada para uma instrução SQL subjacente puder alterar o significado da instrução. Por exemplo, o código a seguir tem como objetivo listar todos os usuários com um nome específico (nomeUsuario) fornecido a partir de um formulário HTML:

```sql
statement = "SELECT * FROM usuarios WHERE name = '" + nomeUsuario + "';"
```

Se o usuário especificar um nome real, a instrução funcionará como pretendido. No entanto, um usuário mal-intencionado pode alterar completamente o comportamento dessa instrução SQL para a nova instrução no exemplo a seguir, simplesmente especificando o texto em negrito para o nomeUsuario.

```sql
SELECT * FROM usuarios WHERE name = 'a'; DROP TABLE usuarios; SELECT * FROM userinfo WHERE 't' = 't';
```

A instrução modificada cria uma instrução SQL válida que exclui a tabela de usuarios e seleciona todos os dados da tabela `userinfo` (que revela as informações de cada usuário). Isso funciona porque a primeira parte do texto injetado ( `a';`) completa a declaração original.

Para evitar esse tipo de ataque, você deve garantir que os dados do usuário passados para uma consulta SQL não possam alterar a natureza da consulta. Uma maneira de fazer isso é utilizar 'escape' em todos os caracteres na entrada do usuário que tenham um significado especial no SQL.

> Nota: A instrução SQL trata o caractere ' como o início e o final de uma cadeia de caracteres literal. Ao colocar uma barra invertida na frente desse caractere (\'), "escapamos" do símbolo e dizemos ao SQL para tratá-lo como um caractere (apenas uma parte da string).

Na declaração a seguir, escapamos o caractere '. O SQL agora interpretará o nome como toda a string em negrito (que é um nome muito estranho, mas não prejudicial).

```sql
SELECT * FROM usarios WHERE name = 'a\';DROP TABLE usuarios; SELECT * FROM userinfo WHERE \'t\' = \'t';
```

Frameworks web geralmente cuidam do caractere que está escapando para você. O Django, por exemplo, garante que todos os dados do usuário passados para os conjuntos de consultas (consultas de modelo) sejam escapados.

### Croos-Site Request Forgery (CSRF)

Esse tipo de ataque é melhor explicado por exemplo. John é um usuário mal-intencionado que sabe que um site específico permite que usuários conectados enviem dinheiro para uma conta especificada usando uma solicitação HTTP `POST` que inclui o nome da conta e uma quantia em dinheiro. John cria um formulário que inclui seus dados bancários e uma quantia de dinheiro como campos ocultos e o envia por e-mail a outros usuários do site (com o botão Enviar, disfarçado como um link para um site "fique rico rapidamente").

Se um usuário clicar no botão enviar, uma solicitação HTTP `POST` será enviada ao servidor contendo os detalhes da transação e quaisquer cookies do lado do cliente que o navegador associou ao site (adicionar cookies do site associados a solicitações é um comportamento normal do navegador). O servidor irá verificar os cookies e usá-los para determinar se o usuário está ou não conectado e tem permissão para fazer a transação.

O resultado é que qualquer usuário que clicar no botão Enviar enquanto estiver conectado ao site de negociação fará a transação. John fica rico.