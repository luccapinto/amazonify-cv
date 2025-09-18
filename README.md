# Amazonify CV - Seu Currículo Turbinado para Vagas na Amazon

## Sobre o Projeto
O Amazonify CV é uma ferramenta de IA que ajuda candidatos a otimizar seus currículos especificamente para vagas na Amazon. A aplicação analisa o currículo do usuário e a descrição da vaga, fornecendo feedback acionável com base nos 16 Princípios de Liderança da Amazon e no método de entrevista STAR.

## Como Rodar
1.  **Clone o repositório e instale as dependências:**
    ```bash
    git clone [URL_DO_SEU_REPOSITORIO]
    cd amazonify-cv
    pip install -r requirements.txt
    ```
2.  **Configure suas credenciais da AWS:**
    Certifique-se de que seu ambiente tenha as credenciais da AWS configuradas para que o Boto3 possa acessar o serviço Amazon Bedrock.

3.  **Execute a aplicação:**
    ```bash
    streamlit run app.py
    ```

## Estimativa de Custo na AWS
O custo operacional deste projeto está associado ao uso do Amazon Bedrock. A cobrança é baseada na quantidade de tokens de entrada (currículo + vaga + prompt) e de saída (análise gerada). Para uso individual e esporádico, o custo é insignificante, geralmente na casa dos centavos de dólar por análise.
```"
---

#### **INTERAÇÃO 2: A Especialista em IA (Engenheira de Prompt)**

**Objetivo:** Esta especialista é o coração do projeto. Ela vai criar o "cérebro" da aplicação, a lógica que se conecta à AWS e contém o conhecimento de como analisar um currículo como um recrutador da Amazon.

**Seu Comando para a IA (Copie e Cole):**

"Atue como uma Engenheira de Prompt e Especialista em Modelos de Linguagem, com foco em AWS Bedrock. Sua única tarefa é criar o arquivo `bedrock_analyzer.py`, que conterá toda a lógica de análise de IA.

O arquivo deve conter uma única função, `analisar_cv_com_bedrock`, com o seguinte código:
```python
import boto3
import json

# Configura o cliente do Bedrock
# Certifique-se de que suas credenciais AWS e região estão configuradas no ambiente
bedrock_client = boto3.client(service_name='bedrock-runtime')

def analisar_cv_com_bedrock(texto_cv: str, texto_vaga: str) -> str:
    """
    Analisa um currículo contra uma vaga usando o Amazon Bedrock (Claude 3 Sonnet).
    """
    prompt = f\"\"\"
Você é um recrutador sênior da Amazon e um 'Bar Raiser', especialista em identificar talentos que se alinham com os 16 Princípios de Liderança da Amazon. Sua tarefa é analisar o currículo fornecido e adaptá-lo para a vaga de emprego da Amazon descrita, fornecendo um feedback construtivo e detalhado.

**Descrição da Vaga Amazon:**
<vaga>
{texto_vaga}
</vaga>

**Currículo Original:**
<cv>
{texto_cv}
</cv>

Analise os dois textos e retorne sua avaliação estritamente no seguinte formato Markdown:

**Análise de Afinidade com os Princípios de Liderança:**
- **Customer Obsession:** (Avalie como as experiências do CV demonstram foco no cliente e sugira melhorias).
- **Ownership:** (Identifique exemplos de responsabilidade e iniciativa e sugira como destacá-los).
- **Invent and Simplify:** (Encontre exemplos de inovação ou simplificação e sugira como evidenciá-los).
- **Are Right, A Lot:** (Avalie se as experiências demonstram bom julgamento e tomada de decisão baseada em dados).

**Sugestões de Melhoria (Método STAR):**
- **Reformule esta experiência:** (Pegue uma frase-chave do currículo e a reescreva usando o método STAR: Situação, Tarefa, Ação, Resultado).
- **Adicione métricas:** (Identifique um ponto no currículo onde um resultado quantificável, como 'aumentou a eficiência em 25%', poderia ser adicionado para demonstrar impacto).

**Resumo Final:**
(Um parágrafo motivacional encorajando o candidato e resumindo as principais mudanças).
\"\"\"

    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 4096,
        "messages": [
            {
                "role": "user",
                "content": [{"type": "text", "text": prompt}],
            }
        ],
    })

    try:
        response = bedrock_client.invoke_model(
            modelId="anthropic.claude-3-sonnet-20240229-v1:0",
            body=body
        )
        response_body = json.loads(response.get("body").read())
        return response_body.get("content")[0].get("text")
    except Exception as e:
        return f"Erro ao processar a análise: {e}"

```"
---

#### **INTERAÇÃO 3: O Desenvolvedor Full-Stack (Especialista em Interface)**

**Objetivo:** Este especialista vai montar a aplicação, criando a interface com o usuário e conectando-a ao cérebro de IA que foi desenvolvido na interação anterior.

**Seu Comando para a IA (Copie e Cole):**

"Atue como um Desenvolvedor Python Full-Stack, especialista em criar aplicações web interativas com Streamlit. Sua missão é criar o arquivo `app.py`, que será o ponto de entrada da aplicação 'Amazonify CV'.

O código deve importar os componentes necessários, criar a interface do usuário e orquestrar a chamada para a função de análise. O conteúdo do arquivo `app.py` deve ser:

```python
import streamlit as st
from bedrock_analyzer import analisar_cv_com_bedrock

# --- Configuração da Página ---
st.set_page_config(
    page_title="Amazonify CV",
    page_icon="🤖",
    layout="wide"
)

# --- Título e Descrição ---
st.title("🤖 Amazonify CV")
st.markdown("Cole seu currículo e a descrição da vaga da Amazon abaixo para receber uma análise de IA focada nos Princípios de Liderança.")

# --- Layout da Interface ---
col1, col2 = st.columns(2)

with col1:
    texto_cv = st.text_area("Cole aqui o seu currículo completo:", height=400, placeholder="Ex: João da Silva...")

with col2:
    texto_vaga = st.text_area("Cole aqui a descrição da vaga da Amazon:", height=400, placeholder="Ex: A Amazon Web Services (AWS) está procurando um Arquiteto de Soluções...")

# --- Botão e Lógica de Ação ---
if st.button("✨ Amazonificar meu Currículo!", use_container_width=True):
    if texto_cv and texto_vaga:
        with st.spinner("Analisando seu currículo com a IA... Isso pode levar um momento."):
            resultado_analise = analisar_cv_com_bedrock(texto_cv, texto_vaga)
            st.divider()
            st.subheader("Análise e Sugestões da IA:")
            st.markdown(resultado_analise)
    else:
        st.error("Por favor, preencha ambos os campos para prosseguir com a análise.")

```"

---

### **Pós-Interações**

Após essas três interações, sua IA especialista terá criado os três arquivos essenciais: `requirements.txt`, `bedrock_analyzer.py` e `app.py`, além do `README.md`. Seu trabalho será apenas executar os comandos do "Como Rodar" para ver seu projeto ganhar vida.
