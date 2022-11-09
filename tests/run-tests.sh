export PYTHONPATH=../src

python ../src/pycheck/main.py ./test.py -h
echo '------------------------------------------------------------------------'
python ../src/pycheck/main.py ./test.py -l
echo '------------------------------------------------------------------------'
python ../src/pycheck/main.py ./test.py 10 10
echo '------------------------------------------------------------------------'
python ../src/pycheck/main.py ./test.py
