python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
echo $(ls)
python3 find_approximate_folding_angles.py $1 $2 $3
