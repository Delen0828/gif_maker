# python make.py --move stat --static True --line 2 &
# python make.py --move stat --static True --line 3 &
# python make.py --move stat --static True --line 4 &

# python make.py --move seq --line 2 &
# python make.py --move seq --line 3 &
# python make.py --move seq --line 4 &

# python make.py --move seq --trace True --line 2 &
# python make.py --move seq --trace True --line 3 &
# python make.py --move seq --trace True --line 4 &

python make.py --move seq --history True --line 2 &
python make.py --move seq --history True --line 3 &
python make.py --move seq --history True --line 4 

# python make.py --move seq --trace True --history True --line 2 &
# python make.py --move seq --trace True --history True --line 3 &
# python make.py --move seq --trace True --history True --line 4 &

# python make.py --move sync --line 2 &
# python make.py --move sync --line 3 &
# python make.py --move sync --line 4 &

# python make.py --move sync --trace True --line 2 &
# python make.py --move sync --trace True --line 3 &
# python make.py --move sync --trace True --line 4
