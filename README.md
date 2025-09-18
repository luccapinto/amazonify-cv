# Amazonify CV

## Sobre o Projeto
"Amazonify CV" é uma ferramenta de IA que otimiza currículos para vagas na Amazon. A aplicação analisa um currículo e uma descrição de vaga, fornecendo feedback detalhado com foco nos Princípios de Liderança da Amazon, e sugere melhorias concretas usando o método STAR.

## Screenshot da Aplicação
(Aqui você deve adicionar o screenshot da sua aplicação rodando)

## Arquitetura
A arquitetura da aplicação é serverless, focada em simplicidade e escalabilidade. O frontend é construído com Streamlit e o backend utiliza o poder do Amazon Bedrock para a análise de IA.

```mermaid
graph TD
    A[Usuário] --> B{Frontend: Streamlit};
    B --> C[Backend: AWS SDK (Boto3)];
    C --> D[Amazon Bedrock];
    D -- Responde com Análise de CV --> C;
    C -- Retorna Análise --> B;
    B -- Exibe Resultado --> A;

    subgraph "AWS Cloud"
        C
        D
    end
```

## Prompts Utilizados (Simulação)
Este projeto foi desenvolvido com o auxílio do Amazon Q Developer. Abaixo estão exemplos dos tipos de prompts que foram utilizados para gerar o código:

### Prompt 1: Geração da Estrutura Inicial do Streamlit
"Crie o esqueleto de uma aplicação web com Streamlit. A interface deve ter um título 'Analisador de CV com IA 🧠', uma breve descrição do que a aplicação faz, duas grandes áreas de texto (st.text_area), uma para 'Currículo' e outra para 'Vaga', e um botão 'Analisar'."

### Prompt 2: Lógica do Backend com Boto3
"Escreva uma função em Python chamada analisar_cv_com_bedrock que recebe dois argumentos: texto_cv e texto_vaga. Dentro dela, use o boto3 para criar um cliente do serviço 'bedrock-runtime' na região 'us-east-1'. A função deve invocar o modelo 'amazon.nova-micro-v1:0' usando a API converse."

### Prompt 3: Engenharia de Prompt para o "Bar Raiser"
"Preciso de um prompt detalhado para o Amazon Bedrock. O prompt deve instruir a IA a agir como um recrutador 'Bar Raiser' da Amazon. A tarefa é analisar um currículo em relação a uma vaga, focando nos Princípios de Liderança. A análise precisa: 1. Avaliar a aderência do CV à vaga (pontos fortes e fracos). 2. Conectar experiências do CV com os Princípios de Liderança. 3. Sugerir melhorias no CV usando o método STAR. 4. Formatar a saída em Markdown. O prompt deve incluir placeholders para o texto do currículo e da vaga."

### Prompt 4: Tratamento de Erros
"Adicione um bloco try/except na função analisar_cv_com_bedrock para capturar ClientError do botocore e exceções genéricas. Em caso de erro, a função deve imprimir o erro no console e retornar uma mensagem amigável para o usuário, como 'Ocorreu um erro ao processar a sua solicitação...'"

## Como Rodar
Para rodar a aplicação localmente, siga os seguintes passos:

1. **Configure suas credenciais AWS:**
   Certifique-se de que seu ambiente tenha credenciais da AWS configuradas com permissão para acessar o Amazon Bedrock.

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a aplicação:**
   ```bash
   streamlit run app.py
   ```

## Testes
O projeto inclui testes automatizados usando pytest. Para executar os testes:

```bash
pip install pytest pytest-mock
pytest test_bedrock_analyzer.py -v
```

## Segurança e VPC
Para maior segurança em produção, recomenda-se executar a aplicação dentro de uma VPC (Virtual Private Cloud) da AWS com um VPC Endpoint para o Amazon Bedrock. Isso garante que as chamadas de API não trafeguem pela internet pública.

### Como implementar:
1. Crie uma VPC para sua aplicação
2. Configure um VPC Endpoint para o serviço `com.amazonaws.<region>.bedrock-runtime`
3. Associe um Security Group que permita tráfego HTTPS (porta 443)
4. Execute sua aplicação dentro da VPC (ex: EC2, ECS, Lambda)

## Infrastructure as Code (IaC)
O projeto inclui código de infraestrutura usando AWS CDK para criar as permissões IAM necessárias. Veja o diretório `iac/` para mais detalhes.

## Estimativa de Custo
O custo principal do projeto está associado ao uso do Amazon Bedrock. A precificação é baseada na quantidade de tokens processados (tokens de entrada + tokens de saída).

O modelo utilizado (amazon.nova-micro-v1:0) é um dos modelos da Amazon e seus custos devem ser consultados na [página oficial de preços do Amazon Bedrock](https://aws.amazon.com/bedrock/pricing/).

### Exemplo de Custo Simulado:
- **Entrada (Input):** Um currículo e uma vaga somam, em média, 1500 tokens
- **Saída (Output):** Uma análise detalhada gera, em média, 1000 tokens
- **Total por Análise:** ~2500 tokens

Se o custo for de, por exemplo, $0.0008 por 1.000 tokens de entrada e $0.0016 por 1.000 tokens de saída, o custo por análise seria:
- (1.5 × $0.0008) + (1.0 × $0.0016) = $0.0012 + $0.0016 = **$0.0028**

Ou seja, o custo é extremamente baixo para uso casual, permitindo realizar centenas de análises por menos de um dólar. Para um caso de uso em produção, um orçamento detalhado e alarmes de custo na AWS são recomendados.
