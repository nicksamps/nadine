from nadine.test_cases import NadineTestCase


def return_whatever(whatever=None):
    return whatever


def return_meh(meh=None):
    return meh


class TestPatch(NadineTestCase):
    def test_called_with_patches_not_defined(self):
        self.patch()

    def test_called_with_patches_falsey(self):
        self.patches = None
        self.patch()

    def test_invalid_patches_type_raises_validation_error(self):
        self.patches = 'bad type'
        with self.assertRaises(TypeError):
            self.patch()

    def test_invalid_patch_type_raises_validation_error(self):
        self.patches = [1]
        with self.assertRaises(TypeError):
            self.patch()

    def test_patch_patches_functions(self):
        self.patches = [
            'tests.test_patching.return_whatever',
            'tests.test_patching.return_meh'
        ]
        self.patch()

        return_whatever()
        return_meh()

        self.return_whatever.assert_called_once_with()
        self.return_meh.assert_called_once_with()
        self.stop_patches()

    def test_patch_patches_function_with_tuple_custom_name(self):
        self.patches = [
            ('tests.test_patching.return_whatever', 'some_name')
        ]
        self.patch()

        return_whatever()

        self.some_name.assert_called_once_with()
        self.stop_patches()

    def test_patch_patches_function_with_tuple_missing_name(self):
        self.patches = [
            ('tests.test_patching.return_whatever', )
        ]
        with self.assertRaises(TypeError):
            self.patch()


class TestStopPatch(NadineTestCase):
    def test_called_with_patchers_not_defined(self):
        self.stop_patches()

    def test_stop_patches_unpatches_function(self):
        self.patches = [
            'tests.test_patching.return_whatever'
        ]
        self.patch()
        self.assertNotEqual(return_whatever('whatever'), 'whatever')

        self.stop_patches()

        self.assertEqual(return_whatever('whatever'), 'whatever')
