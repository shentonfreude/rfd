========
 README
========

To Do
=====

* Folderish Filedrops
* Blobs for files (or repoze.filesafe?)
* Folderish folders
* traversalwrapper

* Users at top level where auth happens
* each drop has own copy of users
* each drop user has perms: read, write, etc


Questions
=========

Store /users/username sep from /drops/dropname, or use BFG's
understanding of what the object is?

How to get per-drop users from global users list? is this a sane way? 
Or does a user have a 'group' which is equivalent to the dropname?

How to make ACLs that allow a drop (group) member to have
read/write/readwrite?
