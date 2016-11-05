# nadine

![](http://vignette4.wikia.nocookie.net/twinpeaks/images/4/4b/NadineNew.jpg/revision/latest/scale-to-width-down/270?cb=20161026023639)

Easy patching for python unittests.

The plan is to make it so that you just add a list of functions you want to patch to `self` during `setUp()` and then the library will patch them and set them on `self`. This means no more decorator piles or long lists of arguments into test functions.

Currently this has only been tested for mocking functions, classes are next!
