# from persistent.mapping import PersistentMapping
from repoze.folder import Folder
from persistent import Persistent
import datetime

#from repoze.folder import Folder
# folder = Folder()
# class Child(Persistent): pass
# folder['child1'] = Child()

# FileDrop/Users/UserInstance
# FileDrop/Drops/DropInstance

def create_child(Klass, parent, name, **kwargs):
    """Create a new child of klass, parenting it, setting kwargs attrs.
    """
    child = Klass()
    child.__dict__ = kwargs
    child.__parent__ = parent
    child.__name__ = name
    return child

class FileDrop(Folder):
    """Top level containing Users and Drops
    """
    __name__ = None
    __parent__ = None

class Users(Folder):
    """Singleton top-level Folder that contains (only) User objects.
    """
    def add(self, name):
        self[name] = create_child(User, self, name)
        

class User(Persistent):
    """User with password, possibly permissions for auth.
    Should exist at only top level?
    Different kinnd of user for each Drop with perms?
    """
    def __init__(self, name):
        self.name = name        # don't need since we have __name__
        

class Drops(Folder):
    """Singleton top-level Folder that contains (only) drops.
    """
    def add_drop(self, name):
        import pdb; pdb.set_trace()
        if name in self:
            name = "%s_%s" % (name, datetime.datetime.now())
        # WTF 'name' is 'get'
        self[name] = create_child(Drop, self, name)
        
class Drop(Folder):
    """Folderish that contains Files, and Folders.
    TODO: how to know about this Drop's users?
    """
    def add_folder(self, name):
        self[name] = create_child(Folder, self, name)

    def add_file(self, name):
        self[name] = create_child(File, self, name)
        
    
class File(Persistent):
    __parent__ = __name__ = None
    def __init__(self, name=None, size=None, mimetype=None, upload_date=None, username=None):
        """should I extract metadata from uploadfile object?
        TODO: call for creation by Drop.add_file() has no args
        """
        self.name = name        # TODO use __name__ 
        self.mimetype = mimetype
        self.upload_date = upload_date
        self.username = username # TODO point at actual user instead?
        # TODO: need a way to store the file content as Blob
        
class Folder(Folder):
    """Folderish object that contains Files, Folders.
    """
    def add_folder(self, name):
        self[name] = create_child(Folder, self, name)

    def add_file(self, name):
        self[name] = create_child(File, self, name)
        
        

    
def appmaker(zodb_root):
    if not 'app_root' in zodb_root:
        # create /users/ and /filedrops/ here?
        app_root = FileDrop()
        users = Users()
        users.__name__ = 'Users'
        users.__parent__ = app_root
        app_root['users'] = Users()
        drops = Drops()
        drops.__name__ = 'Drops'
        drops.__parent__ = app_root
        app_root['drops'] = drops
        zodb_root['app_root'] = app_root
        import transaction
        transaction.commit()
    return zodb_root['app_root']
