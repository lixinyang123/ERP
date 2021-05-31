pyinstaller -F server/main.spec
mkdir -p client/resource/server
mv dist/main/* client/resource/server
rm -rf dist build

cd client
node_modules/.bin/electron-builder
mv build ..