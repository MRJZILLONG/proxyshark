# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_psnfqueue', [dirname(__file__)])
        except ImportError:
            import _psnfqueue
            return _psnfqueue
        if fp is not None:
            try:
                _mod = imp.load_module('_psnfqueue', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _psnfqueue = swig_import_helper()
    del swig_import_helper
else:
    import _psnfqueue
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class queue(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, queue, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, queue, name)
    __repr__ = _swig_repr
    __swig_setmethods__["dummy"] = _psnfqueue.queue_dummy_set
    __swig_getmethods__["dummy"] = _psnfqueue.queue_dummy_get
    if _newclass:dummy = _swig_property(_psnfqueue.queue_dummy_get, _psnfqueue.queue_dummy_set)
    __swig_setmethods__["_h"] = _psnfqueue.queue__h_set
    __swig_getmethods__["_h"] = _psnfqueue.queue__h_get
    if _newclass:_h = _swig_property(_psnfqueue.queue__h_get, _psnfqueue.queue__h_set)
    __swig_setmethods__["_qh"] = _psnfqueue.queue__qh_set
    __swig_getmethods__["_qh"] = _psnfqueue.queue__qh_get
    if _newclass:_qh = _swig_property(_psnfqueue.queue__qh_get, _psnfqueue.queue__qh_set)
    __swig_setmethods__["_cb"] = _psnfqueue.queue__cb_set
    __swig_getmethods__["_cb"] = _psnfqueue.queue__cb_get
    if _newclass:_cb = _swig_property(_psnfqueue.queue__cb_get, _psnfqueue.queue__cb_set)
    __swig_setmethods__["_mode_set"] = _psnfqueue.queue__mode_set_set
    __swig_getmethods__["_mode_set"] = _psnfqueue.queue__mode_set_get
    if _newclass:_mode_set = _swig_property(_psnfqueue.queue__mode_set_get, _psnfqueue.queue__mode_set_set)
    def set_callback(self, *args): return _psnfqueue.queue_set_callback(self, *args)
    def open(self): return _psnfqueue.queue_open(self)
    def close(self): return _psnfqueue.queue_close(self)
    def bind(self, *args): return _psnfqueue.queue_bind(self, *args)
    def unbind(self, *args): return _psnfqueue.queue_unbind(self, *args)
    def create_queue(self, *args): return _psnfqueue.queue_create_queue(self, *args)
    def fast_open(self, *args): return _psnfqueue.queue_fast_open(self, *args)
    def set_queue_maxlen(self, *args): return _psnfqueue.queue_set_queue_maxlen(self, *args)
    def try_run(self): return _psnfqueue.queue_try_run(self)
    def get_fd(self): return _psnfqueue.queue_get_fd(self)
    def set_mode(self, *args): return _psnfqueue.queue_set_mode(self, *args)
    def process_pending(self, arg2=0): return _psnfqueue.queue_process_pending(self, arg2)
    def __init__(self): 
        this = _psnfqueue.new_queue()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _psnfqueue.delete_queue
    __del__ = lambda self : None;
queue_swigregister = _psnfqueue.queue_swigregister
queue_swigregister(queue)

class payload(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, payload, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, payload, name)
    __repr__ = _swig_repr
    __swig_setmethods__["data"] = _psnfqueue.payload_data_set
    __swig_getmethods__["data"] = _psnfqueue.payload_data_get
    if _newclass:data = _swig_property(_psnfqueue.payload_data_get, _psnfqueue.payload_data_set)
    __swig_setmethods__["len"] = _psnfqueue.payload_len_set
    __swig_getmethods__["len"] = _psnfqueue.payload_len_get
    if _newclass:len = _swig_property(_psnfqueue.payload_len_get, _psnfqueue.payload_len_set)
    __swig_setmethods__["id"] = _psnfqueue.payload_id_set
    __swig_getmethods__["id"] = _psnfqueue.payload_id_get
    if _newclass:id = _swig_property(_psnfqueue.payload_id_get, _psnfqueue.payload_id_set)
    __swig_setmethods__["qh"] = _psnfqueue.payload_qh_set
    __swig_getmethods__["qh"] = _psnfqueue.payload_qh_get
    if _newclass:qh = _swig_property(_psnfqueue.payload_qh_get, _psnfqueue.payload_qh_set)
    __swig_setmethods__["nfad"] = _psnfqueue.payload_nfad_set
    __swig_getmethods__["nfad"] = _psnfqueue.payload_nfad_get
    if _newclass:nfad = _swig_property(_psnfqueue.payload_nfad_get, _psnfqueue.payload_nfad_set)
    def get_data(self, *args): return _psnfqueue.payload_get_data(self, *args)
    def get_nfmark(self): return _psnfqueue.payload_get_nfmark(self)
    def get_indev(self): return _psnfqueue.payload_get_indev(self)
    def get_outdev(self): return _psnfqueue.payload_get_outdev(self)
    def get_physindev(self): return _psnfqueue.payload_get_physindev(self)
    def get_physoutdev(self): return _psnfqueue.payload_get_physoutdev(self)
    def get_length(self, *args): return _psnfqueue.payload_get_length(self, *args)
    def set_verdict(self, *args): return _psnfqueue.payload_set_verdict(self, *args)
    def set_verdict_mark(self, *args): return _psnfqueue.payload_set_verdict_mark(self, *args)
    def set_verdict_modified(self, *args): return _psnfqueue.payload_set_verdict_modified(self, *args)
    def set_verdict_mark_modified(self, *args): return _psnfqueue.payload_set_verdict_mark_modified(self, *args)
    def __init__(self): 
        this = _psnfqueue.new_payload()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _psnfqueue.delete_payload
    __del__ = lambda self : None;
payload_swigregister = _psnfqueue.payload_swigregister
payload_swigregister(payload)


def nfq_bindings_version():
  return _psnfqueue.nfq_bindings_version()
nfq_bindings_version = _psnfqueue.nfq_bindings_version
# This file is compatible with both classic and new-style classes.

cvar = _psnfqueue.cvar
NF_DROP = cvar.NF_DROP
NF_ACCEPT = cvar.NF_ACCEPT
NF_STOLEN = cvar.NF_STOLEN
NF_QUEUE = cvar.NF_QUEUE
NF_REPEAT = cvar.NF_REPEAT
NF_STOP = cvar.NF_STOP
NF_MAX_VERDICT = cvar.NF_MAX_VERDICT
NFQNL_COPY_NONE = cvar.NFQNL_COPY_NONE
NFQNL_COPY_META = cvar.NFQNL_COPY_META
NFQNL_COPY_PACKET = cvar.NFQNL_COPY_PACKET

