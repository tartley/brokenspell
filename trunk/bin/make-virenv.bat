
virtualenv virenv-%COMPUTERNAME%
call virenv-%COMPUTERNAME%\Scripts\activate.bat

cd ..\pyglet-1.1.4
python setup.py install
cd ..\sinister-ducks

