cd $(Split-Path -Parent $MyInvocation.MyCommand.Definition)
cd ..

Remove-Item client/resources -recurse
Remove-Item build -recurse

pyinstaller -F server/build.spec
mkdir client/resources/server
mv dist/ERP_SERVICE/* client/resources/server
Remove-Item dist build -recurse

cd client
node_modules/.bin/electron-builder
mv build ..