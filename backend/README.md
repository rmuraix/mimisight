# Backend

uv + FastAPI + Dockerの構成

## 開発サーバーの起動方法

`.env`を作成します。

```bash
GOOGLE_CLOUD_PROJECT=XXX
GOOGLE_CLOUD_LOCATION=us-central1
GOOGLE_GENAI_USE_VERTEXAI=True
GOOGLE_APPLICATION_CREDENTIALS=credentials/sa-key.json
MODEL_NAME=gemini-2.0-flash-live-preview-04-09

```

`credentials/sa-key.json`を作成します。

```bash
gcloud iam service-accounts keys create sa-key.json --iam-account=XXX@XXX
```

サーバーを起動します。

```bash
docker compose up
```

## 本番環境の起動

```bash
docker build -f prod.Dockerfile -t mimisight-prod .
docker run --env-file .env -p 8000:8000 mimisight-prod
```
