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

TensorFlow
----------

The other big Python framework for AI. ~~I haven't checked in depth yet
but it looks like it is also using *Pickle*. However, there are safe
ways to use *Pickle*, so its left to check for the details.~~

*TensorFlow* is supporting various formats such as legacy TF, HDF5 (Hirarchical Data Format)
and the new Keras v3 format. The latter has got a safe-mode for a reason (`False` by default)
when loading saved models, since *TensorFlow* models can have Lambda functions attached which
can be executed upon load. No such safe-mode with the HDF5 format. IOW you can create and save
a model that contains Base64 encoded Python bytecode that gets executed during load.
The dedicated subdir contains PoC code but not the model itself (as with *PyTorch*) since
it contains much more data, so you have to call `create-model.py` first. The version
I tested was `2.15.0`.

NumPy
-----

Not an AI framework but the foundation for a lot of data science stuff.
Their *Pickle* issue was fixed quite a while ago.

ONNX
----

ONNX is a data format used for exchanging model data. It is based on
*Protobuf*, so a simple code smuggling as with *Pickle* is not possible.
However, it is subject to research. A problem with ONNX related to
*PyTorch* can arise, since *PyTorch* is filename-agnostic so that a file
ending in `.onnx` could still be loaded as *Pickle* data, if the scientist
as per confusion is just using `torch.load()` instead of `onnx.load()`.

