#!/usr/bin/env bash
set -euo pipefail
# set -x

node -v; npm -v; pnpm -v

apk add --no-cache build-base g++ cairo-dev pango-dev giflib-dev python3 zlib-dev gcc jpeg-dev python3-dev musl-dev freetype-dev
pip3 install requests

cd /ql
npm config set registry https://registry.npmjs.org/
pnpm add -g pnpm
pnpm install -g npm png-js date-fns axios crypto-js ts-md5 tslib @types/node requests tough-cookie jsdom download tunnel fs ws form-data js-base64 qrcode-terminal silly-datetime
