cd $(Split-Path -Parent $MyInvocation.MyCommand.Definition)
cd ..

Remove-Item client/resources -recurse
Remove-Item build -recurse

pyinstaller -F server/main.spec
mkdir client/resources/server
mv dist/main/* client/resources/server
Remove-Item dist build -recurse

cd client
node_modules/.bin/electron-builder
mv build ..