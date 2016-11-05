# nadine
Easy patching for python unittests.

The plan is to make it so that you just add a list of functions you want to patch to `self` during `setUp()` and then the library will patch them and set them on `self`. This means no more decorator piles or long lists of arguments into test functions.
