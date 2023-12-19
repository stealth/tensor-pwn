The state of AI
===============

I do know nothing about tensors, fancy AI, models and such but I do know
about coding, HPC and storage formats, so I will populate or not this repo
with classic IT security related stuff that I find myself funny about AI.

PyTorch
-------

One of the big Python frameworks for AI. One issue that can be found
in this repo can be exploited by passing model data as plain Pickle
so that the legacy loader is transparently invoked. Usually *PyTorch*
has a much more sophisticated storage format consisting of a zip file
with a certain structure.

<p align="center">
<img src="https://github.com/stealth/tensor-pwn/blob/master/pytorch/model1.jpg" />
</p>

TensorFlow
----------

The other big Python framework for AI. I haven't checked in depth yet
but it looks like it is also using *Pickle*. However, there are safe
ways to use Pickle, so its left to check for the details.

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
ending in onnx could still be loaded as *Pickle* data, if the scientist as
per confusion is just using `torch.load()` instead of `onnx.load()`.

