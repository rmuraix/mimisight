# MimiSight

![Licence](https://img.shields.io/github/license/rmuraix/mimisight)

## 実行方法

### アプリ

```bash
cd app
pnpm install
pnpm start
```

Devcontainerを使用をする場合は`.devcontainer/.env`を作成します。

```bash
REACT_NATIVE_PACKAGER_HOSTNAME=192.168.XXX.XXX # マシンのIPアドレス
```

表示されたQRコードを**Expo Go**で読み取ってください。

## アーキテクチャ

![Arch](./docs/assets/architecture.drawio.svg)
