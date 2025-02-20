7350tarpwn
==========

*We pwn AI setups, too! Ask us about it!*
<p align="center">
<a href="https://github.com/c-skills/welcome">
<img src="https://github.com/c-skills/welcome/blob/master/logo.jpg"/>
</a>
</p>


Demo run
--------

**WARNING. ONLY EXECUTE THESE SCRIPTS IN AN ISOLATED TEST VM. IT WILL SMASH YOUR LOCAL FILES.**

<p align="center">
<img src="https://github.com/stealth/tensor-pwn/blob/master/tarpwn/tarpwn.jpg"/>
</a>
</p>


Please note:

* the beauty of not needing an absolute path name
* how this is an RCE against data scientists if you are one of the privileged folks running TLS MiM appliances
* The beauty of my missing writeup that I originally planned to write about 0day bug finding by AI
  (*man vs. machine*) but instead just made the 0day rather than writing theories about it. Nevertheless,
  my points are written on scratch and you can hit me up discussing it at the next Con.
* the beauty of missing writeup about the bug, which is trivial and left to the reader
* the beauty of how `tarfile.py` makes remarks about a different bug that was fixed in 2007 while doing our nosejob
* the beauty of being a RCE (by file-overwrite, though) against a memory-safe language :)
* the beauty this 0day comes from good old Germany

The demo was run on a RH based system with latest updates and pip'ed tensorflow, so I guess its all current.

