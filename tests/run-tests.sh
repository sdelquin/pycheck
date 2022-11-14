export PYTHONPATH=../src

python ../src/pycheck/main.py ./test_pycheck.py -h
echo '------------------------------------------------------------------------'
python ../src/pycheck/main.py ./test_pycheck.py -l
echo '------------------------------------------------------------------------'
python ../src/pycheck/main.py ./test_pycheck.py 10 10
echo '------------------------------------------------------------------------'
python ../src/pycheck/main.py ./test_pycheck.py
echo '------------------------------------------------------------------------'
python ../src/pycheck/main.py ./test_pycheck.py --hash
