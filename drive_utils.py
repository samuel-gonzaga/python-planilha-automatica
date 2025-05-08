import os
import io
import json
import tempfile
import pickle
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Lê JSON da variável .env
            credentials_json = os.getenv("GOOGLE_CREDENTIALS_JSON")
            if not credentials_json:
                raise Exception("Variável de ambiente GOOGLE_CREDENTIALS_JSON não encontrada.")

            # Converte string para dict e escreve em um arquivo temporário
            data = json.loads(credentials_json)
            with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".json") as temp:
                json.dump(data, temp)
                temp.flush()
                flow = InstalledAppFlow.from_client_secrets_file(temp.name, SCOPES)
                creds = flow.run_console()

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    return build('drive', 'v3', credentials=creds)

def baixar_arquivo_drive(file_id, nome_destino):
    service = authenticate()
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(nome_destino, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print(f"Baixando {nome_destino}: {int(status.progress() * 100)}%")


def enviar_para_drive(nome_arquivo, id_pasta):
    service = authenticate()
    file_metadata = {
        'name': nome_arquivo,
        'parents': [id_pasta]
    }
    media = MediaFileUpload(nome_arquivo, resumable=True)
    file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    print(f"Arquivo enviado! ID: {file.get('id')}")

def deletar_arquivo_local(caminho_arquivo):
    try:
        os.remove(caminho_arquivo)
        print(f"Arquivo local '{caminho_arquivo}' deletado com sucesso.")
    except FileNotFoundError:
        print(f"Arquivo '{caminho_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Erro ao deletar o arquivo '{caminho_arquivo}': {e}")