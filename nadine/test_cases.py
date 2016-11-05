from unittest import TestCase, mock


ERROR_MESSAGES = {
    'patches_type': "'patches' must be a list",
    'patch_type': "Invalid type ({}) used in 'patches'. String expected."
}


class NadineTestCase(TestCase):
    def _NadineTestCase__get_patch_variable_name(self, patch):
        return patch.split('.')[-1]

    def patch(self):
        if not hasattr(self, 'patches') or not self.patches:
            return

        if not isinstance(self.patches, list):
            raise TypeError(ERROR_MESSAGES['patches_type'])

        self._NadineTestCase__patchers = []
        for patch in self.patches:
            if not isinstance(patch, str):
                raise TypeError(ERROR_MESSAGES['patch_type'].format(type(patch)))

            patcher = mock.patch(patch)
            patch_name = self._NadineTestCase__get_patch_variable_name(patch)
            setattr(self, patch_name, patcher.start())
            self.__patchers.append(patcher)

    def stop_patches(self):
        if not hasattr(self, '_NadineTestCase__patchers'):
            return

        for patch in self._NadineTestCase__patchers:
            patch.stop()
