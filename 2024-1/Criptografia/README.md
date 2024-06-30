# Criptografia

### O que é Criptografia?

A criptografia é o processo de converter informações ou dados em um código para impedir o acesso não autorizado. Seu objetivo principal é proteger a confidencialidade e a integridade dos dados enquanto eles estão em trânsito ou armazenados. A criptografia usa algoritmos matemáticos para transformar dados legíveis (texto claro) em um formato ilegível (texto cifrado) que só pode ser revertido para o formato original por quem possuir a chave de descriptografia adequada.

### Tipos de Criptografia

1. **Criptografia Simétrica**:
   - Usa a mesma chave para cifrar e decifrar os dados.
   - Exemplo: AES (Advanced Encryption Standard).

2. **Criptografia Assimétrica**:
   - Usa um par de chaves, uma chave pública para cifrar e uma chave privada para decifrar.
   - Exemplo: RSA (Rivest-Shamir-Adleman).

3. **Hashing**:
   - Transforma dados em um valor fixo (hash) que representa os dados originais.
   - Hashes são unidirecionais e não podem ser revertidos.
   - Exemplo: SHA-256 (Secure Hash Algorithm 256-bit).

### Ferramentas de Criptografia

#### 1. **OpenSSL**
- **Descrição**: Uma biblioteca robusta para criptografia que fornece uma ampla gama de funções de criptografia.
- **Instalação**:
  - Para Ubuntu/Debian:
    ```sh
    sudo apt update
    sudo apt install openssl
    ```
  - Para Fedora:
    ```sh
    sudo dnf install openssl
    ```

- **Uso Básico**:
  - Criptografar um arquivo:
    ```sh
    openssl enc -aes-256-cbc -salt -in arquivo.txt -out arquivo.txt.enc
    ```
  - Descriptografar um arquivo:
    ```sh
    openssl enc -d -aes-256-cbc -in arquivo.txt.enc -out arquivo.txt
    ```

#### 2. **GnuPG (GPG)**
- **Descrição**: Ferramenta para criptografia e assinatura digital de dados.
- **Instalação**:
  - Para Ubuntu/Debian:
    ```sh
    sudo apt update
    sudo apt install gnupg
    ```
  - Para Fedora:
    ```sh
    sudo dnf install gnupg
    ```

- **Uso Básico**:
  - Gerar um par de chaves:
    ```sh
    gpg --gen-key
    ```
  - Criptografar um arquivo:
    ```sh
    gpg -c arquivo.txt
    ```
  - Descriptografar um arquivo:
    ```sh
    gpg arquivo.txt.gpg
    ```

#### 3. **VeraCrypt**
- **Descrição**: Software de criptografia de disco completo, sucessor do TrueCrypt.
- **Instalação**:
  - Baixe o instalador para seu sistema operacional do site oficial e siga as instruções de instalação.

- **Uso Básico**:
  - Crie um volume criptografado e monte-o como um disco virtual onde você pode armazenar arquivos.

#### 4. **BitLocker**
- **Descrição**: Ferramenta de criptografia de disco completo integrada ao Windows.
- **Instalação**: Já está incluído nas edições Professional e Enterprise do Windows.
- **Uso Básico**:
  - Ativar o BitLocker:
    1. Vá para `Painel de Controle` > `Sistema e Segurança` > `Criptografia de Unidade de Disco BitLocker`.
    2. Selecione a unidade que deseja criptografar e clique em `Ativar BitLocker`.

#### 5. **HashiCorp Vault**
- **Descrição**: Ferramenta para gerenciar segredos e proteger dados confidenciais.
- **Instalação**:
  - Baixe e instale do site oficial ou use um gerenciador de pacotes como `apt` ou `brew`.

- **Uso Básico**:
  - Iniciar um servidor Vault:
    ```sh
    vault server -dev
    ```
  - Usar a CLI do Vault para armazenar e recuperar segredos:
    ```sh
    vault kv put secret/mysecret value=myvalue
    vault kv get secret/mysecret
    ```

### Como Utilizar Ferramentas de Criptografia

Aqui está um exemplo prático de uso do OpenSSL para criptografar e descriptografar um arquivo:

1. **Instalar o OpenSSL**:
   ```sh
   sudo apt update
   sudo apt install openssl
   ```

2. **Criptografar um Arquivo**:
   - Comando:
     ```sh
     openssl enc -aes-256-cbc -salt -in arquivo.txt -out arquivo.txt.enc
     ```
   - Isso usará o algoritmo AES-256-CBC para criptografar `arquivo.txt` e salvará o resultado em `arquivo.txt.enc`.

3. **Descriptografar um Arquivo**:
   - Comando:
     ```sh
     openssl enc -d -aes-256-cbc -in arquivo.txt.enc -out arquivo.txt
     ```
   - Isso descriptografará `arquivo.txt.enc` e salvará o resultado em `arquivo.txt`.

A escolha da ferramenta e o método de criptografia dependem do contexto e dos requisitos específicos, como o tipo de dados, a necessidade de segurança, a facilidade de uso e o ambiente de implementação.
