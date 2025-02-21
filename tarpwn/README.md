<p align="center">
<img src="https://github.com/stealth/tensor-pwn/blob/master/tarpwn/banner.jpg"/>
</a>
</p>

This 0day research was sponsored by `c->skills research` for free, so if you are assigning a CVE or make any patches or
otherwise refer to this PoC, please properly credit `Sebastian Krahmer of c->skills research` for bug finding and PoC.

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

* the beauty of not needing a known-name path component
* how this is an RCE against data scientists if you are one of the privileged folks running TLS MiM appliances
* ~~The beauty of my missing writeup that I originally planned to write about 0day bug finding by AI
  (*man vs. machine*) but instead just made the 0day rather than writing theories about it. Nevertheless,
  my points are written on scratch and you can hit me up discussing it at the next Con.~~ See below. I know
  that some readers like to read.
* the beauty of missing writeup about the bug, which is trivial and left to the reader
* the beauty of how `tarfile.py` makes remarks about a different bug that was fixed in 2007 while doing our nosejob
* the beauty of being a RCE (by file-overwrite, though) against a memory-safe language :) Also [check here](https://github.com/c-skills/rust1)
* the beauty this 0day comes from good old Germany

The demo was run on a RH based system with latest updates and pip'ed tensorflow, so I guess its all current.


man vs machine
==============

[Will AI substitute bug finding/research done by humans anytime soon?](https://www.forbes.com/sites/daveywinder/2024/11/05/google-claims-world-first-as-ai-finds-0-day-security-vulnerability/)

Decide yourself:

1. AI cannot be put under NDA
-----------------------------

If you do bug hunting or security at the professional level, you do not want that
everyone knows what you are up to, what your capabilities are and what not. You do have
business secrets to protect, so you put your developers and staff under NDA.
This is not possible with AI, even when some companies [provide premium accounts](https://github.com/features/copilot/plans?cft=copilot_lo.features_copilot) that
shield you from IP infringement claims.
This means that typing straight ahead into online AI prompts or submitting your (not Open)-Source is not an option.
Even if you are trying to drift your questions, add deltas etc. the AI and its observers
will finally get info *out of you*. If you do serious research, this is not an option.

While AI instances can be run on-premise and offline, it will require quite some setup and maintenance effort,
hardware costs and developers/admins to do so. Model rot starts at day 0 (not to say at 0day), so you most likely
need to pay one developer at least to keep everything up to date. At the end you pay twice:
One time for your AI setup/admins to look for bugs and a second time for developers anyway.


2. Prompts are monitored
------------------------

Not only you can't put the AI under NDA, the entered [prompts are monitored.](https://openai.com/index/disrupting-malicious-uses-of-ai-by-state-affiliated-threat-actors/)
What a surprise. Everything you submit is lost forever, not just to the AI itself but to the teams and the companies
behind it and even if you find 0days by asking AI, its not longer a 0day at the time you see the reply.


3. Your adversary knows AI, too
-------------------------------

You are not alone. Your competitors and adversaries know how to use AI, too. So, if you conduct
bug search on Open Source projects, a lot of other people will have stuffed this code into AI and asked
for bugs. This means that AI-spottable bugs will be found soon, likely be fixed and only bugs
will be left for which you need to pay a good bug searcher anyway to find bugs that AI missed.

4. False positives
------------------

Currently, AI produces quantity of [bad quality.](https://daniel.haxx.se/blog/2024/01/02/the-i-in-llm-stands-for-intelligence/)
This may change in future, but given the *trash in, trash out* principle and as there are a lot of bad quality
reports from the past decades, AI might just learn junk. As already stated, this argument might not hold very long
when we extrapolate how fast this tech is growing.
Nonetheless, for AI even with better output quality you still need researchers to understand and review the output and
make sense of it.

5. Vendor Lock-in at AI level
-----------------------------

It is apparent that there is a battle between the hemispheres about AI dominance, just as it was/is about cyber and information
dominance in the past decades. If you do not have the resources to create your own bug finding machine, you will depend
on a vendor badly and you will lose your skills and capabilities over time as you waste your efforts with AI setup and training
instead of generating knowledge. And as stated earlier, you can't put the AI under contract to keep knowledge within your company
as you can do with golden handcuffs to developers.


6. Models can't be trusted: There is no NUMS
--------------------------------------------

Lets put aside security considerations about code execution. If you are using trained models from any hemisphere, how
can you be sure it was not intentionally trained to *not find* specific bugs that this hemisphere wants to keep secret?
Even if they release the model as Open-Source, it may be so well designed that it will not find the bugs you want.
In cryptography there exist a similar known problem with algorithms and magic numbers where the term [NUMS](https://en.wikipedia.org/wiki/Nothing-up-my-sleeve_number) exist in order to proof
that the algorithm does not contain any back-doors. Nothing remotely similar exists for AI models and I consider it very hard
to come close to NUMS in that field.

7. AI generated code will flood the zone
----------------------------------------

It is possible that we will see so much generated code soon that there is a different effect on bugs than one would hope with regards
of finding them. Similar to the PHP effect. Even more so since it enables bad developers to submit more shitty code.


8. Leaks
--------

Imagine for a time you do have a model that can blow any human away in that field just as it happened that machines are
world champion in chess today and noone can compete. You have trainied it and all these skills are eventually within their persitence files
or database. How do you make sure your adversaries will never reach out to it or it just leaks blabbering in a way we can't predict today?
This is similar to *do not put all eggs into one basket* approach which you are going to violate if you are trying to create such a bug-machine.
It might look good at paper first to increase your cyber capabilities, but it might fall off your feat later. Not only you can't NDA
the AI, you also can't threaten it with jail or whatever the preferred coercion method is in that hemisphere.


9. Rice theorem and friends
---------------------------

Eventually I think that its theoretically impossible that any and all bugs will be found by AI, [as math tells us.](https://en.wikipedia.org/wiki/Rice%27s_theorem).
For some programming languages even the [parsing is undecidable.](https://www.perlmonks.org/?node_id=663393) and its not just Perl.


All this does *not* mean that there won't be significant efforts in that field and we *will* see advances and AI found 0day in future,
but we will still see handcrafted xSports and shells all over the place, except the AI effect on 0day could drastically increase their
prices in which case nobody could effort to make any public releases anymore, albeit 0days by humans still exist. But this is a different story.

