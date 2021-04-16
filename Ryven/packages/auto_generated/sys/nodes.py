import ryvencore_qt as rc
import sys


class AutoNode_sys___displayhook__(rc.Node):
    title = '__displayhook__'
    type_ = 'sys'
    doc = '''Print an object to sys.stdout and also save it in builtins._'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.__displayhook__(self.input(0)))
        


class AutoNode_sys___excepthook__(rc.Node):
    title = '__excepthook__'
    type_ = 'sys'
    doc = '''Handle an exception by displaying it with a traceback on sys.stderr.'''
    init_inputs = [
        rc.NodeInputBP(label='exctype'),
rc.NodeInputBP(label='value'),
rc.NodeInputBP(label='traceback'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.__excepthook__(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_sys___interactivehook__(rc.Node):
    title = '__interactivehook__'
    type_ = 'sys'
    doc = ''''''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.__interactivehook__())
        


class AutoNode_sys___unraisablehook__(rc.Node):
    title = '__unraisablehook__'
    type_ = 'sys'
    doc = '''Handle an unraisable exception.

The unraisable argument has the following attributes:

* exc_type: Exception type.
* exc_value: Exception value, can be None.
* exc_traceback: Exception traceback, can be None.
* err_msg: Error message, can be None.
* object: Object causing the exception, can be None.'''
    init_inputs = [
        rc.NodeInputBP(label='unraisable'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.__unraisablehook__(self.input(0)))
        


class AutoNode_sys__clear_type_cache(rc.Node):
    title = '_clear_type_cache'
    type_ = 'sys'
    doc = '''Clear the internal type lookup cache.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys._clear_type_cache())
        


class AutoNode_sys__current_frames(rc.Node):
    title = '_current_frames'
    type_ = 'sys'
    doc = '''Return a dict mapping each thread's thread id to its current stack frame.

This function should be used for specialized purposes only.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys._current_frames())
        


class AutoNode_sys__debugmallocstats(rc.Node):
    title = '_debugmallocstats'
    type_ = 'sys'
    doc = '''Print summary info to stderr about the state of pymalloc's structures.

In Py_DEBUG mode, also perform some expensive internal consistency
checks.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys._debugmallocstats())
        


class AutoNode_sys__enablelegacywindowsfsencoding(rc.Node):
    title = '_enablelegacywindowsfsencoding'
    type_ = 'sys'
    doc = '''Changes the default filesystem encoding to mbcs:replace.

This is done for consistency with earlier versions of Python. See PEP
529 for more information.

This is equivalent to defining the PYTHONLEGACYWINDOWSFSENCODING
environment variable before launching Python.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys._enablelegacywindowsfsencoding())
        


class AutoNode_sys__getframe(rc.Node):
    title = '_getframe'
    type_ = 'sys'
    doc = '''Return a frame object from the call stack.

If optional integer depth is given, return the frame object that many
calls below the top of the stack.  If that is deeper than the call
stack, ValueError is raised.  The default for depth is zero, returning
the frame at the top of the call stack.

This function should be used for internal and specialized purposes
only.'''
    init_inputs = [
        rc.NodeInputBP(label='depth'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys._getframe(self.input(0)))
        


class AutoNode_sys_addaudithook(rc.Node):
    title = 'addaudithook'
    type_ = 'sys'
    doc = '''Adds a new audit hook callback.'''
    init_inputs = [
        rc.NodeInputBP(label='hook'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.addaudithook(self.input(0)))
        


class AutoNode_sys_call_tracing(rc.Node):
    title = 'call_tracing'
    type_ = 'sys'
    doc = '''Call func(*args), while tracing is enabled.

The tracing state is saved, and restored afterwards.  This is intended
to be called from a debugger from a checkpoint, to recursively debug
some other code.'''
    init_inputs = [
        rc.NodeInputBP(label='func'),
rc.NodeInputBP(label='args'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.call_tracing(self.input(0), self.input(1)))
        


class AutoNode_sys_callstats(rc.Node):
    title = 'callstats'
    type_ = 'sys'
    doc = '''Return a tuple of function call statistics.

A tuple is returned only if CALL_PROFILE was defined when Python was
built.  Otherwise, this returns None.

