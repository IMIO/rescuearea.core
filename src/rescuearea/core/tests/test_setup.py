# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from rescuearea.core.testing import RESCUEAREA_CORE_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that rescuearea.core is properly installed."""

    layer = RESCUEAREA_CORE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer["portal"]
        self.installer = api.portal.get_tool("portal_quickinstaller")

    def test_product_installed(self):
        """Test if rescuearea.core is installed."""
        self.assertTrue(self.installer.isProductInstalled("rescuearea.core"))

    def test_browserlayer(self):
        """Test that IRescueareaCoreLayer is registered."""
        from rescuearea.core.interfaces import IRescueareaCoreLayer
        from plone.browserlayer import utils

        self.assertIn(IRescueareaCoreLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = RESCUEAREA_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer["portal"]
        self.installer = api.portal.get_tool("portal_quickinstaller")
        roles_before = api.user.get_roles(TEST_USER_ID)
        setRoles(self.portal, TEST_USER_ID, ["Manager"])
        self.installer.uninstallProducts(["rescuearea.core"])
        setRoles(self.portal, TEST_USER_ID, roles_before)

    def test_product_uninstalled(self):
        """Test if rescuearea.core is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled("rescuearea.core"))

    def test_browserlayer_removed(self):
        """Test that IRescueareaCoreLayer is removed."""
        from rescuearea.core.interfaces import IRescueareaCoreLayer
        from plone.browserlayer import utils

        self.assertNotIn(IRescueareaCoreLayer, utils.registered_layers())
