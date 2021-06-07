cd $(cd $(dirname ${BASH_SOURCE[0]})/..; pwd)

rm -rf client/resources
rm -rf build

pyinstaller -F server/build.spec
mkdir -p client/resources/server
mv dist/ERP_SERVICE/* client/resources/server
rm -rf dist build

cd client
node_modules/.bin/electron-builder
mv build ..