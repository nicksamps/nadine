from unittest import TestCase, mock


ERROR_MESSAGES = {
    'patches_type': "'patches' must be a list",
    'patch_type': "Invalid element in patches list. String or tuple of two strings expected."
}


class NadineTestCase(TestCase):
    def __get_patch_variable_name_from_string(self, patch):
        return patch.split('.')[-1]

    def __get_patch_variable_name_from_tuple(self, patch):
        return patch[1]

    def __get_patch_variable_name(self, patch):
        if isinstance(patch, str):
            return self.__get_patch_variable_name_from_string(patch)
        if isinstance(patch, tuple) and len(patch) > 1:
            return self.__get_patch_variable_name_from_tuple(patch)

        raise TypeError(ERROR_MESSAGES['patch_type'].format(type(patch)))

    def patch(self):
        if not hasattr(self, 'patches') or not self.patches:
            return

        if not isinstance(self.patches, list):
            raise TypeError(ERROR_MESSAGES['patches_type'])

        self.__patchers = []
        for patch in self.patches:
            patch_name = self.__get_patch_variable_name(patch)
            patcher = mock.patch(patch[0]) if isinstance(patch, tuple) else mock.patch(patch)
            setattr(self, patch_name, patcher.start())
            self.__patchers.append(patcher)

    def stop_patches(self):
        if not hasattr(self, '_NadineTestCase__patchers'):
            return

        for patcher in self.__patchers:
            patcher.stop()

    def setUp(self):
        self.patch()

    def tearDown(self):
        self.stop_patches()


class ManualNadineTestCase(NadineTestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass
