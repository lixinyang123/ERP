rm -rf client/resources

pyinstaller -F server/main.spec
mkdir -p client/resources/server
mv dist/main/* client/resources/server
rm -rf dist build

cd client
node_modules/.bin/electron-builder
mv build ..