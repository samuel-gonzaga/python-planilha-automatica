import os
import io
import json
import tempfile
from dotenv import load_dotenv
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload

load_dotenv()

SCOPES = ['https://www.googleapis.com/auth/drive']

def authenticate():
    credentials_json = os.getenv("GOOGLE_CREDENTIALS_JSON")
    if not credentials_json:
        raise Exception("Variável de ambiente GOOGLE_CREDENTIALS_JSON não encontrada.")

    data = json.loads(credentials_json)
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".json") as temp:
        json.dump(data, temp)
        temp.flush()
        creds = service_account.Credentials.from_service_account_file(temp.name, scopes=SCOPES)
    os.remove(temp.name)
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


def enviar_para_drive(nome_arquivo, id_pasta=None, file_id=None):
    service = authenticate()
    media = MediaFileUpload(nome_arquivo, resumable=True)

    if file_id:
        updated_file = service.files().update(
            fileId=file_id,
            media_body=media
        ).execute()
        print(f"Arquivo atualizado! ID: {updated_file.get('id')}")
    else:
        file_metadata = {
            'name': nome_arquivo,
            'parents': [id_pasta] if id_pasta else []
        }
        created_file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields='id'
        ).execute()
        print(f"Arquivo enviado! ID: {created_file.get('id')}")

def deletar_arquivo_local(caminho_arquivo):
    try:
        os.remove(caminho_arquivo)
        print(f"Arquivo local '{caminho_arquivo}' deletado com sucesso.")
    except FileNotFoundError:
        print(f"Arquivo '{caminho_arquivo}' não encontrado.")
    except Exception as e:
        print(f"Erro ao deletar o arquivo '{caminho_arquivo}': {e}")