import setuptools
import setuptools_odoo

setup_keywords = setuptools_odoo.prepare(addon_name='account_reversal')
setuptools.setup(**setup_keywords)
