import pytest
from unittest.mock import MagicMock
from bedrock_analyzer import analisar_cv_com_bedrock
from botocore.exceptions import ClientError

# Exemplo de teste para o caminho de sucesso
def test_analisar_cv_com_bedrock_sucesso(mocker):
    """
    Testa se a função retorna a análise com sucesso quando a API da AWS funciona.
    """
    # Simula (mock) o cliente boto3 e sua resposta
    mock_bedrock_client = MagicMock()
    mock_response = {
        "output": {
            "message": {
                "content": [{"text": "Esta é uma análise de CV bem-sucedida."}]
            }
        }
    }
    mock_bedrock_client.converse.return_value = mock_response
    
    # Configura o mocker para usar nosso cliente simulado ao invés do real
    mocker.patch('boto3.client', return_value=mock_bedrock_client)

    # Chama a função com dados de teste
    resultado = analisar_cv_com_bedrock("texto do cv", "texto da vaga")

    # Verifica se a função retornou o texto esperado
    assert resultado == "Esta é uma análise de CV bem-sucedida."
    # Verifica se o método 'converse' foi chamado com os argumentos corretos
    mock_bedrock_client.converse.assert_called_once()

# Exemplo de teste para um caminho de erro (exceção da AWS)
def test_analisar_cv_com_bedrock_erro_cliente(mocker):
    """
    Testa se a função lida corretamente com uma exceção ClientError do boto3.
    """
    # Simula (mock) o cliente boto3 para lançar uma exceção
    mock_bedrock_client = MagicMock()
    error_response = {'Error': {'Code': 'AccessDeniedException', 'Message': 'Acesso negado'}}
    mock_bedrock_client.converse.side_effect = ClientError(error_response, 'Converse')
    
    # Configura o mocker
    mocker.patch('boto3.client', return_value=mock_bedrock_client)

    # Chama a função e espera um erro
    resultado = analisar_cv_com_bedrock("texto do cv", "texto da vaga")

    # Verifica se a mensagem de erro retornada é a esperada
    assert "Ocorreu um erro ao processar a sua solicitação" in resultado
    assert "Acesso negado" in resultado