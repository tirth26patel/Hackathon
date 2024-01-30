echo "BUILD START"
python3.12 -m pip install -r requiremnet.txt
python3.12 manage.py collectstatic --noinput --clear
echo "BUID END"