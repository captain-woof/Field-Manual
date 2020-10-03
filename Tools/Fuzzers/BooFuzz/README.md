# BooFuzz

BooFuzz is a Python package developed by [*@jtpereyda*](https://www.twitter.com/jtpereyda) that helps to fuzz 'everything'. You can check out his BooFuzz repo on [Github](https://github.com/jtpereyda/boofuzz), and also consult the [Official Documentaion](https://boofuzz.readthedocs.io/en/stable/) whenever required.

Basically, what you do with BooFuzz is, you build tests (of what to fuzz, what to not fuzz), join all these cases to either the root, or between parent and child cases, and fire them off. *(If this sounds confusing, please read 'How It Works.md').*

## Installation
`pip install boofuzz`
(replace 'pip' by 'pip3' if you are installing for Python3.5+ and not Python2.8+)

For advanced installation procedures/info, read [this](https://github.com/jtpereyda/boofuzz/blob/master/INSTALL.rst).
