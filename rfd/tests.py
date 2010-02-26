import unittest

from repoze.bfg.configuration import Configurator
from repoze.bfg import testing
from rfd import models



class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = Configurator()
        self.config.begin()

    def tearDown(self):
        self.config.end()

    def test_filedrop_view(self):
        from rfd.views import filedrop
        request = testing.DummyRequest()
        context = None          # this can't be right
        info = filedrop(context, request)
        self.assertEqual(info['project'], 'rfd (repoze file drop)')

class AppmakerTest(unittest.TestCase):

    def _callFUT(self, zodb_root):
        from rfd.models import appmaker
        return appmaker(zodb_root)
    
    def test_no_app_root(self):
        root = {}
        self._callFUT(root)
        self.assertTrue(root.has_key('app_root'))
        self.assertTrue('users' in root['app_root'])
        self.assertTrue('drops' in root['app_root'])

    def test_with_app_root(self):
        app_root = object()
        root = {'app_root': app_root}
        self._callFUT(root)
        self.failUnless(root['app_root'] is app_root)


class FileDropModelTests(unittest.TestCase):

    def _getTargetClass(self):
        from .rfd.models import FileDrop # DOTTED?
        return FileDrop

    def _makeOne(self):
        return self._getTargetClass()()

    def test_contructor(self):
        instance = self._makeOne()
        self.assertTrue(hasattr(instance, '__name__'))
        self.assertTrue(hasattr(instance, '__parent__'))



class ModelUtilTests(unittest.TestCase):
    def setUp(self):
        self.config = Configurator()
        self.config.begin()

    def tearDown(self):
        self.config.end()

    def test_create_child_no_kwargs(self):
        from rfd.models import create_child
        class Thing(object):
            pass
        parent = Thing()
        name = "alice"
        child = create_child(Thing, parent, name)
        self.assertEqual(child.__parent__, parent)
        self.assertEqual(child.__name__, name)

    def test_create_child_with_kwargs(self):
        from rfd.models import create_child
        class Thing(object):
            pass
        parent = Thing()
        name = "alice"
        child = create_child(Thing, parent, name, foo="foo", bar="bar")
        self.assertEqual(child.__parent__, parent)
        self.assertEqual(child.__name__, name)
        self.assertEqual(child.foo, "foo")
        self.assertEqual(child.bar, "bar")

        
        
