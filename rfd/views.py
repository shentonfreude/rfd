# Templates get 'context' automatically so we don't need to pass it.
from repoze.bfg.url import model_url
from webob.exc import HTTPFound
import logging
logging.basicConfig(level=logging.INFO)

def _make_name_url(context, request, thing):
    """Can I do this differently by having a url() meth on the obj?
    And use __name__ in the template?
    Or maybe we want to display a friendly 'name' instead of __name__
    """
    if hasattr(thing, 'items'):
        return [_make_name_url(context, request, t) for t in thing.items()]

    import pdb; pdb.set_trace()

    return {'name': thing.__name__,
            'url': model_url(context, request, thing)}


def filedrop(context, request):
    return {'project':'rfd (repoze file drop)',
            'droplinks': _make_name_url(context, request, context['drops'])
            }

def add_drop(context, request):
    """Add a Drop under Drops in the top-level FileDrop.
    """
    logging.info('add_drop context=%s' % context)
    if request.method == 'POST':
        name = request.POST['name']
        drops = context['drops']
        drop = drops.add_drop(name)
        # TODO: do I need to save() this? 
        # drop.attributes...
        url = model_url(context, request)
        return HTTPFound(location=url)
    return {}
    

def add_file(context, request):
    """Add an uploaded file to the Folder or Drop context.
    import pdb; pdb.set_trace()
    """
    import pdb; pdb.set_trace()
    logging.info('add_file context=%s' % context)
    name = mimetype = size = body = ''
    if request.method == 'POST':
        file_ = request.POST['file']
        name = file_.filename
        mimetype = file_.type  # ''
        # NO size ATTR?
        body = file_.file.read() # need binary here?
        size = len(body)
    return {'name' : name,
            'mimetype' : mimetype,
            'size' : size,
            'body' : body,
            }
    

    


# def upload(request):
#     name = mimetype = size = body = ''

#     if request.method == 'POST':
#         file_ = request.POST['file']
#         name = file_.filename
#         mimetype = file_.type  # ''
#         # NO size ATTR?
#         body = file_.file.read() # need binary here?
#         size = len(body)
#         import pdb; pdb.set_trace()

#     return {'name' : name,
#             'mimetype' : mimetype,
#             'size' : size,
#             'body' : body,
#             }
    
