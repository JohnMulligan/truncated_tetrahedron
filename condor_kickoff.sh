pip install --user -r requirements.txt
echo $(ls)
python find_approximate_folding_angles.py $1 $2 $3
