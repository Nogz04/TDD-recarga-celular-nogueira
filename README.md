# Repositório tarefa TDD - Recarga de celular

## Oque é o venv (ambiente virtual) e para que ele serve no Python?

> O venv é uma ferramenta do Python usada para criar ambientes virtuais isolados.
>
> Sua principal função é o isolamento. O venv cria uma pasta chamada ```venv``` dentro da raiz do projeto, no venv irá conter uma cópia do executável do Python e um local específico para as bibliotecas.

---

## Vantagens e o que o venv nos proporciona?

### 1 - Evitar conflitos

> Com o venv, você consegue evitar conflitos entre versões, assim cada projeto pode ter suas próprias dependências e bibliotécas, sem interferir no sistema operacional ou em outros projetos.
>
> - Ex: Projeto Estoque usa Django 3.2, enquanto o Projeto RH usa Django 4.2. Com o ```venv```, cada um fica na sua bolha.

### 2 - Facilidade para o time (requirements.txt)

> Quando usamos um ambiente virtual (venv), conseguimos gerar uma lista exata do que o seu projeto precisa rodar.
>
>
> Para isso, você roda esse comando abaixo

```python
pip freeze > requirements.txt
```

> Assim, o colega que está em outra branch, só precisa rodar o comando abaixo dentro do venv dele para ter o ambiente idêntico ao seu.

```python
pip install -r requirements.txt
```

### 3 - Permissões de administrador

Ao usar um ```venv```, você não precisa de permissão de administrador (```sudo``` ou "Executar como admin") para instalar bibliotecas com o ```pip```, pois elas são instaladas apenas na pasta do seu projeto.

### Comandos do venv

Na pasta raiz do seu projeto, execute o comando abaixo para criar a pasta do ```.venv```

```python
python -m venv .venv
```

Agora, precisamos ativar esse ambiente virtual (venv)

- Windows:
  
```python
.\venv\Scripts\activate
```

- Linux/Mac:

```python
source .venv/bin/activate
```

Pronto. Após isso o usuário estará dentro do ambiente virtual (irá aparecer (venv) no inicio da linha do terminal). Agora é só instalar o django, dependencias, etc...

---

## O que é TDD (Test-Driven Development ou Desenvolvimento Guiado por Testes) e quando e como utilizá-lo?


### 1. O Conceito e o Mantra
> O **TDD** é uma técnica de design de software que inverte a lógica tradicional de desenvolvimento. Em vez de escrever o código e depois testar, você define o comportamento esperado através de um teste e só então escreve o código para satisfazê-lo. O processo é regido pelo ciclo **Red-Green-Refactor**:


> * 🔴 **RED (Vermelho):** Escreve-se um teste para uma funcionalidade que ainda não existe. Ao ser executado, o teste **falha** obrigatoriamente.
> * 🟢 **GREEN (Verde):** Escreve-se o **mínimo de código necessário** apenas para que o teste passe. O foco aqui é a funcionalidade, não a perfeição técnica.
> * 🔵 **REFACTOR (Refatorar):** Com a segurança do teste "verde", o código é limpo, as duplicações são removidas e a arquitetura é melhorada sem o risco de quebrar o comportamento já validado.

---

### 2. Por que utilizar?
> Implementar TDD, especialmente em sistemas complexos ou legados, traz benefícios estruturais ao projeto:

> * **Design de Código Superior:** Como o foco está no teste, o código nasce naturalmente modular, desacoplado e fácil de utilizar.
> * **Documentação Viva:** Os testes funcionam como uma especificação técnica sempre atualizada. Ler os testes é a melhor forma de entender as regras de negócio.
> * **Rede de Segurança:** Proporciona total confiança para realizar alterações em partes críticas do sistema, garantindo que novas funcionalidades não causem regressões.
> * **Foco na Entrega:** Evita o desperdício de tempo com implementações complexas que não foram solicitadas (segue o princípio YAGNI - *You Ain't Gonna Need It*).

---

### 3. Quando utilizar?
> Embora seja uma prática poderosa, o TDD deve ser aplicado de forma estratégica:

> **Utilize quando:**
> * A **Lógica de Negócio** for complexa (como cálculos de bônus, regras de operadoras ou diagnósticos médicos).
> * O sistema for de **Longo Prazo** e for mantido por uma equipa ao longo do tempo.
> * Estiver a corrigir um **Bug**: escrever o teste que reproduz o erro garante que ele nunca mais volte a ocorrer.
> * Estiver a criar **APIs ou Contratos**: onde a precisão da entrada e saída de dados é fundamental.

> **Pode ser evitado quando:**
> * For um **Protótipo (PoC)** rápido que será descartado após a validação da ideia.
> * Forem apenas **Ajustes Visuais** de interface (UI/UX) que dependem de percepção estética.
> * O código for um **CRUD trivial** (apenas operações de base de dados) sem qualquer regra de transformação ou lógica associada.
