# Backend

uv + FastAPI + Dockerの構成

## 開発サーバーの起動方法

```bash
docker compoe up
```

## 本番環境の起動

```bash
docker build -f prod.Dockerfile -t mimisight-prod .
docker run -p 8000:8000 mimisight-prod
```