When enabled, this function returns detailed, implementation-specific
details about the number of function calls executed. The return value
is a 11-tuple where the entries in the tuple are counts of:
0. all function calls
1. calls to PyFunction_Type objects
2. PyFunction calls that do not create an argument tuple
3. PyFunction calls that do not create an argument tuple
   and bypass PyEval_EvalCodeEx()
4. PyMethod calls
5. PyMethod calls on bound methods
6. PyType calls
7. PyCFunction calls
8. generator calls
9. All other calls
10. Number of stack pops performed by call_function()'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.callstats())
        


class AutoNode_sys_displayhook(rc.Node):
    title = 'displayhook'
    type_ = 'sys'
    doc = '''Print an object to sys.stdout and also save it in builtins._'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.displayhook(self.input(0)))
        


class AutoNode_sys_exc_info(rc.Node):
    title = 'exc_info'
    type_ = 'sys'
    doc = '''Return current exception information: (type, value, traceback).

Return information about the most recent exception caught by an except
clause in the current stack frame or in an older stack frame.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.exc_info())
        


class AutoNode_sys_excepthook(rc.Node):
    title = 'excepthook'
    type_ = 'sys'
    doc = '''Handle an exception by displaying it with a traceback on sys.stderr.'''
    init_inputs = [
        rc.NodeInputBP(label='exctype'),
rc.NodeInputBP(label='value'),
rc.NodeInputBP(label='traceback'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.excepthook(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_sys_exit(rc.Node):
    title = 'exit'
    type_ = 'sys'
    doc = '''Exit the interpreter by raising SystemExit(status).

If the status is omitted or None, it defaults to zero (i.e., success).
If the status is an integer, it will be used as the system exit status.
If it is another kind of object, it will be printed and the system
exit status will be one (i.e., failure).'''
    init_inputs = [
        rc.NodeInputBP(label='status'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.exit(self.input(0)))
        


class AutoNode_sys_get_asyncgen_hooks(rc.Node):
    title = 'get_asyncgen_hooks'
    type_ = 'sys'
    doc = '''Return the installed asynchronous generators hooks.

This returns a namedtuple of the form (firstiter, finalizer).'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.get_asyncgen_hooks())
        


class AutoNode_sys_get_coroutine_origin_tracking_depth(rc.Node):
    title = 'get_coroutine_origin_tracking_depth'
    type_ = 'sys'
    doc = '''Check status of origin tracking for coroutine objects in this thread.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.get_coroutine_origin_tracking_depth())
        


class AutoNode_sys_getallocatedblocks(rc.Node):
    title = 'getallocatedblocks'
    type_ = 'sys'
    doc = '''Return the number of memory blocks currently allocated.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.getallocatedblocks())
        


class AutoNode_sys_getcheckinterval(rc.Node):
    title = 'getcheckinterval'
    type_ = 'sys'
    doc = '''Return the current check interval; see sys.setcheckinterval().'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.getcheckinterval())
        


class AutoNode_sys_getdefaultencoding(rc.Node):
    title = 'getdefaultencoding'
    type_ = 'sys'
    doc = '''Return the current default encoding used by the Unicode implementation.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.getdefaultencoding())
        


class AutoNode_sys_getfilesystemencodeerrors(rc.Node):
    title = 'getfilesystemencodeerrors'
    type_ = 'sys'
    doc = '''Return the error mode used Unicode to OS filename conversion.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.getfilesystemencodeerrors())
        


class AutoNode_sys_getfilesystemencoding(rc.Node):
    title = 'getfilesystemencoding'
    type_ = 'sys'
    doc = '''Return the encoding used to convert Unicode filenames to OS filenames.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.getfilesystemencoding())
        


class AutoNode_sys_getprofile(rc.Node):
    title = 'getprofile'
    type_ = 'sys'
    doc = '''Return the profiling function set with sys.setprofile.

See the profiler chapter in the library manual.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.getprofile())
        


class AutoNode_sys_getrecursionlimit(rc.Node):
    title = 'getrecursionlimit'
    type_ = 'sys'
    doc = '''Return the current value of the recursion limit.

The recursion limit is the maximum depth of the Python interpreter
stack.  This limit prevents infinite recursion from causing an overflow
of the C stack and crashing Python.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.getrecursionlimit())
        


class AutoNode_sys_getrefcount(rc.Node):
    title = 'getrefcount'
    type_ = 'sys'
    doc = '''Return the reference count of object.

The count returned is generally one higher than you might expect,
because it includes the (temporary) reference as an argument to
getrefcount().'''
    init_inputs = [
        rc.NodeInputBP(label='object'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.getrefcount(self.input(0)))
        


class AutoNode_sys_getswitchinterval(rc.Node):
    title = 'getswitchinterval'
    type_ = 'sys'
    doc = '''Return the current thread switch interval; see sys.setswitchinterval().'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.getswitchinterval())
        


class AutoNode_sys_gettrace(rc.Node):
    title = 'gettrace'
    type_ = 'sys'
    doc = '''Return the global debug tracing function set with sys.settrace.

See the debugger chapter in the library manual.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.gettrace())
        


class AutoNode_sys_getwindowsversion(rc.Node):
    title = 'getwindowsversion'
    type_ = 'sys'
    doc = '''Return info about the running version of Windows as a named tuple.

The members are named: major, minor, build, platform, service_pack,
service_pack_major, service_pack_minor, suite_mask, product_type and
platform_version. For backward compatibility, only the first 5 items
are available by indexing. All elements are numbers, except
service_pack and platform_type which are strings, and platform_version
which is a 3-tuple. Platform is always 2. Product_type may be 1 for a
workstation, 2 for a domain controller, 3 for a server.
Platform_version is a 3-tuple containing a version number that is
intended for identifying the OS rather than feature detection.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.getwindowsversion())
        


