import os
from google import genai
from google.genai import types

# A função agora aceita 'data_input' como argumento
def generate_report(data_input: str):
    """
    Gera um relatório HTML de dados de lotes usando o modelo Gemini 2.5 Pro.

    Args:
        data_input (str): Os dados do lote (ex: JSON) a serem analisados.
    """
    
    # 1. Configuração do Cliente
    try:
        client = genai.Client(
            api_key="AIzaSyC721RQl0wu97unyST-qm_SExxkBOuMbnU",
        )
    except Exception as e:
        # Adicione tratamento de erro para chave da API
        print("Erro ao inicializar o cliente Gemini. Verifique a variável de ambiente GEMINI_API_KEY.")
        print(f"Detalhe: {e}")
        return

    model = "gemini-2.5-pro"

    # 2. Configuração do Conteúdo (Input Dinâmico)
    contents = [
        types.Content(
            role="user",
            parts=[
                # Usa o dado passado como argumento
                types.Part.from_text(text=data_input), 
            ],
        ),
    ]
    
    # 3. Configuração de Geração e Instrução de Sistema
    generate_content_config = types.GenerateContentConfig(
        thinking_config = types.ThinkingConfig(
            thinking_budget=-1,
        ),
        system_instruction=[
            types.Part.from_text(text="""voce vai ler dados de lotes e analisa-los, com base nos dados gere um relatorio com observações e conclusões, faça num formato html, e desconsidere a imagem do produto, apenas gere o html não cite mais nada, tire tambem o ```html```"""),
        ],
    )

    # 4. Geração do Conteúdo por Stream
    print("--- Gerando Relatório ---")
    response_text = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")
        response_text += chunk.text
    
    return response_text # Retorna o relatório completo

# Bloco principal para testar/rodar o script diretamente
if __name__ == "__main__":
    
    # Exemplo de dados (usando os dados do seu pedido anterior)
    DADOS_DO_LOTE = """
    {'batch': {'id': 1, 'cover': {'url': 'http://res.cloudinary.com/dphjceuwh/image/upload/v1757277655/njpb6abexqx3r3ud1br9.png', 'description': '', 'uploaded_on': '2025-09-07T20:40:56.362845Z'}, 'qtd': 12, 'kg': '500.00', 'price': '0.00', 'invoice': 102123, 'material': 'teste', 'composition': '80%', 'status': 'em estoque', 'supplier': {'id': 1, 'name': 'teste', 'cnpj': 'TESTE', 'address': {'id': 1, 'street': 'teste', 'cep': 'teste', 'number': 12, 'state': 1}}}, 'rolls': [{'production_order': 1, 'kg': '12.00', 'nonconformity': False, 'color': None, 'batch': {'id': 1, 'qtd': 12, 'kg': '500.00', 'price': '0.00', 'invoice': 102123, 'material': 'teste', 'composition': '80%', 'status': 'em estoque', 'cover': {'id': 1, 'attachment_key': 'f85997d0-44a4-4ca7-a25a-6c788c258968', 'public_id': '67bd1421-41ac-4529-b60f-e59573a72838', 'file': 'image/upload/v1757277655/njpb6abexqx3r3ud1br9.png', 'description': '', 'uploaded_on': '2025-09-07T20:40:56.362845Z'}, 'supplier': {'id': 1, 'name': 'teste', 'cnpj': 'TESTE', 'address': 1}}}, {'production_order': 2, 'kg': '12.00', 'nonconformity': False, 'color': None, 'batch': {'id': 1, 'qtd': 12, 'kg': '500.00', 'price': '0.00', 'invoice': 102123, 'material': 'teste', 'composition': '80%', 'status': 'em estoque', 'cover': {'id': 1, 'attachment_key': 'f85997d0-44a4-4ca7-a25a-6c788c258968', 'public_id': '67bd1421-41ac-4529-b60f-e59573a72838', 'file': 'image/upload/v1757277655/njpb6abexqx3r3ud1br9.png', 'description': '', 'uploaded_on': '2025-09-07T20:40:56.362845Z'}, 'supplier': {'id': 1, 'name': 'teste', 'cnpj': 'TESTE', 'address': 1}}}, {'production_order': 3, 'kg': '10.00', 'nonconformity': False, 'color': None, 'batch': {'id': 1, 'qtd': 12, 'kg': '500.00', 'price': '0.00', 'invoice': 102123, 'material': 'teste', 'composition': '80%', 'status': 'em estoque', 'cover': {'id': 1, 'attachment_key': 'f85997d0-44a4-4ca7-a25a-6c788c258968', 'public_id': '67bd1421-41ac-4529-b60f-e59573a72838', 'file': 'image/upload/v1757277655/njpb6abexqx3r3ud1br9.png', 'description': '', 'uploaded_on': '2025-09-07T20:40:56.362845Z'}, 'supplier': {'id': 1, 'name': 'teste', 'cnpj': 'TESTE', 'address': 1}}}]}
    """
    generate_report(DADOS_DO_LOTE)