export PYTHONPATH=../src

python ../src/pycheck/main.py -l ./test_pycheck.py
echo '------------------------------------------------------------------------'
python ../src/pycheck/main.py -c ./test_pycheck.py
echo '------------------------------------------------------------------------'
python ../src/pycheck/main.py -r ./test_pycheck.py 10 10