class AutoNode_sys_intern(rc.Node):
    title = 'intern'
    type_ = 'sys'
    doc = '''``Intern'' the given string.

This enters the string in the (global) table of interned strings whose
purpose is to speed up dictionary lookups. Return the string itself or
the previously interned string object with the same value.'''
    init_inputs = [
        rc.NodeInputBP(label='string'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.intern(self.input(0)))
        


class AutoNode_sys_is_finalizing(rc.Node):
    title = 'is_finalizing'
    type_ = 'sys'
    doc = '''Return True if Python is exiting.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.is_finalizing())
        


class AutoNode_sys_set_coroutine_origin_tracking_depth(rc.Node):
    title = 'set_coroutine_origin_tracking_depth'
    type_ = 'sys'
    doc = '''Enable or disable origin tracking for coroutine objects in this thread.

Coroutine objects will track 'depth' frames of traceback information
about where they came from, available in their cr_origin attribute.

Set a depth of 0 to disable.'''
    init_inputs = [
        rc.NodeInputBP(label='depth'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.set_coroutine_origin_tracking_depth(self.input(0)))
        


class AutoNode_sys_setcheckinterval(rc.Node):
    title = 'setcheckinterval'
    type_ = 'sys'
    doc = '''Set the async event check interval to n instructions.

This tells the Python interpreter to check for asynchronous events
every n instructions.

This also affects how often thread switches occur.'''
    init_inputs = [
        rc.NodeInputBP(label='n'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.setcheckinterval(self.input(0)))
        


class AutoNode_sys_setrecursionlimit(rc.Node):
    title = 'setrecursionlimit'
    type_ = 'sys'
    doc = '''Set the maximum depth of the Python interpreter stack to n.

This limit prevents infinite recursion from causing an overflow of the C
stack and crashing Python.  The highest possible limit is platform-
dependent.'''
    init_inputs = [
        rc.NodeInputBP(label='limit'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.setrecursionlimit(self.input(0)))
        


class AutoNode_sys_setswitchinterval(rc.Node):
    title = 'setswitchinterval'
    type_ = 'sys'
    doc = '''Set the ideal thread switching delay inside the Python interpreter.

The actual frequency of switching threads can be lower if the
interpreter executes long sequences of uninterruptible code
(this is implementation-specific and workload-dependent).

The parameter must represent the desired switching delay in seconds
A typical value is 0.005 (5 milliseconds).'''
    init_inputs = [
        rc.NodeInputBP(label='interval'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.setswitchinterval(self.input(0)))
        


class AutoNode_sys_unraisablehook(rc.Node):
    title = 'unraisablehook'
    type_ = 'sys'
    doc = '''Handle an unraisable exception.

The unraisable argument has the following attributes:

* exc_type: Exception type.
* exc_value: Exception value, can be None.
* exc_traceback: Exception traceback, can be None.
* err_msg: Error message, can be None.
* object: Object causing the exception, can be None.'''
    init_inputs = [
        rc.NodeInputBP(label='unraisable'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, sys.unraisablehook(self.input(0)))
        