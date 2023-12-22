The state of AI
===============

I do know nothing about tensors, fancy AI, models and such but I do know
about coding, HPC and storage formats, so I will populate or not this repo
with classic IT security related stuff that I find myself funny about AI.

The usual topic is code execution, which should not be possible by just
loading data (models) since few people would expect that they could
execute malware when fetching pre-trained models from somewhere. If
*you* do expect that, this repo might not be for you but it is still
considered fun for me since I quite know how data is handled in scientific
environments.

If folks are using models to be loaded on drones, you can pop drones! :)


I was pointed to [a link](https://splint.gitbook.io/cyberblog/security-research/tensorflow-remote-code-execution-with-malicious-model) so
someone already had fun with *TensorFlow* in past and all credits should go there. Since the attack surface
for model loading is just too obvious it is also safe to assume that more people (the known
unknowns) had their fun with it in past. So it is interesting to see that AI security is widely anticipated
as prompt-bypassing or mis-training of models on conferences and media but only few people are doing it right.
However when I hear *prompt*, I certainly think of something different. :)

There also exist [tables for a safety overview](https://github.com/huggingface/safetensors), but it has to be read with
caution, e.g. their safety assumption for h5 files is wrong (see *TensorFlow* section).


PyTorch
-------

One of the big Python frameworks for AI. One issue that can be found
in this repo can be exploited by passing model data as plain *Pickle*
so that the legacy loader is transparently invoked. Usually *PyTorch*
has a much more sophisticated storage format consisting of a zip file
with a certain structure.

<p align="center">
<img src="https://github.com/stealth/tensor-pwn/blob/master/pytorch/model1.jpg" />
</p>

*Code Exec demo during model load, popping xeyes on the screen*

The version I tested was `2.1.2`.

The more recent model saving format consists of a zip file containing `__torch__.py`
files and such but I wasn't able to exec arbitrary code with it as the loader seems to
be a stripped down python. But that doesn't say anything, it might just work later in time.
If you happen to find a code exec there, just open a ticket here.

TensorFlow
----------

The other big Python framework for AI. ~~I haven't checked in depth yet
but it looks like it is also using *Pickle*. However, there are safe
ways to use *Pickle*, so its left to check for the details.~~

*TensorFlow* is supporting various formats such as legacy TF, HDF5 (Hirarchical Data Format)
and the new Keras v3 format. The latter has got a `safe_mode` for a reason (`False` by default)
when loading saved models, since *TensorFlow* models can have Lambda functions attached which
can be executed upon load. However, depending on actual used version and local package config,
the Keras code integrated into their upstream repo might not yet profit from the `safe_mode`
(seems to be quite new feature?).
No such safe-mode with the HDF5 (h5) format. IOW you can create and save
a model that contains Base64 encoded Python bytecode that gets executed during load.
The dedicated subdir contains PoC code but not the model itself (as with *PyTorch*) since
it contains much more data, so you have to call `create-model.py` first. The version
I tested was `2.15.0`.

To be noted, that if you rename a h5 file to `model.keras` it still loads by the
same function `tf.keras.models.load_model()` with the vulnerable h5 loader, similar with *PyTorch*
that tries to be as convenient as possible when detecting storage formats.

Keras
-----

Multi-framework API. In some of their versions there is a `safe_mode` check (default set to disable
Lambda execution) but it is not found in the fork thats integrated in *TensorFlow* so it is unclear
which versions benefit from it.


PaddlePaddle
------------

*PArallel Distributed Deep LEarning* framework from China. Also using *Pickle* as storage format
and making a note on its security implications in their docu. If you check the docu, it looks a lot
like *PyTorch*.


Torch
-----

The original one and only real *Torch* written in Lua but seems to be discontinued.

NumPy
-----

Not an AI framework but the foundation for a lot of data science stuff.
Their *Pickle* issue was fixed quite a while ago by setting `allow_pickle=False` by default
in the `load()` function. However this will strip off a lot of functionallity thats commonly
required for the npy persistence.

ONNX
----

ONNX is a data format used for exchanging model data. It is based on
*Protobuf*, so a simple code smuggling as with *Pickle* is not possible.
However, it is subject to research. A problem with ONNX related to
*PyTorch* can arise, since *PyTorch* is filename-agnostic so that a file
ending in `.onnx` could still be loaded as *Pickle* data, if the scientist
as per confusion is just using `torch.load()` instead of `onnx.load()`.


SafeTensors
-----------

A storage format for Tensors but you can't store entire models with it, so its not quite suitable
for the discussion here when you want to load pre-trained models.

