rm -rf dist
pyinstaller main.py -F --hiddenimport six --hiddenimport appdirs --hiddenimport packaging --hiddenimport packaging.version --hiddenimport packaging.specifiers --hiddenimport packaging.requirements
rm -rf build
cp -r assets dist/
mv dist/main dist/anataNoNiwaOSewaShiteKudasai.run
mv dist anataNoNiwaOSewaShiteKudasai
tar -cvzf anataNoNiwaOSewaShiteKudasai.tar.gz anataNoNiwaOSewaShiteKudasai
